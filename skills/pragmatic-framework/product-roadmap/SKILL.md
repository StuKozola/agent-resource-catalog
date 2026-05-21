---
name: product-roadmap
description: >
  Create, review, and refine product roadmaps using the Pragmatic Marketing Framework methodology.
  Use this skill whenever the user asks about product roadmaps, roadmap planning, roadmap strategy,
  roadmap prioritization, roadmap communication, release planning, product vision documents,
  feature prioritization for roadmaps, roadmap presentations, theme-based roadmaps, or any task
  involving illustrating a product's vision and key phases of deliverables over time. Also trigger
  when the user mentions "Pragmatic Framework roadmap," "product roadmap document," "roadmap review,"
  or asks how to build, structure, or present a product roadmap to stakeholders. This skill covers
  the Product Roadmap box from the Pragmatic Framework's Focus category.
---

# Product Roadmap — Pragmatic Marketing Framework

This skill helps create market-driven product roadmaps aligned with the Pragmatic Institute's
framework. The Product Roadmap activity sits in the **Focus** category of the Pragmatic Framework
and is defined as:

> **Illustrate the vision and key phases of deliverables for the product. The roadmap is a plan,
> not a commitment.**

That last phrase is the single most important principle in Pragmatic roadmapping. Internalize it
before doing anything else.

## Core Principles

**Market-driven, not inside-out.** Every item on the roadmap should trace back to a validated
market problem, not an internal stakeholder's pet feature. The Pragmatic Framework insists that
product decisions flow from market evidence — interviews, win/loss analysis, competitive landscape
— not from opinions. If a roadmap item cannot be linked to a real persona with a real problem,
it doesn't belong on the roadmap.

**Vision over features.** A Pragmatic roadmap illustrates *themes and strategic phases*, not a
feature laundry list. Themes communicate the problems being solved; features are implementation
details that belong in a backlog. This keeps the roadmap useful for executives, sales, marketing,
and development alike, rather than being a Gantt chart only engineers can parse.

**Plan, not commitment.** Roadmaps are predictions based on current knowledge. They will change as
the market changes. Presenting a roadmap as a binding promise creates organizational rigidity and
damages trust when (not if) priorities shift. Communicate confidence levels honestly: near-term
items are higher confidence, long-term items are directional.

**Audience-tailored.** Different stakeholders need different views of the same roadmap. Read
`references/audience-tailoring.md` for detailed guidance on creating views for executives,
engineering, sales, marketing, and external customers.

## When to Use This Skill

Trigger on any of these scenarios:

- Creating a new product roadmap from scratch
- Reviewing or critiquing an existing roadmap
- Converting a feature list into a theme-based roadmap
- Preparing roadmap presentations for different audiences
- Prioritizing roadmap items using Pragmatic principles
- Aligning a roadmap with business plans, positioning, or market problems
- Building a product marketing roadmap alongside the technical roadmap

## Step-by-Step: Building a Pragmatic Product Roadmap

### Phase 1: Gather Strategic Inputs

Before touching the roadmap itself, collect and synthesize these inputs. If the user hasn't
provided them, ask for them — each one matters:

1. **Product/portfolio vision** — Where is the product headed in 2-3 years? What market position
   are you targeting?
2. **Validated market problems** — From Market Problems, Win/Loss Analysis, and Competitive
   Landscape activities in the Pragmatic Framework. What urgent, pervasive problems has the market
   told you about?
3. **Distinctive competencies** — What can your organization uniquely deliver that competitors
   cannot?
4. **Business plan constraints** — Revenue targets, investment thresholds, pricing model changes,
   buy/build/partner decisions.
5. **Existing commitments** — Contractual obligations, regulatory deadlines, technical debt that
   blocks progress.
6. **Cross-functional plans** — Marketing's demand-gen calendar, sales enablement timelines,
   partner/channel launch schedules. Roadmaps don't live in isolation.

### Phase 2: Define Themes

Organize roadmap items into **themes** — high-level strategic objectives tied to market problems.
Good themes sound like problems being solved, not features being built.

**Good themes:**
- "Reduce time-to-value for new enterprise customers"
- "Expand compliance coverage for regulated industries"
- "Improve self-service capabilities to reduce support burden"

**Bad themes (these are features, not themes):**
- "Build SSO integration"
- "Add dashboard widgets"
- "Migrate to microservices"

Each theme should connect to: a target persona, a validated market problem, and a measurable
business outcome. If it doesn't connect to all three, it needs more work.

### Phase 3: Prioritize

Use market evidence to prioritize themes, not internal politics. The Pragmatic approach
recommends evaluating each theme on:

- **Urgency** — How painful is this problem right now for the market?
- **Pervasiveness** — How many target personas/segments experience this problem?
- **Willingness to pay** — Will solving this problem generate revenue or retention?
- **Strategic alignment** — Does this leverage distinctive competencies and match the product vision?
- **Feasibility** — Can you realistically deliver this given current resources and dependencies?

Score or rank themes across these dimensions. Document the reasoning — it will be challenged,
and you want evidence, not opinion. A simple prioritization matrix works well. For more detail,
see `references/prioritization-methods.md`.

### Phase 4: Structure the Roadmap

Choose a structure that matches your organizational maturity and audience needs:

**Theme-based with time horizons (recommended for most teams):**
Organize by Now / Next / Later columns with themes as rows. Near-term items (Now) are specific
and high-confidence. Mid-term items (Next) are directional. Long-term items (Later) are
exploratory. This avoids false precision with dates while still communicating sequence and priority.

**Quarterly roadmap:**
Organize themes into Q1, Q2, Q3, Q4 (or rolling 8 quarters for longer planning). Each quarter
shows the primary themes being addressed, with high-level deliverables underneath. Good for
organizations that operate on quarterly business cycles.

**Outcome-based roadmap:**
Structure around measurable outcomes (e.g., "Increase trial-to-paid conversion by 15%") with
initiatives grouped under each outcome. Best for product-led growth organizations already using
OKRs.

Regardless of structure, every roadmap should include:
- Product vision statement at the top
- Clear themes with problem-context (not just feature names)
- Confidence indicators (high/medium/low or committed/planned/exploratory)
- Connection to strategic goals or business plan
- Last-updated date (roadmaps go stale fast)

### Phase 5: Tailor and Communicate

A roadmap that nobody reads is worthless. Create audience-appropriate views:

- **Executive view:** Themes, strategic outcomes, investment level, risk. One page.
- **Engineering/Development view:** Themes broken into epics, dependencies, technical milestones.
  More granular but still problem-framed.
- **Sales view:** What's coming that they can talk about (carefully), what's NOT committed, and
  how themes map to customer pain points they hear in the field.
- **Marketing view:** Themes mapped to launch windows, positioning implications, content and
  campaign planning hooks.
- **External/Customer view:** High-level themes only. No dates, no feature specifics. Focus on
  problems being solved and strategic direction.

Read `references/audience-tailoring.md` for templates and examples of each view.

### Phase 6: Review and Iterate

Roadmaps are living documents. Schedule regular cadences:

- **Monthly:** Review with product and engineering leadership. Adjust priorities based on new
  market data, delivery progress, and resource changes.
- **Quarterly:** Review with executive stakeholders. Align roadmap with updated business plan and
  market conditions.
- **Ongoing:** Feed learnings from win/loss analysis, market interviews, and competitive
  intelligence back into theme prioritization.

When changes happen, communicate them proactively with context. Explain *why* priorities shifted
(new market data, competitive move, resource constraint) — not just *that* they shifted.

## Common Anti-Patterns to Avoid

- **Feature laundry lists** — If the roadmap reads like a backlog, it's not a roadmap. Elevate
  to themes.
- **Date-driven promises** — Putting hard dates on exploratory items creates false commitments.
  Use confidence levels instead.
- **Inside-out planning** — Building what's easy or what the loudest stakeholder wants, rather
  than what the market validated. Always ask: "What market evidence supports this?"
- **Static roadmaps** — A roadmap that hasn't changed in 6 months is either perfect (unlikely)
  or abandoned. Treat it as a living document.
- **One-size-fits-all** — Showing engineering-level detail to executives, or theme-only views to
  developers. Tailor the view.
- **Selling futures** — Sales teams using the roadmap to close deals on unbuilt features. The
  roadmap is a plan, not a commitment. Establish clear rules about what can and cannot be shared
  externally.

## Output Formats

When the user asks you to create a roadmap, produce a structured document. Choose the format
based on context:

- **Markdown document** — For draft roadmaps, internal reviews, or text-based collaboration.
  Use the template in `references/roadmap-template.md`.
- **Presentation (PPTX)** — For executive reviews or stakeholder presentations. Read the pptx
  skill at `/mnt/skills/public/pptx/SKILL.md` before creating.
- **Spreadsheet (XLSX)** — For detailed prioritization matrices or roadmap tracking. Read the
  xlsx skill at `/mnt/skills/public/xlsx/SKILL.md` before creating.

## Relationship to Other Pragmatic Framework Activities

The Product Roadmap doesn't exist in isolation. It draws from and feeds into:

- **Market Problems** → Themes should map to validated market problems
- **Competitive Landscape** → Competitive pressure influences priority and timing
- **Business Plan** → Roadmap must align with investment and revenue assumptions
- **Positioning** → Roadmap themes inform what you'll position around
- **Requirements** → Roadmap themes decompose into detailed requirements
- **Launch** → Roadmap timing drives launch planning
- **Stakeholder Communications** → Roadmap is a primary communication vehicle
- **Innovation** → Roadmap should reserve capacity for creative problem-solving

## Keywords

product roadmap, roadmap planning, roadmap strategy, roadmap prioritization, release plan,
product vision, feature prioritization, theme-based roadmap, outcome-based roadmap, now next
later, roadmap presentation, roadmap review, Pragmatic Framework, Focus category, roadmap
communication, roadmap stakeholders, quarterly roadmap, product marketing roadmap
