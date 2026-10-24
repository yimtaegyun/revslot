# Competitor matrix — cancellation recovery and perishable inventory

Verified from public primary product/help pages on **2026-10-24**. Features vary by market, plan, version and configuration. This is a documentation comparison, not a hands-on product test.

**Critical correction to the original positioning:** waitlists, last-minute promotions, dynamic pricing, demand forecasts, direct-demand protection, and automated revenue optimization already exist. **ClassPass explicitly describes comparing conversion and expected revenue at different prices relative to class start.** Calling that combination novel would be inaccurate. Revslot's proposed differentiation is an inspectable, merchant-controlled, cancellation-specific loop coordinating price, eligible audience, channels, approval and outcome attribution.

## Legend and definitions

- **✓**: directly supported by retrieved public documentation. It does not mean independently benchmarked.
- **◐**: partial/adjacent capability, rule-based or manual variant, general analytics rather than cancellation attribution, or an important scope limitation.
- **?**: not verified in this research. This means **unknown**, not absent.
- **—**: not a comparable consumer-marketplace function (for enterprise pricing infrastructure only).
- **AI Pricing** means documented ML/AI-informed pricing, not a marketing label containing “smart.”
- **Demand Prediction** means forecasting likely fill/demand; a schedule of off-peak discounts alone does not establish forecasting.
- **Customer Matching** includes restricted/adjacent waitlist matching, identified as ◐ where appropriate; it is not automatically a ranking model.
- **Automatic Repricing** includes automated scheduled rules, identified in the evidence notes; it does not automatically imply an observe/replan loop.
- **Revenue Recovery Analytics** means visibility into recovered/unused-inventory revenue. General sales or campaign analytics are ◐.
- **Autonomous Agent** here means a documented multi-step system that plans/uses tools/observes/replans, rather than any automatic reminder or price algorithm. Marketing of AI agents alone is insufficient to prove the cancellation loop.

## Feature table

| Competitor | Waitlist | Marketplace | Dynamic Pricing | AI Pricing | Demand Prediction | Customer Matching | Automatic Repricing | Cross-business Discovery | Revenue Recovery Analytics | Autonomous Agent |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Fresha [F1–F5] | ✓ | ✓ | ◐ scheduled smart pricing | ? | ? | ◐ suitable waitlist / segments | ✓ scheduled rules | ✓ | ◐ deal performance | ◐ AI Concierge; recovery replanning unverified |
| Booksy [B1–B3] | ✓ | ✓ | ◐ flash/happy-hour/last-minute promotions | ? | ? | ◐ waitlist preferences | ? | ✓ | ◐ general reporting | ? |
| Mindbody [M1–M2] | ✓ | ✓ | ✓ | ? | ? | ◐ waitlist auto-add / first claim | ✓ demand pricing | ✓ | ◐ sales/marketplace reporting | ? |
| OpenTable [O1–O2] | ✓ | ✓ | ◐ shoulder-time incentives / experiences | ? | ? | ◐ guest preferences / waitlist | ? | ✓ | ◐ marketing/channel reporting | ? |
| Treatwell / Salonized [S1–S4] | ✓ | ✓ | ◐ scheduled time blocks | ? | ? | ◐ waitlist preferences | ✓ preset rules | ✓ | ◐ business reporting | ? |
| ClassPass SmartTools [C1–C4] | ? | ✓ | ✓ | ✓ | ✓ | ? personalized ranking not established | ✓ | ✓ | ✓ partner revenue/payout insights | ? full LLM-style loop unverified |
| Too Good To Go [T1] | ? | ✓ | ? | ? | ? | ? | ? | ✓ | ✓ surplus sales tracked | ? |
| Phorest [P1–P2] | ✓ with version caveat | ? | ? | ? | ? | ◐ waitlist | ? | ? | ◐ business reporting | ? |
| IDeaS G3 RMS — hotel [I1–I3] | ? | — | ✓ | ✓ documented AI/ML optimization | ✓ | ◐ segment behavior | ✓ | — | ◐ revenue/channel profitability | ? agent loop unverified |
| PROS — airline [A1–A2] | ? | — | ✓ | ✓ | ✓ | ◐ offer optimization | ✓ | — | ◐ revenue optimization | ✓ vendor-described agents; recovery-loop scope unverified |

**Revslot is intentionally omitted from the checked-feature rows until implementation passes tests.** Its specification is an intended product, not evidence that any feature is shipped.

## Cell-level evidence and limitations

| Row / evidence | What the primary pages establish | What remains unknown |
| --- | --- | --- |
| Fresha F1 | Suitable slots are automatically offered to waitlisted clients; a manual option exists. | No public proof here of ML-ranked external customers. |
| Fresha F2 | Last-minute offers, client segmentation, deal-performance pages and smart-pricing features. | Deal analytics do not prove causal incremental revenue. |
| Fresha F3 | Merchants choose days, intervals and fixed/percentage changes; adjusted prices appear automatically online. | Scheduled rules are not a verified forecast or autonomous strategy loop. |
| Fresha F4 | Business feature page describes marketplace reach and reporting. | No source-code or live-account audit. |
| Fresha F5 | AI Concierge uses account services, prices, availability and policies for client conversations and booking assistance. | Its existence does not establish a response-driven pricing/recovery loop. |
| Booksy B1 | Clients join for a day/range; openings trigger automatic waitlist notifications. | Ranking/optimization methods not disclosed. |
| Booksy B2 | Marketplace exposure/Boost, flash sales, happy hours and last-minute discounts. | No verified continuous ML price optimization. |
| Booksy B3 | A US Boost offer charges for a new client's first visit. | This is acquisition billing, not a cancellation-only success fee. |
| Mindbody M1 | Marketplace reach and demand-based prices, merchant control over classes, inventory and price range. | Exact forecast/model and explainability not established by this page. |
| Mindbody M2 | Waitlist first-to-claim and auto-add workflows; dynamic-pricing tools. | “Smart” alone does not establish a separate autonomous agent. |
| OpenTable O1 | Consumer discovery, online waitlist and live place in line. | No verified cancelled-table conversion optimizer in this page. |
| OpenTable O2 | Bonus points encourage shoulder-time bookings; marketing performance is tracked. | An incentive is not itself a dynamic cash-price engine. |
| Salonized S1 | Waitlist can capture service/staff preferences; staff can contact customers or book. | Notification is not necessarily a fully autonomous customer-rank loop. |
| Salonized S2 | Pro users set pricing blocks; booking widget shows changes; strongest applicable discount wins. | No verified ML demand engine. |
| Salonized S3–S4 | Last-minute discounts can sync to Treatwell and affect ranking/discovery. | No verified response-driven automatic replanning. |
| ClassPass C1 | ML evaluates price/likely-conversion/expected-revenue relationships relative to start time. | Public description is not independent experimental evidence. |
| ClassPass C2 | SmartSpot protects direct-fill inventory using historical/live demand; SmartRate prices it; floor applies. | Exact model, fair-pricing policy and per-cancellation audit not established. |
| ClassPass C3–C4 | Payout/rate-floor explanations, revenue visibility and marketplace operation. | No proof here of a merchant-facing LLM tool trace or approval graph. |
| Too Good To Go T1 | Merchant lists surplus with price and pickup time; local discovery, reservation and revenue tracking. | Waitlist, dynamic pricing, ML forecasts and reprice loop not verified. |
| Phorest P1 | Waitlist/request form exists; this help article warns some email requests need manual maintenance. | Do not conflate this specific form with all newer Phorest waitlist functionality. |
| Phorest P2 | A recent vendor article describes cancellation-triggered eligible-waitlist notification. | Version/market/account availability and ranking algorithm unverified. Medical use is outside our MVP. |
| IDeaS I1–I3 | Demand forecasts, optimized rates/inventory controls, automatic price decisions, profitability/channel analytics and AI/ML-based Agile Rates. | Not a consumer beauty marketplace; no claim that these hotel features are identical to our workflow. |
| PROS A1–A2 | AI pricing, forecasts and inventory/offer optimization; vendor describes autonomous pricing, demand and offer agents. | Exact cancellation-recovery action loop and human-approval mechanism unverified. |

## Competitive conclusions for the product and demo

1. **Fresha / Booksy / Salonized:** a basic waitlist plus last-minute discount app is insufficient differentiation. Show why a particular action is chosen, publish it within constraints, observe no response, and change the strategy with an auditable reason.
2. **ClassPass:** do not say it lacks demand prediction, expected-revenue optimization, direct-demand protection, automatic inventory adjustment or rate floors. All are substantially supported. Our thesis is a merchant-operated recovery control plane for a specific cancellation event, not discovery of the expected-revenue formula.
3. **Mindbody:** dynamic pricing and marketplace distribution also exist within the target fitness/wellness vicinity. Merchant control is table stakes.
4. **Too Good To Go:** the perishable-inventory analogy is useful but not a claim that appointment inventory is economically identical to surplus food. Appointment constraints include staff, duration, lead time and booking reliability.
5. **Hotels / airlines:** yield management has a long-established optimization lineage. Borrow the principles of capacity, timing, opportunity cost and floors; do not claim invention of revenue management.
6. **FineHost domestic precedent:** agentic booking/pricing/inventory operations have already been described. See [DOMESTIC_BENCHMARK.md](DOMESTIC_BENCHMARK.md).

**A defensible pitch:** “Existing platforms already help fill unused inventory. Revslot demonstrates a transparent cancellation-recovery agent: merchants set limits; the agent coordinates price, audience and exposure, revises its plan after no response, and records exactly what was recovered.” This is positioning for the prototype, not a verified universal feature gap.

## Business-model evidence

[B3] is a concrete comparator for performance-linked acquisition fees: US Booksy Boost documents a first-visit commission and cap. That does **not** establish an optimal fee for Revslot. A cancellation-recovery fee should be tested with merchants and compared against incremental contribution after discount, fulfillment cost, channel fees and cannibalization. No commercial price is selected from unsupported assumptions. Proposed pilot choices are a recovery success fee or SaaS plus success fee; each needs genuine willingness-to-pay evidence.

## Required production validation

Obtain merchant consented historical bookings/cancellations, natural-fill opportunities, price changes, opt-ins, offer exposures, customer responses, costs and outcomes. Run time-separated validation and merchant-level holdouts; compare randomized eligible slots where feasible. Measure incremental contribution and unnecessary discounting, not just gross recovered sales. A synthetic comparison demonstrates code and assumptions; it cannot establish an advantage over these live commercial products.

## Primary sources

- **F1:** [Fresha waitlist](https://www.fresha.com/help-center/knowledge-base/calendar/259-set-up-and-manage-your-waitlist)
- **F2:** [Fresha marketing / deals](https://www.fresha.com/help-center/knowledge-base/marketing)
- **F3:** [Fresha smart pricing](https://www.fresha.com/help-center/knowledge-base/marketing/101321-enable-smart-pricing)
- **F4:** [Fresha business features](https://www.fresha.com/en-GB/for-business/features)
- **F5:** [Fresha AI Concierge](https://www.fresha.com/help-center/knowledge-base/ai-concierge/102360-ai-concierge-overview)
- **B1:** [Booksy waitlist](https://support.booksy.com/hc/en-us/articles/16463469277714-How-does-the-waitlist-work)
- **B2:** [Booksy features](https://biz.booksy.com/features)
- **B3:** [Booksy Boost](https://biz.booksy.com/features/boost)
- **M1:** [Mindbody marketplace / dynamic pricing](https://www.mindbodyonline.com/business/mindbody-app)
- **M2:** [Mindbody waitlist / dynamic pricing tools](https://www.mindbodyonline.com/education/blog/8-steps-to-get-the-most-out-of-the-mindbody-app)
- **O1:** [OpenTable waitlist](https://www.opentable.com/restaurant-solutions/products/features/opentable-waitlist/)
- **O2:** [OpenTable marketing](https://www.opentable.com/restaurant-solutions/products/features/restaurant-marketing/)
- **S1:** [Salonized waiting list](https://help.salonized.com/en/articles/6596405-how-can-i-use-the-waiting-list-to-manage-my-calendar)
- **S2:** [Salonized dynamic pricing](https://help.salonized.com/en/articles/6563442-how-can-i-use-dynamic-pricing-to-optimise-my-salon-s-schedule)
- **S3:** [Treatwell integration](https://help.salonized.com/en/articles/6417703-how-does-the-treatwell-integration-work-in-salonized)
- **S4:** [Treatwell profile visibility](https://help.salonized.com/en/articles/7973119-how-can-i-improve-my-treatwell-profile)
- **C1:** [ClassPass ML / conversion / expected revenue](https://classpass.com/partners/blog/how-is-classpass-growing-the-overall-fitness-and-wellness-industry/)
- **C2:** [ClassPass direct-demand protection / floor](https://classpass.com/partners/blog/classpass-protects-direct-business)
- **C3:** [ClassPass payout insights](https://classpass.com/partners/blog/smartrate-insights)
- **C4:** [ClassPass partner FAQ](https://classpass.com/partners/faqs)
- **T1:** [Too Good To Go partner workflow](https://www.toogoodtogo.com/en-us/become-a-partner)
- **P1:** [Phorest waitlist form, scope caveat](https://support.phorest.com/hc/en-us/articles/360017434439-How-do-I-enable-the-Online-Booking-Waitlist-Online-Booking-Appointment-Request-feature)
- **P2:** [Phorest waitlist automation description](https://www.phorest.com/us/blog/automating-med-spa-front-desk-booking-marketing/)
- **I1:** [IDeaS hotel RMS guide](https://ideas.com/tools-resources/hospitality-revenue-management-buyers-guide/)
- **I2:** [IDeaS channel forecasts](https://ideas.com/news/hotel-revenue-channel-performance/)
- **I3:** [IDeaS Agile Rates AI/ML](https://ideas.com/news/ideas-breaks-rules-new-superior-agile-pricing-approach/)
- **A1:** [PROS continuous pricing](https://pros.com/solutions/continuous-pricing/)
- **A2:** [PROS AI agents](https://pros.com/ai-agents/)
