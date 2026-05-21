---
name: pragmatic-market-definition
description: "Guide teams through the Market Definition activity from the Pragmatic Marketing Framework. This skill helps product managers and marketers map market problems to target segments, size those segments (TAM/SAM/SOM), validate segment viability, and produce a Market Definition document. Use this skill whenever the user mentions market definition, market segmentation for product strategy, defining target markets, sizing market segments, TAM SAM SOM analysis, identifying which segments to pursue, Pragmatic Framework Focus category activities, or any request to determine whether a market segment is large enough to support a product's current and future business. Also trigger when users ask about segmenting their market for a new or existing product, evaluating market opportunities, or building a segmentation worksheet."
---

# Pragmatic Market Definition Skill

## Context: Where Market Definition Fits

Market Definition is an activity in the **Focus** category of the Pragmatic Framework (formerly Pragmatic Marketing Framework). It sits at the strategic layer between understanding market problems and building a business plan. The Pragmatic Institute defines it as:

> Map needs with target markets and analyze the market segments to actively pursue. Ensure that the targeted segments are large enough to support the current and future business of the product.

Market Definition bridges the upstream **Market** activities (Market Problems, Win/Loss Analysis, Distinctive Competence, Competitive Landscape, Asset Assessment) and the downstream **Business** and **Planning** activities (Business Plan, Positioning, Pricing, Buyer Personas). Without a rigorous Market Definition, every downstream activity is built on guesswork.

## Key Principles

1. **Outside-in thinking** — Pragmatic Rule #2: "The answer to most of your questions is not in the building." Segment based on observed customer problems and buying behavior, not internal assumptions.
2. **Problems over demographics** — Segments should be defined primarily by the problems customers need solved, not solely by firmographic or demographic attributes. Demographics refine; problems define.
3. **Segments must be actionable** — A valid segment must be identifiable (you can find them), reachable (you can market to them), substantial (large enough to be profitable), and differentiable (they respond differently than other segments).
4. **Revisit regularly** — Re-test your industry, market, and segment definitions at least quarterly, and more often for startups or fast-moving markets.
5. **Pragmatic Rule #10** — "Find market segments that value your distinctive competence." Segment selection should align with what your organization uniquely does well.

## Workflow Overview

When a user needs help with Market Definition, walk them through these phases. Adapt depth based on how much information they already have.

### Phase 1: Gather Inputs

Before segmenting, confirm the user has (or help them articulate) these upstream inputs:

- **Market Problems** — What urgent, pervasive problems has the team discovered through customer interviews? Which problems will the market pay to solve?
- **Distinctive Competence** — What unique abilities does the organization have to deliver value?
- **Competitive Landscape** — Who are the alternatives? Where are competitor strengths and weaknesses?
- **Asset Assessment** — What technical assets, skills, patents, or services can be leveraged?

If the user hasn't completed these upstream activities, flag which ones are missing and explain briefly why they matter. Offer to help with those first or proceed with what's available while noting the gaps.

### Phase 2: Identify and Define Segments

Guide the user through segmentation using a layered approach:

**Layer 1 — Industry / Vertical**
Start broad: which industries or verticals experience the problems your product solves? Examples: healthcare, financial services, manufacturing, education.

**Layer 2 — Market Segment**
Within each industry, identify segments by the *problem they share*. Combine problem-based criteria with descriptive attributes:
- Company size / revenue band
- Geography / region
- Regulatory environment
- Technology maturity
- Buying behavior and sales cycle length
- Current solution (or lack thereof)

**Layer 3 — Micro-Segment / Niche**
For early-stage products or focused GTM strategies, narrow further to a beachhead segment — the smallest viable group you can dominate first before expanding.

For each candidate segment, the user should be able to answer:
- What specific problem does this segment face?
- How urgent and pervasive is this problem within the segment?
- Will they pay to solve it?
- Can we identify and reach them?
- Does our distinctive competence align with their needs?

### Phase 3: Size the Segments (TAM / SAM / SOM)

For each candidate segment, estimate market size at three levels. Read `references/market-sizing-guide.md` for detailed methodology, formulas, and examples.

- **TAM (Total Addressable Market)** — Total revenue opportunity if you captured 100% of the market for this problem.
- **SAM (Serviceable Addressable Market)** — The portion of TAM you can realistically target given your product scope, geography, distribution, and business model.
- **SOM (Serviceable Obtainable Market)** — The portion of SAM you can realistically capture in the near term given competition, resources, and current capabilities.

Prefer bottom-up estimation (count target accounts × average deal size) over top-down (industry report % assumptions) when possible. Bottom-up is more credible and forces the user to think about their actual customers.

### Phase 4: Evaluate and Prioritize Segments

Score each candidate segment using these criteria. Read `references/segment-evaluation-criteria.md` for a detailed scoring framework.

| Criterion | Key Question |
|-----------|-------------|
| Problem urgency | How painful is the problem for this segment? |
| Problem pervasiveness | What percentage of the segment experiences this problem? |
| Willingness to pay | Will they spend money to solve it? |
| Market size (SOM) | Is the segment large enough to sustain the business? |
| Competitive intensity | How crowded is this segment? Can we differentiate? |
| Distinctive competence fit | Does our unique strength match what this segment values? |
| Ease of acquisition | Can we identify, reach, and convert these buyers? |
| Strategic alignment | Does pursuing this segment support our long-term vision? |

Rank segments and recommend which to actively pursue versus monitor versus ignore. A strong Market Definition typically results in 2-4 primary segments for a focused GTM strategy.

### Phase 5: Document the Market Definition

Produce a Market Definition document. The format depends on the user's needs, but at minimum it should include:

1. **Executive Summary** — Which segments the team will pursue and why
2. **Segment Profiles** — For each target segment: description, key problems, size estimates (TAM/SAM/SOM), competitive dynamics, and fit with distinctive competence
3. **Prioritization Rationale** — How segments were scored and ranked
4. **Gaps and Risks** — What assumptions still need validation, which upstream inputs are incomplete
5. **Review Cadence** — When the Market Definition will be revisited (quarterly recommended)

## Output Formats

Depending on what the user asks for, produce one of:

- **Full Market Definition Document** — Comprehensive write-up (use docx skill if they want a Word doc, or markdown for a lighter format)
- **Segmentation Worksheet** — A structured table comparing candidate segments across evaluation criteria
- **TAM/SAM/SOM Analysis** — Focused market sizing for one or more segments
- **Segment Profile** — Deep-dive on a single target segment
- **Executive Briefing** — 1-2 page summary for leadership or stakeholders

## Reference Files

Load these as needed based on what the user requires:

- `references/market-sizing-guide.md` — Detailed TAM/SAM/SOM methodology, calculation approaches, and worked examples
- `references/segment-evaluation-criteria.md` — Scoring rubric and prioritization framework for evaluating candidate segments

## Common Pitfalls to Flag

- **Segmenting by product feature instead of customer problem** — Segments should be groups of buyers, not product configurations
- **Making segments too broad** — "All enterprises" is not a segment. Push for specificity.
- **Ignoring willingness to pay** — A large segment with an urgent problem that won't pay is not viable
- **Confusing current customers with target market** — Existing customers may not represent the best segments going forward
- **Skipping upstream work** — Market Definition without Market Problems data is just guessing
- **One-and-done analysis** — Markets shift; revisit quarterly

## Keywords
market definition, market segmentation, target market, TAM SAM SOM, market sizing, segment analysis, pragmatic marketing, pragmatic framework, focus category, addressable market, market opportunity, beachhead strategy, segment prioritization, product market fit, go-to-market segments
