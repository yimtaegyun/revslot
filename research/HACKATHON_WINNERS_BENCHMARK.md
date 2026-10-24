# Hackathon winners benchmark

Checked 2026-10-24. International study: **20 independently identified awarded projects**, including all nine requested examples and eleven additional winners/honorable mentions. Domestic research is maintained separately. This study examines public project descriptions and selected current repositories; it is not a replication study. An award validates placement, not every technical, safety, latency, market-size, or accuracy claim on a project page. Screenshots described on Devpost are evidence of presentation, not proof that a live integration works. Videos were not frame-audited, so their exact first 10/30 seconds and production timing remain unverified. Pitches below are our suggested reconstructions, not quotations from the videos.

## Award provenance

- **G3:** [Gemini 3 official winners announcement](https://gemini3.devpost.com/updates/40729-the-moment-you-ve-been-waiting-so-patiently-for). Globot grand prize, Aegis second, Netra third; ten explicitly named honorable mentions.
- **GL:** [Gemini Live official winners announcement](https://geminiliveagentchallenge.devpost.com/updates/41944-announcing-the-challenge-winners). ORION grand prize; live, UX, innovation, architecture, and creative categories identify the projects below.
- **AWS:** [AWS official winners announcement](https://aws-agent-hackathon.devpost.com/updates/38140-congratulations-to-the-winners-of-the-aws-ai-agent-global-hackathon). EcoLafaek first place.

## 1. Globot — G3 grand prize

[Project](https://devpost.com/software/globot-341w9q) · [Repository reviewed](https://github.com/Vector897/Globot)

- **Problem / 10-second pitch:** A shipping disruption creates fragmented operational and financial decisions. Suggested pitch: turn a supply-chain shock into a reviewed route response.
- **AI need / architecture / tools:** Five specialist perspectives coordinate news interpretation, financial exposure, logistics, document compliance, and adversarial review. The submission lists CrewAI, FastAPI, React, Deck.gl, and vector retrieval.
- **Workflow / data / UI:** Inspect a scenario, compare routes, review agent activity, then approve. Globe/map visualization and live logs make a complicated domain tangible.
- **Safety / explanation / fallback:** Critical actions require human review. Current README clearly labels default inputs mock/synthetic and optional integrations; full external-feed reliability was not reproduced.
- **Outcome / demo:** A scenario walkthrough is documented; production savings and early-warning performance are unverified. The current repository presents decision support rather than autonomous operational execution.
- **Packaging:** README exposes demo, setup, architecture, status, license, and limitations. Devpost uses crisis narrative → capability list → implementation → challenges.
- **Inference / use here:** Borrow the visible decision-to-action transition and accountable approval. Do not copy raw reasoning disclosure or treat roadmap Bloomberg/satellite integrations as verified runtime evidence.

## 2. Aegis — G3 second place

[Project](https://devpost.com/software/aegis-autonomous-multi-agent-crisis-command)

- **Problem / pitch:** Emergency reports overwhelm dispatch. Suggested pitch: prioritize a crisis stream and give a commander a verified action view.
- **AI / architecture / tools:** Specialized triage and surveillance prompts share a central coordinator. Next.js server actions support parallel streams; Maps and search ground reports.
- **Workflow / UI / trace:** A tactical map and priority panels expose the highest-priority incident rather than every model message. The project's spotlight approach directly addresses cognitive overload.
- **Data / explanation:** Search-backed locations and concise displayed justification are described. These explanations are product summaries; they are not evidence that the underlying reasoning is correct.
- **HITL / guardrail / fallback:** Protocol Zero escalates to a person. The reviewed narrative does not establish complete outage or retry behavior.
- **Outcome / demo:** Handoffs and verification are described, but dispatch-scale throughput was not independently reproduced. Exact video opening was not verified.
- **GitHub / README / Devpost:** A linked repository fetch failed; README and code quality remain unaudited. Devpost connects specific engineering challenges to the interface.
- **Inference / adoption:** A coherent live control surface can make multi-step AI understandable. Show Revslot's latest important action, with expandable audit details, instead of a wall of text.

## 3. Netra — G3 third place

[Project](https://devpost.com/software/netra-empowering-the-visually-impaired) · [Repository reviewed](https://github.com/ZentraHost/netra_project)

- **Problem / pitch:** Camera assistance often lacks continuity across daily tasks. Suggested pitch: ask a phone to find an object and guide the task to completion.
- **AI / tools / architecture:** Gemini multimodal processing connects scene questions, persistent object search, spatial memory, and visually checked task steps. FastAPI and WebSockets coordinate media.
- **Workflow / data / UI:** The smartphone camera is the primary input; audio guidance keeps interaction hands-free. Search and task modes show state continuity.
- **HITL / explanation / safety:** Users issue goals. The narrative discusses short hazard-response latency and concise speech, but clinical/accessibility safety validation is unverified. We would not copy intent-inference or safety guarantees.
- **Fallback / outcome:** A speech deduplication priority service is documented; robust offline capability remains a roadmap claim. Independent accuracy and safety measurements were not reproduced.
- **Packaging:** README provides features, stack, project structure, API-key configuration, and launch instructions. Devpost includes forceful judge-directed promotional claims; those are rhetoric, not a pattern to imitate.
- **Inference / use here:** A goal must persist through observation and completion. Revslot should keep one recovery attempt alive through repricing and booking, with no fabricated reliability claim.

## 4. ORION — GL grand prize

[Project](https://devpost.com/software/orion-operating-room-intelligent-orchestration-node)

- **Problem / pitch:** Surgeons with occupied hands cannot operate information systems easily. Suggested pitch: speak a request and see the relevant console panel act.
- **AI / architecture / tools:** A root ADK orchestrator routes voice intent to surgical-domain specialists. Gemini Live provides media and function calls; the page describes nine roles.
- **Workflow / UI / data:** Voice requests open clinical cards, imaging views, checklists, and timestamped records. The product aligns input modality with the user's physical constraint.
- **Safety / HITL / trace:** Tool callbacks and grounding hardening are described; the operator remains involved. Displayed log entries reveal actions without requiring transcript inspection.
- **Fallback / outcome:** Streaming error handling is stated, but latency and clinical efficacy were not independently reproduced. Roadmap explicitly calls for replacing synthetic records and hardcoded pharmacology with validated integrations.
- **Demo / packaging:** Console screenshots, architecture, live URL, videos, and repository link are listed. The repository fetch failed in this review; README quality remains unverified. Devpost moves from workflow constraint to visible tool actions.
- **Inference / adoption:** Make the value visible as a changed product state. Borrow purposeful tool routing; do not borrow medical scope, unsupported safety claims, or nine agents merely for symmetry.

## 5. drone-copilot — GL Best of Live Agents

[Project](https://devpost.com/software/drone-copilot) · [Repository reviewed](https://github.com/BryenInsights/drone-copilot)

- **Problem / pitch:** Conventional drone interaction is command-heavy. Suggested pitch: ask a drone to inspect an object and watch the inspection finish.
- **AI / architecture / tools:** A Cloud Run FastAPI relay holds a Gemini Live session; a local Python client dispatches structured commands to DJI Tello hardware and supplies video.
- **Workflow / UI / data:** Speak, observe physical action, receive confirmation and an inspection report. A dashboard combines mission status, live feed, and telemetry.
- **Explanation / HITL / safety:** The person starts interaction and directs missions. Pydantic constrains tool arguments, though a comprehensive safety envelope was not established by this documentary review.
- **Fallback / outcome:** Session resumption is described. Wind and hardware drift are openly acknowledged. The project narrative reports successful missions; we did not reproduce flights or measure response latency.
- **Demo / packaging:** README offers clearly labeled prerecorded mission replay without hardware, alongside live-flight architecture, dependencies, and setup. Devpost centers a memorable instruction-to-action moment.
- **Inference / adoption:** Design one unmistakable action/result scene and disclose replay status. Revslot's seeded business scenario can be repeatable while separately showing whether inference is live.

## 6. Wand — GL Best Multimodal Integration & UX

[Project](https://devpost.com/software/wand-a-live-agent-that-sees-browses-and-clicks-with-you)

- **Problem / pitch:** Speech alone cannot always identify a screen target. Suggested pitch: point to an element, say the task, and watch the browser act.
- **AI / architecture / tools:** Root, browser, and search roles coordinate through ADK. Cloud FastAPI reasoning connects to local media capture and a Playwright browser over WebSocket.
- **Data / workflow / UI:** Cursor coordinates and annotated screenshots give actions context. The local client resolves the freshest pointer position at execution time.
- **HITL / explanation / trace:** User speech and pointing initiate actions. The narrative describes transparent handoffs; a complete sensitive-action confirmation policy was not established.
- **Fallback / guardrail:** A transfer audio gate avoids stale chunks. Automatic reconnection starts a fresh session, with a manual reconnect option; context loss is an explicit limitation.
- **Outcome / demo:** Seamless interaction is recognized by the organizer, but browsing success rate was not independently measured. The exact opening sequence was not viewed.
- **Packaging:** Devpost ties failure symptoms to concrete fixes and lists a repository, whose fetch failed here; README remains unverified.
- **Inference / adoption:** Stale context is an execution risk. Before booking, revalidate the current slot, price revision, policy, and availability rather than trusting an earlier decision.

## 7. Rayan Memory — GL Best Innovation & Thought Leadership

[Project](https://devpost.com/software/rayan-memory) · [Repository reviewed](https://github.com/yelnady/rayan)

- **Problem / pitch:** Captured knowledge is difficult to recall. Suggested pitch: a spoken concept becomes an artifact in a walkable memory palace.
- **AI / architecture / tools:** Separate capture and recall agents use persistent live sessions, embeddings, memory tools, and web grounding. FastAPI pushes typed events into a React/Three.js environment.
- **Workflow / data / UI / trace:** Capture becomes visible as a scene mutation; recall highlights stored artifacts. Semantic deduplication prevents repeated material from cluttering the interface.
- **HITL / guardrail / explanation:** Confidence gates and retrieval citations are described. Claims of impossible hallucination are not proven by a prompt or retrieval requirement.
- **Fallback / outcome:** Heartbeats and exponential reconnection are documented. No controlled study of learning or recall benefit was reproduced.
- **Demo / packaging:** Spatial artifact creation supplies a visual before/after. README explains agent roles, stack, and local workflow; visible image/GIF placeholder text weakens completeness despite the concept's strength. Devpost devotes substantial space to interface engineering.
- **Inference / adoption:** Convert backend events into understandable visual changes. Revslot should show a listing, price revision, and recovered KPI immediately after the corresponding persisted tool action; avoid impossible certainty claims.

## 8. JohnKeats.AI — GL Best Technical Execution & Agent Architecture

[Project](https://devpost.com/software/johnkeats-ai) · [Repository reviewed](https://github.com/johnkeats-ai/johnkeats-ai)

- **Problem / pitch:** Some conversations require listening rather than immediate advice. Suggested pitch: a voice companion listens while a separate governed process improves its behavior.
- **AI / tools / architecture:** Gemini native audio serves the conversation; Firestore tools maintain memory. An independent calibration pipeline anonymizes, audits, scores, and proposes changes.
- **Workflow / UI / trace:** The main interface is a reactive orb. Operational pipeline views show anonymization, scores, and orchestrator output without burdening the conversation.
- **HITL / guardrail / explanation:** A deterministic policy gate and human approval restrict proposed calibrations. User isolation and privacy processing are described, not independently security-audited.
- **Fallback / outcome:** Core conversation does not depend on calibration availability. The author reports 18 processed conversations and approved/rejected recommendations; this is a small demonstration, not clinical validation.
- **Demo / packaging:** README leads with live demo/video, then architecture, setup, pipeline operation, and deployment. Devpost explains both the product premise and concrete governance.
- **Inference / adoption:** Separate availability of the core workflow from optional enrichment. Revslot can continue deterministic recovery when external context fails and must gate uncertain model decisions explicitly.

## 9. EcoLafaek — AWS first place

[Project](https://devpost.com/software/ecolafaek)

- **Problem / pitch:** Waste reports do not automatically become actionable municipal evidence. Suggested pitch: a citizen photograph becomes a classified report and a hotspot insight.
- **AI / architecture / tools:** Bedrock Nova-Pro interprets images; AgentCore chains SQL, Python charts, maps, browser retrieval, and project-information tools. A separate embedding path enables similarity search.
- **Workflow / UI / data:** Mobile reporting feeds a public dashboard and restricted administration. Geospatial plots connect individual evidence to operational patterns.
- **HITL / guardrail / trace:** Administrative moderation and a local-only admin boundary are described. Tool sequences and sandbox testing are shown; comprehensive security was not reproduced.
- **Fallback / outcome:** Mobile offline caching and API rate limits appear in the architecture. The organizer recognizes the end-to-end solution; actual cleanup reductions were not independently established.
- **Demo / packaging:** Devpost includes architecture, schema, component documentation, screenshots, and a linked repository. Repository fetch failed during this review; code and README quality remain unverified. Public reporting and authority analytics form one coherent story.
- **Inference / adoption:** A multi-sided product needs an end-to-end handoff. Revslot must connect merchant cancellation, consumer reservation, and merchant revenue accounting, rather than demonstrating isolated agent calls.

## 10. Sankofa — GL Best of Creative Storytellers

[Project](https://devpost.com/software/sankofa-y47f9p) · [Linked code](https://github.com/Jeremiah-Sakuda/Sankofa)

- **Problem / pitch:** Heritage fragments lack an accessible narrative experience. Suggested pitch: turn family-history seeds into a sourced story you can hear and explore.
- **AI / architecture / tools:** An ADK narrative agent uses nine tools, including arc validation and enrichment; a second agent serves live conversation. Separate models generate text, images, speech, and live responses.
- **Workflow / UI / data / trace:** Segments stream through SSE with concurrent audio work. Knowledge-base richness changes research behavior. User-visible status tools explain progress.
- **HITL / guardrail / explanation:** Historical, cultural, and reconstructed labels distinguish evidence from imagination. A user supplies initial context; no formal approval gate is established.
- **Fallback / outcome:** Validation can trigger replanning. Chunking mitigates generation delay; performance claims are author-reported and not independently timed.
- **Demo / packaging:** A lengthy cinematic opening masks backend work. Devpost explains orchestration, latency fixes, licensing, and deployment; linked README was not audited here.
- **Inference / adoption:** Provenance can improve rather than damage trust. Use persistent synthetic/live labels. Revslot should avoid a long cinematic loading scene because its own value must appear within the first 30 seconds.

## 11. AgentGuard — G3 honorable mention

[Project](https://devpost.com/software/agentguard-the-semantic-firewall-for-the-agentic-web)

- **Problem / pitch:** A merchant cannot easily distinguish useful agents from abusive bots. Suggested pitch: inspect behavior and produce an auditable traffic verdict.
- **AI / architecture / tools:** Structured telemetry reaches Gemini through FastAPI; novel patterns receive model analysis while a cache handles repeated verdicts. React presents a command-center dashboard.
- **Workflow / UI / data / trace:** A telemetry generator supplies demonstration traffic. Allowed, blocked, and restricted states are visible with concise explanations.
- **HITL / guardrail / explanation:** Structured outputs and explicit rules constrain verdicts. A human security team can inspect decisions; a formal approval boundary is not established in the reviewed excerpt.
- **Fallback / outcome:** Caching addresses the cost and latency problem. Advertised latency, cache percentage, and security effectiveness were not independently benchmarked and must not be adopted as facts.
- **Demo / packaging:** The narrative explicitly describes simulated traffic, plus problem/solution/flow/testing illustrations. Repository and README were not audited; deployment and license quality remain unverified.
- **Inference / adoption:** Cache stable context, not stale availability or price authorization. Adopt structured action summaries and an explicit simulation label; test fallback and expiry behavior rather than inheriting performance claims from an award.

## 12. BatteryForgeAI — G3 honorable mention

[Project](https://devpost.com/software/batteryforgeai)

- **Problem / pitch:** Battery engineers juggle defects, charging, and fleet risks. Suggested pitch: turn battery evidence into an inspection and simulation workflow.
- **AI / architecture / tools:** An ADK commander routes to five specialists. FastAPI services connect vision, PyBaMM physics simulation, impedance analysis, and document retrieval; the page lists more than 20 tools.
- **Workflow / data / UI / trace:** CSVs and visual inputs feed inspection and fleet views. Recharts displays physical curves; WebSocket events expose agent activity and persistent histories.
- **HITL / guardrail / explanation:** A safety role and human-in-the-loop controls are described. Their real emergency effectiveness is not independently validated.
- **Fallback / outcome:** The reviewed narrative does not establish comprehensive retry, containment, or degraded-mode behavior. Manufacturing and battery-lifetime impact remain unverified.
- **Demo / packaging:** Scientific plots and component screenshots connect analysis to tangible outputs. Devpost organizes capabilities by engineering domain. GitHub, README, and repeatable evaluation were not audited here.
- **Inference / adoption:** Use domain computation as a tool rather than asking an LLM to invent numeric answers. Borrow the deterministic-tool boundary; the large feature surface and agent count are unsuitable for this six-day MVP.

## 13. Logic Lift — G3 honorable mention

[Project](https://devpost.com/software/the-bunny-ear-adventure)

- **Problem / pitch:** Legacy COBOL contains difficult-to-recover business logic. Suggested pitch: recover a business rule, modernize it, and inspect parity evidence.
- **AI / architecture / tools:** Gemini interprets legacy source and produces Python plus tests; React/TypeScript provides reports and a browser-oriented verification workflow.
- **Workflow / UI / data / trace:** Modules move through a processing queue and system stream. Blueprint and impact reports aim to make modernization visible.
- **HITL / guardrail / explanation:** Generated code and verification artifacts support human inspection; a mandatory approval step is not established in the reviewed description.
- **Fallback / outcome:** Skip/next handling prevents one module from stalling the pipeline. The page mixes simulated verification, Pyodide execution claims, and future live sandbox work; parity and completion percentages are therefore not treated as reproduced evidence.
- **Demo / packaging:** Devpost emphasizes business meaning and specific engineering failures. Its URL retains an older unrelated slug, illustrating why identity must follow official award links. README was not audited.
- **Inference / adoption:** Make failure recovery explicit and distinguish executable evidence from simulated results. Revslot should publish reproducible test outputs and never imply a simulated counterfactual proves real merchant uplift.

## 14. PROCSee — G3 honorable mention

[Project](https://devpost.com/software/procsee)

- **Problem / pitch:** Short-lived suspicious processes can vanish before investigation. Suggested pitch: capture the evidence and let an investigator query what happened next.
- **AI / architecture / tools:** FastAPI, SQLite, event capture, and Gemini coordinate self-directed process, time-range, pattern, network, and file queries.
- **Workflow / data / UI / trace:** Behavior triggers investigation; periodic monitoring can request additional evidence. A React dashboard shows status, query history, evidence timeline, and reports.
- **HITL / guardrail / explanation:** Integrity hashing and recorded queries make evidence inspectable. A documented action-approval boundary was not established in this review.
- **Fallback / outcome:** WAL storage, phase checkpoints, and restart resumption are explicit engineering features. Advertised detection coverage and sub-10-ms capture are not independently verified.
- **Demo / packaging:** The project description explains storage, query protocol, monitoring modes, and implementation sequence. GitHub, README, and production deployment were not audited. Exact video timing remains unknown.
- **Inference / adoption:** Durable state belongs at every phase boundary. Revslot should deduplicate cancellation events, resume attempts, and preserve an audit history. Show tool arguments/results summaries; do not copy disclosure of raw private model reasoning.

## 15. Proofy.AI — G3 honorable mention

[Project](https://devpost.com/software/fakey-ai)

- **Problem / pitch:** Ordinary users need a usable way to investigate suspicious media. Suggested pitch: inspect content where it appears and see evidence behind a flag.
- **AI / architecture / tools:** Mobile, extension, and web experiences share detection logic. The public narrative covers visual, audio, text, and source analysis but does not establish a detailed independently verified agent/tool graph.
- **Workflow / data / UI:** Users capture a screen or submit material; frame-level and batch views present flagged sections, confidence indicators, and exportable analysis.
- **HITL / guardrail / explanation:** The user inspects results. No mandatory human adjudication or validated forensic threshold is established by the reviewed material.
- **Fallback / outcome:** Handling overlays, compressed inputs, and Android permissions is discussed. Detection reliability, false-positive rates, and adversarial robustness were not reproduced.
- **Demo / packaging:** Screenshots illustrate entry, loading, results, and source discovery. Devpost anchors the idea in a personal scam incident. Linked repository and README quality were not audited; older product naming remains in the URL.
- **Inference / adoption:** The result explanation and usable context matter, but confidence is not proof. Revslot should show model limitations and prediction provenance instead of presenting synthetic conversion estimates as validated forecasts.

## 16. Agent-weaver — G3 honorable mention

[Project](https://devpost.com/software/agent-weaver)

- **Problem / pitch:** Coding agents repeat work and lose shared context. Suggested pitch: one verified code insight becomes reusable team memory.
- **AI / architecture / tools:** Five roles share persistent JSON state; an MCP server exposes 55 tools across modules. AST indexing supplies source structure, while model enrichment adds semantic descriptions.
- **Workflow / data / UI / trace:** Human-verified annotations and git-backed memory connect individual analysis to team use. A Next.js SSE dashboard displays agent activity; a hub synchronizes repository/branch snapshots.
- **HITL / guardrail / explanation:** Human verification marks trusted knowledge. This is a meaningful review checkpoint; it does not establish that all generated code is correct.
- **Fallback / outcome:** Session persistence is central. Full conflict resolution and outage behavior were not reproduced. Reported one-shot improvement is author-reported; a benchmark suite is future work.
- **Demo / packaging:** The story moves from context loss to shared memory, architecture, and observed limitations. Repository and README were not audited during this bounded research pass.
- **Inference / adoption:** Persist decisions and inputs across attempts. Tool count is not an objective. Revslot needs only tools that execute a necessary recovery step, with one owner for each role and a clear state contract.

## 17. Orbital Assets — G3 honorable mention

[Project](https://devpost.com/software/orbital-assets)

- **Problem / pitch:** Asteroid valuations often ignore physical and economic limits. Suggested pitch: turn NASA data into an inspectable investment memorandum.
- **AI / architecture / tools:** NASA SBDB supplies inputs. A deterministic TypeScript library calculates accessibility and valuation; Gemini produces qualitative risk analysis and narrative. Next.js and 3D assets support inspection.
- **Workflow / data / UI / trace:** A URL initiates retrieval, calculation, report generation, and optional delivery. Physical models and streamed progress give an abstract workflow a visible result.
- **HITL / guardrail / explanation:** Numeric valuation is separated from generative output. Human review is implied by the report use case; no mandatory investment approval gate is established.
- **Fallback / outcome:** Missing-input heuristics are described. Valuation assumptions, inferred composition, and commercial viability are not validated by this benchmark.
- **Demo / packaging:** Devpost explicitly explains mathematical versus model responsibilities and lists challenges. Repository/README were not audited. No real investment outcome was reproduced.
- **Inference / adoption:** This is the closest architectural analogue to Revslot's pricing boundary. Keep money calculations deterministic and record assumptions; let the model interpret context, select allowed tools, and explain an already computed choice.

## 18. CineStream — G3 honorable mention

[Project](https://devpost.com/software/cinestream-a2a-mesh-cinematic-learning)

- **Problem / pitch:** Static information can be difficult to learn or coordinate around. Suggested pitch: turn complex material into an interactive strategy or learning narrative.
- **AI / architecture / tools:** Flash models coordinate specialist perspectives; Pro handles trade-off analysis. The narrative describes agent-to-agent orchestration and multimodal output, but does not provide a complete independently verified tool graph.
- **Workflow / data / UI / trace:** Mission, audience, script, and sound views make generation stages visible. Inputs include dense documents and educational material.
- **HITL / guardrail / explanation:** A user frames the mission; explicit sensitive-action approval and deterministic numerical enforcement are not established by the reviewed material.
- **Fallback / outcome:** Free-tier cost and stability constraints motivated a smaller media scope. Learning retention and enterprise time-saving claims were not reproduced.
- **Demo / packaging:** Devpost gives a personal motivation, two product pillars, model responsibilities, and development constraints. The try link points to AI Studio; public GitHub and README quality were not established in this review.
- **Inference / adoption:** Match model size to latency and cost. Avoid copying its broad dual-purpose scope: Revslot's merchant-to-consumer recovery loop must remain the single narrative, with a direct outcome before architecture detail.

## 19. OrphaFold — G3 honorable mention

[Project](https://devpost.com/software/orphafold)

- **Problem / pitch:** Rare-disease research spans disconnected databases. Suggested pitch: assemble clinical, molecular, and literature evidence into a sourced research hypothesis.
- **AI / architecture / tools:** Four specialist roles enrich information from Orphanet, OMIM, UniProt, AlphaFold, ClinVar, PubMed, and trial records before synthesizing hypotheses.
- **Workflow / data / UI / trace:** Clinical grounding precedes mechanism analysis, discovery, and hypothesis work. Structural visualization and bibliography exports give researchers inspectable artifacts.
- **HITL / guardrail / explanation:** A preflight data layer grounds model context in identifiers and citations. Research hypotheses remain subject to expert validation; a formal approval stage was not established.
- **Fallback / outcome:** Parallel enrichment addresses latency, but complete upstream-failure behavior is unknown. Drug efficacy and binding predictions were not independently validated; docking is described as future work.
- **Demo / packaging:** Devpost separates component responsibilities, data sources, challenges, and next steps. A live application and GitHub are linked; README was not audited in this pass.
- **Inference / adoption:** Fetch reliable inputs before synthesis and retain their provenance. Revslot should treat local-event context as weak evidence, never as permission to invent demand or bypass merchant limits.

## 20. Gemini GeoFlow — G3 honorable mention

[Project](https://devpost.com/software/gemini-geoflow)

- **Problem / pitch:** Archaeologists manually connect papers, coordinates, and imagery. Suggested pitch: upload a paper and inspect a sourced satellite-analysis map.
- **AI / architecture / tools:** Gemini extracts structured site metadata, interprets composites, and performs grounded research. Earth Engine unifies satellite and elevation inputs; Maps and Flask support delivery.
- **Workflow / data / UI / trace:** PDF extraction leads to imagery retrieval, analysis, contextual research, visualization, and downloadable data. Validation and confidence appear throughout the documented workflow.
- **HITL / guardrail / explanation:** Domain expertise shaped requirements; citations and structured outputs aid review. A formal action-approval stage was not established.
- **Fallback / outcome:** Consolidating fragmented sources reduces authentication complexity. Field-survey accuracy and archaeological discovery impact were not reproduced; later ground-truth learning remains a roadmap.
- **Demo / packaging:** Devpost explains domain interviews, data choices, coordinate-format challenges, stack, and deployment. Docker/Compose and GitHub are listed, but README and local reproducibility were not audited here.
- **Inference / adoption:** Integration quality can matter more than adding tools. Use one coherent data contract and structured source summaries. Revslot's simulation must clearly separate observed synthetic outcomes from estimated future real-world performance.

## Cross-project comparison and exclusions

| Dimension | Observed pattern | Decision for Revslot |
|---|---|---|
| Problem | Specific constrained user and workflow recur; not universal chat | Merchant cancellation with an expiring slot |
| Agent role | Specialist roles vary greatly in number | Role clarity; no agent-count target |
| Action | Physical move, UI change, query, artifact creation | Persist offer → revised price → booking |
| Numeric trust | Orbital Assets separates math; battery work uses physics | Deterministic expected-revenue optimizer |
| Observability | Maps, mission states, timelines, artifacts | Concise action timeline plus audit details |
| Human control | Some explicit approval gates; many not established | Policy threshold, confidence gate, autopilot switch |
| Reliability | Reconnect, checkpoint, cache, retry patterns are described unevenly | Implement and test own failure paths |
| Evidence | Many impact claims lack reproduced benchmarks | Publish synthetic methodology and actual test results |
| Presentation | Narrative plus visible artifact; broad scope can obscure result | First 30 seconds: cancellation → action → revenue |

The official placement list is evidence of awards. Suggested winning factors above are **inferences**, not recovered judging deliberations or causal explanations. No evidence supports a universal requirement for many agents, a fixed tool count, raw chain-of-thought disclosure, or inflated performance language. The twelve-month development maturity of a current repository must not be confused with its state at judging.
