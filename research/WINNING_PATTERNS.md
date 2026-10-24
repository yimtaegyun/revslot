# Winning patterns translated into product decisions

Research date: 2026-10-24. Read with [the 20-project benchmark](HACKATHON_WINNERS_BENCHMARK.md). These are qualitative design inferences from public awarded submissions, not statistically identified causes of winning. Award announcements establish placements; public project pages contain author claims. No video opening was frame-audited.

## Answers to the thirteen required questions

| Question | Evidence-led answer | Revslot implementation requirement |
|---|---|---|
| 1. Which problems? | Repeatedly a concrete workflow with urgency, inaccessible information, or expensive manual coordination | Expiring service time, one cancellation, measurable recovery |
| 2. One-sentence problem? | Strong entries readily map actor + obstacle + consequence; breadth sometimes weakens this | “An unsold appointment becomes worthless when its start time arrives.” |
| 3. Action or answers? | Winners include physical commands, browser actions, database queries, artifact creation, and reports | Cancellation automatically starts pricing, matching, offers, monitoring, and re-evaluation |
| 4. How many tools? | No universal optimum: projects range from a few memory tools to large MCP surfaces | Count only necessary executable tools; document their inputs and outputs |
| 5. Many agents? | Role division varies. More roles alone establish neither quality nor autonomy | One stateful orchestrator and bounded demand/pricing/matching/operator/outcome responsibilities |
| 6. Action trace? | Mission state, query history, focused explanations, and live artifacts make activity visible | Timestamped tool/action summaries, policy outcome, input provenance; no private reasoning |
| 7. Human approval? | Aegis and JohnKeats explicitly identify escalation or review; other projects leave it uncertain | Threshold and low-confidence gates; booking still requires consumer confirmation |
| 8. Failure fallback? | Wand reconnects, PROCSee checkpoints, JohnKeats decouples optional learning | External search optional; model outage visible; safe rule fallback; durable state and retries |
| 9. Metric evidence? | Outcome claims vary in strength and are often author-reported | Seeded held-out simulation, four strategies, constraints, paired uncertainty, honest limitations |
| 10. First 30 seconds? | Exact videos not reviewed; no factual claim about their openings is warranted | Proposed sequence: cancel $80 appointment → persisted agent action → priced listing |
| 11. Result screen? | Domain-native artifacts provide concrete meaning: map, report, mission, console, memory object | Merchant calendar and revenue KPI update from the actual reservation record |
| 12. Product/technical balance? | Public stories commonly connect pain → workflow → architecture → challenges; no validated percentage | Demo mostly workflow; short architecture segment after proof of action |
| 13. Memorable moment? | A command changes the world or interface rather than merely producing text | Cancellation → autonomous reprice/audience expansion → consumer books → recovered amount animates |

## Patterns to implement immediately

1. **Show a complete transaction.** Merchant and consumer screens must share real application state. Recovery accounting must be based on confirmed bookings, with a unique slot and idempotency key.
2. **Make uncertainty visible.** Distinguish estimated fill probability, synthetic outcome, and observed runtime API success. An API badge lights only after a successful call; a disconnected provider must remain visibly disconnected.
3. **Separate calculation from interpretation.** The pricing engine enumerates feasible candidates and computes expected revenue. The model can plan allowed tool use, summarize weak external context, generate an honest offer, and explain selected evidence. It cannot override a price floor or invent a probability.
4. **Persist the loop.** Observing no booking is an event, not a prerecorded animation. Time advancement triggers reevaluation; a booking stops future repricing. Every state transition records its cause.
5. **Use one focused timeline.** Show the newest important action prominently, with deeper audit data available on demand. Never display raw model chain-of-thought.
6. **Budget for reliability.** Use typed schemas, bounded model output, timeouts, retries, idempotency, restart-safe storage, and fallback paths. A synthetic business scenario may be deterministic; live inference must be labeled independently.
7. **Treat provenance as product.** Always show synthetic-data and accelerated-clock labels. Cite external context. No fake customers, partnerships, reviews, revenue, performance, or runtime integrations.

## Evidence-derived anti-patterns

- A winning Devpost page may contain unsupported superlatives or unreproduced accuracy claims. Placement does not make those claims safe to reuse.
- Several current project descriptions mix implemented features with roadmaps. Keep our README capability table explicit: implemented, locally tested, deployed, provider verified, blocked.
- Raw reasoning displays and overly long narrative openings should not be imitated. Our product requires concise decision summaries and an immediate demonstration.
- Do not infer a causal sales uplift from synthetic data, or evaluate the optimizing agent only against the same probability function that chose its policy. Use a separate generative environment, shared random draws, held-out scenarios, sensitivity analysis, and publish unfavorable results too.
- A research-backed concept still needs actual merchant evidence. We have no interviewed customers or pilot revenue yet; record that limitation instead of inventing validation.

## Specific sources and bounded takeaways

- [Aegis](https://devpost.com/software/aegis-autonomous-multi-agent-crisis-command): focused visibility and natural escalation inform the timeline and approval interaction.
- [Orbital Assets](https://devpost.com/software/orbital-assets): separation of deterministic valuation from model narrative informs pricing boundaries.
- [JohnKeats.AI](https://devpost.com/software/johnkeats-ai): a policy gate and independent optional pipeline inform fail-safe design.
- [Wand](https://devpost.com/software/wand-a-live-agent-that-sees-browses-and-clicks-with-you): stale-context failures and explicit reconnect behavior inform state revalidation.
- [PROCSee](https://devpost.com/software/procsee): phase checkpoints and query auditing inform durable recovery attempts.
- [EcoLafaek](https://devpost.com/software/ecolafaek): a connected reporting-to-analysis workflow informs the merchant-to-consumer handoff.
- [Sankofa](https://devpost.com/software/sankofa-y47f9p): evidence/reconstruction labels inform trust labels, without copying its long loading ceremony.
- [drone-copilot README](https://github.com/BryenInsights/drone-copilot): clearly labeled recorded missions inform honest replay documentation; live inference and replay are separate evidence states.

## Acceptance evidence for judges

Show the same reproducible scenario three ways: UI action trace, persisted audit record, and integration test. Demonstrate one guardrail rejection, one optional API outage, one automatic repricing event, and exactly one successful booking under concurrent attempts. State measured latency only after timing the deployed model path. Provide public source, a working URL, setup instructions, actual screenshots, and a sub-three-minute public video; none can be replaced by research quality.
