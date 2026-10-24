import asyncio
import copy
import os
import secrets
import time
from concurrent.futures import ThreadPoolExecutor
import pytest
import revslot.app as module
from revslot import monitoring
from revslot.audit import append_action,verify_actions
from revslot.seed import initial_state
from revslot.storage import Store,Conflict
from revslot.agents.orchestrator import recover
from test_workflow import post


def running(client):
    post(client,action="cancel")
    return post(client,action="clock",running=True)


async def test_clock_persists_across_store_restart_and_reprices(client):
    s=running(client)
    restarted=Store(module.store.path)
    result=await monitoring.tick_due(restarted,s["clock_control"]["next_tick_at"]+.1)
    recovered=restarted.load(s["run_id"])
    assert result["processed"]==1 and recovered["elapsed_minutes"]==20
    assert recovered["offers"]["slot-1"]["price_cents"]==5600
    assert recovered["offers"]["slot-1"]["radius_km"]==6
    assert verify_actions(recovered["actions"])


def test_two_workers_only_one_claim_and_expired_lease_is_fenced(client):
    s=running(client);now=s["clock_control"]["next_tick_at"]+.1
    with ThreadPoolExecutor(2) as pool:
        claims=list(pool.map(lambda _:module.store.claim_due(now),range(2)))
    assert sum(len(x) for x in claims)==1
    rid,old_token=next(x[0] for x in claims if x)
    rid,new_token=module.store.claim_due(now+61)[0]
    stale=module.store.load(rid)
    with pytest.raises(Conflict):module.store.save(stale,stale["revision"],lease_token=old_token)
    module.store.release_job(rid,old_token,remove=True)
    assert module.store.claim_due(now+62)==[]
    module.store.release_job(rid,new_token)
    assert len(module.store.claim_due(now+62))==1


async def test_pause_and_booking_stop_all_future_ticks(client):
    s=running(client)
    paused=post(client,action="clock",running=False)
    assert await monitoring.tick_due(module.store,time.time()+200)=={"processed":0,"conflicts":0,"failed":0}
    s=post(client,action="clock",running=True)
    finished=post(client,action="book",offer_revision=s["offers"]["slot-1"]["revision"])
    assert not finished["clock_control"]["running"]
    assert module.store.claim_due(time.time()+200)==[]


async def test_restart_catches_up_to_expiry_without_browser(client):
    s=running(client)
    result=await monitoring.tick_due(Store(module.store.path),s["clock_control"]["next_tick_at"]+180)
    final=module.store.load(s["run_id"])
    assert result["processed"]<=3
    assert final["elapsed_minutes"]==180 and final["slots"][0]["status"]=="expired"
    assert not final["offers"]["slot-1"]["published"] and not final["clock_control"]["running"]


def test_reset_stops_the_previous_sessions_clock(client):
    old=running(client)
    assert client.post("/api/session").status_code==200
    assert not module.store.load(old["run_id"])["clock_control"]["running"]
    assert module.store.claim_due(time.time()+200)==[]


async def test_failed_tick_rolls_back_and_remains_retryable(client,monkeypatch):
    s=running(client);real=monitoring.advance_clock
    async def failed(*a,**kw):raise RuntimeError("demo failure")
    monkeypatch.setattr(monitoring,"advance_clock",failed)
    now=s["clock_control"]["next_tick_at"]+.1
    assert (await monitoring.tick_due(module.store,now))["failed"]==1
    assert module.store.load(s["run_id"])["elapsed_minutes"]==0
    monkeypatch.setattr(monitoring,"advance_clock",real)
    assert (await monitoring.tick_due(module.store,now))["processed"]==1
    assert module.store.load(s["run_id"])["elapsed_minutes"]==20


def test_scheduler_requires_secret_and_durable_serverless_storage(client,monkeypatch):
    monkeypatch.delenv("CRON_SECRET",raising=False)
    assert client.get("/api/jobs/tick").status_code==503
    monkeypatch.setenv("CRON_SECRET","ci-only-scheduler-secret")
    assert client.get("/api/jobs/tick").status_code==401
    assert client.get("/api/jobs/tick",headers={"Authorization":"Bearer wrong"}).status_code==401
    auth={"Authorization":"Bearer ci-only-scheduler-secret"}
    assert client.get("/api/jobs/tick",headers=auth).status_code==200
    monkeypatch.setenv("VERCEL","1")
    assert client.get("/api/jobs/tick",headers=auth).status_code==503
    post(client,action="cancel")
    assert client.post("/api/action",json={"action":"clock","running":True}).status_code==503
    assert client.get("/api/state").json()["monitoring_mode"]=="manual"


@pytest.mark.skipif(not os.getenv("TEST_DATABASE_URL"),reason="CI PostgreSQL service required")
async def test_real_postgres_clock_restart_claims_and_atomic_updates(monkeypatch):
    monkeypatch.setenv("DATABASE_URL",os.environ["TEST_DATABASE_URL"])
    monkeypatch.delenv("NEBIUS_API_KEY",raising=False)
    monkeypatch.delenv("TAVILY_API_KEY",raising=False)
    db=Store();rid=secrets.token_hex(20)
    s=initial_state(rid);s["slots"][0]["status"]="recovering"
    append_action(s,"Orchestrator","cancellation.receive","Cancellation detected","Synthetic PostgreSQL integration scenario",slot_id="slot-1")
    s=await recover(s,"slot-1")
    db.create(s)
    now=time.time();s["clock_control"]={"running":True,"next_tick_at":now-.1}
    db.save(s,0)
    try:
        with ThreadPoolExecutor(2) as pool:
            claims=list(pool.map(lambda _:Store().claim_due(now),range(2)))
        assert sum(len(x) for x in claims)==1
        job=next(x[0] for x in claims if x);db.release_job(*job)
        assert (await monitoring.tick_due(Store(),now))["processed"]==1
        a=Store().load(rid);b=copy.deepcopy(a)
        assert a["elapsed_minutes"]==20 and a["offers"]["slot-1"]["price_cents"]==5600
        db.save(a,a["revision"])
        with pytest.raises(Conflict):Store().save(b,b["revision"])
        assert verify_actions(a["actions"])
    finally:
        with db.connection() as c:
            c.execute(db.sql("DELETE FROM clock_jobs WHERE run_id=?"),(rid,))
            c.execute(db.sql("DELETE FROM runs WHERE id=?"),(rid,))
