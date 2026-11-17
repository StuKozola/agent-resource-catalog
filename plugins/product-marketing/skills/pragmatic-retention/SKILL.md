---
name: pragmatic-retention
description: >
  Guides Retention planning per the 2027 Pragmatic Framework (Go-to-Market category; formerly Revenue Retention). Retention answers "Why do customers stay, and why do they leave?" and covers keeping customers and deepening the value they get through renewal, continued use, expansion and repeat engagement. Use whenever someone needs a retention plan or budget, churn reduction, churn analysis, learning from churned customers, early disengagement or at-risk signals, customer health scores, net revenue retention (NRR) or gross revenue retention (GRR), expansion revenue, upsell/cross-sell to existing customers, renewal strategy, account expansion, or customer loyalty programs. Do NOT use for acquiring new customers or users (pragmatic-growth), onboarding and activation design (pragmatic-adoption), satisfaction measurement (pragmatic-customer-satisfaction), or proving customer outcomes (pragmatic-customer-value-realization).
---

# Retention — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Go-to-Market — *How will the market find, choose and stay with the product?*
- **Focus-area question:** *Why do customers stay, and why do they leave?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Marketing Plan, Growth, Launch, Organizational Alignment, Awareness, Engagement, Customer Satisfaction
- **Formerly:** Revenue Retention

## Purpose

Retention is the work of keeping customers and deepening the value they get over time. It shows up as **renewal, continued use, expansion and repeat engagement**. The pre-2027 definition was limited to plans and budgets for loyalty and selling more to existing customers; the 2027 version adds continued use and engagement, so a customer who renews but stops using the product is a retention risk, not a success.

**Net revenue retention (NRR) above 100%** means expansion from existing customers (upsell, cross-sell, more seats or usage) outweighs what you lose to churn and downgrades. The existing base grows on its own, before any new customers. Always read it next to gross revenue retention (GRR), which excludes expansion and can't exceed 100%, so a few large expansions can't hide broad churn.

Three ideas from the guide shape this skill:
1. **Retention starts with onboarding** and continues through engagement and service. It is not a renewal-time activity.
2. **Watch for disengagement early.** Falling usage, unused seats and silence show up months before a cancellation.
3. **Learn from customers who leave.** Churned customers are market evidence; use what they say to improve the product and the experience.

## Boundaries with nearby focus areas

| Focus area | What it owns | How Retention uses it |
|---|---|---|
| **Growth** (Go-to-Market), `pragmatic-growth` | New revenue, new users, new sources of use | Agree who owns each expansion target; share churn and expansion assumptions |
| **Adoption** (Enablement), `pragmatic-adoption` | Onboarding, activation, meaningful and ongoing use | Retention depends on it; usage signals feed health scores |
| **Customer Satisfaction** (Go-to-Market), `pragmatic-customer-satisfaction` | Customers' own judgment of their experience and relationship | Satisfaction trends are leading indicators of churn risk |
| **Customer Value Realization** (Operations), `pragmatic-customer-value-realization` | Whether customers got the outcome they bought for | Unrealized value is a top churn driver; value evidence supports renewal and expansion |

## Framework Context

**Inputs:**
- **Buyer Personas** and **User Personas** (Planning) — who existing customers and users are
- **Buyer Journey** (Planning) — how renewal and expansion decisions get made and who approves them
- **Market Problems** (Market) — evolving customer problems that make expansion relevant
- **Positioning** (Planning) — retention and expansion messaging by persona and segment
- **Pricing** (Business) — tiers and packaging that create natural expansion paths
- **Win/Loss Analysis** (Market) — loss interviews applied to churned accounts
- **Competitive Landscape** (Market) — competitor win-back campaigns targeting your customers

**Feeds:**
- **Market Problems** and **Requirements** — churn reasons and disengagement patterns become product evidence
- **Business Outcomes** (Business) — retention and NRR results
- **Measurement** (Business) — leading and lagging retention indicators
- **Organizational Alignment** (Go-to-Market) — success, support and sales share the same picture of at-risk and expansion accounts
- **Engagement** (Go-to-Market) — lifecycle and repeat-engagement programs for existing customers

## Workflow

Adapt depth to the business model: subscription SaaS emphasizes NRR and churn; contract businesses emphasize renewals; B2C emphasizes repeat purchase and engagement.

### Phase 1: Customer Base Assessment

Ask about:
1. **Customer segments** — size, industry, product line, contract type, persona.
2. **Revenue composition** — share from existing vs. new customers; recurring, transactional or hybrid.
3. **Current metrics** — logo retention, NRR, GRR, churn (voluntary and involuntary), CLV, expansion revenue, active use.
4. **Churn analysis** — top churn drivers, when in the lifecycle churn concentrates, and what churned customers said in interviews.
5. **Existing programs** — customer success, renewals, QBRs, health scores, loyalty programs.

If data is missing, help define what to measure. See `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-retention/references/metrics-guide.md`.

### Phase 2: Retention Strategy

Build strategies across the customer lifecycle.

**Onboard — start retention on day one**
- Define time-to-first-value and the activation milestones that predict renewal (design with `pragmatic-adoption`)
- Identify customers whose onboarding stalls and intervene early

**Protect — detect disengagement and reduce churn**
- Define early disengagement signals: declining logins or usage, unused seats, missed QBRs, sponsor changes, rising support tickets, falling satisfaction scores, payment failures
- Build a customer health score from those signals with thresholds and action triggers
- Design proactive intervention workflows for at-risk accounts
- Fix involuntary churn (dunning, payment retry)
- Set the renewal process and timeline (when renewal conversations start)

**Learn — from customers who leave**
- Interview churned customers (someone other than the account owner, 2–4 weeks after the decision)
- Log reasons in a consistent taxonomy; separate product gaps, unrealized value, service failures, price and competitive losses
- Feed patterns to Market Problems and Requirements, and report what changed as a result

**Grow — expansion**
- Upsell (upgrades, seats, premium tiers) and cross-sell (complementary products, services)
- Time expansion offers from usage data and value evidence (`pragmatic-customer-value-realization`)
- Packaging that creates natural upgrade paths (with `pragmatic-pricing`)
- Customer-success-qualified leads (CSQLs) for sales

**Deepen — continued use and repeat engagement**
- Service quality and responsiveness (support is part of retention)
- Customer education, community, advisory boards, executive sponsors
- Feedback loops that show customers their input changed something
- Satisfied customers can become references; manage that in `pragmatic-customer-satisfaction`

### Phase 3: Budget and Resources

1. **Program inventory** — all retention programs
2. **Resources** — people, technology, content, services
3. **Budget** — by program, quarter and segment
4. **ROI** — what a 1-point retention or NRR gain is worth (see "Retention Economics" in `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-retention/references/metrics-guide.md`)
5. **Technology** — CRM, customer success platform, product analytics, lifecycle automation

### Phase 4: Measurement

1. **Primary KPIs** — 3–5 headline metrics (NRR, GRR, logo churn, expansion revenue, active use)
2. **Leading indicators** — health scores, usage and engagement trends, satisfaction trends, onboarding completion
3. **Cadence and targets** — monthly and quarterly reviews with numeric targets
4. **Adjustment triggers** — what result changes the strategy
5. **Corporate alignment** — tie KPIs to business goals (`pragmatic-measurement`, Business)

## Internal Products

For internal platforms, retention is continued use: teams that keep using the platform instead of drifting back to spreadsheets or building their own. Track active teams over time, depth of use and teams that leave, and interview those that leave the same way you would churned customers.

## Output Formats

- **Retention Plan** — all four phases; use `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-retention/references/retention-plan-template.md`
- **Retention Strategy Brief** — 1–2 pages of priorities, owners and timelines
- **NRR/GRR Dashboard Specification** — definitions, data sources, calculation logic
- **Disengagement Signals and Health Score Model** — inputs, weights, thresholds, triggers
- **Churn Learning Review** — interview guide, reason taxonomy, findings routed to product
- **Expansion Playbook** — upsell/cross-sell triggers, talk tracks, measures

## Common Pitfalls

- **Treating retention as a renewal event** — By renewal time, the decision is usually made. Retention starts at onboarding.
- **Masking churn with expansion** — Always track GRR next to NRR.
- **Counting renewals but not use** — A renewed customer who stopped using the product is a future churn.
- **Not learning from churn** — Exit reasons logged as "price" with no interview. Talk to churned customers and route findings to product.
- **Treating all customers the same** — Segment by value, risk and persona.
- **Ignoring the product** — No retention program fixes a product that doesn't solve the customer's problem.
- **No budget for retention** — Retaining customers is usually far cheaper than acquiring new ones.
- **Measuring too late** — Lagging churn metrics only; build leading indicators into the plan.
- **Forgetting involuntary churn** — Payment failures are often a large and easy-to-fix share of churn.

## Pragmatic Principles

- **Outside-in** — Build from what customers need and how they experience the product.
- **NIHITO (Nothing Important Happens In The Office)** — Talk to current and churned customers; don't rely only on dashboards.
- **Your opinion, although interesting, is irrelevant** — Base strategy on customer feedback and behavior, not internal guesses about why customers stay or leave.

## Using AI in this focus area

- Analyze usage, support and billing data to find early disengagement patterns and draft health-score models.
- Summarize churned-customer interviews and support tickets into a consistent churn-reason taxonomy.
- Draft segment-specific renewal and expansion messaging from positioning.
- Rules: check AI output against real market evidence — talk to the market, NIHITO still applies; keep sensitive customer, contract and revenue data out of tools not approved for it; the team, not the tool, owns the decision. AI can flag accounts at risk, but it can't tell you *why* a customer is leaving — that takes a conversation.

## Reference Files

- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-retention/references/metrics-guide.md` — Definitions, formulas, benchmarks and interpretation for retention metrics, including NRR and retention economics.
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-retention/references/retention-plan-template.md` — Recommended structure for a full Retention plan.
