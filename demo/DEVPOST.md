# Revslot — submission text draft, pending live gates

Public preview: https://revslot-one.vercel.app/ . Source: https://github.com/yimtaegyun/revslot . Current public mode is a labeled rules preview with Neon PostgreSQL and a verified hosted scheduler; this draft is not submitted.

**Tagline:** An autonomous revenue recovery agent for cancelled beauty and wellness appointments.

## Inspiration

For a salon or wellness studio, an empty hour cannot sit in a warehouse until tomorrow. A cancellation turns a booked appointment into inventory with an expiration time. We wanted to give the merchant more than another notification: a visible recovery process that can act, observe and revise its plan.

## What it does

Revslot follows a cancelled appointment through demand evaluation, permitted pricing, customer matching, an offer, an unsold observation, a revised strategy and a confirmed sandbox reservation. The merchant sees the actual tool trace, controls the limits and can approve a specific offer. Consumers see nearby openings at one shared slot price.

The seeded demonstration starts with an $80 massage. It publishes $64, then after 20 simulated unsold minutes selects $56 and expands reach. The consumer’s confirmation updates the calendar and records 70% of original value as booked gross recovery. The businesses, profiles, demand and money are synthetic and clearly labeled.

## How we built it

Next.js/TypeScript/Tailwind provides merchant, consumer, analytics and policy screens. FastAPI/Pydantic handles schema-validated actions. A three-node LangGraph coordinates demand, planning and execution; pricing, customer eligibility, constraints and booking arithmetic remain deterministic Python. SQLite revision transactions work locally. The Vercel app uses Neon PostgreSQL; a completed reservation survived redeployment. The server wakes a small authenticated Neon function, which calls the existing Python monitoring tick at ten-second target intervals. It exits on an empty queue; a native 15-minute schedule retries interruptions. An API-only session autonomously repriced without browser-driven clock actions.

The implemented live planner adapter discovers available NVIDIA Nemotron models through Nebius Token Factory, requests structured actions and accepts only publish, expand, wait or recommend. Public context retrieval uses optional Tavily search with cited sources and a bounded feature. Provider failure cannot authorize an unsafe price. A no-key run is explicitly a rules preview.

## Why existing tools are not the whole experiment

We found meaningful existing waitlists, marketplaces, demand prediction and dynamic pricing, especially ClassPass SmartTools. We do not claim those ideas are new. Our focus is merchant accountability for one cancellation: price, audience, channel, policy, observation, revised action and outcome in one inspectable record.

## Safety and measurement

The same slot has the same price for every customer. Profiles contain no real PII or sensitive attributes. Floors, margin, caps, opt-out, exact-revision approval and atomic booking are enforced outside the language model. The interface exposes concise actions rather than private reasoning.

Our evaluation compares no recovery, waitlist only, fixed 20% and the numerical recovery policy on 1,000 independent-seed synthetic scenarios using common random numbers. The report includes fill, gross revenue, margin, discount, time, unnecessary discount, paired intervals and elasticity sensitivity. It does not measure LLM business value. The policy’s unnecessary-discount result remains weak and is reported openly. A real merchant pilot and causal demand validation are next, not claimed achievements.

## Challenges and learning

An early model retained nonzero fill probability as time reached zero; repeated interval evaluation was therefore incoherent. We retained that diagnostic result and replaced the model with a time-to-arrival formulation. We also separated provider reasoning from public action summaries, bound approval to quote revisions and made concurrent state changes fail rather than silently overwrite each other.

The strongest lesson was that filling more slots is not the same as protecting revenue or margin. A simulation can also favor its own assumptions. We report the assumptions and unfavorable metrics alongside the positive results.

## What’s next

Verify live NVIDIA-on-Nebius runtime and final submission delivery; recruit an opt-in beauty/wellness pilot; integrate actual calendars; estimate merchant-specific causal demand and cannibalization. Fitness/PT and other perishable service inventory are later directions. Medical appointments remain excluded.

## Built with

Next.js, TypeScript, React, Tailwind CSS, shadcn/ui, Lucide, Python, FastAPI, Pydantic, LangGraph, HTTPX, SQLite, Neon PostgreSQL, Neon Functions, Function Triggers, Vercel, SciPy, scikit-learn, Playwright. Nebius Token Factory, NVIDIA Nemotron and Tavily are implemented integration targets whose actual verification status must be checked in `docs/RUNTIME_EVIDENCE.json` before the final form is submitted.

## Final-form gates

Public demo access and hosted persistence/scheduling are verified; public YouTube remains unverified. Replace this draft’s conditional runtime language only after genuine successful calls; add observed provider feedback. Do not submit the rules-preview build as a completed eligible entry. No legal terms have been accepted by this session.
