# Exceptions Guide

Deeper guidance for the Exceptions focus area (Operations) of the 2027 Pragmatic Framework.

## 1. Why exceptions matter

Every exception is a small decision about what the product is. Individually they look harmless; collectively they create a shadow product with its own code paths, contracts and support burden. They are also one of the richest free sources of market evidence a team has: real customers telling you, with money on the line, where the standard offer falls short.

The goal is not to minimize exceptions. It is to make them deliberately, know their cost, and learn from them.

## 2. Approval matrix (example)

| Exception type | Small / reversible | Medium | Large / permanent / precedent-setting |
|---|---|---|---|
| Product (config, custom feature, integration) | Product owner | Product manager + engineering lead | Product leadership / exception review board |
| Commercial (discount, terms, packaging) | Sales manager within band | Deal desk / finance | CRO + CFO, product consulted |
| Contract / policy (SLA, liability, security, data) | n/a | Legal + owning function | Legal + executive owner |
| Service (extra onboarding, dedicated support, manual processing) | CS or support lead | CS/support director | Ops leadership + product consulted |

Define "small/medium/large" with numbers: e.g., engineering effort (< 2 days / < 2 weeks / more), discount (within band / up to X% beyond / more), duration (one-time / < 12 months / permanent).

Set turnaround targets (e.g., 2 business days for small, 5 for medium, next review board for large).

## 3. Scoring a request

Score 1–5 on each; weights are a starting point.

| Criterion | Weight | 1 | 5 |
|---|---|---|---|
| Strategy fit | 25% | Pulls away from strategy or target segment | Directly supports strategy, target segment |
| Problem breadth | 20% | Unique to this customer | Likely common across the segment |
| Value | 20% | Low revenue/strategic value | High revenue, retention or strategic value |
| Cost (inverted) | 20% | High one-time + ongoing cost | Negligible cost |
| Reversibility / precedent (inverted) | 15% | Permanent, sets precedent, forks product | Time-boxed, contained, no precedent |

Guidance, not rules: high strategy fit + high breadth → route to product as a capability. Low strategy fit + high cost → decline with alternative. High value + low breadth + moderate cost → approve as one-off with owner and sunset date.

## 4. Pilot exceptions

When a request looks like it might be a real capability, approve it as a **pilot**: explicitly time-boxed, built in a way that can become standard (or be removed), with learning goals agreed in advance. A pilot is ideation with a paying customer; connect it to `pragmatic-ideation` (Planning) and `pragmatic-requirements` (Planning).

## 5. Finding the problem behind the request

Requests arrive as solutions: "add a field," "give us 90-day terms," "custom report." Before deciding, ask:
- What are you trying to do when you need this?
- What happens today without it? What does it cost you?
- How often does it come up? Who else is affected?
- What would "solved" look like?

Log the answers. This is the same discipline as `pragmatic-market-problems`: problems, not solutions.

## 6. Pattern thresholds

Pick a threshold that fits your volume, for example:
- The same underlying problem from 3+ accounts in 12 months, or
- Exceptions on one problem costing more than X hours or $Y per quarter, or
- Any exception requested by a significant share of a target segment.

When a pattern is found:
1. Write a problem statement with evidence (accounts, quotes, frequency, revenue affected, cost of exceptions so far).
2. Validate with customers and prospects who did not ask (requesters over-represent large or vocal accounts).
3. Hand to `pragmatic-requirements` with frequency and personas, and log in `pragmatic-market-problems`.
4. Decide what happens to existing exceptions when the capability ships (migration plan).
5. If the decision is "keep declining," record the reason and confirm it with `pragmatic-product-strategy` so sales hears one answer.

## 7. The cost of exceptions

Track for granted exceptions:
- Engineering effort to build and maintain; test-matrix growth
- Support and operations effort (tickets, manual steps)
- Margin impact (discounts, free services)
- Release friction (custom code paths, feature flags kept forever)
- Opportunity cost (roadmap capacity diverted)

Report this quarterly; it is often the evidence needed to fund a proper capability or to tighten policy. Feed it to `pragmatic-scaling` and `pragmatic-business-outcomes`.

## 8. Saying no well

- Explain the reason in terms of the customer's interest where possible (reliability, upgrades, support quality).
- Offer an alternative: standard configuration, documented workaround, partner solution, roadmap item with honest timing.
- Log the decline and the problem; tell the customer you've recorded it as input.
- Give sales and CS a consistent answer (`pragmatic-organizational-alignment`, `pragmatic-assets`).

## 9. Hygiene for granted exceptions

- Every exception has an owner, a review or sunset date, and a link to the contract or ticket.
- Custom code is flagged and documented; support knows which customers have what.
- Review the active list at least annually; retire or standardize.

## 10. Internal products and platforms

- Exceptions often look like "our team needs to bypass the standard pipeline" or "can you build us a custom connector."
- Platform teams should publish standards and an exception path, log every bypass, and review patterns to decide what becomes a supported capability.
- Track exceptions per team; a team with many exceptions may have an unmet need the platform should address, or may be outside the platform's intended scope.
