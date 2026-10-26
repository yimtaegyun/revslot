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
| Latest browser | Client reset restored access; fresh signed-in page confirms the incomplete billing form, ready for user takeover |

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

## Credit exhaustion and automatic charges — verified 2026-10-25 KST

**Result:** no vendor-supported setting that guarantees credit-only usage with zero automatic card charges was verified. This is not proof that support cannot offer an account-specific arrangement.

| Control/source | What the current official material establishes |
|---|---|
| [Token Factory billing](https://docs.tokenfactory.nebius.com/other-capabilities/billing-new) | Negative balances at month start or reaching the billing threshold can trigger automatic card charges; no credit-exhaustion hard-stop procedure is documented. |
| [Token Factory Supplemental Terms §6.1](https://docs.nebius.com/legal/token-factory), effective October22,2026 | Default service fees are postpaid unless an Order Form specifies otherwise. |
| [Nebius AI Cloud budgets](https://docs.nebius.com/signup-billing/budgets) | Budgets send alerts and do not stop/cap usage. This separate AI Cloud feature is not evidence of a Token Factory hard cap. |
| [Current Token Factory documentation index](https://docs.tokenfactory.nebius.com/llms.txt) | Links to billing-new. The separate /other-capabilities/billing page describing automatic top-ups should not be treated as proof that turning top-ups off prevents current postpaid charges. |

The signed-in account was checked again: default-project is present, but mandatory Billing details is still incomplete, with no card and the agreement unchecked. Settings beyond onboarding cannot be inspected without completing that financial/legal step. No such step was performed for this check.

A server-side request/token budget can reduce application usage, but is not a provider-enforced account-wide billing guarantee. A payment-card block also does not erase incurred service fees; see [Services Agreement §9](https://docs.nebius.com/legal/agreement).

Do not promise free-credit-only operation or tell the user to register a card merely to discover hidden settings. A definitive exception requires a provider-confirmed no-overage arrangement or a verifiable credit-exhaustion stop. No support inquiry was sent, no exception obtained and no billing setting changed.

## Card-free route investigation — 2026-10-26 KST

The [expanded research](CARD_FREE_ACCESS_RESEARCH.md) found no verified card-free self-service activation. Promo/Builders credits do not document a card waiver. Official organization invitations and scoped project keys are supported, but bypassing this account's personal onboarding via invitation is untested. Nebius participant provisioning remains a request, not an approved exception. A [support message](../demo/NEBIUS_SUPPORT_REQUEST.md) is prepared and unsent. No card, charge, invitation, grant or key was created.
