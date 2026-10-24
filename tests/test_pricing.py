import pytest
from pydantic import ValidationError
from revslot.seed import initial_state
from revslot.pricing import optimize,policy_gate
from revslot.schemas import PolicyConfig


@pytest.mark.parametrize("floor,cap,margin",[(0,.4,0),(5000,.4,800),(7000,.2,800),(10000,.4,800),(5000,0,800),(0,.5,6000)])
def test_money_constraints(floor,cap,margin):
    state=initial_state("test");slot=state["slots"][0]
    policy=PolicyConfig(min_price_cents=floor,max_discount=cap,min_margin_cents=margin)
    quote=optimize(slot,policy,3)
    if quote.selected:
        assert quote.selected.price_cents>=max(floor,slot["cost_cents"]+margin)
        assert quote.selected.discount<=cap
        allowed=[c for c in quote.candidates if c.allowed]
        assert quote.selected.expected_revenue_cents==max(c.expected_revenue_cents for c in allowed)
    else: assert all(not c.allowed for c in quote.candidates)


def test_expected_revenue_and_reproducibility():
    state=initial_state("t");a=optimize(state["slots"][0],state["policy"],3)
    assert a==optimize(state["slots"][0],state["policy"],3)
    for candidate in a.candidates:
        assert candidate.expected_revenue_cents==round(candidate.price_cents*candidate.fill_probability,3)
        assert isinstance(candidate.price_cents,int)


@pytest.mark.parametrize("hours",[0,-1])
def test_expired_inventory_cannot_be_priced(hours):
    s=initial_state("t");assert optimize(s["slots"][0],s["policy"],hours).selected is None


def test_approval_and_low_confidence():
    s=initial_state("t");p=PolicyConfig(approval_above=0)
    q=optimize(s["slots"][0],p,3)
    assert policy_gate(q,p)[0]=="approval"
    q=optimize(s["slots"][0],p,.2)
    assert policy_gate(q,p)[0]=="recommendation"
    assert policy_gate(optimize(s["slots"][0],s["policy"],3),PolicyConfig(),live_failure=True)[0]=="recommendation"


def test_probability_respects_time_and_high_demand_can_keep_full_price():
    from revslot.pricing import predict
    assert predict(.000001,.5,10)<.00001
    s=initial_state("high-demand");slot=s["slots"][0]
    slot["popularity"]=1;slot["waitlist_size"]=30
    quote=optimize(slot,s["policy"],12)
    assert quote.natural_fill>.65
    assert quote.selected.discount==0


@pytest.mark.parametrize("kwargs",[{"max_discount":.9},{"min_price_cents":-1},{"max_radius_km":100},{"confidence_threshold":float('nan')}])
def test_invalid_policy_rejected(kwargs):
    with pytest.raises(ValidationError):PolicyConfig(**kwargs)
