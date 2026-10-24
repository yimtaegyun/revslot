# Server-owned monitoring

The accelerated demo clock is persisted on the server. Clicking Play schedules 20 demo minutes every10 real seconds. Closing every browser page no longer stops observation/repricing. It remains explicitly synthetic, accelerated time; it is not a live calendar integration.

Standalone FastAPI starts a worker in its application lifespan by default. SQLite on a persistent volume or PostgreSQL stores both run state and scheduled jobs. `REVSlot_WORKER=0` disables the daemon. Resetting the session stops its previous clock; booking the final active slot or expiry stops future ticks. Manual +20-minute advance remains available.

`clock_jobs` records the next due time and a60-second lease. Conditional SQL claims serialize workers. A lease token and state revision fence every worker commit; state and the next due time commit in one transaction. An expired/replaced worker cannot commit. After a crash/restart, overdue ticks catch up in bounded batches, honoring current policies and expiry. A hard-killed worker's lease must expire before another claims its job. No provider text or secrets are written to failure logs.

## Serverless boundary

Vercel instances do not run this permanent daemon. Their Play control is disabled unless an external scheduler is explicitly configured. Manual advance continues to work. A stateless function cannot honestly promise continuous execution merely because a Python task was created.

An external scheduler can call `GET /api/jobs/tick` with `Authorization: Bearer <CRON_SECRET>`. Without the secret the endpoint fails closed. Vercel additionally requires PostgreSQL; `/tmp` SQLite is rejected. Set `REVSlot_EXTERNAL_TICK=1` only after configuring the actual scheduler. Environment-variable presence is configuration, not proof that scheduled invocations occurred. The health/provenance views expose the current mode.

No paid scheduler or plan was activated. [Official Vercel Cron limits](https://vercel.com/docs/cron-jobs/usage-and-pricing) currently restrict Hobby jobs to once per day; that is unsuitable for this10-second demonstration. A stable standalone backend with its included worker is the supplied low-cost option; a hosted deployment still requires account access. Docker is supplied but remains unexecuted in this environment.

## Verification

Python tests cover persistence/restart, two competing workers, token fencing, pause/reset/booking termination, expiry catch-up, failed-tick retry and protected scheduler access. CI provisions a real PostgreSQL17 service to test its SQL, competing claims, CAS and repricing. A separate browser case starts Play, closes every page, observes state using read-only API requests and reopens the merchant view to verify $56 repricing. Check QA_REPORT.md for actual run status rather than assuming these tests passed because they exist.
