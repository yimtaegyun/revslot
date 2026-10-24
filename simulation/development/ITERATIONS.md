# Development evaluation log

The first 1,000-scenario run is preserved in `v0_heuristic_report.json`. It showed more fill but no significant revenue advantage over fixed 20% discounts; both discount strategies unnecessarily discounted all synthetic natural-fill cases in that run.

Review also found a model-coherence issue: logistic `log(1+hours)` leaves nonzero fill probability as available time approaches zero. Repeatedly converting that probability into interval hazards can distort the arrival process. The report is a **development diagnostic, not final impact evidence**.

V2 uses a complementary-log-log arrival model with fixed log(time) offset. Outcomes use the same explicit rate process over real remaining durations. Noise and elasticity misspecification remain. No outcome is manually altered to make the agent win. V2 is a modelling correction, not independent real-world evidence.

Development scenarios are not a sealed test set. A final independent-seed evaluation must be recorded after policy freeze. Synthetic results must never be used to promise commercial revenue.
