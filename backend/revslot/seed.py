import random
from .schemas import Merchant, Service, Staff, Slot, CustomerProfile, PolicyConfig

SEED = 20261024
MERCHANTS = [
    Merchant(id="m1", name="Still Wellness", category="Massage & recovery", area="Brooklyn, NY", accent="sage"),
    Merchant(id="m2", name="Forma Studio", category="Pilates & movement", area="Brooklyn, NY", accent="clay"),
    Merchant(id="m3", name="Sunday Salon", category="Hair & nails", area="Brooklyn, NY", accent="sand"),
]
SERVICES = [
    Service(id="s1", merchant_id="m1", name="Deep tissue massage", category="massage", duration=60, price_cents=8000, cost_cents=3200),
    Service(id="s2", merchant_id="m1", name="Restorative massage", category="massage", duration=45, price_cents=6500, cost_cents=2400),
    Service(id="s3", merchant_id="m2", name="Private reformer", category="pilates", duration=50, price_cents=9500, cost_cents=3800),
    Service(id="s4", merchant_id="m2", name="Personal training", category="fitness", duration=60, price_cents=9000, cost_cents=3500),
    Service(id="s5", merchant_id="m3", name="Signature haircut", category="hair", duration=45, price_cents=7000, cost_cents=2800),
    Service(id="s6", merchant_id="m3", name="Gel manicure", category="nails", duration=60, price_cents=5500, cost_cents=1900),
]
STAFF = [Staff(id="t1", display_name="Practitioner 01", merchant_id="m1"), Staff(id="t2", display_name="Instructor 02", merchant_id="m2"), Staff(id="t3", display_name="Stylist 03", merchant_id="m3")]


def customers():
    rng = random.Random(SEED)
    profiles = []
    for i in range(84):
        profiles.append(CustomerProfile(
            id=f"guest-{i+1:03}",
            distance_km=round(1.1+i*0.12, 2) if i < 14 else round(rng.uniform(0.5, 8), 2),
            interests=["massage"] if i < 14 else rng.sample(["massage", "pilates", "hair", "nails", "fitness"], 2),
            preferred_hours=[18, 19, 20, 21] if i < 14 else rng.sample([16, 17, 18, 19, 20, 21], 3),
            price_sensitivity=rng.choice(["low", "medium", "high"]),
            reliability=round(rng.uniform(.65, 1), 3), engagement=round(rng.uniform(.3, .95), 3),
            notifications_opt_in=True if i < 14 else rng.random()>.15,
        ).model_dump())
    return profiles


def initial_state(run_id):
    return {
        "run_id": run_id, "revision": 0, "synthetic": True,
        "clock": "2026-10-30T17:00:00-04:00", "elapsed_minutes": 0,
        "clock_control": {"running":False,"next_tick_at":None},
        "policy": PolicyConfig().model_dump(),
        "merchants": [m.model_dump() for m in MERCHANTS],
        "services": [s.model_dump() for s in SERVICES],
        "staff": [s.model_dump() for s in STAFF],
        "slots": [Slot(id=f"slot-{i+1}", service_id=s.id, merchant_id=s.merchant_id,
                       staff_id=f"t{int(s.merchant_id[1])}",
                       start=f"2026-10-30T{20 if i==0 else 18+(i%3):02}:00:00-04:00",
                       original_price_cents=s.price_cents, cost_cents=s.cost_cents,
                       duration=s.duration, popularity=.52 if i==0 else .5+.07*(i%4),
                       waitlist_size=12 if i==0 else 4+i).model_dump()
                  for i,s in enumerate(SERVICES)],
        "customers": customers(), "offers": {}, "decisions": {}, "attempts": [],
        "bookings": [], "outcomes": {}, "actions": [], "cancellation_ids": [],
        "contexts": {}, "last_evaluated": {}, "integrations": {},
    }
