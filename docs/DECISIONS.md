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
