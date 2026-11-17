# Value Realization Guide

Deeper guidance for the Customer Value Realization focus area (Operations) of the 2027 Pragmatic Framework. Draws on outcome-based customer success practice.

## 1. Outcome categories and example metrics

| Category | Example outcomes | Example metrics |
|---|---|---|
| **Revenue** | Grow sales, improve conversion, raise deal size | Win rate, conversion %, average order value, pipeline velocity |
| **Cost** | Reduce labor, vendors, waste | Hours per task, FTE redeployed, vendor spend, cost per transaction |
| **Speed** | Faster cycles | Cycle time, time to close/ship/resolve, lead time |
| **Quality** | Fewer errors, better accuracy | Error rate, rework, defect rate, data accuracy |
| **Risk and compliance** | Pass audits, reduce incidents | Audit findings, incidents, time to compliance, exposure |
| **Experience** | Better employee or end-customer experience | Their CSAT/NPS, retention of their customers, employee effort |
| **Strategic** | Enable new capability or business model | Launch of new offering, entry to new market, capability live |

Pick 1–3 primary outcomes per customer. More than that dilutes focus and makes reviews tedious.

## 2. Desired outcomes vs. required outcomes

Customers often have two layers:
- **Business outcome** — what the economic buyer cares about (cost, revenue, risk).
- **Personal or functional outcome** — what the user or champion cares about (less manual work, visibility, promotion).

Capture both; the business outcome justifies renewal, the personal outcome drives adoption.

## 3. Baselining

Methods, from strongest to weakest:
1. **Customer system data** before go-live (their reports, their numbers).
2. **Time-boxed measurement** before rollout (e.g., two weeks of timing a process).
3. **Comparison group** — teams or regions not yet using the product.
4. **Customer estimate**, documented and agreed at kickoff.
5. **Industry benchmark** — weakest; use only when nothing else is available, and label it.

Record the method; it determines how much weight the result can bear.

## 4. Time to value

- **Time to first value** — first measurable result (often tied to the activation event from `pragmatic-adoption`).
- **Time to full value** — target outcomes achieved.

Set realistic expectations during the sale; over-promising time to value is a leading cause of early churn. Feed actuals back to sales via `pragmatic-assets` and `pragmatic-organizational-alignment`.

## 5. Evidence strength

| Level | Description | Use |
|---|---|---|
| A | Customer-confirmed, quantified, vs. baseline | External proof points (with permission), pricing and positioning evidence |
| B | Product-measured, quantified | Internal reporting; external only if customer agrees |
| C | Estimated (model or calculator) agreed with customer | Internal; label as estimate |
| D | Anecdotal / qualitative | Direction-setting, interview follow-up |

Track the share of accounts with A/B evidence; it's a good indicator of how mature the practice is.

## 6. Value review agenda (30–60 min)

1. Recap desired outcomes and success criteria (have they changed?)
2. Progress vs. baseline and target, with evidence
3. What's working (use cases, teams, practices)
4. Blockers on both sides
5. Agreed actions and owners (customer and vendor)
6. Next milestone and review date
7. Optional: permission to share results; references (hand to `pragmatic-customer-satisfaction` / `pragmatic-assets`)

Keep it about outcomes. Feature roadmaps and renewal pricing belong in other meetings.

## 7. Diagnosing unrealized value

| Cause | Signals | Route |
|---|---|---|
| Low or shallow adoption | Activation missed, low breadth/depth | `pragmatic-adoption` |
| Capability gap | Use case not supported; workarounds; exceptions requested | `pragmatic-requirements`, `pragmatic-exceptions` |
| Implementation | Configuration, data or integration incomplete | Implementation/CS plan |
| Customer change management | Old process still running; no sponsor | Joint plan with customer sponsor |
| Wrong expectations | Outcome was never realistic for this product or segment | `pragmatic-positioning`, `pragmatic-market-definition`, sales enablement |
| External change | Customer's priorities shifted | Redefine outcomes |
| Reliability | Escalations, incidents | `pragmatic-escalations`, `pragmatic-scaling` |

## 8. Aggregating across accounts

Roll up per segment and outcome:
- % of accounts with agreed success criteria
- % with baseline
- % achieving target outcomes by milestone; median time to first/full value
- Typical result ranges (e.g., "cycle time reduced 25–40% at mid-market customers")
- Top reasons for unrealized value

Segment differences are often the most valuable finding: they show where the product fits best (input to `pragmatic-market-definition` and `pragmatic-product-strategy`).

## 9. Sharing with build, sell and support

- **Build:** a quarterly summary of unmet outcomes with evidence and frequency, written as problems, for `pragmatic-requirements` and roadmap planning.
- **Sell:** proof points and realistic time-to-value ranges by segment; case studies via `pragmatic-assets`; ensure claims match evidence level.
- **Support/success:** practices that correlate with faster value; update onboarding and adoption playbooks.
- **Pricing:** realized value informs value-based pricing (`pragmatic-pricing`).

## 10. Closing the loop to Market Problems

At least twice a year, write a short "what customers achieved and didn't" brief:
- Outcomes reliably achieved (strengths to reinforce in positioning)
- Outcomes not achieved, by cause
- New outcomes customers are asking for
- Segments with notably better or worse results

Hand to `pragmatic-market-problems` as evidence, then validate with the broader market, including non-customers, before acting.

## 11. Internal products and platforms

- Agree outcomes with the business owner at rollout (e.g., "reduce manual reconciliation hours by 30%").
- Baseline from the business process, not from the platform.
- Report realized value to the sponsoring executive; it justifies continued investment and is input to `pragmatic-business-outcomes`.
- Unrealized value often traces to the old process not being retired; check with `pragmatic-adoption`.
