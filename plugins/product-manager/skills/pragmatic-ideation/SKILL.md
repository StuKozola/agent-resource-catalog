---
name: pragmatic-ideation
description: "Guide teams through the Ideation focus area of the Pragmatic Framework (formerly Innovation): exploring and shaping possible solutions before committing to delivery by turning validated market problems and user insight into concepts, prototypes and experiments tested with real users. Use whenever someone asks about ideation, product discovery, solution exploration, concept testing, prototyping, experiments, assumption testing, riskiest assumption, ideation or innovation workshops, ideation or innovation briefs, opportunity scorecards, idea or innovation portfolios, market-driven innovation, or 'which ideas hold up when we test them with users?'. Also trigger when a team wants to channel creative energy toward validated market problems, decide which ideas to keep or drop based on evidence, or plan an experiment before building. Even without the word 'Pragmatic', use this skill when someone wants to connect idea generation to real customer problems and user testing."
---

# Ideation — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Planning — *What are we building, for whom, and why?*
- **Focus-area question:** *Which ideas hold up when we test them with users?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Positioning, Buyer Journey, Buyer Personas, User Personas, Requirements, Stakeholder Management
- **Formerly:** Innovation (moved from the Business category to Planning)

## What This Skill Does

Ideation is where the team explores and shapes possible solutions before committing to full delivery. It turns market problems and user insight into concepts, prototypes and experiments that can be tested. The rules are simple: ground every idea in a validated market problem, involve the people who will build and use the product, test early with real users, and keep only the ideas that earn evidence. Drop the rest.

This is not brainstorming in a vacuum, and it is not "innovation" as a department. It's a disciplined loop: **problem → concept → test with users → keep, change or drop.** The Pragmatic Institute Design course covers Ideation together with Market Problems and User Personas.

## Core Principles

1. **Validated market problems are the starting point.** If you can't name the problem, who has it and how often, you're guessing, not ideating.
2. **Involve builders and users.** Engineers, designers and real users shape better concepts than a product manager alone. Builders who watch users struggle make better design decisions later.
3. **Test early, cheaply, with real users.** A paper prototype tested with five target users this week beats a polished build next quarter. Colleagues and friendly customers are not a substitute.
4. **Ideas must earn evidence.** Set a success threshold before each test. Keep what meets it; change or drop what doesn't. Dropping ideas is a sign the process works.
5. **Innovation ≠ invention.** A valuable idea can be a new feature, a new delivery model, new pricing or packaging, a new service or a process change. It doesn't have to be revolutionary.
6. **Leverage what you're good at.** Distinctive competencies and existing assets make ideas more defensible, but they are an input, not the starting point. The problem comes first.

## Prerequisites

- **Market Problems** (Market, `pragmatic-market-problems`) — required. Validated, prioritized, urgent and pervasive problems from customer interviews.
- **User Personas** (Planning, `pragmatic-user-personas`) — required. Who will use the solution, their workflows and workarounds, and real users to test with.
- **Distinctive Competencies** and **Product Strategy** (Market) — recommended. What you're good at and what the product will (and won't) be known for.
- **Competitive Landscape** (Market) — recommended. Alternatives, including doing nothing.
- **Win/Loss Analysis** (Market) — helpful. Unmet needs from recent deals.

If the required inputs are missing, gather them first. Use `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/references/readiness-checklist.md`.

## How to Use This Skill

### Step 1: Check readiness

Ask: Which validated market problem are we working on? Who are the users, and can we put concepts in front of them this month? Who decides keep, change or drop? Use `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/references/readiness-checklist.md`.

### Step 2: Choose the deliverable

| Need | Template |
|---|---|
| Run a session that turns problems into testable concepts | `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/workshop-plan.md` |
| Capture one concept, its assumptions and its tests | `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/ideation-brief.md` |
| Plan a single test: hypothesis, riskiest assumption, method, users, success threshold, decision | `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/experiment-plan.md` |
| Compare concepts to decide what to test or fund | `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/opportunity-scorecard.md` |
| Manage many concepts and experiments together | `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/idea-portfolio.md` |

### Step 3: Run the loop

**Market problem → concept → riskiest assumption → experiment with users → decision**

1. Generate concepts against a specific validated problem (workshop).
2. Write a short Ideation Brief for the promising ones.
3. Name the riskiest assumption (desirability, usability, viability or feasibility).
4. Design the cheapest test that could prove it wrong: concept interviews, paper or clickable prototypes, fake doors, concierge tests, technical spikes, small pilots.
5. Set the success threshold and decision rule *before* testing.
6. Run it with real target users, with builders watching.
7. Decide: keep (test the next assumption or hand to delivery), change and re-test, or drop. Record what was learned either way.

If someone says "we should build X because it would be cool," redirect: "Which market problem does X solve, for whom, and how would we know users want it?"

### Step 4: Hand off what earned evidence

- **Requirements** (Planning, `pragmatic-requirements`) — Kept concepts become problem-based requirements and use scenarios, with the test evidence attached.
- **Product Roadmap** (Focus, `pragmatic-product-roadmap`) — Kept concepts are sequenced as outcomes.
- **Business Plan** (Business, `pragmatic-business-plan`) — Large bets need an investment case.
- **Positioning** (Planning, `pragmatic-positioning`) — Concepts that change what the product solves may change the positioning.
- **Stakeholder Management** (Planning, `pragmatic-stakeholder-management`) — Keep leaders clear on what's being tested, what was dropped and why.

## Roles

**Primary owner:** product manager or product line manager.
**Involved:** engineering and design (shaping concepts and building prototypes), real users (testing), customer-facing teams (market signal), an executive sponsor for larger bets.
**Skills:** synthesizing research into a story, designing fair experiments, technical judgment about what's feasible, facilitation, and the discipline to drop ideas.

## Types of Ideas

- **Incremental** — Improvements to existing products. Lower risk, faster to test.
- **Adjacent** — Existing capabilities applied to new markets, or new approaches in existing markets.
- **Transformational** — New products, technologies or business models. Highest risk; test the riskiest assumption first and expect most to be dropped.

A healthy idea portfolio covers all three, weighted toward incremental and adjacent.

## Common Anti-Patterns

1. **Technology push** — "We built something cool; now let's find a market." Start from the problem.
2. **Single-customer ideas** — Building for one loud customer without checking pervasiveness.
3. **Copying competitors** — Adopting a competitor's feature without validating that your market needs it.
4. **Ideation theater** — Workshops and hackathons that produce excitement but no tests and no decisions.
5. **Testing with the wrong people** — Colleagues, executives or only friendly customers instead of target users.
6. **Moving the goalposts** — Setting the success threshold after seeing the results.
7. **Never dropping anything** — If every idea "passes," you aren't testing.

## Using AI in this focus area

- Generate a wide range of concepts and analogies from other industries against a stated problem, then filter them as a team.
- Build quick prototypes, mock screens and test scripts so the team can get in front of users sooner.
- Summarize usability sessions and experiment results against the success threshold.

AI makes ideas and prototypes cheap; it does not make evidence. Only tests with real users count (NIHITO still applies). Keep sensitive customer and company data out of tools not approved for it. The team, not the tool, decides what to keep and what to drop.

## Reference Files

- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/references/readiness-checklist.md` — Readiness check before starting ideation
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/workshop-plan.md` — Facilitation guide for an ideation workshop
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/ideation-brief.md` — One-concept brief (formerly the Innovation Brief)
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/experiment-plan.md` — One-page experiment plan
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/opportunity-scorecard.md` — Weighted scorecard for comparing concepts
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-ideation/templates/idea-portfolio.md` — Idea portfolio assessment across many concepts
