# Verification status

Verified locally on 2026-10-24:

- **34 pytest tests passed**, including price/margin/cap constraints, probability/time behavior, high-demand full price, opt-in matching, strict schemas, cancellation idempotency, full recovery, actual repricing/reach, same-slot pricing, human approval, stale/double booking, expiry, origin/session isolation, atomic competing writes, audit modification detection, provider parser failures and total inference timeout.
- Next.js production build and TypeScript passed again after dependency/source cleanup (Next.js 16.3.4).
- Dataset generator and independent-seed simulation executed; data card/checksum and unfavorable metrics retained.
- Connectivity checker executed and correctly returned blocked (exit 2): no Nebius/Tavily key configured. Unit mocked calls are not runtime evidence.

**Full-stack browser verification passed:** [CI run 40064620041](https://github.com/yimtaegyun/revslot/actions/runs/40064620041), commit `574de1d52a5bc8d185a20df08e9ca7e45833e88e`. Python: 34 passed in 0.67 seconds. Production build/TypeScript: passed. Chromium: 3 passed in 11.7 seconds, covering cancellation → $64 offer → +20 demo minutes → $56 reprice/expanded audience → sandbox reservation → merchant metrics, human approval, and mobile navigation/no horizontal overflow. Nine real screenshots and the 7.64-second raw workflow recording are in [demo](../demo/README.md); checksums and log excerpts are in [QA_EVIDENCE.json](QA_EVIDENCE.json). The main agent inspected every captured view, including final provenance. Text readability and an inactive skip-link capture defect were corrected before the passing run.

The first GitHub CI run failed before hydration because development-resource requests were blocked for the loopback host. Tests now exercise the production build; development origins are limited to localhost/127.0.0.1. A Strict Mode initialization race, client fetch timeout and explicit SQL connection cleanup were repaired. A subsequent run passed all tests but failed a cache-save cleanup; that invalid cache configuration was removed. Both final runs succeeded. Managed preview itself cannot launch Python/uvicorn; CI is the verified full-stack environment.

The 1920×1080, 170-second captioned review film uses actual inspected captures. It is silent and retains a rules-preview disclosure throughout. It is **not** the final live-inference/public-YouTube submission video. No generated mock UI or fabricated provider call is substituted for browser evidence.

Docker and PostgreSQL have not been executed/connected. Vercel project creation succeeded, but account-scope access denied storage linking; no successful live deployment is recorded. Video/public YouTube/Devpost remain open gates.

Regression after subsequent changes must update this report and PROJECT_STATE.md. Check CI artifacts for actual merchant, offer, repricing, marketplace, recovery, analytics, guardrail and mobile screenshots.
