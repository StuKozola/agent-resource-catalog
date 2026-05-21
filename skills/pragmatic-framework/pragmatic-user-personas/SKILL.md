---
name: pragmatic-user-personas
description: "Guide teams through the User Personas activity from the Pragmatic Marketing Framework. Helps product teams define archetypical users of their products using Pragmatic Institute methodology. Use whenever the user mentions user personas, creating personas, archetypical users, user research for persona development, persona discovery, provisional or refined personas, user goals and behaviors, empathy mapping, persona socialization, persona-driven requirements, or Pragmatic Framework Planning activities. Also trigger for questions about user vs buyer persona differences, interviewing users for personas, prioritizing personas, keeping personas alive across teams, or using personas to drive product decisions. Covers the full workflow: research planning, user interviews, contextual inquiry, empathy mapping, persona synthesis, classification (primary/secondary/negative), and organizational socialization."
---

# Pragmatic User Personas Skill

## Context: Where User Personas Fits

User Personas is an activity in the **Planning** category of the Pragmatic Framework (formerly Pragmatic Marketing Framework). The Pragmatic Institute defines it as:

> Define the archetypical users of your products or services.

User Personas sits alongside Buyer Personas, Requirements, Use Scenarios, and Positioning in the Planning category. It is a bridge between upstream market knowledge (Market Problems, Market Definition, Win/Loss Analysis) and downstream execution (Requirements, Use Scenarios, product design and development). The Design course at Pragmatic Institute covers User Personas as a core competency, emphasizing a human-centered approach to understanding users.

### User Personas vs. Buyer Personas

The Pragmatic Framework explicitly separates User Personas from Buyer Personas because the person who uses a product is often not the same person who buys it:

- **User Persona** — The archetypical person who interacts with the product day-to-day. Defined by goals, behaviors, attitudes, environment, skills, and pain points related to product usage.
- **Buyer Persona** — The archetypical person involved in the purchasing decision. Defined by buying criteria, decision-making role (economic buyer, functional buyer, technical buyer), and the buyer's journey.

A single person can be both a user and a buyer, but the lenses are different. This skill addresses the User Persona lens exclusively.

### Persona Types (Pragmatic Taxonomy)

The Pragmatic Framework recognizes four persona types:

1. **Primary Persona** — The main user of the product or interface. Product decisions prioritize this persona's needs above all others.
2. **Secondary Persona** — Another user type whose needs are accommodated as long as the primary persona's experience is not compromised.
3. **Negative Persona** — A user type for whom you explicitly will NOT add features. Including a negative persona prevents scope creep and keeps the product focused.
4. **Buyer Persona** — The purchaser (handled by the separate Buyer Personas activity).

## Key Principles

1. **Goals, attitudes, and behaviors over demographics** — Pragmatic Institute emphasizes that age and gender matter far less than what users are trying to accomplish, how they feel about it, and how they behave. Demographics may refine a persona, but goals define it.
2. **Grounded in research, not assumptions** — A valid persona must be discovered through interviewing actual users and company employees exposed to users. Personas should represent observed patterns, not imagined archetypes.
3. **Outside-in thinking** — Pragmatic Rule #2: the answer is not in the building. Persona discovery requires going out and talking to real users in their real environments.
4. **Personas must be lifelike** — You know you have a valid persona when you could imagine working alongside them, encountering them while shopping, or recognizing them at a user conference.
5. **Empathy is the mechanism** — Personas work because people respond to individual stories with more empathy than they do to statistics. A well-crafted persona lets developers, designers, and marketers put themselves in the user's shoes.
6. **Only include what impacts design** — Persona details should be information that directly affects product design and development decisions. Extraneous details dilute focus.

## Workflow Overview

The User Personas activity follows a four-phase workflow. Route to the appropriate reference guide based on where the user is:

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

Before creating personas, gather upstream Pragmatic Framework artifacts:

**Required inputs:**
- Market Problems documentation (validated problems, urgency, pervasiveness)
- Market Definition (target segments, segment profiles)
- Any existing customer data, support logs, or usage analytics

**Helpful inputs:**
- Win/Loss Analysis findings (who evaluated, why they chose or didn't)
- Competitive Landscape (how users interact with alternatives)
- Asset Assessment (technical constraints that shape user experience)

**If upstream artifacts are incomplete:** Start with provisional personas based on available knowledge and stakeholder interviews, then validate through user research. Read `references/research-planning.md` for detailed guidance on planning the research effort.

## Phase 2: Conduct User Research

User persona discovery requires talking to real users. The research methods include:

- **One-on-one user interviews** (primary method) — Deep conversations about goals, workflows, frustrations, and environment
- **Contextual inquiry** — Observing users in their natural environment while they use the product or workarounds
- **Empathy mapping** — Structuring observations into Says/Thinks/Does/Feels quadrants
- **Usage analytics** — Quantitative data to validate behavioral patterns observed in qualitative research
- **Support and feedback analysis** — Mining existing data for recurring themes

Read `references/user-research-guide.md` for the complete research methodology including interview scripts, observation techniques, and empathy mapping instructions.

## Phase 3: Synthesize & Build Personas

Pattern analysis across research inputs to create persona documents:

1. **Identify behavioral clusters** — Group users by shared goals, behaviors, and attitudes (not demographics)
2. **Create provisional personas** — Draft initial persona hypotheses using the `templates/provisional-persona.md` template
3. **Validate and refine** — Test provisional personas against additional data; refine into complete personas using `templates/refined-persona.md`
4. **Classify persona types** — Designate primary, secondary, and negative personas
5. **Prioritize** — Determine which personas get design priority based on strategic alignment with Market Definition and Market Problems

Read `references/persona-creation.md` for the detailed synthesis methodology.

## Phase 4: Socialize & Activate

A persona that sits in a document is a dead persona. Pragmatic Institute emphasizes that personas must become part of the organizational vocabulary:

- Share across product management, development, marketing, sales, support, HR, and training
- Reference personas by name in meetings, requirements, and design reviews
- Use physical or digital representations (cardboard cutouts, posters, Slack channels named after personas)
- Keep personas alive by updating them as new research emerges
- Use personas to drive Requirements and Use Scenarios (downstream Pragmatic activities)

Read `references/socialization-activation.md` for strategies to embed personas in organizational culture.

## Downstream Connections

Completed User Personas feed directly into these Pragmatic Framework activities:

- **Requirements** — Articulate and prioritize personas and their problems so appropriate products get built
- **Use Scenarios** — Illustrate market problems as stories that put the problem in the persona's context
- **Positioning** — Create messages focused on each key persona
- **Buyer Experience** — Understand the buyer's journey for the segments and personas identified
- **Product Roadmap** — Prioritize features based on persona needs and strategic importance

## Common Anti-Patterns

When helping users, watch for and flag these mistakes:

1. **Demographic-first personas** — Starting with age, gender, income instead of goals and behaviors
2. **Too many personas** — More than 3-5 personas dilutes focus; consolidate or use negative personas to exclude
3. **Assumption-based personas** — Creating personas from internal opinions without user research
4. **Static personas** — Treating personas as one-time deliverables instead of living documents
5. **Orphaned personas** — Creating personas that never get socialized or referenced in decisions
6. **Conflating users and buyers** — Mixing purchasing criteria into user personas
