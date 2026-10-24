# Revslot frontend

Next.js application for merchant recovery, consumer marketplace, analytics and policy control.

Run the full application from the repository root with `node scripts/dev.mjs` after installing Python and frontend dependencies. To run the web service separately, use `pnpm dev`; FastAPI must then be running at the configured `FASTAPI_URL` (default `http://127.0.0.1:8000`).

Production build: `pnpm run build:vercel`. Browser tests: `pnpm exec playwright test`. See the root README and `docs/QA_REPORT.md` for actual verification status and environment limits.
