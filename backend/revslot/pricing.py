"""Deterministic, integer-cent pricing. No model-generated number can set a price."""
import json
import math
from functools import lru_cache
from pathlib import Path
from datetime import datetime
from .schemas import PolicyConfig, Slot, PriceCandidate, PricingDecision

DATA = Path(__file__).parent / "data"
DISCOUNTS = (0, .10, .15, .20, .25, .30, .35, .40)
FEATURE_NAMES = ["log_hours", "popularity", "waitlist", "context", "discount", "discount_stage", "stage", "radius"]


def sigmoid(z):
    return 1/(1+math.exp(-max(-35, min(35, z))))


def feature_vector(hours, popularity, waitlist, context, discount, stage, radius):
    return [math.log(max(.000001, hours)), popularity-.5, min(waitlist,30)/15,
            max(-1,min(1,context)), discount, discount*stage, stage, (radius-3)/3]


@lru_cache(maxsize=1)
def model():
    path = DATA / "demand_model.json"
    if not path.exists():
        raise RuntimeError("Run scripts/generate_data.py first; demand coefficients are missing")
    return json.loads(path.read_text())


def predict(hours, popularity, waitlist, context=0, discount=0, stage=0, radius=3):
    m = model()
    x = feature_vector(hours,popularity,waitlist,context,discount,stage,radius)
    z=m["intercept"]+sum(a*b for a,b in zip(m["coefficients"],x))
    return -math.expm1(-math.exp(max(-35,min(35,z))))


def remaining_hours(slot, clock):
    return max(0,(datetime.fromisoformat(slot["start"])-datetime.fromisoformat(clock)).total_seconds()/3600)


def optimize(slot: Slot | dict, policy: PolicyConfig | dict, hours: float,
             stage=0, radius=3, context=0) -> PricingDecision:
    s = Slot.model_validate(slot) if isinstance(slot,dict) else slot
    p = PolicyConfig.model_validate(policy) if isinstance(policy,dict) else policy
    natural = predict(hours,s.popularity,s.waitlist_size,context,0,stage,0)
    confidence = .87 if .5 <= hours <= 12 and 0 <= s.waitlist_size <=30 else .48
    floor = max(p.min_price_cents,s.cost_cents+p.min_margin_cents)
    candidates=[]
    for discount in DISCOUNTS:
        price = (s.original_price_cents*(100-int(round(discount*100)))+50)//100
        reason = None
        if discount>p.max_discount+1e-8: reason="Maximum discount exceeded"
        elif price<floor: reason="Below merchant floor or minimum margin"
        elif hours<=0: reason="Appointment has started"
        elif natural>=.65 and discount>0: reason="Protect likely direct/full-price demand"
        probability=predict(hours,s.popularity,s.waitlist_size,context,discount,stage,radius)
        candidates.append(PriceCandidate(discount=discount,price_cents=price,fill_probability=probability,
            expected_revenue_cents=round(price*probability,3),allowed=reason is None,rejection=reason))
    eligible=[c for c in candidates if c.allowed]
    selected=max(eligible,key=lambda c:(c.expected_revenue_cents,-c.discount)) if eligible else None
    explanation=(f"{selected.discount:.0%} maximizes predicted revenue among {len(eligible)} allowed candidates "
                 f"(${selected.expected_revenue_cents/100:.2f} expected). The effective floor is ${floor/100:.2f}. "
                 "Probabilities are trained on synthetic data, not validated merchant demand.") if selected else "No price satisfies the current floor, margin and time constraints."
    return PricingDecision(selected=selected,candidates=candidates,natural_fill=natural,confidence=confidence,
        explanation=explanation,model_version=model()["version"])


def policy_gate(decision: PricingDecision, policy: PolicyConfig, *, reprice=False, live_failure=False):
    if decision.selected is None: return "blocked", "No valid price candidate"
    if live_failure: return "recommendation", "Live inference failed; merchant review required"
    if decision.confidence<policy.confidence_threshold: return "recommendation", "Outside supported synthetic training range"
    if not policy.autopilot: return "approval", "Autopilot is off"
    if reprice and not policy.allow_auto_reprice: return "approval", "Automatic repricing is disabled"
    if decision.selected.discount>policy.approval_above+1e-8: return "approval", "Discount exceeds approval threshold"
    return "allowed", "Within merchant price, margin, radius and approval policy"
