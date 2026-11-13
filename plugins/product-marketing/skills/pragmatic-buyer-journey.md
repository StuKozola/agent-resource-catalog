---
name: pragmatic-buyer-journey
description: >
  Guides mapping and documenting the Buyer Journey (formerly Buyer Experience) per the Pragmatic
  Framework (Pragmatic Institute): how buyers, sponsors and approvers move from recognizing a need
  to making a decision, including their questions, friction points and moments of influence.
  Use whenever the user mentions buyer journey, buyer journey mapping, buyer experience, buying
  process documentation, path to purchase, purchase process analysis, buying barriers, buying
  committee decision process, evaluation process mapping, or how buyers buy. Also trigger when
  leads aren't converting, deals stall, messaging falls flat, or the user wants to know how
  customers evaluate and select products, or how internal stakeholders approve and fund an
  internal product or platform. Suited to B2B technology with complex evaluation cycles and
  multiple stakeholders, and applies to B2C and internal products.
---

# Buyer Journey — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Planning — *What are we building, for whom, and why?*
- **Focus-area question:** *How do buyers move from a need to a decision?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Positioning, Buyer Personas, User Personas, Requirements, Ideation, Stakeholder Management
- **Formerly:** Buyer Experience

## What This Skill Does

The buyer journey maps how buyers, sponsors and approvers get from recognizing a need to making a decision. It captures the questions they ask at each step, where they hit friction, and the moments where something (a peer, a demo, a proof point, a price) changes their direction. The output is a document that product, marketing and sales teams use to line up go-to-market work with how buyers actually buy, not how the company assumes they buy.

### When to map the journey

- Leads aren't converting, or deals stall at the same stage.
- Messaging falls flat: buyers don't respond, or sales stops using it.
- "No decision" is a common outcome.
- Buyer preferences have shifted (new channels, new approvers, self-serve evaluation, procurement changes).
- Before a launch or a move into a new segment.

A documented journey helps you address objections, refine messaging and keep up with changing buyer preferences.

### Internal-product variant

For internal products and platforms, the "buyers" are the stakeholders who approve and fund the work: the sponsoring executive, budget owner, architecture or security review board, and the business units asked to adopt it. Map how they move from recognizing a need to approving funding or a rollout: what triggers the request, which reviews it must pass, who can block it, and what evidence persuades them. The same document structure works; replace "vendor evaluation" with "option review" (including build vs. buy and doing nothing) and "selection and negotiation" with "funding and rollout approval."

## Context Within the Pragmatic Framework

**Inputs to Buyer Journey:**
- **Buyer Personas** (Planning, `pragmatic-buyer-personas`) — You need defined buyers, sponsors and approvers before you can map their journey. If they don't exist yet, help sketch lightweight personas as a starting point.
- **Win/Loss Analysis** (Market, `pragmatic-win-loss-analysis`) — Interviews with recent evaluators are the richest source of buying process data.
- **Market Problems** (Market, `pragmatic-market-problems`) — Which urgent, pervasive problems drive buyers into an evaluation.
- **Competitive Landscape** (Market, `pragmatic-competitive-landscape`) — The alternatives buyers consider, including doing nothing.

**What Buyer Journey feeds:**
- **Positioning** (Planning, `pragmatic-positioning`) — What buyers care about at each stage.
- **Marketing Plan** and **Engagement** (Go-to-Market, `pragmatic-marketing-plan`, `pragmatic-engagement`) — Programs and content mapped to journey stages.
- **Assets** and **Content** (Enablement, `pragmatic-assets`, `pragmatic-content`) — Tools that match the buying process, not the selling process.
- **Launch** (Go-to-Market, `pragmatic-launch`) — Go-to-market sequenced to the buyer's timeline.

## How to Gather Buyer Journey Data

The gold standard is **interviews with recent evaluators**: people who recently made a buying decision, whether they chose you, a competitor or nothing. This overlaps with win/loss analysis but focuses on the *process* rather than the *outcome*. See `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buyer-journey/references/interview-guide.md`.

### Who to interview
- Recent buyers (won deals), 2–4 weeks after the decision, before they shift to a user mindset
- Recent non-buyers (lost deals), same window
- Prospects who went "no decision"; they reveal the barriers that stop a process
- People in different roles: functional, financial and technical buyers, sponsors, approvers (procurement, legal, security) and champions

### What to ask
- What triggered the evaluation? What problem were you trying to solve?
- Who was involved in the decision? Who sponsored it, and who had to approve it?
- What steps did you go through from recognizing the need to making a final decision?
- What questions did you need answered at each step? Where did you look, and which sources did you trust?
- What friction did you hit? Where did it stall, and why?
- What changed your mind or moved the decision forward?
- What criteria mattered most in comparing options?
- What would have made the process easier?

### Supplementary data sources
- CRM data and deal-stage analysis
- Website and product-trial analytics (content and feature use by stage)
- Sales team debrief notes
- Customer advisory board feedback
- Industry analyst reports on buying behavior
- Third-party review sites (G2, TrustRadius, Gartner Peer Insights)

## Document Structure

Read `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buyer-journey/references/document-template.md` for the full template with field-level guidance.

1. **Executive Summary** — Who this document covers, why it was created, and the key insight
2. **Buyer Persona Summary** — Brief recap of the buyers, sponsors and approvers this journey maps to
3. **Buying Trigger** — What starts the journey (pain event, mandate, contract renewal, etc.)
4. **Journey Stages** — The core of the document. For each stage:
   - Stage name and description
   - Buyer's goals and the questions they need answered
   - Information sources and trusted channels
   - Activities the buyer performs
   - Stakeholders involved (including sponsors and approvers) and their concerns
   - Friction points and stall indicators
   - Moments of influence: what moves the decision forward or changes its direction
   - Typical duration
5. **Decision Criteria** — What buyers weigh when comparing options, ranked, by role
6. **Barriers and Friction Points** — Consolidated view across the journey
7. **Buying Journey Map** — A visual summary
8. **Implications and Recommendations** — For positioning, messaging, content, sales process and product
9. **Methodology** — How the data was gathered (interview count, timeframe, segments)

### Journey stage framework

Most B2B journeys follow a variation of these stages; names and boundaries vary by market:

| Stage | Buyer's Focus | Typical Activities |
|-------|--------------|-------------------|
| **Problem Recognition** | "We have a problem worth solving" | Internal discussion, pain quantification, building a business case |
| **Solution Exploration** | "What kinds of solutions exist?" | Web research, peer conversations, analyst reports, content consumption |
| **Requirements Building** | "What do we need?" | Cross-functional input, RFP/RFI creation, must-have vs. nice-to-have |
| **Vendor Evaluation** | "Who can deliver?" | Demos, trials, reference calls, proof of concept |
| **Consensus & Approval** | "Can we agree and get budget?" | Internal selling to sponsors, risk review, procurement/legal/security approval |
| **Selection & Negotiation** | "Let's finalize the deal" | Contract negotiation, pricing discussion, implementation planning |

Stages are not always linear. Buyers loop back, stall or skip stages. Document the real journey, not an idealized funnel.

## Formatting and Output Guidance

- **Default output format**: Word document (.docx) using the docx skill if available, otherwise Markdown.
- **Tone**: Professional, clear, actionable, for a cross-functional audience.
- **Length**: Typically 8–15 pages; 5–8 for a single persona in a well-understood market.
- **Visuals**: Include a journey map: a horizontal flow of stages with rows for goals, questions, touchpoints, friction, moments of influence and emotional state. Use Mermaid or SVG in Markdown/HTML.
- If the user provides raw interview notes or win/loss data, synthesize patterns rather than reorganizing the notes.

## Common Pitfalls to Avoid

- **Mapping the sales process instead of the buying process.** Buyers do significant work before they ever talk to sales.
- **Assuming a linear journey.** Stakeholders enter and exit at different stages.
- **Ignoring "no decision" outcomes.** Understanding why evaluations die is as valuable as wins and losses.
- **Focusing only on the champion.** Sponsors, approvers and technical and financial buyers experience the journey differently and face different friction.
- **Creating a document that lives on a shelf.** End with concrete recommendations for positioning, content, sales and product.
- **Conflating the buyer journey with the customer experience after the sale.** Post-sale use and value belong to Adoption (Enablement), Customer Satisfaction and Retention (Go-to-Market) and Customer Value Realization (Operations).

## Adapting to What the User Provides

- **"I need a buyer journey from scratch"** — Confirm who the buyers, sponsors and approvers are, what data exists (interviews, CRM, sales feedback), and help structure a research plan. Then build the document framework.
- **"Here are my interview notes / win-loss data"** — Synthesize into the structure above, looking for patterns in stages, friction, moments of influence and decision criteria.
- **"Leads aren't converting / our messaging isn't landing"** — Start with where in the journey buyers drop out and what question they couldn't get answered there.
- **"Help me map the buying process for [persona/market]"** — Ask about market context, deal size and buying committee composition.
- **"Our internal platform can't get funded/adopted"** — Use the internal-product variant above.
- **"Review / improve my existing document"** — Evaluate against the structure and pitfalls; suggest gaps.
- **"I need a buyer journey diagram"** — Create a visual journey map with stages, touchpoints, friction and moments of influence.

## Using AI in this focus area

- Synthesize interview transcripts and win/loss notes into stage-by-stage patterns (questions, friction, moments of influence).
- Mine CRM stage data and call notes to find where deals stall.
- Draft the journey map and first-pass recommendations for the team to challenge.

AI can't replace talking to recent evaluators; it can only organize what they told you. Check its output against real market evidence (NIHITO still applies). Keep sensitive customer, deal and company data out of tools not approved for it. The team, not the tool, owns the conclusions.

## Reference Files

- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buyer-journey/references/document-template.md` — Full document template with field-level instructions and example content
- `https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-buyer-journey/references/interview-guide.md` — Question bank for buyer journey research interviews
