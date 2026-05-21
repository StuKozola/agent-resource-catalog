---
name: pragmatic-pricing
description: Guide for executing the Pricing activity from the Pragmatic Marketing Framework. Use this skill whenever the user needs help with product pricing strategy, establishing pricing models, creating pricing schedules, setting pricing guidelines and procedures, willingness-to-pay analysis, price segmentation, value-based pricing, pricing governance, pricing recommendations, or any pricing-related work in the context of the Pragmatic Framework. Also trigger when users mention terms like "pricing model," "price strategy," "price segmentation," "pricing guidelines," "willingness to pay," "Van Westendorp," "Gabor-Granger," "total cost of ownership," "pricing recommendations," "discount policy," "pricing governance," or "packaging and bundling." If someone is working through the Pragmatic Framework and reaches the Pricing box, this is the skill to use.
---

# Pragmatic Framework: Pricing

## What This Activity Is

The Pricing box in the Pragmatic Framework is defined as:

> **Establish a pricing model, schedules, guidelines and procedures.**

Pricing lives in the **Business** row of the Pragmatic Framework — the layer that translates market understanding and strategic focus into concrete business decisions. It sits alongside Business Plan, Buy/Build/Partner, and Operational Metrics. Pricing is not a one-time launch decision; it is an ongoing discipline that requires market data, cross-functional alignment, and governance structures to execute well.

The Pragmatic approach to pricing is **market-driven and value-based**. Rather than starting from internal costs or copying competitors, it starts from the customer's perception of value and uses that as the anchor for all pricing decisions. The core philosophy: your price should reflect what the market is willing to pay for the problems you solve, not what it costs you to solve them.

## How to Use This Skill

When a user asks for help with pricing, follow this process:

1. **Assess where they are** — Are they starting from scratch, revising existing pricing, or building governance around an established model? Read `references/pricing-process.md` for the full step-by-step workflow.
2. **Identify what they need** — The Pricing activity has four pillars (model, schedules, guidelines, procedures). Determine which pillars the user needs help with.
3. **Apply the right tools** — Depending on the task, guide them through willingness-to-pay research, segmentation strategy, pricing model selection, or governance design. Details for each are in the references.

## The Four Pillars of Pragmatic Pricing

### 1. Pricing Model
How money changes hands between customer and company. This defines the fundamental structure of your pricing.

**Common models include:**
- **Subscription** — Recurring fee (monthly/annual) for ongoing access. Best for products with continuous value delivery.
- **Usage-based** — Price scales with consumption (API calls, transactions, storage). Best when value correlates directly with usage volume.
- **Tiered** — Multiple packages at different price points with escalating features or capacity. Best for serving multiple segments from a single product.
- **Per-user/per-seat** — Price multiplied by number of users. Simple to understand but can limit adoption.
- **Flat-rate** — Single price for full access. Simple but leaves money on the table across segments.
- **Perpetual license** — One-time purchase with optional maintenance fees. Traditional software model.
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
- **Exception handling** — How non-standard pricing requests are evaluated and approved
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
| **Dynamic** | Price adjusts in real-time based on demand | High-volume transactional businesses with real-time demand signals |

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

## Price Segmentation

Not all customers perceive the same value. Segmentation allows you to capture more value by tailoring pricing to different groups. Segment along three dimensions:

- **Product-based** — Different editions, modules, or feature sets at different price points
- **Customer-based** — Different pricing for enterprise vs. SMB, education vs. commercial, new vs. renewal
- **Transaction-based** — Volume discounts, contract length incentives, payment terms, bundling

Effective segmentation requires **fences** — mechanisms that prevent high-value segments from accessing low-value pricing. Examples: feature gates, volume thresholds, contract commitments, verification (e.g., .edu email for education pricing).

## Connecting Pricing to Other Framework Activities

Pricing does not exist in isolation. Key dependencies:

- **Market Problems & Win/Loss Analysis** → Tells you what value customers see and what they're comparing you against
- **Competitive Analysis** → Sets the competitive context for your pricing
- **Positioning** → Your price must be consistent with your positioning (premium positioning demands premium pricing)
- **Segmentation** → Defines which customer groups need different pricing
- **Business Plan** → Pricing feeds directly into revenue projections and financial models
- **Operational Metrics** → Pricing KPIs (ASP, discount depth, win rate by price) measure execution effectiveness
- **Channel Support** → Channel pricing, margins, and rules must align with your overall pricing strategy
- **Buyer Personas & Buyer's Journey** → Understanding who buys and how informs packaging, discounting rules, and sales enablement

## Reference Files

For detailed step-by-step workflows and templates, read:
- `references/pricing-process.md` — The complete end-to-end pricing process with templates and deliverable formats
