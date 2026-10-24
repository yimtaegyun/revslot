"""Write factual runtime evidence without logging credentials or provider reasoning."""
import asyncio
import json
import sys
from datetime import datetime,timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/"backend"))
from revslot.seed import initial_state
from revslot.pricing import optimize
from revslot.providers import plan_strategy,demand_context,provider_status


async def main():
    s=initial_state("connectivity-check")
    quote=optimize(s["slots"][0],s["policy"],3).model_dump()
    plan,context=await asyncio.gather(plan_strategy({"stage":0,"slot":s["slots"][0],"remaining_minutes":180,
        "pricing_tool_result":quote,"policy":s["policy"],"external_context":{"sources":[],"signal":0},
        "allowed_tools":["publish_shared_offer","wait_for_response","request_merchant_approval"]}),demand_context("2026-10-30"))
    report={"checked_at_utc":datetime.now(timezone.utc).isoformat(),"synthetic_connectivity_payload":True,
      "configured":provider_status(),"nebius":{k:v for k,v in plan.items() if k!="plan"},
      "tavily":{"verified":context["status"]=="live","status":context["status"],"source_count":len(context["sources"])},
      "core_runtime_gate_passed":plan["verified"],"no_credentials_or_reasoning_stored":True}
    (ROOT/"docs/RUNTIME_EVIDENCE.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))
    return 0 if plan["verified"] else 2


if __name__=="__main__":raise SystemExit(asyncio.run(main()))
