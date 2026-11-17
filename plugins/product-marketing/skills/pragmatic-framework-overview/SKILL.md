---
name: pragmatic-framework-overview
description: >
  Orientation and routing for the 2027 Pragmatic Framework (Pragmatic Institute): 37 focus areas in
  7 categories — Market, Focus, Business, Planning, Go-to-Market, Enablement and Operations. Use this
  skill when the user asks about the Pragmatic Framework as a whole, asks which focus area or skill fits
  their problem, wants to map their team to the Framework, assess strengths and gaps, decide who leads
  each focus area, plan where to start, or asks what changed in the 2027 refresh (renamed focus areas,
  the new Operations category, where AI fits). Also trigger for "Pragmatic Marketing Framework",
  "Pragmatic boxes", the old Programs or Support categories, "framework assessment", "team worksheet",
  "where do I start with Pragmatic", or a request that spans several focus areas at once. For work inside
  a single focus area, route to that focus area's pragmatic-* skill.
---

# The Pragmatic Framework (2027) — Overview and Router

The Pragmatic Framework helps product teams understand market needs, decide where to invest, coordinate product work and evaluate results. The 2027 refresh kept **7 categories and 37 focus areas** and the same purpose: make products the market wants to buy. It modernized terminology and added a full **Operations** category for the work after launch.

Read `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-framework-overview/references/framework-2027.md` for the full table of focus areas, their questions, the skill for each, the explicit boundaries between neighbors, and the pre-2027 → 2027 rename table.

## How the Framework is arranged

- **Strategy → execution, left to right.** It isn't a one-way sequence. Teams go back to focus areas as they gather evidence, make decisions and learn from results.
- **Above the bar: the market** (problems, segments, buyers, business models). **Below the bar: the product and the teams around it** (roadmaps, requirements, enablement, operations).
- **The loop.** Customer Value Realization, Exceptions, Escalations and Win/Loss findings become the next round of Market Problems.
- **Market evidence over opinion.** Test opinions and assumptions against what buyers, users and non-buyers actually say and do.

| Category | Question it answers | Focus areas |
|---|---|---|
| **Market** | What problems does the market have, and where can we win? | Market Problems, Product Strategy, Distinctive Competencies, Win/Loss Analysis, Competitive Landscape |
| **Focus** | Where should we play, and where should we invest? | Market Definition, Distribution Strategy, Product Portfolio, Product Roadmap |
| **Business** | Is this a good investment, and is it paying off? | Business Plan, Pricing, Buy, Build or Partner, Business Outcomes, Measurement |
| **Planning** | What are we building, for whom, and why? | Positioning, Buyer Journey, Buyer Personas, User Personas, Requirements, Ideation, Stakeholder Management |
| **Go-to-Market** | How will the market find, choose and stay with the product? | Marketing Plan, Growth, Retention, Launch, Organizational Alignment, Awareness, Engagement, Customer Satisfaction |
| **Enablement** | Can the people around the product make it succeed? | Adoption, Content, Assets, Channel Support |
| **Operations** | Is the product delivering value as it grows? | Scaling, Exceptions, Escalations, Customer Value Realization |

## Workflow

### 1. Identify what the user actually needs

Ask what decision or deliverable they're working toward, what product and market it concerns, and what already exists (personas, positioning, research). Then pick one of three paths:

- **A single focus area** → route to its skill (step 2).
- **Several connected focus areas** (e.g. "prepare for launch", "we're losing deals") → build a short sequence (step 3).
- **The team or the whole Framework** (e.g. "where are our gaps?", "who owns what?") → run the team assessment (step 4).

### 2. Route to a focus-area skill

| If the user is talking about… | Use |
|---|---|
| Customer pains, discovery interviews, "what problem are we solving?" | `pragmatic-market-problems` |
| Long-term direction, what the product stands for, what we say no to | `pragmatic-product-strategy` |
| What makes us unique, PRIME, hard-to-copy strengths | `pragmatic-distinctive-competencies` |
| Why deals were won or lost, evaluator interviews | `pragmatic-win-loss-analysis` |
| Competitors, substitutes, do-nothing, battlecards | `pragmatic-competitive-landscape` |
| Target segments, TAM/SAM/SOM, which segment to pursue | `pragmatic-market-definition` |
| Direct vs. partner, route to market, how customers buy and get the product | `pragmatic-distribution-strategy` |
| Multiple offers, lifecycle, investment horizons | `pragmatic-product-portfolio` |
| Roadmap, sequencing outcomes, prioritization | `pragmatic-product-roadmap` |
| Business case, funding a product or release | `pragmatic-business-plan` |
| Price models, packaging, willingness to pay | `pragmatic-pricing` |
| Acquire, build or partner for a capability | `pragmatic-buy-build-partner` |
| Revenue, profit, margin, ROI of the product | `pragmatic-business-outcomes` |
| KPIs, leading and lagging indicators, dashboards | `pragmatic-measurement` |
| Positioning statements, messaging, differentiation | `pragmatic-positioning` |
| How buyers move from need to decision | `pragmatic-buyer-journey` |
| Who makes or influences the purchase | `pragmatic-buyer-personas` |
| Who uses the product and their workflows | `pragmatic-user-personas` |
| PRDs, MRDs, user stories, use scenarios | `pragmatic-requirements` |
| Concepts, prototypes, experiments, solution exploration | `pragmatic-ideation` |
| Keeping leaders, teams and partners aligned on priorities and trade-offs | `pragmatic-stakeholder-management` |
| Annual marketing plan | `pragmatic-marketing-plan` |
| New revenue, new users, acquisition | `pragmatic-growth` |
| Churn, renewal, expansion, NRR | `pragmatic-retention` |
| Launch planning and readiness | `pragmatic-launch` |
| Sales, CS, support and ops working from the same picture | `pragmatic-organizational-alignment` |
| Brand and problem awareness, thought leadership, events | `pragmatic-awareness` |
| Moving prospects through evaluation and trial, nurture | `pragmatic-engagement` |
| CSAT, NPS, relationship health, references and advocates | `pragmatic-customer-satisfaction` |
| Onboarding, activation, continued use | `pragmatic-adoption` |
| Blog posts, guides, webinars, content plans | `pragmatic-content` |
| Decks, demos, case studies, ROI calculators, playbooks | `pragmatic-assets` |
| Partners, resellers, channel training and support | `pragmatic-channel-support` |
| Growing pains, manual work, capacity | `pragmatic-scaling` |
| Custom requests, one-offs, policy exceptions | `pragmatic-exceptions` |
| Critical customer issues, severity, post-incident learning | `pragmatic-escalations` |
| Whether customers achieved their intended outcomes | `pragmatic-customer-value-realization` |

If the user uses a pre-2027 name (Buyer Experience, Nurturing, Sales Tools, Revenue Retention and so on), use the rename table in `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-framework-overview/references/framework-2027.md` and tell them the current name once.

### 3. Sequence connected focus areas

When a request spans several areas, lay out a short path and say what each step produces for the next. Common paths:

- **New product or major bet:** Market Problems → Market Definition → Product Strategy → Business Plan → Buy, Build or Partner → Requirements.
- **Go-to-market for a release:** Positioning → Buyer Personas / Buyer Journey → Launch → Organizational Alignment → Assets / Content → Measurement.
- **Losing deals:** Win/Loss Analysis → Competitive Landscape → Positioning → Assets.
- **Churn or weak usage:** Adoption → Customer Value Realization → Retention → Market Problems.
- **Growing pains after launch:** Scaling → Exceptions → Escalations → Requirements / Product Roadmap.

Check what inputs exist before starting downstream work. Positioning without validated market problems, for example, is guesswork. Say so and offer to start upstream.

### 4. Map the team to the Framework

Use `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-framework-overview/templates/team-framework-worksheet.md`. It's a discussion tool, not a validated diagnostic.

1. **Who leads and who contributes.** Name a lead for each of the 37 focus areas. Flag areas with no owner or several owners.
2. **Rate each area today:** Strong, Partial or Gap. A gap can affect related areas anywhere in the Framework, not only the work to its right.
3. **Choose where to start.** Pick the gaps that matter most to the market and the strategy. Closing one may call for changes to responsibilities, processes, resources or skills. The Core Course table in the reference shows which Pragmatic Institute courses emphasize which focus areas.

Output a summary that includes the heat map by category, unowned and over-owned areas, the top 3 gaps with why they matter, and the first concrete action for each.

## Using AI with the Framework

The 2027 Framework has no AI box. AI is part of how teams practice product work in every focus area: organizing research, exploring alternatives, drafting requirements, analyzing results. Three rules apply everywhere:

- **Verify against market evidence.** AI output is a hypothesis until real buyers, users or data back it up.
- **Protect sensitive information.** Keep customer, deal and company data out of tools that aren't approved for it.
- **Stay accountable.** The team, not the tool, owns the decision.

## Common pitfalls

- Treating the Framework as a waterfall checklist instead of a set of focus areas teams revisit.
- Mapping job titles to categories ("PM does the left, PMM does the right"). Ownership is decided per focus area.
- Jumping to execution (launch, content, assets) without market problems, personas and positioning underneath.
- Stopping at launch. The Operations category and the loop back to Market Problems are where much of the learning happens.

## Reference files

- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-framework-overview/references/framework-2027.md`: all 37 focus areas with questions, bar position and skill; boundaries; rename table; Core Courses.
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-framework-overview/templates/team-framework-worksheet.md`: lead and Strong/Partial/Gap worksheet for team discussion.
