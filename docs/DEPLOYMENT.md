# Verified public deployment

Public preview: https://revslot-one.vercel.app/ . Existing Vercel project prj_BWTzn2W1WebpfwmOVUldqvTxOC3y, team_YKG2g9hfvRoFYSxyM0Oc5wzn. Account grant is resolved; do not request it again or duplicate this project. Production deployment dpl_AqCrPafSjQotgVD7m9t3aYktZ7xG is READY and publicly accessible without judge login. No paid plan or domain was purchased.

The49-file runtime bundle matched reviewed Git commit d6a6a06a3d7b9aac7cb1b50b89fa115de93253d0 byte for byte. Vercel Services (Beta) routes /api/* to FastAPI and the remaining paths to Next.js; preserve the API prefix. Git-source import initially failed, so exact reviewed source files were uploaded. A historical missing-module packaging error was fixed before this successful deployment.

## Durable state

The public app uses a Free Neon PostgreSQL17 project in aws-us-east-2. Migration001 was first applied to an isolated child branch, then production. DATABASE_URL uses the pooled host and is a sensitive production Vercel variable. Neither its value nor the scheduler credential is stored in source, client code, screenshots or evidence. An anonymously created$56 reservation survived redeployment with revision3 unchanged. Native SQL independently confirmed the stored snapshot. See NEON_DEPLOYMENT_EVIDENCE.json.

SQLite remains the local default and an explicitly ephemeral serverless fallback. It is not the current public storage. A named Docker volume is another supplied standalone option; Docker has not been executed.

## Hosted scheduling

The existing FastAPI /api/jobs/tick endpoint requires a server-only Bearer CRON_SECRET and PostgreSQL on Vercel. After committing a durable clock job, FastAPI POSTs to the protected Neon /wake endpoint. Neon tracks bounded post-response work, at most12calls at a ten-second target cadence, covering the seeded90-real-second inventory horizon. Empty queues exit immediately. A native15-minute schedule retries interruptions. The function and waitUntil own no durable queue or daemon. The existing Python graph, SQL jobs, leases and revision fences handle due work, overlapping invocations, retries and booking races. No permanent Vercel or Neon isolate daemon is assumed.

CRON_SECRET is sensitive production configuration shared with the function. REVSlot_EXTERNAL_TICK=1 was set after the real function and schedule were created. Actual wake logs recorded3calls,1processed job and zero failures, then exited after booking; an idle scheduled retry made only1call. An API-only session repriced$64→$56, expanded reach to6km and advanced20demo minutes after12.02real seconds; its observer only made read-only state requests. The public browser independently exercised the clock and confirmed a later$52 reservation after60demo minutes.

REVSlot_SCHEDULER_WAKE_URL is an encrypted, server-only Vercel variable. A failed wake pauses the persisted clock and returns a readable503. Source/reproducible config: infrastructure/neon. Run npm ci, npm test, npm run build. For an authorized Neon CLI account, deploy neon.ts with a gitignored environment file containing the shared CRON_SECRET; never inline that credential in command history. Verify trigger deliveries and health, not just configuration presence. Free service quotas and network/cold-start delays apply; no paid upgrade is authorized.

Official references: [Functions](https://neon.com/docs/compute/functions/overview), [deploy API](https://neon.com/docs/compute/functions/deploy), [trigger authentication](https://neon.com/docs/compute/functions/triggers/overview), [free quotas](https://neon.com/pricing).

## Remaining provider/submission gates

NEBIUS_API_KEY and optional TAVILY_API_KEY are absent. The runtime discovers a live NVIDIA Nemotron catalogue entry; keys never use NEXT_PUBLIC_* or a client-side form. Actual inference/context evidence must be recorded before changing the preview disclosure. Do not substitute Neon AI Gateway for the required Nebius/NVIDIA runtime.

Keep free public judging access through the official judging period, subject to service availability. Final live-model video/public YouTube, observed sponsor feedback and Devpost submission are open. The user must personally accept legally binding registration/submission terms.
