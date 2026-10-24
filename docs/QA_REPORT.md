# Verification status

## Latest bounded-wake production checks

[CI40095746361](https://github.com/yimtaegyun/revslot/actions/runs/40095746361), source d6a6a06a3d7b9aac7cb1b50b89fa115de93253d0:45 Python tests passed in1.19s with PostgreSQL17;6 Node scheduler tests passed; production build/TypeScript passed;4 Chromium tests passed in23.7s. Local44 passed/1 PostgreSQL skipped.

Production deployment dpl_AqCrPafSjQotgVD7m9t3aYktZ7xG is READY. Anonymous tests retained the previous$56 reservation across redeployment. The authenticated wake returned in0.86s; an API-only session repriced$64→$56 /6km /20demo minutes after12.02s, paused, booked$56/70% and stopped future work. Native function logs recorded3calls /1processed /0failed, then an idle scheduled retry exited after1call. SQL confirmed zero pending clock jobs. Public/forged schedule requests and missing/wrong-token wake requests all returned401. This deployment's error/fatal scan for16:17:21.934Z–16:32:21.934Z returned no matching logs.

The native retry schedule is now every15minutes; starting Play initiates bounded work immediately. This avoids constant idle database warming while retaining SQL jobs/leases and retry ownership. All values are synthetic; live provider verification is still open.

## Earlier executed checks

- [CI40092611551](https://github.com/yimtaegyun/revslot/actions/runs/40092611551), commit9ae376e9c5741d13699f1dde74e8570c5166645b:42 Python tests passed in1.05s including the versioned migration, real PostgreSQL17, competing leases, CAS and repricing; production build/TypeScript passed;4 Chromium tests passed in22.4s. The fourth closed every page and confirmed server repricing after reopening.
- New Neon scheduler source:3 local Node tests passed, covering ten-second cadence, redirect/failure stop and missing trigger provenance; production bundle built. This small infrastructure change is added to CI.
- Public deployment dpl_HxFvaBsDjxFFrA8KVpJWnMHubKWd: anonymous health/session/cancel/reprice/book returned200 with durability=postgres. A$56 booking at revision3 survived redeployment unchanged.
- Real hosted Neon trigger: six calls /one processed recovery job /zero failures in native logs at2026-10-24T12:34:51Z. A separate API-only session repriced$64→$56 /6km after13.27real seconds, with only read-only GET observation after clock start. No browser heartbeat, manual advance or test-side tick call drove that transition.
- Actual public browser session: automatic clock advanced to60demo minutes, further repriced to$52, paused and confirmed$52 /65% sandbox recovery. The screenshot records this actual state rather than relabeling it as the earlier$56 scenario.
- Runtime error/fatal scan of this production deployment from12:26:55.757Z through12:41:55.757Z returned no matching logs.
- Public requests and forged Neon trigger headers to the verification function both returned401. A$56 reservation was independently observed in Neon SQL before the redeployment check.

[Neon evidence](NEON_DEPLOYMENT_EVIDENCE.json), [public deployment evidence](LIVE_DEPLOYMENT_EVIDENCE.json), [captures](../demo/README.md). All business/customer data and booked amounts are synthetic.

## Historical capture provenance

The original nine screenshots and raw7.64s recording came from [CI40064620041](https://github.com/yimtaegyun/revslot/actions/runs/40064620041), commit574de1d52a5bc8d185a20df08e9ca7e45833e88e:34 Python /3 Chromium tests passed. Original hashes and log excerpts remain in QA_EVIDENCE.json. The browser initially failed development-resource hydration; development-origin/initialization issues were repaired and tests switched to a production build. An invalid cache-save configuration was also removed before the final successful run.

[CI40089803664](https://github.com/yimtaegyun/revslot/actions/runs/40089803664) subsequently verified42 Python /4 browser tests and the server-owned clock. Separate before-close and after-reopen page videos are unedited; the no-page interval is established by the test and read-only observation, not a fabricated continuous recording. Screenshot11 records the first public ephemeral/manual deployment. Screenshot12 records the later durable/scheduled deployment.

The170-second silent captioned review film uses actual original captures and retains rules-preview disclosure throughout. It is not the final eligible live-model/public-YouTube take.

## Open verification

No Nebius/Tavily key is configured. The connectivity checker previously correctly returned exit2; mocked calls do not satisfy actual NVIDIA-on-Nebius usage. Live model latency, final public YouTube, observed sponsor feedback, user legal acceptance and Devpost submission remain open. Docker remains unexecuted. No real merchant pilot, customer, payment, outbound message or incremental revenue is claimed.
