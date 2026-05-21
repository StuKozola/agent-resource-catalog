# Gathering Upstream Inputs for Requirements

Before writing a single requirement, you need to assemble the market knowledge that feeds the requirements process. This guide walks through each input source and what to extract from it.

## Table of Contents
1. Market Problems Input
2. Persona Definitions Input
3. Win/Loss Analysis Input
4. Competitive Landscape Input
5. Business Plan Constraints
6. Assessing Readiness

---

## 1. Market Problems Input

Market Problems is the most critical upstream input. Requirements without validated market problems are just opinions.

**What to extract:**
- The master list of validated problems from NIHITO interviews
- For each problem: urgency rating, pervasiveness (number of customer/prospect sites reporting it), and willingness to pay
- The distinction between problems reported by current customers vs. prospects vs. lost deals
- Any quantitative data on frequency and business impact

**Key question to ask the user:**
"Do you have a validated set of market problems with pervasiveness data? If not, the Market Problems activity should come first — requirements without market evidence tend to reflect internal assumptions rather than market reality."

**If market problems exist but are informal:**
Help the user structure them into a problem inventory with columns for: Problem Statement, Source Count (how many unique sites reported it), Urgency (1-5), Segment, and Persona.

---

## 2. Persona Definitions Input

Pragmatic requirements are persona-centric. Every requirement must be tied to a specific persona.

**Two persona types matter for requirements:**

### Buyer Personas
- Involved in the purchase decision
- Concerned with value, ROI, total cost of ownership
- Requirements from buyers tend to be about integration, compliance, vendor stability, pricing models
- Types: Economic Buyer (approves budget), Technical Buyer (evaluates fit with tech environment)

### User Personas
- Actually use the product in daily work
- Concerned with capabilities, ease of use, workflow efficiency
- Requirements from users tend to be about tasks, pain points, workarounds
- There are usually only one or two primary user personas

**What to extract from existing personas:**
- Name and role description
- Key goals and tasks
- Primary frustrations and pain points
- Technical proficiency level
- Frequency of product use
- Current workarounds for unsolved problems

**If personas don't exist yet:**
Help the user create lightweight persona sketches sufficient for requirements. At minimum, each persona needs: a name, a role, their top 3 goals, and their top 3 frustrations. Full persona development is a separate Pragmatic activity, but requirements can begin with sketches.

---

## 3. Win/Loss Analysis Input

Win/Loss data reveals requirements that the market is actively making purchase decisions around.

**What to extract:**
- Top reasons evaluators chose a competitor (loss reasons) — these often point to missing capabilities
- Top reasons evaluators chose your product (win reasons) — these reveal requirements you're already meeting and should protect
- Steps in the buying process where evaluators got stuck or dropped out
- Feature gaps cited during evaluations
- Unexpected requirements that surfaced during sales cycles

**How to use this in requirements:**
- Loss reasons with high frequency become candidate requirements
- Requirements that drove wins should be flagged as "protect" items — regression in these areas would be damaging
- Buying process friction points may indicate non-functional requirements (trial experience, documentation, integration ease)

---

## 4. Competitive Landscape Input

Competitive intelligence helps you understand the requirement landscape — what's table stakes vs. differentiating.

**What to extract:**
- Features competitors offer that you don't (potential gap requirements)
- Features where you lead (distinctive competence to protect)
- Market direction — where competitors are investing signals emerging requirements
- Alternative solutions customers use (including manual workarounds, spreadsheets, etc.)

**Caution:** Competitive features should not automatically become requirements. The question is always "Is this solving a validated market problem for our target personas?" A competitor feature that doesn't solve a problem your personas care about is noise, not signal.

---

## 5. Business Plan Constraints

The Business Plan sets boundaries on what requirements are feasible to pursue.

**What to extract:**
- Target market segments and their relative priority
- Revenue targets and financial model assumptions
- Resource constraints (team size, budget, timeline)
- Strategic bets or commitments already made
- Contractual obligations to specific customers
- Platform or technology constraints

**How constraints shape requirements:**
- Requirements for deprioritized segments get lower scores
- Resource constraints determine how many requirements can fit in a release
- Contractual commitments may force certain requirements to the top regardless of market scoring
- Strategic bets may override pure market-evidence prioritization (but this should be explicit and rare)

---

## 6. Assessing Readiness

Before proceeding to write requirements, verify that sufficient inputs exist. Use this readiness checklist:

**Minimum viable inputs (can proceed):**
- [ ] At least 5-10 validated market problems with some pervasiveness data
- [ ] At least one user persona defined (even if lightweight)
- [ ] General awareness of competitive landscape
- [ ] Awareness of any hard constraints (timeline, budget, commitments)

**Ideal inputs (will produce the best MRD):**
- [ ] Comprehensive market problem inventory with urgency/pervasiveness/willingness-to-pay scores
- [ ] Both buyer and user personas fully defined
- [ ] Win/Loss analysis completed with pattern data
- [ ] Competitive landscape documented with gap analysis
- [ ] Business plan with financial model and segment priorities
- [ ] Product roadmap context (what release are we targeting?)

If the user has minimal inputs, help them work with what they have while flagging gaps. An imperfect MRD based on some market evidence is far better than no MRD, but be transparent about confidence levels.
