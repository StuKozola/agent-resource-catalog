---
name: pragmatic-requirements
description: "Guide product managers through the Requirements activity from the Pragmatic Framework. Helps teams articulate and prioritize personas and their problems to produce a Market Requirements Document (MRD). Use whenever the user mentions market requirements, writing an MRD, defining what to build based on market problems, prioritizing persona problems for development, writing use scenarios in a Pragmatic context, translating market problems into requirements for engineering, the difference between requirements and specifications, or Pragmatic Framework Planning category work. Also trigger for structuring requirements documents, prioritizing features based on market evidence, communicating market needs to dev teams, writing problem-based requirements, or bridging customer insights and product development."
---

# Pragmatic Requirements Skill

## Context: Where Requirements Fits

Requirements is an activity in the **Planning** category of the Pragmatic Framework. The Pragmatic Institute defines it as:

> Articulate and prioritize personas and their problems so that the appropriate products can be built.

Requirements sits at the critical handoff point between strategy and execution. It translates upstream market knowledge into guidance that development teams can act on. The primary output is the **Market Requirements Document (MRD)** — a prioritized list of persona problems that tells the team *what* to solve without prescribing *how* to solve it.

### Relationship to Adjacent Activities

**Feeds into Requirements (upstream inputs):**
- **Market Problems** — validated, pervasive problems from NIHITO interviews
- **Buyer Personas** — archetypical buyers involved in purchase decisions
- **User Personas** — archetypical users of the product
- **Win/Loss Analysis** — reasons evaluators bought or didn't buy
- **Positioning** — how the product solves market problems (provides framing context)
- **Business Plan** — financial model and investment thesis that constrains scope

**Requirements feeds (downstream consumers):**
- **Use Scenarios** — stories that put requirements in context (Use Scenarios are a *component* of requirements)
- **Product Roadmap** — phases of deliverables informed by prioritized requirements
- **Development / Product Architects** — who write functional and technical specifications based on requirements
- **QA / Testing** — who build test plans to verify that problems were solved

### The Cardinal Rule: Requirements ≠ Specifications

This is the single most important principle in Pragmatic requirements work. A requirement describes the *problem*. A specification describes the *solution*. Product managers own requirements; product architects and developers own specifications.

When these get combined into "ReqSpecs" — part problem, part implementation — dysfunction follows. Developers complain they can't program to marketing-flavored specs, and product managers end up in design meetings sharing blame for poor design instead of gathering market knowledge.

The clean separation:
- **Product Manager** → finds and quantifies market problems, articulates them as requirements
- **Product Architect/Designer** → writes a functional specification describing the approach to solving the problem
- **Product Developer** → creates a technical specification for implementation

## Workflow Router

Determine the user's situation and route to the appropriate phase. Read the relevant reference file before proceeding.

**"I need to write requirements / an MRD from scratch"**
→ Start at Phase 1. Read `references/gathering-inputs.md` then `references/writing-requirements.md`

**"I have market problems and personas — help me turn them into requirements"**
→ Start at Phase 2. Read `references/writing-requirements.md`

**"I have a draft MRD — help me prioritize"**
→ Start at Phase 3. Read `references/prioritization-guide.md`

**"I need to produce the final MRD document"**
→ Start at Phase 4. Read `templates/mrd-template.md`

**"I need to communicate requirements to my dev team / work with agile"**
→ Read `references/dev-handoff-and-agile.md`

**"What's the difference between an MRD and PRD?" or conceptual questions**
→ Answer from the Key Concepts section below, supplemented by relevant reference files

## Key Concepts

### What Is a Market Requirements Document?

The MRD is a prioritized list of problems for target personas. It serves as a bridge between customer needs and development solutions. Its contents include:
- Persona definitions (both buyer and user personas)
- Phases of deliverables (tied to the product roadmap)
- Requirements: problems with use scenarios and frequency

The MRD is distinct from a Product Requirements Document (PRD). The MRD focuses on the "why" — identifying and prioritizing market problems. The PRD focuses on the "how" — translating those problems into features and technical specifications. Product managers write MRDs; designers, developers, and QA consume PRDs.

### The Story-Based Requirement Format

The Pragmatic preferred format for a requirement is a **use scenario**:

**[Persona] has this [problem] with [frequency]**

Example: "Sarah, the college student, needs to pay her tuition each semester using multiple credit cards."

- "Sarah" is the persona
- "pay tuition using multiple credit cards" is the problem
- "each semester" reveals the frequency

Notice: no proposed solution. The story puts the designer in the customer's chair, seeing the problem from their point of view.

### Requirement Types

While the story format is primary, well-rounded requirements also account for:

- **Functional** — observable capabilities the persona needs to complete their goals
- **Performance** — capacity, speed, concurrency characteristics
- **Constraints** — conditions that legitimately limit the design
- **Interface** — defined interactions with hardware/software components
- **Security** — compliance with mandates and customer privacy

Software vendors should also consider: standardization, certification, installation, implementation, customization, localization, documentation, and education requirements.

### The Three Artifacts

Requirements exist within a set of interrelated planning artifacts:

1. **Business Plan** — the business of the product (market research, win/loss results, market definition, financial plan)
2. **Product Roadmap** — phases of deliverables over the next 18-36 months
3. **Market Requirements Document** — the prioritized problems to be addressed in the next release

### Requirements Management Is Ongoing

Requirements management is not a one-time document. Product managers should continuously refine requirements by driving customer insights into the organization, always thinking at least one product generation ahead. This ongoing refinement pays dividends when it is time to launch a new development effort and prevents the common failure of delivering the PRD after development has already started.

## Phases Overview

### Phase 1: Gather Upstream Inputs
Collect and organize the market knowledge that feeds requirements: validated market problems, persona definitions, win/loss findings, competitive landscape, and business plan constraints.

### Phase 2: Write Requirements
Transform market problems into well-structured, implementation-free requirements using the persona + problem + frequency format. Apply the SMART criteria.

### Phase 3: Prioritize Requirements
Rank requirements using evidence-based scoring to determine what goes into the next release versus future releases.

### Phase 4: Assemble the MRD
Compile the prioritized requirements, persona profiles, and use scenarios into the Market Requirements Document.

### Phase 5: Hand Off and Iterate
Communicate requirements to development, support the transition to specifications, and manage requirements through the agile/development cycle.

## Common Pitfalls

1. **Writing solutions instead of problems** — The requirement should never prescribe how the problem is solved. If you find yourself describing UI elements, algorithms, or architecture, you've crossed into specification territory.

2. **Bloated, unreadable documents** — An MRD that reads like parliamentary committee minutes fails its audience. Requirements should be short (one to two paragraphs each, never more than a page). Peripheral information like interview notes should be linked, not embedded.

3. **Single static document** — The MRD should be a living document that can be sliced for different audiences: executives see top-level priorities, development groups see categorized requirements relevant to their area, customers see a sanitized view of direction.

4. **Letting sales escalations drive the product** — Without good requirements management, account managers lose confidence that their customer needs are being heard, and escalation politics take over. Visible requirements management creates transparency and trust.

5. **No contact information for real users** — Provide two or three potential users' contact details so designers and developers can get real insight directly, without the product manager being a bottleneck.

6. **Confusing buyer and user personas** — Buyers have one set of requirements (concerned with value, ROI); users have another (concerned with capabilities, usability). For most technology products, buyers and users are different people.

## Formatting Guidance

When producing any requirements-related document:
- Write requirements in the words of the persona, using business or personal terms, not technical jargon
- Keep individual requirements short — one to two paragraphs, never more than a page
- Use the [Persona] + [Problem] + [Frequency] story format as the primary structure
- Separate requirements from specifications rigorously
- Include a prioritization score alongside each requirement
- Provide persona contact information for development team access
- Structure the MRD so it can be filtered by audience (executives, dev teams, customers)
