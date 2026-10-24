# Server-owned monitoring

The accelerated demo clock is persisted on the server. Clicking Play targets20demo minutes every10real seconds. Closing every browser page no longer stops observation/repricing. It remains explicitly synthetic, accelerated time; it is not a live calendar integration.

Standalone FastAPI starts a worker in its application lifespan by default. SQLite on a persistent volume or PostgreSQL stores both run state and scheduled jobs. `REVSlot_WORKER=0` disables the daemon. Resetting the session stops its previous clock; booking the final active slot or expiry stops future ticks. Manual +20-minute advance remains available.

`clock_jobs` records the next due time and a60-second lease. Conditional SQL claims serialize workers. A lease token and state revision fence every worker commit; state and the next due time commit in one transaction. An expired/replaced worker cannot commit. After a crash/restart, overdue ticks catch up in bounded batches, honoring current policies and expiry. A hard-killed worker's lease must expire before another claims its job. No provider text or secrets are written to failure logs.

## Serverless boundary

Vercel instances do not run this permanent daemon. Their Play control is disabled unless an external scheduler is explicitly configured. Manual advance continues to work. A stateless function cannot honestly promise continuous execution merely because a Python task was created.

An external scheduler can call `GET /api/jobs/tick` with `Authorization: Bearer <CRON_SECRET>`. Without the secret the endpoint fails closed. Vercel additionally requires PostgreSQL; `/tmp` SQLite is rejected. Set `REVSlot_EXTERNAL_TICK=1` only after configuring the actual scheduler. Environment-variable presence is configuration, not proof that scheduled invocations occurred. The health/provenance views expose the current mode.

No paid scheduler or plan was activated. [Official Vercel Cron limits](https://vercel.com/docs/cron-jobs/usage-and-pricing) currently restrict Hobby jobs to once per day; that is unsuitable for this10-second demonstration. A stable standalone backend with its included worker is the supplied low-cost option; the current public deployment instead uses the verified Neon scheduler described below. Docker is supplied but remains unexecuted in this environment.

## Verification

Python tests cover persistence/restart, two competing workers, token fencing, pause/reset/booking termination, expiry catch-up, failed-tick retry and protected scheduler access. CI provisions a real PostgreSQL 17 service to test its SQL, competing claims, CAS and repricing. A separate browser case starts Play, closes every page, observes state using read-only API requests and reopens the merchant view to verify $56 repricing. Check QA_REPORT.md for actual run status rather than assuming these tests passed because they exist.

Verified: [CI 40089803664](https://github.com/yimtaegyun/revslot/actions/runs/40089803664),42 Python tests including PostgreSQL 17 and 4 Chromium cases. This is real test execution. Hosted scheduling was subsequently verified separately below.


## Actual public Neon scheduler

Production now uses Neon PostgreSQL17 plus a native every-minute schedule invoking infrastructure/neon/recoveryclock.mjs. parseTriggerDelivery requires native platform provenance; public and forged-header requests both returned401. Each bounded function invocation calls the existing authenticated Python tick six times at a ten-second target cadence. It performs no pricing, matching or booking arithmetic and holds no recovery state. SQL leases/CAS remain authoritative; overlapping delayed schedules are safe.

Actual native logs recorded six calls /one processed job /zero failures at2026-10-24T12:34:51Z. An API-only session, observed only with GET requests after starting Play, repriced$64→$56 and expanded to6km after13.27real seconds. A completed reservation also survived redeployment. The independent visible browser run continued to60demo minutes and$52 before being paused/booked. These are separate actual runs, not a fixed fabricated outcome. [Evidence](NEON_DEPLOYMENT_EVIDENCE.json).

Free hosting quotas, cold starts and network delays remain limits; ten seconds is a target cadence, not a timing guarantee. No paid plan was activated. A missing/disabled scheduler must be reflected in configuration and the UI rather than assumed to run because code exists.


## Current idle-efficient activation

The current production source is d6a6a06a3d7b9aac7cb1b50b89fa115de93253d0. FastAPI first commits the SQL job, then makes a bounded authenticated POST /wake. Failure pauses the persisted clock. Neon tracks one bounded invocation (maximum12calls at a ten-second target cadence); it exits immediately when the authenticated tick reports zero active jobs. A native */15 * * * * retry schedule owns periodic recovery. waitUntil provides bounded post-response execution only; SQL owns job state, leases and lifecycle. The seeded latest appointment expires after90real seconds of accelerated time, within this bound.

This reduces idle Free-quota consumption rather than waking PostgreSQL every ten seconds throughout the judging period. Quotas/network availability still apply. Actual production proof:0.86s start request,12.02s browser-free repricing,$56/70% reservation,3calls/1processed/0failed followed by an idle1call retry; SQL jobs then zero. [Latest evidence](NEON_DEPLOYMENT_EVIDENCE.json).
