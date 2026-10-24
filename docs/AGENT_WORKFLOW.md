# Responsibilities and tools

| Role | Actual implementation | Observable result |
|---|---|---|
| Orchestrator | LangGraph/structured action allowlist | Event, action, runtime provenance |
| Demand analyst | Forecast + optional public search | Natural-fill estimate and cited sources |
| Pricing strategist | Integer-cent candidate optimizer | Allowed/blocked candidates, expected revenue |
| Matchmaker | Opt-in preference/time/radius filtering | Audience IDs, one shared price |
| Recovery operator | Publish, observe unsold, replan | Quote revision, reach, approval state |
| Outcome analyst | Atomic booking and arithmetic | Gross booked dollars, discount, time, recovery |

Three nodes (`analyze`, `plan`, `execute`) implement these responsibilities without redundant model calls. Validated `publish`, `expand`, `wait`, `recommend` actions control execution. Expansion actually changes reach during reassessment; pricing is recalculated for that chosen reach. Initial broad expansion outside the action policy becomes review-required.

State path: booked → recovering → recovered. Review adds recovering → approval → recovering, bound to an exact revision. Expired inventory cannot be booked. A recovered slot cannot be booked twice. Animations do not advance state.

The preview planner is deterministic and labeled. The live planner must be NVIDIA Nemotron served by Nebius. Benchmarks deliberately exclude LLM calls and compare numerical policies only.

The accelerated clock is a sandbox tool; a browser heartbeat advances it. This version does not monitor forever after browsers close. Outcomes are stored, but automatic retraining/online learning is **not** implemented. New production models require separate data-quality, calibration, causal and out-of-sample checks.
