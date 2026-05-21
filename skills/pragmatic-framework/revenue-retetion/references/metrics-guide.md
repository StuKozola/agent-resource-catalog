# Revenue Retention Metrics Guide

This reference provides detailed definitions, formulas, benchmarks, and interpretation guidance for the key metrics used in Revenue Retention planning.

## Table of Contents

1. Core Retention Metrics
2. Expansion Metrics
3. Customer Health Metrics
4. Retention Economics
5. Benchmarks by Business Model
6. Interpreting Metric Combinations

---

## 1. Core Retention Metrics

### Net Revenue Retention (NRR)

Also called Net Dollar Retention (NDR). The single most important metric for Revenue Retention — it captures the full picture of how revenue from existing customers changes over time.

**Definition:** The percentage of recurring revenue retained from existing customers over a specific period, including expansion (upsells, cross-sells) and contraction (downgrades, churn).

**Formula:**
```
NRR = (Starting MRR + Expansion MRR − Contraction MRR − Churned MRR) / Starting MRR × 100
```

**Interpretation:**
- NRR > 100% means the business is growing revenue from existing customers even without adding new ones
- NRR < 100% means revenue from existing customers is shrinking — the business must acquire new customers faster just to maintain current revenue
- NRR is the most comprehensive single metric because it captures both retention and expansion dynamics

**Caution:** NRR can mask a serious churn problem if expansion revenue from a few large accounts compensates. Always pair NRR with GRR.

### Gross Revenue Retention (GRR)

**Definition:** The percentage of recurring revenue retained from existing customers, excluding expansion revenue. GRR isolates pure retention — it only goes down, never above 100%.

**Formula:**
```
GRR = (Starting MRR − Contraction MRR − Churned MRR) / Starting MRR × 100
```

**Interpretation:**
- GRR can never exceed 100%
- GRR shows the "floor" — how much revenue you keep before any expansion efforts
- A large gap between NRR and GRR signals heavy reliance on expansion to compensate for churn

### Customer Retention Rate (Logo Retention)

**Definition:** The percentage of customers (by count, not revenue) retained over a period.

**Formula:**
```
Customer Retention Rate = ((Customers at End − New Customers Added) / Customers at Start) × 100
```

**Note:** Logo retention can be misleading if customer sizes vary dramatically. A company could retain 95% of customers but lose its largest account, dramatically impacting revenue.

### Churn Rate

**Definition:** The percentage of customers or revenue lost over a period.

**Revenue Churn:**
```
Revenue Churn Rate = (Churned MRR / Starting MRR) × 100
```

**Logo (Customer) Churn:**
```
Customer Churn Rate = (Lost Customers / Starting Customers) × 100
```

Distinguish between voluntary churn (customer actively cancels) and involuntary churn (payment failure, credit card expiration). Involuntary churn is often 20-40% of total churn and is addressable through dunning processes and payment retry logic.

---

## 2. Expansion Metrics

### Expansion MRR / Expansion Revenue

**Definition:** Additional recurring revenue generated from existing customers through upsells, cross-sells, add-ons, price increases, or increased usage.

**Sources of expansion revenue:**
- Upsells — Customer upgrades to a higher tier or plan
- Cross-sells — Customer purchases additional or complementary products
- Add-ons — Customer purchases supplementary features or services
- Seat/license expansion — Customer adds more users
- Usage-based growth — Customer's consumption naturally increases
- Price increases — Existing customers renew at higher rates

### Expansion Rate

```
Expansion Rate = (Expansion MRR / Starting MRR) × 100
```

### Upsell/Cross-sell Conversion Rate

```
Conversion Rate = (Customers who expanded / Customers offered expansion) × 100
```

Track this by offer type, segment, and channel to understand what expansion motions work best.

### Customer Success Qualified Leads (CSQLs)

Expansion opportunities identified by customer success teams based on usage patterns, expressed needs, or account growth signals. Track CSQL volume, conversion rate, and revenue generated to measure CS team contribution to expansion.

---

## 3. Customer Health Metrics

### Customer Lifetime Value (CLV / LTV)

**Definition:** The total revenue expected from a customer over the duration of the relationship.

**Simplified formula:**
```
CLV = Average Revenue Per Account (ARPA) × Gross Margin % × (1 / Churn Rate)
```

Or:
```
CLV = Average Order Value × Purchase Frequency × Average Customer Lifespan
```

CLV is critical for determining how much to invest in retaining different customer segments.

### Net Promoter Score (NPS)

A survey-based metric measuring customer loyalty and likelihood to recommend. While NPS alone does not predict retention, declining NPS within a segment is a leading indicator of increased churn risk.

### Customer Satisfaction (CSAT)

Typically measured at specific touchpoints (post-support interaction, post-onboarding, post-renewal). Track trends over time rather than absolute scores.

### Customer Effort Score (CES)

Measures how easy it is for customers to accomplish tasks, get support, or resolve issues. High effort correlates with churn risk. Typically measured on a 1-7 scale after specific interactions.

### Product Adoption / Engagement Metrics

Usage-based indicators that vary by product type:
- Daily/Monthly Active Users (DAU/MAU)
- Feature adoption rates
- Login frequency
- Time-to-value for new customers
- Depth of usage (features used, integrations enabled)

Low or declining engagement is the strongest leading indicator of future churn.

### Customer Health Score

A composite score combining multiple signals into a single risk/health indicator. Common inputs:
- Product usage and engagement trends
- Support ticket volume and sentiment
- NPS/CSAT responses
- Contract renewal timeline
- Stakeholder engagement (champion changes, executive sponsor turnover)
- Payment history

---

## 4. Retention Economics

### The Cost of Churn

Calculate the revenue impact of churn to justify retention investment:

```
Annual Revenue at Risk = Annual Recurring Revenue × Annual Churn Rate
```

For example, a company with $10M ARR and 15% annual churn loses $1.5M per year from existing customers before any expansion.

### Compounding Effect of Churn

Churn compounds over time. At 10% annual churn:
- After 1 year: 90% of original revenue remains
- After 3 years: 73% of original revenue remains
- After 5 years: 59% of original revenue remains

This compounding makes even small improvements in retention enormously valuable over multi-year horizons.

### Retention Investment ROI

```
Retention ROI = (Revenue Saved through Reduced Churn − Retention Program Cost) / Retention Program Cost × 100
```

### The 5% Retention Rule

Research from Bain & Company (featured in Harvard Business Review) found that increasing customer retention by just 5% can boost profits by 25-95%. This is because:
- Retained customers cost less to serve over time
- They make larger and more frequent purchases
- They refer new customers
- They are less price-sensitive

### Acquisition vs. Retention Cost

Acquiring a new customer typically costs 5-7x more than retaining an existing one. When building a Revenue Retention budget, frame investments against what equivalent acquisition would cost.

### CLV:CAC Ratio

```
CLV:CAC = Customer Lifetime Value / Customer Acquisition Cost
```

Target CLV:CAC > 3:1 as a general benchmark. Improvements in retention directly increase CLV and thus improve this ratio without additional acquisition spending.

---

## 5. Benchmarks by Business Model

### SaaS / Subscription

| Metric | Good | Great | Best-in-Class |
|--------|------|-------|---------------|
| NRR | >100% | >110% | >120% |
| GRR | >85% | >90% | >95% |
| Annual Revenue Churn | <10% | <7% | <5% |
| Logo Churn (Annual) | <15% | <10% | <7% |

Enterprise SaaS companies typically achieve higher NRR (110-130%) due to larger expansion opportunities, while SMB-focused companies often see lower NRR (90-105%) due to higher churn and fewer upsell paths.

### B2B Non-SaaS (Services, Manufacturing, Distribution)

Benchmarks vary more widely. Focus on:
- Customer retention rate: >85% is healthy for most B2B industries
- Revenue retention from existing accounts: >90% year-over-year
- Same-store revenue growth: positive growth indicates healthy expansion

### B2C / E-Commerce

- Repeat purchase rate: >30% within 12 months is healthy
- Customer retention rate varies dramatically by vertical
- Focus on CLV vs. Customer Acquisition Cost (CAC) ratio: target CLV:CAC > 3:1

---

## 6. Interpreting Metric Combinations

### High NRR + High GRR
The ideal state. Strong retention and healthy expansion. Customers stay and buy more.

### High NRR + Low GRR
A warning sign. Expansion revenue is masking significant churn. The business is overly dependent on upselling the customers who stay while losing many others. Investigate churn drivers urgently.

### Low NRR + High GRR
Customers stay but do not expand. Possible causes: limited upsell paths, pricing/packaging that does not encourage growth, poor expansion playbooks, or satisfaction plateau without deeper engagement.

### Low NRR + Low GRR
The business is in trouble. Customers are leaving and those who stay are not growing. Requires fundamental reassessment of product-market fit, customer experience, and value delivery before building retention programs on top.

### Rising Churn + Stable NPS
Check whether NPS is being measured at the right touchpoints and with the right audience. Or, the churn may be concentrated in segments not well represented in NPS surveys.

### Declining Engagement + Stable Revenue
A leading indicator of future trouble. Revenue lags engagement — customers may still be under contract but are not getting value and are likely to churn at renewal.

### High Logo Churn + High NRR
Common in companies with a long tail of small customers and a few large, expanding accounts. The small-customer churn may be acceptable if it doesn't threaten the overall business, but investigate whether the long-tail segment is worth serving or if pricing/packaging adjustments could reduce churn there.
