# Acquisition Metrics Guide

This reference provides detailed guidance on the metrics, formulas, benchmarks, and measurement practices for Revenue Growth planning. Use it when the user needs help defining, calculating, or interpreting new-customer acquisition KPIs.

---

## Table of Contents

1. Core Acquisition Metrics
2. Pipeline and Funnel Metrics
3. Channel Performance Metrics
4. Unit Economics
5. Benchmarks by Business Model
6. Building a Measurement System
7. Common Measurement Mistakes

---

## 1. Core Acquisition Metrics

### New-Customer Revenue

**Definition**: Total revenue generated from customers acquired during the measurement period. Includes only first-contract or first-purchase revenue — expansion revenue from these customers in subsequent periods belongs to Revenue Retention.

**Formula**:
```
New-Customer Revenue = Sum of first-contract revenue from all customers whose initial purchase occurred in the period
```

**Why it matters**: The primary outcome metric for Revenue Growth. Directly measures whether acquisition plans are delivering against targets.

**Tracking notes**: Requires clear attribution rules — define when a customer is "new" (first invoice date, contract signature date, or first payment date) and stick to it consistently.

### New-Logo Count

**Definition**: The number of net-new customer accounts acquired during the period.

**Formula**:
```
New Logos = Count of unique customer accounts with first purchase in the period
```

**Why it matters**: Revenue can be inflated by a few large deals. Logo count ensures the acquisition engine is generating breadth, not just depth.

**Tracking notes**: Define what constitutes a "logo" clearly — is it a parent company, a division, a location? Be consistent.

### Customer Acquisition Cost (CAC)

**Definition**: The total cost to acquire one new customer, including all sales and marketing expenses allocated to acquisition.

**Formula**:
```
CAC = Total Acquisition Spend (Sales + Marketing) ÷ Number of New Customers Acquired
```

**Components of acquisition spend**:
- Sales team compensation (base + commission for new-business roles)
- SDR/BDR team costs
- Marketing spend allocated to acquisition (paid media, content, events)
- Sales and marketing technology (CRM, marketing automation, prospecting tools)
- Partner/channel incentives for new-customer referrals
- Overhead allocated to acquisition activities

**Why it matters**: CAC determines whether acquisition is economically sustainable. Rising CAC without corresponding increases in customer value signals trouble.

**Tracking notes**:
- Calculate both blended CAC (all channels) and channel-specific CAC
- Use fully-loaded costs (include personnel, tools, overhead) for accuracy
- Account for time lag — marketing spend in Q1 may generate customers in Q2/Q3. Consider using a time-adjusted CAC calculation for longer sales cycles.

### CAC Payback Period

**Definition**: The number of months required to recover the cost of acquiring a customer through the gross margin they generate.

**Formula**:
```
CAC Payback = CAC ÷ (Monthly Revenue per Customer × Gross Margin %)
```

**Why it matters**: Tells you how long new-customer capital is tied up before returning value. Shorter payback = faster reinvestment in growth.

**Benchmarks**:
- Strong: < 12 months
- Acceptable: 12-18 months
- Concerning: > 18 months
- For SaaS: best-in-class is < 12 months; median is ~15-17 months

---

## 2. Pipeline and Funnel Metrics

### Pipeline Generated

**Definition**: The total dollar value of new sales opportunities created during the period.

**Formula**:
```
Pipeline Generated = Sum of opportunity values created in period
```

**Why it matters**: A leading indicator of future revenue. If pipeline generation slows, revenue will follow 1-2 quarters later.

### Pipeline Coverage Ratio

**Definition**: The ratio of total pipeline value to the revenue target.

**Formula**:
```
Pipeline Coverage = Total Qualified Pipeline ÷ Revenue Target
```

**Why it matters**: Determines whether there are enough opportunities in play to hit revenue targets given historical win rates.

**Benchmarks**:
- Minimum: 3× coverage
- Healthy: 3-5× coverage
- High-velocity/transactional: 2-3× may suffice
- Enterprise/long-cycle: 4-5× or higher recommended

### Conversion Rates by Funnel Stage

Track conversion between each stage:

| Transition | Formula | Typical B2B Range |
|-----------|---------|-------------------|
| Lead → MQL | MQLs ÷ Total Leads | 10-25% |
| MQL → SQL | SQLs ÷ MQLs | 15-30% |
| SQL → Opportunity | Opportunities ÷ SQLs | 30-50% |
| Opportunity → Closed-Won | Closed-Won ÷ Opportunities | 15-30% |
| Lead → Customer (overall) | New Customers ÷ Total Leads | 1-5% |

**Why it matters**: Identifies where prospects drop off. Low conversion at a specific stage points to a specific problem (messaging, qualification, sales process, pricing).

### Sales Cycle Length

**Definition**: Average number of days from first meaningful engagement to closed-won for new customers.

**Formula**:
```
Sales Cycle = Average(Close Date - First Touch Date) for new customers closed in period
```

**Why it matters**: Longer cycles mean delayed revenue realization and higher CAC. Shortening sales cycles is a powerful growth lever.

**Tracking notes**: Measure by segment and deal size — enterprise deals naturally take longer than SMB. Track trends over time rather than focusing on absolute numbers.

### Win Rate

**Definition**: Percentage of qualified opportunities that result in a closed-won deal.

**Formula**:
```
Win Rate = Closed-Won Deals ÷ Total Closed Deals (Won + Lost)
```

**Benchmarks**:
- B2B average: 15-30%
- Strong performers: 30%+
- Competitive situations: 20-25% is common

---

## 3. Channel Performance Metrics

### Cost Per Lead (CPL)

**Definition**: The cost to generate one lead through a specific channel.

**Formula**:
```
CPL = Channel Spend ÷ Leads Generated from Channel
```

**Why it matters**: Enables apples-to-apples comparison of lead generation efficiency across channels.

### Channel Conversion Rate

**Definition**: The percentage of leads from a specific channel that ultimately become customers.

**Formula**:
```
Channel Conversion = New Customers from Channel ÷ Leads from Channel
```

**Why it matters**: A high-CPL channel with strong conversion may deliver better economics than a low-CPL channel with poor conversion. Always evaluate CPL alongside conversion rate.

### Channel ROI

**Definition**: The return on investment for each acquisition channel.

**Formula**:
```
Channel ROI = (Revenue from Channel - Channel Cost) ÷ Channel Cost × 100
```

**Why it matters**: The ultimate measure of channel effectiveness. Drives budget reallocation decisions.

### Revenue Attribution by Channel

Track what percentage of new-customer revenue is sourced from each channel. Use consistent attribution methodology (first-touch, last-touch, multi-touch, or weighted).

**Attribution considerations**:
- First-touch attribution: credits the channel that first attracted the prospect
- Last-touch attribution: credits the channel that directly preceded the sale
- Multi-touch attribution: distributes credit across all touchpoints
- Choose a model and apply it consistently; perfection is less important than consistency

---

## 4. Unit Economics

### Customer Lifetime Value (CLV)

**Definition**: The total revenue (or gross profit) expected from a customer over their entire relationship with the company.

**Formula (simple)**:
```
CLV = Average Revenue Per Customer Per Year × Average Customer Lifespan (years)
```

**Formula (gross-margin adjusted)**:
```
CLV = Average Revenue Per Customer Per Year × Gross Margin % × Average Customer Lifespan
```

**Formula (with churn)**:
```
CLV = Average Revenue Per Customer Per Month × Gross Margin % ÷ Monthly Churn Rate
```

### CLV:CAC Ratio

**Definition**: The relationship between the lifetime value of a customer and the cost to acquire them.

**Formula**:
```
CLV:CAC = Customer Lifetime Value ÷ Customer Acquisition Cost
```

**Benchmarks**:
- Minimum viable: 3:1
- Strong: 4-5:1
- Very strong: >5:1
- Below 3:1: acquisition spending may be unsustainable
- Above 8:1: may indicate under-investment in growth (leaving money on the table)

### New-Customer Revenue as % of Total Revenue

**Definition**: What share of total company revenue comes from new customers.

**Formula**:
```
New-Customer Revenue % = New-Customer Revenue ÷ Total Revenue × 100
```

**Benchmarks**: Strong growers typically target >10% of annual revenue growth coming from new customers.

---

## 5. Benchmarks by Business Model

### SaaS / Subscription

| Metric | Good | Great |
|--------|------|-------|
| CAC Payback | < 18 months | < 12 months |
| CLV:CAC | 3:1 | 5:1+ |
| Net Revenue Retention | > 100% | > 120% |
| New-Logo Growth Rate | 15-25% YoY | 30%+ YoY |
| Sales Cycle (SMB) | 14-30 days | < 14 days |
| Sales Cycle (Mid-Market) | 30-90 days | < 60 days |
| Sales Cycle (Enterprise) | 90-180 days | < 90 days |

### B2B Services / Professional Services

| Metric | Good | Great |
|--------|------|-------|
| CAC Payback | < 12 months | < 6 months |
| CLV:CAC | 4:1 | 6:1+ |
| Win Rate | 20-30% | 35%+ |
| Referral as % of New Business | 20-30% | 40%+ |

### B2B Product / Manufacturing

| Metric | Good | Great |
|--------|------|-------|
| New-Customer Revenue Growth | 5-10% YoY | 15%+ YoY |
| CAC (varies widely) | Industry-competitive | Below industry avg |
| Channel Partner Contribution | 20-40% of new revenue | 50%+ |

### General B2B Acquisition Budget Benchmarks

| Company Stage | Acquisition Budget as % of Revenue |
|--------------|-----------------------------------|
| Early-stage / High-growth | 20-30% |
| Growth stage | 15-20% |
| Mature / Established | 8-15% |
| B2B Services | 10-12% |
| B2B Products | 8-10% |

---

## 6. Building a Measurement System

### Measurement Infrastructure

To accurately track Revenue Growth metrics, ensure:

1. **CRM discipline**: New customers are flagged as "new" in the CRM with accurate first-purchase dates
2. **Source tracking**: Every lead has a source/channel attribution
3. **Cost allocation**: Marketing and sales costs are allocated to acquisition vs. retention activities
4. **Pipeline stages**: Clearly defined and consistently applied funnel stages
5. **Reporting cadence**: Weekly leading indicators, monthly performance, quarterly strategic review

### Dashboard Design

A Revenue Growth dashboard should include:

**Top-level (executive view)**:
- New-customer revenue vs. target (trend line)
- New-logo count vs. target
- CAC (current and trailing)
- CLV:CAC ratio

**Operational view**:
- Pipeline generated this period
- Pipeline coverage ratio
- Funnel conversion rates
- Sales cycle length trends

**Channel view**:
- Performance by channel (CPL, conversion, revenue, ROI)
- Budget consumed vs. allocated by channel

### Review Rhythm

| Frequency | Focus | Audience | Action |
|-----------|-------|----------|--------|
| Weekly | Leading indicators (MQLs, SQLs, pipeline) | Marketing and sales ops | Tactical adjustments |
| Monthly | Revenue, logos, conversion rates, channel mix | Marketing and sales leadership | Program optimization |
| Quarterly | CAC, CLV:CAC, channel ROI, budget reallocation | VP/C-level | Strategic plan adjustments |
| Annually | Full-year performance, plan vs. actual, next-year planning | Executive team | Revenue Growth plan reset |

---

## 7. Common Measurement Mistakes

1. **Counting expansion as acquisition**: Revenue from upsell, cross-sell, or seat expansion for existing customers is not new-customer revenue. Keep them separate.

2. **Using vanity metrics as KPIs**: Website visits, social followers, and email opens are activity metrics, not outcome metrics. Always tie measurement back to revenue and customer count.

3. **Ignoring time lag**: In B2B, marketing spend today generates revenue months later. Use cohort analysis and lagged attribution rather than same-month comparisons.

4. **Blending CAC across channels**: A single blended CAC number hides channel-level economics. Always calculate per-channel CAC alongside the blended figure.

5. **Inconsistent definitions**: Define "new customer," "MQL," "SQL," and each pipeline stage once and enforce consistently. Changing definitions mid-period makes trend analysis meaningless.

6. **Over-attributing to last touch**: Last-touch attribution over-credits bottom-of-funnel activities and under-credits awareness and nurturing that made the conversion possible. Consider multi-touch models for better insight.

7. **Not separating marketing-sourced from sales-sourced**: Track whether new opportunities were generated by marketing efforts or direct sales prospecting. This determines optimal budget allocation between marketing and sales.

8. **Measuring activity instead of outcomes**: Number of emails sent, calls made, or campaigns run are inputs. Revenue and customers acquired are outcomes. Optimize for outcomes.
