---
name: pragmatic-customer-value-realization
description: >
  Guides the Customer Value Realization focus area of the 2027 Pragmatic Framework
  (Operations): finding out whether customers achieved the outcome they bought or adopted
  the product for, from the customer's side. Covers agreeing success criteria with
  customers, setting baselines, gathering evidence of results, running value reviews,
  sharing findings with the teams who build, sell and support the product, and feeding
  what's learned back to Market Problems so the cycle continues. Use whenever the user
  mentions value realization, customer outcomes, customer success plans, success criteria,
  mutual success plan, time to value, value reviews, outcome-focused QBRs/EBRs, ROI
  realized by customers, value evidence, or "did customers get what they bought it for?" Also trigger for a customer success plan or value evidence record. Not
  for satisfaction surveys (pragmatic-customer-satisfaction) or company results
  (pragmatic-business-outcomes).
---

# Customer Value Realization — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Operations — *Is the product delivering value as it grows?*
- **Focus-area question:** *Did customers get the outcome they bought the product for?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Scaling, Exceptions, Escalations

## What Customer Value Realization covers

Customer Value Realization (CVR) asks whether customers achieved the outcome they bought or adopted the product for, judged from the customer's side rather than by the vendor's metrics. Usage, renewals and satisfaction scores are all useful, but none of them answers the question directly. A customer can use the product daily, like the team, and still not hit the result that justified the purchase.

The 2027 Framework describes three moves: agree with customers on what success looks like, gather evidence of the results they get, and share that evidence with the teams who build, sell and support the product. CVR is also where the Framework loops: what you learn about customer value becomes the next round of market problems, and the cycle starts again at Market Problems.

**Boundaries:**
- **vs. Customer Satisfaction** (`pragmatic-customer-satisfaction`, Go-to-Market) — satisfaction is the customer's judgment of their experience and relationship with you. CVR is whether they got the outcome. They often move together but can diverge: a happy customer with no measurable result, or an unhappy one who hit every target.
- **vs. Business Outcomes** (`pragmatic-business-outcomes`, Business) — results for *your* organization (revenue, margin, ROI on the product). CVR is results for the *customer*.
- **vs. Measurement** (`pragmatic-measurement`, Business) — Measurement sets the indicators, leading and lagging. CVR uses them, with customer-specific success criteria, to judge outcomes.
- **vs. Adoption** (`pragmatic-adoption`, Enablement) — adoption is meaningful use; it is a precondition for value, not proof of it.

**Internal products and platforms.** The "customer" is the business team that adopted the tool. Success criteria are their outcomes (cycle time, error rate, cost, compliance), agreed with the business owner at rollout and reviewed afterwards.

## How CVR connects to the rest of the Framework

**Feeds CVR:**
- `pragmatic-market-problems` (Market) — the problem and desired outcome that define "value."
- `pragmatic-positioning` (Planning) and `pragmatic-buyer-journey` (Planning) — what customers were promised and why they bought; success criteria should match.
- `pragmatic-measurement` (Business) — the indicator framework and data sources.
- `pragmatic-adoption` (Enablement) — whether customers are using the product enough to get results.
- `pragmatic-escalations` and `pragmatic-exceptions` (Operations) — signals that outcomes are at risk.

**CVR feeds:**
- `pragmatic-market-problems` (Market) — **the loop.** Unmet outcomes, new outcomes customers want, and results that differ by segment become the next round of market problems.
- `pragmatic-requirements` (Planning) and `pragmatic-product-roadmap` (Focus) — gaps between promised and realized outcomes.
- `pragmatic-retention` and `pragmatic-growth` (Go-to-Market) — proven value supports renewal and expansion.
- `pragmatic-assets` (Enablement) — case studies, ROI evidence and proof points (with customer permission).
- `pragmatic-positioning` and `pragmatic-pricing` (Planning, Business) — evidence of what value customers actually get, and how much.
- `pragmatic-business-outcomes` (Business) — customer outcomes often lead company outcomes.
- `pragmatic-win-loss-analysis` (Market) — compare why customers bought with what they got.

## Workflow

### Step 1: Clarify scope and current practice

Ask the user:
1. Which customers or segments are in scope? All accounts, strategic accounts, a new product's early customers?
2. Do you know why each customer bought? Where is that captured (sales notes, business case, mutual action plan)?
3. Does anyone agree success criteria with customers today? Who (sales, CS, implementation, product)?
4. What evidence of customer results exists (case studies, QBR decks, usage data, customer-reported metrics)?
5. Who needs this evidence and for what decisions?

### Step 2: Define value with the customer

Value is defined *with* each customer, not assumed. For each account (or segment template):
- **Desired outcomes** — the business results they bought for, in their words and their metrics (e.g., "cut month-end close from 10 to 6 days").
- **Baseline** — where they are today on each metric, measured before or at go-live. Without a baseline you can only claim anecdotes.
- **Success criteria and targets** — the measurable level that counts as success, and by when.
- **Required capabilities and adoption** — which use cases must be live and which personas must be active.
- **Milestones** — first value, interim checkpoints, full value.
- **Customer-side owner** — who on their side owns the result and will confirm it.

Capture this in `templates/customer-success-plan-template.md`. Start the conversation during the sale or at kickoff; agreeing success criteria after the fact invites revisionism on both sides.

### Step 3: Build segment-level value hypotheses

For repeatable products, define 3–5 standard outcomes per segment or persona with typical metrics and benchmarks, drawn from `pragmatic-market-problems` and early customer evidence. Teams then tailor rather than invent per account. Read `references/value-realization-guide.md` for outcome categories and metric examples.

### Step 4: Gather evidence of results

At each milestone, collect evidence:
- **Customer-reported metrics** — the strongest evidence; ask for their numbers.
- **Product data** — usage, throughput, time saved, errors avoided, where the product can observe it.
- **Qualitative evidence** — interviews with the customer owner and users about what changed.
- **Third-party or audited results** — for high-stakes claims.

Rate evidence strength (customer-confirmed and quantified > product-measured > estimated > anecdotal). Record each in `templates/value-evidence-record-template.md`. Ask directly about outcomes that weren't achieved, and why.

### Step 5: Run value reviews

Hold periodic value reviews (often part of a QBR or EBR) focused on outcomes: progress vs. baseline and target, what's blocking, what changes are needed on both sides, and whether the desired outcomes have shifted. Not achieving value is a joint problem: diagnose whether it's adoption, product capability, implementation, or the customer's own change.

### Step 6: Share with the teams who build, sell and support

Aggregate evidence across accounts:
- **Build** — unmet or partly met outcomes with causes → `pragmatic-requirements`, `pragmatic-product-roadmap`.
- **Sell** — quantified proof points, typical results by segment, realistic time to value → `pragmatic-assets`, `pragmatic-positioning`, `pragmatic-organizational-alignment`.
- **Support and success** — playbooks that correlate with faster value → `pragmatic-adoption`, `pragmatic-retention`.
- **Leadership** — portfolio view of customer outcomes alongside `pragmatic-business-outcomes`.

Get customer permission before using results externally.

### Step 7: Close the loop to Market Problems

Each cycle, summarize: outcomes customers achieve reliably, outcomes they don't, new outcomes they're asking for, and segments where results differ. Write these as market-problem evidence and take them to `pragmatic-market-problems`. Validate with the broader market, including non-customers (NIHITO).

## Worked example

A finance-automation product's mid-market customers buy it to close the books faster.

- **Success plan:** at kickoff, the customer's controller agrees on one outcome (month-end close from 10 days to 6 within two quarters), a baseline from their last three close calendars, and two prerequisites: bank feeds connected and the spreadsheet reconciliation retired.
- **Evidence:** at the first value review, close time is 8 days (customer-confirmed, evidence level A). Reconciliation is still partly in spreadsheets because two subsidiaries use a currency the product handles poorly.
- **Diagnosis:** a capability gap, not an adoption problem. Similar gaps show up in four other accounts with foreign subsidiaries.
- **Share and loop:** product gets a multi-currency problem statement with five accounts of evidence (`pragmatic-requirements`); sales gets a realistic proof point ("typically 20–40% faster close; slower where multi-currency is involved"); the pattern goes to `pragmatic-market-problems` to check how common multi-entity, multi-currency needs are in the target segment.

## Output formats

- **Customer success plan** — outcomes, baseline, metrics, milestones, owners (`templates/customer-success-plan-template.md`).
- **Value evidence record / value review** — per-account evidence and review notes (`templates/value-evidence-record-template.md`).
- **Segment value hypotheses** — standard outcomes and metrics per segment.
- **Value realization report** — cross-account summary for product, sales, CS and leadership, with routed findings.
- **Market-problem hand-off** — unmet and emerging outcomes with evidence.

## Common pitfalls

- **Treating usage or renewal as value.** Both are proxies. Ask the customer about the outcome.
- **No baseline.** Without "before," there's no credible "after."
- **Vendor-defined success.** If the customer wouldn't recognize the criteria, they aren't success criteria.
- **Only collecting good news.** Unmet outcomes are the most useful finding for product.
- **Confusing CVR with satisfaction.** A high NPS doesn't prove results; a frustrated customer may still be getting them.
- **Keeping evidence in CS.** Value evidence that never reaches product, marketing and sales doesn't close the loop.
- **Overstating results externally.** Use customer-confirmed numbers with permission; label estimates as estimates.

## Using AI in this focus area

- Extract stated purchase reasons and success criteria from sales notes, business cases and kickoff recordings to draft success plans.
- Summarize value reviews and customer interviews; aggregate evidence across accounts by outcome and segment.
- Draft value reports and proof-point summaries for product and sales, clearly marking estimated vs. confirmed results.
- Rules: confirm every claimed outcome with the customer; AI can't tell you whether they got value, only organize what they told you (NIHITO still applies); keep customer metrics and account data out of tools not approved for them; the team, not the tool, owns conclusions and external claims.

## Reference files

- `references/value-realization-guide.md` — outcome categories and metrics, baselining methods, evidence strength, value review agenda, diagnosing unrealized value, sharing and the loop to Market Problems, internal-product notes. Read before Steps 2–7.
- `templates/customer-success-plan-template.md` — customer success plan template. Read when defining success with a customer.
- `templates/value-evidence-record-template.md` — value evidence record and value review template. Read when gathering evidence or running a review.
