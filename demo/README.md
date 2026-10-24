# Actual browser evidence

[Successful verification](https://github.com/yimtaegyun/revslot/actions/runs/40064620041) ran the real Next.js production build and FastAPI at commit `574de1d52a5bc8d185a20df08e9ca7e45833e88e`: 34 Python tests and 3 browser tests passed. All business/customer data is synthetic. Provider keys were absent; these captures show the labeled rules preview. No real revenue, inference or customer claim is implied.

The [raw workflow recording](browser-workflow.webm) is 7.64 seconds of the actual browser test. It is verification evidence, not the final narrated submission video. A separate 2:50 silent, captioned review film was rendered from these captures. [Rendering source](render_review_video.py), [final narration script](VIDEO_SCRIPT.md), [shot list](SHOT_LIST.md), [checksums/log excerpts](../docs/QA_EVIDENCE.json).

| Capture | Actual state |
|---|---|
| [Merchant ready](screenshots/01-merchant-ready.png) | Fictional $80 appointment before cancellation |
| [Initial offer](screenshots/02-agent-first-offer.png) | $64, 12 profiles, 3 km, actual tool/action trace |
| [Repricing](screenshots/03-reprice.png) | Unsold +20 demo minutes; $56, 24 profiles, 6 km |
| [Marketplace](screenshots/04-marketplace.png) | One shared $56 offer; sandbox reservation |
| [Recovered](screenshots/05-recovered.png) | Confirmed booking; $56, 70%, 20 demo minutes |
| [Analytics](screenshots/06-analytics.png) | All four policies and unfavorable metrics |
| [Guardrails](screenshots/07-guardrails.png) | Merchant settings and non-overridable protections |
| [Mobile](screenshots/08-mobile.png) | 390px viewport, working navigation, no page overflow |
| [Provenance](screenshots/09-integrations.png) | Both providers explicitly unconfigured |

The README hero is a crop of the actual recovered screenshot. Other source captures are unmodified. No generated UI frame is used. Final eligible capture must show a real successful NVIDIA call through Nebius and anonymous live hosting; the public YouTube and Devpost gates remain open.
