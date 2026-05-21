---
name: pragmatic-nurturing
description: "Guide users through the Pragmatic Institute Framework's Nurturing activity — developing programs to move prospects quickly and effectively through the funnel, turning them into satisfied customers. Use this skill whenever someone mentions lead nurturing, nurture programs, nurture campaigns, drip campaigns, lead scoring, MQL-to-SQL conversion, prospect progression, funnel velocity, nurture workflows, buyer journey content mapping, or moving leads through the funnel. Also trigger when users ask about designing email sequences for prospects, building lead scoring models, mapping content to funnel stages, aligning marketing automation with buyer personas, or creating programs that convert awareness into pipeline. This skill applies the Pragmatic Institute's market-driven, outside-in philosophy to nurturing strategy — grounding every nurture program in validated market problems, buyer personas, and the documented buyer experience rather than product-centric messaging."
---

# Pragmatic Framework: Nurturing

## Overview

**Nurturing** is an activity in the **Programs** category of the Pragmatic Framework. The official Pragmatic Institute definition:

> **Develop programs to move prospects quickly and effectively through the funnel, with the objective of turning prospects into satisfied customers.**

Nurturing sits on the **execution** side of the framework and connects directly to several other Pragmatic activities: Awareness (which fills the top of funnel), Buyer Personas (which define who you nurture), Buyer Experience (which maps how they buy), Positioning (which supplies the messaging), Content (which provides the assets), and Measurement (which tunes performance). Nurturing is covered in Pragmatic Institute's **Launch** and **Market** courses.

### Pragmatic Responsibilities (from Framework Roles & Responsibilities)

- Develop a lead nurturing process to turn prospects into satisfied customers
- Upsell or cross-sell existing customers on new products and services

### Required Skills

- Understanding of business goals and market problems
- Analytics and measurement focus
- Digital marketing

## When to Read Reference Files

Before starting work, read the appropriate reference file:

1. **Starting a new nurturing strategy or audit** → Read `references/nurturing-strategy-guide.md` for the complete methodology, lead scoring frameworks, content mapping, and workflow design patterns
2. **Creating a nurture workflow or campaign document** → Read `references/nurturing-strategy-guide.md` for workflow design, then use `templates/nurturing-program-template.md` as the deliverable structure

## Workflow

Follow these six steps to guide the user through developing a Nurturing program grounded in Pragmatic principles.

### Step 1: Establish Nurturing Foundation

Gather the user's context before designing anything. Ask about:

- **Product / market context**: What product or portfolio? What market segments?
- **Current state**: Do they have existing nurture programs? Marketing automation platform? CRM?
- **Buyer personas**: Have they completed the Pragmatic Buyer Personas activity? Who are the key buyers?
- **Buyer experience**: Is the buying process documented? What are the typical stages and barriers?
- **Awareness programs**: What fills the top of funnel today (campaigns, content, events)?
- **Sales cycle**: Average length? Typical deal size? Number of touches before close?
- **Goals**: What does success look like — more MQLs, faster conversion, higher win rates, expansion revenue?

If buyer personas or buyer experience work hasn't been done, flag this as a gap. Nurturing without these inputs leads to generic, product-centric programs that underperform. Recommend completing those activities first, or at minimum, build lightweight versions as part of this effort.

### Step 2: Define Lead Lifecycle Stages

Help the user define clear lifecycle stages that map to their buyer experience. A typical Pragmatic-aligned model:

1. **Subscriber / Known Contact** — Opted in but no engagement signal
2. **Engaged Lead** — Showing interest (content downloads, webinar attendance, repeat visits)
3. **Marketing Qualified Lead (MQL)** — Meets fit + engagement thresholds; ready for targeted nurturing
4. **Sales Accepted Lead (SAL)** — Sales has reviewed and accepted for outreach
5. **Sales Qualified Lead (SQL)** — Active opportunity with confirmed need, authority, timeline
6. **Customer** — Closed/won; transitions to retention and expansion nurturing
7. **Advocate** — Engaged customer willing to amplify (connects to Advocacy activity)

For each stage, define:
- **Entry criteria** (what qualifies a lead to enter this stage)
- **Exit criteria** (what triggers progression to the next stage)
- **Owner** (marketing vs. sales responsibility)
- **SLA** (how quickly the receiving team must act)

### Step 3: Build the Lead Scoring Model

Design a scoring system that combines **fit** (who they are) and **engagement** (what they do). Load `references/nurturing-strategy-guide.md` for detailed scoring frameworks.

**Fit scoring** (demographic/firmographic):
- Matches target buyer persona (+high)
- Company in target market segment (+high)
- Right role / title / authority level (+medium)
- Company size and revenue in range (+medium)

**Engagement scoring** (behavioral):
- High-intent actions: pricing page, demo request, contact form (+high)
- Mid-intent: case study downloads, webinar attendance, product page visits (+medium)
- Low-intent: blog reads, social engagement, email opens (+low)
- Negative signals: unsubscribe, bounce, inactivity over 90 days (−points)

Define thresholds:
- **MQL threshold**: Score at which marketing passes to sales
- **Recycle threshold**: Score at which rejected leads return to nurturing
- **Decay rules**: How scores decrease over time without activity

### Step 4: Map Content to Funnel Stages and Personas

Create a content map that aligns available and needed content to each funnel stage and buyer persona. This directly leverages the Pragmatic Content and Positioning activities.

| Funnel Stage | Buyer Need | Content Types | Messaging Focus |
|---|---|---|---|
| **TOFU** (Awareness → Engaged) | Understanding the problem | Blog posts, infographics, industry reports, educational videos | Market problem education; no product pitch |
| **MOFU** (Engaged → MQL) | Evaluating approaches | Whitepapers, webinars, comparison guides, solution briefs | How the category solves the problem; thought leadership |
| **BOFU** (MQL → SQL) | Selecting a vendor | Case studies, ROI calculators, product demos, testimonials | Proof of value; competitive differentiation |
| **Post-Sale** (Customer → Advocate) | Maximizing value | Onboarding guides, best practices, user community, advanced training | Adoption, expansion, loyalty |

For each buyer persona, identify:
- Which content assets already exist
- Which gaps need to be filled (flag for the Content activity)
- Which Positioning messages apply at each stage

### Step 5: Design Nurture Workflows

Build specific automated workflows. For each workflow:

1. **Name and purpose** — What segment does this serve and what's the goal?
2. **Entry trigger** — What action or status places someone into this workflow?
3. **Sequence** — Ordered series of touches with timing, channel, and content
4. **Branching logic** — How the workflow adapts based on prospect behavior
5. **Exit conditions** — What removes someone (conversion, disqualification, opt-out)
6. **Handoff protocol** — How and when leads transfer to sales

**Common Pragmatic-aligned workflows:**

- **New Subscriber Welcome**: Introduce brand, share top educational content, progressive profiling
- **Problem Education (TOFU → MOFU)**: Educate on market problems the product solves
- **Solution Evaluation (MOFU → BOFU)**: Comparison content, analyst reports, peer proof
- **Sales Acceleration (BOFU)**: Demo offers, consultation requests, buying guides
- **Stalled Deal Re-engagement**: Re-nurture leads that went cold after sales contact
- **Customer Onboarding**: Drive adoption and time-to-value for new customers
- **Expansion / Cross-sell**: Introduce adjacent products to existing customers
- **Win-back**: Re-engage churned or lapsed customers

### Step 6: Define Metrics and Optimization Plan

Establish KPIs aligned with Pragmatic's Measurement activity:

**Funnel velocity metrics:**
- Stage-to-stage conversion rates (Engaged → MQL → SAL → SQL → Won)
- Average time in each stage
- Overall funnel velocity (time from first touch to close)

**Engagement metrics:**
- Email open rates, click-through rates by workflow
- Content engagement by funnel stage
- Lead score progression over time

**Business impact metrics:**
- MQL-to-SQL conversion rate
- Nurtured vs. non-nurtured win rates
- Average deal size: nurtured vs. non-nurtured
- Customer acquisition cost (CAC) impact
- Pipeline contribution from nurture programs

**Optimization cadence:**
- Weekly: Monitor email engagement and delivery metrics
- Monthly: Review stage conversion rates and workflow performance
- Quarterly: Audit lead scoring model accuracy, content gaps, and funnel velocity
- Annually: Full nurture strategy review aligned with marketing plan refresh

## Key Pragmatic Principles for Nurturing

- **Outside-in thinking**: Nurture content should address market problems, not product features. Lead with the buyer's world, not yours.
- **NIHITO (Nothing Important Happens In The Office)**: Validate nurture messaging with actual prospects and customers, not just internal assumptions.
- **Buyer experience alignment**: Every nurture touch should map to a documented step in the buyer's journey.
- **Persona specificity**: Generic nurture programs underperform. Segment by buyer persona and tailor messaging to their specific problems, language, and evaluation criteria.
- **Sales-marketing alignment**: Nurturing fails without clear handoff protocols and shared definitions of MQL/SQL. This connects directly to the Sales Alignment activity.

## Deliverable

The primary output is a **Nurturing Program Document** — use `templates/nurturing-program-template.md` as the structure. This document should be actionable enough for marketing operations to implement in their automation platform.
