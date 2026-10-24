from typing import Literal
from pydantic import BaseModel, Field, ConfigDict, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", allow_inf_nan=False)


class PolicyConfig(StrictModel):
    autopilot: bool = True
    min_price_cents: int = Field(5000, ge=0, le=100000)
    max_discount: float = Field(0.40, ge=0, le=0.50)
    min_margin_cents: int = Field(800, ge=0, le=100000)
    max_radius_km: float = Field(6, ge=1, le=15)
    allow_auto_reprice: bool = True
    approval_above: float = Field(0.35, ge=0, le=0.50)
    confidence_threshold: float = Field(0.65, ge=0.5, le=0.99)


class Merchant(StrictModel):
    id: str
    name: str
    category: str
    area: str
    accent: str


class Service(StrictModel):
    id: str
    merchant_id: str
    name: str
    category: str
    duration: int = Field(ge=15, le=180)
    price_cents: int = Field(gt=0)
    cost_cents: int = Field(ge=0)


class Staff(StrictModel):
    id: str
    display_name: str
    merchant_id: str


class Booking(StrictModel):
    id: str
    slot_id: str
    customer_id: str
    price_cents: int
    offer_revision: int
    simulated_at: str
    sandbox: bool = True


class Slot(StrictModel):
    id: str
    service_id: str
    merchant_id: str
    staff_id: str
    start: str
    original_price_cents: int
    cost_cents: int
    duration: int
    popularity: float = Field(ge=0, le=1)
    waitlist_size: int = Field(ge=0)
    status: Literal["booked", "recovering", "approval", "recovered", "expired"] = "booked"


class CancellationEvent(StrictModel):
    event_id: str
    slot_id: str
    simulated_at: str


class CustomerProfile(StrictModel):
    id: str
    distance_km: float = Field(ge=0, le=30)
    interests: list[str]
    preferred_hours: list[int]
    price_sensitivity: Literal["low", "medium", "high"]
    reliability: float = Field(ge=0, le=1)
    engagement: float = Field(ge=0, le=1)
    notifications_opt_in: bool


class Offer(StrictModel):
    slot_id: str
    revision: int
    price_cents: int
    discount: float
    headline: str
    message: str
    audience_count: int
    radius_km: float
    channel: str
    published: bool


class PriceCandidate(StrictModel):
    discount: float
    price_cents: int
    fill_probability: float
    expected_revenue_cents: float
    allowed: bool
    rejection: str | None = None


class PricingDecision(StrictModel):
    selected: PriceCandidate | None
    candidates: list[PriceCandidate]
    natural_fill: float
    confidence: float
    explanation: str
    model_version: str


class AgentAction(StrictModel):
    id: int
    slot_id: str | None = None
    timestamp: str
    simulated_at: str
    agent: str
    tool: str
    title: str
    detail: str
    policy_status: str
    outcome: str
    previous_hash: str
    digest: str


class RecoveryAttempt(StrictModel):
    slot_id: str
    attempt: int
    decision: PricingDecision
    audience_ids: list[str]
    plan_action: str
    provider: str


class BookingOutcome(StrictModel):
    original_cents: int
    recovered_cents: int
    discount_cost_cents: int
    recovery_rate: float
    time_to_recovery_minutes: int
    incremental_revenue_proven: bool = False


class AgentPlan(StrictModel):
    action: Literal["publish", "expand", "wait", "recommend"]
    headline: str = Field(min_length=3, max_length=90)
    summary: str = Field(min_length=5, max_length=300)
    context_delta: float = Field(0, ge=-0.03, le=0.03)


class ActionRequest(StrictModel):
    action: Literal["cancel", "advance", "approve", "book", "policy", "optout", "clock"]
    slot_id: str = "slot-1"
    event_id: str | None = Field(None, max_length=80)
    minutes: int = Field(20, ge=1, le=60)
    offer_revision: int | None = Field(None, ge=0)
    customer_id: str = Field("demo-guest", max_length=40)
    policy: PolicyConfig | None = None
    running: bool | None = None

    @model_validator(mode="after")
    def validate_action(self):
        if self.action in {"approve", "book"} and self.offer_revision is None:
            raise ValueError("Current offer_revision is required")
        if self.action == "policy" and self.policy is None:
            raise ValueError("Policy is required")
        if self.action == "clock" and self.running is None:
            raise ValueError("Clock running state is required")
        return self
