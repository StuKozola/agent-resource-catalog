# Product Profitability KPI Guide

A comprehensive reference of KPIs relevant to product profitability analysis, organized by product type. Use this guide when helping a user select the right metrics for their product.

## Table of Contents
1. Universal KPIs (All Product Types)
2. SaaS / Subscription Products
3. Physical / E-commerce Products
4. Marketplace / Platform Products
5. Internal Products & Services
6. KPI Selection Decision Tree

---

## 1. Universal KPIs (All Product Types)

These metrics apply regardless of product type.

### Revenue Metrics

**Total Product Revenue**
- Definition: All revenue directly attributable to the product
- Formula: Sum of all revenue streams for the product
- Frequency: Weekly (trending), Monthly (reporting)
- Why it matters: The starting point for all profitability analysis

**Revenue Growth Rate**
- Definition: Period-over-period change in revenue
- Formula: (Current Period Revenue - Prior Period Revenue) / Prior Period Revenue × 100
- Frequency: Monthly, Quarterly
- Why it matters: Growth context matters — a product with shrinking revenue and stable margins is still in trouble

**Revenue Concentration**
- Definition: Percentage of revenue from top N customers or segments
- Formula: Revenue from Top 10 Customers / Total Revenue × 100
- Frequency: Quarterly
- Why it matters: High concentration (e.g., one customer = 30% of revenue) is a profitability risk. Losing that customer collapses the P&L.

### Margin Metrics

**Gross Profit & Gross Margin %**
- Definition: Revenue minus direct costs of delivering the product
- Formula: (Net Revenue - COGS) / Net Revenue × 100
- Frequency: Monthly
- Why it matters: The most fundamental profitability metric. If gross margin is negative, the product destroys value with every sale.

**Contribution Margin %**
- Definition: Revenue minus all variable costs (COGS + variable selling/delivery costs)
- Formula: (Net Revenue - Total Variable Costs) / Net Revenue × 100
- Frequency: Monthly
- Why it matters: Shows how much each incremental sale contributes to covering fixed costs and generating profit. Critical for pricing and product mix decisions.

**Operating Margin %**
- Definition: Profit after allocating operating expenses (team costs, R&D, marketing share)
- Formula: Operating Profit / Net Revenue × 100
- Frequency: Quarterly
- Why it matters: Answers "is this product self-sustaining at its current scale, including the team that builds and supports it?"

**Net Profit Margin %**
- Definition: Bottom-line profitability after all costs, depreciation, and allocations
- Formula: Net Profit / Net Revenue × 100
- Frequency: Quarterly
- Why it matters: The definitive answer to "does this product make money?"

### Efficiency Metrics

**Revenue per Employee (Product-Allocated)**
- Definition: Product revenue divided by headcount allocated to the product
- Formula: Product Revenue / Product Team FTEs
- Frequency: Quarterly
- Why it matters: Indicates operational efficiency. Useful for comparing across products in a portfolio.

**Cost of Revenue as % of Revenue**
- Definition: How much of each revenue dollar goes to direct costs
- Formula: COGS / Net Revenue × 100
- Frequency: Monthly
- Why it matters: Trend indicator — rising cost-of-revenue percentage signals margin erosion before it hits the bottom line.

---

## 2. SaaS / Subscription Products

### Revenue Metrics

**Monthly Recurring Revenue (MRR)**
- Definition: Predictable monthly revenue from active subscriptions
- Formula: Sum of (Monthly subscription price × active subscribers) for each plan
- Components: New MRR, Expansion MRR, Churned MRR, Contraction MRR, Net New MRR
- Frequency: Monthly (often tracked weekly)

**Annual Recurring Revenue (ARR)**
- Definition: Annualized recurring revenue
- Formula: MRR × 12
- Frequency: Monthly, Quarterly

**Average Revenue Per User (ARPU) / Per Account (ARPA)**
- Definition: Revenue generated per user or account
- Formula: Total Revenue / Total Active Users (or Accounts)
- Frequency: Monthly
- Why it matters: ARPU trends reveal pricing power and upsell effectiveness

**Net Revenue Retention (NRR)**
- Definition: Revenue retained from existing customers, including expansion
- Formula: (Starting MRR + Expansion - Contraction - Churn) / Starting MRR × 100
- Target: >110% for high-growth SaaS, >100% minimum
- Frequency: Monthly
- Why it matters: NRR above 100% means existing customers generate more revenue over time even without new sales — the most powerful profitability driver in SaaS.

### Cost & Efficiency Metrics

**Customer Acquisition Cost (CAC)**
- Definition: Total cost to acquire one new customer
- Formula: Total Sales & Marketing Spend / New Customers Acquired
- Frequency: Monthly, Quarterly
- Why it matters: If CAC exceeds what a customer will ever pay you, the business model is broken

**CAC Payback Period**
- Definition: Months to recoup acquisition cost
- Formula: CAC / (Monthly ARPU × Gross Margin %)
- Target: <12 months for SMB SaaS, <18 months for enterprise
- Frequency: Quarterly

**Customer Lifetime Value (LTV)**
- Definition: Total gross profit expected from a customer over their lifetime
- Formula: ARPU × Gross Margin % × (1 / Monthly Churn Rate) — or — ARPU × Gross Margin % × Average Customer Lifespan
- Frequency: Quarterly

**LTV:CAC Ratio**
- Definition: Return on customer acquisition investment
- Formula: LTV / CAC
- Target: >3:1 (healthy), >5:1 (consider investing more in growth)
- Frequency: Quarterly
- Why it matters: The single most important SaaS profitability ratio. Below 3:1, the unit economics don't work.

**Gross Margin-Adjusted CAC Payback**
- Definition: Months to recover CAC from gross profit (not revenue)
- Formula: CAC / (ARPU × Gross Margin %)
- Why it matters: More accurate than revenue-based payback because you can only "pay back" CAC from profit, not from revenue that goes to COGS

### Churn Metrics (Profitability Destroyers)

**Gross Revenue Churn**
- Definition: Revenue lost from cancellations and downgrades
- Formula: (Churned MRR + Contraction MRR) / Starting MRR × 100
- Target: <2% monthly for SMB, <1% for enterprise
- Frequency: Monthly

**Logo Churn (Customer Churn)**
- Definition: Percentage of customers lost
- Formula: Customers Lost / Starting Customers × 100
- Frequency: Monthly

---

## 3. Physical / E-commerce Products

### Revenue Metrics

**Revenue per Unit / Average Selling Price (ASP)**
- Definition: Average price at which units are sold
- Formula: Total Revenue / Units Sold
- Frequency: Monthly
- Why it matters: ASP trends reveal discounting pressure, channel mix shifts, and pricing power

**Sales Volume by Channel**
- Definition: Units or revenue broken out by sales channel (DTC, wholesale, marketplace, retail)
- Frequency: Monthly
- Why it matters: Different channels have very different margin profiles. A shift from DTC to wholesale can dramatically change profitability.

**Return Rate**
- Definition: Percentage of sold units returned
- Formula: Units Returned / Units Sold × 100
- Frequency: Monthly
- Why it matters: Returns directly reduce net revenue and add cost. A 10% return rate can cut effective margin by 15-20%.

### Cost Metrics

**COGS per Unit**
- Definition: Direct cost to produce/acquire and deliver one unit
- Components: Raw materials, manufacturing, packaging, inbound freight
- Frequency: Monthly, tracked per SKU
- Why it matters: The building block of gross margin. COGS creep is the most common margin killer in physical products.

**Fulfillment Cost per Order**
- Definition: Cost to pick, pack, and ship one order
- Formula: Total Fulfillment Costs / Total Orders
- Frequency: Monthly

**Inventory Carrying Cost**
- Definition: Cost of holding unsold inventory (storage, insurance, depreciation, obsolescence)
- Formula: (Average Inventory Value × Carrying Cost Rate) / 12 for monthly
- Why it matters: Unsold inventory is a hidden profitability drain — especially for seasonal or perishable products

### Profitability Metrics

**Gross Margin by SKU/Product Line**
- Definition: Gross margin calculated at the individual product or product line level
- Why it matters: Portfolio averages can hide unprofitable products. Always drill down.

**Contribution Margin after Fulfillment**
- Definition: Revenue minus COGS minus fulfillment and shipping costs
- Formula: (Revenue - COGS - Fulfillment Costs) / Revenue × 100
- Why it matters: For e-commerce, fulfillment is often the difference between a profitable and unprofitable product

**Break-Even Volume**
- Definition: Units needed to cover all fixed costs
- Formula: Total Fixed Costs / Contribution Margin per Unit
- Frequency: Quarterly, or when costs/prices change

---

## 4. Marketplace / Platform Products

### Revenue Metrics

**Gross Merchandise Value (GMV)**
- Definition: Total value of transactions on the platform
- Frequency: Monthly
- Why it matters: GMV is the top-line activity measure, but it's NOT revenue. Revenue is the take rate applied to GMV.

**Take Rate**
- Definition: Percentage of GMV captured as revenue
- Formula: Platform Revenue / GMV × 100
- Frequency: Monthly
- Why it matters: Take rate × GMV = Revenue. Changes in take rate directly impact profitability.

### Cost & Efficiency Metrics

**Cost per Transaction**
- Definition: Total platform operating cost divided by transactions
- Formula: Total Operating Costs / Total Transactions
- Frequency: Monthly

**Seller/Supplier Acquisition Cost**
- Definition: Cost to onboard a new seller or supply-side participant
- Frequency: Quarterly

**Buyer Acquisition Cost**
- Definition: Cost to acquire a new buyer or demand-side participant
- Frequency: Quarterly

### Profitability

**Net Revenue Margin (on Take Rate Revenue)**
- Definition: Margin calculated on actual platform revenue, not GMV
- Formula: Net Profit / Platform Revenue × 100
- Why it matters: A marketplace with 10% take rate and 50% margin on that revenue has a very different profile than one with 25% take rate and 20% margin, even if both process the same GMV

---

## 5. Internal Products & Services

For products that don't generate direct revenue, profitability is measured through value creation and cost avoidance.

### Adoption Metrics (Proxy for Revenue)

**Active Users / Adoption Rate**
- Definition: Percentage of eligible users who actively use the product
- Formula: Monthly Active Users / Total Eligible Users × 100
- Frequency: Monthly

**Feature Utilization Rate**
- Definition: Which features are being used and how frequently
- Frequency: Monthly

**User Satisfaction (Internal NPS or CSAT)**
- Definition: How satisfied internal users are with the tool
- Frequency: Quarterly

### Value Metrics (Proxy for Profit)

**Time Saved per User**
- Definition: Hours saved per user per month compared to the previous process
- Frequency: Quarterly (via surveys or process measurement)
- How to monetize: Multiply by fully-loaded hourly labor cost for cost avoidance estimate

**Error/Defect Reduction Rate**
- Definition: Reduction in errors since the product was deployed
- Formula: (Pre-deployment Error Rate - Post-deployment Error Rate) / Pre-deployment Error Rate × 100

**Process Throughput Improvement**
- Definition: Increase in volume of work processed per unit time

### Cost Metrics

**Total Cost of Ownership (TCO)**
- Definition: All costs to build, run, and maintain the internal product
- Components: Development team salaries, infrastructure, licensing, support
- Frequency: Annually

**Cost per Active User**
- Definition: TCO divided by active users
- Formula: Annual TCO / Monthly Active Users
- Why it matters: If cost-per-user is rising while adoption is flat, the product is becoming less efficient

**ROI (for Internal Products)**
- Definition: Value delivered relative to investment
- Formula: (Annual Value Created - Annual TCO) / Annual TCO × 100
- Where "Value Created" = time saved × labor cost + error reduction savings + throughput improvement value

---

## 6. KPI Selection Decision Tree

Use this to quickly narrow down the right KPIs for a given product:

1. **Does the product generate direct revenue?**
   - YES → Go to step 2
   - NO (internal product) → Focus on Adoption + Value metrics from Section 5

2. **Is revenue subscription/recurring?**
   - YES → Prioritize: MRR/ARR, NRR, Gross Margin, LTV:CAC, CAC Payback, Churn
   - NO → Go to step 3

3. **Is it a physical product or marketplace?**
   - PHYSICAL → Prioritize: Gross Margin by SKU, COGS per Unit, Contribution Margin after Fulfillment, Break-Even Volume, Return Rate
   - MARKETPLACE → Prioritize: GMV, Take Rate, Net Revenue Margin, Cost per Transaction
   - DIGITAL ONE-TIME → Prioritize: Revenue per User, Gross Margin, CAC, LTV (if repeat purchases expected)

4. **What lifecycle stage?**
   - PRE-LAUNCH → Focus on projected unit economics (target margins, break-even estimates)
   - GROWTH → Focus on LTV:CAC, Gross Margin trend, Revenue Growth Rate
   - MATURE → Focus on Operating Margin, Net Margin, Revenue per Employee
   - DECLINING → Focus on Contribution Margin (is it still positive?), sunset analysis
