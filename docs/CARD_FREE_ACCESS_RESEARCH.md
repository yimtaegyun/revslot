# Card-free Nebius access research
Checked: 2026-10-26 Asia/Seoul. Scope: satisfy this hackathon's real Nebius/NVIDIA runtime requirement while avoiding personal card registration.

## Finding
No verified self-service path was found that activates this individual's new Token Factory account without a payment card. Two conditional avenues merit follow-up: a Nebius-approved participant arrangement, or authorized access to an existing funded organization. Neither has been granted or tested for Revslot.

## Routes checked
| Route | Evidence and conclusion |
|---|---|
| Direct Token Factory signup | Current [billing guide](https://docs.tokenfactory.nebius.com/other-capabilities/billing-new) requires a card. Our last signed-in inspection stopped at incomplete Billing details. |
| Hackathon $25 form / Builders Program | [Resources](https://nebiusglobalaihackathon.devpost.com/resources) and [Builders Program](https://dev.nebius.com/builders) offer credits, not an explicit billing waiver. An application code or received promo code is not an activated account. |
| Ask Nebius for a participant arrangement | Official [FAQ](https://nebiusglobalaihackathon.devpost.com/details/faqs) routes provisioning/credit cases to Nebius Discord. It does not promise a card-free account or no-overage plan. Support approval is necessary before claiming this works. |
| Existing funded organization / genuine team project | Official [invitations](https://docs.tokenfactory.nebius.com/team-access/invitations), [organization hierarchy](https://docs.tokenfactory.nebius.com/team-access/org-projects) and [roles](https://docs.tokenfactory.nebius.com/team-access/groups) support project membership and creating one's own project API key. This is the strongest documented collaboration mechanism to investigate for avoiding a separate personal billing account. Whether the current onboarding wall is skipped for this account remains untested. Organization-owner approval, scoped access and an agreed usage budget are necessary; it is not inherently zero-cost. |
| Nebius AI Cloud instead | [Individual signup instructions](https://docs.nebius.com/signup-billing/sign-up) still require card details; skipping billing during signup prompts for it when creating the first resource. Company bank-transfer arrangements are not a free individual workaround. |
| Old promo-without-card instructions | The separate /other-capabilities/billing URL returned404 in this check. Current documentation links billing-new. Cached older text is not a functioning current onboarding path. |
| OpenRouter / Hugging Face / local model alone | The official FAQ explicitly rejects a different inference provider as a substitute for Nebius. Local execution alone similarly does not establish the required Nebius runtime. |
| A publicly exposed or borrowed unrestricted API key | Not an acceptable route. An organization owner must authorize the application's actual use; no third-party credential was sought or used. |

## Public discussion evidence
The [card-free access thread](https://nebiusglobalaihackathon.devpost.com/forum_topics/45365-token-factory-access-without-a-credit-debit-card) contains participant reports of being blocked even after receiving a promo code. The manager directs users to Nebius Discord; no working self-service solution appears in the inspected replies.

In [how to obtain the API without a card](https://nebiusglobalaihackathon.devpost.com/forum_topics/45433-how-can-we-get-the-nebius-api-without-card) and [the no-US-card thread](https://nebiusglobalaihackathon.devpost.com/forum_topics/45457-is-there-a-way-to-get-api-credits-without-a-us-card), the Devpost manager says their team cannot resolve the issue and refers it to Nebius.

The [Pakistan provisioning discussion](https://nebiusglobalaihackathon.devpost.com/forum_topics/45424-pakistan-not-supported-for-token-factory-billing-how-can-i-submit) includes participants reporting support refusals of manual exceptions. These are participant accounts about unsupported countries, not a verified universal policy or a ruling about South Korea. They do not justify promising that an exception will be available.

Officially linked current Discord: https://discord.com/invite/eXYTGhgnhK . This link was retrieved from the FAQ/manager responses. The server was not joined, invite acceptance was not tested, and no message was sent.

## Next concrete action
Request an explicit answer from Nebius: can it provide a card-free promotional-credit-only project, with no negative balance or automatic payment and sufficient access for the judging period? If not, can an invited project member use an already funded organization without completing separate personal billing?

A ready-to-review [support request](../demo/NEBIUS_SUPPORT_REQUEST.md) contains only the public project and the observed onboarding issue. It has not been sent. General approval to research is not consent to send messages, accept terms or register a card.

## Evidence boundary
No new account, card, payment, legal acceptance, project invitation, grant, credential or runtime inference was created during this research. Credit and provider gates stay open. This research changes no application code or evaluation result.
