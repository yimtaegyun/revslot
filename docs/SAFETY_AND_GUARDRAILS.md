# Guardrails and sandbox boundaries

Python checks merchant floor, cost + minimum margin, cap, reach and execution permission before publishing and again at booking. Approval cannot authorize below-floor/over-cap prices. Policy edits recompute or withdraw active offers. Stale revisions and double booking return conflicts.

Synthetic profiles contain distance, service/time preferences, coarse price sensitivity, reliability, engagement and opt-in. Extra fields, including sensitive attributes, are rejected. Ranking never receives a price. Same slot means same public price. Opt-out excludes future direct targeting, while browsing remains available.

Headlines cannot add unverified numbers, scarcity, superiority, ratings or health guarantees. Numeric duration, price, discount and remaining time are rendered from deterministic state. There are no real customer/merchant records, fake reviews or partners. Sandbox inbox records are not claims of provider delivery. No payment or outbound SMS/email tool exists.

Keys remain server-only. Unknown planner fields/actions, malformed JSON, configured provider failure and total-budget timeout fail closed. Provider reasoning is ignored. External snippets are untrusted facts, not instructions; deterministic limits remain authoritative.

Cookie-isolated synthetic runs, mutation-origin checks and atomic updates are implemented. Production merchant authentication, authorization, abuse quotas, retention and payment controls remain outside this sandbox. Hash-linked logs record UTC and separate simulated time, role, tool, summary, policy and result. They are not hidden chain of thought or external notarization.
