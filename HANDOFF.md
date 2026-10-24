# Resume Revslot

Read PROJECT_STATE.md first. This is implemented code, not an idea-only handoff.

## Source and current verified state

- Checkout: `/workspace/sites/slotwake` (historical folder name; final brand Revslot).
- Public repository: https://github.com/yimtaegyun/revslot .
- All 107 source/data/research/docs files were pushed to main commit `ec93ed4a23ba161cd356eb169addaa9ccbaa6e41` (tree `3843190fad3eaafad35cd40004ac1690d833f43d`). Initial parent was `f3d24d6c5234bf933e016d986bd8932dd0d2cd85`.
- GitHub write APIs were used; the local Git index contains the same files but local HEAD is unborn. Do not force-push local Git. Continue via GitHub create_tree/create_commit/update_ref with current-head checks, or fetch/clone normally when available.
- Backend: FastAPI/Pydantic/LangGraph, deterministic hazard forecast/pricing/matching/policy, review, audit, revision CAS, SSE, clock, booking and metrics. Frontend: real Next.js/TS/Tailwind/shadcn screens, error/empty/loading states, mobile navigation.
- **34 pytest tests pass**. Next production build and TypeScript pass after cleanup. Exact commands are in README.
- Actual API seeded flow: $80 cancellation → $64/20%/12 profiles/3km → +20 demo minutes unsold → $56/30%/24 profiles/6km → reservation → $56 recovered/70%/20-minute fill. Natural-fill percentage is model-derived, not the prompt's 18%.
- 12,000 synthetic events, 5,022 cancellation events, 180 days, three merchants, six services. Temporal holdout model; final independent evaluation seed 20261030 / 1,000 scenarios. Final agent revenue/slot $53.17 vs fixed20 $48.70; fill 92.5% vs81.4%; average discount22.95% vs20%; unnecessary-discount100% for both. Do not hide negative metrics or claim real uplift. Earlier failed/coherence development reports retained.

## Open gates

No NEBIUS_API_KEY or TAVILY_API_KEY is configured. `scripts/check_integrations.py` ran and wrote an honest blocked evidence file (exit2). Mocked unit tests are not runtime evidence.

Vercel project exists `prj_BWTzn2W1WebpfwmOVUldqvTxOC3y`, owner scope `team_YKG2g9hfvRoFYSxyM0Oc5wzn`. Storage linking returned403 account-scope authorization denied. The recovery operation authorize_team_access is not exposed; don't create a duplicate project or bypass account authorization. No storage or paid plan created. Public deployment is not verified. PostgreSQL DATABASE_URL is supported but unconnected; Vercel /tmp SQLite is ephemeral.

Managed Sites preview failed because its runtime excludes the checkout virtualenv and lacks Python/uvicorn. Do not invent screenshots or claim browser QA. A GitHub Actions workflow (`Recovery verification`) and three Playwright E2E tests were pushed to obtain real browser evidence in an environment with Python. At the last connector read, workflow_runs was empty even though the GitHub commit UI showed a pending check. Investigate actual workflow/check status using supported GitHub tools. Prefer those over browser; browser fallback after repeated sufficient-plugin failures needs user approval. Do not silently substitute an unrelated demo.

No polished video/public YouTube/Devpost submission exists yet. `demo/` contains detailed 2:50 script, shots, draft story, feedback and checklist. Only final user terms acceptance can finish registration/submission.

## Next work

1. Resolve/verify GitHub CI run and obtain/inspect actual screenshots/video artifacts; fix observed defects only after feature freeze.
2. Update QA/state and deliverable statuses based on evidence. Current README/architecture/synthetic evaluation/portfolio materials are ready to review.
3. Obtain Vercel account authorization and server-side Nebius secret (Tavily optional bonus); use current project. Never ask for passwords/OTP in chat; never commit keys.
4. Deploy durable backend + frontend, verify public/incognito complete flow and actual NVIDIA model catalogue/inference; record real status/latency/model ID.
5. Capture honest final video, upload public YouTube via authorized account, finalize feedback and user-approved Devpost submission before 2026-10-31 02:00 KST.

## Tool/transfer notes

Source snapshot exporter is temporary `/workspace/scratch/f7abf47048bd/export_source.py`. Small UTF-8 entries were read in bounded groups; four large/binary files were GitHub blobs. Functions session store includes source manifests and tree/blob results, but files and this handoff are authoritative if memory resets. Research agents finished; no active code editing agents remain.

The existing combined competition reminder was updated to include this hackathon and an Oct30 08:00 KST deadline check, preserving its existing schedule and avoiding a duplicate automation.
