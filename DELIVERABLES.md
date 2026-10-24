# Revslot deliverables and open gates

This index distinguishes a concrete implementation/draft from verified external delivery. The project is **not yet submitted or fully eligible**.

| Requested item | Artifact / actual status |
|---|---|
| Final name / pitch | Revslot — autonomous recovery for cancelled beauty/wellness appointments |
| Public source | https://github.com/yimtaegyun/revslot (code, research and documentation published; verified commit in PROJECT_STATE.md) |
| Live app URL | https://revslot-one.vercel.app/ — anonymous API and browser workflow verified; labeled rules preview, ephemeral state/manual clock |
| README | [README.md](README.md) |
| Architecture / agent roles | [Architecture](docs/ARCHITECTURE.md), [SVG](docs/architecture.svg), [workflow](docs/AGENT_WORKFLOW.md) |
| Screenshots / browser video | [Nine actual inspected captures and raw workflow recording](demo/README.md); [passing CI](https://github.com/yimtaegyun/revslot/actions/runs/40089803664) |
| Synthetic generator / dataset | [Generator](scripts/generate_data.py), [data card](data/DATA_CARD.json), compressed data in `data/` |
| Evaluation / comparison | [Report](docs/EVALUATION_REPORT.md), [results](simulation/results.json), development failures retained |
| Demo scenario / script / shots | [Scenario](docs/DEMO_SCENARIO.md), [2:50 script](demo/VIDEO_SCRIPT.md), [shots](demo/SHOT_LIST.md) |
| Review video / final YouTube | 1920×1080,2:50 silent captioned review rendered from actual screenshots and delivered privately; [rendering source](demo/render_review_video.py). Final live-provider/narrated public YouTube remains pending. |
| Devpost text / Built With | [Draft](demo/DEVPOST.md), [technology list](demo/BUILT_WITH.md) |
| Sponsor feedback | [Evidence-aware feedback draft](demo/FEEDBACK.md); actual usage feedback pending |
| Safety / pricing | [Guardrails](docs/SAFETY_AND_GUARDRAILS.md), [model card](docs/PRICING_ENGINE.md) |
| Limitations / roadmap / business questions | [README](README.md), [competitive FAQ](docs/COMPETITIVE_FAQ.md) |
| Job portfolio / resume / STAR / detailed article | [Korean portfolio notes](docs/PORTFOLIO_KO.md), [full development article](docs/BLOG_KO.md) |
| Rules / research | [Rules](docs/HACKATHON_RULES_VERIFIED.md), [20 overseas cases](research/HACKATHON_WINNERS_BENCHMARK.md), [domestic](research/DOMESTIC_BENCHMARK.md), [competitors](research/COMPETITOR_MATRIX.md), [patterns](research/WINNING_PATTERNS.md) |
| Current state / resume work | [PROJECT_STATE.md](PROJECT_STATE.md), [HANDOFF.md](HANDOFF.md), [decisions](docs/DECISIONS.md) |
| Final submission | [Open checklist](demo/SUBMISSION_CHECKLIST.md); user acceptance and final submission not performed |

Runtime secrets are absent. A mocked unit test or rules preview does not satisfy the official NVIDIA-on-Nebius requirement. No payment, legal acceptance, real outreach or commercial claim has been made.
