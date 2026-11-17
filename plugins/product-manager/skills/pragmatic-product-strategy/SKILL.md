---
name: pragmatic-product-strategy
description: "Guides the Product Strategy focus area of the 2027 Pragmatic Framework (Pragmatic Institute): what will this product be known for, and what will we say no to? Helps teams write a one-page product strategy grounded in validated market problems and distinctive competencies: the value the product creates, the problems it solves, the target market, the competencies it draws on, what it says no to, the company goals it supports, and when to revisit it. Use whenever the user mentions product strategy, product vision and strategy, strategic direction, 'what should our product be known for', saying no, strategic trade-offs, a strategy one-pager, aligning roadmap or portfolio to strategy, revisiting strategy after a market change, or an asset inventory / asset assessment / asset registry ('what do we already have?', formerly the Asset Assessment focus area). Downstream it guides the roadmap, portfolio and business plan."
---

# Product Strategy — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Market — *What problems does the market have, and where can we win?*
- **Focus-area question:** *What will this product be known for, and what will we say no to?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Market Problems, Distinctive Competencies, Win/Loss Analysis, Competitive Landscape
- **Formerly:** New in 2027. Replaces Asset Assessment in the Market category; the asset inventory is now an input to this focus area.

## What Product Strategy Is

Product strategy sets the long-term direction for a product: the value it will create, the problems it will solve, and the choices that guide decisions over time. It gives the roadmap, the portfolio and the business plan a shared point of reference, so they stop pulling in different directions.

Four tests from the Framework define a working product strategy:

1. **Grounded** in validated market problems and the organization's distinctive competencies, not in internal preference.
2. **Written down.** A strategy that lives in people's heads can't be checked, shared or challenged.
3. **Connected to company goals.** It says which goals the product serves and how.
4. **Used.** It is revisited when the market changes, and it is used to say no to work that doesn't serve it.

Product Strategy is emphasized in Pragmatic Institute's Focus course.

### Strategy is not the roadmap

| | Product strategy | Product roadmap |
|---|---|---|
| Answers | What will the product be known for? What won't we do? | Which outcomes come next, and in what order? |
| Horizon | Multi-year; stable unless the market shifts | Quarters; changes often |
| Content | Value, problems, target market, competencies, trade-offs, goals | Sequenced outcomes and themes |
| Changes when | Review triggers fire (market, competitor, goal change) | Priorities, evidence or capacity change |

If the roadmap changes and the strategy doesn't, that's normal. If the strategy changes every quarter, it's a roadmap in disguise.

## Inputs

| Input | From (focus area, category) | What it contributes |
|---|---|---|
| Validated market problems, with desired outcomes | Market Problems (Market) — `pragmatic-market-problems` | The problems the strategy can choose among |
| Distinctive competencies | Distinctive Competencies (Market) — `pragmatic-distinctive-competencies` | Where you have a right to win |
| Asset inventory ("what do we already have?") | This skill — `references/asset-categories.md`, `references/asset-registry-template.md` | Technology, IP, skills, data, relationships you can build on |
| Win/loss findings | Win/Loss Analysis (Market) — `pragmatic-win-loss-analysis` | Why evaluators chose you or didn't |
| Alternatives, including doing nothing | Competitive Landscape (Market) — `pragmatic-competitive-landscape` | Where others are entrenched; where the gaps are |
| Target segments | Market Definition (Focus) — `pragmatic-market-definition` | Who the product is for (can be refined in parallel) |
| Company goals | Leadership, company strategy, OKRs | What the business needs the product to deliver |

If market problems or distinctive competencies are missing, say so. A strategy without them is a guess; offer to help with those first or proceed with clearly labeled assumptions.

## Process

### Step 1: Confirm the scope and the company goals

Which product (or product line) is this strategy for, and over what horizon (typically 2–3 years)? Write down the company goals it must support: growth targets, new markets, retention, efficiency, platform consolidation. Get them from leadership, not from memory.

### Step 2: Take stock: what do we already have?

Run a proportionate asset inventory: technology, IP, skills and expertise, products and components, services, marketing and content, data, and relationships. The aim is to find what the strategy can build on and what gaps it would have to close.

- Use `references/asset-categories.md` for discovery questions by category and the short inventory method.
- Record results in the registry structure in `references/asset-registry-template.md`. For one product strategy, the lightweight version is usually enough.
- Flag assets that map to a validated market problem; those are strategy candidates. Pass candidate competencies to `pragmatic-distinctive-competencies` for PRIME validation.

### Step 3: Choose the problems and the market

From the validated problems, choose the few the product will be known for solving, for a defined target market. Favor problems that are urgent, pervasive and paid for, and where your distinctive competencies give you an edge. Name the desired outcomes customers want.

### Step 4: State the value

In one or two sentences: what value does the product create, for whom, and why it's better than the alternatives (including doing nothing). This is not positioning copy; it is the internal statement positioning will later draw from.

### Step 5: Decide what you'll say no to

List the segments, problems, use cases, feature categories, deal types and business models the product will **not** pursue, with a one-line reason each. This is the part teams skip and the part that makes the strategy useful. Good "no" items are specific enough that someone could cite them to turn down a real request.

### Step 6: Tie it to company goals and measures

For each company goal, say how the product contributes and how you'll know: one or two measures per goal. Hand detailed indicators to `pragmatic-measurement` (Business).

### Step 7: Set review triggers

Write down what would make you revisit the strategy before the scheduled review: a competitor move that changes the alternatives, a shift in the target market's problems, a change in company goals, repeated losses in a segment, a technology change, a pattern in Customer Value Realization, Exceptions or Escalations. Set a scheduled review too (annually at least; semiannually in fast markets).

### Step 8: Write it down and share it

Fill in `templates/product-strategy.md`, one page. Share it with product, engineering, marketing, sales, customer success and leadership. Ask each group what they would now do differently; if the answer is "nothing," the strategy isn't specific enough.

## Using the strategy downstream

| Downstream focus area (category) | How the strategy guides it |
|---|---|
| Product Roadmap (Focus) — `pragmatic-product-roadmap` | Roadmap themes sequence the outcomes the strategy commits to; "no" items stay off |
| Product Portfolio (Focus) — `pragmatic-product-portfolio` | Each offer's role and investment level is checked against the strategy |
| Business Plan (Business) — `pragmatic-business-plan` | The plan confirms fit with the strategy before modeling; fund, delay or stop |
| Market Definition (Focus) | Target market choices stay consistent |
| Positioning (Planning) — `pragmatic-positioning` | Positioning draws on the value statement and chosen problems |
| Buy, Build or Partner (Business) | Asset gaps that block the strategy become BBP decisions |

### Saying no in practice

When a request arrives (a big customer's feature, an executive's idea, a competitor's move), check it against the strategy:

1. Does it solve one of the chosen problems for the target market?
2. Is it on the "no" list?
3. Does it support a stated company goal?

If it fails, decline and cite the strategy. If the request is compelling and still fails, that's a signal to check the review triggers, not to quietly make an exception.

## Internal products and platforms

For an internal product, the same structure applies. "Market" is the internal teams and workflows served; "value" is usually time saved, risk reduced or cost avoided; company goals often include efficiency or consolidation. The "no" list matters even more, because internal products tend to collect one-off requests from every team.

## Common Pitfalls

- **A vision statement with no choices** — inspiring words, nothing ruled out
- **A roadmap relabeled as strategy** — a list of features with dates
- **Inside-out strategy** — built on what engineering wants to build, not on validated problems
- **Unwritten strategy** — "everyone knows it," so no one can check against it
- **Disconnected from company goals** — leadership can't see why to fund it
- **Never revisited** — the market moved and the strategy didn't
- **Asset-led strategy** — "we have this technology, so let's find a use" without a market problem

## Output Formats

- **One-page product strategy** — `templates/product-strategy.md`
- **Asset registry** (spreadsheet) — `references/asset-registry-template.md`; use the xlsx skill
- **Strategy review memo** — what changed, which triggers fired, what the strategy now says
- **Strategy-to-roadmap check** — roadmap themes mapped to strategic choices, with orphans flagged

## Using AI in this focus area

- Draft a first-pass strategy one-pager from your market problems report, competency assessment and company goals, for the team to challenge.
- Speed up the asset inventory by summarizing existing docs, repos and wikis into draft registry rows.
- Stress-test the "no" list: generate realistic requests and check whether the strategy settles them.
- Rules: check AI output against real market evidence; NIHITO still applies, and AI can't tell you which problems your market will pay to solve. Keep unreleased strategy, financials and customer data out of tools not approved for them. The team, not the tool, makes the strategic choices.
- Weak spot: AI writes fluent strategy that commits to nothing. If a draft rules nothing out, it isn't done.

## Reference Files

- `templates/product-strategy.md` — one-page product strategy template
- `references/asset-categories.md` — asset categories, discovery questions and inventory method (Step 2)
- `references/asset-registry-template.md` — asset registry structure, including strategy-relevance columns (Step 2)
