---
name: pragmatic-pricing
description: Guide for the Pricing focus area of the Pragmatic Framework (Pragmatic Institute, 2027) — "How will we capture the value we create?" Use whenever the user needs help with product pricing strategy, choosing a pricing model (one-time fee, subscription, usage-based, tiered, per-seat), pricing schedules, pricing guidelines and procedures, willingness-to-pay analysis, price testing, price segmentation, value-based pricing, pricing governance, or pricing recommendations. Also use for internal products and platforms — funding models, chargeback/showback, cost allocation and ROI. Trigger terms include "pricing model," "price strategy," "usage-based pricing," "consumption pricing," "value metric," "price segmentation," "pricing guidelines," "willingness to pay," "Van Westendorp," "Gabor-Granger," "price test," "total cost of ownership," "discount policy," "pricing governance," "packaging and bundling," "chargeback," or "cost allocation."
---

# Pricing — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Business — *Is this a good investment, and is it paying off?*
- **Focus-area question:** *How will we capture the value we create?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Business Plan, Buy, Build or Partner, Business Outcomes, Measurement
- **Related Pragmatic Institute course:** Price (covers Pricing and Business Outcomes)

## What This Focus Area Is

Pricing puts a monetary value on the product — as a one-time fee, a subscription, or a usage-based model. Price drives revenue, signals value, and sets customer expectations. A **pricing strategy** decides how prices are set, normally with input from product and executive teams; common approaches are value-based, cost-plus and dynamic pricing. In practice the work produces a pricing model, schedules, guidelines and procedures, and it is an ongoing discipline, not a one-time launch decision.

The Pragmatic approach to pricing is **market-driven and value-based**. Rather than starting from internal costs or copying competitors, it starts from the customer's perception of value. Your price should reflect what the market is willing to pay for the problems you solve, not what it costs you to solve them.

**Three pitfalls the Framework calls out:** delays (pricing left until just before launch, or price changes stalled for months), overly complex models (buyers and sellers can't explain or predict the bill), and skipping price testing (shipping a price nobody has validated). See Common Pitfalls below.

## How to Use This Skill

When a user asks for help with pricing, follow this process:

1. **Assess where they are** — Are they starting from scratch, revising existing pricing, or building governance around an established model? Read `references/pricing-process.md` for the full step-by-step workflow.
2. **Identify what they need** — Pricing work has four pillars (model, schedules, guidelines, procedures). Determine which pillars the user needs help with.
3. **Apply the right tools** — Depending on the task, guide them through willingness-to-pay research, price testing, segmentation strategy, pricing model selection, or governance design. Details for each are in the references.
4. **Check for an internal product** — If the "customers" are internal teams, use the internal-product variant below.
5. **Test before committing** — Recommend at least one lightweight price test before a price goes live.

## The Four Pillars of Pragmatic Pricing

### 1. Pricing Model
How money changes hands between customer and company. This defines the fundamental structure of your pricing.

**Common models include:**
- **Subscription** — Recurring fee (monthly/annual) for ongoing access. Best for products with continuous value delivery.
- **One-time fee** — Single payment for a product or perpetual license, sometimes with optional maintenance. Best when value is delivered at the point of purchase.
- **Usage-based** — Price scales with consumption (API calls, transactions, compute, storage, documents processed). Best when value correlates directly with usage volume. Watch for bill unpredictability: offer committed-use tiers, caps, or prepaid credits so buyers can budget. Common in AI and infrastructure products where your own cost also scales with use.
- **Tiered** — Multiple packages at different price points with escalating features or capacity. Best for serving multiple segments from a single product.
- **Per-user/per-seat** — Price multiplied by number of users. Simple to understand but can limit adoption.
- **Flat-rate** — Single price for full access. Simple but leaves money on the table across segments.
- **Hybrid** — Platform or seat fee plus usage-based overage. Gives predictability with upside as usage grows.
- **Freemium** — Free base tier with paid upgrades. An acquisition model, not strictly a pricing model.
- **Revenue-share** — Price tied to customer outcomes or revenue generated. High alignment but complex to administer.

The right model depends on how your customers realize value from your product, not on what's easiest to implement.

### 2. Pricing Schedules
When and how prices change over time.

- **Price lists and rate cards** — Published prices by SKU, tier, or segment
- **Promotional calendars** — Planned discounts, seasonal pricing, introductory offers
- **Price increase cadence** — How often and by how much prices adjust (annual increases, inflation adjustments)
- **Contract renewal pricing** — How pricing works at renewal vs. new business
- **Geographic/regional pricing** — Adjustments for different markets, currencies, or purchasing power

### 3. Pricing Guidelines
Rules that govern how pricing is applied in practice.

- **Discount authority** — Who can approve what level of discount and under what conditions
- **Floor prices** — Minimum acceptable prices below which no deal should close
- **Bundling rules** — When and how products can be combined for package pricing
- **Competitive response policies** — How to respond when a competitor undercuts your price
- **Segment-specific rules** — Different pricing approaches for enterprise vs. SMB, new vs. renewal, etc.
- **Channel pricing** — How pricing works through partners, resellers, distributors

### 4. Pricing Procedures
Operational processes that keep pricing running smoothly.

- **Price change approval workflow** — Steps and stakeholders required to change a price
- **Quote-to-cash process** — From pricing a deal to collecting revenue
- **Exception handling** — How non-standard pricing requests are evaluated and approved (repeat exceptions are evidence for Exceptions, Operations — `pragmatic-exceptions`)
- **Pricing review cadence** — Regular schedule for evaluating pricing effectiveness
- **Communication plan** — How price changes are communicated internally and externally
- **Measurement and tracking** — KPIs to monitor pricing health (win rates, discount depth, average selling price, revenue per user)

## Pricing Strategy Selection

Before choosing a model, establish your **pricing strategy** — the philosophy that guides your pricing decisions:

| Strategy | How It Works | Best When |
|---|---|---|
| **Value-based** | Price reflects perceived customer value | You understand your buyers deeply and can quantify value delivered |
| **Cost-plus** | Cost of delivery + target margin | Commodity products or when you lack market data (not recommended as a long-term approach) |
| **Competitive** | Priced relative to competitors | Entering a mature market with established price expectations |
| **Penetration** | Low initial price to capture share | New entrant needing rapid adoption; plan to raise prices later |
| **Skimming** | High initial price, reduced over time | Innovative product with early adopters willing to pay premium |
| **Dynamic** | Price adjusts in real time based on demand | High-volume transactional businesses with real-time demand signals |

The Pragmatic approach strongly favors **value-based pricing** because it is grounded in market understanding — the foundation of the entire framework.

## Willingness-to-Pay Research

Understanding what customers will pay is the empirical foundation of pricing. Three established methods:

### Van Westendorp Price Sensitivity Meter (PSM)
Use **early in the process** to establish acceptable price ranges. Asks four open-ended questions:
1. At what price would this be **so cheap** you'd question its quality?
2. At what price is this a **bargain** — great value for the money?
3. At what price does this start feeling **expensive** but you'd still consider it?
4. At what price is it **too expensive** to even consider?

Plot cumulative responses to find the acceptable price range. Best for new products where you don't yet know what price points to test.

### Gabor-Granger Method
Use **after you have candidate price points** to find the revenue-maximizing price. Shows respondents specific prices and asks purchase intent (yes/no). Uses adaptive logic — if they say yes at $50, show $60 next; if no, show $40. Produces a demand curve and revenue-maximization curve.

### Conjoint Analysis
Use **when features and pricing interact** — i.e., you need to understand trade-offs between price, features, and packaging. More complex to design and analyze, but produces the richest insights for tiered or bundled offerings.

**Practical guidance:** Start with Van Westendorp to define corridors, then use Gabor-Granger to pinpoint optimal levels within those corridors. Layer in conjoint if you're designing multi-tier packaging.

### Price Testing in Market
Surveys tell you stated intent; tests tell you behavior. Before rolling out broadly, test with a limited segment, region, or cohort of new deals (A/B price pages for self-serve, a pilot price in one sales region, or a time-boxed offer). Define the success measure up front (conversion, win rate, discount depth, ASP) and agree how long the test runs. Skipping this step is one of the most common and expensive pricing mistakes.

## Price Segmentation

Not all customers perceive the same value. Segmentation allows you to capture more value by tailoring pricing to different groups. Segment along three dimensions:

- **Product-based** — Different editions, modules, or feature sets at different price points
- **Customer-based** — Different pricing for enterprise vs. SMB, education vs. commercial, new vs. renewal
- **Transaction-based** — Volume discounts, contract length incentives, payment terms, bundling

Effective segmentation requires **fences** — mechanisms that prevent high-value segments from accessing low-value pricing. Examples: feature gates, volume thresholds, contract commitments, verification (e.g., .edu email for education pricing).

## Internal Products and Platforms

For internal products (platforms, shared services, internal tools) there may be no price tag, but the same thinking applies to **funding, cost allocation and return on investment**:

- **Funding model** — Central funding, project-based funding, or a consumption-based budget. Decide who pays for the platform's existence vs. its growth.
- **Cost allocation** — Showback (report each team's consumption without charging) or chargeback (bill teams internally). Allocate on a driver teams understand and can influence — seats, usage, transactions — the internal equivalent of a value metric.
- **ROI** — Express value in the business's terms: cost avoided, time saved, risk reduced, revenue enabled. This becomes the baseline Business Outcomes tracks.
- **Same pitfalls** — Opaque or overly complex allocation formulas cause the same distrust as confusing external pricing, and teams may route around the platform.

See `references/pricing-process.md` for an internal-product worksheet.

## Common Pitfalls (summary)

- **Delays** — Pricing decided at the last minute before launch, or needed price changes stalled for months. Start pricing work alongside the business plan.
- **Overly complex models** — Too many tiers, metrics, add-ons and exceptions. If sales can't quote it and buyers can't predict the bill, simplify.
- **Skipping price testing** — Launching an untested price. Run at least a lightweight willingness-to-pay study or in-market test.
- Also: cost-plus as default, set-and-forget, undisciplined discounting, copying competitors. Full list in `references/pricing-process.md`.

## Connecting Pricing to Other Focus Areas

Pricing does not exist in isolation. Key dependencies:

- **Market Problems & Win/Loss Analysis** (Market) → Tells you what value customers see and what they're comparing you against
- **Competitive Landscape** (Market) → Sets the competitive context, including substitutes and doing nothing
- **Market Definition** (Focus) → Defines which customer groups need different pricing
- **Distribution Strategy** (Focus) and **Channel Support** (Enablement) → Channel pricing, margins, and rules must align with your overall pricing strategy
- **Business Plan** (Business) → Pricing feeds directly into revenue projections and the financial model
- **Business Outcomes** (Business) → Revenue, margin and profit by product and customer show whether pricing captures the value expected
- **Measurement** (Business) → Leading pricing indicators (win rate by price point, discount depth, trial-to-paid conversion) flag problems before revenue does
- **Positioning** (Planning) → Your price must be consistent with your positioning (premium positioning demands premium pricing)
- **Buyer Personas & Buyer Journey** (Planning) → Who buys and how they decide informs packaging, discounting rules and approvals

## Using AI in this focus area

AI can help summarize willingness-to-pay survey results and open-ended responses, model revenue under alternative pricing models and usage scenarios, analyze discount and deal data for patterns, and draft pricing pages and change communications. Rules:
- Check AI output against real market evidence. AI can't tell you what buyers will pay; price tests and conversations with buyers and non-buyers can (NIHITO still applies). Don't let AI benchmark "typical" competitor prices without verifying them.
- Keep sensitive customer, deal, discount and margin data out of tools not approved for it.
- The team, not the tool, owns the pricing decision.

## Reference Files

For detailed step-by-step workflows and templates, read:
- `references/pricing-process.md` — The complete end-to-end pricing process (discovery, willingness to pay, price testing, model design, packaging, governance, measurement), the internal-product worksheet, templates, and the full pitfalls list
