# Resume Revslot

Read PROJECT_STATE.md and docs/NEON_DEPLOYMENT_EVIDENCE.json. Continue the existing architecture and feature freeze; do not restart research.

## Current source and runtime
- Source: /workspace/sites/slotwake. Public MIT repo https://github.com/yimtaegyun/revslot . Verified application code d6a6a06a3d7b9aac7cb1b50b89fa115de93253d0, tree276a420da26bfa471412a3ce19fc4a89fe80fb0b. Exact native source commit imported; git fsck passed. Later documentation on main records the verified deployment and screenshot12. Inspect the actual branch head before a write. Never force-push.
- Live: https://revslot-one.vercel.app/ . Current READY deployment dpl_AqCrPafSjQotgVD7m9t3aYktZ7xG from d6a6a06a... .49 runtime files matched reviewed source. Vercel project prj_BWTzn2W1WebpfwmOVUldqvTxOC3y /team_YKG2g9hfvRoFYSxyM0Oc5wzn. Access grant resolved; do not ask again.
- Neon Free project late-band-96300538, aws-us-east-2, PostgreSQL17. Production br-lively-flower-b5wc7kd9; isolated verification br-silent-art-b5lyqre2. Migration001 applied to both. Pooled DATABASE_URL, CRON_SECRET and server wake URL configured in protected production env. No paid plan, payment or domain purchase.

## Actual hosted proof
A$56 synthetic reservation at revision3 survived multiple redeployments unchanged. Latest API-only run: server clock-start response0.86s;12.02s later20demo minutes elapsed, shared price6400→5600cents and reach6km, then reservation$56/70% and clock stopped. After starting the clock, the observer only issued GET state requests until the transition. This is not a test-side tick, browser heartbeat or fabricated result.

Native Neon recoveryclock deployment2 is completed. Trusted FastAPI /wake starts bounded post-response work, max12 ten-second target calls covering the seeded90-real-second inventory horizon, exiting immediately on zero active SQL jobs. Native cron trigger-e2c212f4-410d-4afd-8157-d5bf544148b1 retries at */15 * * * *. The trigger's legacy name is recovery-clock-every-minute; its actual cron field is15minutes. SQL jobs, leases and revision/token fencing own durability; waitUntil/module state is not a durable queue or daemon. Failed wake pauses the persisted clock and returns503. This avoids constant empty-queue database warming during the judge-access period throughDec15.

Native logs16:29:09Z recorded3calls /1processed /0conflicts /0failed; idle retry16:30:03Z recorded1call /0processed /0failed. SQL pending jobs0. Public/forged schedule and missing/wrong-token wake requests all returned401. Current Vercel error/fatal scan16:17:21.934Z–16:32:21.934Z had no matches. Raw check report:/workspace/scratch/f7abf47048bd/neon-wake-production-verification.json . Authoritative public evidence: docs/NEON_DEPLOYMENT_EVIDENCE.json.

A separate actual visible browser run on the prior durable deployment advanced60demo min, selected$52, paused/booked65% gross recovery. Screenshot12 records that actual state, not the earlier$56 result. Original nine screenshots/video retain their original capture provenance. The170s silent captioned review is disclosed rules preview, not a final live-model YouTube take.

## Latest checks
CI https://github.com/yimtaegyun/revslot/actions/runs/40095746361 at d6a6a06a... passed45 Python tests in1.19s with actual PostgreSQL17,6 Node scheduler tests, production build/TypeScript and4 Chromium tests in23.7s. Local44 passed/1 PG skipped. The browser case closes all pages and verifies server repricing after reopening. No repeat testing is needed without code changes/new concerns. Docker remains unexecuted.

## Immediate next work / external gates
No NEBIUS_API_KEY or TAVILY_API_KEY. A real NVIDIA open-model invocation through Nebius Token Factory is required. Do not substitute Neon AI Gateway or mocked tests. Adapter discovers /models then selects an available NVIDIA Nemotron; no deprecated model ID is assumed. Structured public action summaries only; never persist provider reasoning.

Cloud browser was opened to https://tokenfactory.nebius.com/ and the actual Log in button led to https://auth.tokenfactory.nebius.com/ui/login . Visible methods: Get started with SSO, Google, GitHub. No method/account chosen and no credential/API key entered/created. BrowserAuth documentation was read; use secure browserAuth.request for method choice and any credential entry. Do not choose an account/method or type secrets through lower-level UI. Confirm any new credential access/terms at the actual step, hand off signup if needed. The website may create a new account during first OAuth; stop before legal acceptance or payment. No private/sensitive login values belong in chat. Browser-bound handles can reset; inspect actual tab inventory only as necessary and preserve target origin.

Continue secure Nebius login and server key; verify actual catalogue/model/context and latency; record final live-provider take; public YouTube under3min; observed sponsor feedback; user Devpost terms acceptance and actual submission. Deadline2026-10-31 02:00 KST, targetOct30 20:00 KST. Existing combined competition reminder is set; do not duplicate.

## Truthful evaluation
12,000 synthetic events /180days /3merchants /6services. Independent-seed1,000 cancellation comparison:$53.17 agent vs$48.70 fixed20 gross/slot; discount22.95% vs20%; unnecessary discount100% both. Preserve negative findings; no real uplift or minimum-discount claim. Actual representative$80→$64→$56→$56/70% is a calculated sandbox scenario. Natural fill initially23% rounded, not the brief's illustrative18%.

## Tool/reconciliation notes
Prefer native tools. GitHub normalized workflow queries previously returned empty; github_fetch of actual REST actions endpoints and decoded job logs are reliable. Native GitHub ref updates must use expected-SHA guards. If importing native commits locally, reconstruct exact public metadata internally; native timezone+0900, no terminal newline. Never print author email or secrets. Reconcile any failed/truncated mutation before retrying.

Vercel responses can nest lists at result.deployments.deployments and details at result.deployment. Guard types before mapping; do not treat a null structuredContent as account failure. Previous deployment attempt yielded no usable ID; listing confirmed nothing created before the successful explicit retry dpl_Aq... . Runtime upload must include monitoring.py; the historical omitted-module packaging bug is fixed. Updated bundle:/workspace/scratch/f7abf47048bd/deploy-wake-source-files.json .

Functions store disappears across user turns. Secrets remain in protected Vercel/Neon env, so app-driven verification needs no test-client secret. Native function responses may contain environment as an array: output metadata only, never env values. Do not request Neon/Vercel access again or create duplicate projects.
