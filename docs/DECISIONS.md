# Decisions

## D001 — Canonical deterministic pricing

Decision: integer-cent candidate optimization with policy validation before any publish/booking.

Reason: LLM arithmetic and text can be wrong; a merchant's minimum margin is a contract of the application.

Alternatives: freeform LLM pricing; fixed universal discount.

Trade-off: demo conversion curves are synthetic assumptions, not evidence of causal business uplift.

## D002 — Credible differentiation

Decision: focus on cancellation-specific orchestration and merchant accountability.

Reason: official ClassPass material already documents natural demand protection and adaptive price optimization.

Alternatives: claim novel dynamic discounting.

Trade-off: narrower novelty claim; stronger factual credibility.

## D003 — External keys remain outside source

Decision: server environment secrets; no browser key form and no credentials committed.

Reason: protect accounts and make provider status verifiable.

Alternatives: hardcoded keys; browser local storage.

Trade-off: live AI testing waits for account credentials; deterministic preview remains usable and labeled.

## D004 — Verify the production build in a full-stack CI environment

Decision: Chromium E2E runs Next production mode alongside real FastAPI, with actual captures, not the managed preview image.

Reason: managed preview lacks Python; the first development-mode run failed hydration because of loopback resource origins. Production-mode verification subsequently passed the entire reservation flow.

Alternatives: claim code/build as browser evidence; replace the Python stack; fabricate a visual mock.

Trade-off: CI runs take longer; real provider calls and hosted access still need separate evidence. Capture cleanup waits for the real toast to disappear and resets scrolling without altering UI values.

## D005 — Preserve an honest review film before runtime credentials

Decision: produce a170-second captioned film from actual inspected screenshots, labeled rules preview throughout; retain the unedited browser recording separately.

Reason: the work can be reviewed while external authorization is pending, without suggesting unverified NVIDIA or Tavily usage.

Alternatives: final live recording before keys; script only.

Trade-off: the review film is silent and not the eligible final submission take. Live-provider recording, public YouTube and final Devpost acceptance remain open.

## D006 — Move the demo clock off the browser

Decision: persist scheduled ticks and run them with a leased standalone FastAPI worker; expose an authenticated bounded tick for an explicitly configured external scheduler.

Reason: browser intervals stopped monitoring when a judge closed the tab. SQL leases and revision/token fences protect restarts, overlapping workers and booking races.

Alternatives: continue browser heartbeat; assume a serverless daemon is permanent; activate a paid scheduler without consent.

Trade-off: serverless Play requires durable PostgreSQL and a real external scheduler. A stable standalone backend works without that added service. The pre-existing pricing model, policy objective, agent graph and UI layout are retained. This completes the requested monitoring behavior; it is not a new product feature or architecture rewrite.

## D007 — Deploy existing monitoring with Neon PostgreSQL and native triggers

Decision: use a Free Neon PostgreSQL17 project and a small trigger-authenticated Node function that calls the existing FastAPI tick in bounded six-call invocations. Keep inference on Nebius.

Reason: Vercel temporary SQLite cannot retain state across instances/deployments, and Hobby Cron cannot drive the requested ten-second demo clock. The Neon plugin became available and the account was verified as Free. Schema was applied on an isolated branch before production.

Alternatives: a stable standalone worker with a volume; paid scheduler; an unreliable serverless daemon.

Trade-off: another deployment primitive and free service quotas; timing varies with network/cold starts. PostgreSQL remains the source of truth, with leases and revision fencing; the function owns no booking state. Actual redeployment retention, scheduled repricing and public forged-trigger rejection are verified in NEON_DEPLOYMENT_EVIDENCE.json. No new agent, pricing objective or product feature was added.


## D008 — Exit idle work and wake only active demo monitoring

Decision: commit SQL jobs before a trusted server wake; cap a Neon invocation at12ten-second calls and exit on zero jobs; retain native15-minute retries.

Reason: constant empty-queue polling prevents PostgreSQL scale-to-zero and wastes the Free allowance during the required judging-access period throughDec15.

Alternatives: keep a constant hot scheduler; pay for always-on capacity; rely only on ephemeral memory or an open browser.

Trade-off: failed/interrupted work can wait until the next retry and may expire; the UI fails closed if the initial wake is rejected. SQL remains authoritative, and post-response work is bounded rather than an isolate daemon. Actual wake, idle exit, retained reservations and failure/authorization behavior are tested; no paid upgrade was made.
