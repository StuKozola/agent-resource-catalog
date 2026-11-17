---
name: pragmatic-requirements
description: "Guide product managers through the Requirements focus area of the Pragmatic Framework (now including Use Scenarios): describing the market problem the team must solve, for whom, and how often, with the context, intent, constraints and priorities needed to build the right solution. Use whenever the user mentions market requirements, writing an MRD, problem-based requirements, use scenarios, problem narratives, user problem stories, requirements context, translating market problems into requirements for engineering, requirements vs. specifications, use scenarios vs. user stories vs. use cases, prioritizing persona problems for development, or writing requirements that people and AI coding or design tools can act on. Also trigger for structuring requirements documents, prioritizing features based on market evidence, handing requirements to dev teams or agile backlogs, or reviewing whether requirements or scenarios are solution-free."
---

# Requirements — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Planning — *What are we building, for whom, and why?*
- **Focus-area question:** *What problem must the team solve, for whom, and how often does it happen?*
- **Position:** Below the bar (product- and team-focused)
- **Other focus areas in this category:** Positioning, Buyer Journey, Buyer Personas, User Personas, Ideation, Stakeholder Management
- **Formerly:** Requirements and Use Scenarios (Use Scenarios is now part of Requirements)

Requirements give development and design teams the context, intent, constraints and priorities they need to design and build the right solution. A good requirement describes the market problem — who has it, what it is and how often it happens — without prescribing a solution. That leaves the team free to innovate with the market context in hand. Product managers usually own requirements, for new products and updates alike. Write them specifically enough that both people and the AI tools your team uses can act on them.

The primary output is the **Market Requirements Document (MRD)**: a prioritized list of persona problems, each expanded with use scenarios, that tells the team *what* to solve and *why*, not *how*. The Pragmatic Institute Build course covers Requirements.

### Relationship to Other Focus Areas

**Inputs:**
- **Market Problems** (Market, `pragmatic-market-problems`) — validated, pervasive problems from NIHITO interviews
- **User Personas** and **Buyer Personas** (Planning, `pragmatic-user-personas`, `pragmatic-buyer-personas`)
- **Win/Loss Analysis** (Market) — reasons evaluators bought or didn't
- **Positioning** (Planning, `pragmatic-positioning`) — framing context
- **Business Plan** (Business, `pragmatic-business-plan`) — investment case that constrains scope
- **Ideation** (Planning, `pragmatic-ideation`) — concepts and experiments that earned evidence
- **Exceptions** and **Escalations** (Operations) — repeated one-offs and critical issues that point to a missing capability

**Outputs:**
- **Product Roadmap** (Focus, `pragmatic-product-roadmap`) — outcomes sequenced from prioritized requirements
- **Development / product architects** — functional and technical specifications
- **QA / testing** — test plans that verify the problem was solved
- **Stakeholder Management** (Planning, `pragmatic-stakeholder-management`) — shared clarity on priorities and trade-offs

### The Cardinal Rule: Requirements ≠ Specifications

A requirement describes the *problem*. A specification describes the *solution*. Product managers own requirements; architects, designers and developers own specifications. Combined "ReqSpecs" — part problem, part implementation — cause dysfunction: developers can't build to marketing-flavored specs, and product managers end up in design meetings instead of in the market.

- **Product Manager** → finds and quantifies market problems; writes them as requirements
- **Product Architect/Designer** → writes a functional specification describing the approach
- **Product Developer** → creates the technical specification for implementation

## Workflow Router

Read the relevant reference file before proceeding.

| User says | Go to |
|---|---|
| "Write requirements / an MRD from scratch" | Phase 1: `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/gathering-inputs.md`, then `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/writing-requirements.md` |
| "I have market problems and personas — turn them into requirements" | Phase 2: `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/writing-requirements.md` |
| "Write / review use scenarios" | Use Scenarios section below; `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/templates/use-scenario-template.md`, `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/use-scenario-examples.md`, `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/use-scenario-quality-checklist.md` |
| "Help me prioritize my draft MRD" | Phase 3: `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/prioritization-guide.md` |
| "Produce the final MRD" | Phase 4: `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/templates/mrd-template.md` |
| "Hand off to dev / work with agile / feed AI tools" | Phase 5: `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/dev-handoff-and-agile.md` |
| "MRD vs. PRD?" or other concept questions | Key Concepts below |

## Key Concepts

### What a requirement contains

- **Who** has the problem (a named persona, not "the user")
- **What** the problem is, in the persona's terms
- **How often** it happens (frequency establishes urgency and impact)
- **Context** — the situation and the market evidence
- **Intent** — the outcome the persona needs
- **Constraints** — legitimate limits on the solution
- **Priority** — rank and rationale

The core format: **[Persona] has this [problem] with [frequency].**
Example: "Sarah, the college student, needs to pay her tuition each semester using multiple credit cards." No proposed solution; the reader sits in the customer's chair.

### Writing for people and AI tools

Requirements now go to AI coding, design and test tools as well as to people. Anything left implicit will be guessed. Name the persona and situation, give frequencies and volumes as numbers, state constraints and "solved when..." signals explicitly, and define domain terms. Being specific about the problem is not the same as prescribing the solution. See `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/writing-requirements.md`.

### Requirement types

Beyond the story format, account for: **functional** (capabilities the persona needs), **performance** (capacity, speed, concurrency), **constraints**, **interface** (interactions with other hardware/software), and **security/privacy**. Software vendors should also consider standardization, certification, installation, implementation, customization, localization, documentation and education.

### MRD vs. PRD

The MRD focuses on the "why": which market problems, for whom, in what priority. A PRD (or specification) focuses on the "how": features and technical design. Product managers write MRDs; designers, developers and QA work from specifications.

### The three planning artifacts

1. **Business Plan** — the business case for the product
2. **Product Roadmap** — outcomes in sequence over the coming quarters and years
3. **MRD** — the prioritized problems for the next release

### Requirements management is ongoing

Requirements are a living set, not a one-time document. Keep refining them as market insight arrives, think at least one product generation ahead, and you won't be writing the PRD after development has already started.

## Use Scenarios

Use scenarios (formerly their own focus area) are one component of requirements. A use scenario is a short narrative that shows one persona hitting one problem in a real situation: who, what, when/where and why it matters. It gives designers, developers and QA the problem context behind a requirement.

Use scenarios are **not** use cases (system interactions), user stories ("As a [role], I want [feature]..." often implies a solution), feature requests or process documentation.

**Workflow:**
1. **Confirm prerequisites** — validated User Personas, prioritized Market Problems, and at least a draft requirement to expand.
2. **Pick one persona + one problem** — and how often the persona hits it.
3. **Draft the narrative** — 2–6 sentences, third person: introduce the persona in context, the situation that surfaces the problem, what happens, the consequence. End at the problem, never at a solution.
4. **Write 2–4 scenarios per requirement** where useful, each showing a different trigger or facet.
5. **Validate** with `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/use-scenario-quality-checklist.md`: one persona, one problem, solution-free, grounded in real market observation, clear on why it matters.
6. **Link to the parent requirement** in the MRD so teams can trace problems to decisions.

**Solution-creep test:** if "should," "could," "would allow," "needs a way to," a feature name or a UI element appears, the scenario has crossed into solution territory. Remove it.

Template: `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/templates/use-scenario-template.md`. Annotated examples: `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/use-scenario-examples.md`.

## Phases Overview

1. **Gather upstream inputs** — market problems, personas, win/loss findings, competitive landscape, business plan constraints.
2. **Write requirements** — persona + problem + frequency, with context, intent, constraints; apply the SMART test.
3. **Prioritize** — evidence-based scoring for the next release vs. later.
4. **Assemble the MRD** — prioritized requirements, persona profiles and use scenarios.
5. **Hand off and iterate** — support the move to specifications, manage requirements through agile delivery, and check after release that the problem was solved.

## Common Pitfalls

1. **Writing solutions instead of problems** — UI elements, algorithms or architecture mean you've crossed into specification.
2. **Vague requirements** — "the user," no frequency, no constraints. People and AI tools will fill gaps with guesses.
3. **Bloated documents** — Keep each requirement to one or two paragraphs; link interview notes rather than embedding them.
4. **Single static document** — Make the MRD sliceable: executives see priorities, dev groups see their area, customers see a sanitized direction.
5. **Letting sales escalations drive the product** — Visible requirements management builds trust and takes the politics out.
6. **No path to real users** — Give designers and developers two or three user contacts so the PM isn't a bottleneck.
7. **Confusing buyer and user personas** — Buyers care about value and risk; users care about capability and usability.

## Formatting Guidance

- Write in the persona's words, not technical jargon
- Keep individual requirements short; one requirement, one problem
- Use the [Persona] + [Problem] + [Frequency] structure, plus context, intent, constraints and priority
- Separate requirements from specifications rigorously
- Include a prioritization score with each requirement
- Structure the MRD so it can be filtered by audience

## Using AI in this focus area

- Turn interview notes and market-problem research into draft requirements and use scenarios in the standard format.
- Check drafts for solution creep, missing personas, missing frequency and undefined terms.
- Generate test scenarios and acceptance signals from requirements for QA.

Check AI drafts against real market evidence; a well-formed requirement for a problem nobody has is still wrong (NIHITO still applies). Keep sensitive customer, deal and company data out of tools not approved for it. The team, not the tool, owns the priorities.

## Reference Files

- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/gathering-inputs.md` — Phase 1: collecting and checking upstream inputs
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/writing-requirements.md` — Phase 2: writing problem-based requirements, for people and AI tools
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/prioritization-guide.md` — Phase 3: evidence-based scoring
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/dev-handoff-and-agile.md` — Phase 5: handoff, agile, closing the loop
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/use-scenario-examples.md` — Annotated use scenario examples
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/references/use-scenario-quality-checklist.md` — Use scenario review checklist
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/templates/mrd-template.md` — Market Requirements Document template
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-requirements/templates/use-scenario-template.md` — Use scenario template
