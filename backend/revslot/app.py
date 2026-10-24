import asyncio
import json
import os
import re
import secrets
import time
from contextlib import asynccontextmanager
from datetime import datetime,timedelta
from pathlib import Path
from fastapi import FastAPI,Request,Response,HTTPException
from fastapi.responses import StreamingResponse
from .schemas import ActionRequest, PolicyConfig, Booking, BookingOutcome
from .seed import initial_state
from .storage import Store,Conflict,Missing
from .pricing import remaining_hours,optimize
from .providers import provider_status
from .audit import append_action,verify_actions
from .agents.orchestrator import recover,get_slot
from .monitoring import advance_clock,has_active,stop_clock,tick_due,monitoring_mode,worker_loop,wake_scheduler

@asynccontextmanager
async def lifespan(application):
    task=asyncio.create_task(worker_loop(lambda:store)) if monitoring_mode()=="worker" else None
    try:
        yield
    finally:
        if task:
            task.cancel()
            await asyncio.gather(task,return_exceptions=True)


app=FastAPI(lifespan=lifespan,title="Revslot Recovery API",version="0.1.0",description="Synthetic sandbox only. No real payments or outbound messages.")
store=Store()
COOKIE="revslot_run"


@app.exception_handler(Conflict)
async def conflict_handler(request,exc):
    from fastapi.responses import JSONResponse
    return JSONResponse({"detail":str(exc)},status_code=409)


@app.exception_handler(Missing)
async def missing_handler(request,exc):
    from fastapi.responses import JSONResponse
    return JSONResponse({"detail":str(exc)},status_code=404)


def run_id(request):
    rid=request.cookies.get(COOKIE,"")
    if not re.fullmatch(r"[0-9a-f]{40}",rid): raise HTTPException(401,"Load a demo scenario first")
    return rid


def check_origin(request):
    origin=request.headers.get("origin")
    if origin and origin.split("://",1)[-1]!=request.headers.get("x-forwarded-host",request.headers.get("host")):
        raise HTTPException(403,"Cross-origin mutation rejected")


def public_state(state):
    state=json.loads(json.dumps(state))
    # IDs/preferences are fictional, but reduce unnecessary client payload regardless.
    state.pop("customers",None)
    state["provider_config"]=provider_status()
    state["durability"]=store.durability
    state.setdefault("clock_control",{"running":False,"next_tick_at":None})
    state["monitoring_mode"]=monitoring_mode()
    cancelled=[s for s in state["slots"] if s["status"]!="booked"]
    recovered=sum(b["price_cents"] for b in state["bookings"])
    potential=sum(s["original_price_cents"] for s in cancelled)
    outcomes=list(state["outcomes"].values())
    state["metrics"]={"at_risk_cents":sum(s["original_price_cents"] for s in cancelled if s["status"] in {"recovering","approval"}),
        "recovered_cents":recovered,"recovery_rate":recovered/potential if potential else 0,
        "recovered_slots":len(outcomes),"average_discount":sum(o["discount_cost_cents"]/o["original_cents"] for o in outcomes)/len(outcomes) if outcomes else 0,
        "average_time_minutes":sum(o["time_to_recovery_minutes"] for o in outcomes)/len(outcomes) if outcomes else 0,
        "agent_actions":len(state["actions"]),"cancelled_potential_cents":potential}
    return state


@app.get("/api/health")
async def health():
    return {"status":"ok","synthetic":True,"providers":provider_status(),"durability":store.durability,
            "monitoring_mode":monitoring_mode(),"submission_ready":False,"note":"Authenticated inference evidence, public video, and final submission remain external gates."}


@app.post("/api/session")
async def session(request:Request,response:Response):
    check_origin(request)
    previous=request.cookies.get(COOKIE,"")
    if re.fullmatch(r"[0-9a-f]{40}",previous):
        for retry in range(3):
            try:
                old=store.load(previous)
                if old.get("clock_control",{}).get("running"):
                    revision=old["revision"]; stop_clock(old); store.save(old,revision)
                break
            except Missing: break
            except Conflict:
                if retry==2: raise
    state=initial_state(secrets.token_hex(20))
    store.create(state)
    response.set_cookie(COOKIE,state["run_id"],httponly=True,secure=request.url.scheme=="https" or request.headers.get("x-forwarded-proto")=="https",samesite="lax",max_age=86400,path="/")
    response.headers["Cache-Control"]="no-store"
    return public_state(state)


@app.get("/api/state")
async def state(request:Request,response:Response):
    response.headers["Cache-Control"]="no-store"
    return public_state(store.load(run_id(request)))


@app.post("/api/action")
async def action(body:ActionRequest,request:Request,response:Response):
    check_origin(request)
    state=store.load(run_id(request)); expected=state["revision"]
    try: slot=get_slot(state,body.slot_id)
    except StopIteration: raise HTTPException(404,"Slot not found")
    if body.action=="cancel":
        event=body.event_id or f"cancel:{slot['id']}"
        if event in state["cancellation_ids"]: return public_state(state)
        if slot["status"]!="booked": raise Conflict("Appointment was already cancelled")
        if remaining_hours(slot,state["clock"])<=0: raise Conflict("Appointment has already started")
        slot["status"]="recovering"; state["cancellation_ids"].append(event)
        append_action(state,"Orchestrator","cancellation.receive","Cancellation detected",f"{slot['id']}: ${slot['original_price_cents']/100:.2f} of expiring inventory.",slot_id=slot["id"])
        state=await recover(state,slot["id"])
    elif body.action=="clock":
        if body.running and monitoring_mode()=="manual":
            raise HTTPException(503,"Automatic clock needs a running backend worker or a configured external scheduler with PostgreSQL")
        if body.running and not has_active(state): raise Conflict("Cancel an appointment before starting the demo clock")
        state["clock_control"]={"running":body.running,"next_tick_at":time.time()+10 if body.running else None}
        append_action(state,"Merchant","clock.control","Server demo clock started" if body.running else "Server demo clock paused",
                      "Server-owned 120x demo clock; continues without an open browser while its backend worker/scheduler runs.")
    elif body.action=="advance":
        state=await advance_clock(state,body.minutes)
        if state.get("clock_control",{}).get("running"):
            state["clock_control"]["next_tick_at"]=time.time()+10
    elif body.action=="approve":
        offer=state["offers"].get(slot["id"])
        if not offer or offer["revision"]!=body.offer_revision: raise Conflict("Offer changed; review the latest revision")
        if slot["status"]!="approval" or remaining_hours(slot,state["clock"])<=0: raise Conflict("No current approvable offer")
        floor=max(state["policy"]["min_price_cents"],slot["cost_cents"]+state["policy"]["min_margin_cents"])
        if offer["price_cents"]<floor or offer["discount"]>state["policy"]["max_discount"]+1e-8: raise Conflict("Offer no longer satisfies policy")
        offer["published"]=True; slot["status"]="recovering"
        append_action(state,"Merchant","approval.confirm","Merchant approved offer",f"Explicit approval of revision {offer['revision']} at ${offer['price_cents']/100:.2f}.",slot_id=slot["id"])
        attempt=next(a for a in reversed(state["attempts"]) if a["slot_id"]==slot["id"])
        eligible={c["id"] for c in state["customers"] if c["notifications_opt_in"]}
        notifications=state.setdefault("notifications",[])
        existing={(n["customer_id"],n["slot_id"],n["offer_revision"]) for n in notifications}
        for cid in attempt["audience_ids"]:
            if cid in eligible and (cid,slot["id"],offer["revision"]) not in existing:
                notifications.append({"customer_id":cid,"slot_id":slot["id"],"offer_revision":offer["revision"],"price_cents":offer["price_cents"],"channel":"sandbox_inbox"})
    elif body.action=="book":
        offer=state["offers"].get(slot["id"])
        if not offer or offer["revision"]!=body.offer_revision: raise Conflict("This price changed. Refresh and confirm the new price.")
        if slot["status"]!="recovering" or not offer["published"] or remaining_hours(slot,state["clock"])<=0:
            raise Conflict("Slot is no longer available")
        floor=max(state["policy"]["min_price_cents"],slot["cost_cents"]+state["policy"]["min_margin_cents"])
        if offer["price_cents"]<floor or offer["discount"]>state["policy"]["max_discount"]+1e-8: raise Conflict("Policy changed; offer withdrawn")
        slot["status"]="recovered"; offer["published"]=False
        booking=Booking(id=secrets.token_hex(8),slot_id=slot["id"],customer_id=body.customer_id,
                        price_cents=offer["price_cents"],offer_revision=offer["revision"],simulated_at=state["clock"])
        state["bookings"].append(booking.model_dump())
        first=next(a for a in state["actions"] if a["tool"]=="cancellation.receive" and a["slot_id"]==slot["id"])
        minutes=round((datetime.fromisoformat(state["clock"])-datetime.fromisoformat(first["simulated_at"])).total_seconds()/60)
        state["outcomes"][slot["id"]]=BookingOutcome(original_cents=slot["original_price_cents"],recovered_cents=offer["price_cents"],
            discount_cost_cents=slot["original_price_cents"]-offer["price_cents"],recovery_rate=offer["price_cents"]/slot["original_price_cents"],time_to_recovery_minutes=minutes).model_dump()
        append_action(state,"Outcome analyst","booking.commit","Revenue recovered",f"Sandbox booking confirmed at ${offer['price_cents']/100:.2f}; {minutes} simulated minutes to fill. This is booked gross revenue, not proven incremental lift.",slot_id=slot["id"])
    elif body.action=="policy":
        state["policy"]=body.policy.model_dump()
        append_action(state,"Merchant","policy.update","Guardrails updated","Merchant policy changed. Existing offers are revalidated before further booking.")
        for current in state["slots"]:
            if current["status"] in {"recovering","approval"}:
                state=await recover(state,current["id"],sum(a["slot_id"]==current["id"] for a in state["attempts"]))
    elif body.action=="optout":
        for customer in state["customers"]:
            if customer["id"]==body.customer_id: customer["notifications_opt_in"]=False
        append_action(state,"Consumer","notifications.optout","Notification preference saved","This synthetic profile is excluded from future direct notifications.")
    if not has_active(state): stop_clock(state)
    store.save(state,expected)
    if body.action=="clock" and body.running and monitoring_mode()=="external_scheduler":
        try:
            await wake_scheduler()
        except Exception:
            # A rejected/unknown wake must not leave a misleading running clock.
            for retry in range(3):
                state=store.load(state["run_id"])
                if not state.get("clock_control",{}).get("running"): break
                revision=state["revision"];stop_clock(state)
                append_action(state,"Recovery operator","clock.wake_failed","Server clock paused","Scheduler wake failed. Persisted clock paused; retry when the service is available.")
                try:
                    store.save(state,revision)
                    break
                except Conflict:
                    if retry==2: raise
            raise HTTPException(503,"Scheduler could not start. The demo clock is paused; please retry.")
    response.headers["Cache-Control"]="no-store"
    return public_state(state)


@app.get("/api/audit")
async def audit(request:Request):
    state=store.load(run_id(request))
    return {"synthetic":True,"actions":state["actions"],"hash_chain_valid":verify_actions(state["actions"]),
            "note":"Hash chain detects accidental modification; it is not an externally notarized audit."}


@app.get("/api/evaluation")
async def evaluation():
    path=Path(__file__).parent/"data"/"evaluation.json"
    if not path.exists(): raise HTTPException(503,"Run simulation/evaluate.py")
    return json.loads(path.read_text())


@app.get("/api/events")
async def events(request:Request):
    rid=run_id(request)
    async def stream():
        revision=-1
        for _ in range(20):
            if await request.is_disconnected(): break
            try: state=store.load(rid)
            except Missing: break
            if state["revision"]!=revision:
                revision=state["revision"]
                yield f"event: state\ndata: {json.dumps(public_state(state))}\n\n"
            else: yield ": heartbeat\n\n"
            await asyncio.sleep(1)
    return StreamingResponse(stream(),media_type="text/event-stream",headers={"Cache-Control":"no-store","X-Accel-Buffering":"no"})


@app.get("/api/jobs/tick")
async def scheduled_tick(request:Request):
    secret=os.getenv("CRON_SECRET","")
    if not secret: raise HTTPException(503,"External scheduler is not configured")
    if not secrets.compare_digest(request.headers.get("authorization",""),"Bearer "+secret):
        raise HTTPException(401,"Scheduler authorization required")
    if os.getenv("VERCEL") and store.durability!="postgres":
        raise HTTPException(503,"Serverless scheduling requires durable PostgreSQL")
    result=await tick_due(store)
    return {**result,"active_jobs":store.scheduled_count()}
