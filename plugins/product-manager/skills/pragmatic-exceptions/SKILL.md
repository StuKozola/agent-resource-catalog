---
name: pragmatic-exceptions
description: >
  Guides the Exceptions focus area of the 2027 Pragmatic Framework (Operations): deciding
  which one-offs are worth making and which point to a missing capability. Covers
  non-standard requests, edge cases, policy exceptions, custom work, special pricing or
  contract terms, custom features for a single deal, workarounds and "just this once"
  favors; setting approval owners and decision criteria; logging every exception; and
  reviewing patterns so repeated exceptions become evidence for market problems and
  requirements. Use whenever the user mentions exception requests, custom development for a
  customer, one-off requests, special deals, non-standard terms, policy waivers, deal desk
  rules, feature requests tied to a single deal, customization creep, snowflake customers,
  bespoke configurations, or "sales keeps promising things the product doesn't do." Also
  trigger for an exception policy, exception approval process, exception log or pattern
  review.
---

# Exceptions — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Operations — *Is the product delivering value as it grows?*
- **Focus-area question:** *Which one-offs are worth making, and which point to a missing capability?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Scaling, Escalations, Customer Value Realization

## What Exceptions covers

Once a product is in the market, requests arrive that don't fit the standard offer: a customer needs an edge case handled, a deal needs a policy waived, a key account wants custom work. Handled well, exceptions keep customers successful without eroding strategy, consistency or margin. Handled badly, they become a hidden second product nobody planned, supported by heroics.

The 2027 Framework asks teams to decide who approves exceptions and on what criteria, and to track every one. The key idea: an exception that keeps coming back is not an exception. It is evidence of a market problem the product doesn't yet solve, and it belongs in Market Problems and Requirements.

**Types of exceptions** (use these to classify):
- **Product** — custom features, configurations, integrations, or workarounds for one customer
- **Commercial** — non-standard pricing, discounts, payment terms, packaging, licensing
- **Contractual / policy** — SLA changes, liability, data residency, security terms, refund or return policy waivers
- **Service** — extra onboarding, dedicated support, custom reports, manual processing
- **Edge cases** — legitimate situations the product didn't anticipate (data shapes, workflows, regulations)

**Internal products.** Exceptions show up as one team's special workflow, a bypass of platform standards, or a custom integration. The same discipline applies: approve deliberately, log, and look for patterns that should become platform capabilities.

## How Exceptions connects to the rest of the Framework

**Feeds Exceptions:**
- `pragmatic-product-strategy` (Market) — what the product will be known for and what it says no to; the first test of any exception.
- `pragmatic-pricing` (Business) — the standard price and packaging that commercial exceptions deviate from.
- `pragmatic-market-definition` (Focus) — whether the requester is in the target segment.
- `pragmatic-adoption` (Enablement) — unanticipated uses often surface as exception requests.

**Exceptions feeds:**
- `pragmatic-market-problems` (Market) — recurring exceptions are market-problem evidence. This is part of the loop from Operations back to Market.
- `pragmatic-requirements` (Planning) — patterns that justify a product capability, with frequency and affected personas.
- `pragmatic-product-roadmap` (Focus) — patterns that compete for roadmap capacity.
- `pragmatic-scaling` (Operations) — custom work is manual work; it must be counted in capacity and cost to serve.
- `pragmatic-pricing` and `pragmatic-business-outcomes` (Business) — discount and custom-work patterns affect margin and price realization.
- `pragmatic-organizational-alignment` (Go-to-Market) — sales, CS and support need the same rules about what can be offered.
- `pragmatic-escalations` (Operations) — some escalations are resolved by granting an exception; log it in both places.

## Workflow

### Step 1: Understand the current state

Ask the user:
1. What kinds of exceptions come up most? Can you give three recent examples?
2. Who asks for them (sales, CS, customers directly, executives) and who decides today?
3. Is there any record of exceptions granted? Where (CRM, contracts, tickets, Slack)?
4. What has gone wrong with past exceptions? (custom code nobody maintains, discount precedents, support confusion)
5. What does the product strategy say the product will *not* do?

If no record exists, the first deliverable is usually a lightweight log and a backfill of the last 6–12 months from contracts, deal desk notes and engineering tickets.

### Step 2: Define the approval model

Decide, by exception type and size, who approves. Principles:
- Approval sits with the person accountable for the consequence (product for product changes, finance/deal desk for commercial terms, legal for contract terms, support/ops leadership for service commitments).
- Set thresholds: small, reversible exceptions can be approved by a team lead; large, permanent or precedent-setting ones need product leadership and possibly an exception review board.
- Define a turnaround time so the process doesn't become a reason to lose deals.
- No verbal approvals. If it isn't logged, it isn't approved.

### Step 3: Set the decision criteria

Use `templates/exception-request-template.md`. Core questions for every request:
1. **Strategy fit** — Does this move toward or away from the product strategy? Is the requester in the target segment?
2. **Problem** — What problem is the customer actually trying to solve? (Ask why until you reach the problem, not the requested solution.)
3. **Frequency** — Have we seen this before? How many others likely have it?
4. **Cost** — One-time and ongoing cost: build, support, maintenance, testing burden, operational effort, margin.
5. **Value** — Revenue, retention, strategic account, reference value, learning value.
6. **Precedent and reversibility** — Will others expect the same? Can we undo it? Does it fork the product?
7. **Alternatives** — Can the standard product, a configuration, a partner or a documented workaround meet the need?

Possible decisions: **approve as one-off** (with expiry or review date), **approve as pilot** (explicitly testing a possible capability), **decline with alternative**, **decline**, or **route to product** (it's a capability gap, not an exception).

Read `references/exceptions-guide.md` for scoring, thresholds and how to say no well.

### Step 4: Log every exception

Use `templates/exception-log-template.md`. Log approved *and* declined requests; declined ones are market evidence too. Capture the underlying problem in the customer's words, not just the requested solution, and tag it so patterns can be found.

### Step 5: Review patterns on a cadence

Monthly or quarterly, review the log:
- Group by underlying problem, not by requested solution.
- Count requests, accounts, revenue affected, and cost of exceptions granted.
- Flag any problem seen in 3+ accounts (or your chosen threshold) as a **pattern**.
- For each pattern, decide: productize (send to `pragmatic-requirements` with the evidence), update policy or packaging (`pragmatic-pricing`), standardize as a service offering, or keep declining (confirm with `pragmatic-product-strategy`).
- Record each pattern as market-problem evidence in `pragmatic-market-problems`, then validate it with customers who did *not* ask; requesters are not a representative sample.

### Step 6: Manage the exceptions you granted

Track ongoing cost and ownership of granted exceptions. Set review or sunset dates. When a capability ships that replaces a custom solution, migrate those customers to the standard product.

## Worked example

A sales rep asks engineering to add a custom CSV export for a large prospect, due before contract signature.

- **Problem behind the request:** the prospect's finance team reconciles product data with their ERP every month by hand. The CSV is their proposed solution.
- **Log search:** four similar requests in nine months, all from mid-market and enterprise finance teams, two declined, two built as one-off scripts that support now maintains.
- **Decision:** approve a time-boxed one-off using the existing scripts (owner: CS, review in six months) so the deal isn't blocked, and route the pattern to product.
- **Pattern review:** problem statement "finance teams need monthly reconciliation with their ERP" goes to `pragmatic-market-problems` with five accounts of evidence. Product validates it with finance users at customers who never asked, then writes a requirement for a standard ERP export (`pragmatic-requirements`). When it ships, the two custom scripts are retired and those customers migrated.

## Output formats

- **Exception policy** — types, approval matrix, thresholds, turnaround times, criteria.
- **Exception request and decision record** — one per request (`templates/exception-request-template.md`).
- **Exception log** — running register with tags (`templates/exception-log-template.md`).
- **Pattern review** — periodic summary of patterns, costs and routed decisions (in the log template).
- **Requirements hand-off** — problem statement, frequency, affected personas and accounts for `pragmatic-requirements`.

## Common pitfalls

- **Logging the solution, not the problem.** "Wants a CSV export" hides "needs to reconcile with their ERP monthly." Patterns live in the problems.
- **Only logging approvals.** Declined requests are equally useful market evidence.
- **Approval by escalation volume.** The loudest account or the largest deal sets precedent by default. Use criteria.
- **Permanent one-offs.** Custom work without an owner or sunset date becomes unmaintained product.
- **Treating requesters as the market.** A pattern from existing customers still needs validation with the broader segment (NIHITO).
- **A process too slow to use.** If approval takes weeks, people route around it.
- **No connection to cost.** Count support, maintenance and margin impact, or exceptions look free.

## Using AI in this focus area

- Extract and classify exception requests from contracts, CRM notes, tickets and chat threads to backfill a log.
- Cluster logged requests by underlying problem to surface patterns and count affected accounts.
- Draft decision records and requirements hand-offs from the log for the team to review.
- Rules: check AI-identified patterns against the customers themselves before treating them as market problems (NIHITO still applies); keep contracts, deal terms and customer data out of tools not approved for them; the team, not the tool, owns approval decisions. AI clustering tends to group by the words in the request, which often reflect the requested solution; review clusters for the real problem.

## Reference files

- `references/exceptions-guide.md` — exception types, approval matrix, scoring, pattern thresholds, saying no well, handling custom work, internal-product notes. Read before designing a policy or reviewing patterns.
- `templates/exception-request-template.md` — request and decision criteria template. Read when evaluating a request or writing a policy.
- `templates/exception-log-template.md` — exception log and pattern review template. Read when setting up tracking or running a review.
