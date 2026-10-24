# Sponsor feedback — evidence boundary

## Documentation observations from this build

- Nebius: the OpenAI-compatible endpoint and explicit runtime qualification in the FAQ make the integration boundary clear. The August deprecation table shows why runtime model discovery matters; older hardcoded IDs would be fragile.
- NVIDIA: the implementation needs short, schema-valid operational plans and concise summaries rather than unconstrained pricing text. We isolate the numerical optimizer so model evaluation can focus on valid actions, grounding, failure behavior and latency.
- Tavily: public, date-specific event retrieval is an appropriate optional enrichment; retrieved sources should be inspectable. A retrieved event is not automatically evidence of a causal increase in wellness demand.

## Usage feedback still required

Authenticated runtime credentials were absent. No inference-quality, latency, model-comparison, throughput, credit-usage or search-quality claim has been fabricated. After connecting keys, record actual model ID, request status, structured-output behavior, latency and concrete issues in `RUNTIME_EVIDENCE.json`, then replace this section with observed usage feedback before submitting.
