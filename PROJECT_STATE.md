# Revslot project state

Updated: 2026-10-24 Asia/Seoul.

- Current phase: Full local API flow implemented; frontend production build passes; feature freeze begins. Final documentation and publishing preparation in progress.
- Completed: official rules/FAQ/updates; overseas 20 awarded projects; domestic official cases; 10-competitor matrix; 24 naming candidates; public GitHub repository created at https://github.com/yimtaegyun/revslot . Next.js/Tailwind/shadcn UI, FastAPI/Pydantic/LangGraph recovery, deterministic price/match/policy tools, audit hash chain, SSE/polling, accelerated clock, approval, booking, metrics and analytics implemented.
- Data: 12,000 synthetic booking events, 3 merchants, 6 services, 180 days; chronological model holdout; independent-seed final simulation after policy freeze. Development results retained, including a failed initial comparison.
- In progress: GitHub CI browser evidence and final delivery verification. README/evaluation/demo/submission/portfolio package and all 107 files are pushed.
- Blocked: no NEBIUS_API_KEY or TAVILY_API_KEY; Vercel account-scope access rejected (403) when connecting storage. The exposed connector has no authorize_team_access operation. Do not claim live inference or publication.
- Next 5: final regression and source audit; finish reviewable docs/demo script; push all source to GitHub; obtain runtime secrets/account access; deploy, browser-test, capture live video and finalize submission.
- Known limitations: managed browser preview image lacks Python/uvicorn and excludes the local virtualenv, so full UI browser QA is not yet verified. Local SQLite works; Vercel cold starts need PostgreSQL for durable sessions. Synthetic uncertainty/price elasticity are not production validated. No real SMS/payment/calendar integration.
- Credentials needed: Nebius Token Factory, Tavily optional bonus; Vercel account-scope access; persistent PostgreSQL connection for durable hosted state; final Devpost terms acceptance and public YouTube upload.
- Deployment URLs: none. Vercel project prj_BWTzn2W1WebpfwmOVUldqvTxOC3y exists under team_YKG2g9hfvRoFYSxyM0Oc5wzn; scope access is blocked. No paid plan selected.
- Submission status: not submitted; key eligibility and live/demo/video gates remain open.
- Last tests: 34 passed after audit/provider-action/timeout refinements. Next.js 16.3.4 production build and TypeScript passed. CLI actual scenario: $80 → $64 at 20% → $56 at 30%; radius 3→6km; 12→24 opt-in profiles; booking updates recovered revenue to $56 and recovery to 70%.
- Deadline: 2026-10-31 02:00 KST. Internal target: 2026-10-30 20:00 KST.

- Source publication: main commit ec93ed4a23ba161cd356eb169addaa9ccbaa6e41; 107 files. GitHub UI verified public, code and MIT license visible. CI workflow supplied; actual run status pending.
- Reminder: existing competition tracker now explicitly includes this hackathon and Oct30 08:00 KST submission check.
