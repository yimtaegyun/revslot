import json
from datetime import datetime
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from .. import providers
from ..schemas import PolicyConfig, PricingDecision, Offer
from ..pricing import optimize, remaining_hours, policy_gate
from ..matching import rank_customers
from ..audit import append_action


class RecoveryGraph(TypedDict, total=False):
    state: dict
    slot_id: str
    stage: int
    context: dict
    quote: dict
    inference: dict


def get_slot(state,slot_id):
    return next(s for s in state["slots"] if s["id"]==slot_id)


async def analyze(g: RecoveryGraph):
    state=g["state"]; slot=get_slot(state,g["slot_id"])
    date=slot["start"][:10]
    context=state["contexts"].get(date)
    if context is None:
        context=await providers.demand_context(date)
        state["contexts"][date]=context
    append_action(state,"Demand analyst","tavily.search","Demand context checked",context["note"],outcome=context["status"])
    stage=g["stage"]
    radius=min(6 if stage else 3,state["policy"]["max_radius_km"])
    quote=optimize(slot,state["policy"],remaining_hours(slot,state["clock"]),min(stage,1),radius,0)
    append_action(state,"Demand analyst","demand.predict",f"Natural fill: {quote.natural_fill:.0%}",
                  "Estimated full-price fill without recovery exposure. Synthetic time-to-arrival forecast; not calibrated on real merchants.")
    append_action(state,"Pricing strategist","pricing.optimize",f"{len(quote.candidates)} prices evaluated",quote.explanation)
    return {"state":state,"quote":quote.model_dump(),"context":context}


async def plan(g: RecoveryGraph):
    state=g["state"]; slot=get_slot(state,g["slot_id"])
    quote=g["quote"]
    inference=await providers.plan_strategy({"stage":g["stage"],"slot":slot,
        "remaining_minutes":round(remaining_hours(slot,state["clock"])*60),
        "pricing_tool_result":quote,"policy":state["policy"],"external_context":g["context"],
        "allowed_tools":["publish_shared_offer","expand_opt_in_audience","wait_for_response","request_merchant_approval"]})
    state["integrations"]["nebius"]= {k:v for k,v in inference.items() if k!="plan"}
    state["integrations"]["tavily"]={"verified":g["context"]["status"]=="live","status":g["context"]["status"]}
    # Only explicitly date-grounded source text can contribute this tiny external feature.
    date=slot["start"][:10]
    grounded=any(date in x["snippet"] for x in g["context"]["sources"])
    delta=inference["plan"]["context_delta"] if grounded else 0
    selected_action=inference["plan"]["action"]
    if selected_action=="expand" and not g["stage"]:
        inference["plan"]["action"]="recommend"
        inference["plan"]["summary"]="Initial broad-audience expansion is outside this workflow's action policy. Merchant review required."
        selected_action="recommend"
    radius=min(6 if selected_action=="expand" and g["stage"] else 3,state["policy"]["max_radius_km"])
    quote=optimize(slot,state["policy"],remaining_hours(slot,state["clock"]),min(g["stage"],1),radius,delta).model_dump()
    if quote!=g["quote"]:
        append_action(state,"Pricing strategist","pricing.revalidate","Price refreshed for chosen plan",
                      f"Selected reach {radius:g} km; external feature {delta:.3f}. "+quote["explanation"])
    label="NVIDIA plan validated" if inference["verified"] else "Rule-based preview" if inference["mode"]=="rules_preview" else "Inference unavailable"
    append_action(state,"Orchestrator","nebius.plan",label,inference["plan"]["summary"],outcome=inference["mode"])
    return {"state":state,"inference":inference,"quote":quote}


async def execute(g: RecoveryGraph):
    state=g["state"]; slot=get_slot(state,g["slot_id"])
    quote=PricingDecision.model_validate(g["quote"])
    state["decisions"][slot["id"]]=quote.model_dump()
    policy=PolicyConfig.model_validate(state["policy"])
    stage=g["stage"]; inference=g["inference"]
    status,reason=policy_gate(quote,policy,reprice=stage>0,live_failure=inference["mode"]=="inference_failed")
    plan_action=inference["plan"]["action"]
    if plan_action=="recommend" and status=="allowed": status,reason="recommendation","Planner requested merchant review"
    if plan_action=="wait" and status=="allowed": status,reason="waiting","Planner chose to observe without publishing a new offer"
    append_action(state,"Policy guard","policy.validate","Merchant policy checked",reason,policy=status)
    service=next(s for s in state["services"] if s["id"]==slot["service_id"])
    radius=min(6 if plan_action=="expand" and stage else 3,policy.max_radius_km)
    try:
        ranked=rank_customers(state["customers"],service["category"],datetime.fromisoformat(slot["start"]).hour,radius,24 if stage else 12)
    except (ValueError,TypeError):
        ranked=[]
        append_action(state,"Matchmaker","matching.fallback","Public listing fallback","Customer matching failed; no direct notifications will be sent.",outcome="degraded")
    audience=[r["customer_id"] for r in ranked]
    append_action(state,"Matchmaker","customers.rank",f"{len(ranked)} opt-in customers matched",f"Within {radius:g} km; matching category and time preferences. Priority varies; the slot price does not.")
    previous=state["offers"].get(slot["id"])
    revision=(previous["revision"] if previous else 0)+1
    selected=quote.selected
    if selected:
        minutes=max(0,round(remaining_hours(slot,state["clock"])*60))
        message=f"{service['duration']}-minute {service['name'].lower()} · ${selected.price_cents/100:.2f} · {selected.discount:.0%} off · starts in {minutes} demo minutes."
        published=status=="allowed"
        offer=Offer(slot_id=slot["id"],revision=revision,price_cents=selected.price_cents,discount=selected.discount,
            headline=inference["plan"]["headline"],message=message,audience_count=len(audience),radius_km=radius,
            channel="Marketplace + sandbox inbox" if stage else "Marketplace + priority inbox",published=published).model_dump()
        state["offers"][slot["id"]]=offer
        slot["status"]="recovering" if status in {"allowed","waiting"} else "approval"
        if published:
            notifications=state.setdefault("notifications",[])
            notifications.extend({"customer_id":c,"slot_id":slot["id"],"offer_revision":revision,
                                  "price_cents":offer["price_cents"],"channel":"sandbox_inbox"} for c in audience)
            append_action(state,"Recovery operator","offers.publish", "Strategy updated" if stage else "Recovery offer published",
                f"${offer['price_cents']/100:.2f} shared price; {radius:g} km reach. {len(audience)} sandbox inbox records created. No real messages sent.")
        else:
            append_action(state,"Recovery operator","approval.request","Observing demand" if status=="waiting" else "Merchant review required",reason,policy=status,outcome="pending")
    else:
        state["offers"].pop(slot["id"],None)
        slot["status"]="approval"
    state["attempts"].append({"slot_id":slot["id"],"attempt":stage+1,"decision":quote.model_dump(),"audience_ids":audience,
                               "plan_action":plan_action,"provider":inference["mode"]})
    state["last_evaluated"][slot["id"]]=state["elapsed_minutes"]
    return {"state":state}


builder=StateGraph(RecoveryGraph)
builder.add_node("analyze",analyze)
builder.add_node("plan",plan)
builder.add_node("execute",execute)
builder.add_edge(START,"analyze")
builder.add_edge("analyze","plan")
builder.add_edge("plan","execute")
builder.add_edge("execute",END)
graph=builder.compile()


async def recover(state,slot_id,stage=0):
    state["_active_slot_id"]=slot_id
    result=await graph.ainvoke({"state":state,"slot_id":slot_id,"stage":stage})
    result["state"].pop("_active_slot_id",None)
    return result["state"]
