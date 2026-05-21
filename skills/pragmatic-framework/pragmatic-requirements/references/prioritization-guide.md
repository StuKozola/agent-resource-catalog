# Prioritizing Market Requirements

Prioritization determines what gets built next. Without a systematic, evidence-based approach, products get shaped by the loudest voice in the room — typically executive opinion or sales escalations — rather than market reality.

## Table of Contents
1. Why Prioritization Matters
2. The Evidence-Based Scoring Model
3. Scoring Dimensions
4. Calculating Priority Scores
5. Handling Special Cases
6. Presenting Priorities to Stakeholders
7. Maintaining Priorities Over Time

---

## 1. Why Prioritization Matters

Not all problems are equally important. A requirement that represents a widespread, urgent problem that customers will pay to solve should rank above a niche problem that mildly inconveniences a few users. Prioritization creates a defensible, transparent basis for deciding what makes it into the next release.

Good prioritization also resolves organizational dysfunction. When account managers can see that their customer requirements are tracked, scored, and ranked against peers, they gain confidence in the process and escalation behavior decreases. When executives can see the evidence behind priorities, opinion-driven overrides become less frequent.

---

## 2. The Evidence-Based Scoring Model

The scoring model evaluates each requirement across multiple dimensions, producing a numeric priority score that allows objective comparison.

### Input Requirements for Scoring

Each requirement being scored should have:
- A clear problem statement tied to a specific persona
- Evidence of pervasiveness (how many sites/customers report this problem)
- An assessment of urgency (how pressing is this for those who experience it)
- An assessment of willingness to pay (would customers pay to solve this)
- A rough understanding of implementation effort

---

## 3. Scoring Dimensions

Score each requirement on a 1-5 scale across these dimensions:

### Dimension 1: Urgency (Weight: High)

How pressing is this problem for the personas who experience it?

| Score | Description |
|-------|-------------|
| 5 | **Critical** — Persona cannot accomplish core tasks; active workarounds consume significant time/money; customers threatening to churn |
| 4 | **High** — Significant pain; costly workarounds exist but are fragile or time-consuming |
| 3 | **Moderate** — Noticeable friction; workarounds are manageable but annoying |
| 2 | **Low** — Minor inconvenience; persona has adapted |
| 1 | **Minimal** — Nice-to-have; persona rarely notices the problem |

### Dimension 2: Pervasiveness (Weight: High)

How widespread is this problem across the target market?

| Score | Description |
|-------|-------------|
| 5 | **Universal** — 80%+ of target persona population reports this problem |
| 4 | **Very common** — 60-79% report it |
| 3 | **Common** — 40-59% report it |
| 2 | **Uncommon** — 20-39% report it |
| 1 | **Rare** — Under 20% report it |

Pervasiveness should be based on evidence from market interviews, surveys, support data, or win/loss analysis — not assumptions. If the data is thin, note the confidence level alongside the score.

### Dimension 3: Willingness to Pay (Weight: High)

Would customers pay (more) to have this problem solved?

| Score | Description |
|-------|-------------|
| 5 | **Strong signal** — Customers have explicitly stated budget availability or asked for pricing on a solution |
| 4 | **Positive indication** — Customers rank this highly and have paid competitors to solve it |
| 3 | **Probable** — Customers express desire but haven't been tested on willingness to pay specifically |
| 2 | **Uncertain** — Interest exists but no pricing signals; may be expected as part of existing product |
| 1 | **Unlikely** — Customers see this as table stakes or a minor enhancement not worth incremental spend |

### Dimension 4: Strategic Alignment (Weight: Medium)

How well does solving this problem align with the company's strategic direction?

| Score | Description |
|-------|-------------|
| 5 | **Core to strategy** — Directly supports the company's stated strategic bets and distinctive competence |
| 4 | **Strongly aligned** — Supports target segment growth or key market positioning |
| 3 | **Moderately aligned** — Consistent with strategy but not a focal point |
| 2 | **Tangential** — Serves a secondary segment or peripheral use case |
| 1 | **Misaligned** — Pulls resources toward areas outside strategic focus |

### Dimension 5: Competitive Pressure (Weight: Medium)

What is the competitive dynamic around this problem?

| Score | Description |
|-------|-------------|
| 5 | **Critical gap** — Competitors solve this well and it is a primary loss reason |
| 4 | **Significant gap** — Competitors address this; it comes up in evaluations |
| 3 | **Emerging factor** — Competitors are beginning to address this |
| 2 | **Neutral** — Neither advantage nor disadvantage |
| 1 | **Our advantage** — We already lead here; solving further yields diminishing returns |

### Dimension 6: Implementation Effort (Weight: Medium, Inverted)

How much effort is required to address this problem? Note: this dimension is *inverted* — lower effort gets a higher score because it increases priority.

| Score | Description |
|-------|-------------|
| 5 | **Trivial** — Days of work; minor changes to existing systems |
| 4 | **Small** — Weeks of work; contained to one team or component |
| 3 | **Moderate** — 1-2 months; involves multiple components or teams |
| 2 | **Large** — One quarter or more; significant architectural work |
| 1 | **Massive** — Multiple quarters; foundational changes needed |

---

## 4. Calculating Priority Scores

### Simple Weighted Formula

**Priority Score = (Urgency × 3) + (Pervasiveness × 3) + (Willingness to Pay × 3) + (Strategic Alignment × 2) + (Competitive Pressure × 2) + (Effort Score × 2)**

Maximum possible score: (5×3) + (5×3) + (5×3) + (5×2) + (5×2) + (5×2) = 75

### Interpreting Scores

| Score Range | Priority Tier | Implication |
|-------------|--------------|-------------|
| 60-75 | **Must Have** | Strong candidate for current release |
| 45-59 | **Should Have** | Strong candidate; include if capacity allows |
| 30-44 | **Could Have** | Future release candidate; keep on roadmap |
| Below 30 | **Won't Have (Now)** | Deprioritize; revisit if evidence changes |

### Adjusting Weights

The weights above are starting points. The user may adjust weights based on their specific situation:
- **Growth-stage companies** may weight Willingness to Pay and Pervasiveness even higher
- **Competitive markets** may weight Competitive Pressure higher
- **Resource-constrained teams** may weight Implementation Effort higher
- **Platform/infrastructure products** may weight Strategic Alignment higher

When adjusting weights, document the rationale so the scoring system remains transparent and defensible.

---

## 5. Handling Special Cases

### Contractual Commitments
Requirements tied to contractual customer commitments may need to override the scoring model. Flag these separately with a "Committed" tag and the contract details. They consume capacity but don't compete in the scoring model.

### Executive Mandates
When an executive overrides prioritization, document it transparently: the requirement, the override decision, the executive who made it, and the requirements it displaced. This creates accountability and a record for post-release analysis.

### Dependencies
Some requirements have technical dependencies — requirement B cannot be addressed without first solving requirement A. Note dependencies and ensure prerequisite requirements receive appropriate priority even if their standalone score is lower.

### Regulatory / Compliance
Requirements driven by regulatory deadlines (GDPR, HIPAA, PCI, etc.) with hard enforcement dates should be flagged as "Regulatory" and scheduled by deadline regardless of market scoring. They are constraints, not options.

---

## 6. Presenting Priorities to Stakeholders

### For Executives
Show the top 10-15 requirements with their scores, the scoring methodology, and the strategic rationale. Highlight any tension between market evidence and current strategic bets.

### For Development Teams
Show the categorized requirements relevant to their domain, with priority scores, persona context, and use scenarios. Highlight recently modified requirements.

### For Account Managers / Sales
Show that customer-reported requirements are tracked, scored, and ranked. Help them understand where their customer's requirement fits relative to the full market picture.

### For Customers
Show a sanitized, directional view — themes and timeframes, not specific requirements or scores. Never share internal scoring with external audiences.

---

## 7. Maintaining Priorities Over Time

Priorities are not set once — they should be revisited regularly:

- **Quarterly:** Full re-scoring as new market data comes in from ongoing customer interviews, support data, and win/loss analysis
- **After major market events:** Competitor launches, regulatory changes, or large customer losses may shift priorities
- **After each release:** Verify that addressed requirements actually solved the problem (closed-loop validation) and adjust remaining priorities based on what was learned

Keep a version history of the prioritization to track how priorities evolved and why. This becomes valuable institutional knowledge.
