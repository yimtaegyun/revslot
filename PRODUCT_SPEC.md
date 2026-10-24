# Revslot — product specification

An autonomous revenue recovery agent for perishable service inventory.

## Scope and evidence

Beauty and wellness only. Three fictional merchants, five or more services, opt-in synthetic customer profiles. No medical appointments, real payments, real SMS, real reviews, or claims of commercial revenue. Dataset, simulated clock, and sandbox booking are visibly labeled.

ClassPass already provides demand-based inventory protection and price optimization. The demonstrable wedge is a cancellation-specific merchant workflow with a visible closed loop, shared slot prices, deterministic policy/approval gates, and an auditable outcome. Do not claim invention of yield management.

## User story

A merchant cancels a $80 20:00 massage at 17:00. The recovery graph evaluates natural fill, computes allowed expected-revenue candidates, selects a plan, ranks opt-in customers, publishes one shared offer, monitors time, and reprices/expands reach if unsold. A consumer confirms a sandbox reservation. Merchant KPIs and audit records update from that reservation, not a scripted success label.

## Acceptance criteria

- Load/reset the seeded scenario without affecting another visitor's run.
- Cancellation idempotency prevents duplicate recoveries.
- Every price is computed in integer cents; price >= maximum of merchant floor and cost-plus-minimum margin; discount <= cap.
- High natural demand can retain full price.
- A single price and offer revision are shared by every customer for a slot.
- Customer ranking only uses permitted preferences, distance, reliability and engagement. Opt-out excludes direct notification, not ordinary browsing.
- Approval threshold, autopilot off, low confidence, and disabled repricing prevent unauthorized actions on the server.
- Approval binds to an exact price/revision and expires if inputs change.
- Booking uses an atomic available-to-recovered transition; concurrent buyers cannot double book. Stale offer revisions return a conflict and refresh.
- Simulated time advances explicitly; wall-clock runtime and simulated timestamps remain distinguishable. No fake scarcity.
- Every action emits a short input/output/policy record, never hidden model reasoning.
- Nebius is called server-side using a runtime-discovered NVIDIA model. Validated structured output selects only allowlisted actions; pricing remains deterministic.
- Missing/failed Nebius yields labeled rule-based preview or recommendation-only mode, never a claim of live AI.
- Tavily uses public event context with citations, an explicitly bounded effect and safe degradation.
- Comparison uses >=100 held-out synthetic scenarios, common random numbers, fixed seed, four baselines, uncertainty and sensitivity analysis. No winner is preselected.

## Screens

Merchant overview (KPIs/calendar/recovery inspector), consumer flash-slot feed and confirmation, analytics with baseline table, policy settings, integration health and audit export. Every visible button has an implemented behavior, loading/error/empty state, keyboard label and responsive layout.

## Architecture

Requested canonical stack: Next.js/TypeScript/Tailwind frontend; FastAPI/Pydantic/LangGraph backend; SQLite locally; persistent database needed for multi-instance production. Vercel Services deployment is an option (Beta), with a free account check and no plan upgrades. Container deployment remains reproducible. The Sites workflow supplies local preview/QA when useful; no replacement of the user's requested public hosting without documenting the reason.

## Model boundary

Six meaningful graph stages, not six independent chatbots: interpret/plan, context/demand, optimize, policy/match, publish/monitor, outcome. LLM plans and explains within a schema. Deterministic code handles prices, eligibility, transactions, counters and policy. External text is untrusted data, never instructions.

## Milestones / freeze

Research first; API/CLI flow; web flow; full loop + evaluation; polish/deploy; submission. Feature freeze after the full loop; no architecture redesign to chase prizes. Runtime keys, account verification and legal acceptance are the only planned human blockers.
