# Nebius access and credit checkpoint

Checked 2026-10-25 Asia/Seoul. Live NVIDIA-on-Nebius inference remains a submission gate.

## Observed state

| Step | Evidence/status |
|---|---|
| Google/email authentication | Confirmed on the target service after user verification |
| Default project | `default-project` creation observed |
| Billing activation | Last observed page requires individual identity/address, card and agreement; completion unverified |
| Payment/legal actions | No card, address, agreement, top-up or payment submitted by the agent |
| Server credentials | Current Vercel variable metadata contains database/scheduler settings; no NEBIUS_API_KEY or TAVILY_API_KEY |
| Official credit application | Public project fields prepared; no personal fields submitted, no credit received |
| Real inference | No authenticated catalogue or model response captured; rules-preview disclosure remains |
| Latest browser | Empty inventory, then two operation timeouts; current page unavailable, no bot-block evidence |

Private account identifiers and onboarding screenshots are excluded from the repository.

## Official credit paths

The [hackathon resources](https://nebiusglobalaihackathon.devpost.com/resources) link a $25 Token Factory application. Its activation code is `NEBIUS-DEVPOST-GLOBAL26`.

[Official application](https://nebius.com/promo-code?utm_promo_activation_code=NEBIUS-DEVPOST-GLOBAL26&utm_promo_code_type=Token_Factory&utm_promo_event_code=2026-devpost-global-ai-hack). The observed form requires name, email, job title and company/project details. Prepared project fields were `Revslot (individual hackathon project)` and the public demo URL. This does not claim a registered company. The application code is not proof of a granted balance or a redeemable top-up code.

The free [Builders Program](https://dev.nebius.com/builders) separately advertises $25 Token Factory and $25 Tavily credits, subject to eligibility, availability and partner terms. It has not been joined in this session.

## Billing is a separate requirement

[Current billing documentation](https://docs.tokenfactory.nebius.com/other-capabilities/billing-new) makes a bank card mandatory during onboarding. The observed card button mentioned a temporary $0 authorization; that is not a promise that future usage is free. Negative balances or the configured billing threshold can trigger an automatic charge. A granted promo code is redeemed through balance → top up → promo code, then verified in transactions.

The user must personally review the billing details, card registration and Services Agreement. Do not enter invented residence details or submit a payment while obtaining credits. If the user declines the card requirement, preserve the functioning preview and leave eligibility open.

## Resume after activation

1. Verify the signed-in account is activated and inspect the actual credit balance. Do not infer a grant from a sent application.
2. At the actual access step, obtain authorization for the required API key; enter it through protected server configuration, never chat, source, browser storage or `NEXT_PUBLIC_*`.
3. Query the live `/models` catalogue and select a currently available NVIDIA Nemotron. Capture only public action summaries and non-secret status/latency/model metadata.
4. Run the existing integration check and application workflow. A model failure remains a recommendation-only state; numerical pricing stays deterministic.
5. Record the final live-provider video and observed sponsor feedback before final submission.

The [official FAQ](https://nebiusglobalaihackathon.devpost.com/details/faqs) says missing-country/credit issues are handled case by case by Nebius and that another inference provider does not satisfy the runtime requirement. No support message was sent and no exception was obtained.
