---
name: pragmatic-engagement
description: "Guides Engagement in the 2027 Pragmatic Framework (Go-to-Market; formerly Nurturing): programs that move people from awareness to active interest, evaluation, trial and early use, and keep the product in view through long or complex buying cycles. Covers multi-channel engagement, objection handling, making differentiation clear, trial and proof-of-concept programs, lead lifecycle stages, lead scoring, persona-by-stage content mapping, workflow design, marketing-sales handoffs and funnel metrics. Use whenever someone mentions engagement programs, lead nurturing, nurture campaigns, drip campaigns, lead scoring, MQL-to-SQL conversion, funnel velocity, trial conversion, free trial or POC programs, evaluation-stage content, objection handling in campaigns, stalled deals, re-engagement, or moving prospects from interest to evaluation. Grounds every program in validated market problems, buyer personas, positioning and the buyer journey."
---

# Engagement — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Go-to-Market — *How will the market find, choose and stay with the product?*
- **Focus-area question:** *What moves people from interest to evaluation and trial?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Marketing Plan, Growth, Retention, Launch, Organizational Alignment, Awareness, Customer Satisfaction
- **Formerly:** Nurturing (Programs category)

## Overview

Engagement picks up where Awareness leaves off. It moves people from initial awareness to active interest, evaluation, trial and early use, and keeps your product in view through long or complex buying cycles. Good engagement:

- **uses several channels** — email, web, webinars and events, trials, communities, direct sales conversations — coordinated rather than repeated;
- **addresses objections** evaluators actually raise, with evidence;
- **makes differentiation clear** against the alternatives buyers compare you with, including doing nothing.

Lead nurturing (scoring, lifecycle stages, automated workflows) is still a core technique, but it's one part of the job, not the definition.

### Who does the work

Sales often leads engagement, especially in complex B2B deals. Marketing runs programs and automation, customer experience teams contribute what they hear from trial users and new customers, and product teams bring knowledge of buyer behavior, objections and the product's real differentiators. Product marketers connect all of it to positioning and the buyer journey.

### Related focus areas

- **Awareness** (`pragmatic-awareness`, Go-to-Market) — brings people into view; Engagement takes over at interest. Events serve both; use Awareness's event briefing and speaker prep templates for engagement events.
- **Buyer Journey** (`pragmatic-buyer-journey`, Planning) and **Buyer Personas** (`pragmatic-buyer-personas`, Planning) — who you engage and how they buy.
- **Positioning** (`pragmatic-positioning`, Planning) — the differentiation each touch must make clear.
- **Competitive Landscape** and **Win/Loss Analysis** (Market) — alternatives and objections.
- **Content** and **Assets** (`pragmatic-content`, `pragmatic-assets`, Enablement) — what engagement programs deliver; objection handlers and case studies live in Assets.
- **Organizational Alignment** (`pragmatic-organizational-alignment`, Go-to-Market) — shared definitions and handoffs across marketing, sales and CS.
- **Growth** (`pragmatic-growth`, Go-to-Market) — trial conversion and new pipeline.
- **Adoption** (`pragmatic-adoption`, Enablement) and **Retention** (`pragmatic-retention`, Go-to-Market) — take over once early use becomes ongoing use.
- **Measurement** (`pragmatic-measurement`, Business) — indicators for engagement programs.

## When to Read Reference Files

1. **New engagement strategy or audit** → `references/engagement-strategy-guide.md` (lifecycle stages, scoring, content mapping, workflow patterns, multi-channel orchestration, objections, trials, metrics).
2. **Writing the program document** → use `templates/engagement-program-template.md` as the deliverable structure.

## Workflow

### Step 1: Establish the Engagement Foundation

Ask about:
- **Product / market context** — product or portfolio, target segments.
- **Current state** — existing programs, marketing automation, CRM, trial or freemium offer.
- **Buyer personas and buyer journey** — documented? Typical stages, sponsors and approvers, friction points?
- **Awareness programs** — what brings people into view today?
- **Sales cycle** — length, deal size, number of touches, who leads.
- **Objections and alternatives** — what evaluators push back on, and what they compare you with.
- **Goals** — more qualified pipeline, faster evaluation, higher trial conversion, higher win rates.

If buyer personas or buyer journey work is missing, flag it. Engagement without them becomes generic and product-centric. Recommend completing that work first, or build lightweight versions as part of this effort.

### Step 2: Define Lifecycle Stages

Map stages to the buyer journey. A typical model:

1. **Known contact** — opted in, no engagement signal
2. **Engaged** — showing interest (content, webinars, repeat visits)
3. **Marketing Qualified (MQL)** — meets fit and engagement thresholds
4. **Sales Accepted (SAL)** — sales has accepted for outreach
5. **Opportunity / Evaluation (SQL)** — confirmed need, authority, timeline
6. **Trial / Proof of Concept** — hands-on evaluation with defined success criteria
7. **Customer, early use** — closed; hand off to Adoption and Retention

For each stage define entry and exit criteria, owner (marketing, sales, CS, product) and SLA. Product-led models may put trial before sales contact; adjust the order to how your buyers actually buy.

### Step 3: Build the Lead Scoring Model

Combine **fit** (who they are: persona, segment, role, company size) with **engagement** (what they do: high-intent actions such as pricing page, demo or trial requests; mid-intent such as case studies and webinars; low-intent such as blog reads; negative signals such as inactivity). Set MQL, recycle and decay thresholds. Details in `references/engagement-strategy-guide.md`.

### Step 4: Map Content, Objections and Differentiation to Stages

Build a persona × stage matrix:

| Stage | Buyer need | Content types | Messaging focus |
|---|---|---|---|
| Interest | Understand the problem | Articles, research, explainer videos | Market problem education; no pitch |
| Evaluation | Compare approaches and vendors | Webinars, comparison guides, solution briefs, demos | Differentiation against real alternatives |
| Decision | Build the case, remove risk | Case studies, ROI calculators, references, security docs | Proof of value; answers to top objections |
| Trial / early use | Reach first value | Guided setup, in-product help, office hours | Getting to the outcome they bought for |

Then build an **objection map** (objection → persona → stage → evidence → touch) from win/loss interviews, sales notes and trial feedback, and a **differentiation proof** table (alternative → differentiator → proof). Flag content gaps for Content (`pragmatic-content`) and tool gaps for Assets (`pragmatic-assets`).

### Step 5: Design Multi-Channel Workflows

For each workflow: purpose, entry trigger, sequence (timing, channel, content), branching logic, exit conditions and handoff protocol. Coordinate channels — email, web personalization, retargeting, social, events and webinars, direct sales outreach, in-product messages — so they complement rather than repeat each other.

Common workflows: welcome; problem education; solution evaluation; trial conversion (first-value moment, stall triggers, sales or solutions assist); stalled-deal re-engagement; early-use handoff to onboarding; expansion and cross-sell; win-back.

### Step 6: Define Metrics and Optimization

- **Progression** — stage-to-stage conversion, time in stage, overall velocity
- **Evaluation and trial** — trial start and conversion rates, time to first value, POC success rate
- **Engagement** — channel and content engagement by stage, score progression
- **Business impact** — MQL-to-SQL conversion, win rate and deal size for engaged vs. non-engaged, pipeline contribution, CAC impact
- **Cadence** — weekly delivery and engagement; monthly conversion and workflow performance; quarterly scoring, objections and content-gap review; annual strategy review with the marketing plan

## Internal products

For internal platforms, "evaluation and trial" means teams piloting the platform before committing to migrate. Engage them with pilots that have clear success criteria, demos and office hours aimed at specific objections (migration effort, reliability, lost flexibility), and named champions. Track pilot-to-adoption conversion rather than pipeline.

## Key Pragmatic Principles

- **Outside-in** — lead with the buyer's problems, not your features.
- **NIHITO** (Nothing Important Happens In The Office) — validate messages and objection handling with real prospects and customers.
- **Journey alignment** — every touch maps to a real step buyers take.
- **Persona specificity** — tailor to each persona's problems, language and evaluation criteria.
- **Shared handoffs** — engagement fails without agreed definitions and SLAs across marketing, sales and CS.

## Common Pitfalls

1. Treating engagement as "just email" or just lead scoring.
2. Repeating benefits without answering the objections evaluators raise.
3. Claiming differentiation instead of proving it against real alternatives.
4. Offering trials with no defined first-value moment, owner or follow-up.
5. Scoring models set once and never validated against outcomes.
6. No sales feedback loop on lead quality.
7. Workflows built around the internal sales process rather than the buyer journey.
8. Over-messaging, and no clear exits from programs.

## Using AI in this focus area

- Cluster objections from call transcripts, win/loss notes and trial feedback, and draft first versions of objection-handling content.
- Draft persona- and stage-specific email and content variants from approved positioning; suggest branching logic.
- Analyze engagement and trial data to spot stall points and test scoring weights against closed deals.
- Rules: check AI output against real market evidence — AI can summarize objections but can't replace talking to evaluators (NIHITO still applies). Keep sensitive customer, deal and company data out of tools not approved for it. The team, not the tool, owns the decisions. Watch for over-automated, impersonal sequences that hurt trust in long buying cycles.

## Deliverable

The primary output is an **Engagement Program Document** using `templates/engagement-program-template.md`, actionable enough for marketing operations and sales to implement.

## Reference Files

| File | Use |
|---|---|
| `references/engagement-strategy-guide.md` | Full methodology: lifecycle, scoring, content mapping, workflows, multi-channel, handoffs, objections, trials, metrics, pitfalls |
| `templates/engagement-program-template.md` | Program document template |
