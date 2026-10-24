# Pricing and model card

Discount candidates: 0%, 10%, 15%, 20%, 25%, 30%, 35%, 40%. Integer-cent expected revenue is `price × remaining-horizon fill probability`; ties favor smaller discounts. This is myopic optimization, not guaranteed lifetime revenue maximization.

Price must exceed max(floor, cost + minimum margin); discount cannot exceed cap. Expired slots are blocked. Natural full-price probability ≥65% restricts candidates to full price. Autopilot, review threshold, support and repricing are separate execution gates. No model-generated price or customer identity can override them.

The forecast is a complementary-log-log Bernoulli fit with a fixed log(hours) offset. Probability approaches zero as time approaches zero, allowing coherent interval arrival hazards. Features: popularity, waitlist count, bounded context, discount, prior-offer stage, discount/stage interaction and reach proxy.

The generator creates 12,000 synthetic events over 180 days, three merchants, six services. Cancellations are intentionally oversampled at 42%; this is not an industry estimate. Treatments are randomized in the generator. Earlier 70% of cancellations train the model, 15% is reserved, and final 15% is a chronological holdout. Exact metrics/rows/checksum are in `data/DATA_CARD.json`. Outcome and time-to-rebook fields never enter prediction. Coefficients are JSON; restart after regeneration to clear the process cache.

The 0.87/0.48 confidence gate is a **demo coverage heuristic** for supported remaining-time/waitlist ranges. It is not learned uncertainty, an accuracy figure or a confidence interval. Production needs merchant-specific support, drift and calibration.

Tavily's external feature stays zero without date-grounded evidence; any value is constrained to ±0.03. No real concert-to-massage causal model was trained. Forecast and simulator share a structural family; noise, independent seeds and elasticity sensitivity do not turn synthetic results into market evidence. The final policy still over-discounts synthetic natural-fill cases.
