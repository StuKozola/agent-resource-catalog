# Prioritization Methods for Product Roadmaps

Prioritization is the hardest part of roadmapping. The Pragmatic Framework insists that
prioritization be evidence-based and market-driven — not driven by the loudest voice in the room.
This guide covers methods that align with Pragmatic principles.

## The Pragmatic Prioritization Lens

Before applying any framework, run every candidate roadmap item through these five questions from
the Pragmatic approach:

1. **Urgency:** How painful is this problem for the market right now? Is it blocking purchases,
   causing churn, or creating workarounds?
2. **Pervasiveness:** How many of our target personas and segments experience this problem? Is it
   niche or widespread?
3. **Willingness to pay:** If we solve this, will it drive new revenue, reduce churn, or justify
   a price increase? Would customers pay for this?
4. **Strategic alignment:** Does solving this leverage our distinctive competencies? Does it move
   us toward our product vision?
5. **Feasibility:** Can we deliver this with available resources in a reasonable timeframe? What
   are the dependencies and risks?

These five dimensions form the foundation. The methods below are ways to structure and score
against them.

---

## Method 1: Pragmatic Prioritization Scorecard

A simple weighted scoring model using the five Pragmatic dimensions.

**How it works:**
- List all candidate themes/initiatives
- Score each on a 1-5 scale across the five dimensions
- Apply weights based on your current strategic priority (e.g., if growth is the priority, weight
  Willingness to Pay higher; if retention is the priority, weight Urgency higher)
- Calculate a weighted total and rank

**Template:**

| Theme | Urgency (1-5) | Pervasiveness (1-5) | Willingness to Pay (1-5) | Strategic Alignment (1-5) | Feasibility (1-5) | Weighted Score |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| [Theme A] | 4 | 5 | 3 | 5 | 4 | — |
| [Theme B] | 3 | 3 | 5 | 4 | 2 | — |

**Default weights (adjust to your strategy):**
- Growth-focused: Urgency 20%, Pervasiveness 25%, Willingness to Pay 25%, Strategic Alignment 20%, Feasibility 10%
- Retention-focused: Urgency 30%, Pervasiveness 20%, Willingness to Pay 15%, Strategic Alignment 20%, Feasibility 15%
- Innovation-focused: Urgency 10%, Pervasiveness 15%, Willingness to Pay 20%, Strategic Alignment 30%, Feasibility 25%

**When to use:** Good default method for most teams. Works well for quarterly roadmap reviews.

**Watch out for:** Scores can create a false sense of precision. A theme scoring 3.7 vs 3.5 is
effectively tied. Use scores to sort into tiers (must-do, should-do, could-do), not to create
a strict rank order.

---

## Method 2: RICE Framework (Adapted for Pragmatic)

RICE (Reach, Impact, Confidence, Effort) is popular in product management. Here's how to adapt
it to be more market-driven:

- **Reach:** How many target personas will this affect in a given time period? (Maps to
  Pervasiveness)
- **Impact:** How significantly will this solve the market problem? Score 0.25 (minimal), 0.5
  (low), 1 (medium), 2 (high), 3 (massive). (Maps to Urgency + Willingness to Pay)
- **Confidence:** How strong is the market evidence? 100% = direct customer interviews confirm.
  80% = win/loss data supports it. 50% = competitive intel suggests it. 20% = internal hunch.
  (This is the Pragmatic gut-check — low confidence items need more market research before
  committing)
- **Effort:** Person-months of engineering work. (Maps to Feasibility, inverted)

**Formula:** (Reach × Impact × Confidence) / Effort = RICE Score

**When to use:** When you need a single numeric score to compare very different types of
initiatives. Good for teams already familiar with RICE.

**Watch out for:** RICE penalizes high-effort items even when they're strategically essential.
Use it as input, not gospel.

---

## Method 3: Value vs. Effort Matrix

A 2×2 matrix that's quick and collaborative, good for workshop settings.

**Axes:**
- **X-axis: Effort** (Low → High). Based on engineering estimates and dependency complexity.
- **Y-axis: Market Value** (Low → High). Composite of Urgency, Pervasiveness, and Willingness
  to Pay.

**Quadrants:**
- **High Value, Low Effort (Quick Wins):** Do these first. They build momentum and credibility.
- **High Value, High Effort (Big Bets):** Strategic investments. Plan carefully, phase delivery.
- **Low Value, Low Effort (Fill-Ins):** Do these when capacity allows. Don't prioritize them
  over big bets.
- **Low Value, High Effort (Money Pits):** Avoid unless there's a compelling strategic reason
  (e.g., regulatory requirement).

**When to use:** In collaborative sessions with cross-functional stakeholders. The visual format
makes trade-offs tangible and debatable.

**Watch out for:** "Value" is often under-defined. Be explicit that value means *market-validated
value*, not internal opinion of value.

---

## Method 4: MoSCoW (for Constraint-Based Prioritization)

When capacity is fixed and you need to decide what fits, MoSCoW is efficient:

- **Must Have:** The roadmap fails without these. Typically contractual obligations, regulatory
  requirements, or problems so urgent that churn is imminent.
- **Should Have:** Important but not fatal if delayed one cycle. High market evidence, but the
  business won't collapse without them this quarter.
- **Could Have:** Desirable, would delight, but postponable. Often items with moderate market
  evidence or lower pervasiveness.
- **Won't Have (this time):** Explicitly excluded. Documenting what you're NOT doing is as
  important as what you're doing — it prevents scope creep and manages expectations.

**When to use:** During quarterly planning when you know your capacity and need to make hard
cut-line decisions.

**Watch out for:** Everything becomes a "Must Have" without discipline. Require that Must Haves
have direct market evidence or contractual/regulatory backing.

---

## Method 5: Opportunity Scoring (Outcome-Driven Innovation)

Based on the ODI (Outcome-Driven Innovation) methodology, this is ideal when you have access to
quantitative customer survey data.

**How it works:**
- Identify the outcomes customers want (not features — outcomes)
- Survey customers on two dimensions per outcome: Importance (how important is this outcome?)
  and Satisfaction (how well does the current solution deliver on this outcome?)
- Calculate: Opportunity Score = Importance + max(Importance - Satisfaction, 0)
- High importance, low satisfaction = underserved outcomes = top priorities

**When to use:** When you have quantitative market data and want the most evidence-based
approach possible. Aligns well with Pragmatic's emphasis on market-driven decisions.

**Watch out for:** Requires upfront investment in customer surveys. Not suitable for rapid
pivots or early-stage products without an established customer base.

---

## Combining Methods

No single method is complete. The best Pragmatic teams combine:

1. **Pragmatic Scorecard** for initial ranking across market dimensions
2. **Value vs. Effort Matrix** for collaborative stakeholder alignment
3. **MoSCoW** for final cut-line decisions given capacity constraints

Use the scorecard to do the analytical homework, the matrix to get cross-functional buy-in, and
MoSCoW to make the final call.

---

## Common Prioritization Traps

**The HiPPO trap:** Highest Paid Person's Opinion overrides market data. Counter by requiring
evidence for every priority claim. The Pragmatic mantra: "Your opinion, although interesting,
is irrelevant" — what matters is what the market says.

**The squeaky-wheel trap:** One loud customer or one aggressive salesperson dominates priorities.
Counter by asking: "Is this one customer's problem, or is it pervasive across the target
segment?"

**The sunk-cost trap:** Continuing investment in a theme because you've already spent time on it.
Counter by re-evaluating every theme every cycle on its current merits, not its history.

**The recency trap:** Over-prioritizing the most recently discovered problem. Counter by requiring
that new problems go through the same evidence-gathering process as everything else before
jumping the queue.

**The feasibility trap:** Always doing what's easiest rather than what's most valuable. Counter
by separating value assessment from effort assessment. Score value first, then factor in effort.
