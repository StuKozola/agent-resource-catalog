# Market Sizing Guide: TAM / SAM / SOM

This reference provides detailed methodology for sizing market segments as part of the Pragmatic Market Definition activity.

## Overview of the Three Tiers

**TAM (Total Addressable Market)** is the total revenue opportunity available if you captured 100% of the market demand for your product or service, with no constraints. It represents the theoretical ceiling — the size of the entire pie.

**SAM (Serviceable Addressable Market)** is the portion of TAM that your business can realistically target and serve, given your product scope, geography, distribution model, pricing, and business model. It's the slice of the pie you could reasonably go after.

**SOM (Serviceable Obtainable Market)** is the portion of SAM you can realistically capture in the near-to-medium term, given competition, your current resources, brand awareness, and sales capacity. It's what you can actually win.

These are hierarchical: TAM > SAM > SOM. Each level adds more realism.

## Two Calculation Approaches

### Top-Down Approach

Start with broad industry data and narrow down.

**How it works:**
1. Find total industry/market revenue from analyst reports (Gartner, IDC, Forrester, IBISWorld, Statista, etc.)
2. Apply filters to narrow to your relevant segment (geography, customer type, product category)
3. Estimate your capturable share

**Strengths:** Quick to execute, good for early-stage planning, provides big-picture context
**Weaknesses:** Relies on assumptions, can be imprecise, may not reflect your specific opportunity

**When to use:** Initial business planning, investor pitches requiring market context, industries with robust published research.

**Example:**
- Industry report says global project management software market = $10B
- You only serve mid-market companies (200-2000 employees) in North America = 15% of market → TAM = $1.5B
- Your product is cloud-only, which excludes some buyers → SAM = $900M
- Given competition and your current reach → SOM = $45M (5% of SAM)

### Bottom-Up Approach

Start with your specific customer data and build up.

**How it works:**
1. Count the number of potential customers in your target segment
2. Estimate average annual revenue per customer (contract value, deal size)
3. Multiply to get market size

**Strengths:** More credible, forces you to identify actual customers, better for realistic planning
**Weaknesses:** More labor-intensive, requires customer data or reasonable proxies

**When to use:** Whenever possible. Investors and executives generally prefer bottom-up analysis because it demonstrates understanding of the customer.

**Example:**
- There are 12,000 mid-market companies in North America in your target verticals
- Average annual contract value for your category of product = $50,000
- TAM = 12,000 × $50,000 = $600M
- 60% match your ideal customer profile (cloud-ready, right tech stack) → SAM = $360M
- You can realistically win 8% in the next 3 years → SOM = $28.8M

## Step-by-Step Market Sizing Process

### Step 1: Define the Market Boundary

Clearly articulate what "the market" means for your analysis. Specify:
- The problem being solved (not just the product category)
- The buyer type (enterprise, SMB, consumer)
- Geographic scope
- Time horizon (usually annual)

Be specific. "The CRM market" is too broad. "Cloud CRM for mid-market B2B companies in North America" is actionable.

### Step 2: Estimate TAM

Choose top-down, bottom-up, or ideally both for cross-validation.

**Top-down formula:**
```
TAM = Industry Market Size × Relevant Segment Percentage
```

**Bottom-up formula:**
```
TAM = Total Potential Customers × Average Annual Revenue Per Customer
```

### Step 3: Narrow to SAM

Apply your business constraints:
- Geographic reach (where can you actually sell?)
- Product fit (which customers does your product actually serve?)
- Distribution model (direct sales, channel, self-serve — who can you reach?)
- Pricing tier (which customers can afford your product?)
- Technical requirements (what buyers have compatible infrastructure?)

**SAM formula:**
```
SAM = TAM × Percentage of Market You Can Serve
```

Or bottom-up:
```
SAM = Count of Customers Matching Your ICP × Average Deal Size
```

### Step 4: Estimate SOM

Factor in competitive dynamics and your own capacity:
- What market share can you realistically capture?
- How many deals can your sales team handle?
- What is your expected win rate?
- What is your current pipeline and growth trajectory?

**SOM formula:**
```
SOM = SAM × Expected Market Share Capture Rate
```

Or capacity-based:
```
SOM = Number of Sales Reps × Deals Per Rep Per Year × Average Deal Size × Win Rate
```

### Step 5: Validate and Sense-Check

Cross-check your estimates:
- Do TAM/SAM/SOM pass a basic reasonableness test?
- Are your assumptions documented and defensible?
- Does the SOM support your revenue targets and business plan?
- Have you compared against known competitor revenues as a sanity check?
- If a competitor has $X in revenue in this segment, your SOM should be in a plausible range relative to that.

## Presenting Market Size Data

When helping users present their sizing:

- Always state assumptions explicitly
- Show the methodology (top-down, bottom-up, or both)
- Use ranges rather than false precision (e.g., "$30M-$50M" rather than "$37.2M")
- Visualize as concentric circles or a funnel (TAM → SAM → SOM)
- Include the time horizon (usually "annual" or "over 3 years")
- Cite data sources

## Common Mistakes

- **Inflating TAM to impress** — An enormous TAM with a tiny SOM signals you don't understand your market
- **Confusing TAM with SAM** — Quoting the total industry size as if it's all addressable to you
- **No bottom-up validation** — Top-down-only estimates lack credibility
- **Static analysis** — Markets change; update sizing at least annually
- **Ignoring adjacent segments** — Document segments you're not pursuing now but could expand into
- **Using revenue when units would be more useful** — Sometimes counting potential customers is more insightful than dollar estimates, especially early on
