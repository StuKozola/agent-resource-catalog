---
name: pragmatic-buyer-personas
description: "Create buyer persona documents following the Pragmatic Framework (Pragmatic Institute). Use this skill whenever the user asks to create, define, develop or document buyer personas, buying committee profiles, or archetypical buyer profiles: the people who make or influence the purchase decision, including sponsors, approvers and influencers. Also trigger when the user mentions Pragmatic buyer personas, buyer archetypes, functional/financial/technical buyer profiles, economic buyer profiles, buying influences, decision authority, buyer success criteria, persona discovery, buyer profiling, or a Buyer Personas with AI workshop. Trigger even if the user just says 'persona' or 'buyer profile' in a purchase context. Covers B2B and B2C buyer personas and supports Positioning, Buyer Journey (formerly Buyer Experience) and Organizational Alignment, which depend on well-defined buyer personas. For people who use the product day to day, use pragmatic-user-personas."
---

# Buyer Personas — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Planning — *What are we building, for whom, and why?*
- **Focus-area question:** *Who makes or influences the purchase decision?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Positioning, Buyer Journey, User Personas, Requirements, Ideation, Stakeholder Management

## What this skill does

Buyer personas are research-based profiles of the people who make or influence the purchase decision: the buyers themselves plus the sponsors who champion the spend, the approvers who can say no (procurement, legal, security, finance), and the influencers whose opinion carries weight. Each persona describes that person's goals, concerns, authority and success criteria.

Personas make clear who you are targeting, keep internal teams focused on customer needs, and help prioritize features and marketing. Most organizations need only a **small set** of personas, based on their market and the people who make decisions in it.

**Buyer Personas vs. User Personas.** Buyers make or influence the purchase decision; they may never touch the product. Users work with the product, and their success decides whether it succeeds. Users belong in `pragmatic-user-personas`. In some sales the same person is both; profile both roles anyway.

## When to use this skill

- User asks to create or draft buyer personas or buying committee profiles
- User needs functional, financial or technical buyer profiles, or sponsor/approver profiles
- User wants to align sales and marketing around buyer understanding
- User is working on Positioning, Buyer Journey or a message matrix that needs persona inputs
- User is running or following up a Buyer Personas with AI workshop

## How to use this skill

### Step 1 — Gather context

Ask for what's missing; skip what the user already gave you. Don't dump all questions at once.

1. **Product / solution description** — What does it do? What market problems does it solve? (`pragmatic-market-problems`)
2. **Market segment(s)** — Which segment are these personas for? Personas often vary by segment. (`pragmatic-market-definition`)
3. **B2B or B2C context** — Buying committee or individual purchase?
4. **Known buyer roles** — Who is already known to be involved (e.g., VP of IT, procurement, end-user manager)?
5. **Available research** — Win/loss interviews, market interviews, surveys? Or do they need a template to fill in later?
6. **Output format** — Word document, Markdown, presentation or chat?

### Step 2 — Identify the buyer types and roles

Use the same three buyer types as `pragmatic-positioning`, so each persona maps to a positioning document:

| Buyer Type | Focus | What They Care About |
|---|---|---|
| **Functional buyer** | Day-to-day results for their team | Workflow fit, ease of use, how it solves their daily problems |
| **Financial buyer** (sometimes called the economic buyer) | Budget and ROI | Total cost of ownership, payback, risk, strategic alignment |
| **Technical buyer** | Feasibility and integration | Interoperability, security, implementation effort, admin burden |

Then identify the roles people play in the decision, which cut across those types:

- **Sponsor** — Champions the purchase and puts political capital behind it; often the executive who owns the outcome
- **Approver** — Can approve or block: procurement, legal, security review, finance sign-off
- **Influencer** — Shapes the decision without owning it: analysts, trusted peers, internal experts, end users consulted during evaluation
- **Champion / lead evaluator** — Runs the evaluation day to day

For B2C products, buyer and user often overlap, but the distinction still matters (parents buying for children, managers buying for teams).

Help the user pick the 2–5 roles that matter most for their sale. Segment changes the answer: one vendor found 4 personas for a generic market and 26 once segments were accounted for. Start with the primary segment and expand only if needed.

### Step 3 — Build each persona document

Read `references/persona-template.md` for the full template and field-by-field guidance. At minimum, each persona covers:

- **Goals** — what they want to achieve, personally and for their organization
- **Concerns** — risks, objections and past bad experiences
- **Authority** — decision authority, budget authority, and when they enter the process
- **Success criteria** — how they will judge whether the purchase was a good decision (their metrics, not yours)

Principles:

- **Archetypes, not stereotypes.** Represent the pattern of a buyer segment, not a caricature. Avoid stock-photo bias and overly narrow demographics.
- **Research-based, not fictional.** The best personas come from win/loss and market interviews and surveys, not a conference-room brainstorm. Without research, label the persona a hypothesis to validate. See `references/research-discovery-guide.md`.
- **Buying role, not just job title.** The same title plays different roles in different deals.
- **Keep it small.** 3–5 buyer personas usually cover 90%+ of sales. More scatters effort; zero leaves teams guessing.
- **Keep it alive.** Refresh regularly; companies that beat revenue goals are far more likely to have refreshed personas in the last six months. See `references/validation-maintenance-guide.md`.

A valid persona feels like someone you could work alongside or meet at a user conference. See `references/example-b2b-personas.md` for a worked example.

### Step 4 — Connect personas to other focus areas

- **Positioning** (Planning, `pragmatic-positioning`) — A positioning document for each buyer persona whose problems differ.
- **Buyer Journey** (Planning, `pragmatic-buyer-journey`) — Map how each buyer, sponsor and approver moves from need to decision.
- **Organizational Alignment** (Go-to-Market, `pragmatic-organizational-alignment`) — Help sales, success and support recognize which persona they're dealing with and what that person needs.
- **Content** and **Assets** (Enablement, `pragmatic-content`, `pragmatic-assets`) — White papers, ROI calculators, technical specs and battle cards for specific personas at specific journey stages.
- **Product Roadmap** and **Requirements** — Persona priorities inform which features matter to the purchase decision.

### Step 5 — Deliver the output

- **Word document (.docx)** — Use the `docx` skill if available. Cover page, contents, one section per persona, buying committee summary.
- **Markdown** — Clean, structured document.
- **Presentation (.pptx)** — Use the `pptx` skill if available. One slide per persona plus a buying committee overview.
- **Chat** — Structured persona profiles in the conversation.

Default to a Word document if the user doesn't specify; personas are meant to be shared.

## Responsibilities and skills

- Define the archetypical buyers, sponsors, approvers and influencers involved in purchasing your products and services
- Create and share a persona document for each, and keep it current

Skills needed: win/loss and market interviewing; synthesizing interview data and spotting trends; making personas come alive across the organization and keeping them relevant.

## Using AI in this focus area

- Synthesize win/loss and market interview transcripts into draft goals, concerns, authority and success criteria per role.
- Compare draft personas against CRM data (who actually shows up in won and lost deals) to spot missing sponsors or approvers.
- Draft persona documents and a buying committee map from validated research (the Buyer Personas with AI workshop covers this workflow).

AI will produce convincing personas from nothing; that is the risk. Check every attribute against real interview evidence and mark unvalidated ones as hypotheses (NIHITO still applies). Keep sensitive customer, deal and company data out of tools not approved for it. The team, not the tool, decides which personas to target.

## Reference Files

- `references/persona-template.md` — Field-by-field persona template and buying committee summary
- `references/research-discovery-guide.md` — How to research buyers, interview questions by buyer type, synthesis
- `references/validation-maintenance-guide.md` — Confidence levels, validation and refresh cadence
- `references/example-b2b-personas.md` — Completed example personas for a B2B SaaS product
