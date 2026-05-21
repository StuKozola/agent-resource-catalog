---
name: pragmatic-positioning
description: "Use this skill whenever the user needs help with product positioning following the Pragmatic Marketing Framework (Pragmatic Institute). Triggers include: creating positioning documents, writing positioning statements, crafting buyer-specific messaging, developing a 25-word primary message, tailoring positioning for different buyer types (functional, financial, technical), building a family of positioning documents, aligning product messaging with market problems, or any mention of 'Pragmatic positioning', 'positioning document', 'product positioning', 'positioning statement', or 'buyer messaging'. Also use when the user asks about company vs. product family vs. product-level positioning, wants to move from feature-focused to problem-focused messaging, or needs to create positioning for multiple buyer personas. Even if the user simply says 'help me position my product' or 'write positioning for this feature', use this skill."
---

# Pragmatic Positioning Skill

Create product positioning documents aligned with the Pragmatic Marketing Framework (Pragmatic Institute). Positioning is an internal strategic activity that describes a product by its ability to solve market problems, resulting in a family of documents used to develop all external messaging.

## Core Principles

Positioning in the Pragmatic Framework follows these rules — internalize them before writing anything:

1. **Positioning focuses on problems you solve, not features you ship.** The buyer cares about outcomes. Technical specs only appear as evidence supporting a promise.
2. **Create a separate positioning document for each buyer persona whose problems are different.** A single generic document fails everyone.
3. **Positioning should be complete before development messaging begins.** It is an early strategic activity, not a last-minute launch task.
4. **Product management owns the message; marketing communications owns the delivery.** The positioning document is the authoritative source.
5. **Name the product after positioning is finished.** The name should reinforce the positioning, not the other way around.
6. **Positioning is internal.** It drives external messaging, sales tools, collateral, and campaigns — but the document itself is for internal alignment.
7. **Be sincere.** Buzzwords, vague superlatives, and clever taglines that obscure meaning are positioning failures. If your product is inferior in an area, don't claim otherwise.

## Positioning Document Structure

Each positioning document targets one buyer persona and contains these sections in order. Read `references/document-template.md` for the full annotated template before generating any document.

### Section Summary

1. **Buyer Persona** — Who this document is written for (role, goals, context).
2. **Problem Statement** — The overriding market problem this buyer faces, written in the buyer's language.
3. **Ideal Solution** — What the buyer wishes existed to solve the problem (1–2 sentences).
4. **Primary Message (≤25 words)** — The single most important thing you want this buyer to remember. Use the formula: "[Product] helps [Persona] solve [Problem] by providing [Unique Value]."
5. **Product Description** — 2–3 sentences expanding on the primary message in terms of the buyer's needs.
6. **Key Capabilities (3–5)** — Features relevant to this buyer, each tied to a problem or outcome. Not a spec sheet — each capability answers "so what?" for the buyer.
7. **Proof Points** — Evidence: customer results, metrics, case references, analyst quotes.

## Buyer Types

For complex B2B purchases, expect at least three buyer types. Each gets their own positioning document (or at minimum their own tailored section):

- **User/Functional Buyer** — Cares about daily workflow improvement, ease of use, productivity gains. Ask: "How does this make my job easier?"
- **Technical Buyer** — Cares about integration, security, architecture, standards compliance. Ask: "Does this fit our environment?"
- **Financial/Economic Buyer** — Cares about ROI, total cost of ownership, risk reduction, strategic alignment. Ask: "Is this a sound investment?"

When the user hasn't specified buyer types, ask which personas matter most before drafting.

## Positioning Hierarchy

Products exist within a hierarchy. Each level has its own positioning, and lower levels must reinforce higher levels:

- **Company Positioning** — The overarching brand promise and market differentiation.
- **Product Family Positioning** — The value of a category of related products.
- **Product Positioning** — The specific value of an individual product.

When creating product-level positioning, ask about (or confirm assumptions about) company and family positioning to ensure alignment.

## Workflow

Follow this sequence when a user asks for positioning help:

### Step 1: Gather Inputs

Before writing anything, collect or confirm these inputs. If the user hasn't provided them, ask:

- What product or product family is being positioned?
- Who are the target buyer personas? (roles, not demographics)
- What are the top 2–3 market problems this product solves for each persona?
- What is the product's distinctive competence — what can it do that competitors cannot?
- Who are the primary competitors or alternative approaches?
- Is there existing company or product family positioning to align with?
- What evidence or proof points exist (customer wins, metrics, analyst coverage)?

### Step 2: Draft the Positioning Document(s)

Generate one document per buyer persona using the structure above. Follow the template in `references/document-template.md`.

Key writing guidelines:
- **Use the buyer's language**, not internal jargon. If a buyer says "keeping our systems safe," don't write "unified threat management."
- **Lead with problems, not features.** Every sentence should connect back to a pain the buyer feels.
- **Keep the primary message under 25 words.** This is the hardest part — iterate until it is crisp.
- **Tie each capability to an outcome.** Format: "[Capability] — [What it does for this buyer]."
- **Be honest about what the product does and doesn't do.** Insincere positioning erodes trust.

### Step 3: Review and Refine

After drafting, check the document against these quality criteria:
- Does it pass the "so what?" test for every claim?
- Could a competitor paste their name into the primary message and have it still be true? If yes, it's not differentiated enough.
- Is the language problem-oriented (not spec-oriented)?
- Would a salesperson be able to use this language verbatim with the buyer?
- Does it align with company/family positioning?

### Step 4: Create the Document Family

If multiple personas are involved, create the full set. Then create a summary view showing how each persona's positioning connects to the others and to the product's overall value.

## Output Formats

- **Default**: Produce a clean, well-structured document in the conversation. Use clear headings for each section.
- **If the user requests a file**: Create a .docx file using the docx skill. Read the docx SKILL.md at `/mnt/skills/public/docx/SKILL.md` for file creation instructions.
- **If the user requests a presentation**: Create a .pptx using the pptx skill. Read `/mnt/skills/public/pptx/SKILL.md`.

## Common Mistakes to Watch For

- **Feature dumping** — Listing features without connecting them to buyer problems.
- **One-size-fits-all** — Using the same message for all buyer types.
- **Buzzword soup** — "Best-in-class," "innovative," "cutting-edge," "synergy" — these communicate nothing.
- **Inside-out language** — Using internal product names, codenames, or technical architecture terms that buyers don't know.
- **Positioning too late** — Treating positioning as a launch-week activity rather than a strategic input.
- **Confusing positioning with messaging** — Positioning is the internal strategy; messaging is the external expression. Don't skip the strategy.

## Reference Files

- `references/document-template.md` — Full annotated template for a positioning document. Read this before generating any positioning document.
- `references/examples.md` — Two complete example positioning documents (one B2B SaaS, one physical product) showing the template in action.
