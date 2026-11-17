---
name: pragmatic-growth
description: Guide users through Growth planning per the 2027 Pragmatic Framework (Go-to-Market category; formerly Revenue Growth). Growth answers "Where will new revenue or new users come from?" and covers the programs and experiments that bring in new revenue, new users and expanded use — or, for internal products, broader adoption across the organization. Use whenever the user mentions growth plan, revenue growth, new customer acquisition, new logo targets, new user acquisition, acquisition budget or strategy, growth levers, trial conversion, product-led growth, expanding into new segments, growth experiments, growth forecasting with CAC, churn and recurring revenue, pipeline math, or internal platform adoption targets. Do NOT use for keeping existing customers, renewals, churn reduction or net revenue retention — use pragmatic-retention.
---

# Growth — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Go-to-Market — *How will the market find, choose and stay with the product?*
- **Focus-area question:** *Where will new revenue or new users come from?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Marketing Plan, Retention, Launch, Organizational Alignment, Awareness, Engagement, Customer Satisfaction
- **Formerly:** Revenue Growth

## Purpose

Growth is the set of programs and experiments that bring in **new revenue, new users and expanded use**. For a commercial product it's usually expressed as revenue growth over time. For an internal product it means broader adoption across the organization.

Typical levers are **pricing, converting trials, expanding into new segments and focusing on high-impact features**. Forecasts rest on **customer acquisition cost (CAC), churn and recurring revenue**.

The pre-2027 Revenue Growth focus area was limited to plans and budgets for new customers. The 2027 version is broader: new users and expanded use count, and growth is driven by experiments as well as funded plans.

### Boundary with Retention

Retention (`pragmatic-retention`) owns keeping customers and deepening their value: renewal, continued use, account-level expansion and net revenue retention. Growth owns bringing in new customers and users and opening new sources of use (new segments, new teams, new use cases). Expansion inside existing accounts can appear in both plans; agree which plan owns each expansion target so it isn't counted twice, and share churn and expansion assumptions so the two forecasts agree.

## Framework Context

**Inputs:**
- **Market Definition** (Focus) and **Buyer Personas** (Planning) — target segments and buyers
- **Positioning** (Planning) — how the product solves market problems for each persona
- **Buyer Journey** (Planning) — how buyers move from need to decision (`pragmatic-buyer-journey`)
- **Pricing** (Business) — model, packaging, trial and entry offers (`pragmatic-pricing`)
- **Distribution Strategy** (Focus) — how people find, buy and get the product
- **Business Plan** (Business) — financial model and investment basis
- **Competitive Landscape** (Market) — alternatives, including doing nothing
- **Marketing Plan** (Go-to-Market) — the annual plan Growth programs sit within

**Feeds:**
- **Organizational Alignment** (Go-to-Market) — sales, success and support share the growth targets and audience (`pragmatic-organizational-alignment`)
- **Engagement** and **Awareness** (Go-to-Market) — programs that fill and move the funnel
- **Content** and **Assets** (Enablement) — materials to execute growth programs
- **Channel Support** (Enablement) — partners who sell, deliver or support the product
- **Product Roadmap** (Focus) — high-impact features that unlock growth
- **Measurement** (Business) — growth indicators, leading and lagging

## Key Principles

1. **Outside-in.** Growth plans start with how buyers want to buy and what users need, not how the company wants to sell.
2. **Pick the source.** Be explicit about where growth comes from: new customers, new users in existing customers, new segments, new use cases.
3. **Experiment, then fund.** Treat each lever as a hypothesis. Test it small, then put budget behind what works.
4. **Plans and budgets.** Targets need funded plans with channel investments, headcount and timeline commitments.
5. **Market-driven channels.** Choose channels from buyer preferences and the Distribution Strategy, not internal convenience.
6. **Measurable targets.** New revenue, new users, CAC, conversion rates and pipeline — tied to the Business Plan model.

## Workflow

Adapt depth and sequence to what the user already has.

### Step 1: Gather Inputs

Ask about:
- **Target segments and personas** — who are the ideal new customers or users?
- **Positioning** — how the product solves their specific problems
- **Buyer journey** — steps and barriers from need to decision
- **Pricing model** — trials, freemium, entry offers, land-and-expand, usage-based options
- **Distribution channels** — direct, partners, self-serve, marketplace
- **Competitive landscape** — main alternatives for new-customer attention
- **Baseline** — current new revenue, new users, recurring revenue, churn, CAC

If critical inputs are missing, name the focus area that would supply them and keep going with stated assumptions.

### Step 2: Set Growth Targets

Define quantified targets by source:
- **New-customer revenue** and **new-logo count**
- **New users / active teams** (product-led or internal products)
- **Expanded use** — new segments, teams or use cases (agree ownership with Retention)
- **Average deal size**, **by segment**, **by quarter with ramp assumptions**

```
New-Customer Revenue Target = New-Logo Target × Average Deal Size
```

Cross-check against the Business Plan and Market Definition (TAM/SAM/SOM).

### Step 3: Choose Growth Levers

For each lever, write the hypothesis, the evidence, the experiment that tests it and the expected impact:
- **Pricing** — packaging, entry tiers, usage-based options (coordinate with `pragmatic-pricing`)
- **Trial conversion** — trial or freemium to paid or active use; onboarding friction
- **New segments** — adjacent segments or geographies backed by market-problem evidence
- **High-impact features** — the few features that unlock a new buyer or new use (feed to the roadmap)

### Step 4: Define Acquisition Channels

Selection criteria: where target buyers discover and evaluate solutions (Buyer Journey), what Distribution Strategy specifies, expected CAC per channel, capacity and scalability.

Common channels: direct sales, inbound content and SEO, paid digital, partners and resellers, product-led (trial, freemium, self-serve), events and webinars, account-based marketing, referral programs.

For each channel: segments served, expected contribution, budget, tactics, timeline, owner.

### Step 5: Build the Budget and Pipeline Model

Budget categories: personnel, demand generation, sales enablement and tooling, partner programs, product-led infrastructure, ABM and referral programs.

Validation:
- Target CAC = Total Acquisition Budget ÷ New-Logo Target
- CLV:CAC ≥ 3:1
- Pipeline coverage typically 3–5× target

```
Required Pipeline      = Revenue Target ÷ Win Rate
Required Opportunities = Required Pipeline ÷ Average Deal Size
Required SQLs          = Required Opportunities ÷ SQL-to-Opportunity Rate
Required MQLs          = Required SQLs ÷ MQL-to-SQL Rate
Required Leads         = Required MQLs ÷ Lead-to-MQL Rate
```

### Step 6: Forecast and Measure

Forecast with CAC, churn and recurring revenue (see `references/acquisition-metrics-guide.md`, "Forecasting Growth"). Track:
- **Outcomes:** new revenue, new logos, new users, CAC, CAC payback, CLV:CAC
- **Funnel:** pipeline generated and coverage, stage conversion, trial-to-paid, sales cycle, win rate
- **Channels:** CPL, conversion, revenue contribution, ROI
- **Leading indicators:** MQLs, SQLs, trial and demo requests, target-segment traffic

### Step 7: Assemble and Review

Use `references/growth-plan-template.md`. Then check: Does it match the Business Plan? Are targets realistic for the segment size and competition? Does the budget support the pipeline math? Are churn and expansion assumptions consistent with Retention? Is there a quarterly review?

## Internal Products

For internal platforms and tools, growth is **broader adoption across the organization**: more teams, more active users, more workflows moved onto the platform. Replace revenue with active users or teams, CAC with the effort to onboard a team, and churn with teams that stop using it. Levers still apply: pricing becomes cost allocation or chargeback, trials become pilots, new segments become new departments or regions. Hand off sustained use to `pragmatic-adoption` (Enablement).

## Output Formats

1. **Growth Plan** — targets, levers, channels, budget, metrics, timeline (template)
2. **Growth Lever / Experiment Plan** — hypotheses, tests and expected impact
3. **Acquisition Budget** — by channel and category
4. **Pipeline Model** — leads → MQLs → SQLs → opportunities → closed-won
5. **Growth Forecast** — recurring revenue built from CAC, churn and expansion assumptions
6. **Executive Summary** — one page on targets, key bets and expected return

## Common Pitfalls

- **Unclear growth source** — Mixing new customers, new users and account expansion in one number hides what's working. Report each source.
- **Double counting expansion** — Expansion counted in both Growth and Retention plans. Agree ownership.
- **Targets without funded plans** — Every target needs a funded path.
- **Scaling an untested lever** — Spending heavily on a pricing change or new segment before a small test shows it works.
- **Ignoring the buyer journey** — Plans built around internal capabilities instead of how buyers find and buy.
- **Ignoring churn in the forecast** — High churn turns acquisition into refilling a leaking bucket.
- **Channel concentration** — Diversify across at least 2–3 channels; track CAC by channel.
- **Disconnected from Organizational Alignment** — Growth plans not shared with sales, success and support underperform.

## Using AI in this focus area

- Build and stress-test pipeline and recurring-revenue forecasts under different CAC, churn and conversion assumptions.
- Analyze trial and product-usage data to find where conversion drops and which features correlate with conversion.
- Draft growth hypotheses and experiment designs for each lever, and summarize experiment results.
- Rules: check AI output against real market evidence — talk to the market, NIHITO still applies; keep sensitive customer, deal and company data (pipeline, pricing, revenue) out of tools not approved for it; the team, not the tool, owns the decision. AI can find correlations in usage data but can't tell you why a segment buys — that still takes buyer interviews.

## Reference Files

- `references/growth-plan-template.md` — Full Growth Plan template, including growth levers. **Load when the user wants a complete plan.**
- `references/acquisition-metrics-guide.md` — Acquisition metrics, formulas, benchmarks and growth forecasting. **Load when defining or calculating KPIs or building a forecast.**
