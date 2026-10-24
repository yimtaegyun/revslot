import json
import pytest
import httpx
from revslot import providers


@pytest.mark.asyncio
async def test_real_adapter_catalog_and_content_only(monkeypatch):
    monkeypatch.setenv("NEBIUS_API_KEY","unit-test-placeholder")
    monkeypatch.delenv("NEBIUS_MODEL",raising=False)
    providers._model_cache=None
    calls=[]
    def handler(request):
        calls.append(str(request.url))
        if request.url.path.endswith("models"):
            return httpx.Response(200,json={"data":[{"id":"other/model"},{"id":"nvidia/unit-nemotron-nano"}]})
        return httpx.Response(200,json={"choices":[{"message":{"reasoning_content":"PRIVATE_REASONING_MUST_NOT_ESCAPE","content":json.dumps({"action":"publish","headline":"A little time for yourself","summary":"Use the verified pricing tool result.","context_delta":0})}}],"usage":{"total_tokens":40}})
    original=httpx.AsyncClient
    monkeypatch.setattr(providers.httpx,"AsyncClient",lambda **kw:original(transport=httpx.MockTransport(handler),**kw))
    result=await providers.plan_strategy({"stage":0})
    assert result["verified"] and result["model"]=="nvidia/unit-nemotron-nano"
    assert len(calls)==2 and "PRIVATE_REASONING" not in json.dumps(result)


@pytest.mark.asyncio
async def test_invalid_tool_action_fails_closed(monkeypatch):
    monkeypatch.setenv("NEBIUS_API_KEY","unit-test-placeholder")
    monkeypatch.delenv("NEBIUS_MODEL",raising=False);providers._model_cache=None
    def handler(request):
        if request.url.path.endswith("models"):return httpx.Response(200,json={"data":[{"id":"nvidia/test-nemotron"}]})
        return httpx.Response(200,json={"choices":[{"message":{"content":'{"action":"override_floor","price":1}'}}]})
    original=httpx.AsyncClient;monkeypatch.setattr(providers.httpx,"AsyncClient",lambda **kw:original(transport=httpx.MockTransport(handler),**kw))
    result=await providers.plan_strategy({"stage":0})
    assert result["mode"]=="inference_failed" and result["plan"]["action"]=="recommend" and not result["verified"]


@pytest.mark.asyncio
async def test_tavily_failure_is_optional(monkeypatch):
    monkeypatch.setenv("TAVILY_API_KEY","unit-test-placeholder")
    original=httpx.AsyncClient
    monkeypatch.setattr(providers.httpx,"AsyncClient",lambda **kw:original(transport=httpx.MockTransport(lambda r:httpx.Response(503)),**kw))
    result=await providers.demand_context("2026-10-30")
    assert result["status"]=="unavailable" and result["signal"]==0


@pytest.mark.parametrize("headline",["Only one left","Best rated studio","Save 50 dollars"])
def test_ungrounded_offer_headline_replaced(headline):
    plan=providers.parse_plan(json.dumps({"action":"publish","headline":headline,"summary":"Use the verified public price.","context_delta":0}))
    assert plan.headline=="A little time for yourself"
