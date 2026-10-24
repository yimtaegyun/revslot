# Verification status

Latest verified code: [CI 40089803664](https://github.com/yimtaegyun/revslot/actions/runs/40089803664) passed **42 Python tests, real PostgreSQL 17, production build/TypeScript and 4 Chromium cases**, including server repricing with every browser page closed. Earlier evidence below is retained with its original capture provenance.

Verified locally on 2026-10-24:

- **34 pytest tests passed**, including price/margin/cap constraints, probability/time behavior, high-demand full price, opt-in matching, strict schemas, cancellation idempotency, full recovery, actual repricing/reach, same-slot pricing, human approval, stale/double booking, expiry, origin/session isolation, atomic competing writes, audit modification detection, provider parser failures and total inference timeout.
- Next.js production build and TypeScript passed again after dependency/source cleanup (Next.js 16.3.4).
- Dataset generator and independent-seed simulation executed; data card/checksum and unfavorable metrics retained.
- Connectivity checker executed and correctly returned blocked (exit 2): no Nebius/Tavily key configured. Unit mocked calls are not runtime evidence.

**Full-stack browser verification passed:** [CI run 40064620041](https://github.com/yimtaegyun/revslot/actions/runs/40064620041), commit `574de1d52a5bc8d185a20df08e9ca7e45833e88e`. Python: 34 passed in 0.67 seconds. Production build/TypeScript: passed. Chromium: 3 passed in 11.7 seconds, covering cancellation → $64 offer → +20 demo minutes → $56 reprice/expanded audience → sandbox reservation → merchant metrics, human approval, and mobile navigation/no horizontal overflow. Nine real screenshots and the 7.64-second raw workflow recording are in [demo](../demo/README.md); checksums and log excerpts are in [QA_EVIDENCE.json](QA_EVIDENCE.json). The main agent inspected every captured view, including final provenance. Text readability and an inactive skip-link capture defect were corrected before the passing run.

The first GitHub CI run failed before hydration because development-resource requests were blocked for the loopback host. Tests now exercise the production build; development origins are limited to localhost/127.0.0.1. A Strict Mode initialization race, client fetch timeout and explicit SQL connection cleanup were repaired. A subsequent run passed all tests but failed a cache-save cleanup; that invalid cache configuration was removed. Both final runs succeeded. Managed preview itself cannot launch Python/uvicorn; CI is the verified full-stack environment.

The 1920×1080, 170-second captioned review film uses actual inspected captures. It is silent and retains a rules-preview disclosure throughout. It is **not** the final live-inference/public-YouTube submission video. No generated mock UI or fabricated provider call is substituted for browser evidence.

Docker has not been executed; the hosted database is unconnected. PostgreSQL 17 SQL was subsequently verified in CI (latest section below). Vercel project creation succeeded, but account-scope access denied storage linking; no successful live deployment is recorded. Video/public YouTube/Devpost remain open gates.

Regression after subsequent changes must update this report and PROJECT_STATE.md. Check CI artifacts for actual merchant, offer, repricing, marketplace, recovery, analytics, guardrail and mobile screenshots.

## Latest: server monitoring and real PostgreSQL

[CI 40089803664](https://github.com/yimtaegyun/revslot/actions/runs/40089803664) at commit1fc77683a1a73f05e044636a3ff7e429e95b5a4d passed 42 Python tests in 1.52 seconds, including a real PostgreSQL 17 service. Production build/TypeScript passed;4 Chromium tests passed in 23.7 seconds. The new browser case started the server clock, closed every page, observed repricing through read-only API polling and reopened the dashboard to confirm $56 before pausing it. That case took 12.3 seconds.

Persistence/restart, competing leases, expired-token fencing, CAS, retry, pause/reset/booking termination, expiry catch-up and scheduler authorization are tested. Hosted PostgreSQL is still unconnected; this result verifies the SQL against a real CI database, not production provisioning. Docker and public deployment remain unexecuted. Old screenshot/video files remain explicitly tied to their original verified capture commit. The numerical evaluation and live-provider gates are unchanged.

## Public deployment verification

[Revslot public preview](https://revslot-one.vercel.app/) is READY at deployment dpl_4DHbjT2Ma8RB1WNoqBp42yzc3fd2, source875c8f59ba8517ed798e2b80546a274c792db0d5. A fresh HTTP client without Vercel authentication received200 for health, session, cancel, advance and booking; prices6400→5600 cents,6km and70% recovery matched application state. The cloud browser independently completed the same visible workflow and saved an actual result screenshot. Project protection was scoped to allow this requested public audience. [Machine-readable evidence](LIVE_DEPLOYMENT_EVIDENCE.json).

Git-source deployment failed git_info_fail. The first direct upload omitted the newly-added monitoring module; production logs revealed the exact import error. The corrected49-file bundle matched the published Git tree and passed import/session/cancel/reprice before redeployment. No model result was fabricated. Current public mode is rules preview, manual clock and ephemeral SQLite. This is not proof of durable hosted monitoring or live NVIDIA inference; those gates remain open.

## Versioned migration readiness

[CI40092611551](https://github.com/yimtaegyun/revslot/actions/runs/40092611551) at9ae376e9c5741d13699f1dde74e8570c5166645b passed42 Python tests including applying backend/migrations/001_recovery_state.sql to PostgreSQL17, production build/TypeScript and4 Chromium cases. Neon installation is confirmed, but this session exposes no Neon DB tools and the official CLI has no authenticated profile. No Neon remote schema, project or DATABASE_URL has been created. The public preview remains unchanged and functional.
