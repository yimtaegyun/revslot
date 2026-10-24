import asyncio
import pytest
from revslot import providers


@pytest.mark.asyncio
async def test_total_inference_budget_fails_closed(monkeypatch):
    async def slow(_):
        await asyncio.sleep(.05)
    monkeypatch.setattr(providers,"_plan_strategy",slow)
    monkeypatch.setattr(providers,"PLAN_BUDGET_SECONDS",.01)
    result=await providers.plan_strategy({"stage":0})
    assert result["mode"]=="inference_failed" and result["plan"]["action"]=="recommend"
