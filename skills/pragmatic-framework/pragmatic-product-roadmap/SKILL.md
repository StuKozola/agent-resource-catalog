---
name: pragmatic-product-roadmap
description: >
  Create, review and refine product roadmaps using the 2027 Pragmatic Framework's Product
  Roadmap focus area: which outcomes come next, and in what order? Use whenever the user asks
  about product roadmaps, roadmap planning, sequencing outcomes, roadmap strategy or
  prioritization, outcome-based or theme-based roadmaps, roadmap types (strategy, portfolio,
  release, feature, theme), dated vs undated vs hybrid timelines, now/next/later, release
  planning, roadmap presentations, or tailoring a roadmap to executives, engineering, sales,
  marketing or customers. Also trigger on "roadmap review," "product roadmap document," tying
  a roadmap to product strategy, or how to build, structure or present a roadmap to stakeholders.
---

# Product Roadmap — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Focus — *Where should we play, and where should we invest?*
- **Focus-area question:** *Which outcomes come next, and in what order?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Market Definition, Distribution Strategy, Product Portfolio

## What a Product Roadmap Is

A product roadmap is a visual plan of the product's direction and priorities over time. It
communicates strategy, wins buy-in, and guides execution. The 2027 question frames it as a
**sequence of outcomes**: what results the product will deliver for the market and the business,
and in what order, not a list of features with dates.

Build one by gathering input, setting goals and success measures, and prioritizing work that
supports the **product strategy**. Choose a format that leaves room to change (dated, undated or
hybrid), tailor the detail to each audience, and update it as priorities change. Product Roadmap
is emphasized in Pragmatic Institute's Focus course.

A roadmap is a plan, not a commitment. Internalize that before anything else.

## Core Principles

**Outcomes in sequence.** Each roadmap item is an outcome: a problem solved for a persona, with a
measurable result ("cut month-end close from five days to two for operations analysts"). The
roadmap's job is to show which outcomes come first and why.

**Anchored in product strategy.** The roadmap is downstream of the product strategy
(`pragmatic-product-strategy`). Every theme should serve what the product is meant to be known
for. Work the strategy says no to stays off the roadmap, however loud the request.

**Market-driven, not inside-out.** Every item traces to a validated market problem, not an
internal pet feature. Evidence comes from market interviews, win/loss analysis and the
competitive landscape. If an item can't be linked to a real persona with a real problem, it
doesn't belong.

**Plan, not commitment.** Roadmaps are predictions. They change as the market changes. Be honest
about confidence: near-term items are higher confidence, later items are directional.

**Audience-tailored.** Different stakeholders need different views of the same roadmap. See
`references/audience-tailoring.md`.

## Roadmap Types

Pick the type that matches the decision and audience. Many teams keep more than one.

| Type | Shows | Typical audience |
|---|---|---|
| **Strategy** | How product strategy turns into outcomes over 1–3 years | Executives, board |
| **Portfolio** | Outcomes across several products and how they relate (see `pragmatic-product-portfolio`) | Leadership, portfolio council |
| **Release** | What ships in upcoming releases and what each release achieves | Engineering, launch teams, support |
| **Feature** | How a major capability evolves over time | Product and engineering, key customers |
| **Theme** | Problem-based themes and the outcomes under each | Most audiences; good default |

## Timeline Formats

| Format | What it looks like | Use when |
|---|---|---|
| **Undated** | Now / Next / Later | Uncertainty is high; you want to show sequence without false precision |
| **Dated** | Quarters or months | Contracts, regulation or fiscal planning demand dates; near-term work is well understood |
| **Hybrid** | Dates for near-term, Now/Next/Later beyond | Most mature teams: commit where you can, stay flexible where you can't |

## When to Use This Skill

- Creating a roadmap from scratch, or converting a feature list into outcomes and themes
- Reviewing or critiquing an existing roadmap
- Prioritizing and sequencing outcomes
- Preparing roadmap views for different audiences
- Aligning a roadmap with product strategy, business plan, positioning or market problems
- Building a product marketing roadmap alongside the product roadmap

## Step-by-Step: Building a Roadmap

### Phase 1: Gather Input

Collect these before touching the roadmap. If the user hasn't provided them, ask:

1. **Product strategy** — what the product will be known for, the problems it solves, what it
   says no to, and the company goals it supports (`pragmatic-product-strategy`)
2. **Validated market problems** — from Market Problems, Win/Loss Analysis and Competitive
   Landscape (Market category)
3. **Post-launch evidence** — Customer Value Realization, Exceptions and Escalations
   (Operations) often reveal outcomes customers aren't getting
4. **Distinctive competencies** — what you can deliver that others can't easily copy
5. **Business plan constraints** — revenue targets, investment limits, pricing changes,
   buy/build/partner decisions
6. **Existing commitments** — contracts, regulatory deadlines, technical debt that blocks progress
7. **Cross-functional plans** — marketing plan, launch calendar, partner schedules

### Phase 2: Set Goals and Success Measures

Turn the strategy into a short list of outcomes for the roadmap period. For each, define how
you'll know it worked: a leading indicator you can see early and a lagging result
(coordinate with `pragmatic-measurement`).

### Phase 3: Define Themes

Group work into **themes** — problems being solved, each tied to one or more outcomes.

**Good themes:** "Reduce time-to-value for new enterprise customers"; "Expand compliance
coverage for regulated industries"; "Improve self-service to reduce support load."

**Not themes (these are features):** "Build SSO integration"; "Add dashboard widgets";
"Migrate to microservices."

Each theme connects to a target persona, a validated market problem, and a measurable outcome.
If it doesn't connect to all three, it needs more work.

### Phase 4: Prioritize and Sequence

Use market evidence, not politics. Evaluate each theme on:

- **Urgency** — how painful is the problem now?
- **Pervasiveness** — how many target personas and segments have it?
- **Willingness to pay** — will solving it drive revenue or retention?
- **Strategic alignment** — does it serve the product strategy and use distinctive competencies?
- **Feasibility** — can you deliver it given resources and dependencies?

Then sequence: which outcome unlocks the next? Which must come first for the business plan to
hold? Document the reasoning; it will be challenged. See `references/prioritization-methods.md`.

### Phase 5: Choose Type and Format

Pick the roadmap type(s) and timeline format from the tables above. Whatever you choose, include:
- The product strategy or vision statement at the top
- Outcomes and themes with problem context, not just feature names
- Success measures per outcome
- Confidence levels (committed / planned / exploratory)
- What you're not doing this period, and why
- Last-updated date

Templates: `references/roadmap-template.md`.

### Phase 6: Tailor and Communicate

- **Executive:** outcomes, strategic fit, investment, risk. One page.
- **Engineering:** themes broken into epics, dependencies, technical milestones; still problem-framed.
- **Sales:** what they can discuss (carefully), what's not committed, how themes map to customer pain.
- **Marketing:** themes mapped to launch windows, positioning implications, content and campaign hooks.
- **External/customer:** high-level themes and problems being solved; no dates or feature specifics.

See `references/audience-tailoring.md`. For keeping stakeholders aligned on priorities and
trade-offs over time, see `pragmatic-stakeholder-management`.

### Phase 7: Review and Update

- **Monthly:** with product and engineering leads; adjust for new evidence, delivery progress, resources.
- **Quarterly:** with executives; check against the product strategy and business plan.
- **Ongoing:** feed in win/loss, market interviews, competitive intelligence and post-launch
  evidence (CVR, exceptions, escalations).
- **When the product strategy changes**, re-check every theme.

Explain *why* priorities shifted, not just *that* they shifted.

## Common Anti-Patterns

- **Feature laundry lists** — if it reads like a backlog, it's not a roadmap. Elevate to outcomes.
- **No link to strategy** — a roadmap that can't say which strategic choice each theme serves.
- **Date-driven promises** — hard dates on exploratory items. Use hybrid formats and confidence levels.
- **Inside-out planning** — building what's easy or what the loudest stakeholder wants.
- **Static roadmaps** — unchanged for six months means perfect (unlikely) or abandoned.
- **One-size-fits-all** — engineering detail for executives, or theme-only views for developers.
- **Selling futures** — sales closing deals on unbuilt features. Set clear rules on what can be shared.

## Output Formats

- **Markdown** — drafts and internal reviews; use `references/roadmap-template.md`
- **Presentation** — executive and stakeholder reviews; use the pptx skill
- **Spreadsheet** — prioritization matrices and tracking; use the xlsx skill

## Relationship to Other Focus Areas

- **Product Strategy** (Market) → the roadmap sequences the outcomes the strategy calls for
- **Market Problems** (Market) → themes map to validated problems
- **Competitive Landscape** (Market) → competitive pressure affects priority and timing (validate before copying)
- **Product Portfolio** (Focus) → portfolio roadmaps coordinate across products
- **Business Plan** (Business) → roadmap must fit investment and revenue assumptions
- **Measurement** (Business) → success measures and leading indicators for each outcome
- **Positioning** and **Requirements** (Planning) → themes inform positioning and decompose into requirements
- **Ideation** (Planning) → tested concepts earn their way onto the roadmap
- **Stakeholder Management** (Planning) → the roadmap is a primary tool for shared clarity on priorities
- **Launch** (Go-to-Market) → roadmap timing drives launch planning

## Using AI in this focus area

- Cluster a raw feature backlog into problem-based themes and draft outcome statements.
- Generate audience-specific views from one master roadmap.
- Run scoring and what-if sequencing across prioritization methods.
- Rules: check AI output against real market evidence; NIHITO still applies, and AI can't tell
  you which outcomes customers value most. Keep unreleased plans, customer commitments and
  financials out of tools not approved for them. The team, not the tool, owns the sequence.
- Weak spot: AI tends to restate features as "outcomes" without a measurable result. Check
  each one has a persona, a problem and a measure.

## Reference Files

- `references/roadmap-template.md` — theme (Now/Next/Later), quarterly, outcome-based and product marketing templates
- `references/prioritization-methods.md` — scoring, RICE, value vs effort, MoSCoW, opportunity scoring
- `references/audience-tailoring.md` — executive, engineering, sales, marketing and external views
