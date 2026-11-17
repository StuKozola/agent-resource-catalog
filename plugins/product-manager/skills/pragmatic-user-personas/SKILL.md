---
name: pragmatic-user-personas
description: "Guide teams through the User Personas focus area of the Pragmatic Framework (Pragmatic Institute): research-based profiles of the people who use the product, their workflows, needs, context and behavior. Use whenever the user mentions user personas, creating personas, archetypical users, user research for persona development, persona discovery, provisional or refined personas, user goals and behaviors, empathy mapping, persona socialization, persona-driven requirements, or 'who uses the product and what do they need to get done?'. Also trigger for user vs. buyer persona differences, interviewing users for personas, prioritizing personas (primary, secondary, negative), keeping personas alive across teams, or using personas to drive requirements, ideation, testing and adoption. Covers research planning through persona synthesis and socialization. For people who make or influence the purchase, use pragmatic-buyer-personas."
---

# User Personas — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Planning — *What are we building, for whom, and why?*
- **Focus-area question:** *Who uses the product, and what do they need to get done?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Positioning, Buyer Journey, Buyer Personas, Requirements, Ideation, Stakeholder Management

User personas profile the people who use the product. Users often don't make the purchase decision, but their workflows, needs, context and behavior decide whether the product succeeds. Personas condense user research into something the whole team can design and build against:

- **Developers** get clearer direction on who they are building for and why.
- **Testers** can simulate realistic scenarios instead of generic happy paths.
- **Product managers** can see how user behavior affects results such as adoption, retention and business outcomes.

User Personas bridges upstream market knowledge (Market Problems, Market Definition, Win/Loss Analysis) and downstream work (Requirements, Ideation, Adoption, product design and development). The Pragmatic Institute Design and Build courses both cover User Personas.

### User Personas vs. Buyer Personas

The person who uses a product is often not the person who buys it:

- **User Persona** — The archetypical person who works with the product. Defined by workflows, needs, context, behavior, goals, skills and pain points related to use.
- **Buyer Persona** — The archetypical person who makes or influences the purchase decision (functional, financial or technical buyer; sponsor; approver; influencer). See `pragmatic-buyer-personas`.

One person can be both, but the lenses differ. This skill covers the user lens only.

### Persona Types

1. **Primary Persona** — The main user of the product or interface. Product decisions prioritize this persona's needs.
2. **Secondary Persona** — Another user type whose needs are accommodated as long as the primary persona's experience is not compromised.
3. **Negative Persona** — A user type for whom you explicitly will NOT add features. Prevents scope creep and keeps the product focused.
4. **Buyer Persona** — The purchaser, handled in the Buyer Personas focus area.

## Key Principles

1. **Workflows, needs, context and behavior over demographics** — Age and gender matter far less than what users are trying to get done, where and how they work, and how they behave. Demographics may refine a persona; goals and behavior define it.
2. **Grounded in research, not assumptions** — Discover personas by interviewing and observing real users and the employees who work with them.
3. **Outside-in thinking** — The answer is not in the building (NIHITO). Go talk to users in their real environments.
4. **Lifelike** — You have a valid persona when you could imagine working alongside them or recognizing them at a user conference.
5. **Empathy is the mechanism** — People respond to individual stories more than statistics. A good persona lets developers, testers, designers and marketers step into the user's shoes.
6. **Only include what affects design** — Details that don't change product decisions dilute focus.

## Workflow Overview

Route to the right reference guide based on where the user is:

| Phase | What Happens | Reference Guide |
|-------|-------------|-----------------|
| **Phase 1: Gather Inputs & Plan Research** | Collect upstream artifacts, identify knowledge gaps, plan user research | `references/research-planning.md` |
| **Phase 2: Conduct User Research** | Interview users, observe environments, map empathy | `references/user-research-guide.md` |
| **Phase 3: Synthesize & Build Personas** | Analyze patterns, create provisional then refined personas | `references/persona-creation.md` |
| **Phase 4: Socialize & Activate** | Communicate personas across the org, embed in workflows | `references/socialization-activation.md` |

### Templates Available

| Template | Use For | Location |
|----------|---------|----------|
| Provisional User Persona | Early-stage persona with hypotheses to validate | `templates/provisional-persona.md` |
| Refined User Persona | Research-validated, complete persona document | `templates/refined-persona.md` |
| User Research Interview Guide | Structured interview script for persona discovery | `templates/interview-guide.md` |

## Phase 1: Gather Inputs & Plan Research

**Required inputs:**
- Market Problems (Market, `pragmatic-market-problems`): validated problems, urgency, pervasiveness
- Market Definition (Focus, `pragmatic-market-definition`): target segments, segment profiles
- Existing customer data, support logs or usage analytics

**Helpful inputs:**
- Win/Loss Analysis (Market): who evaluated, why they chose or didn't
- Competitive Landscape (Market): how users work with alternatives and workarounds
- Product Strategy (Market) and an inventory of existing assets: technical constraints that shape the user's experience

**If upstream artifacts are incomplete:** Start with provisional personas based on available knowledge and stakeholder interviews, then validate through user research. See `references/research-planning.md`.

## Phase 2: Conduct User Research

- **One-on-one user interviews** (primary method) — Goals, workflows, frustrations and environment
- **Contextual inquiry** — Observing users in their real environment, using the product or their workarounds
- **Empathy mapping** — Says/Thinks/Does/Feels
- **Usage analytics** — Quantitative checks on behavior patterns seen in interviews
- **Support and feedback analysis** — Recurring themes in existing data

See `references/user-research-guide.md` and `templates/interview-guide.md`.

## Phase 3: Synthesize & Build Personas

1. **Identify behavioral clusters** — Group users by shared workflows, goals and behaviors, not demographics
2. **Create provisional personas** — Use `templates/provisional-persona.md`
3. **Validate and refine** — Test against more data; complete with `templates/refined-persona.md`
4. **Classify persona types** — Primary, secondary and negative
5. **Prioritize** — Decide which personas get design priority, based on Market Definition and Market Problems

See `references/persona-creation.md`.

## Phase 4: Socialize & Activate

A persona that sits in a document is a dead persona. Make personas part of the team's vocabulary:

- Share across product, development, testing, design, marketing, sales, support and training
- Reference personas by name in meetings, requirements, test plans and design reviews
- Use visible reminders (posters, channels named after personas)
- Update personas as new research emerges

See `references/socialization-activation.md`.

## Connections to Other Focus Areas

- **Requirements** (Planning, `pragmatic-requirements`) — The "who" in every requirement and use scenario.
- **Ideation** (Planning, `pragmatic-ideation`) — Concepts and experiments start from persona problems and are tested with users who match the persona.
- **Adoption** (Enablement, `pragmatic-adoption`) — Define meaningful use, onboarding and training per persona; low adoption sends you back to the persona.
- **Positioning** (Planning, `pragmatic-positioning`) — How value is described for users who influence the decision.
- **Product Roadmap** (Focus, `pragmatic-product-roadmap`) — Prioritize outcomes by persona importance.

## Common Anti-Patterns

1. **Demographic-first personas** — Starting with age, gender, income instead of workflows and behavior
2. **Too many personas** — More than 3–5 dilutes focus; consolidate or use negative personas
3. **Assumption-based personas** — Built from internal opinion without user research
4. **Static personas** — One-time deliverables instead of living documents
5. **Orphaned personas** — Never socialized or referenced in decisions
6. **Conflating users and buyers** — Mixing purchasing criteria into user personas

## Using AI in this focus area

- Cluster interview transcripts, support tickets and usage data into candidate behavior patterns.
- Draft provisional personas and empathy maps from research notes for the team to validate.
- Generate persona-based test scenarios for testers and acceptance criteria for developers.

AI can summarize what users said; it can't observe them at work, so contextual inquiry still needs people. Check AI output against real user evidence (NIHITO still applies). Keep sensitive customer and company data out of tools not approved for it. The team, not the tool, decides which personas to prioritize.
