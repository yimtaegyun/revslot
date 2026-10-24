import hashlib
import json
from datetime import datetime, timezone


def append_action(state,agent,tool,title,detail,policy="allowed",outcome="completed",slot_id=None):
    previous=state["actions"][-1]["digest"] if state["actions"] else "0"*64
    item={"id":len(state["actions"])+1,"timestamp":datetime.now(timezone.utc).isoformat(),
          "simulated_at":state["clock"],"agent":agent,"tool":tool,"title":title,
          "detail":detail,"policy_status":policy,"outcome":outcome,"previous_hash":previous,
          "slot_id":slot_id or state.get("_active_slot_id")}
    item["digest"]=hashlib.sha256(json.dumps(item,sort_keys=True,separators=(",",":")).encode()).hexdigest()
    state["actions"].append(item)


def verify_actions(actions):
    previous="0"*64
    for a in actions:
        item={k:v for k,v in a.items() if k!="digest"}
        if item["previous_hash"]!=previous: return False
        digest=hashlib.sha256(json.dumps(item,sort_keys=True,separators=(",",":")).encode()).hexdigest()
        if digest!=a["digest"]: return False
        previous=digest
    return True
