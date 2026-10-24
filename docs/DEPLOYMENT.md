# Deployment and access status

The requested Vercel project was created: `prj_BWTzn2W1WebpfwmOVUldqvTxOC3y`, account `team_YKG2g9hfvRoFYSxyM0Oc5wzn`. A storage connection request returned **403 account-scope access denied**. No storage was created and no paid plan was selected. The recovery operation was initially unavailable, then became exposed and generated a single-use10-minute consent link, shown to the user. Access is not granted merely by generating that link. App permission inspection showed the default low-risk permission, which is separate from Vercel account-scope authorization.

After full browser CI passed, reading this exact existing project under the same team also returned403 for scope `yimtaegyun0217-7000`. This confirms the blocker is account-scope access, not merely a storage feature. No deployment mutation was attempted after target verification failed. The returned recovery asks for team authorization. After the user approves the supplied consent link, retry this exact project GET on the same connection before deploying. Generate a new official link only if the old one expired; do not publish ephemeral consent URLs in source.

Do not create a duplicate project. After access is granted, link the existing project to `yimtaegyun/revslot` and deploy `main`. Vercel Services is Beta. `vercel.json` routes API calls to FastAPI and other paths to Next.js. Preserve the original API prefix.

Configure server-only `NEBIUS_API_KEY`, optional `NEBIUS_MODEL`, `TAVILY_API_KEY` and PostgreSQL `DATABASE_URL`. The live model must appear in the runtime NVIDIA Nemotron catalogue. Never put a key in `NEXT_PUBLIC_*`, source, screenshots or logs. Check provider status and save runtime evidence only after real successful calls.

SQLite `/tmp` is an explicitly ephemeral preview fallback. Use PostgreSQL for reliable judging sessions across serverless instances. PostgreSQL provisioning/connection has not been verified. Docker with a named SQLite volume is a reproducible single-instance alternative; it has not been run in this session.

Public judge access is required. The newly created project's protection defaults must be deliberately reviewed for that requested audience; no domain was purchased and no protection bypass link was invented. Verify the final URL anonymously after deployment.

Keep free judge access available through the official end of judging. Final Devpost registration/submission accepts terms and publicity permissions; the user must perform that acceptance.

## Monitoring deployment requirement

A standalone FastAPI backend with a persistent SQLite volume or PostgreSQL runs the included server worker automatically. It remains active without an open browser while that host runs. For Vercel serverless, Play remains disabled until a real external scheduler, CRON_SECRET, REVSlot_EXTERNAL_TICK=1 and PostgreSQL are configured. Hobby Cron runs once per day and cannot drive this 10-second accelerated demonstration. No paid scheduler was activated. See BACKGROUND_MONITORING.md.

## Latest status: access resolved and public preview verified

The official account grant succeeded. Deployment dpl_4DHbjT2Ma8RB1WNoqBp42yzc3fd2 is READY at https://revslot-one.vercel.app/ . Project SSO was disabled only for this deliberately public synthetic demonstration. Anonymous API and browser reservation flows passed. Do not ask for the same Vercel account authorization again.

Git-source import returned git_info_fail. Exact reviewed source files were uploaded instead; the corrected49-file bundle matched Git tree eadff2161e9197dba60a3dcc06f445d1a85c9fd3 (commit875c8f59ba8517ed798e2b80546a274c792db0d5). Deployment environment metadata contains no Nebius/Tavily/DATABASE_URL. Public mode therefore remains a labeled rules preview with ephemeral SQLite and manual advance. Hosted durable storage, actual inference and unattended hosted scheduling remain unverified. LIVE_DEPLOYMENT_EVIDENCE.json records the observed result.
