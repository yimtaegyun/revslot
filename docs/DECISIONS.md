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
