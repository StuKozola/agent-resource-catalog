---
name: product-profitability
description: >
  Guide product teams through Product Profitability analysis as defined by the Pragmatic Framework (formerly Pragmatic Marketing Framework). Use this skill whenever the user asks about product profitability, product P&L, product-level financial performance, product KPIs, product margin analysis, contribution margin by product, product revenue tracking, or monitoring how a product contributes to profit. Also trigger when the user mentions the Pragmatic Framework's Business category activities related to financial monitoring, product performance metrics, or profitability dashboards. This skill covers KPI selection, financial modeling, profitability dashboards, margin analysis (gross/contribution/net), and ongoing monitoring cadences. Use it even if the user doesn't say "Pragmatic" explicitly — any request to assess whether a product is making money, losing money, or how it impacts company operations falls squarely in this skill's scope.
---

# Product Profitability — Pragmatic Framework Skill

## Context: Where This Fits in the Pragmatic Framework

Product Profitability is one of the activities in the **Business** category of the Pragmatic Framework (the proven blueprint from Pragmatic Institute for building and marketing products people buy). The framework organizes 37 activities across 7 categories: Market, Focus, Business, Planning, Programs, Enablement, and Support.

The official definition from Pragmatic Institute:

> **Product Profitability**: Monitor and analyze key performance indicators to determine how well the product is performing in the market, how it impacts the company operations, and ultimately, how it contributes to profit. For internal products or services, instead of revenue or profit, determine success through improved usage or adoption rates.

Product Profitability sits alongside these sibling activities in the Business category:
- **Business Plan** — objective analysis of market opportunity and investment basis
- **Pricing** — pricing models, schedules, guidelines, and procedures
- **Buy, Build or Partner** — determining delivery approach for the solution
- **Innovation** — focusing creativity on solving market problems via distinctive competencies

Product Profitability is the *ongoing monitoring and analysis* layer. While Business Plan is forward-looking ("should we invest?") and Pricing is structural ("how do we charge?"), Product Profitability answers: **"Is this product actually making us money, and how much?"**

## Required Skills & Responsibilities

Per the Pragmatic Framework, the person or team owning Product Profitability needs:

**Responsibilities:**
1. Monitor and analyze KPIs to assess market performance
2. Evaluate how the product impacts company operations (costs, resources, complexity)
3. Determine the product's contribution to profit
4. For internal/non-revenue products: track usage and adoption as proxies for value

**Skills needed:**
- Analytical thinking
- Strategic thinking
- Financial acumen (P&L, margins, forecasting)
- Profit & loss understanding

## How to Use This Skill

When a user asks for help with product profitability, follow this workflow:

### Step 1: Clarify the Product Context

Before diving into analysis, understand what you're working with. Ask about:

- **Product type**: SaaS subscription, physical product, marketplace, internal tool, professional services, or hybrid?
- **Lifecycle stage**: Pre-launch, growth, mature, or declining?
- **Revenue model**: Subscription (MRR/ARR), one-time purchase, usage-based, freemium, advertising, licensing?
- **Current visibility**: Does the team already have product-level financials, or are they starting from scratch?

The product type and revenue model fundamentally shape which KPIs matter. A SaaS product and a physical goods product have very different cost structures and margin profiles.

### Step 2: Select the Right KPIs

Read `references/kpi-guide.md` for a comprehensive KPI reference organized by product type. At a high level, every product profitability analysis should cover three tiers:

**Tier 1 — Revenue Health** (Is the product generating income?)
- Total Revenue / Revenue Growth Rate
- Revenue by segment, channel, or geography
- Average Revenue Per User (ARPU) — for subscription/digital products
- MRR / ARR — for subscription products

**Tier 2 — Margin & Cost Efficiency** (Is the product generating *profit*?)
- Gross Margin (Revenue minus COGS, as a percentage of revenue)
- Contribution Margin (Revenue minus all variable costs)
- Operating Margin (after allocating operating expenses)
- Customer Acquisition Cost (CAC) and CAC Payback Period

**Tier 3 — Strategic & Operational Impact** (How does it affect the rest of the business?)
- Customer Lifetime Value (LTV) and LTV:CAC Ratio
- Product-level Net Profit Margin
- Operational cost impact (support tickets, infrastructure, team headcount)
- Cannibalization or halo effects on other products in the portfolio

For **internal products** (no direct revenue), substitute Tier 1 with:
- Active users / Adoption rate
- Time saved or efficiency gained (measured in FTE-hours or cost avoidance)
- Employee satisfaction / NPS for the tool
- Process error reduction rates

### Step 3: Build or Review the Financial Model

The core of product profitability analysis is a product-level P&L. If the user needs help building one, use the script at `scripts/generate_profitability_model.py` to create a starter spreadsheet, or guide them through building it manually.

A product P&L should follow this structure:

```
Revenue
  - Product Revenue (by stream if multiple)
  - Revenue adjustments (discounts, refunds, credits)
= Net Revenue

Cost of Goods Sold (COGS)
  - Direct production / hosting / infrastructure costs
  - Third-party licenses or data costs
  - Direct labor (support, customer success tied to product)
= Gross Profit
  → Gross Margin % = Gross Profit / Net Revenue × 100

Variable Expenses
  - Sales commissions
  - Transaction / payment processing fees
  - Variable marketing spend (performance/paid)
= Contribution Margin
  → Contribution Margin % = Contribution / Net Revenue × 100

Allocated Operating Expenses
  - Product team salaries (PM, engineering, design)
  - Marketing (brand, content — allocated share)
  - G&A allocation
  - R&D allocation
= Operating Profit
  → Operating Margin % = Operating Profit / Net Revenue × 100

Below-the-line adjustments
  - Depreciation / amortization of capitalized dev costs
  - Interest on product-specific debt
= Product Net Profit
  → Net Margin % = Net Profit / Net Revenue × 100
```

**Common pitfalls in product P&L construction:**
- **Over-allocating shared costs**: If your company has 5 products and you allocate 20% of the CEO's salary to each, the numbers become meaningless. Use activity-based costing where possible, and clearly separate direct costs from allocations.
- **Ignoring COGS for SaaS**: SaaS products still have COGS — hosting, third-party APIs, customer success labor. A common mistake is treating SaaS as "zero marginal cost."
- **Mixing up contribution margin and gross margin**: Gross margin subtracts COGS only. Contribution margin subtracts all variable costs (including sales commissions, transaction fees, etc.). Both are useful; don't conflate them.
- **Forgetting opportunity cost**: A product consuming 40% of engineering time but generating 10% of revenue has a high hidden cost even if its standalone P&L looks acceptable.

### Step 4: Establish a Monitoring Cadence

Product profitability isn't a one-time exercise. Recommend a cadence:

| Review Type | Frequency | Focus | Audience |
|---|---|---|---|
| KPI Dashboard Check | Weekly | Revenue trends, anomalies, leading indicators | Product team |
| Margin Review | Monthly | Gross/contribution margin trends, cost changes | Product + Finance |
| Full P&L Review | Quarterly | Complete product P&L, strategic assessment | Leadership / Portfolio |
| Deep Profitability Audit | Annually | Full cost allocation review, benchmark vs. competitors, sunset analysis | Executive team |

### Step 5: Interpret and Act on Findings

The point of monitoring is to drive decisions. Common actions that emerge from product profitability analysis:

- **Healthy and growing margins** → Invest more (expand marketing, add features, enter new segments)
- **Revenue growing but margins declining** → Investigate cost creep (infrastructure scaling, support burden, discount abuse)
- **Flat or declining revenue with stable margins** → Market saturation or competitive pressure; consider repositioning or innovation
- **Negative contribution margin** → The product loses money on every unit sold. Either fix pricing/costs urgently or consider sunsetting
- **Strong contribution margin, negative operating margin** → The product covers its variable costs but can't justify its team overhead at current scale. Needs growth or cost restructuring
- **Internal product with low adoption** → Re-evaluate whether the problem it solves is real and urgent; consider repositioning or sunsetting

### Step 6: Communicate Results

Product profitability findings should feed into:
- **Business Plan** updates — is the original investment thesis holding?
- **Pricing** reviews — are margins where the pricing model predicted?
- **Product Portfolio** decisions — should this product be grown, maintained, or retired?
- **Stakeholder Communications** — regular updates to leadership on product health

## Output Formats

When helping the user, produce deliverables appropriate to their request:

1. **KPI Dashboard Specification** — a document listing recommended KPIs, definitions, data sources, targets, and owners. Produce as a markdown file or Word doc.
2. **Product P&L Spreadsheet** — use `scripts/generate_profitability_model.py` to create an Excel workbook with formulas. Read the xlsx skill at `/mnt/skills/public/xlsx/SKILL.md` before generating spreadsheets.
3. **Profitability Analysis Report** — a narrative document interpreting the numbers and recommending actions. Read the docx skill at `/mnt/skills/public/docx/SKILL.md` before generating Word documents.
4. **Executive Presentation** — slides summarizing product profitability for leadership. Read the pptx skill at `/mnt/skills/public/pptx/SKILL.md` before generating presentations.
5. **Monitoring Cadence Plan** — a lightweight document defining who reviews what, when, and what triggers escalation.

Always match the deliverable to what the user actually needs. If they just want help thinking through KPIs, a conversational response may be enough — not everything needs a 20-page report.

## Key Formulas Quick Reference

```
Gross Margin %          = (Net Revenue - COGS) / Net Revenue × 100
Contribution Margin %   = (Net Revenue - Variable Costs) / Net Revenue × 100
Operating Margin %      = Operating Profit / Net Revenue × 100
Net Profit Margin %     = Net Profit / Net Revenue × 100
CAC                     = Total Sales & Marketing Spend / New Customers Acquired
LTV                     = ARPU × Gross Margin % × (1 / Churn Rate)
LTV:CAC Ratio           = LTV / CAC  (target: >3:1)
CAC Payback Period      = CAC / (ARPU × Gross Margin %)  (in months)
Break-Even Units        = Fixed Costs / Contribution Margin per Unit
Break-Even Revenue      = Fixed Costs / Contribution Margin Ratio
```

## Industry Benchmarks (General Guidance)

For context when interpreting margins — these are rough benchmarks, not targets:

- **SaaS Products**: Gross margin 70-85%, operating margin 15-25% at maturity
- **E-commerce / Physical Products**: Gross margin 25-50%, operating margin 5-15%
- **Marketplace / Platform**: Gross margin 60-75% (on take rate), operating margin 10-30%
- **Professional Services**: Gross margin 30-50%, operating margin 10-20%

Always benchmark against the specific industry and stage. A pre-profit growth-stage SaaS product with 75% gross margins but -20% operating margin may be perfectly healthy if growth justifies the investment.

## Additional References

- `references/kpi-guide.md` — Detailed KPI definitions organized by product type (SaaS, physical, marketplace, internal)
- `references/profitability-checklist.md` — Step-by-step checklist for conducting a product profitability review
