"""Seeded randomized-treatment synthetic data; model fitting happens only on earlier dates."""
import csv
import gzip
import hashlib
import json
import math
import random
import sys
from datetime import datetime,timedelta,timezone
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from sklearn.metrics import brier_score_loss,log_loss,roc_auc_score

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"backend"))
from revslot.seed import SERVICES,SEED
from revslot.pricing import feature_vector,FEATURE_NAMES,sigmoid


def truth(hours,popularity,waitlist,context,discount,stage,radius,latent=0,elasticity=1):
    x=feature_vector(hours,popularity,waitlist,context,discount,stage,radius)
    coefs=[1,1.4,.3,.18,16*elasticity,-6*elasticity,-.25,.28]
    z=-2.95+sum(a*b for a,b in zip(x,coefs))+latent
    return -math.expm1(-math.exp(max(-35,min(35,z))))


def generate(n=12000):
    rng=random.Random(SEED); rows=[]; base=datetime(2026,4,30,8,tzinfo=timezone.utc)
    for i in range(n):
        service=SERVICES[i%len(SERVICES)]
        appointment=base+timedelta(days=i*180/n,hours=rng.choice([0,2,4,6,8,10]))
        hours=round(rng.uniform(.5,12),3); popularity=rng.uniform(.05,.98)
        waitlist=rng.randint(0,25); discount=rng.choice([0,.1,.15,.2,.25,.3,.35,.4]);stage=rng.choice([0,1]);radius=rng.choice([3,6])
        context=rng.uniform(-1,1);cancelled=rng.random()<.42
        probability=truth(hours,popularity,waitlist,context,discount,stage,radius,rng.gauss(0,.45))
        filled=int(rng.random()<probability) if cancelled else 0
        rows.append({"synthetic":True,"booking_time":(appointment-timedelta(days=rng.randint(1,20))).isoformat(),
          "appointment_time":appointment.isoformat(),"merchant_id":service.merchant_id,"service":service.category,"service_id":service.id,
          "price":service.price_cents/100,"staff":service.merchant_id.replace("m","t"),"cancelled":cancelled,
          "cancellation_lead_time":hours,"waitlist_size":waitlist,"slot_popularity":round(popularity,4),
          "day_of_week":appointment.weekday(),"hour":appointment.hour,"discount":discount if cancelled else 0,"offer_sent":int(cancelled),"previous_offer_sent":int(stage) if cancelled else 0,
          "customer_segment":rng.choice(["flexible","category_interested","evening_preference"]),"booked_after_cancel":filled,
          "time_to_rebook":round(rng.uniform(5,hours*60),2) if filled else "",
          "synthetic_context_signal":round(context,4),"audience_radius_km":radius})
    return sorted(rows,key=lambda r:r["appointment_time"])


def main():
    rows=generate(); data=ROOT/"data";data.mkdir(exist_ok=True)
    # gzip header mtime fixed for byte-reproducible archives.
    import io
    buf=io.StringIO(newline="");writer=csv.DictWriter(buf,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    with open(data/"synthetic_bookings.csv.gz","wb") as f:
        with gzip.GzipFile(fileobj=f,mode="wb",mtime=0) as z:z.write(buf.getvalue().encode())
    cancelled=[r for r in rows if r["cancelled"]]
    x=np.array([feature_vector(r["cancellation_lead_time"],r["slot_popularity"],r["waitlist_size"],r["synthetic_context_signal"],r["discount"],r["previous_offer_sent"],r["audience_radius_km"]) for r in cancelled])
    y=np.array([r["booked_after_cancel"] for r in cancelled]);cut=int(.7*len(x));val=int(.85*len(x))
    # Complementary-log-log Bernoulli likelihood with a log(time) offset.
    # This makes probability approach zero with zero available time and gives
    # coherent per-interval hazards. The offset coefficient is fixed at one.
    design=np.column_stack([np.ones(cut),x[:cut,1:]])
    def objective(beta):
        z=np.clip(design@beta+x[:cut,0],-25,25);hazard=np.exp(z)
        logp=np.log(np.maximum(-np.expm1(-hazard),1e-15))
        loss=-np.mean(y[:cut]*logp-(1-y[:cut])*hazard)+.0001*np.sum(beta[1:]**2)
        dlog=y[:cut]*hazard/np.expm1(np.minimum(hazard,50))-(1-y[:cut])*hazard
        grad=-(design.T@dlog)/cut
        grad[1:]+=.0002*beta[1:]
        return loss,grad
    fitted=minimize(objective,np.array([-2.,1.,.2,.1,10.,-3.,-.1,.1]),jac=True,method="L-BFGS-B",options={"maxiter":1500,"ftol":1e-12})
    if not fitted.success:raise RuntimeError(f"Hazard fit failed: {fitted.message}")
    coefficients=[1.0,*fitted.x[1:].tolist()]
    predicted=-np.expm1(-np.exp(np.clip(fitted.x[0]+x[val:]@np.array(coefficients),-25,25)))
    bins=[]
    for lo in np.arange(0,1,.2):
        mask=(predicted>=lo)&(predicted<lo+.2)
        if mask.any():bins.append({"lower":round(float(lo),2),"n":int(mask.sum()),"predicted":round(float(predicted[mask].mean()),4),"observed":round(float(y[val:][mask].mean()),4)})
    report={"synthetic":True,"seed":SEED,"booking_events":len(rows),"cancelled_events":len(cancelled),"merchants":3,"services":6,"days":180,
      "split":"chronological 70% train / 15% validation reserved / 15% untouched test by appointment date",
      "training_rows":cut,"validation_rows":val-cut,"test_rows":len(x)-val,
      "test_brier":round(float(brier_score_loss(y[val:],predicted)),4),"test_log_loss":round(float(log_loss(y[val:],predicted)),4),
      "test_auc":round(float(roc_auc_score(y[val:],predicted)),4),"baseline_brier":round(float(brier_score_loss(y[val:],np.full(len(predicted),float(y[:cut].mean())))),4),
      "calibration_bins":bins,"source_sha256":hashlib.sha256((data/"synthetic_bookings.csv.gz").read_bytes()).hexdigest(),
      "limitations":["Synthetic randomized treatments do not establish real customer price elasticity.","Cancellations are intentionally oversampled at 42%; this is not an industry cancellation-rate estimate.","No production validation or causal uplift claim.","Shared simulation family can favor an optimizer; evaluate misspecified elasticity separately.","Validation partition is reserved, not used to tune hyperparameters in this version."]}
    out=ROOT/"backend/revslot/data";out.mkdir(exist_ok=True)
    (out/"demand_model.json").write_text(json.dumps({"version":"synthetic-hazard-v2","link":"complementary_log_log","intercept":float(fitted.x[0]),"coefficients":coefficients,"features":FEATURE_NAMES,"synthetic":True,"training_seed":SEED},indent=2)+"\n")
    (data/"DATA_CARD.json").write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(report,indent=2))


if __name__=="__main__":main()
