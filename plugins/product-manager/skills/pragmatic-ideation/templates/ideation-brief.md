# Ideation Brief Template

The Ideation Brief (formerly the Innovation Brief) captures one concept before the team commits to full delivery. It connects a validated market problem and user insight to a proposed concept, names the assumptions that must be true, and lays out how the team will test them with real users. Think of it as the case for *testing* an idea, and later, with evidence attached, the case for *building* it.

## When to Use

- A workshop or discovery work has produced a concept worth exploring
- A product manager needs to present a concept to leadership for a test budget or a delivery decision
- A concept needs to be compared with others in the idea portfolio (`templates/idea-portfolio.md`)
- The team wants to move from "interesting idea" to "tested concept"

## How to Guide the User

Walk through each section. Ask the guiding questions and help draft clear, concise answers. Push back if answers are vague or not connected to market evidence. Sections 6 and 7 get updated as experiments run.

---

## Ideation Brief Structure

### 1. Market Problem Statement
*What pain are we addressing, and for whom?*

- **Who** has this problem (specific persona or segment)
- **What** the problem is (in the customer's language)
- **How often** it happens
- **Why** it matters (consequences of leaving it unsolved)
- **How urgent** and **how pervasive** it is

**Evidence required**: Specific customer interviews, win/loss data, support data or market research. If the user can't point to external evidence, stop: the problem is assumed, not validated. Go back to Market Problems (`pragmatic-market-problems`).

Example:
> Mid-market IT directors spend about 12 hours a week manually reconciling security alerts across 4+ disconnected tools, delaying incident response (avg 6 hours) and creating compliance gaps. In 23 of 30 customer interviews in Q2 this was a top-3 pain point. Three recent losses cited our lack of a unified view as the deciding factor.

### 2. User Insight
*What do we know about the people who will use the solution?*

- Which user persona(s) does this serve? (`pragmatic-user-personas`)
- What does their current workflow and workaround look like?
- What did we observe (not just hear) that suggests an opportunity?

### 3. Concept Description
*What are we proposing to build or do differently?*

- What is it? (feature, new product, service, process change, packaging or pricing change, etc.)
- Type: incremental, adjacent or transformational
- How does it address the stated problem for the persona?
- What would the experience look like? (a sketch, storyboard or prototype link beats a paragraph)

Keep it specific and free of buzzwords. Could a reasonably informed person read this and understand what you'd actually build?

### 4. Why Us
*What makes us well placed to do this?*

- Which distinctive competencies or existing assets apply? (`pragmatic-distinctive-competencies`)
- Does it fit Product Strategy, or is it something we said we'd say no to? (`pragmatic-product-strategy`)
- What are customers using today instead, including doing nothing? (`pragmatic-competitive-landscape`)

If any well-funded competitor could do the same thing just as easily, that doesn't kill the idea, but it changes the risk.

### 5. Assumptions and Riskiest Assumption
*What must be true for this to work?*

List assumptions by type, then pick the one that is both most uncertain and most damaging if wrong:
- **Desirability** — users have the problem and want this solution
- **Usability** — users can figure out how to use it
- **Viability** — the market will pay, and it works for the business
- **Feasibility** — we can build and support it

**Riskiest assumption:** ______________________

### 6. Experiments
*How will we test it, cheaply and early, with real users?*

For each experiment, attach an experiment plan (`templates/experiment-plan.md`) and summarize here:

| # | Assumption tested | Method | Users | Success threshold | Result | Decision |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |

### 7. Expected Value
*What outcomes do we expect if it works?*

**For customers:** time saved, cost reduced, risk lowered; how users would measure success.
**For the business:** revenue, retention, adoption, efficiency or strategic position, in rough order of magnitude. Large bets feed the Business Plan (`pragmatic-business-plan`).

### 8. Recommendation and Next Steps
*Keep, change or drop?*

- **Before testing:** which experiment runs first, who owns it, by when
- **After testing:** keep (hand to Requirements and the roadmap), change and re-test, or drop (record what was learned)

---

## Quality Checklist

- [ ] The market problem is backed by external evidence, not internal opinion
- [ ] The target user persona is named and real users are lined up to test with
- [ ] The riskiest assumption is identified and has an experiment planned against it
- [ ] Each experiment has a success threshold set *before* it runs
- [ ] The people who will build it were involved in shaping it
- [ ] Customer value is described in the customer's terms
- [ ] The brief is short enough to read in 10 minutes
