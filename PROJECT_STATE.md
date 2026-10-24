# Revslot project state

Updated: 2026-10-24 Asia/Seoul.

- Current phase: Feature freeze; implementation, reproducible evaluation and full browser QA verified. Final evidence publication and external integration gates.
- Completed: official rules/FAQ/updates, 20 overseas awarded projects, domestic official cases, 10-competitor matrix, 24 naming candidates; public MIT GitHub repository https://github.com/yimtaegyun/revslot . Next.js/Tailwind/shadcn frontend; FastAPI/Pydantic/LangGraph; deterministic pricing/matching/policy; revision CAS, audit, SSE/polling, clock, approval, reservation and analytics.
- Data: 12,000 synthetic events /180 days /3 merchants /6 services; temporal holdout; independent seed 20261030 /1,000 evaluation cancellations. Negative results retained. Agent gross revenue/slot $53.17 vs fixed20 $48.70; average discount 22.95% vs20%; unnecessary discount100% for both. No real uplift claim.
- Verified source: application and capture code at main commit 574de1d52a5bc8d185a20df08e9ca7e45833e88e. CI https://github.com/yimtaegyun/revslot/actions/runs/40064620041 succeeded: 34 Python tests, production build/TypeScript and3 Chromium tests. Local Git history restored to match published ancestry; no force-push needed.
- Evidence package: final documentation,9 inspected screenshots plus README crop, the raw7.64-second browser recording, rendering source and detailed portfolio article. A1920x1080 /170-second silent review film is saved and delivered; it retains rules-preview disclosure throughout and is not the final eligible take.
- Blocked: no NEBIUS_API_KEY or TAVILY_API_KEY; Vercel account-scope authorization403 for storage linking and existing-project GET. The authorization tool became available; a single-use consent link was generated and shown to the user. Grant is not yet verified. Do not claim live inference or public deployment.
- Next5: obtain server-side keys and Vercel scope access; verify actual Token Factory catalogue+NVIDIA inference and optional Tavily; deploy existing project with durable storage; verify anonymous browser flow and record final live video; finalize observed sponsor feedback, public YouTube and user-accepted Devpost submission.
- Known limitations: synthetic forecast/elasticity not market validated; support heuristic not calibrated; browser heartbeat controls demo monitoring; no real SMS/payment/POS/calendar integration, production auth or abuse quotas. Docker/PostgreSQL remain unexecuted. Vercel /tmp SQLite is ephemeral.
- Credentials needed: Nebius Token Factory; optional Tavily bonus; Vercel scope yimtaegyun0217-7000; durable PostgreSQL connection or stable single-instance backend; later YouTube/Devpost account access and user terms acceptance. Never paste keys into public source or client UI.
- Deployment URLs: none. Existing Vercel project prj_BWTzn2W1WebpfwmOVUldqvTxOC3y /team_YKG2g9hfvRoFYSxyM0Oc5wzn. No paid plan selected.
- Submission status: not submitted, not fully eligible; runtime/hosting/final-video/terms gates open.
- Actual browser scenario: $80 cancellation -> $64/20%/12 profiles/3km -> +20 demo minutes unsold -> $56/30%/24 profiles/6km -> booking -> $56 gross recovery /70% /20 demo minutes. Natural fill is model-derived (23% rounded initially), not the brief's18%.
- Deadline: 2026-10-31 02:00 KST. Internal target: 2026-10-30 20:00 KST.
- Reminder: existing combined competition tracker includes the hackathon and Oct30 08:00 KST submission check; no duplicate automation created.
