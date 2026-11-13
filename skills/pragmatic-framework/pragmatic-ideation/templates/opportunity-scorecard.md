# Ideation Opportunity Scorecard

## Purpose

The Opportunity Scorecard provides a structured, repeatable way to evaluate whether a specific idea or concept is worth pursuing further. It helps product teams decide what to test next, and what to commit to delivery, based on market evidence, user test results and strategic alignment rather than enthusiasm or politics. Score early (before testing) to choose what to test, and again after experiments to decide keep, change or drop.

This template operationalizes the Pragmatic principle: "Only build solutions for problems that are urgent, pervasive, and the market will pay to solve."

## When to Use

- Evaluating an Ideation Brief before running experiments or committing development resources
- Comparing multiple concepts to decide which to test or fund
- Reviewing experiment results to decide whether a concept continues or is dropped
- Building the case for or against moving a concept into Requirements and the roadmap

## How to Guide the User

Walk through each scoring dimension. For each dimension, ask the guiding questions, then help the user assign a score from 1-5 based on the evidence available. The scoring criteria are intentionally qualitative — the goal is structured thinking, not false precision.

After scoring all dimensions, calculate the weighted total and use the interpretation guide to recommend a course of action.

---

## Scoring Dimensions

### 1. Market Problem Validity (Weight: 25%)

*Every idea must be grounded in a validated market problem.*

*Is this solving a real, validated problem?*

| Score | Criteria |
|-------|----------|
| 5 | Problem validated through 15+ customer interviews; urgent and pervasive across segment; customers actively seeking solutions and willing to pay |
| 4 | Problem validated through 5-15 interviews; clearly urgent or pervasive; some willingness to pay signals |
| 3 | Problem mentioned in several interviews but not deeply validated; urgency or pervasiveness unclear |
| 2 | Problem assumed based on internal observations or a small number of anecdotes; minimal external validation |
| 1 | No external validation; problem is hypothesized by the internal team |

**Key questions**:
- How many customers independently confirmed this problem?
- Did the problem surface organically, or did you have to lead people to it?
- Are customers spending money or time on workarounds today?
- Does this show up in win/loss data?

### 2. User Test Evidence (Weight: 20%)

*What happened when real users tried the concept or prototype?*

| Score | Criteria |
|-------|----------|
| 5 | Multiple experiments with target users met or beat their success thresholds; users completed the key task and asked when they can have it |
| 4 | At least one well-run experiment met its threshold; feedback consistent across users |
| 3 | Early concept tests are encouraging but small or mixed; riskiest assumption not yet tested |
| 2 | Only internal reviews or friendly users; no test against a success threshold |
| 1 | Not tested with users, or tests missed their threshold |

**Key questions**:
- Which riskiest assumption has been tested, and what was the success threshold?
- Were the test participants real target users (matching the user persona)?
- Did users behave differently from what they said?
- See `templates/experiment-plan.md`.

### 3. Distinctive Competency Alignment (Weight: 10%)

*Are we uniquely positioned to solve this?*

| Score | Criteria |
|-------|----------|
| 5 | Directly leverages 2+ distinctive competencies; competitors would need years to replicate our approach |
| 4 | Leverages at least one strong distinctive competency; meaningful competitive moat |
| 3 | Leverages core competencies but nothing truly distinctive; moderate defensibility |
| 2 | Requires building new competencies we don't currently have; low defensibility |
| 1 | No alignment with existing competencies; any well-funded competitor could do this equally well |

**Key questions**:
- Which specific PRIME attributes does this leverage?
- Could a competitor with more resources build the same thing just as well?
- What existing assets (tech, data, expertise, relationships) accelerate our ability to deliver?
- Is there a natural connection between this idea and what our brand is known for?

### 4. Market Size and Impact (Weight: 15%)

*Is the opportunity large enough to matter?*

| Score | Criteria |
|-------|----------|
| 5 | Large addressable market within target segments; could become a significant revenue driver or fundamentally change competitive position |
| 4 | Meaningful market opportunity; clear path to material revenue or strategic impact |
| 3 | Moderate opportunity; will contribute to growth but not transformational |
| 2 | Niche opportunity affecting a small subset of the market |
| 1 | Minimal market impact; benefits very few customers |

**Key questions**:
- How many customers/accounts in our target segments would benefit?
- What's the potential revenue impact (new sales, retention, expansion)?
- Does this open new market segments or strengthen position in existing ones?
- What would winning here mean for our competitive position?

### 5. Feasibility (Weight: 15%)

*Can we actually deliver this?*

| Score | Criteria |
|-------|----------|
| 5 | Well within current technical capabilities; clear architecture; reasonable timeline |
| 4 | Mostly within current capabilities; some manageable technical challenges |
| 3 | Requires significant technical work but no fundamental unknowns; 6-12 month timeline |
| 2 | Major technical challenges or unknowns; requires new skills or infrastructure; 12+ months |
| 1 | Fundamental technical uncertainty; may not be possible with current technology |

**Key questions**:
- Do we have the technical skills and infrastructure to build this?
- Have we done a technical feasibility assessment or proof of concept?
- What's the realistic timeline from start to first customer?
- What dependencies exist (third-party tech, regulatory, partnerships)?

### 6. Strategic Fit (Weight: 10%)

*Check against Product Strategy (Market, `pragmatic-product-strategy`): does this fit what the product will be known for, or is it something we said no to?*

*Does this align with where the business is heading?*

| Score | Criteria |
|-------|----------|
| 5 | Directly supports stated company strategy and product vision; executive priority |
| 4 | Aligns with strategy; reinforces product direction |
| 3 | Neutral — doesn't conflict with strategy but isn't a stated priority |
| 2 | Tangential to current strategy; would require strategy adjustment |
| 1 | Conflicts with current strategic direction |

### 7. Competitive Urgency (Weight: 5%)

*What happens if we don't do this?*

| Score | Criteria |
|-------|----------|
| 5 | Competitors are actively building this; we risk losing significant market share without it |
| 4 | Competitive gap is emerging; early action gives meaningful advantage |
| 3 | No immediate competitive pressure but the market is moving in this direction |
| 2 | Low competitive pressure; nice-to-have from a competitive standpoint |
| 1 | No competitive relevance |

---

## Calculating the Score

Weighted Score = (Problem × 0.25) + (User Evidence × 0.20) + (Competency × 0.10) + (Market × 0.15) + (Feasibility × 0.15) + (Strategic × 0.10) + (Urgency × 0.05)

**Maximum possible score: 5.00**

## Interpretation Guide

| Score Range | Recommendation |
|-------------|---------------|
| 4.0 – 5.0 | **Strong Invest** — Well-validated, well-aligned opportunity. Move toward Requirements, the roadmap and (for large bets) a business case. |
| 3.0 – 3.9 | **Conditional Invest** — Promising but has gaps. Identify the lowest-scoring dimensions and design the next experiment to close that gap before committing delivery resources. |
| 2.0 – 2.9 | **Explore Further** — Interesting but not yet investment-ready. Needs more market validation or a first test with users. |
| Below 2.0 | **Pass** — Drop it. Document the reasoning and the evidence, and revisit only if market conditions change. |

## Important Caveats

- **Scores are conversation starters, not final answers.** A transformational concept might score lower on feasibility but still be worth pursuing if the strategic upside is enormous. Use the scorecard to structure the conversation, then apply judgment.

- **Low scores on Problem Validity should be disqualifying regardless of total score.** An idea that scores 5 on everything else but 1 on problem validity is building something nobody asked for. Don't let exciting technology compensate for missing market evidence.

- **Revisit scores as new information emerges.** An idea scored today will look different after a round of user testing or a technical prototype. Re-score when material new evidence appears.

- **Compare across opportunities.** The scorecard is most useful when applied consistently across multiple opportunities, allowing apples-to-apples comparison for portfolio prioritization.
