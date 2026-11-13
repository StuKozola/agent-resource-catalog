---
name: pragmatic-positioning
description: "Use this skill whenever the user needs help with product positioning following the Pragmatic Framework (Pragmatic Institute). Triggers include: creating positioning documents, writing positioning statements, crafting buyer-specific messaging, developing a 25-word primary message, tailoring positioning for functional, financial and technical buyers, building a family of positioning documents, separating positioning from messaging, aligning product messaging with market problems, or any mention of 'Pragmatic positioning', 'positioning document', 'product positioning', 'positioning statement', 'value proposition', or 'buyer messaging'. Also use when the user asks about company vs. product family vs. product-level positioning, wants to move from feature-focused to problem-focused messaging, or needs to answer 'who is this for and why is it the right choice?'. Even if the user simply says 'help me position my product' or 'write positioning for this feature', use this skill."
---

# Positioning — Pragmatic Framework (2027)

## Where this fits in the 2027 Pragmatic Framework

- **Category:** Planning — *What are we building, for whom, and why?*
- **Focus-area question:** *Who is this for, and why is it the right choice?*
- **Position:** Above the bar (market-focused)
- **Other focus areas in this category:** Buyer Journey, Buyer Personas, User Personas, Requirements, Ideation, Stakeholder Management

Positioning explains how the product solves market problems for a specific audience and why it is the right choice for them. It gives engineering, marketing and sales one consistent story and makes the value clear to each buyer type. Do it early, and build it around the buyer's needs rather than the product's features. The output is a family of internal documents that all external messaging is derived from.

**Positioning vs. messaging.** Positioning is *what* you want to communicate. Messaging is *how* you'll communicate it: the words, channels and formats used with a given audience. Settle the positioning first; messaging follows from it.

## Core Principles

Internalize these before writing anything:

1. **Positioning focuses on problems you solve, not features you ship.** The buyer cares about outcomes. Technical specs only appear as evidence supporting a promise.
2. **Create a separate positioning document for each buyer persona whose problems are different.** A single generic document fails everyone.
3. **Position early.** Positioning should be complete before development messaging begins. It is a strategic input, not a last-minute launch task.
4. **Product management owns the message; marketing communications owns the delivery.** The positioning document is the authoritative source.
5. **Name the product after positioning is finished.** The name should reinforce the positioning, not the other way around.
6. **Positioning is internal.** It drives external messaging, assets, content and campaigns, but the document itself is for internal alignment.
7. **Be specific and sincere.** Avoid jargon, vague superlatives and clever taglines that obscure meaning. Don't try to appeal to everyone; a position that fits every buyer differentiates for none. If the product is weaker in an area, don't claim otherwise.

## Positioning Document Structure

Each positioning document targets one buyer persona and contains these sections in order. Read `references/document-template.md` for the full annotated template before generating any document.

1. **Buyer Persona** — Who this document is written for (role, goals, context).
2. **Problem Statement** — The overriding market problem this buyer faces, written in the buyer's language.
3. **Ideal Solution** — What the buyer wishes existed to solve the problem (1–2 sentences).
4. **Primary Message (≤25 words)** — The single most important thing you want this buyer to remember. Formula: "[Product] helps [Persona] solve [Problem] by providing [Unique Value]."
5. **Product Description** — 2–3 sentences expanding on the primary message in terms of the buyer's needs.
6. **Key Capabilities (3–5)** — Features relevant to this buyer, each tied to a problem or outcome. Each capability answers "so what?" for the buyer.
7. **Proof Points** — Evidence: customer results, metrics, case references, analyst quotes.

A strong positioning document states the problem, the solution and the differentiation, with messaging for each buyer type.

## Buyer Types

For complex B2B purchases, expect at least three buyer types. Each gets its own positioning document, or at minimum its own tailored section. Use the same three types as `pragmatic-buyer-personas`:

- **Functional buyer** — Cares about daily workflow improvement, ease of use, productivity gains. Asks: "How does this make my team's work easier?"
- **Financial buyer** — Cares about ROI, total cost of ownership, risk reduction, strategic alignment. Asks: "Is this a sound investment?"
- **Technical buyer** — Cares about integration, security, architecture, standards compliance. Asks: "Does this fit our environment?"

When the user hasn't specified buyer types, ask which personas matter most before drafting. Sponsors, approvers and influencers (from `pragmatic-buyer-personas`) usually map onto one of these three types.

## Positioning Hierarchy

Products exist within a hierarchy. Each level has its own positioning, and lower levels must reinforce higher levels:

- **Company Positioning** — The overarching brand promise and market differentiation.
- **Product Family Positioning** — The value of a category of related products.
- **Product Positioning** — The specific value of an individual product.

When creating product-level positioning, ask about (or confirm assumptions about) company and family positioning. Product-level positioning should also be consistent with Product Strategy (Market category, `pragmatic-product-strategy`): what the product will be known for.

## Workflow

### Step 1: Gather Inputs

Before writing anything, collect or confirm these inputs. If the user hasn't provided them, ask:

- What product or product family is being positioned?
- Who are the target buyer personas? (roles, not demographics)
- What are the top 2–3 market problems this product solves for each persona? (`pragmatic-market-problems`)
- What can the product do that competitors cannot? (`pragmatic-distinctive-competencies`)
- Who are the primary competitors or alternatives, including doing nothing? (`pragmatic-competitive-landscape`)
- Is there existing company or product family positioning to align with?
- What evidence or proof points exist (customer wins, metrics, analyst coverage)?

### Step 2: Draft the Positioning Document(s)

Generate one document per buyer persona using the structure above and the template in `references/document-template.md`.

- **Use the buyer's language**, not internal jargon. If a buyer says "keeping our systems safe," don't write "unified threat management."
- **Lead with problems, not features.** Every sentence should connect back to a pain the buyer feels.
- **Keep the primary message under 25 words.** Iterate until it is crisp.
- **Tie each capability to an outcome.** Format: "[Capability] — [What it does for this buyer]."
- **Be honest about what the product does and doesn't do.**

### Step 3: Review and Refine

Check the document against these criteria:
- Does every claim pass the "so what?" test?
- Could a competitor paste their name into the primary message and have it still be true? If yes, it's not differentiated enough.
- Is the language problem-oriented, not spec-oriented, and free of jargon?
- Is it focused on a specific audience rather than trying to appeal to everyone?
- Would a salesperson be able to use this language verbatim with the buyer?
- Does it align with company/family positioning?

### Step 4: Create the Document Family

If multiple personas are involved, create the full set. Then create a summary view showing how each persona's positioning connects to the others and to the product's overall value. From there, messaging and assets can be built per audience (`pragmatic-content`, `pragmatic-assets` in Enablement; `pragmatic-organizational-alignment` in Go-to-Market).

## Output Formats

- **Default**: Produce a clean, well-structured document in the conversation. Use clear headings for each section.
- **If the user requests a file**: Create a .docx file using the docx skill, if available.
- **If the user requests a presentation**: Create a .pptx using the pptx skill, if available.

## Common Mistakes to Watch For

- **Feature dumping** — Listing features without connecting them to buyer problems.
- **One-size-fits-all** — Using the same message for all buyer types.
- **Appealing to everyone** — Broad positioning that no specific buyer recognizes as theirs.
- **Jargon and buzzword soup** — "Best-in-class," "innovative," "cutting-edge," "synergy" communicate nothing.
- **Inside-out language** — Internal product names, codenames or architecture terms that buyers don't know.
- **Positioning too late** — Treating positioning as a launch-week task rather than a strategic input.
- **Confusing positioning with messaging** — Writing taglines and copy before deciding what you want to communicate.

## Related focus areas

- **Buyer Personas** and **Buyer Journey** (Planning) — who the buyers are and how they decide; `pragmatic-buyer-personas`, `pragmatic-buyer-journey`.
- **Market Problems**, **Distinctive Competencies**, **Competitive Landscape** (Market) — the evidence positioning rests on.
- **Organizational Alignment**, **Launch**, **Marketing Plan** (Go-to-Market) and **Content**, **Assets** (Enablement) — where positioning is put to work.

## Using AI in this focus area

- Draft first-pass positioning documents and primary-message variants from interview notes and market-problem research.
- Run the "competitor name swap" test and flag jargon, superlatives and feature-first sentences.
- Adapt one positioning document into functional, financial and technical versions for review.

Check AI output against real market evidence; it will happily produce plausible, generic positioning that no buyer said. Talk to the market (NIHITO still applies). Keep sensitive customer, deal and company data out of tools not approved for it. The team, not the tool, owns the positioning decision.

## Reference Files

- `references/document-template.md` — Full annotated template for a positioning document. Read this before generating any positioning document.
- `references/examples.md` — Two complete example positioning documents (one B2B SaaS, one physical product) showing the template in action.
