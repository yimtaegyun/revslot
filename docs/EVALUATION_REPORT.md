# Synthetic evaluation report

This is a reproducible synthetic policy experiment, not real recovered revenue, causal merchant uplift, or an evaluation of LLM business value. No live LLM is used in the numerical comparison.

## Final independent-seed comparison

Policy frozen before seed 20261030 was evaluated. This is an internal post-freeze test, not externally preregistered research. Same scenarios, latent demand, time intervals and random draws for every strategy. 1,000 cancellation scenarios. Lower support and approval-required actions are not executed; no instantaneous human approval is assumed.

| Strategy | Fill | Revenue / cancelled slot | Avg discount (filled) | Time to fill | Margin preserved | Unnecessary discount |
|---|---:|---:|---:|---:|---:|---:|
| No recovery | 18.8% | $14.12 | 0.0% | 146.8 min | 18.9% | 0.0% |
| Waitlist only | 20.5% | $15.47 | 0.0% | 142.6 min | 20.7% | 0.0% |
| Fixed 20% | 81.4% | $48.70 | 20.0% | 43.1 min | 54.2% | 100.0% |
| Revslot agent | 92.5% | $53.17 | 22.9% | 48.9 min | 56.9% | 100.0% |

Paired agent minus fixed-20 revenue difference: **$4.48 per cancelled slot**, synthetic paired-bootstrap 95% interval **$3.20 to $5.84**. This excludes real-market and model uncertainty.

The agent collects more gross dollars and fills more slots under these assumptions, but its average discount is higher and its conditional time to fill is longer. **It does not improve the unnecessary-discount rate.** Do not turn this into a claim of minimum discount, faster recovery, or reduced cannibalization.

## Definitions

- **revenue:** Booked gross dollars, including natural/direct fills; not profit or causal incremental revenue.
- **margin_preservation:** Recovered gross margin / full original gross margin of all cancelled slots.
- **unnecessary_discount_rate:** Among slots that fill under no recovery using the same latent random draws, fraction exposed to any discount by this policy.
- **time:** Conditional on successful fill, simulated minutes from cancellation.
- **confidence_interval:** Paired bootstrap over synthetic scenarios; excludes real-market/model uncertainty.

## Elasticity misspecification

The fitted policy is unchanged; only the true outcome generator's price sensitivity changes.

| True elasticity multiplier | No recovery | Waitlist | Fixed 20% | Agent |
|---|---:|---:|---:|---:|
| 0.5× | $14.12 | $15.47 | $30.08 | $33.75 |
| 1.0× | $14.12 | $15.47 | $48.70 | $53.17 |
| 1.5× | $14.12 | $15.47 | $57.84 | $59.03 |

## Forecast/data validation

- 12,000 events, 5,026 cancellations, 3 merchants, 6 services, 180-day generation window. All synthetic; cancellation prevalence is deliberately oversampled, not an industry rate.
- Chronological 70% training / 15% reserved / 15% test; 3518 training and 754 final test rows.
- Test Brier 0.0725; constant-rate baseline 0.1249; ROC AUC 0.9285. These are synthetic-data scores, not production ML accuracy.
- Model: complementary-log-log Bernoulli likelihood with fixed log(time) offset; outcomes never enter features.
- Dataset SHA-256: `62f6d36e5d73884694e31c7535a711dca049e423b435b616398072e19e77b310`.

## Limitations

- Not real merchants, customers, demand, or recovered money.
- Outcome generator and forecast share a functional family; latent noise and elasticity sensitivity reduce but do not remove circularity.
- All strategies use the same scenarios, time steps, latent demand and random draws.
- Channel expansion is part of the agent policy, so the comparison does not isolate LLM reasoning or price effects.
- The radius feature is an assumed exposure proxy, not measured advertising reach or a causal channel effect.
- No LLM participates in these numerical simulations; they evaluate the deterministic recovery policy.
- Approval-required or low-confidence agent actions are not executed; no instantaneous human approval is assumed.

## Reproduction and retained failures

Run `python scripts/generate_data.py` then `python simulation/evaluate.py` with the locked development dependencies. Machine-readable results are in `simulation/results.json`. The earlier failed comparison and the probability-coherence correction are retained in `simulation/development/`; the initial diagnostic is not final impact evidence. No test result was removed to make the policy look successful.

A real pilot needs randomized offers or another credible counterfactual, incremental profit, direct-booking cannibalization, opt-in engagement and merchant-specific calibration. Neither an independent seed nor a bootstrap replaces that evidence.
