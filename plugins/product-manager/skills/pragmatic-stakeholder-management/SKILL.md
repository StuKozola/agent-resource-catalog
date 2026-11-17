---
name: pragmatic-stakeholder-management
description: >
  Guide product managers and product marketers through the Stakeholder Management focus area of the
  Pragmatic Framework (formerly Stakeholder Communications): building and keeping shared clarity on
  priorities, decisions, timing, responsibilities and trade-offs across leaders, teams and partners.
  Use whenever someone needs to identify or map stakeholders, assess interest and influence, set up a
  RACI or decision rights, build a stakeholder communication plan, prepare roadmap updates or
  executive briefings, communicate trade-offs or priority changes, align cross-functional teams on
  who owns what, or report on product progress. Trigger for "stakeholder management," "stakeholder
  communications," "stakeholder map," "RACI," "stakeholder update," "roadmap communication,"
  "executive briefing," "release communication," "keeping stakeholders informed," or
  "are priorities and responsibilities clear to everyone?".
---

# Stakeholder Management — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Planning — *What are we building, for whom, and why?*
- **Focus-area question:** *Are priorities, responsibilities and trade-offs clear to everyone involved?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Positioning, Buyer Journey, Buyer Personas, User Personas, Requirements, Ideation
- **Formerly:** Stakeholder Communications

## What Stakeholder Management Covers

Stakeholder management builds and keeps shared clarity on **priorities, decisions, timing, responsibilities and trade-offs** across leaders, teams and partners. Done well, it builds trust, keeps people informed and reduces risk: fewer surprises, fewer stalled decisions, fewer arguments about who owns what.

It is broader than sending updates. Communication is the main tool, but the goal is that everyone involved can answer: *What are we prioritizing and why? Who decides what? When is it happening? What did we give up?*

Start by identifying your stakeholders and what each needs from you. Different groups need different things: employees often need detailed updates, executives need strategic insight, and customers want clear timelines for features or upgrades. Then plan how and when you'll engage each group.

**Key principle — proactive, not reactive.** Don't wait for stakeholders to ask. Set a cadence, make decision rights explicit, and deliver the right information to the right audience before they need it. The Pragmatic Institute Build course covers Stakeholder Management.

**Responsibilities:**
- Identify stakeholders and what each needs; maintain a stakeholder map
- Make decision rights and responsibilities explicit (RACI)
- Communicate priorities, timing and trade-offs proactively, from strategy through execution
- Define key metrics and goals for progress, and report against them
- Surface risks and priority changes before they surprise anyone

**Skills:** understanding of the roadmap, release plan and project plan; written and verbal communication; working with project and program management; managing up, down and sideways.

## When This Applies

- **Strategy:** market problems, product strategy, positioning decisions
- **Planning:** roadmap, release plans, priority rationale, what was said no to
- **Build:** progress, scope changes, trade-offs, expectations
- **Launch:** cross-functional readiness, pre-launch briefings
- **Post-launch:** metrics, progress toward goals, market response, escalations

## Core Workflow

### Step 1 — Map stakeholders

List the people and groups affected by, contributing to, or able to block the work, and rate interest and influence.

- **Internal:** executives, engineering, design, sales, marketing, customer success and support, product operations, finance, legal
- **External:** key customers and design partners, channel and implementation partners, analysts and press (via marketing)

For each, capture: interest, influence, what they need from you, cadence, channel and owner.

> Template: `templates/stakeholder-map.md` (stakeholder map, interest/influence grid, decision RACI, trade-off log).
> Reference: `references/stakeholder-audience-guide.md` (each audience's information needs and triggers).

### Step 2 — Make decision rights explicit

Shared clarity breaks down most often over *who decides*. For the key decisions on the initiative (which problems to solve next, scope and trade-offs, timing, positioning, pricing, launch go/no-go, external roadmap commitments), record who is Responsible, Accountable, Consulted and Informed. Exactly one accountable person per decision. Use the RACI in `templates/stakeholder-map.md`.

### Step 3 — Determine what each audience needs

Apply outside-in thinking internally too. For each audience:
1. What decisions are they making that your information should inform?
2. What level of detail: strategic themes, milestone dates or feature specifics?
3. What concerns or objections might they have?
4. What format works: executive summary, release notes, roadmap visual, chat update?

Always connect the "what" to the market problem it solves. The roadmap is a plan, not a commitment; be clear about what is known, planned and future.

### Step 4 — Define metrics and goals

Ground updates in measurable reality: which progress metrics you'll report (delivery progress, adoption, win rates), which milestones mark progress (beta, GA, adoption targets), and how often. Indicators come from Measurement (Business, `pragmatic-measurement`).

### Step 5 — Build the communication plan

For each audience: purpose, key content, format, frequency, owner, and how you'll know it landed.

| Audience | Purpose | Key Content | Format | Frequency | Owner |
|---|---|---|---|---|---|
| Executives | Strategic alignment | Progress vs. goals, risks, trade-offs, decisions needed | Briefing doc | Monthly | PM |
| Sales | Readiness | Upcoming releases, competitive context | Update + Q&A | Bi-weekly | PMM |
| Engineering | Context | Market rationale for priorities, trade-offs | Sprint context notes | Per sprint | PM |
| Key customers | Relationship + feedback | Problems being worked on, not dates | Roadmap conversation | Quarterly | PM |
| Partners | Readiness | Timelines, integration and training needs | Partner update | Quarterly + per release | PMM |

> Template: `templates/communication-plan-template.md`.

### Step 6 — Present the roadmap per audience

The roadmap is one of the most common stakeholder artifacts. Building it belongs to Product Roadmap (Focus, `pragmatic-product-roadmap`); here the job is presenting it so each audience gets the right view: executives see themes and outcomes, sales sees problems solved and competitive impact, engineering sees initiatives and sequencing, customers see problems being solved. Dated roadmaps create commitment expectations; undated (now/next/later) roadmaps communicate direction without locking dates.

> Reference: `references/roadmap-formats.md`.

### Step 7 — Communicate trade-offs and changes

When priorities shift, tell the people affected before they hear it elsewhere: what changed, why (market evidence), what was given up, who decided, and what it means for them. Log decisions and trade-offs (Part 3 of `templates/stakeholder-map.md`). Define out-of-cycle triggers: major scope change, competitive move, missed milestone, priority shift, escalation.

### Step 8 — Maintain cadence and measure

Make it routine: calendar holds, reusable templates, feedback loops (questions received, alignment in follow-ups). Report against the agreed metrics and flag goals at risk *before* they're missed. Revisit the stakeholder map at least quarterly.

## Common Output Artifacts

1. **Stakeholder map and decision RACI** — `templates/stakeholder-map.md`
2. **Communication plan** — `templates/communication-plan-template.md`
3. **Executive briefing** — `templates/executive-briefing-template.md`
4. **Release communication** — `templates/release-communication-template.md`
5. **Audience-specific roadmap views** — `references/roadmap-formats.md`
6. **Progress report** — metrics vs. goals, milestones, risks, trade-offs and decisions needed

## Related Focus Areas

| Focus area | Relationship |
|---|---|
| **Product Roadmap** (Focus) | Source of plans; translate into audience-specific views |
| **Product Strategy** and **Market Problems** (Market) | The "why" behind every priority and every "no" |
| **Requirements** (Planning) | What is being built, for whom and why; use scenarios ground updates in real problems |
| **Ideation** (Planning) | What's being tested, what was dropped and why |
| **Positioning** (Planning) | Internal audiences understand the strategic "why" |
| **Organizational Alignment** and **Launch** (Go-to-Market) | Go-to-market teams share the picture of audience, value and readiness |
| **Escalations** (Operations) | Who owns a critical issue and how leaders and customers are kept informed |

Boundary: Stakeholder Management keeps leaders, teams and partners clear on the *product's* priorities, decisions and trade-offs. Organizational Alignment (`pragmatic-organizational-alignment`) gets go-to-market and customer-facing teams sharing the same picture of the audience and the value.

## Common Pitfalls

- **Reactive communication** — waiting to be asked
- **Unclear decision rights** — two people think they're accountable, or nobody does
- **Hidden trade-offs** — announcing what's in without saying what's out
- **One-size-fits-all messaging** — the same update for executives, sales and engineering
- **Feature-first framing** — not connecting work to the market problem it solves
- **Dates as commitments** — roadmap dates without caveats
- **No metrics** — narrative-only progress
- **Surprise changes** — stakeholders hearing about priority shifts second-hand
- **Stale map** — a stakeholder map that isn't updated after reorgs or leadership changes

## Using AI in this focus area

- Draft audience-specific versions of the same update (executive, sales, engineering, customer) from one source.
- Summarize meeting notes and decision threads into a decision and trade-off log.
- Check that a draft update states the decision, the trade-off and the owner.

AI can draft the message, but relationships and trust are built by people; review every update before it goes out, and check claims against real evidence (NIHITO still applies for market rationale). Keep sensitive customer, deal and company data, including notes on individual stakeholders, out of tools not approved for it. The team, not the tool, owns the decisions and what is communicated.

## Reference Files

- `references/stakeholder-audience-guide.md` — Stakeholder types, information needs and communication triggers
- `references/roadmap-formats.md` — Presenting dated and undated roadmaps to different audiences
- `templates/stakeholder-map.md` — Stakeholder map, interest/influence grid, decision RACI and trade-off log
- `templates/communication-plan-template.md` — Communication plan
- `templates/executive-briefing-template.md` — Executive update format
- `templates/release-communication-template.md` — Release announcement structure
