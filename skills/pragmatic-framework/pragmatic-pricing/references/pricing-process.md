# Pragmatic Pricing: End-to-End Process & Templates

This reference covers the complete workflow for executing the Pricing activity from the Pragmatic Framework. Work through these phases sequentially, though iteration between phases is expected and healthy.

---

## Table of Contents

1. [Phase 1: Discovery & Market Foundation](#phase-1-discovery--market-foundation)
2. [Phase 2: Willingness-to-Pay Research](#phase-2-willingness-to-pay-research)
3. [Phase 3: Pricing Model Design](#phase-3-pricing-model-design)
4. [Phase 4: Segmentation & Packaging](#phase-4-segmentation--packaging)
5. [Phase 5: Pricing Governance](#phase-5-pricing-governance)
6. [Phase 6: Implementation & Measurement](#phase-6-implementation--measurement)
7. [Templates & Deliverables](#templates--deliverables)
8. [Common Pitfalls](#common-pitfalls)

---

## Phase 1: Discovery & Market Foundation

Before any pricing decision, gather the inputs that make pricing market-driven rather than assumption-driven.

### Inputs to Collect

**From Win/Loss Analysis:**
- Why did recent evaluators buy or not buy?
- Was price cited as a factor in losses? How often?
- What alternatives did evaluators compare against?
- What was the typical deal size and discount level?

**From Competitive Analysis:**
- How do competitors price? (model, tiers, price points)
- Where are they positioned — premium, mid-market, budget?
- What does their packaging look like?
- Do they offer free tiers, trials, or freemium?

**From Market Problems & Personas:**
- What problems does the product solve?
- How do different buyer personas value those solutions differently?
- What is the economic impact of the problem on the customer? (This becomes the value ceiling)
- How urgently do customers need the solution?

**From Positioning:**
- Is the product positioned as premium, competitive, or value?
- What is the key differentiation?
- Does the brand support premium pricing?

### Value Quantification Exercise

For each key persona or segment, build a simple value model:

```
Cost of the problem to the customer (per year):     $________
Your product's effectiveness at solving it:           ________%
Economic value delivered:                             $________
Your target capture rate (typically 10-30% of value): ________%
Implied price point:                                  $________
```

This gives you a **value ceiling** — the maximum price a rational buyer would pay. Your actual price will be somewhere between your cost floor and this value ceiling, informed by competitive context and willingness-to-pay research.

---

## Phase 2: Willingness-to-Pay Research

### Choosing the Right Method

| Situation | Recommended Method |
|---|---|
| Brand-new product, no price context exists | Van Westendorp first, then Gabor-Granger |
| Existing product, testing a price change | Gabor-Granger |
| Designing multi-tier packaging with feature trade-offs | Conjoint Analysis |
| Quick directional read, limited budget | Van Westendorp only |
| Highly complex offering with many variables | Conjoint Analysis |

### Running a Van Westendorp Study

**Setup:**
1. Define the product or offering clearly — respondents must understand exactly what they're evaluating
2. Screen for qualified respondents (decision-makers or influencers in the buying process)
3. Show a clear product description, then ask the four PSM questions
4. Aim for at least 100 qualified respondents per segment

**Analysis:**
Plot four cumulative distribution curves on the same chart. The intersections define:
- **Point of Marginal Cheapness (PMC):** Where "too cheap" crosses "expensive but acceptable" — lower bound of optimal range
- **Point of Marginal Expensiveness (PME):** Where "too expensive" crosses "bargain" — upper bound of optimal range
- **Indifference Price Point (IDP):** Where "expensive" crosses "cheap" — the price at which equal numbers find it cheap vs. expensive
- **Optimal Price Point (OPP):** Where "too cheap" crosses "too expensive" — fewest objections

The range between PMC and PME is your **acceptable pricing corridor**.

### Running a Gabor-Granger Study

**Setup:**
1. Define 5-15 price points spanning your expected range (informed by Van Westendorp or competitive analysis)
2. Show respondents the product at a randomly selected starting price
3. Ask: "Would you buy this product at $X?" (yes/no or 5-point purchase intent scale)
4. If yes, show next higher price. If no, show next lower price.
5. Find each respondent's maximum acceptable price

**Analysis:**
- Plot a **demand curve**: % willing to buy at each price point
- Multiply demand × price to create a **revenue curve**
- The peak of the revenue curve is your **revenue-maximizing price**
- Look for sharp drops in demand — these are price sensitivity cliffs to avoid

### Running a Conjoint Study

**Setup:**
1. Define attributes to test (features, support levels, contract length, price)
2. Define levels for each attribute (e.g., price: $29, $49, $99, $149)
3. Create choice sets — pairs or groups of product configurations for respondents to evaluate
4. Respondents choose their preferred option from each set

**Analysis:**
- Part-worth utilities show relative importance of each attribute
- Price sensitivity can be measured per feature or bundle
- Simulator allows you to test "what-if" scenarios for different packaging configurations
- Outputs include willingness to pay for individual features and optimal tier composition

---

## Phase 3: Pricing Model Design

### Model Selection Framework

Answer these questions to narrow down the right pricing model:

1. **How does the customer realize value?**
   - Continuously over time → Subscription
   - Proportional to usage volume → Usage-based
   - At point of purchase → Perpetual/one-time
   - Through outcomes achieved → Revenue-share or outcome-based

2. **How complex is your product?**
   - Single product, uniform value → Flat-rate or per-user
   - Multiple features with varying value by segment → Tiered
   - Platform with many modules → Modular/add-on pricing

3. **What does your market expect?**
   - If all competitors use subscription, a perpetual model may confuse buyers (or differentiate you)
   - Market norms set expectations — deviate only with clear strategic rationale

4. **What is your growth strategy?**
   - Land-and-expand → Freemium or low entry tier with usage-based expansion
   - Enterprise-first → Annual subscription with volume discounts
   - Product-led growth → Free tier with self-serve upgrades

### Defining the Value Metric

The **value metric** is what you charge for — the unit of pricing. It should scale with how the customer receives value.

Good value metrics:
- Correlate with the value the customer receives
- Are easy for buyers to understand and predict
- Grow as the customer succeeds (aligning your success with theirs)
- Are difficult to game or circumvent

Examples: per active user, per transaction, per GB stored, per contact managed, per revenue generated.

Bad value metrics:
- Punish usage (discouraging adoption)
- Are opaque or unpredictable (creating bill shock)
- Don't correlate with customer value

---

## Phase 4: Segmentation & Packaging

### Building Pricing Tiers

If using tiered pricing, design tiers around **distinct buyer personas** with different needs:

**Tier Design Principles:**
- Each tier should serve a clearly identifiable segment with different needs and budgets
- Feature differences between tiers should be meaningful and easy to understand
- Tiers should create a natural upgrade path — customers should be able to start small and grow
- Aim for 3-4 tiers maximum for simplicity (Good/Better/Best or Starter/Professional/Enterprise)
- Include one tier as the obvious "best value" — this is your **anchor tier** that most customers should select

**Good/Better/Best Structure:**

| Element | Good (Starter) | Better (Professional) | Best (Enterprise) |
|---|---|---|---|
| **Target** | Individual / small team | Growing team / mid-market | Large org / enterprise |
| **Features** | Core functionality | Core + collaboration + integrations | Full platform + admin + security |
| **Support** | Self-serve / community | Email + chat | Dedicated CSM + SLA |
| **Pricing** | Low, self-serve | Mid, may involve sales | Custom, sales-led |

### Packaging Dos and Don'ts

**Do:**
- Package based on buyer needs, not engineering architecture
- Make the most popular tier obvious (use visual emphasis, "Most Popular" badges)
- Ensure each tier has at least one compelling feature the tier below lacks
- Test packaging with real buyers before launching
- Include an annual billing discount to improve retention and cash flow

**Don't:**
- Create tiers that differ only in limits (storage, users) — this feels arbitrary
- Hide the price of your highest tier entirely ("Contact Sales" with no indication)
- Create more than 4 tiers — decision paralysis hurts conversion
- Bundle unrelated features just to inflate tier value
- Make it hard to understand what you get at each level

### Fencing Strategies

To maintain segment-based pricing integrity, implement fences:
- **Feature gates** — Advanced features only in higher tiers
- **Volume thresholds** — Volume pricing kicks in at defined thresholds
- **Verification** — Education, nonprofit, startup program eligibility requirements
- **Contract commitment** — Lower per-unit price for longer commitments
- **Channel-specific** — Different pricing through direct vs. partner vs. marketplace

---

## Phase 5: Pricing Governance

Pricing governance answers the question: "Who can do what with pricing, and under what rules?"

### Decision Rights Matrix

| Decision Type | Authority | Approval Required | Documentation |
|---|---|---|---|
| Standard deal at list price | Sales rep | None | CRM entry |
| Discount up to 10% | Sales rep | Manager notification | Discount reason logged |
| Discount 10-25% | Sales manager | VP Sales approval | Business justification |
| Discount 25%+ | VP Sales / Pricing committee | Executive approval | Full business case |
| New pricing model or structure | Product / Pricing team | Executive team approval | Pricing strategy document |
| Price increase | Product / Pricing team | Executive approval | Market analysis + comms plan |
| Custom / non-standard deal | Deal desk | Cross-functional review | Custom agreement terms |

### Discount Policy Design

**Principles:**
- Every discount should have a documented business rationale
- Discounts erode margin and set expectations — use them strategically, not habitually
- Track discount frequency and depth as operational metrics
- Common valid reasons: multi-year commitment, volume purchase, competitive displacement, strategic account
- Common invalid reasons: "customer asked," "we need to hit quota," "it feels expensive"

**Discount guardrails to set:**
- Maximum discount without escalation (e.g., 10%)
- Floor price — the absolute minimum below which no deal closes
- Sunset provisions — promotional pricing must have an end date
- Reciprocity requirements — what does the customer give in exchange? (case study, reference, multi-year commit)

### Pricing Review Cadence

| Frequency | Activity |
|---|---|
| Monthly | Review pricing KPIs (ASP, discount depth, win rate at price) |
| Quarterly | Competitive pricing update, segment performance review |
| Semi-annually | Willingness-to-pay pulse check, packaging effectiveness review |
| Annually | Full pricing strategy review, price adjustment decision |

---

## Phase 6: Implementation & Measurement

### Price Change Communication

**Internal (2-4 weeks before external):**
- Brief sales team on new pricing, positioning rationale, and talk tracks
- Update all sales tools, proposals, and CPQ systems
- Provide FAQ for common objections
- Train support team on how to handle customer questions

**External:**
- Notify existing customers with adequate lead time (30-90 days depending on contract terms)
- Frame changes around value delivered, not cost increases
- Grandfather existing customers or offer transition pricing where appropriate
- Prepare retention offers for at-risk accounts

### Pricing KPIs

Track these metrics to evaluate pricing health:

- **Average Selling Price (ASP)** — Actual revenue per deal, compared to list price
- **Discount depth** — Average discount as % of list price
- **Discount frequency** — % of deals that receive any discount
- **Win rate by price tier** — Are certain tiers converting better than others?
- **Revenue per user/account** — Is pricing capturing value as customers grow?
- **Price realization** — Actual revenue ÷ theoretical revenue at list price
- **Gross margin** — Ensure pricing supports target profitability
- **Expansion revenue** — Revenue from upsells and tier upgrades
- **Churn by price point** — Are certain price points causing excess churn?

---

## Templates & Deliverables

### Pricing Strategy Document (Outline)

```
1. Executive Summary
   - Recommended pricing model and rationale
   - Key price points and expected impact

2. Market Context
   - Competitive pricing landscape
   - Customer willingness-to-pay findings
   - Value quantification by segment

3. Pricing Model
   - Selected model and value metric
   - Tier structure (if applicable)
   - Packaging details

4. Price Points
   - Recommended prices by tier/segment
   - Supporting research data
   - Sensitivity analysis

5. Segmentation Strategy
   - Segments and fencing mechanisms
   - Segment-specific pricing rules

6. Governance
   - Decision rights matrix
   - Discount policy
   - Escalation procedures

7. Implementation Plan
   - Timeline and milestones
   - System and process changes required
   - Internal and external communication plan

8. Measurement Plan
   - KPIs and targets
   - Review cadence
   - Success criteria
```

### Value Matrix Worksheet

For each key segment or persona, document:

```
Segment:              ___________________
Key Problem Solved:   ___________________
Economic Impact:      $________ / year
Competitive Alternative: ________________
Alternative's Price:  $________
Your Differentiated Value: _______________
Implied Value-Based Price: $________
Recommended Price:    $________
Rationale:            ___________________
```

### Price Implementation Table

| Element | Details |
|---|---|
| Product/SKU | |
| Pricing model | |
| Value metric | |
| List price(s) | |
| Volume discount schedule | |
| Promotional pricing | |
| Geographic adjustments | |
| Channel margins | |
| Floor price | |
| Target discount depth | |
| Effective date | |
| Review date | |

---

## Common Pitfalls

1. **Cost-plus as default** — Starting from your costs and adding margin ignores market reality. Your costs are irrelevant to the buyer; start from their value perception.

2. **Pricing by committee** — When everyone has input but no one owns the decision, pricing becomes a compromise that satisfies no one. Assign clear ownership.

3. **Set-and-forget** — Pricing is not a launch activity; it's an ongoing discipline. Markets change, competitors adjust, and your product evolves. Review regularly.

4. **Undisciplined discounting** — Without guardrails, sales teams will discount to close. Every unnecessary discount trains your market to expect lower prices. Set clear policies and track compliance.

5. **Copying competitors** — Competitive pricing provides context but shouldn't drive your strategy. Your product delivers different value; your price should reflect that.

6. **Ignoring packaging** — How features are bundled into tiers matters as much as the price itself. Bad packaging can make a good price feel wrong.

7. **No segmentation** — One-size-fits-all pricing leaves money on the table with high-value segments and prices out lower-value ones. Segment thoughtfully.

8. **Skipping research** — Gut-feel pricing may be fast, but willingness-to-pay research pays for itself many times over. Even a lightweight Van Westendorp study is better than guessing.

9. **Price changes without communication** — Surprising customers with price increases destroys trust. Always communicate early, clearly, and with value context.

10. **Treating pricing as a finance exercise** — Pricing is a market-facing decision that requires product, marketing, sales, and finance collaboration. Don't hand it entirely to any single function.
