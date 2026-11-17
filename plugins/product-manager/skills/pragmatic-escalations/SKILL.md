---
name: pragmatic-escalations
description: >
  Guides the Escalations focus area of the 2027 Pragmatic Framework (Operations): making sure
  every critical issue has a clear owner and response path, and that the team learns from
  it. Covers critical customer issues, product incidents, risks and stakeholder concerns that
  need fast, coordinated action; severity levels; owners and roles; response and handoff
  paths; communication with customers and leaders; and post-escalation reviews that feed
  requirements, the roadmap and operations. Use whenever the user mentions escalations,
  escalation path, critical customer issue, executive escalation, P1/Sev1, incident management, incident commander, customer at risk, war room, status page,
  customer communication during an outage, post-mortem, post-incident review, root cause
  analysis, RCA, blameless review, or "who owns this?" Also trigger for a severity matrix,
  escalation runbook or post-escalation review. Explains product management's role versus
  support, customer success and engineering.
---

# Escalations — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Operations — *Is the product delivering value as it grows?*
- **Focus-area question:** *Who owns a critical issue, and what do we learn from it?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Scaling, Exceptions, Customer Value Realization

## What Escalations covers

Escalations are the critical issues, risks and stakeholder concerns that need fast, coordinated action: a major outage, a data problem at a key account, a security concern, a strategic customer threatening to leave, an executive demanding answers. What keeps them from turning into crises is clear ownership and a known response path.

The 2027 Framework asks teams to define severity levels, owners, and how they'll communicate with customers and leaders, and then, after each escalation, to capture what they learned and feed it into requirements, the roadmap and operations. The second half is what most organizations skip.

**Kinds of escalations:**
- **Technical incidents** — outages, degraded performance, data loss or corruption, security events
- **Customer escalations** — a key account's unresolved problem, failed implementation, threat to churn
- **Commercial or contractual** — SLA breaches, disputes, commitments made that can't be met
- **Stakeholder concerns** — executives, partners, regulators or the board raising a risk that needs a coordinated answer

## Product's role in escalations

Product management rarely runs the incident response; support, customer success and engineering usually do. Product's distinct responsibilities are to:
- Help set severity definitions based on customer impact, not internal convenience.
- Supply product and market context during the response: which customers and personas are affected, what the workaround is, what was promised.
- Make or broker product trade-off decisions (hotfix scope, feature flag, rollback, temporary exception).
- Join customer and executive communication when the issue is about product direction or a capability gap.
- Own the *learning* loop: turn findings into requirements, roadmap items and operational changes, and close the loop with customers.

Use the RACI in `references/escalation-management-guide.md` to make this explicit for your organization.

**Internal products and platforms.** The "customers" are internal teams; escalations often arrive through leaders rather than tickets. Define severity by business impact (revenue processes blocked, regulatory deadlines), and publish the path so teams don't escalate through personal networks.

## How Escalations connects to the rest of the Framework

**Feeds Escalations:**
- `pragmatic-stakeholder-management` (Planning) — who must be informed and who decides; escalation paths should match.
- `pragmatic-organizational-alignment` (Go-to-Market) — shared hand-offs among sales, CS, support, operations and product.
- `pragmatic-customer-satisfaction` (Go-to-Market) — relationship health signals that predict customer escalations.
- `pragmatic-scaling` (Operations) — breakpoints that, if missed, show up as incidents.

**Escalations feeds:**
- `pragmatic-requirements` (Planning) — gaps, reliability needs and edge cases found in reviews.
- `pragmatic-product-roadmap` (Focus) — fixes and preventive work that need roadmap capacity.
- `pragmatic-scaling` (Operations) — operational changes: monitoring, runbooks, capacity, staffing.
- `pragmatic-exceptions` (Operations) — escalations resolved by an exception get logged there too.
- `pragmatic-market-problems` (Market) — recurring escalation themes are market-problem evidence; part of the loop back to Market.
- `pragmatic-retention` (Go-to-Market) and `pragmatic-customer-value-realization` (Operations) — the account recovery plan after a serious escalation.
- `pragmatic-assets` (Enablement) — communication templates and talk tracks for customer-facing teams.

## Workflow

### Step 1: Assess the current state

Ask the user:
1. What were the last three serious escalations? How did they start, who handled them, how long did they take?
2. Is there a written severity scale? Do support, engineering, CS and sales use the same one?
3. Who can declare an escalation, and how? Where is it coordinated?
4. How are customers and executives updated today?
5. Are post-escalation reviews done? What happened to the action items?

Look for gaps: unclear ownership, severity inflation ("everything is P1"), executives pulled in through side channels, reviews that produce documents but no changes.

### Step 2: Define severity levels

Define 3–5 levels using customer and business impact: scope (how many customers, which segments), severity of harm (data, money, safety, compliance), availability of a workaround, and strategic risk. Attach to each level the response time, update cadence, who's engaged and who's notified. Use the matrix in `templates/severity-matrix-and-runbook-template.md`. Allow severity to be raised or lowered as facts emerge.

### Step 3: Assign owners and roles

For each escalation, one person is accountable for coordination (incident commander or escalation owner), separate from the people fixing the problem. Common roles: escalation owner, technical lead, communications lead, customer owner (account or CS lead), product lead, executive sponsor for the highest severities. Make on-call and backup coverage explicit.

### Step 4: Define response paths

Write the runbook: how an issue is raised, triaged, declared, worked, communicated, resolved and handed to review. Include where coordination happens (channel, bridge), decision rights (who can approve a rollback, a hotfix, a credit, an exception) and handoffs between support tiers, engineering and CS. Keep it short enough to use under pressure.

### Step 5: Plan communication

Define, per severity:
- **Customers** — who tells them, through what channel (status page, email, account team call), how often, and what each update must contain (what's affected, what we're doing, workaround, next update time).
- **Leaders** — who briefs whom, when, and in what format (short written summary beats a meeting).
- **Internal teams** — sales and CS need talk tracks before customers call them.

Read `references/escalation-management-guide.md` for update templates and communication principles.

### Step 6: Review and learn after each escalation

Run a blameless post-escalation review using `templates/post-escalation-review-template.md`. Focus on what happened, why the system allowed it, what went well, and what to change. Every action item gets an owner, a due date and a destination:
- Product changes → `pragmatic-requirements` and `pragmatic-product-roadmap`
- Operational changes (monitoring, runbooks, capacity, staffing, process) → operations owners and `pragmatic-scaling`
- Communication and enablement changes → `pragmatic-assets`, `pragmatic-organizational-alignment`
- Customer recovery → account plan with CS (`pragmatic-retention`)

Close the loop with affected customers: tell them what you learned and what's changing.

### Step 7: Review trends

Quarterly, review escalations as a set: volume by severity, time to resolve, repeat causes, affected segments, action-item completion. Recurring themes are evidence of unsolved problems; log them in `pragmatic-market-problems` and bring them to roadmap discussions.

## Worked example

A scheduled data sync fails silently for eight days at three customers, including one strategic account in renewal.

- **Declare:** the CSM for the strategic account notices missing data and raises it. The escalation owner sets Sev 2 (multiple accounts, data impact, workaround exists via manual re-sync), upgrading to Sev 1 an hour later when the renewal risk is confirmed.
- **Respond:** engineering re-syncs and patches; the product lead confirms which reports were affected and decides to add a visible sync-status warning as part of the hotfix; the CSM and an executive sponsor call the strategic account; the communications lead sends updates every two hours.
- **Review:** the blameless review finds three contributing factors: no alerting on sync failure, no customer-visible sync status, and a support macro that told customers to "wait 24 hours."
- **Route:** sync monitoring to operations (`pragmatic-scaling`); customer-visible sync status and failure notifications to `pragmatic-requirements`; updated support macro to `pragmatic-assets`; a recovery plan for the strategic account to `pragmatic-retention`. Product writes to all three customers explaining what changed.

## Output formats

- **Severity matrix** and **escalation runbook** (`templates/severity-matrix-and-runbook-template.md`).
- **RACI for escalations** across support, CS, engineering, product, sales and leadership.
- **Communication templates** — customer updates, executive summary, internal talk track.
- **Post-escalation review** (`templates/post-escalation-review-template.md`).
- **Quarterly escalation trend report** — themes, action-item status, routed product and operations changes.

## Common pitfalls

- **Severity by volume of complaint.** The loudest executive gets Sev1. Define severity by impact.
- **No single owner.** Many people working, nobody coordinating; customers get conflicting updates.
- **Fixers doing the comms.** The person debugging shouldn't also be writing executive updates.
- **Silence.** Customers tolerate problems better than uncertainty. Commit to an update time and keep it.
- **Blame-focused reviews.** People hide information next time. Look at systems and decisions, not culprits.
- **Reviews without follow-through.** Action items that never reach the roadmap guarantee repeat escalations.
- **Product absent until the review.** Product context early prevents wrong trade-offs during the response.
- **Treating each escalation as unique.** Trends are where the market evidence is.

## Using AI in this focus area

- Summarize long incident channels and ticket histories into timelines and draft executive and customer updates for human review.
- Search past escalations and reviews for similar incidents, known workarounds and repeat causes.
- Cluster review findings across quarters to surface recurring themes for the roadmap.
- Rules: verify AI summaries against the actual timeline and talk to affected customers before drawing conclusions (NIHITO still applies); keep customer data, security details and incident specifics out of tools not approved for them; the team, not the tool, owns severity calls and customer commitments. Never send AI-drafted customer communication during an incident without a named person checking every fact.

## Reference files

- `references/escalation-management-guide.md` — severity design, roles and RACI, product's role, communication principles and update templates, blameless review method, trend analysis, internal-product notes. Read before Steps 2–6.
- `templates/severity-matrix-and-runbook-template.md` — severity matrix and escalation runbook template. Read when defining severity or response paths.
- `templates/post-escalation-review-template.md` — post-escalation review template. Read when running a review.
