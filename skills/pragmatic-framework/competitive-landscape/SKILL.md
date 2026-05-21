---
name: competitive-landscape
description: "Use this skill whenever the user wants to analyze, map, or document their competitive landscape for product management or product marketing. Triggers: 'competitive landscape', 'competitive analysis', 'competitor analysis', 'battlecard', 'competitive matrix', 'competitive positioning', 'win strategy', 'competitive intelligence', 'competitor profiling'. Also triggers when referencing the Pragmatic Framework's competitive activities, assessing competitors' strengths/weaknesses, creating sales battlecards, or asking 'who are we competing against', 'how do we stack up', or 'brief the sales team on competitors'. Produces competitor profiles, competitive matrices, battlecards, and strategic recommendations grounded in market problems. Do NOT use for general market research, pricing strategy, or win/loss analysis."
---

# Competitive Landscape Analysis

## What This Skill Does

This skill guides the creation of competitive landscape analyses aligned with the Pragmatic Institute Framework. In the Pragmatic Framework, Competitive Landscape is one of the five "Market" activities. Its official definition:

> **Identify competitive and alternative offerings in the market. Assess their strengths and weaknesses. Develop a strategy for winning against the competition.**

The activity has three distinct responsibilities:
1. **Identify** competitive and alternative offerings — including knowing what kind of problem you're really solving and what kind of product you're really offering (the "frame of reference")
2. **Assess** competitive strengths and weaknesses objectively
3. **Develop a strategy** for winning — knowing when to fight and when to run

This skill produces structured deliverables: competitor profiles, competitive matrices, battlecards, and strategic recommendations. It emphasizes the Pragmatic principle of being market-driven ("your opinion, although interesting, is irrelevant") — every claim about a competitor should be grounded in evidence from the market, not internal assumptions.

## How This Skill Connects to the Broader Framework

Competitive Landscape doesn't exist in isolation. It feeds into and draws from several adjacent Pragmatic Framework activities:

- **Market Problems** (upstream): You need to understand what problems the market cares about before you can assess how competitors solve them. Always anchor competitive analysis in market problems, not feature checklists.
- **Win/Loss Analysis** (peer): Win/loss data is one of the richest sources of competitive intelligence — it tells you how buyers actually perceive competitors during real evaluations. If the user has win/loss data, incorporate it.
- **Distinctive Competencies** (peer): Your organization's unique abilities define where you can realistically win. Competitive strategy should leverage these.
- **Positioning** (downstream): Competitive landscape directly informs how you position your product — you describe your product by its ability to solve market problems better than alternatives.
- **Sales Alignment & Battlecards** (downstream): Sales teams need competitive intelligence distilled into actionable tools they can use mid-conversation.

## Workflow

When the user asks for competitive landscape help, follow this sequence:

### Step 1: Understand the Context

Before producing anything, clarify:
- **What product/service** is being analyzed?
- **What market segment** are we focused on? (Competitive dynamics differ by segment)
- **What's the goal?** Options include: strategic planning, sales enablement, product roadmap input, investor/board communication, or entering a new market.
- **What competitors do they already know about?** Start with what they have — don't make them start from scratch.

If the user provides limited context, work with what they give you and note assumptions. Don't block progress with excessive questions.

### Step 2: Define the Frame of Reference

This is a step many teams skip, and it's the one that causes the most strategic errors. The "frame of reference" means understanding what category you're actually competing in. A project management tool might think it competes with other project management tools, but buyers might be comparing it against spreadsheets, email, or doing nothing at all.

Help the user think through:
- **Direct competitors**: Companies offering substantially the same product/service to the same buyers
- **Indirect competitors**: Companies solving the same problem with a different approach
- **Alternative solutions**: Non-product alternatives (manual processes, status quo, in-house builds)
- **Potential entrants**: Adjacent companies that could enter the space

Categorize competitors into tiers:
- **Primary** (Tier 1): Direct competitors you encounter frequently in deals — these deserve deep profiling
- **Secondary** (Tier 2): Competitors you see occasionally or who serve adjacent segments — moderate profiling
- **Tertiary** (Tier 3): Alternatives and potential entrants — monitor-level awareness

### Step 3: Build Competitor Profiles

For each primary competitor, build a structured profile. Read `references/competitor-profile-template.md` for the full template. At a minimum, each profile covers:

- Company overview (size, funding, trajectory)
- Target market and positioning
- Product strengths and weaknesses (anchored to market problems, not features)
- Go-to-market approach
- Pricing model (if known)
- Key differentiators
- Known vulnerabilities

The most important principle: **assess strengths and weaknesses relative to the market problems that buyers care about**, not relative to your feature set. A competitor might have a "weaker" product technically but a stronger answer to the buyer's actual problem.

### Step 4: Create the Competitive Matrix

The competitive matrix is the core analytical artifact. It maps competitors against the dimensions that matter to buyers. Read `references/matrix-guidance.md` for detailed formatting.

Key rules for a good matrix:
- Columns = competitors (including your product). Rows = evaluation dimensions.
- Dimensions should come from market problems and buyer priorities, not your internal feature list.
- Use a consistent scoring approach (1-5 scale, or qualitative ratings like Strong/Moderate/Weak with brief evidence).
- Include a "trend" indicator where possible — is a competitor getting stronger or weaker on this dimension?
- Don't rig it. If a competitor is genuinely better on a dimension, say so. Credibility matters more than painting a rosy picture.

### Step 5: Develop the Winning Strategy

This is where analysis becomes action. For each primary competitor, articulate:

- **Where we win**: Dimensions and scenarios where we have genuine advantages
- **Where we lose**: Dimensions where the competitor is stronger — and what we do about it (roadmap it, partner around it, reframe the conversation, or concede and compete elsewhere)
- **Key battleground**: The 1-2 dimensions where the deal is most likely to be decided
- **Recommended talk track**: How sales should position against this competitor
- **Landmines to set**: Questions or criteria that, if introduced early in a buyer's evaluation, tilt the field in your favor
- **Traps to avoid**: Topics or comparisons that play to the competitor's strengths

The strategy should reflect Pragmatic's principle of knowing "when to fight and when to run." Not every deal is worth pursuing — if a competitor owns a particular segment or use case, it may be better to focus elsewhere.

### Step 6: Produce Deliverables

Based on the user's goal (from Step 1), produce the appropriate output:

| Goal | Deliverable | Format |
|------|------------|--------|
| Strategic planning | Full competitive landscape report | Document (docx/md) with profiles, matrix, and strategy |
| Sales enablement | Battlecards | One-page per competitor — read `references/battlecard-template.md` |
| Product roadmap input | Competitive gap analysis | Matrix highlighting gaps with prioritized recommendations |
| Board/investor communication | Competitive positioning summary | 2-3 page executive overview with market map |
| New market entry | Landscape overview | Broad scan with tier categorization and entry strategy |

For document creation, use the docx skill if the user wants a Word document or the pptx skill for presentations. For quick in-conversation outputs, use well-structured markdown.

## Output Quality Checklist

Before delivering any competitive analysis, verify:

- [ ] Every competitive claim is evidence-based or clearly marked as an assumption
- [ ] Strengths and weaknesses are assessed relative to market problems, not just features
- [ ] The analysis includes the user's own product honestly — not just competitors
- [ ] Alternative/indirect competitors are considered, not just direct rivals
- [ ] The "so what" is clear — analysis leads to actionable strategy
- [ ] Scoring and ratings are consistent across competitors
- [ ] The deliverable matches what the user actually needs (don't over-produce)

## Common Pitfalls to Avoid

- **Feature-list syndrome**: Comparing feature-for-feature instead of evaluating how well each competitor solves the buyer's actual problem. Always anchor in market problems.
- **Confirmation bias**: Building the matrix so your product wins on every dimension. This destroys credibility with sales teams and executives. Be honest about where competitors are strong.
- **Snapshot thinking**: A competitive landscape is not a one-time artifact. Recommend a review cadence (quarterly is typical) and note which competitors are on strong growth trajectories.
- **Ignoring the status quo**: For many products, the biggest "competitor" is doing nothing or using a manual workaround. Include this in the analysis.
- **Over-indexing on product, under-indexing on GTM**: A competitor with an inferior product but superior sales execution, partnerships, or brand awareness can still win deals. Assess the whole picture.

## Using Web Search

When the user asks you to research specific competitors, use web search to gather current information. Good search strategies:

- Search for the competitor's name + "review" or "vs" to find comparison content
- Check G2, Capterra, and TrustRadius for user reviews and feature comparisons
- Look at the competitor's own website for positioning, pricing, and messaging
- Search for recent news (funding rounds, acquisitions, product launches) to assess trajectory
- Look for analyst reports or industry publications covering the competitive space

Always note the recency and source quality of information you find. A G2 review from 3 years ago may not reflect the current product.

## Reference Files

- `references/competitor-profile-template.md` — Detailed template for individual competitor profiles
- `references/matrix-guidance.md` — How to structure and score a competitive matrix
- `references/battlecard-template.md` — Template for sales-ready competitive battlecards
