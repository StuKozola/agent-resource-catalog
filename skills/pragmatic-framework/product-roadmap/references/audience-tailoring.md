# Audience-Tailoring Guide for Product Roadmaps

A single roadmap cannot serve every audience. The Pragmatic Framework emphasizes that roadmaps are
communication tools — and effective communication requires knowing your audience. This guide
provides templates and best practices for creating audience-specific roadmap views.

## Principle: Same Strategy, Different Lenses

Every view derives from the same underlying roadmap. You are not creating different roadmaps —
you are creating different *presentations* of the same strategic plan. This ensures consistency
while respecting that a VP of Sales and a Staff Engineer need different information to do their
jobs well.

---

## Executive View

**Audience:** C-suite, VP-level leaders, board members
**Their question:** "Are we investing in the right things to hit our business goals?"

**Include:**
- Product vision statement (1-2 sentences)
- 3-5 strategic themes with one-sentence problem statements
- How each theme maps to business objectives (revenue, retention, expansion, cost reduction)
- Investment level per theme (relative sizing: S/M/L or percentage of capacity)
- Key risks and dependencies that could derail plans
- Confidence level per theme (Committed / Planned / Exploratory)

**Exclude:**
- Feature-level details
- Technical implementation specifics
- Sprint-level timelines
- Jargon or acronyms that assume product/engineering context

**Format:** One page. Ideally a single slide or one-page document. If it takes more than one
page, it's too detailed for this audience.

**Template:**

```
# [Product Name] Roadmap — [Quarter/Year]

## Vision
[1-2 sentence product vision tied to market opportunity]

## Strategic Themes

| Theme | Market Problem | Business Outcome | Investment | Confidence |
|-------|---------------|-----------------|------------|------------|
| [Theme 1] | [Problem statement] | [Target metric] | [S/M/L] | Committed |
| [Theme 2] | [Problem statement] | [Target metric] | [S/M/L] | Planned |
| [Theme 3] | [Problem statement] | [Target metric] | [S/M/L] | Exploratory |

## Key Risks
- [Risk 1 and mitigation]
- [Risk 2 and mitigation]

## Key Decisions Needed
- [Decision needed from leadership and timeline]

Last updated: [Date]
```

---

## Engineering / Development View

**Audience:** Engineering managers, tech leads, architects, development teams
**Their question:** "What are we building, what are the dependencies, and how does it connect
to what the market needs?"

**Include:**
- Themes broken down into epics or major initiatives
- Technical dependencies between initiatives and across teams
- Known technical constraints or infrastructure prerequisites
- Relative sizing estimates (T-shirt sizes) where available
- Connection back to the market problem each epic addresses — engineers who understand *why*
  they're building something make better design decisions
- Milestone markers for key integration points

**Exclude:**
- Revenue projections and financial details
- Sales enablement timelines
- Marketing campaign details
- Political context about why certain things are prioritized (keep it evidence-based)

**Format:** Can be more detailed than the executive view — 2-4 pages or a detailed board view.
Engineers appreciate thoroughness over brevity, as long as it's well-structured.

**Template:**

```
# [Product Name] Engineering Roadmap — [Quarter/Year]

## Theme: [Theme Name]
**Market Problem:** [Why this matters to customers]
**Target Outcome:** [Measurable goal]

### Epics
1. **[Epic Name]** — [Brief description]
   - Dependencies: [List upstream/downstream dependencies]
   - Estimated size: [T-shirt size]
   - Key risks: [Technical risks]
   - Confidence: [High/Medium/Low]

2. **[Epic Name]** — [Brief description]
   - Dependencies: ...
   - Estimated size: ...

### Technical Prerequisites
- [Infrastructure or platform work needed before epics can begin]

---
[Repeat for each theme]
```

---

## Sales View

**Audience:** Sales leaders, account executives, sales engineers
**Their question:** "What can I tell my customers is coming, and what will help me close deals?"

**Include:**
- Themes framed in customer-problem language (how a buyer would describe the pain)
- General timing (this quarter, next quarter, later this year) without hard dates
- What is safe to share with customers vs. what is internal-only (mark this clearly)
- How themes map to common objections or competitive gaps sales encounters
- What is NOT on the roadmap — so sales doesn't inadvertently promise it

**Exclude:**
- Engineering details and architecture decisions
- Internal prioritization debates
- Specific feature names that could become contractual commitments
- Hard delivery dates

**Critical rule:** Reinforce that the roadmap is a plan, not a commitment. Establish a clear
policy: sales can discuss themes and direction, but cannot use the roadmap to make delivery
promises to close deals. If your organization struggles with this, consider creating a separate
"externally shareable" version with even less specificity.

**Format:** 1-2 pages. Conversational tone. Problem-first language.

**Template:**

```
# What's Coming — [Product Name] — [Quarter/Year]

## What customers are asking for, and how we're responding

### [Customer Problem in Their Words]
We're investing in [theme description]. Customers in [segment] have told us
that [problem statement]. We're targeting improvements in [general timeframe].

**Safe to share:** [What can be discussed externally]
**Internal only:** [What should not be shared with customers]
**Competitive context:** [How this positions against competitors]

### What's NOT on the near-term roadmap
[List common requests that are not currently planned, with brief rationale]

---
Reminder: This roadmap represents our current plan. Priorities may shift as
we learn more from the market. Please do not use this document as a delivery
commitment with customers.
```

---

## Marketing View

**Audience:** Product marketing, demand gen, content teams, campaign managers
**Their question:** "What's coming that I need to build messaging, campaigns, and launch plans
around?"

**Include:**
- Themes with positioning implications — what story does this tell about the product?
- Target personas affected by each theme
- Estimated launch windows (even approximate) for campaign planning
- Dependencies on marketing deliverables (positioning docs, sales tools, content)
- Win/loss insights that informed each theme — this helps marketing craft resonant messaging

**Exclude:**
- Deep technical architecture
- Internal engineering milestones
- Financial details beyond what marketing needs for budgeting

**Format:** 2-3 pages. Connect each theme to the go-to-market motion it requires.

**Template:**

```
# Product Marketing Roadmap Alignment — [Quarter/Year]

## Theme: [Theme Name]
**Target Persona:** [Buyer/User persona]
**Market Problem:** [Problem statement from market research]
**Positioning Angle:** [How we'll talk about this — what story does it tell?]
**Estimated Window:** [Quarter or approximate timeframe]
**Marketing Deliverables Needed:**
- [ ] Positioning document update
- [ ] Sales enablement materials
- [ ] Blog/thought leadership content
- [ ] Launch communications
- [ ] Competitive battlecard update

**Win/Loss Insight:** [What buyers told us that validates this theme]
```

---

## External / Customer View

**Audience:** Existing customers, prospects, partners, advisory boards
**Their question:** "Where is this product going, and does it align with my needs?"

**Include:**
- High-level vision and strategic direction
- Themes described as customer problems being addressed
- General time horizons (near-term, mid-term, long-term) with no specific dates
- Recently delivered improvements (builds credibility and shows momentum)
- Invitation to provide feedback

**Exclude:**
- Anything that could be construed as a delivery commitment
- Specific feature names or technical details
- Competitive positioning (keep it about your product, not against others)
- Internal prioritization rationale
- Anything labeled "internal only" in other views

**Format:** Highly visual. Minimal text. Consider using a published web page, a polished PDF,
or a presentation slide. This is a marketing asset as much as a planning document.

**Template:**

```
# [Product Name] — Where We're Headed

## Our Focus
[2-3 sentences about the product vision and who it serves]

## What We're Working On

### Near-Term
- [Theme described as a customer benefit]
- [Theme described as a customer benefit]

### Coming Up
- [Theme described as a customer benefit]

### On Our Radar
- [Theme described as a customer benefit]

## Recently Delivered
- [Recent improvement and the problem it solved]
- [Recent improvement and the problem it solved]

## Your Input Matters
[How to provide feedback — advisory board, surveys, customer success contact]
```

---

## Tips for All Views

1. **Always include a "last updated" date.** Stale roadmaps erode trust.
2. **Always lead with the problem, not the solution.** Themes should be recognizable to the
   audience as problems they care about.
3. **Be explicit about confidence levels.** Near-term items should be high confidence.
   Long-term items should be clearly marked as directional.
4. **Don't surprise people.** If priorities change, communicate the change with context before
   sharing an updated roadmap.
5. **Use consistent theme names across views.** The executive who sees "Reduce enterprise
   onboarding friction" should recognize that same phrase when talking with engineering or sales.
   Consistent naming prevents confusion.
