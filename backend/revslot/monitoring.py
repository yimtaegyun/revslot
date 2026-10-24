"""Persisted demo clock: standalone worker or an explicitly configured scheduler.

Serverless instances must not pretend to host a permanent background daemon.
"""
import asyncio
import logging
import math
import os
import time
from urllib.parse import urlsplit
import httpx
from datetime import datetime,timedelta
from .agents.orchestrator import recover
from .audit import append_action
from .pricing import remaining_hours
from .storage import Conflict,Missing

LOG=logging.getLogger(__name__)
TICK_SECONDS=10
DEMO_MINUTES=20


def monitoring_mode():
    if not os.getenv("VERCEL") and os.getenv("REVSlot_WORKER","1")=="1": return "worker"
    if os.getenv("REVSlot_EXTERNAL_TICK")=="1" and os.getenv("DATABASE_URL") and os.getenv("CRON_SECRET"):
        return "external_scheduler"
    return "manual"


async def wake_scheduler():
    """Bounded authenticated wake-up; SQL, not an isolate, owns the job."""
    target=os.getenv("REVSlot_SCHEDULER_WAKE_URL","")
    url=urlsplit(target)
    if (url.scheme!="https" or not (url.hostname or "").endswith(".aws.neon.tech")
        or url.path!="/wake" or url.username or url.password or url.query or url.fragment):
        raise RuntimeError("Scheduler wake URL is not configured")
    async def call():
        async with httpx.AsyncClient(timeout=4,follow_redirects=False) as client:
            response=await client.post(target,headers={"Authorization":"Bearer "+os.getenv("CRON_SECRET","")})
            if response.status_code!=202: raise RuntimeError("Scheduler wake was rejected")
    await asyncio.wait_for(call(),timeout=4.5)


def has_active(state):
    return any(s["status"] in {"recovering","approval"} for s in state["slots"])


def stop_clock(state):
    state["clock_control"]={"running":False,"next_tick_at":None}


async def advance_clock(state,minutes,*,source="manual"):
    state["clock"]=(datetime.fromisoformat(state["clock"])+timedelta(minutes=minutes)).isoformat()
    state["elapsed_minutes"]+=minutes
    for current in state["slots"]:
        if current["status"] not in {"recovering","approval"}: continue
        if remaining_hours(current,state["clock"])<=0:
            current["status"]="expired"
            if current["id"] in state["offers"]: state["offers"][current["id"]]["published"]=False
            append_action(state,"Recovery operator","clock.expire","Slot expired","The appointment start has passed. Booking and offers are closed.",slot_id=current["id"])
        elif state["elapsed_minutes"]-state["last_evaluated"].get(current["id"],0)>=20:
            append_action(state,"Recovery operator","monitor.check","No booking — reassessing",f"{minutes} simulated minutes advanced by {source}; observing an actual unsold sandbox slot.",slot_id=current["id"])
            stage=sum(a["slot_id"]==current["id"] for a in state["attempts"])
            state=await recover(state,current["id"],stage)
    if not has_active(state): stop_clock(state)
    return state


async def tick_due(store,now=None):
    """Bounded, leased work; state and next due time commit together with CAS."""
    now=time.time() if now is None else now
    result={"processed":0,"conflicts":0,"failed":0}
    # Claim one at a time so time spent on another inference cannot consume its lease.
    for _ in range(3):
        jobs=store.claim_due(now,limit=1)
        if not jobs: break
        rid,token=jobs[0];remove=False
        try:
            state=store.load(rid); expected=state["revision"]
            control=state.get("clock_control",{})
            if not control.get("running"):
                remove=True
                continue
            due=control["next_tick_at"]
            if due>now: continue
            if not has_active(state):
                stop_clock(state)
            else:
                ticks=min(3,max(1,math.floor((now-due)/TICK_SECONDS)+1))
                state=await advance_clock(state,ticks*DEMO_MINUTES,source="server worker")
                if state["clock_control"]["running"]:
                    state["clock_control"]["next_tick_at"]=due+ticks*TICK_SECONDS
            store.save(state,expected,lease_token=token)
            result["processed"]+=1
        except Missing:
            remove=True
        except Conflict:
            result["conflicts"]+=1
        except Exception:
            # No provider text/secrets in logs; persisted job remains retryable.
            LOG.error("Recovery clock tick failed; job retained")
            result["failed"]+=1
        finally:
            store.release_job(rid,token,remove=remove)
        if result["failed"] or result["conflicts"]: break
    return result


async def worker_loop(store_factory):
    while True:
        try:
            await tick_due(store_factory())
        except Exception:
            LOG.error("Recovery worker unavailable; retrying after one second")
        await asyncio.sleep(1)
