---
name: pragmatic-scaling
description: >
  Guides the Scaling focus area of the 2027 Pragmatic Framework (Operations): finding what
  will break as adoption, complexity or demand grows, and expanding the product's reach,
  reliability and efficiency before customers feel the strain. Covers inventorying manual
  and heroic processes, stress-testing at 2x/5x/10x demand, deciding what to standardize,
  automate or build into the product, and planning capacity ahead of demand. Use whenever
  the user mentions scaling a product, product operations, growing pains, operational
  scalability, manual work, toil, onboarding bottlenecks, support volume growing faster than
  customers, capacity planning, cost to serve, unit economics of delivery, standardizing
  processes, moving upmarket or into new regions, reliability as usage grows, or "what
  worked for the first customers doesn't work now." Also trigger for a scaling readiness
  assessment. Links to the Pragmatic Institute Product Operations course.
---

# Scaling — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Operations — *Is the product delivering value as it grows?*
- **Focus-area question:** *What will break as demand grows?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Exceptions, Escalations, Customer Value Realization
- **Pragmatic course:** Product Operations

## What Scaling covers

Scaling is about extending the product's reach, reliability and efficiency as adoption, complexity or demand increases. Processes, configurations and support models that worked for the first customers often stop working at higher volume. Someone hand-builds every onboarding, one engineer knows how to run the billing fix, a sales engineer customizes every demo environment. These are fine at 20 customers and painful at 500.

The 2027 Framework asks teams to watch for work that depends on manual effort, decide what to standardize, find product changes that would remove recurring work, and plan capacity before demand arrives so that growth doesn't come at the customer's expense.

Scaling is not only an infrastructure question. It spans the product itself (performance, configuration, self-service), the operating processes around it (provisioning, onboarding, support, billing, data migration), the people (specialist knowledge, team capacity) and the commercial model (cost to serve versus price).

**Internal products and platforms.** Demand grows when more teams, business units or regions are onboarded. Breakpoints are usually support load on a small platform team, bespoke integrations per team, and governance (access, data ownership) that was handled informally.

## How Scaling connects to the rest of the Framework

**Feeds Scaling:**
- `pragmatic-adoption` (Enablement) and `pragmatic-growth` (Go-to-Market) — the demand forecast: how many customers, users, transactions and segments are coming.
- `pragmatic-product-roadmap` (Focus) — planned launches, new segments and regions that change load and complexity.
- `pragmatic-exceptions` (Operations) — recurring one-offs are often manual work that should be standardized or productized.
- `pragmatic-escalations` (Operations) — incidents under load reveal breakpoints.
- `pragmatic-measurement` (Business) — operational indicators such as cost to serve, time to onboard, tickets per account.

**Scaling feeds:**
- `pragmatic-requirements` (Planning) — product changes that remove recurring work (self-service, configuration, automation, reliability).
- `pragmatic-product-roadmap` (Focus) — scaling investments compete for roadmap capacity; make the case with evidence.
- `pragmatic-business-outcomes` (Business) and `pragmatic-pricing` (Business) — cost to serve and margin as volume grows.
- `pragmatic-organizational-alignment` (Go-to-Market) — standardized processes and hand-offs across sales, CS, support and operations.
- `pragmatic-channel-support` (Enablement) — partners can extend reach and delivery capacity.
- `pragmatic-customer-value-realization` (Operations) — the test that growth hasn't degraded customer outcomes.

## Workflow

Ask questions in small groups. Expect the user to know some answers and need to find others.

### Step 1: Frame the growth scenario

Ask:
1. What growth is expected over the next 12–24 months? (customers, users, transactions, data volume, regions, segments, product lines)
2. What is changing in *complexity*, not only volume? (larger customers, regulated industries, new integrations, more configurations)
3. Where do customers or teams already feel strain? (wait times, errors, slow onboarding, outages)
4. What does the business expect of efficiency? (margin targets, headcount plans, cost to serve)

Turn this into explicit scenarios: today, 2x, 5x and 10x on the relevant demand drivers. Not every driver grows evenly; a move upmarket may halve account count growth but triple configuration complexity.

### Step 2: Map the value-delivery chain

List every step needed to get a customer from signed to successful and keep them there: provisioning, configuration, data migration, integration, onboarding and training, support, billing and renewals, upgrades, reporting, compliance reviews. For internal products: access requests, team onboarding, integrations, support.

For each step capture who does it, how long it takes per customer, and how much is manual.

### Step 3: Inventory manual and fragile work

Use the manual-work inventory in `templates/scaling-readiness-assessment-template.md`. Look for:
- Work done by hand per customer, per user or per transaction (volume-linked effort)
- Work that relies on one or two people (key-person risk)
- Spreadsheets, scripts or tribal knowledge holding a process together
- Repeated "special" handling that is really standard (check the exception log from `pragmatic-exceptions`)
- Support tickets that are really product or documentation gaps

Ask: "If we signed twice as many customers next month, which team would break first?" and "What do you do every week that you wish the product did?"

Other useful questions for frontline teams:
- "Which tasks can only one person do, and what happens when they're on vacation?"
- "Which customer requests do you handle the same way every time, but by hand?"
- "Where do customers wait on us today, and for how long?"

### Step 4: Find the breakpoints

For each process, product component and team, estimate at what demand level it breaks: capacity runs out, quality drops, cost per customer becomes unacceptable, or response times exceed commitments. Read `references/scaling-guide.md` for capacity math, leading indicators and common breakpoints.

Rate each breakpoint by when it will be hit (from the forecast) and the customer impact if it is.

### Step 5: Decide: standardize, automate or productize

For each item on the inventory decide:
- **Standardize** — one documented way to do it, with templates and defined options. Cheapest; do first when variation is the problem.
- **Automate** — internal tooling or scripts that remove effort without changing the customer experience.
- **Productize** — change the product so the work disappears or the customer can do it themselves (self-service setup, configuration options, bulk import, better defaults). Send these to `pragmatic-requirements`.
- **Staff or partner** — add capacity deliberately (hire, train, use partners) where the work must stay human.
- **Accept or stop** — some work isn't worth scaling; consider dropping a variant or segment (raise with `pragmatic-product-strategy`).

Standardize before you automate: automating a messy process makes the mess faster.

### Step 6: Plan capacity ahead of demand

Build a capacity plan with lead times. Hiring and training take months; infrastructure and vendor changes can take quarters; product changes take at least a roadmap cycle. Work back from when each breakpoint will be hit to when action must start. Define leading indicators and thresholds that trigger the next step.

### Step 7: Make the case and track

Present the scaling plan as customer and business impact: risk avoided, cost to serve, time to onboard, margin. Get scaling items onto the roadmap with evidence (`pragmatic-product-roadmap`, `pragmatic-stakeholder-management`). Review quarterly against the forecast and actual growth.

## Worked example

A B2B analytics product has 120 customers and expects 300 within 18 months, with a push into enterprise accounts.

- **Inventory:** every onboarding includes a hand-built data mapping (14 hours per customer, done by two implementation specialists); SSO is configured manually by one engineer; enterprise security questionnaires are answered from scratch by sales engineers.
- **Breakpoints:** implementation capacity is about 15 new customers a month; bookings forecast says 18 a month from Q3. SSO setup depends on one person (key-person risk now). Questionnaire load doubles with the enterprise push.
- **Decisions:** standardize data mapping with templates for the five most common source systems (cuts effort to ~5 hours); productize self-service SSO configuration (to `pragmatic-requirements`); build a maintained security answer library (to `pragmatic-assets`); hire one implementation specialist now, given a four-month hire-and-ramp lead time.
- **Triggers:** onboarding backlog over three weeks, or time from contract to go-live over 45 days, escalates the next hire.

The result goes to the roadmap review with the cost of doing nothing: delayed go-lives for roughly 40 customers and lower activation (see `pragmatic-adoption`).

## Output formats

- **Scaling readiness assessment** — manual-work inventory, breakpoints at 2x/5x/10x, decisions (`templates/scaling-readiness-assessment-template.md`).
- **Capacity plan** — demand forecast, capacity per team/component, lead times, trigger thresholds.
- **Productization proposal** — recurring work to remove through product changes, with effort saved and requirements hand-off.
- **Cost-to-serve analysis** — effort and cost per customer by segment, and how it changes with scale.

## Common pitfalls

- **Treating scaling as only an engineering problem.** Onboarding, support, billing and specialist knowledge break as often as servers do.
- **Waiting for the breakage.** By the time customers feel it, the fix is months away.
- **Automating before standardizing.** Ten variations automated are ten things to maintain.
- **Heroics as a process.** A person who always saves the day is a single point of failure, not a scaling plan.
- **Scaling every variant.** Some customizations and segments shouldn't be carried forward; decide deliberately.
- **Ignoring cost to serve.** Revenue can grow while margin shrinks if delivery effort grows linearly with customers.
- **No roadmap capacity for scaling work.** Without evidence of impact, scaling items lose to features every time.

## Using AI in this focus area

- Analyze ticket, onboarding and time-tracking data to find volume-linked manual work and recurring requests.
- Draft standard operating procedures and runbooks from notes and recordings of how experts do the work today.
- Build first-pass capacity models and scenario tables for the team to check.
- Rules: check AI findings against the people doing the work and against customer impact (talk to the market and to frontline teams; NIHITO still applies); keep customer data, contracts and internal cost data out of tools not approved for it; the team, not the tool, owns the decisions. AI-generated forecasts are only as good as the assumptions you feed them; make the assumptions explicit.

## Reference files

- `references/scaling-guide.md` — scaling dimensions, capacity math, leading indicators, common breakpoints by function, standardize/automate/productize criteria, internal-platform notes. Read before Steps 4–6.
- `templates/scaling-readiness-assessment-template.md` — the assessment template. Read when producing an assessment.
