# Sponsor feedback — evidence boundary

## Documentation observations from this build

- Nebius: the OpenAI-compatible endpoint and explicit runtime qualification in the FAQ make the integration boundary clear. The August deprecation table shows why runtime model discovery matters; older hardcoded IDs would be fragile.
- NVIDIA: the implementation needs short, schema-valid operational plans and concise summaries rather than unconstrained pricing text. We isolate the numerical optimizer so model evaluation can focus on valid actions, grounding, failure behavior and latency.
- Tavily: public, date-specific event retrieval is an appropriate optional enrichment; retrieved sources should be inspectable. A retrieved event is not automatically evidence of a causal increase in wellness demand.

## Usage feedback still required

Authenticated runtime credentials were absent. No inference-quality, latency, model-comparison, throughput, credit-usage or search-quality claim has been fabricated. After connecting keys, record actual model ID, request status, structured-output behavior, latency and concrete issues in `RUNTIME_EVIDENCE.json`, then replace this section with observed usage feedback before submitting.

## Observed account setup — 2026-10-25 KST

Google/email authentication succeeded and a default project was created. The next screen required billing identity, a card and Services Agreement acceptance before access to an API key. The official hackathon credit application is separate from account activation; only public project details were prepared and no application was submitted. No credit or model usage was observed. A useful documentation improvement would be to show the card requirement and credit-application/redemption distinction together at the hackathon entry point. This is account-setup feedback, not inference-quality feedback.

Later cloud-browser operations timed out, so account activation was not reverified. This is an observation about the automation session, not evidence of a Nebius outage. [Sources and next steps](../docs/NEBIUS_ACCESS_AND_CREDITS.md).
