# Deterministic demonstration

- Fictional merchant: Still Wellness, Brooklyn.
- Service: 60-minute deep-tissue massage; original $80; cost $32.
- Scenario clock: Friday 2026-10-30, 17:00 local; appointment 20:00.
- Cancel: evaluate current model natural fill, eight candidates, policy, 12 profiles within 3km.
- Initial allowed quote: $64 (20% off).
- Advance 20 simulated minutes with no reservation.
- Reassessment: $56 (30%), 24 opt-in profiles within 6km.
- Confirm reservation from Marketplace using current revision.
- Actual state: recovered $56; original-value recovery 70%; discount difference $24; 20 simulated minutes to fill.

These values were observed through the API integration scenario. The natural-fill estimate must be read from the current model; do not substitute the prompt’s 18% or a fake 42-minute fill. Missing keys mean rules preview, not live NVIDIA. Live inference can legitimately choose wait/review; capture the actual result rather than replacing it with a canned trace.

For a human gate: turn autopilot off, cancel, inspect unpublished review-required offer, approve the exact revision. A floor above $80 blocks the offer and cannot be overridden.
