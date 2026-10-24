# Deployment and access status

The requested Vercel project was created: `prj_BWTzn2W1WebpfwmOVUldqvTxOC3y`, account `team_YKG2g9hfvRoFYSxyM0Oc5wzn`. A storage connection request returned **403 account-scope access denied**. No storage was created and no paid plan was selected. The suggested `authorize_team_access` recovery operation is not exposed in this session. App permission inspection showed the default low-risk permission, which is separate from Vercel account-scope authorization.

Do not create a duplicate project. After access is granted, link the existing project to `yimtaegyun/revslot` and deploy `main`. Vercel Services is Beta. `vercel.json` routes API calls to FastAPI and other paths to Next.js. Preserve the original API prefix.

Configure server-only `NEBIUS_API_KEY`, optional `NEBIUS_MODEL`, `TAVILY_API_KEY` and PostgreSQL `DATABASE_URL`. The live model must appear in the runtime NVIDIA Nemotron catalogue. Never put a key in `NEXT_PUBLIC_*`, source, screenshots or logs. Check provider status and save runtime evidence only after real successful calls.

SQLite `/tmp` is an explicitly ephemeral preview fallback. Use PostgreSQL for reliable judging sessions across serverless instances. PostgreSQL provisioning/connection has not been verified. Docker with a named SQLite volume is a reproducible single-instance alternative; it has not been run in this session.

Public judge access is required. The newly created project's protection defaults must be deliberately reviewed for that requested audience; no domain was purchased and no protection bypass link was invented. Verify the final URL anonymously after deployment.

Keep free judge access available through the official end of judging. Final Devpost registration/submission accepts terms and publicity permissions; the user must perform that acceptance.
