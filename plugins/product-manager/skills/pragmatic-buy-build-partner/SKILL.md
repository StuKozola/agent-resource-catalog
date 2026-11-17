---
name: pragmatic-buy-build-partner
description: >
  Guide product teams through the Buy, Build or Partner focus area of the Pragmatic Framework
  (Pragmatic Institute, 2027) — "Is building it ourselves the best path?" Use whenever a user needs to
  decide how to fill a gap in their product offering or solve a market problem — acquire a company,
  product or technology (buy), develop a capability internally (build), or collaborate with another
  company (partner). Also trigger for: buy vs build analysis, make or buy decision, build buy partner
  framework, partnership evaluation, acquisition vs internal development, capability gap analysis,
  product gap analysis, vendor vs build assessment, build vs license an AI model or component, or any
  variation of "should we build this ourselves or get it from somewhere else." Produces structured
  analysis documents, scoring matrices, and recommendation memos. Even if the user just casually asks
  "should we build X or buy it?" — use this skill.
---

# Buy, Build or Partner — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Business — *Is this a good investment, and is it paying off?*
- **Focus-area question:** *Is building it ourselves the best path?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Business Plan, Pricing, Business Outcomes, Measurement
- **Related Pragmatic Institute course:** Focus

## Context

Buy, Build or Partner (BBP) is a Business focus area. Organizations that want to expand can buy another business or product, build something new, or partner with another company. Product teams face the same three-way choice whenever they need to solve a market problem their current offering doesn't fully address.

The decision draws on several roles — engineering, finance, legal, executives — but **product leaders should guide it based on market needs**, not internal bias or engineering preference. The sequence is: identify the problem through market analysis, **define the ideal solution together with technical leaders**, and only then choose a path. Each path has a characteristic trade-off: buying is fast but can be costly; building creates a proprietary solution but takes time; partnering adds expertise or speed to market but depends on careful agreements.

## Start With "What Do We Already Have?"

Before comparing paths, take stock of existing assets — technology, IP, skills, data, products, services and relationships. Something you already own may close part of the gap, change the build estimate, or make a partner more attractive. Use the asset inventory maintained with Product Strategy (`pragmatic-product-strategy`, Market): `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-product-strategy/references/asset-registry-template.md` (formerly the Asset Assessment registry). Pull the relevant rows and their leverage scores into Phase 2.

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

Follow this structured process. Read `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buy-build-partner/references/process.md` for the detailed step-by-step walkthrough, and `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buy-build-partner/references/scoring.md` for the evaluation matrix template.

### Phase 1: Define the Problem and Gap
Product leaders lead this phase, using market analysis.
1. Articulate the market problem you're solving (reference your Market Problems and Win/Loss Analysis work)
2. Map the competitive landscape (what do competitors offer here, and what do buyers do today, including nothing?)
3. Identify the specific gap in your current offering
4. Validate that solving this gap is worth the investment (is the problem urgent, pervasive, and will the market pay?)

### Phase 2: Define the Ideal Solution
Define the ideal solution **with technical leaders** (product architect, lead engineer, CTO) before looking at specific vendors or build plans, so the options are judged against the market need rather than against each other.
1. Bring in what you already have (asset inventory) and what it covers
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
3. Define success metrics and exit triggers (what would cause you to revisit the decision?) — hand these to Business Outcomes and Measurement
4. Create an integration/execution plan

## Output Formats

When a user asks for help with a BBP decision, produce **one or more** of these deliverables based on what they need. If unclear, ask which format would be most useful.

### 1. BBP Analysis Document (default)
A structured memo for stakeholder review. Use the template in `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buy-build-partner/references/process.md`.

### 2. Scoring Matrix
A weighted evaluation spreadsheet. Use the template in `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buy-build-partner/references/scoring.md`. Create as an `.xlsx` file when the user wants something they can edit and share.

### 3. Executive Summary / Recommendation Slide
A concise 1-page recommendation suitable for a slide deck or exec review. Include: the gap, the three options evaluated, the scoring summary, the recommendation, and next steps.

### 4. Partnership Evaluation
If the user is specifically evaluating potential partners, use the partnership criteria in `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buy-build-partner/references/scoring.md` to assess partner candidates.

## Important Principles

- **Market-driven, not ego-driven.** Product leaders guide the decision based on market needs, not internal preferences. Teams with strong engineering cultures tend to over-index on "build." Teams with strong BD cultures tend to over-index on "partner." Be aware of these biases.
- **Revisit regularly.** A buy decision today may shift to build in 2 years as your capabilities mature. A partnership may become an acquisition target. Set review cadences.
- **Hybrid is OK.** Many organizations adopt a blended approach — build core differentiators internally while buying or partnering for non-core components.
- **Don't forget opportunity cost.** If you build, what else *won't* get built? Always account for the opportunity cost of engineering capacity.
- **Integration is always harder than you think.** Whether buying or partnering, budget 2x what you estimate for integration work.
- **Internal products too.** For internal platforms and tools the same choice applies — build in-house, buy a SaaS tool, or partner with another team or vendor. Judge it against the internal users' problem, not the platform team's preference.


## Related Focus Areas

BBP doesn't happen in isolation. It builds on and feeds into:
- **Market Problems** (Market) — What problem are we solving, and how do we know?
- **Product Strategy** (Market) — Does this fit what the product will be known for? Includes the asset inventory ("what do we already have?").
- **Distinctive Competencies** (Market) — What can we do that others can't easily copy? Build where this applies; buy or partner elsewhere.
- **Competitive Landscape** (Market) — What alternatives exist, including doing nothing?
- **Product Portfolio** and **Product Roadmap** (Focus) — How does this fit the portfolio and the sequence of outcomes?
- **Business Plan** (Business) — What's the business case? BBP cost and timing feed the financial model.
- **Pricing** (Business) — How does the chosen path affect cost, pricing and margins?
- **Business Outcomes** (Business) — Did the chosen path deliver the results expected?
- **Channel Support** (Enablement) — A partner path often means new partner enablement.

## Using AI in this focus area

AI can help scan the vendor and partner landscape, summarize product documentation and contract terms, draft build estimates and integration risk lists for engineering to challenge, and stress-test the scoring matrix with sensitivity analysis. AI coding tools may also shrink build estimates — re-check assumptions rather than relying on old ones. Rules:
- Check AI output against real market evidence and your technical leaders' judgment. AI can't tell you whether the market needs the capability (talk to buyers and non-buyers; NIHITO still applies), and vendor summaries can be out of date.
- Keep sensitive deal terms, acquisition targets, and company data out of tools not approved for it — M&A work is especially sensitive.
- The team, not the tool, owns the decision.

## Reference Files

- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buy-build-partner/references/process.md` — Detailed step-by-step walkthrough, BBP analysis document template, common pitfalls, and stakeholder RACI.
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buy-build-partner/references/scoring.md` — Weighted scoring matrix, 1–5 rubrics, quick-decision heuristics, partnership and acquisition evaluation templates.
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-product-strategy/references/asset-registry-template.md` — Asset inventory (input: "what do we already have?"), maintained with Product Strategy.
