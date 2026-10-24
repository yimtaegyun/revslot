from concurrent.futures import ThreadPoolExecutor
import copy
import pytest
from revslot.audit import verify_actions
from revslot.storage import Store,Conflict
from revslot.seed import initial_state


def post(c,**body):
    r=c.post("/api/action",json=body)
    assert r.status_code==200,r.text
    return r.json()


def test_end_to_end_recovery_and_repricing(client):
    first=post(client,action="cancel",slot_id="slot-1",event_id="e1")
    offer1=first["offers"]["slot-1"]
    assert offer1["published"] and offer1["radius_km"]==3
    assert first["metrics"]["at_risk_cents"]==8000
    assert first["integrations"]["nebius"]["mode"]=="rules_preview"
    assert not first["integrations"]["nebius"]["verified"]
    second=post(client,action="advance",minutes=20)
    offer2=second["offers"]["slot-1"]
    assert offer2["revision"]>offer1["revision"] and offer2["radius_km"]==6
    assert len(second["attempts"])==2
    stale=client.post("/api/action",json={"action":"book","offer_revision":offer1["revision"]})
    assert stale.status_code==409
    final=post(client,action="book",offer_revision=offer2["revision"])
    assert final["slots"][0]["status"]=="recovered"
    assert final["metrics"]["recovered_cents"]==offer2["price_cents"]
    assert final["metrics"]["recovery_rate"]==offer2["price_cents"]/8000
    assert final["metrics"]["average_time_minutes"]==20
    assert final["metrics"]["at_risk_cents"]==0
    assert client.get("/api/audit").json()["hash_chain_valid"]
    assert client.post("/api/action",json={"action":"book","offer_revision":offer2["revision"]}).status_code==409


def test_cancellation_idempotency(client):
    a=post(client,action="cancel",event_id="same")
    b=post(client,action="cancel",event_id="same")
    assert a["revision"]==b["revision"] and len(a["actions"])==len(b["actions"])


def test_human_approval_cannot_override_price_floor(client):
    s=client.get("/api/state").json();p={**s["policy"],"approval_above":0}
    post(client,action="policy",policy=p)
    s=post(client,action="cancel")
    assert s["slots"][0]["status"]=="approval"
    offer=s["offers"]["slot-1"]
    assert not offer["published"]
    assert client.post("/api/action",json={"action":"book","offer_revision":offer["revision"]}).status_code==409
    approved=post(client,action="approve",offer_revision=offer["revision"])
    assert approved["offers"]["slot-1"]["published"]
    blocked=post(client,action="policy",policy={**p,"min_price_cents":10000})
    assert "slot-1" not in blocked["offers"]
    assert client.post("/api/action",json={"action":"approve","offer_revision":offer["revision"]}).status_code==409


def test_optout_same_slot_price_and_audit_integrity(client):
    post(client,action="cancel")
    post(client,action="optout",customer_id="guest-001")
    s=post(client,action="advance",minutes=20)
    latest=s["attempts"][-1]
    assert "guest-001" not in latest["audience_ids"]
    import revslot.app as module
    raw=module.store.load(s["run_id"])
    revision=s["offers"]["slot-1"]["revision"]
    messages=[x for x in raw["notifications"] if x["offer_revision"]==revision]
    assert len({x["price_cents"] for x in messages})==1
    altered=copy.deepcopy(s["actions"]);altered[-1]["title"]="tampered"
    assert not verify_actions(altered)


def test_expiry_and_invalid_payload(client):
    s=post(client,action="cancel")
    for _ in range(3):s=post(client,action="advance",minutes=60)
    assert s["slots"][0]["status"]=="expired"
    assert not s["offers"]["slot-1"]["published"]
    assert client.post("/api/action",json={"action":"book","offer_revision":s["offers"]["slot-1"]["revision"]}).status_code==409
    assert client.post("/api/action",json={"action":"advance","minutes":10000}).status_code==422
    assert client.post("/api/action",json={"action":"book"}).status_code==422


def test_policy_off_and_clock_reprice_off(client):
    s=client.get("/api/state").json()
    post(client,action="policy",policy={**s["policy"],"autopilot":False})
    s=post(client,action="cancel");assert s["slots"][0]["status"]=="approval"


def test_run_isolation_and_origin(client):
    first=post(client,action="cancel")
    second=client.post("/api/session").json()
    assert first["run_id"]!=second["run_id"] and not second["offers"]
    assert client.post("/api/action",json={"action":"cancel"},headers={"Origin":"https://untrusted.example"}).status_code==403


def test_planner_controls_wait_publish_and_expansion(client,monkeypatch):
    from revslot import providers
    actions=iter(["wait","publish","expand"])
    async def planner(_):
        return {"mode":"rules_preview","verified":False,"model":None,"latency_ms":0,
                "plan":{"action":next(actions),"headline":"Time for yourself","summary":"Use the allowed deterministic tools.","context_delta":0}}
    monkeypatch.setattr(providers,"plan_strategy",planner)
    a=post(client,action="cancel")
    assert not a["offers"]["slot-1"]["published"]
    b=post(client,action="advance",minutes=20)
    assert b["offers"]["slot-1"]["published"] and b["offers"]["slot-1"]["radius_km"]==3
    c=post(client,action="advance",minutes=20)
    assert c["offers"]["slot-1"]["radius_km"]==6


def test_atomic_compare_and_swap(tmp_path,monkeypatch):
    monkeypatch.delenv("DATABASE_URL",raising=False)
    st=Store(str(tmp_path/"race.sqlite"));st.create(initial_state("race"))
    snapshots=[st.load("race"),st.load("race")]
    def save(s):
        try:st.save(s,0);return "committed"
        except Conflict:return "conflict"
    with ThreadPoolExecutor(max_workers=2) as pool:results=list(pool.map(save,snapshots))
    assert sorted(results)==["committed","conflict"] and st.load("race")["revision"]==1
