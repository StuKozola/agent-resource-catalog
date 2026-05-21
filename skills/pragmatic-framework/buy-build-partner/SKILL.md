---
name: buy-build-partner
description: >
  Guide product teams through the Pragmatic Marketing Framework's "Buy, Build, or Partner" decision.
  Use this skill whenever a user needs to decide how to fill a gap in their product offering — whether
  to acquire a company or technology (buy), develop a capability internally (build), or collaborate with
  an external provider (partner). Also trigger when the user mentions: buy vs build analysis, make or buy
  decision, build buy partner framework, partnership evaluation, acquisition vs internal development,
  capability gap analysis, product gap analysis, strategic sourcing for product features, vendor vs build
  assessment, or any variation of "should we build this ourselves or get it from somewhere else." This
  skill produces structured analysis documents, scoring matrices, and recommendation memos. Even if the
  user just casually asks "should we build X or buy it?" — use this skill.
---

# Buy, Build, or Partner — Pragmatic Marketing Framework

## Context

In the Pragmatic Marketing Framework (now called the Pragmatic Framework), **Buy, Build, or Partner** is a strategic activity in the **Business** category. Its purpose is to determine the most effective way to deliver a complete solution to an identified market problem. When there are gaps in the current offering, product teams analyze whether to buy, build, or partner to close those gaps.

The core philosophy: the decision should be driven by **what the market needs**, not by internal bias or engineering preference. Product managers own this decision because they understand the market best, but it requires cross-functional collaboration with engineering, finance, legal, and executive leadership.

## The Three Paths

### Buy (Acquire)
Acquire another company, license technology, or purchase an off-the-shelf solution that already solves the problem.

**Choose Buy when:**
- A proven solution already exists in the market
- Speed to market is critical and you can't afford to build from scratch
- The capability is not core to your differentiation but is necessary for a complete solution
- The acquisition target has customers, revenue, or talent you also want
- You want full eventual control over the capability

**Risks:** Integration complexity, culture clash, high upfront cost, potential technical debt from acquired systems, post-merger distraction.

### Build (Develop Internally)
Use internal engineering and product teams to create the capability from the ground up.

**Choose Build when:**
- Nothing like it exists in the market
- The capability is core to your competitive advantage and distinctive competence
- You need deep, tight integration with your existing product architecture
- Building will add to your company's DNA and strengthen your IP portfolio
- You have the engineering talent, budget, and runway to deliver in time
- You need full control over the roadmap and development trajectory

**Risks:** Longer time to market, opportunity cost (what else won't get built), underestimating complexity, maintenance burden, talent scarcity.

### Partner (Collaborate)
Form a strategic alliance, integration, white-label agreement, or co-development arrangement with another company.

**Choose Partner when:**
- Both companies would benefit from the relationship (mutual value)
- Customers would benefit from the combined offering
- You need speed to market but don't need full ownership
- The capability requires specialized expertise you lack
- You want to test market demand before committing to build or buy
- The ecosystem or platform model makes partnerships natural

**Risks:** Dependency on partner's roadmap and reliability, less control over the end experience, partnership governance overhead, potential competitive conflicts, risk the partner gets acquired by a competitor.

## How to Run a BBP Analysis

Follow this structured process. Read `references/process.md` for the detailed step-by-step walkthrough, and `references/scoring.md` for the evaluation matrix template.

### Phase 1: Define the Problem and Gap
1. Articulate the market problem you're solving (reference your Market Problems and Win/Loss Analysis work)
2. Map the competitive landscape (what do competitors offer here?)
3. Identify the specific gap in your current offering
4. Validate that solving this gap is worth the investment (is the problem urgent, pervasive, and will the market pay?)

### Phase 2: Define the Ideal Solution
1. Collaborate with your product architect / lead engineer / CTO
2. Define what "done" looks like — functional requirements, integration needs, performance criteria
3. Assess alignment with your distinctive competencies
4. Estimate the scope and complexity of the solution

### Phase 3: Evaluate the Three Options
Score each option (Buy, Build, Partner) across these seven criteria:

| Criterion | Description | Weight |
|-----------|-------------|--------|
| Time-to-Value | How quickly can we deliver to market? | 15% |
| Total Cost of Ownership | 3-year cost including integration, maintenance, licensing | 20% |
| Strategic Differentiation | Does this strengthen our competitive moat? | 20% |
| Integration Risk | How complex is the technical integration? | 15% |
| Control & IP | How much control do we retain over roadmap and IP? | 10% |
| Scalability | Will this scale with our growth trajectory? | 10% |
| Risk & Dependencies | What external risks or dependencies does this create? | 10% |

Score each option 1–5 per criterion, multiply by weight, and compare totals. Require at least a 10% margin between the top two options; if closer, run a deeper risk assessment.

### Phase 4: Decide and Align
1. Document the recommendation with rationale
2. Present to cross-functional stakeholders (Product, Engineering, Finance, Legal, Exec)
3. Define success metrics and exit triggers (what would cause you to revisit the decision?)
4. Create an integration/execution plan

## Output Formats

When a user asks for help with a BBP decision, produce **one or more** of these deliverables based on what they need. If unclear, ask which format would be most useful.

### 1. BBP Analysis Document (default)
A structured memo for stakeholder review. Use the template in `references/process.md`.

### 2. Scoring Matrix
A weighted evaluation spreadsheet. Use the template in `references/scoring.md`. Create as an `.xlsx` file when the user wants something they can edit and share.

### 3. Executive Summary / Recommendation Slide
A concise 1-page recommendation suitable for a slide deck or exec review. Include: the gap, the three options evaluated, the scoring summary, the recommendation, and next steps.

### 4. Partnership Evaluation
If the user is specifically evaluating potential partners, use the partnership criteria in `references/scoring.md` to assess partner candidates.

## Important Principles

- **Market-driven, not ego-driven.** The decision should reflect market needs, not internal preferences. Teams with strong engineering cultures tend to over-index on "build." Teams with strong BD cultures tend to over-index on "partner." Be aware of these biases.
- **Revisit regularly.** A buy decision today may shift to build in 2 years as your capabilities mature. A partnership may become an acquisition target. Set review cadences.
- **Hybrid is OK.** Many organizations adopt a blended approach — build core differentiators internally while buying or partnering for non-core components.
- **Don't forget opportunity cost.** If you build, what else *won't* get built? Always account for the opportunity cost of engineering capacity.
- **Integration is always harder than you think.** Whether buying or partnering, budget 2x what you estimate for integration work.

## Related Pragmatic Framework Activities

BBP doesn't happen in isolation. It builds on and feeds into:
- **Market Problems** — What gap are we filling?
- **Competitive Landscape** — What alternatives exist?
- **Distinctive Competencies** — What are we uniquely good at?
- **Asset Assessment** — What do we already have to leverage?
- **Product Roadmap** — How does this fit the roadmap?
- **Business Plan** — What's the business case?
- **Pricing** — How does the approach affect pricing and margins?
- **Innovation** — Is this an innovation play or a table-stakes play?
