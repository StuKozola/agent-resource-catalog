---
name: pragmatic-use-scenarios
description: Guide teams through the Pragmatic Framework Use Scenarios activity — writing narrative stories that put market problems in context for a specific user persona. Use this skill whenever someone wants to write, improve, or review use scenarios; needs to understand the difference between use scenarios, user stories, and use cases; is working on requirements, personas, or MRDs; wants to validate whether their use scenarios are solution-free and persona-grounded; or is building product requirements in the Pragmatic Framework. Trigger for any mention of "use scenario," "use case story," "problem narrative," "user problem story," or "requirements context."
---

# Pragmatic Framework: Use Scenarios

## Framework Context

**Category:** Planning  
**Official Definition:** Illustrate market problems in a "story" that puts the problem in context. Use scenarios are one component of requirements.

Use Scenarios live in the **Planning** band of the Pragmatic Framework, alongside Positioning, Buyer Experience, Buyer Personas, User Personas, Requirements, and Stakeholder Communications. They sit downstream of market research activities (Market Problems, User Personas) and feed directly into Requirements — giving development, design, and QA the rich problem context they need to build the right solutions.

**Key principle:** Use scenarios describe *problems*, never solutions. They answer "what is the user experiencing and why is it painful?" — not "what should the product do."

---

## What Is a Use Scenario?

A use scenario is a short narrative story that walks through a typical situation in which a specific user persona encounters a problem. It provides:

- **Who** — the persona experiencing the problem
- **What** — the specific problem or friction they face
- **When/Where** — the context and circumstances
- **Why it matters** — the emotional or business impact

Use scenarios are **not**:
- Use cases (which describe system interactions and flows)
- User stories (which follow "As a [role], I want [feature]..." and often imply solutions)
- Feature requests or specifications
- Step-by-step process documentation

They are living documents — never truly finished — and should be updated as personas and market problems evolve.

---

## Who Owns This Activity?

**Primary:** Product Manager (has market context and NIHITO research)  
**May also own:** Product Owner, Product Marketing Manager

**Stakeholders who inform use scenarios:**
- Designers
- Developers
- Customer experience / support teams
- Analysts
- Executives
- External customers and evaluators (for NIHITO grounding)

---

## Workflow

### Step 1: Confirm Prerequisites

Before writing use scenarios, verify:
- [ ] User Personas exist and are market-validated
- [ ] Market Problems have been identified and prioritized (ideally from NIHITO interviews)
- [ ] Requirements (at least a draft) exist to expand upon

If these are missing, pause and help the user address upstream activities first.

### Step 2: Select Persona + Problem Pair

Each use scenario starts from **one persona** facing **one problem**. Ask:
- Which user persona does this scenario describe?
- What specific requirement or problem are we expanding?
- How frequently does this persona encounter this problem?

### Step 3: Draft the Narrative

Write a short story (2–6 sentences typically; longer for complex scenarios) that:
1. Introduces the persona briefly in their real-world context
2. Describes the situation that surfaces the problem
3. Shows what they try to do or what happens
4. Conveys the frustration, friction, or consequence
5. Ends at the problem — never at a solution

**Core rule:** If the word "should," a feature name, a UI element, or a proposed action appears — the scenario has crossed into solution territory. Remove it.

### Step 4: Write Multiple Scenarios Per Persona/Problem

A single requirement can yield 2–4 use scenarios, each illuminating a different facet of the problem or a different triggering context. Depth creates empathy and helps teams avoid building solutions that only address one angle.

### Step 5: Validate

Review each scenario against the quality checklist (see references/quality-checklist.md). Key questions:
- Does it focus on exactly one persona?
- Does it contain exactly one problem?
- Is it solution-free?
- Is it grounded in real market observation (NIHITO), not assumed?
- Does it help a designer, developer, or QA engineer understand *why* this matters?

### Step 6: Integrate with Requirements

Use scenarios are **one component of requirements** — they provide context, not replacement. Link each scenario explicitly to its parent requirement so the development team can trace problems to decisions.

---

## Writing Quality Standards

**Do:**
- Write in third-person narrative ("Maria opens her laptop...")
- Use the persona's name and context from the Persona document
- Include frequency/timing details ("every Monday morning," "quarterly," "at the point of sale")
- Convey emotional stakes — anxiety, frustration, confusion, risk
- Keep it specific enough to be vivid; avoid generalities

**Don't:**
- Name product features, UI elements, or system components
- Use "should," "could," "would allow," or "needs a way to"
- Combine multiple personas in one scenario
- Combine multiple problems in one scenario
- Write in first person
- Prescribe any solution, workaround, or resolution

---

## Common Pitfalls

| Pitfall | Example (Bad) | Fix |
|---|---|---|
| Solution creep | "...she wishes the app had a filter" | End at the frustration, not the wish |
| Compound problems | "...she can't find classes AND can't pay tuition" | Split into two separate scenarios |
| Multiple personas | "Jessica and her advisor both struggle to..." | One persona per scenario |
| Vague context | "Sometimes users have trouble logging in" | Add who, when, where, how often |
| Internal perspective | "Our system doesn't support bulk exports" | Reframe as the user's experience |
| Assumed (not observed) | Invented scenarios not grounded in NIHITO | Validate with real market interviews |

---

## Adjacent Framework Activities

- **User Personas** → must exist before writing; use scenario personas come from here
- **Market Problems** → the source problems that use scenarios contextualize
- **Requirements** → use scenarios are a component of; link explicitly
- **Buyer Experience** → use scenarios complement the buyer's journey with user-side depth
- **Buyer Personas** → distinct from User Personas; some scenarios may span both

---

## Output Formats

When helping a user produce use scenarios, default to the template in `templates/use-scenario-template.md`. Offer both:
1. **Single scenario** — one persona, one problem narrative
2. **Scenario set** — 2–4 scenarios for the same persona/requirement, showing different contexts

For reviews/critiques, use the quality checklist in `references/quality-checklist.md`.

---

## Reference Files

- `references/quality-checklist.md` — Checklist for validating a use scenario
- `references/examples-library.md` — Annotated examples across multiple industries
- `templates/use-scenario-template.md` — Blank template with prompts
