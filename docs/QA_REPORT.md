# Verification status

Verified locally on 2026-10-24:

- **34 pytest tests passed**, including price/margin/cap constraints, probability/time behavior, high-demand full price, opt-in matching, strict schemas, cancellation idempotency, full recovery, actual repricing/reach, same-slot pricing, human approval, stale/double booking, expiry, origin/session isolation, atomic competing writes, audit modification detection, provider parser failures and total inference timeout.
- Next.js production build and TypeScript passed again after dependency/source cleanup (Next.js 16.3.4).
- Dataset generator and independent-seed simulation executed; data card/checksum and unfavorable metrics retained.
- Connectivity checker executed and correctly returned blocked (exit 2): no Nebius/Tavily key configured. Unit mocked calls are not runtime evidence.

The first GitHub CI run passed Python tests, install and production build, but all three browser cases failed before application initialization. Actual logs showed Next development-resource requests blocked for the loopback host, preventing hydration. The development origin allowlist is now explicitly limited to localhost/127.0.0.1; browser tests use the production build. A Strict Mode initialization race, client fetch timeout and explicit SQL connection cleanup were also repaired. **Browser tests are not marked passed until the repaired run finishes.** Managed preview itself cannot launch Python/uvicorn; CI provides the full-stack verification environment. No fabricated screen is claimed.

Docker and PostgreSQL have not been executed/connected. Vercel project creation succeeded, but account-scope access denied storage linking; no successful live deployment is recorded. Video/public YouTube/Devpost remain open gates.

Regression after subsequent changes must update this report and PROJECT_STATE.md. Check CI artifacts for actual merchant, offer, repricing, marketplace, recovery, analytics, guardrail and mobile screenshots.
