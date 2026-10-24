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

## Server monitoring update

[CI 40089803664](https://github.com/yimtaegyun/revslot/actions/runs/40089803664) verified42 Python tests (real PostgreSQL 17), production build and 4 Chromium cases. The new case closes all pages, waits while the server reprices, then reopens to confirm $56. [Before closure](server-clock-before-close.webm) and [after reopening](server-clock-after-reopen.webm) are separate unedited page recordings; the interval with no browser page is established by the test assertion and read-only state observation, not a fabricated continuous screen recording. The earlier screenshot set remains tied to its original capture commit.

## Public browser verification

[Public preview](https://revslot-one.vercel.app/) passed an anonymous API sequence and an independent visible browser reservation flow. [Actual live-browser result](screenshots/11-live-browser.jpg), [deployment evidence](../docs/LIVE_DEPLOYMENT_EVIDENCE.json). That first public capture used ephemeral SQLite and manual advance. The current deployment uses Neon PostgreSQL and actual hosted scheduling, verified separately below.


## Hosted Neon verification

A $56 reservation survived a Vercel redeployment with its revision unchanged. A separate API-only session received no mutation after starting the clock: the real Neon schedule repriced $64 to$56 and expanded reach to6km after13.27 real seconds. Native function logs independently recorded6 calls /1 processed job /0 failures. [Detailed evidence](../docs/NEON_DEPLOYMENT_EVIDENCE.json).

The [latest visible public browser capture](screenshots/12-live-neon-scheduled.jpg) is a separate session: the actual clock continued to60 demo minutes, selected$52 after further reassessment, was paused and confirmed a$52/65% sandbox reservation. It is not relabeled as the earlier$56 result. Missing NVIDIA credentials remain visible as deterministic preview.


## Latest bounded-wake deployment

[CI40095746361](https://github.com/yimtaegyun/revslot/actions/runs/40095746361) at d6a6a06a3d7b9aac7cb1b50b89fa115de93253d0 passed45 Python tests with real PostgreSQL17,6 Node scheduler tests, production build/TypeScript and4 Chromium cases. Production deployment dpl_AqCrPafSjQotgVD7m9t3aYktZ7xG retains the same public URL.

An authenticated server wake returned in0.86s. Without a browser, the slot repriced$64→$56 /6km /20demo minutes after12.02real seconds, then booked at$56/70%. Native logs showed3calls /1processed /0failures and the work exited after booking; the later idle retry made only1call. The pre-existing$56 reservation also survived this redeployment. Public/forged trigger calls and unauthenticated/wrong-token wake calls returned401. No provider key or live NVIDIA inference is claimed.
