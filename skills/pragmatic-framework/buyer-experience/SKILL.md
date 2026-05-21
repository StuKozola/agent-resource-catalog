---
name: buyer-experience
description: >
  Guides creation of Buyer Experience documentation aligned with the Pragmatic Institute Framework.
  The Buyer Experience activity involves researching and documenting how target buyer personas
  navigate their purchasing process — from problem recognition through vendor selection — and
  identifying the barriers, friction points, and decision criteria they encounter along the way.
  Use this skill whenever the user mentions buyer experience, buyer journey mapping, buying process
  documentation, purchase process analysis, buyer journey stages, buying barriers, evaluation
  process mapping, or any Pragmatic Framework planning activity related to how buyers buy.
  Also trigger when the user asks about documenting how customers evaluate and select products,
  mapping the path to purchase, understanding buyer decision-making steps, or creating buying
  process documentation. This skill applies to B2B and B2C contexts but is especially suited
  to B2B technology product marketing where multiple stakeholders and complex evaluation cycles
  are common.
---

# Buyer Experience — Pragmatic Framework Skill

## What This Skill Does

This skill helps you produce **Buyer Experience documentation** as defined by the Pragmatic Institute Framework. The Buyer Experience activity lives in the **Planning** category of the framework and is defined as:

> Research and document the buying process your target personas use to select a product. Understand the barriers that buyers encounter during their selection process.

The output is a structured document that product management, product marketing, and sales teams can use to align go-to-market efforts with how buyers actually buy — not how the company thinks they buy.

## Context Within the Pragmatic Framework

Buyer Experience is one of 37 activities across 7 categories (Market, Focus, Business, Planning, Programs, Enablement, Support). It sits in **Planning** alongside Positioning, Buyer Personas, User Personas, Use Scenarios, and Stakeholder Communications.

**Key dependencies (inputs to Buyer Experience):**
- **Buyer Personas** — You need defined buyer archetypes before you can map their journey. If the user hasn't defined personas yet, prompt them to do so or help them sketch lightweight personas as a starting point.
- **Win/Loss Analysis** — Post-decision interviews with recent evaluators are the richest source of buying process data. Reference these if available.
- **Market Problems** — Understanding which urgent, pervasive problems drive buyers into an evaluation cycle.
- **Competitive Landscape** — Knowing what alternatives buyers consider during evaluation.

**Key outputs (what Buyer Experience feeds):**
- **Positioning** — Messages must align to what buyers care about at each stage.
- **Marketing Plan** — Programs and content mapped to journey stages.
- **Sales Tools & Collateral** — Assets that match the buying process, not the selling process.
- **Launch Plan** — Go-to-market sequenced to the buyer's timeline.

## How to Gather Buyer Experience Data

The gold standard is **interviews with recent evaluators** — people who have recently completed a buying decision (whether they chose you or a competitor). This is closely related to win/loss analysis but focused specifically on the *process* rather than the *outcome*.

### Who to Interview
- Recent buyers (won deals) — 2 to 4 weeks post-purchase, before they shift to "user" mindset
- Recent non-buyers (lost deals) — same timing window
- Prospects who went "no decision" — they abandoned the process entirely, which reveals barriers
- Aim for people in different buying roles: economic buyer, functional/end-user buyer, technical buyer, champion/evaluator

### What to Ask
- What triggered the evaluation? What problem were you trying to solve?
- Who was involved in the decision? What were their roles and concerns?
- What steps did you go through from recognizing the need to making a final decision?
- Where did you look for information at each stage? What sources did you trust?
- What barriers or friction did you encounter during the process?
- What criteria mattered most in comparing options?
- How long did the process take? Were there stalls or delays? Why?
- What would have made the process easier?

### Supplementary Data Sources
- CRM data and deal stage analysis
- Website analytics (content consumption patterns by stage)
- Sales team debrief notes
- Customer advisory board feedback
- Industry analyst reports on buying behavior
- Third-party review sites (G2, TrustRadius, Gartner Peer Insights)

## Document Structure

When creating a Buyer Experience document, use the following structure. Read the reference file at `references/document-template.md` for the full template with field-level guidance.

### Required Sections

1. **Executive Summary** — Who this document covers, why it was created, and the key insight
2. **Buyer Persona Summary** — Brief recap of the persona(s) this journey maps to
3. **Buying Trigger** — What initiates the buying process (pain event, mandate, contract renewal, etc.)
4. **Journey Stages** — The core of the document. Map each stage the buyer goes through:
   - Stage name and description
   - Buyer's goals and questions at this stage
   - Information sources and trusted channels
   - Key activities the buyer performs
   - Stakeholders involved and their concerns
   - Barriers and friction points encountered
   - Content and touchpoints that influence decisions
   - Typical duration
5. **Decision Criteria** — What factors buyers weigh when comparing options, ranked by importance
6. **Barriers and Friction Points** — Consolidated view of obstacles across the journey
7. **Implications and Recommendations** — What this means for positioning, content, sales process, and product
8. **Methodology** — How the data was gathered (interview count, timeframe, segments)

### Journey Stage Framework

Most B2B buying journeys follow a variation of these stages, though the names and boundaries will vary by market:

| Stage | Buyer's Focus | Typical Activities |
|-------|--------------|-------------------|
| **Problem Recognition** | "We have a problem worth solving" | Internal discussion, pain quantification, building a business case |
| **Solution Exploration** | "What kinds of solutions exist?" | Web research, peer conversations, analyst reports, content consumption |
| **Requirements Building** | "What do we need?" | Cross-functional input, RFP/RFI creation, must-have vs. nice-to-have |
| **Vendor Evaluation** | "Who can deliver?" | Demos, trials, reference calls, proof of concept |
| **Consensus & Approval** | "Can we agree and get budget?" | Internal selling, risk mitigation, procurement/legal review |
| **Selection & Negotiation** | "Let's finalize the deal" | Contract negotiation, pricing discussion, implementation planning |

These stages are not always linear. Buyers frequently loop back, stall, or skip stages. Document the real journey, not an idealized funnel.

## Formatting and Output Guidance

- **Default output format**: Word document (.docx) using the docx skill if available, otherwise Markdown
- **Tone**: Professional, clear, actionable. Written for a cross-functional audience (product, marketing, sales, executives)
- **Length**: A thorough Buyer Experience document typically runs 8–15 pages. For a single persona in a well-understood market, 5–8 pages may suffice.
- **Visuals**: Include a journey map diagram when possible — a horizontal flow showing stages, with rows for buyer goals, activities, touchpoints, barriers, and emotions. Use Mermaid or an SVG diagram if creating in Markdown/HTML.
- If the user provides raw interview notes or win/loss data, synthesize it into the structured format rather than just reorganizing the raw notes.

## Common Pitfalls to Avoid

- **Mapping the sales process instead of the buying process.** The buyer's journey is not the mirror image of your pipeline stages. Buyers do significant work before they ever talk to sales.
- **Assuming a linear journey.** B2B buying is messy. Multiple stakeholders enter and exit at different stages. Document the reality.
- **Ignoring "no decision" outcomes.** A large percentage of B2B evaluations end without any purchase. Understanding why is as valuable as understanding wins and losses.
- **Focusing only on the champion.** Different buying roles (economic, technical, end-user) experience the journey differently and face different barriers.
- **Creating a document that lives on a shelf.** The Buyer Experience document should directly inform positioning, content strategy, sales enablement, and product decisions. End with concrete recommendations.
- **Conflating buyer experience with customer experience.** Buyer experience covers the path to purchase. Customer experience begins after the sale. They're related but distinct.

## Adapting to What the User Provides

The user may come to you with varying levels of input:

- **"I need a buyer experience document from scratch"** — Walk them through who their buyer personas are, what data they have (interviews, CRM data, sales feedback), and help them structure a research plan. Then build the document framework they can populate.
- **"Here are my interview notes / win-loss data"** — Synthesize the raw data into the structured Buyer Experience format. Look for patterns across interviews, especially around stages, barriers, and decision criteria.
- **"Help me map the buying process for [specific persona/market]"** — Build a journey map focused on that persona. Ask about their market context, typical deal size, and buying committee composition.
- **"Review / improve my existing buyer experience document"** — Evaluate against the structure above. Check for common pitfalls. Suggest gaps to fill.
- **"I need a buyer journey diagram"** — Create a visual journey map (Mermaid, SVG, or describe a layout). Include stages, touchpoints, barriers, and emotional states.

## Reference Files

- `references/document-template.md` — Full document template with field-level instructions and example content
- `references/interview-guide.md` — Question bank for buyer experience research interviews
