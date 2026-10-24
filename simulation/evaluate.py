"""Common-random-number comparison. No strategy's result is hard-coded to win."""
import json
import math
import random
import sys
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1];sys.path[:0]=[str(ROOT/"backend"),str(ROOT/"scripts")]
from revslot.pricing import optimize,policy_gate
from revslot.schemas import PolicyConfig
from revslot.seed import SEED
from generate_data import truth

STRATEGIES=["No recovery","Waitlist only","Fixed 20%","Revslot agent"]


def scenarios(n=1000,seed=20261030):
    rng=random.Random(seed);out=[]
    for i in range(n):
        out.append({"hours":rng.uniform(.5,8),"popularity":rng.uniform(.1,.95),"waitlist":rng.randint(0,25),
                    "price":rng.choice([5500,6500,7000,8000,9000,9500]),"context":rng.uniform(-1,1),
                    "latent":rng.gauss(0,.6),"uniforms":[rng.random() for _ in range(12)]})
    return out


def rollout(s,strategy,elasticity=1):
    slot={"id":"evaluation","service_id":"s1","merchant_id":"m1","staff_id":"t1","start":"2026-10-30T20:00:00-04:00",
          "original_price_cents":s["price"],"cost_cents":round(s["price"]*.4),"duration":60,"popularity":s["popularity"],"waitlist_size":s["waitlist"]}
    policy=PolicyConfig(min_price_cents=round(s["price"]*.6),min_margin_cents=round(s["price"]*.1))
    had_discount=False
    for step,u in enumerate(s["uniforms"]):
        hours=s["hours"]*(1-step/12);stage=int(step>=2)
        if strategy=="No recovery":d=0;radius=0
        elif strategy=="Waitlist only":d=0;radius=1.5
        elif strategy=="Fixed 20%":d=.2;radius=3
        else:
            radius=3 if not stage else 6
            quote=optimize(slot,policy,hours,stage,radius,0)
            status,_=policy_gate(quote,policy,reprice=stage>0)
            if status=="allowed":d=quote.selected.discount
            else:d=0;radius=0  # no assumed human approval; only natural/direct demand remains
        had_discount|=d>0
        p=truth(hours,s["popularity"],s["waitlist"],s["context"],d,stage,radius,s["latent"],elasticity)
        # Forecast is a remaining-horizon probability; convert to a one-step hazard.
        q=1-(1-p)**(1/(12-step))
        if u<q:
            price=round(s["price"]*(1-d))
            return {"filled":1,"revenue":price/100,"discount":d,"time":(step+.5)*s["hours"]*60/12,
                    "margin":(price-slot["cost_cents"])/100,"discounted":int(had_discount)}
    return {"filled":0,"revenue":0,"discount":0,"time":None,"margin":0,"discounted":int(had_discount)}


def evaluate(n=1000,seed=20261030):
    samples=scenarios(n,seed); raw={name:[rollout(s,name) for s in samples] for name in STRATEGIES}
    naturally=[r["filled"] for r in raw["No recovery"]];summary=[]
    for name,rows in raw.items():
        filled=[r for r in rows if r["filled"]]
        summary.append({"strategy":name,"fill_rate":round(len(filled)/n,4),"recovered_revenue":round(sum(r["revenue"] for r in rows),2),
            "revenue_per_cancelled_slot":round(sum(r["revenue"] for r in rows)/n,2),
            "average_discount":round(float(np.mean([r["discount"] for r in filled])) if filled else 0,4),
            "average_time_minutes":round(float(np.mean([r["time"] for r in filled])) if filled else 0,2),
            "margin_preservation":round(sum(r["margin"] for r in rows)/sum(s["price"]*.6/100 for s in samples),4),
            "unnecessary_discount_rate":round(sum(r["discounted"]*natural for r,natural in zip(rows,naturally))/max(1,sum(naturally)),4)})
    rng=np.random.default_rng(SEED)
    paired=np.array([a["revenue"]-b["revenue"] for a,b in zip(raw["Revslot agent"],raw["Fixed 20%    ".strip()])])
    boot=np.array([rng.choice(paired,n,replace=True).mean() for _ in range(1000)])
    sensitivity=[]
    for elasticity in [.5,1,1.5]:
        sensitivity.append({"true_elasticity_multiplier":elasticity,**{name:round(sum(rollout(s,name,elasticity)["revenue"] for s in samples)/n,2) for name in STRATEGIES}})
    return {"synthetic":True,"seed":seed,"scenarios":n,"evaluation_stage":"post-policy-freeze independent-seed synthetic test; not externally preregistered","strategies":summary,
      "paired_revenue_delta_vs_fixed20":{"mean":round(float(paired.mean()),2),"bootstrap95":[round(float(np.quantile(boot,.025)),2),round(float(np.quantile(boot,.975)),2)]},
      "elasticity_sensitivity":sensitivity,"data_card":json.loads((ROOT/"data/DATA_CARD.json").read_text()),
      "policy":{"max_discount":.4,"floor_fraction_of_original":.6,"minimum_margin_fraction":.1,"approval_above":.35,"confidence_threshold":.65,"human_approval_simulated":False},
      "definitions":{"revenue":"Booked gross dollars, including natural/direct fills; not profit or causal incremental revenue.","margin_preservation":"Recovered gross margin / full original gross margin of all cancelled slots.",
       "unnecessary_discount_rate":"Among slots that fill under no recovery using the same latent random draws, fraction exposed to any discount by this policy.",
       "time":"Conditional on successful fill, simulated minutes from cancellation.","confidence_interval":"Paired bootstrap over synthetic scenarios; excludes real-market/model uncertainty."},
      "limitations":["Not real merchants, customers, demand, or recovered money.","Outcome generator and forecast share a functional family; latent noise and elasticity sensitivity reduce but do not remove circularity.","All strategies use the same scenarios, time steps, latent demand and random draws.","Channel expansion is part of the agent policy, so the comparison does not isolate LLM reasoning or price effects.","The radius feature is an assumed exposure proxy, not measured advertising reach or a causal channel effect.","No LLM participates in these numerical simulations; they evaluate the deterministic recovery policy.","Approval-required or low-confidence agent actions are not executed; no instantaneous human approval is assumed."]}


if __name__=="__main__":
    report=evaluate()
    for path in [ROOT/"backend/revslot/data/evaluation.json",ROOT/"simulation/results.json"]:
        path.parent.mkdir(exist_ok=True,parents=True);path.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({k:v for k,v in report.items() if k not in {"data_card","definitions"}},indent=2))
