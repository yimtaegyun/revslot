# Architecture

```mermaid
flowchart TD
  Merchant["Merchant calendar"] --> API["FastAPI session API"]
  Consumer["Consumer marketplace"] --> API
  API --> Store["SQLite / PostgreSQL revision CAS"]
  API --> Graph["LangGraph recovery state"]
  Graph --> Demand["Synthetic demand forecast"]
  Graph --> Model["NVIDIA Nemotron on Nebius"]
  Graph --> Context["Optional Tavily context"]
  Demand --> Price["Deterministic candidate pricing"]
  Model --> Guard["Validated plan + policy gate"]
  Price --> Guard
  Context --> Guard
  Guard --> Review["Merchant review when required"]
  Guard --> Publish["Shared offer + sandbox inbox"]
  Publish --> Monitor["Clock observes unsold state"]
  Monitor --> Graph
  Publish --> Booking["Revision-checked reservation"]
  Review --> Publish
  Booking --> Outcome["Booked revenue + audit"]
  Outcome --> Store
  Store --> UI["SSE / polling dashboard"]
```

The frontend has no key or pricing authority. Vercel ingress routes `/api/*` to Python; the Next.js proxy supports local/separate hosting. Three graph nodes coordinate six responsibilities; these are not six independently billed models.

Each anonymous run has an unguessable HttpOnly/SameSite cookie and isolated synthetic records. A transaction updates its snapshot only if the previously read revision still matches. Competing actions/booking lose the compare-and-swap and must reload. No external charge/message occurs before commit. Sessions expire after 24 hours.

SQLite is suitable for a local process. `DATABASE_URL` selects PostgreSQL; its hosted connection remains unverified. Serverless `/tmp` SQLite is explicitly ephemeral. Provider calls occur outside database locks; a revision conflict never silently applies a stale action.

The UI receives concise tool records, not provider reasoning. Hash-linked audit entries detect accidental edits, not externally certified tampering.

| Failure | Response |
|---|---|
| Missing key | Labeled deterministic preview |
| Configured inference failure/invalid plan/timeout | Review-required recommendation |
| Tavily failure | Zero context signal; continue |
| No permitted price | Withdraw offer, blocked state |
| Matching failure | Public listing; no direct targeting |
| Stale/concurrent write | 409 and refresh |
| API offline | Readable error and retry |
| SSE failure | Polling fallback |
