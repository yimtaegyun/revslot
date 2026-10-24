# Domestic benchmark — verified scope and limits

Checked: 2026-10-24 (Asia/Seoul). Research supports product decisions; an award does not independently validate an entrant's technical or commercial claims. **Facts**, **author reports**, and **our design inferences** are separated. An unavailable architecture, recording, metric, or repository is marked unverified rather than reconstructed.

## Findings that change this product

1. **FineHost is directly adjacent.** End-to-end agentic revenue management already exists as a publicly described award project. Do not pitch agentic pricing itself as unprecedented.
2. Domestic finalists show a useful pattern: a narrow operational problem, a recognizable end user, and a visible outcome. Revslot should show one cancelled appointment becoming one confirmed booking, with the accounting following the actual state change.
3. A public leaderboard position, public vote, entrant's award claim, and official final award are different evidence classes. They are not interchangeable below.

## Official AI Champion Competition winners: five confirmed projects

The following concise factual digest derives from the [MSIT official award announcement][D1]. Its top five are confirmed; the public article is not a code audit.

| Project | Official result | Confirmed problem / technology |
| --- | --- | --- |
| AutoPhone | 2025 AI Champion, first | Mobile agent operates apps from commands; follow-up work targets an on-device action model. |
| Stratio Korea | AI Innovator, second | Infrared multispectral recognition for material identification and recycling sorting. |
| Revivo | AI Challenger, top five | Vehicle condition diagnosis with modular sensors, 3D reconstruction, semantic fusion, and repair-cost estimation. |
| SafeAngel | AI Challenger; popular-vote award | Industrial hearing protection; anomaly detection, on-device voice guidance, and active noise control. |
| FineHost / Vacatio | AI Challenger, top five | Hospitality operations from voice: booking, pricing, inventory, reviews; LangGraph agents and multilingual revenue management. |

D1 describes staged live demonstrations and presentations. It does not disclose per-project source repositories, complete tool inventories, latencies, independently measured accuracy, customer counts, or production revenue.

### A. AutoPhone — design interpretation

**Suggested ten-second framing:** ask for a task; watch the relevant app operations happen. This is our framing, not a recovered quotation from its pitch. The transferable pattern is a user-visible action boundary: an app action is stronger evidence than a generated answer. For Revslot, that boundary is publishing a permitted offer and then confirming a reservation.

Architecture and guardrails beyond the digest, internal action traces, approval points, failure handling, model details, repository quality, and README structure were not verified from D1. Do not infer that autonomous mobile operation is risk-free. **Adopt:** show the state before and after each business action and make irreversible actions require permission. **Judge relevance:** implementation and coherent user experience. **Outcome we can substantiate:** award result; operational performance remains unverified.

### B. Stratio Korea — design interpretation

**Suggested framing:** a specific sensing limitation prevents reliable sorting; a better signal changes the sorting decision. Its useful lesson is to match the technical method to the actual bottleneck. For Revslot, a deterministic numerical optimizer is more appropriate for prices than unconstrained language generation.

No public project UI walkthrough, API contract, model score, source audit, failure policy, or end-to-end action log was verified in this pass. **Adopt:** explicitly distinguish raw observations from derived signals. Tavily context should be attributed, low-weight, optional evidence rather than an unexplained demand fact. **Judge relevance:** credible technical fit and problem understanding. The recycling application's award is not evidence that our appointment pricing works.

### C. Revivo — design interpretation

**Suggested framing:** one inspection produces a condition assessment and a cost estimate. The transferable product idea is to join several processing steps around a concrete decision, rather than expose a collection of unrelated AI features.

Source code, exact model versions, inference costs, screen design, human override, audit details, error recovery, and prediction quality were not publicly verified here. **Adopt:** use one cancellation identifier across feature extraction, price evaluation, policy checking, offer publication, and booking outcome. A reviewer should follow a single record through the system. **Judge relevance:** complete workflow and practical impact. **Measurable target for Revslot:** time to decision, fill, recovered cash, and discount cost, measured by code rather than narration.

### D. SafeAngel — design interpretation

**Suggested framing:** industrial noise should not prevent a worker from hearing useful guidance. This is an example of an operational setting that makes reliability and human consequences part of the product.

The public announcement does not establish specific safety certification, production deployments, an agent count, or a verified fallback design. **Adopt:** represent degraded operation honestly; when demand confidence is low, recommend rather than execute. Do not turn uncertainty into a reassuring percentage without an empirical basis. **Judge relevance:** impact and responsible execution. **UI lesson:** exception states deserve an explicit label and a clear next action.

### E. FineHost — closest domestic architecture precedent

**Suggested framing:** a hospitality operator gives one instruction and operational agents coordinate the work. LangGraph and revenue operations are confirmed in D1; the exact graph, conflict-resolution policy, revenue lift, screens, and public GitHub were not verified.

**Our inference:** role separation is useful when it prevents conflicting changes to inventory or rates. It is not useful merely to increase the agent count. **Adopt:** one authoritative slot state, deterministic policy checks before publication, idempotent booking, and a complete audit trail. **Positioning constraint:** Revslot focuses on beauty/wellness cancellation recovery with explicit merchant limits and visible price/audience/channel iteration; it must not claim to invent autonomous revenue management. **Judge relevance:** technological implementation and completeness. D1's award statement is not a head-to-head benchmark against Revslot.

## NIA / Ministry of the Interior AI Champion Hackathon (2026)

The [NIA public-data newsletter][D2] gives a result table. This is a **different event** from the MSIT competition above. The [official government demonstration transcript][D3] provides a deeper account of its grand-prize service.

| Project / team | Confirmed result and product | Verified limits | Lesson for Revslot (inference) |
| --- | --- | --- | --- |
| 쨍하고 해뜰날 / 동동즈, LX | Grand prize; solar-installation suitability and revenue guidance. D3 describes address API, V-WORLD and land, terrain, weather, grid and ordinance data. | No audited public code, correctness rate, or complete agent graph was inspected. The later government demo is an evolved version, not proof every later feature existed during the hackathon. | One input, tool-backed analysis, visible map/result, and constraint explanation make a complex workflow legible. |
| 아빠GO / 아들넷딸둘 | Highest excellence award; game-like exploration of a relocation destination to reduce children's anxiety. [D2] | Architecture, model, UI recording, performance and repository unverified. | Shape the interface around the user's actual decision rather than a chat box by default. |
| 대국민 지역정착 / 보듬 | Excellence plus special award; eligibility checking and application support for local support programmes. [D2] | No verified execution permissions, API list, agent count, or application-completion metric. | Show eligibility before offering an action; distinguish a recommendation from a completed transaction. |
| 우리집 / 이어드림 | Excellence award; settlement diagnosis, unclaimed support discovery and local-government connection. [D2] | No independently inspected UI, source or error recovery. | Connect discovery to a next action and make status explicit. |

**Demo / explanation pattern inferred from D3:** an address-driven workflow is easy to demonstrate because the input, context sources, constraints, analysis and output are visible. Revslot's equivalent is cancellation → candidate-price table → policy check → offer → booking receipt. Do not borrow governmental credibility or imply a partnership.

## K Intelligence Hackathon 2025

[KT's winner interview][D4] confirms **박현재, Track 2 grand prize**, with an interactive history-learning service using SOTA K and RAG. [KT's organizer retrospective][D5] distinguishes Track 1 B2B/B2G agents using 믿:음 K 2.0 from Track 2 prompt/service work.

- **Problem and ten-second framing:** students ask historical questions and receive explanations grounded in retrieved material. The framing is our interpretation.
- **AI necessity:** language interaction and retrieval-supported explanation, rather than a static list of history facts.
- **Verified tools / autonomy:** SOTA K and RAG; an autonomous business-action loop was not established.
- **UI / demo / data:** conversational education and grounding are described by KT. Exact data licensing, repository, full tool trace, fallback and measured classroom outcomes were not audited.
- **README / Devpost:** no verified public code/Devpost structure in the retrieved material. Do not turn an organizer interview into a source-code-quality score.
- **Adopt:** require source-backed local context and evaluate whether the model response changes a meaningful action. **Judge connection (inference):** a specific audience and an understandable use case help impact claims.

## DACON service-development case

The [2025 SW-centred university SW-track leaderboard][D6] lists **말벗 / 말:뻗**, an articulation-training service, first in the displayed ranking. Its [official project post][D7] provides a demo link and YouTube link. This is a **verified public project/ranking**, not a verified final jury-award declaration; the displayed ranking includes voting and a score.

- **Problem:** articulation practice. **Suggested ten-second framing:** open the app and perform a short exercise.
- **Verified submission pattern:** one project post links the live demonstration and video; this is useful submission hygiene.
- **Unverified:** actual model, architecture, tools, training corpus, clinical validity, action trace, reliability metric, guardrails, source code quality and final award. The linked demo was not used to assert these.
- **Adopt:** keep the submission entry navigable, with a short video and directly testable workflow. Revslot's portfolio should give the reviewer an immediate cancellation scenario and a reset control.
- **Avoid:** claiming clinical effectiveness or copying a medical scope. Revslot excludes medical bookings.

A separate [smart-manufacturing AI-agent competition brief][D8] confirms that a service-development event requested role-defined cooperating agents and a working MVP. Its winner list was not verified in this pass, so no fabricated winner is added.

## Big Contest

The [author's PetJJu project report][D9] describes a Jeju pet-friendly travel/restaurant recommender, map interface, personalization and an attached presentation/demo, and reports a 2024 generative-AI excellence award. **Status: entrant-reported award, not independently reconciled with an organizer final-result list.** Its architecture and measured effectiveness are not independently verified.

A [team-authored public GitHub discussion][D10] links the **잘도 맛있수다** demo and repository. The [team member's award account][D11] reports the grand prize and names LangGraph, LangChain, Streamlit, Neo4j, GraphRAG, HyDE and Text2Cypher. **Status: author-primary technical account; award corroboration by organizer remains incomplete.** The repository open returned an error during this pass; it therefore receives no code-quality score.

**Transferable inference:** context-sensitive discovery benefits from a map and source grounding, but an elaborate retrieval stack is not automatically necessary for a numerical booking optimizer. Revslot should use Tavily for optional context and keep prices in deterministic code. A polished demo does not validate recommendation accuracy. The official Big Contest notice archive was reached but did not expose a usable final-result body in retrieval; this limitation is retained rather than replaced with a guessed ranking.

## SeSAC generative-AI hackathon

The [Seoul municipal event video transcript][D12] confirms **이즈리드** as the 2024 grand-prize team. [The official recruitment page][D13] confirms the generative-AI/social-inclusion theme. **Project function and architecture unverified:** neither the team name nor the theme proves that it was a dyslexia or reading service. No such guess is recorded.

The useful observed submission pattern is a live, publicly understandable demonstration and award ceremony. **Inference for Revslot:** the first half-minute must be understandable to a merchant, not only to an agent-framework developer. No claim about this project's model, repository, metrics, guardrails, or exact UI is supported by the retrieved sources.

## Coverage and adoption checklist

| Requested category | Evidence status |
| --- | --- |
| AI Champion Competition and FineHost | Five official winners; FineHost architecture scope confirmed. |
| NIA AI Champion Hackathon | Four named official winners sampled; deeper grand-prize demonstration verified. |
| DACON service-development agent projects | Public SW project/ranking and agent-MVP brief verified; final jury award for the sampled SW project not verified. |
| Big Contest | Author-primary projects and award accounts; official final-result reconciliation incomplete. |
| K Intelligence | Organizer-confirmed Track 2 grand prize; exact technical performance unverified. |
| SeSAC | Grand-prize team verified through city video; product details not inferred. |

**Do now:** maintain one authoritative state machine, visible tool/action events, constrained pricing, explicit approval, reliable reset, and a complete submission page. **Do not adopt:** unsupported winner metrics, a large swarm, an unneeded retrieval stack, or claims of commercial traction.

## Sources

[D1]: https://www.msit.go.kr/eng/bbs/view.do?bbsSeqNo=42&mId=4&nttSeqNo=1188&sCode=eng
[D2]: https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?bcIdx=29624&cbIdx=27974
[D3]: https://m.korea.kr/briefing/policyBriefingView.do?newsId=156775445
[D4]: https://kode.kt.com/blog/article/10218
[D5]: https://kode.kt.com/blog/article/8409
[D6]: https://dacon.io/competitions/official/236474/leaderboard
[D7]: https://dacon.io/competitions/official/236474/codeshare/12583
[D8]: https://dacon.io/competitions/official/236652/overview/description
[D9]: https://minsunstudio.tistory.com/59
[D10]: https://github.com/Pseudo-Lab/life-is-short-you-need-recommendation-system/discussions/20
[D11]: https://kr.linkedin.com/posts/nahcklee_%EB%B9%85%EC%BD%98%ED%85%8C%EC%8A%A4%ED%8A%B8-2024-%EC%83%9D%EC%84%B1%ED%98%95-ai%EB%B6%84%EC%95%BC-%EA%B3%BC%EA%B8%B0%EC%A0%95%ED%86%B5%EB%B6%80-%EC%9E%A5%EA%B4%80%EC%83%81%EB%8C%80%EC%83%81-%EC%88%98%EC%83%81-%ED%9B%84%EA%B8%B0-activity-7274365024117145600-HtbS
[D12]: https://tv.seoul.go.kr/v/dc6eac09a0274eaba2ea073e1b51f145
[D13]: https://mediahub.seoul.go.kr/gongmo/2000536
