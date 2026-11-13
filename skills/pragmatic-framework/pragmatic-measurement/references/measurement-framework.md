# Measurement Framework Reference

Reference for the Measurement focus area (Business category, 2027 Pragmatic Framework): *Which indicators tell us early whether this is working?* Measurement sets the indicators for product, strategy and go-to-market work. Business Outcomes (`pragmatic-business-outcomes`) tracks results for the organization; Customer Value Realization (`pragmatic-customer-value-realization`) asks whether customers got their outcome.

## Table of Contents
1. [The Goal Cascade: Corporate → Product → Strategy and Go-to-Market](#the-goal-cascade)
2. [Leading vs. Lagging Indicators](#leading-vs-lagging)
3. [Seven Essential Product and Go-to-Market Metrics](#seven-essential-metrics)
4. [Indicators by Focus Area](#indicators-by-focus-area)
5. [KPI Selection Criteria](#kpi-selection-criteria)
6. [Common KPI Mistakes to Avoid](#common-kpi-mistakes)
7. [Metrics vs KPIs: The Distinction That Matters](#metrics-vs-kpis)
8. [Attribution Models](#attribution-models)
9. [Reporting Cadences and Audiences](#reporting-cadences)
10. [The Tune Process: From Data to Action](#the-tune-process)
11. [SaaS-Specific Measurement Considerations](#saas-measurement)
12. [B2B vs B2C Measurement Differences](#b2b-vs-b2c)

---

## The Goal Cascade

The 2027 Pragmatic Framework places Measurement in the Business category: it is the early-warning system for whether product, strategy and go-to-market work is paying off. The fundamental principle is that indicators must cascade from corporate goals.

**Level 1 — Corporate Goals**
These are set by the executive team and board. Common examples:
- Grow annual revenue by X%
- Achieve profitability by target date
- Expand into new market segments
- Increase market share from X% to Y%
- Improve customer retention to X%

**Level 2 — Product Goals**
Product goals translate corporate objectives into product-level targets:
- Product revenue targets (new business + renewals)
- Product adoption rates (users, usage frequency, feature adoption)
- Product retention and churn rates
- Product market share within defined segments
- Customer satisfaction scores (NPS, CSAT)

**Level 3 — Strategy and Go-to-Market Indicators**
These show how strategy, product and go-to-market work contribute to product goals. Go-to-market examples:
- Pipeline generated and pipeline influenced
- Marketing-sourced revenue
- Customer acquisition cost (CAC)
- Customer lifetime value (CLV)
- Marketing-influenced close rate
- Lead-to-customer conversion rate
- Net revenue retention (NRR) influence

Product and strategy examples:
- Activation rate and time to first value for new users
- Adoption of features tied to a strategic bet or roadmap outcome
- Win rate in the target segment named in the product strategy
- Share of evaluations that include the product

**Level 4 — Diagnostic Metrics**
These explain movement in the KPIs above:
- Website traffic by source and segment
- MQL and SQL volume and velocity
- Content engagement rates
- Campaign-specific conversion rates
- Email and engagement program performance
- Event attendance and follow-up engagement
- Product usage events and funnel steps

---

## Leading vs. Lagging Indicators

- **Leading indicators** predict results and arrive early enough to act on. Example: incoming leads.
- **Lagging indicators** confirm results after the fact. Example: product sales.

Every goal needs at least one lagging indicator (did it happen?) and one or two leading indicators (is it going to happen?).

| Goal | Lagging (confirms) | Leading (predicts) |
|---|---|---|
| New revenue | Product sales, new ARR | Incoming qualified leads, pipeline created, trial starts, demo requests |
| Retention | Renewal rate, gross revenue retention, churn | Active use, activation, declining logins, support escalations, health score |
| Expansion | Expansion revenue, NRR | Usage growth, seats added, adoption of premium features |
| Strategy bet lands | Segment revenue or share | Win rate in segment, share of evaluations, problem awareness in segment |
| Roadmap outcome | Outcome metric named on the roadmap | Adoption of the shipped capability in the first 30–90 days |
| Launch success | Launch revenue goal | Sales readiness, pipeline in launch window, early adoption |
| Internal platform value | Cost reduction, ROI | Onboarding completion, active teams, workloads migrated |

**Rules of thumb**
- Validate that the leading indicator actually moves first, using your own history. If it doesn't predict, replace it.
- Leading indicators are easier to game (e.g., lowering the bar for a "qualified" lead). Pair them with a quality check.
- Review leading indicators often (weekly or monthly); lagging indicators less often (monthly or quarterly).
- Lagging results for the organization are reported in Business Outcomes; Measurement keeps the definitions consistent.

---

## Seven Essential Product and Go-to-Market Metrics

Pragmatic Institute identifies seven metrics product teams and product marketers should track. They cover the outcomes product and go-to-market work are expected to influence: sales support, market adoption, and customer retention. The type column shows how each usually behaves.

| Metric | Usually |
|---|---|
| Adoption rate | Leading (for retention) |
| Retention rate | Lagging |
| Revenue | Lagging |
| Average length of a sale | Leading (for revenue timing) |
| Close rate | Leading/lagging, depending on use |
| Customer lifetime value | Lagging |
| Customer acquisition cost | Lagging (efficiency) |

### 1. Adoption and Adoption Rate
- **What it measures:** How many customers are actively using the product and its specific features
- **Why it matters:** High adoption correlates with higher retention and lower churn; it's a leading indicator of future retention issues
- **Key questions:** Are features built for a handful of demanding customers while the broader base ignores them? Do customers try the product once and disengage?
- **Formula:** Active users in period / Total customers
- **Feature-level:** Users of Feature X / Total active users

### 2. Retention and Retention Rate
- **What it measures:** How many customers remain customers at renewal time
- **Why it matters:** Acquiring new customers costs far more than retaining existing ones; small improvements yield outsized returns
- **Formula:** (Customers at End of Period − New Customers During Period) / Customers at Start of Period
- **Example:** 1,000 customers, 85% retention = 850 remaining. To grow 30%, you need 450 new customers (150 to replace churn + 300 for growth), not just 300.
- **Key questions:** Is the rate trending up or down over time? Does it vary across market segments?
- **Inverse: Churn Rate** — the rate at which customers leave. Churn and retention have an inverse relationship.

### 3. Revenue
- **What it measures:** Income generated by product sales
- **Why it matters:** Directly connects to corporate goals; the ultimate outcome metric
- **Supporting metric — Average Selling Price (ASP):** The average price at which the product sells over a period. Understanding ASP by segment reveals pricing effectiveness and helps identify unrealistic revenue targets.
- **Key questions:** How does actual revenue track against the goal? Does ASP vary across market segments?

### 4. Average Length of a Sale
- **What it measures:** Time from initial qualified buyer contact to completed sale
- **Why it matters:** A lengthening sales cycle means more resources needed to hit revenue targets; a shortening cycle means the team can sell more with fewer resources
- **Key questions:** Is the cycle consistent across segments? Which segments have notably shorter or longer cycles, and why?
- **Connection to go-to-market:** Effective Awareness, Engagement and Organizational Alignment work should shorten this metric over time

### 5. Close Rate
- **What it measures:** Percentage of leads that complete a purchase
- **Formula:** Conversions / Total Leads
- **Why it matters:** Highlights gaps in marketing performance, sales performance, or product-market fit. Small improvements have significant business impact.
- **Key questions:** Does the rate vary across segments? Are low rates caused by poor targeting, ineffective enablement, or weak product-market fit?

### 6. Customer Lifetime Value (CLV)
- **What it measures:** Total profit a customer delivers from acquisition to churn
- **Why it matters:** Informs which markets to pursue, how much to spend on acquisition, and which positioning strategies to invest in
- **Key questions:** Are some customer segments dramatically more valuable? Are any customers costing more than they generate? How much should you spend to acquire or retain a high-CLV customer?
- **Formula:** Average Revenue Per Account × Gross Margin % × Average Customer Lifespan

### 7. Customer Acquisition Cost (CAC)
- **What it measures:** Total cost to acquire a single customer
- **Why it matters:** Must decrease over time for sustainable growth; varies dramatically between markets
- **Formula:** Total Sales & Marketing Spend / Number of New Customers Acquired
- **Key questions:** Are there outlier segments where acquisition costs vastly exceed others? Is CAC trending down as programs mature?
- **Critical ratio — CLV:CAC:** A healthy ratio is generally 3:1 or higher. Below 3:1 suggests unsustainable acquisition economics.

---

## Indicators by Focus Area

Common indicators for focus areas that Measurement supports. Category in parentheses.

### Awareness (Go-to-Market) — Top of Funnel
- Impressions and reach within target segments
- Website traffic from target segments (by source)
- Brand awareness surveys (aided and unaided recall)
- Share of voice in target market
- Content consumption (downloads, views, time on page)

### Engagement (Go-to-Market) — Interest to Evaluation and Trial
- MQL volume and MQL conversion rate
- SQL volume and SQL conversion rate
- Lead velocity rate (month-over-month growth in qualified leads)
- Engagement program activity (email opens, clicks, content progression, event follow-up)
- Trial starts and trial-to-paid conversion
- Time in stage (how long leads spend at each funnel stage)

### Launch (Go-to-Market) — Cross-Funnel
- Launch goal achievement (unique to each launch)
- Pipeline generated within launch window
- Win rate changes pre/post launch
- Sales team readiness scores
- Market awareness lift (pre/post launch surveys)

### Customer Satisfaction (Go-to-Market) — Experience and Relationship
- CSAT and NPS trends (signals of satisfaction, not the definition of it)
- Relationship health and trust scores
- Number of willing reference customers and referral-sourced pipeline
- Review-site ratings and sentiment
- Case studies produced (an Assets output)

### Adoption (Enablement) — Meaningful Use
- Activation rate and time to first value
- Active users / eligible users
- Adoption of key features and workflows
- Onboarding completion

### Growth (Go-to-Market) — New Revenue and New Users
- New logo revenue and new users vs. target
- Pipeline coverage ratio (3x–4x target is healthy)
- Win rate on new business opportunities
- Average deal size for new customers
- Time to first value (for new customer onboarding)

### Retention (Go-to-Market) — Existing Business
- Net Revenue Retention (NRR)
- Gross Revenue Retention (GRR)
- Expansion revenue (upsell + cross-sell)
- Renewal rate
- Customer health scores

### Product Strategy and Product Roadmap (Market, Focus)
- Win rate and share of evaluations in the target segment
- Adoption of capabilities tied to each roadmap outcome
- Requests and exceptions related to what the strategy says no to (signals pressure on the strategy)

---

## KPI Selection Criteria

Use these criteria when helping users choose their KPIs:

**1. Aligned** — The KPI traces directly to a corporate or product goal. If you can't explain the connection in one sentence, it doesn't belong.

**2. Measurable** — You can actually collect the data. A theoretically perfect KPI that requires data you don't have is useless.

**3. Actionable** — The team can influence the metric through their work. Metrics you can't affect are informational, not operational.

**4. Timely** — The data is available frequently enough to inform decisions. Annual-only metrics can't drive monthly tuning — this is why leading indicators matter.

**5. Understandable** — Stakeholders can interpret the metric without a statistics degree. If it requires extensive explanation, simplify or replace it.

**6. Limited** — Keep to 3–5 outcome KPIs and 3–5 diagnostic metrics. More than 10 total means nothing is truly "key." When you have too many, people focus on whatever looks good rather than what matters.

**7. Owned** — Each KPI has a named individual responsible for tracking, reporting, and acting on it.

---

## Common KPI Mistakes to Avoid

Pragmatic Institute identifies several recurring mistakes:

### Mistake 1: Having No KPIs at All
Without metrics, you have no evidence that product or go-to-market investment pays off. Unmeasured work is the first budget to get cut.

### Mistake 2: Too Many KPIs
When everything is "key," nothing is. Teams spread attention across irrelevant metrics and miss the signals that matter.

### Mistake 3: Borrowed or Generic KPIs
Adopting another company's KPIs without tailoring them to your business goals leads to measuring irrelevant things. Analyze your own data and business objectives.

### Mistake 4: Vanity Metrics as KPIs
Vanity metrics measure activity (likes, clicks, impressions) rather than results. They focus on quantity over quality. Management understands revenue, profit, and sales forecasts — not open rates and impressions. Translate soft metrics into hard business outcomes.

### Mistake 5: Pursuing Perfection
The goal is not perfect KPIs but reliable, significantly relevant metrics that generate actionable insights. Start measuring, learn from the data, and refine over time.

### Mistake 6: Failing to Connect KPIs to Financials
If you can't draw a line from your indicators to financial outcomes like CLV or revenue, you will struggle to prove the work's value to the C-suite. Business Outcomes is where that line is checked.

### Mistake 8: Only Lagging Indicators
A dashboard of revenue, churn and sales tells you what already happened. Without leading indicators, you find problems a quarter too late.

### Mistake 7: Ignoring Data Segmentation
Analyzing data as one aggregate lump hides the most important insights. Segment by channel, persona, market segment, and product line to find where performance diverges.

---

## Metrics vs KPIs: The Distinction That Matters

- **Metrics** are data points — everything you can measure (website visitors, email open rates, social followers, downloads)
- **KPIs** are the select few metrics chosen because they directly indicate progress toward critical business goals
- **All KPIs are metrics, but only the most strategically important metrics earn KPI status**

Example: Website traffic is a metric. Customer Acquisition Cost is a KPI — because it's directly tied to the business objective of profitable growth.

The Pragmatic approach: Focus on outcome metrics that demonstrate the contribution of product and go-to-market work to the business. Use activity and diagnostic metrics to explain and optimize, but report outcome KPIs to leadership.

---

## Attribution Models

Marketing attribution determines how credit for conversions is assigned across touchpoints. This is critical for measuring program effectiveness accurately.

### Single-Touch Models
- **First touch:** Credits the first interaction (good for measuring Awareness programs)
- **Last touch:** Credits the final interaction before conversion (good for measuring late-stage Engagement)
- **Limitation:** Both oversimplify the buyer's journey

### Multi-Touch Models
- **Linear:** Distributes credit equally across all touchpoints
- **Time decay:** Gives more credit to touchpoints closer to conversion
- **U-shaped (position-based):** Gives 40% to first touch, 40% to lead conversion touch, 20% distributed among middle touches
- **W-shaped:** Adds a third weighted touchpoint at opportunity creation
- **Data-driven / algorithmic:** Uses machine learning to assign credit based on actual contribution patterns

### Pragmatic Recommendation
For most go-to-market teams, a U-shaped or W-shaped model provides the best balance of accuracy and simplicity. The key is consistency — pick a model, apply it uniformly, and use it to compare programs against each other rather than seeking absolute precision.

---

## Reporting Cadences

### Weekly — Operational Review
- **Audience:** Product and marketing team, initiative owners
- **Focus:** Leading indicators and activity metrics
- **Metrics:** Leading indicators — pipeline generated this week, MQL/SQL volume, trial starts, activation, campaign performance
- **Action:** Tactical adjustments to active campaigns

### Monthly — Strategic Review
- **Audience:** Product and marketing leadership, cross-functional partners (sales, customer success)
- **Focus:** KPI trends and initiative performance
- **Metrics:** Revenue vs. target, pipeline coverage, CAC trend, funnel conversion rates, initiative-level ROI
- **Action:** Adjustments to programs, onboarding, pricing or priorities; budget reallocation; messaging changes

### Quarterly — Executive Review
- **Audience:** Executive team, C-suite
- **Focus:** Business impact and strategic alignment
- **Metrics:** Lagging results (shared with Business Outcomes) — revenue contribution, CLV and CAC trends, retention rates, market share movement — plus the leading indicators that explain what's coming
- **Action:** Strategic decisions, investment priorities, goal adjustments
- **Presentation approach:** Tell the story — what happened, why, and what you're doing about it. Use business language, not jargon.

---

## The Tune Process: From Data to Action

Measurement without "tune" is just reporting. Here is a structured approach:

### 1. Monitor Against Thresholds
Set performance bands for each KPI:
- **Green:** On track or exceeding target
- **Yellow:** Within acceptable variance (e.g., within 10% of target)
- **Red:** Below acceptable threshold for two or more consecutive periods

### 2. Investigate Root Causes
When a KPI enters yellow or red:
- Drill into diagnostic metrics to identify where the breakdown occurs
- Segment the data (by channel, persona, market segment, product) to isolate the issue
- Compare against external factors (market shifts, competitive moves, seasonality)

### 3. Develop and Test Hypotheses
- Formulate 2–3 hypotheses about what's causing the deviation
- Design quick experiments to validate or invalidate each hypothesis
- Prioritize based on potential impact and speed to test

### 4. Adjust the Work
- Make targeted changes to the specific initiative, program or tactic causing underperformance (campaigns, onboarding, pricing, roadmap priorities)
- Reallocate budget and resources from underperforming to high-performing work
- Update messaging, targeting, channels, or tactics as the data directs

### 5. Communicate Changes
- Inform stakeholders what changed, why, and what to expect
- Update forecasts if KPI changes affect revenue or pipeline projections
- Document learnings for future reference

### 6. Reassess
- Monitor adjusted work for the expected impact
- If improvement doesn't materialize within the expected timeframe, return to Step 2
- At quarterly review, assess whether KPIs themselves need updating based on evolving corporate goals, and whether leading indicators actually predicted the lagging results

---

## SaaS-Specific Measurement Considerations

For SaaS products, several additional metrics become essential:

- **Monthly Recurring Revenue (MRR) / Annual Recurring Revenue (ARR):** The foundation of SaaS business measurement
- **Net Revenue Retention (NRR):** Measures revenue retained from existing customers including expansion; best-in-class is 120%+
- **Gross Revenue Retention (GRR):** Measures revenue retained excluding expansion; shows pure churn impact
- **Expansion Revenue:** Revenue from upsell and cross-sell to existing customers
- **Time to Value:** How quickly new customers achieve their first meaningful outcome (a leading indicator; whether they reach the full outcome they bought for is Customer Value Realization)
- **Product Qualified Leads (PQLs):** Users who demonstrate buying intent through product usage behavior
- **Feature Adoption Rate:** Percentage of users engaging with specific features

---

## B2B vs B2C Measurement Differences

### B2B Emphasis
- Longer sales cycles make multi-touch attribution more important
- Account-level metrics (pipeline per account, account penetration) supplement individual lead metrics
- Organizational alignment metrics (lead acceptance rate, lead follow-up time) are critical
- Content influence on pipeline is a key differentiator
- Smaller deal volumes mean individual deal analysis is feasible

### B2C Emphasis
- Higher volume enables statistical significance faster
- Conversion rate optimization (CRO) is more directly measurable
- Channel-specific ROAS (Return on Ad Spend) is a primary KPI
- Customer segmentation and cohort analysis drive targeting decisions
- Speed metrics (time to purchase, cart abandonment rate) are highly actionable
