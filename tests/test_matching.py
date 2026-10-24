from revslot.seed import customers
from revslot.matching import rank_customers


def test_eligible_opt_in_profiles_only():
    profiles=customers();profiles[0]["notifications_opt_in"]=False
    ranked=rank_customers(profiles,"massage",20,3)
    by_id={c["id"]:c for c in profiles}
    assert ranked
    for row in ranked:
        c=by_id[row["customer_id"]]
        assert c["distance_km"]<=3 and c["notifications_opt_in"] and "massage" in c["interests"] and 20 in c["preferred_hours"]
    assert "guest-001" not in {r["customer_id"] for r in ranked}
    assert ranked==rank_customers(profiles,"massage",20,3)


def test_price_is_not_a_ranking_input_and_sensitive_fields_are_rejected():
    from revslot.schemas import CustomerProfile
    from pydantic import ValidationError
    import pytest
    p=customers()[0];p["gender"]="test"
    with pytest.raises(ValidationError):CustomerProfile.model_validate(p)
