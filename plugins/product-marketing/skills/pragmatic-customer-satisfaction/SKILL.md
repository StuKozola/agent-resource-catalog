---
name: pragmatic-customer-satisfaction
description: >
  Guides Customer Satisfaction in the 2027 Pragmatic Framework (Go-to-Market; new, built
  partly from the former Advocacy focus area): how customers judge their experience with
  the product and their relationship with you after purchase, adoption or continued use —
  satisfaction, trust and relationship health. Covers building a satisfaction program,
  measuring regularly (CSAT, NPS, CES, relationship health scores, qualitative feedback),
  spotting issues early, acting on feedback and closing the loop, plus advocate
  identification and reference programs as signals of satisfaction. Use whenever the user
  mentions customer satisfaction, CSAT, NPS, customer effort score, customer health score,
  relationship health, customer trust, voice of the customer, satisfaction surveys,
  detractor follow-up, closed-loop feedback, customer advocacy, reference program,
  advocate recruitment or peer reviews. Case studies: pragmatic-assets; outcomes
  achieved: pragmatic-customer-value-realization.
---

# Customer Satisfaction — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Go-to-Market — *How will the market find, choose and stay with the product?*
- **Focus-area question:** *How do customers judge their experience with the product and their relationship with us?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Marketing Plan, Growth, Retention, Launch, Organizational Alignment, Awareness, Engagement
- **Formerly:** New in 2027; advocate and reference material comes from the retired Advocacy focus area

## What This Focus Area Covers

Customer satisfaction is the customer's **own evaluation** of their experience with the product and of their relationship with your organization, after purchase, adoption or continued use. It covers three things: **satisfaction** with the product and service, **trust** in you, and the **health of the relationship**.

The work is to measure satisfaction regularly, look for issues that could damage the relationship, act on what customers tell you, and close the loop with them and with the teams that can fix things.

**Signals, not the definition.** Willingness to recommend, references and reviews are useful signals that customers are satisfied. They don't define satisfaction. A customer may be very satisfied but barred by policy from being a reference; a vocal reviewer may be unhappy with your support. That's why the advocate and reference program is a sub-section of this skill, built on top of satisfaction measurement.

### Boundaries

| Focus area | Question | Relationship to Customer Satisfaction |
|---|---|---|
| **Customer Value Realization** (`pragmatic-customer-value-realization`, Operations) | Did customers get the outcome they bought the product for? | Different question. Satisfaction is how customers *feel* about their experience and relationship; value realization is whether they *achieved results*. Track both; they diverge. |
| **Retention** (`pragmatic-retention`, Go-to-Market) | Why do customers stay, and why do they leave? | Satisfaction is a leading input to renewal and expansion; retention tracks the behavior. |
| **Adoption** (`pragmatic-adoption`, Enablement) | Do customers start and keep using the product meaningfully? | Usage is behavior; satisfaction is judgment. |
| **Escalations** (`pragmatic-escalations`, Operations) | Who owns a critical issue, and what do we learn? | Severe satisfaction issues become escalations. |
| **Assets** (`pragmatic-assets`, Enablement) | Do teams have the tools to sell and support consistently? | Case studies are now built in Assets, using advocates identified here. |

### Who does the work

Customer success and support usually own day-to-day measurement and follow-up. Product managers and product marketers own the patterns: what customers' judgments say about the product, positioning and experience, and what should change. Sales and account managers own executive relationships. Marketing runs the advocate and reference program with customer success.

## Workflow

### Step 1: Assess the Current State

Ask about:
- **Existing measures** — CSAT, NPS, CES, health scores? Response rates? Which personas are surveyed?
- **Feedback channels** — surveys, CSM notes, support tickets, reviews, advisory boards, community.
- **What happens to feedback** — who reads it, who acts, does anyone tell the customer?
- **Known issues** — recent escalations, churn reasons, detractor themes, negative reviews.
- **Personas** — which buyer and user personas matter at renewal (economic buyer, admin, end user)?
- **Advocacy** — existing references, review presence, sales demand for references.

### Step 2: Define What Satisfaction Means Here

Decide the dimensions you'll judge (product experience, service experience, trust, relationship health), the personas you'll hear from at both person and account level, and the boundaries with value realization, adoption and retention. Load `references/satisfaction-measurement-guide.md`.

### Step 3: Design the Measurement Program

Choose measures and cadence:
- **Transactional** CSAT and CES after key touchpoints (onboarding, support, releases, renewal)
- **Relationship** survey (NPS plus satisfaction and trust items) quarterly or semiannually
- **Relationship health score** per account, refreshed monthly and validated against renewals and churn
- **Qualitative** interviews and coded verbatims every quarter, across satisfied, neutral and unhappy customers

Set baselines and targets, sampling rules and survey-fatigue limits. Use `templates/satisfaction-program-plan.md`.

### Step 4: Detect and Triage Issues

Define thresholds that trigger action: detractor responses, health score drops, repeated support contacts, sponsor changes or silence, negative reviews, declined advocacy requests. Route each to customer-specific fixes (CS/support), systemic fixes (product, operations, policy) or Escalations.

### Step 5: Act and Close the Loop

- **Inner loop** — contact the customer quickly (especially detractors), agree what will happen, follow up when done.
- **Outer loop** — review themes monthly or quarterly with product, CS, support and sales; assign owners; tell customers what changed ("you told us…, we did…"). Feed systemic themes to Market Problems (`pragmatic-market-problems`, Market) and Requirements (`pragmatic-requirements`, Planning).

Measure loop closure itself: % detractors contacted on time, % themes with an owner, time from theme to fix.

### Step 6: Build the Advocate and Reference Program (signals of satisfaction)

Once you know who is satisfied, invite them to speak for you. Load `references/advocacy-program-guide.md`.

- **Identify** — high CSAT/NPS and green health scores, recent successful go-lives or renewals, expansions, active community members, positive CSM feedback.
- **Recruit** — personal, specific, reciprocal asks that start small (a quote or review) and build up the advocacy ladder (testimonial → case study → reference calls → speaking → advisory board).
- **Operate** — request workflow, advocate database, consent and approvals, utilization caps to prevent burnout.
- **Hand off** — case studies are written in Assets (`pragmatic-assets`); event speakers in Awareness (`pragmatic-awareness`); value evidence in Customer Value Realization.
- **Watch the signal** — a declined request or a cooling advocate is satisfaction data; route it to Step 4.

Track with `templates/advocacy-scorecard-template.md`, reported alongside — never instead of — core satisfaction measures.

## Internal products

For internal platforms, the customers are the teams that use the platform. Measure their satisfaction with the platform and with the platform team (responsiveness, transparency, trust), using short internal surveys, effort scores after requests, and regular conversations with team leads. Internal users often can't switch, so low scores may not show up as churn; treat them as seriously as an external renewal risk, because they show up as workarounds and shadow tools.

## Output Formats

1. **Customer Satisfaction Program Plan** — `templates/satisfaction-program-plan.md`
2. **Satisfaction review** — trends, themes, issues and actions for a quarterly meeting
3. **Relationship health score definition** — inputs, weights, thresholds, actions
4. **Advocate and reference program plan and scorecard** — `templates/advocacy-scorecard-template.md`

## Common Pitfalls

1. **Treating NPS or references as the definition of satisfaction.** They're signals. Use several measures and qualitative feedback.
2. **Measuring without acting.** Surveys with no follow-up teach customers not to answer.
3. **Hearing only from champions.** Survey every persona that matters at renewal, including unhappy ones.
4. **Confusing satisfaction with value realized.** Check outcomes separately in Customer Value Realization.
5. **Account averages that hide people.** One unhappy executive sponsor can outweigh many happy users.
6. **No route for systemic issues.** If themes never reach product, operations or policy owners, the same problems repeat.
7. **Over-asking advocates.** Burnout turns your best customers into detractors.
8. **Ignoring declined advocacy requests.** They often reveal satisfaction problems early.

## Using AI in this focus area

- Code and cluster open-text survey answers, support tickets and reviews into themes by persona and segment.
- Summarize account history before detractor follow-up calls; draft "you said, we did" updates.
- Test which health-score inputs actually predict churn or expansion, and flag accounts whose signals are shifting.
- Rules: check AI output against real market evidence — theme summaries are a starting point, so read the verbatims and talk to customers (NIHITO still applies). Keep customer names, account data and survey responses out of tools not approved for them. The team, not the tool, owns the decisions. AI sentiment scoring misreads sarcasm, polite B2B language and non-English feedback; spot-check it.

## Reference Files

| File | Use |
|---|---|
| `references/satisfaction-measurement-guide.md` | Measures (CSAT, NPS, CES, health, trust, qualitative), survey design, issue triage, closing the loop |
| `references/advocacy-program-guide.md` | Advocate identification, recruitment, advocacy ladder, reference operations, relationship management |
| `templates/satisfaction-program-plan.md` | Satisfaction program plan |
| `templates/advocacy-scorecard-template.md` | Advocate and reference program scorecard |
