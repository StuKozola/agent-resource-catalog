---
name: pragmatic-business-outcomes
description: >
  Guide product teams through the Business Outcomes focus area of the Pragmatic Framework (Pragmatic Institute, 2027; formerly Product Profitability) — "Is the product delivering the results the business expected?" Use whenever the user asks whether a product is doing what its business plan said it would, or about product results such as revenue, profit, margin, efficiency, cost reduction or ROI. Triggers: business outcomes, product profitability, product P&L, product-level financial performance, margin or contribution margin by product, customer profitability, which products or customers create or consume profit, product revenue tracking, ROI of a product or internal platform, stage-appropriate success measures (validation and adoption before profit), grow/maintain/sunset reviews. For choosing early indicators use pragmatic-measurement; for whether customers got their outcome use pragmatic-customer-value-realization.
---

# Business Outcomes — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Business — *Is this a good investment, and is it paying off?*
- **Focus-area question:** *Is the product delivering the results the business expected?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Business Plan, Pricing, Buy, Build or Partner, Measurement
- **Formerly:** Product Profitability
- **Related Pragmatic Institute course:** Price (covers Pricing and Business Outcomes)

## What This Focus Area Is

Business Outcomes describes how the product contributes to the organization's results — **revenue, profit, margin, efficiency, cost reduction and return on investment**. Tracking those results answers one plain question: **is the product doing what the business plan said it would?**

Profit is still central: measure it by subtracting all related costs from revenue, and look at **which products and which customers create profit and which consume it**. But profit is not the only outcome, and not always the right one yet. **Choose outcomes that fit the product's stage** — an early product may be judged on validation and adoption long before it is expected to be profitable.

How it relates to its siblings:
- **Business Plan** is forward-looking ("why is this worth funding?") and sets the expected results.
- **Pricing** is structural ("how will we capture the value?").
- **Buy, Build or Partner** decides the delivery path and its costs.
- **Measurement** defines the indicators, leading and lagging, that show early whether things are on track.
- **Business Outcomes** checks the actual results against the plan.

## Boundary: Measurement vs. Business Outcomes vs. Customer Value Realization

| Focus area | Question | Owns |
|---|---|---|
| **Measurement** (Business) — `pragmatic-measurement` | Which indicators tell us early whether this is working? | Defining the indicators, leading (e.g., incoming leads, trial starts) and lagging (e.g., product sales), and how they're tracked |
| **Business Outcomes** (Business) — this skill | Is the product delivering the results the business expected? | Results for *your organization*: revenue, profit, margin, efficiency, cost reduction, ROI, stage-appropriate milestones |
| **Customer Value Realization** (Operations) — `pragmatic-customer-value-realization` | Did customers get the outcome they bought the product for? | Results for *the customer*: agreed success criteria and evidence they were met |

They connect: Measurement's leading indicators warn early; Business Outcomes confirms the organization's results; customers who realize value renew and expand, which shows up later in Business Outcomes. Don't use revenue as a stand-in for customer value, or customer satisfaction scores as a stand-in for business results.

## Responsibilities

1. Translate the business plan's expectations into tracked outcomes and targets
2. Choose stage-appropriate outcomes for each product
3. Monitor and analyze results — revenue, profit, margin, efficiency, cost reduction, ROI
4. Identify which products and customers create or consume profit
5. Evaluate how the product affects company operations (costs, resources, complexity)
6. Report results honestly and recommend actions (invest, fix, restructure, sunset)

**Skills needed:** analytical and strategic thinking; financial acumen (P&L, margins, forecasting); comfort presenting bad news to leadership.

## Stage-Appropriate Outcomes

| Stage | Primary outcomes to judge it on | Profit expectation |
|---|---|---|
| **Pre-launch / validation** | Problem and solution validated with the market; pilot or design-partner commitments; early willingness to pay | None — track burn against plan |
| **Early adoption** | Activation and meaningful use (see `pragmatic-adoption`); early retention; first revenue; unit-economics trend | Gross margin direction, not level |
| **Growth** | Revenue growth, net revenue retention, LTV:CAC, CAC payback, gross margin | Contribution margin positive and improving |
| **Mature** | Operating and net margin, profit contribution, efficiency, customer profitability | Expected to contribute profit |
| **Declining** | Contribution margin, cost to serve, migration of customers | Positive contribution, or plan to sunset |

Agree the stage and its outcomes with leadership up front, ideally in the business plan, so a young product isn't judged on profit too soon and a mature one isn't excused for poor margins.

## How to Use This Skill

### Step 1: Clarify the Product Context

- **What did the business plan promise?** Expected results, timing, key assumptions. If there's no plan, reconstruct the expectations leadership holds.
- **Product type**: SaaS subscription, physical product, marketplace, internal tool, professional services, or hybrid?
- **Lifecycle stage**: validation, early adoption, growth, mature, or declining?
- **Revenue model**: one-time, subscription, usage-based, freemium, advertising, licensing?
- **Current visibility**: Are product-level and customer-level financials available, or starting from scratch?

### Step 2: Select Outcomes and KPIs

Read `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-business-outcomes/references/kpi-guide.md` for definitions organized by product type and stage. Cover the outcome types that fit the stage:

- **Revenue** — total revenue and growth rate; revenue by segment, channel or geography; ARPU; MRR/ARR; net revenue retention
- **Profit and margin** — gross, contribution, operating and net margin; product net profit
- **Efficiency** — CAC and payback, LTV:CAC, revenue per employee, cost to serve, cost of revenue %
- **Cost reduction** — costs removed from the business (for the company or, for internal products, for other teams)
- **ROI** — return on the investment the business plan asked for
- **Validation and adoption** (early stage) — validated problems, pilot conversions, activation and active use

Leading indicators that predict these results are defined in Measurement; use them, don't duplicate them.

### Step 3: Build or Review the Product P&L

A product P&L is the core profit view. Build it as a spreadsheet (use the xlsx skill) or guide the user through it:

```
Revenue
  - Product Revenue (by stream if multiple)
  - Revenue adjustments (discounts, refunds, credits)
= Net Revenue

Cost of Goods Sold (COGS)
  - Direct production / hosting / infrastructure / AI inference costs
  - Third-party licenses or data costs
  - Direct labor (support, customer success tied to product)
= Gross Profit                → Gross Margin %

Variable Expenses
  - Sales commissions, transaction / payment fees, variable marketing
= Contribution Margin         → Contribution Margin %

Allocated Operating Expenses
  - Product team (PM, engineering, design), marketing share, G&A, R&D
= Operating Profit            → Operating Margin %

Below-the-line adjustments
  - Depreciation / amortization of capitalized dev costs
= Product Net Profit          → Net Margin %
```

**Common P&L pitfalls:**
- **Over-allocating shared costs** — Spreading overhead evenly makes the numbers meaningless. Use activity-based costing where possible and separate direct costs from allocations.
- **Ignoring COGS for SaaS** — Hosting, third-party APIs, model inference and customer success labor are real marginal costs.
- **Mixing up contribution and gross margin** — Gross subtracts COGS only; contribution subtracts all variable costs.
- **Forgetting opportunity cost** — A product consuming 40% of engineering time for 10% of revenue has a high hidden cost.

### Step 4: Find Who Creates and Consumes Profit

Averages hide problems. Break results down:
- **By product** — Which products, editions or SKUs carry the portfolio, and which drain it? Feed this to Product Portfolio (Focus).
- **By customer or segment** — Cost to serve (support load, custom work, discounts, implementation effort) vs. revenue. Some large customers consume profit; some small segments are highly profitable.
- **By channel** — Partner and direct sales often have very different margins.

Repeated custom work or one-off terms for unprofitable customers are worth logging as Exceptions (Operations).

### Step 5: Compare Results to the Business Plan

For each expected outcome: target, actual, variance, and why. Separate **assumption errors** (the market was smaller, adoption slower, costs higher) from **execution gaps**. Send corrected assumptions back to the Business Plan so the next fund/delay/stop decision uses better numbers.

### Step 6: Establish a Review Cadence

| Review Type | Frequency | Focus | Audience |
|---|---|---|---|
| Outcome dashboard check | Monthly | Results vs. targets; anomalies (leading indicators live in Measurement) | Product team |
| Margin and cost review | Monthly | Gross/contribution margin trends, cost changes, cost to serve | Product + Finance |
| Business outcomes review | Quarterly | Full P&L, results vs. business plan, product and customer profitability | Leadership / Portfolio |
| Deep audit | Annually | Cost allocation review, benchmarks, stage reassessment, sunset analysis | Executive team |

### Step 7: Interpret and Act

- **On or ahead of plan, healthy margins** → Invest more (marketing, features, new segments)
- **Revenue growing but margins declining** → Investigate cost creep (infrastructure, support burden, discounting)
- **Flat or declining revenue with stable margins** → Saturation or competitive pressure; revisit positioning, Growth or Ideation
- **Negative contribution margin** → Losing money on every sale; fix pricing or costs urgently, or sunset
- **Strong contribution margin, negative operating margin** → Needs scale or cost restructuring
- **Early product missing validation or adoption milestones** → Revisit the market problem and requirements before adding spend
- **Internal product with low adoption or weak ROI** → Re-check whether the problem is real and urgent; reposition or retire

### Step 8: Communicate Results

Findings feed:
- **Business Plan** (Business) — is the investment case holding? Update assumptions.
- **Pricing** (Business) — are margins where the pricing model predicted?
- **Product Portfolio** (Focus) — grow, maintain, restructure or retire?
- **Product Roadmap** (Focus) — which outcomes come next?
- **Stakeholder Management** (Planning) — regular, honest updates to leadership

## Internal Products and Platforms

For products with no direct revenue, outcomes are expressed as **adoption, efficiency, cost reduction and ROI**: active use by eligible users, time saved, errors reduced, costs avoided, and ROI = (value created − total cost of ownership) ÷ total cost of ownership. Stage still matters — a new platform is judged on adoption first, ROI later. Funding and cost allocation are covered in `pragmatic-pricing`.

## Output Formats

1. **Outcomes Dashboard Specification** — outcomes, KPIs, definitions, data sources, targets (from the business plan), stage, owners. Markdown or Word.
2. **Product P&L Spreadsheet** — Excel workbook with formulas (use the xlsx skill).
3. **Business Outcomes Report** — results vs. plan, product and customer profitability, recommended actions (use the docx skill for Word).
4. **Executive Presentation** — slides for leadership (use the pptx skill).
5. **Review Cadence Plan** — who reviews what, when, and what triggers escalation.

Match the deliverable to the need; a conversational answer is sometimes enough.

## Key Formulas Quick Reference

```
Gross Margin %          = (Net Revenue - COGS) / Net Revenue × 100
Contribution Margin %   = (Net Revenue - Variable Costs) / Net Revenue × 100
Operating Margin %      = Operating Profit / Net Revenue × 100
Net Profit Margin %     = Net Profit / Net Revenue × 100
Customer Profit         = Customer Revenue - Cost to Serve that Customer
CAC                     = Total Sales & Marketing Spend / New Customers Acquired
LTV                     = ARPU × Gross Margin % × (1 / Churn Rate)
LTV:CAC Ratio           = LTV / CAC  (target: >3:1)
CAC Payback Period      = CAC / (ARPU × Gross Margin %)  (in months)
ROI                     = (Value or Profit Created - Investment) / Investment × 100
Break-Even Revenue      = Fixed Costs / Contribution Margin Ratio
```

## Industry Benchmarks (General Guidance)

Rough benchmarks, not targets: SaaS gross margin 70–85% and operating margin 15–25% at maturity; e-commerce/physical gross 25–50%, operating 5–15%; marketplace gross 60–75% on take rate, operating 10–30%; professional services gross 30–50%, operating 10–20%. Always benchmark against the specific industry and stage — a growth-stage SaaS product with 75% gross margin and −20% operating margin may be healthy if growth justifies it.

## Using AI in this focus area

AI can help reconcile and summarize financial data, draft variance explanations against the business plan, spot outliers in product or customer profitability, and turn results into leadership-ready narratives. Rules:
- Check AI output against the source numbers and real market evidence; AI can explain a variance plausibly and wrongly. Talking to customers (NIHITO) still explains *why* results moved.
- Keep sensitive financial, customer and deal data out of tools not approved for it.
- The team, not the tool, owns the conclusions and the invest/fix/sunset recommendation.

## Reference Files

- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-business-outcomes/references/kpi-guide.md` — Outcome and KPI definitions by product type and stage, including customer profitability and internal products, plus a selection decision tree
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-business-outcomes/references/business-outcomes-checklist.md` — Step-by-step checklist for a business outcomes review
