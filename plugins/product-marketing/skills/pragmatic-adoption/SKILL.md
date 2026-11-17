---
name: pragmatic-adoption
description: >
  Guides the Adoption focus area of the 2027 Pragmatic Framework (Enablement): making sure
  customers and end users start using the product in meaningful ways and keep using it.
  Covers planning adoption before launch, defining meaningful use (activation event, core
  action, habit), deciding who needs onboarding and training, tracking continued use with
  cohorts and breadth/depth/frequency, spotting unanticipated uses, and diagnosing low
  adoption. Use whenever the user mentions product adoption, user adoption, onboarding,
  activation rate, time to value, aha moment, feature adoption, usage analytics,
  DAU/MAU, stickiness, engagement cohorts, training plans, change management for a rollout,
  internal tool or platform adoption, shelfware, or "people bought it but aren't using it."
  Also trigger for an adoption plan, adoption metrics definition, or onboarding design.
  Not for acquiring new customers (pragmatic-growth) or renewal/churn programs
  (pragmatic-retention), though it feeds both.
---

# Adoption — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Enablement — *Can the people around the product make it succeed?*
- **Focus-area question:** *Do customers and users start using the product in meaningful ways, and do they keep using it?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Content, Assets, Channel Support

## What Adoption covers

Adoption is the onboarding, activation and behavior change that gets customers and end users to begin real use of a product and stay with it. The premise is simple: a product creates value only when people use it. A signed contract, an install or a login is not adoption.

The 2027 Framework asks teams to plan adoption before launch, not after usage disappoints. That means deciding what meaningful use looks like, who needs onboarding or training, and how continued use will be tracked. It also asks teams to watch for uses they didn't anticipate, because those can reveal new value or new problems. When adoption is low, the response is to revisit requirements, onboarding or positioning rather than to push harder on the same plan.

**Internal products and platforms.** For internal tools, adoption across the organization often *is* the success measure. The "customers" are teams and employees, the "purchase" is a mandate or a choice to switch from a workaround, and the competition is usually the spreadsheet or legacy process people already know. The same workflow applies; pay extra attention to change management, manager sponsorship and removing the old path.

## How Adoption connects to the rest of the Framework

**Feeds Adoption:**
- `pragmatic-user-personas` (Planning) — who uses the product, their workflows, skills and context; the basis for onboarding by persona.
- `pragmatic-requirements` (Planning) — the problems the product must solve; meaningful use should map to solving them.
- `pragmatic-market-problems` (Market) — the outcome customers want, which defines what "meaningful" means.
- `pragmatic-positioning` (Planning) — sets expectations; a mismatch between promise and experience shows up as early drop-off.
- `pragmatic-measurement` (Business) — the indicator framework adoption metrics plug into.
- `pragmatic-launch` (Go-to-Market) — adoption readiness is part of launch readiness.

**Adoption feeds:**
- `pragmatic-retention` (Go-to-Market) — early usage is the strongest leading indicator of renewal and expansion.
- `pragmatic-customer-value-realization` (Operations) — customers can't realize outcomes from a product they don't use.
- `pragmatic-content` and `pragmatic-assets` (Enablement) — onboarding guides, tutorials, in-product help, training decks.
- `pragmatic-channel-support` (Enablement) — partners who deliver or service the product need the adoption playbook too.
- `pragmatic-growth` (Go-to-Market) — trial-to-paid conversion and expanded use; for internal products, org-wide adoption is growth.
- `pragmatic-scaling` (Operations) — rising adoption is often what exposes manual onboarding work that won't scale.

## Workflow

Adapt depth to the situation: a new product before launch, a live product with disappointing usage, or an internal rollout. Ask questions one group at a time; don't dump the whole list.

### Step 1: Establish context

Ask the user:
1. Is this pre-launch, recently launched, or a mature product with an adoption problem?
2. Commercial or internal product? Self-serve, sales-led, or mandated rollout?
3. Who buys versus who uses? (Buyers sign; users decide whether value happens.)
4. What problem did customers buy this to solve, and what outcome do they expect?
5. What usage data exists today (product analytics, logs, license utilization, support tickets)?

### Step 2: Define meaningful use

This is the most important step and the one most teams skip. Work with the user to define, per user persona:

- **Activation event** — the first action that shows a user has experienced the core value (e.g., "first report shared with a colleague," not "account created").
- **Core action** — the repeated action that delivers the product's value.
- **Habit / expected frequency** — how often a healthy user should perform the core action given the real-world rhythm of the problem (daily, weekly, monthly, per project). Don't impose daily-use targets on a monthly problem.
- **Breadth and depth** — how many of the intended users at an account are active (breadth) and how much of the relevant capability they use (depth).

Ask: "If a customer did only one thing in the product each week and got value, what would it be?" and "What would you see in the data that tells you an account is in trouble?" Validate the activation definition against retained versus churned accounts if data exists. Read `references/adoption-measurement-guide.md` for metric definitions and how to pick activation thresholds.

### Step 3: Identify who needs onboarding and training

Map the people involved, not just "the user":
- End users by persona (power users, occasional users, reluctant users)
- Admins and implementers who configure the product
- Managers and sponsors whose expectations drive behavior change
- Partners or service providers who onboard on your behalf

For each, decide the onboarding mode (self-serve in-product, guided, live training, certification, partner-led) and what they must be able to do by the end of it. Behavior change matters: if the product replaces an existing process, plan for retiring the old one.

### Step 4: Build the adoption plan

Use `templates/adoption-plan-template.md`. Cover:
- Meaningful-use definitions and targets by persona and segment
- Onboarding journey: first session, first week, first 30/60/90 days, with time-to-value targets
- Training and content needs (hand off to `pragmatic-content` and `pragmatic-assets`)
- Owners across product, customer success, support, marketing and partners
- Instrumentation needed before launch (what events must be tracked)
- Intervention triggers: what happens when an account misses activation or usage drops
- Link to the launch plan (`pragmatic-launch`) so adoption readiness is checked before go-live

### Step 5: Track continued use

Define adoption metrics with `templates/adoption-metrics-template.md`. At minimum:
- Activation rate and time to activation
- Cohort retention curves for the core action (does the curve flatten or keep falling?)
- Breadth (active users / licensed or intended users), depth (features or workflows used), frequency
- Feature adoption for capabilities tied to key requirements

Review cohorts on a fixed cadence. Segment by persona, customer size, acquisition channel and onboarding path; averages hide the story.

### Step 6: Watch for unanticipated uses

Ask support, customer success and sales what customers are doing that nobody planned for. Look for odd usage patterns, workarounds, exports to other tools and integration requests. Classify each:
- **New value** — a use case or segment worth investigating; send to `pragmatic-market-problems` and `pragmatic-market-definition`.
- **New problem** — a workaround for a gap, or misuse that will hurt outcomes; send to `pragmatic-requirements`, and to `pragmatic-exceptions` if customers are asking for one-offs to support it.

### Step 7: Diagnose low adoption

When adoption is below target, find where people stop and why. Talk to users who stalled (NIHITO applies). Then route the fix:
- **Requirements** — the product doesn't solve the problem well enough, or is too hard to use → `pragmatic-requirements`
- **Onboarding** — users never reach value, or the path is unclear → revise the onboarding plan
- **Positioning** — the wrong customers bought, or expected something else → `pragmatic-positioning`, `pragmatic-market-definition`
- **Organizational** — no sponsor, no time, the old process still exists → change management with the customer

## Worked example

A team-collaboration product sees 85% of new accounts log in during the first week, but only 30% are still active at day 60.

- **Meaningful use:** the team had been counting logins. Retention analysis shows accounts that create a shared project and invite at least three colleagues in the first 14 days retain at nearly three times the rate of those that don't. That becomes the activation event; the core action is weekly project updates.
- **Diagnosis:** only 35% of accounts reach activation. Interviews with stalled admins show they set up a project alone and never invite their team because inviting requires IT approval at many customers.
- **Routing:** an invite flow that works with customers' SSO groups goes to `pragmatic-requirements`; onboarding adds a guided "invite your team" step; an IT-approval checklist goes to `pragmatic-assets` for sales to share before the deal closes.
- **Unanticipated use:** several customers use the product for client-facing project portals. That goes to `pragmatic-market-problems` as a possible new use case to validate.

## Output formats

- **Adoption plan** — full plan for a launch or rollout (`templates/adoption-plan-template.md`).
- **Adoption metrics definition** — meaningful-use definitions, metric formulas, targets, data sources (`templates/adoption-metrics-template.md`).
- **Onboarding journey map** — stages, actions, time-to-value targets and owners per persona.
- **Adoption diagnostic** — funnel and cohort findings, root causes, routed recommendations.
- **Unanticipated-use log** — observed uses, classification (value or problem), where each was routed.

## Common pitfalls

- **Counting logins as adoption.** Logins, installs and seats assigned measure access, not value. Tie adoption to the core action.
- **Defining adoption after launch.** If events aren't instrumented before go-live, you'll spend the first quarter guessing.
- **One definition for every persona.** An admin, a daily operator and an executive viewer have different meaningful-use patterns.
- **Optimizing for frequency the problem doesn't have.** Push notifications won't make a quarterly task daily; they'll make users mute you.
- **Training only the champion.** Adoption stalls when the buyer is trained and the end users are not.
- **Leaving the old process running.** People default to the familiar path. Plan its retirement, especially for internal products.
- **Blaming users.** Persistent low adoption is a product, onboarding or positioning signal. Treat it as evidence, not a training problem by default.
- **Ignoring surprising usage.** Unplanned uses are free market research.

## Using AI in this focus area

- Cluster support tickets, onboarding survey answers and session notes to find where users get stuck.
- Draft onboarding emails, in-product guidance and training outlines by persona for the team to edit.
- Scan usage data for drop-off points, cohort differences and unusual usage patterns worth investigating.
- Rules: check AI findings against what users actually tell you (talk to them; NIHITO still applies); keep customer usage data and account details out of tools not approved for it; the team, not the tool, owns the adoption definition and decisions. AI can show *where* people stop, but rarely *why*; that needs conversations.

## Reference files

- `references/adoption-measurement-guide.md` — meaningful-use definitions, metric formulas, activation-threshold method, cohort analysis, diagnosing low adoption, internal-product adoption. Read before defining metrics or diagnosing a problem.
- `templates/adoption-plan-template.md` — adoption plan template. Read when producing a plan.
- `templates/adoption-metrics-template.md` — adoption metrics definition template. Read when defining metrics.
