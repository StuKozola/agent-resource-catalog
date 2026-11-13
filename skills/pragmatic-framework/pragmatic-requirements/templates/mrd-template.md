# Market Requirements Document Template

Use this template to produce the final MRD. Replace all bracketed placeholders with actual content. Delete any instructional notes before finalizing.

---

# Market Requirements Document: [Product Name]

**Version:** [X.X]
**Date:** [Date]
**Author:** [Product Manager Name]
**Target Release:** [Release name/number or timeframe]
**Status:** [Draft | Under Review | Approved]

---

## 1. Executive Summary

[2-3 paragraphs summarizing: the target personas, the top market problems being addressed in this release, the strategic rationale for this set of priorities, and the expected market impact. This section is for executives who will not read the full document.]

---

## 2. Scope and Context

### Target Market Segments
[List the segments this release targets, in priority order. Reference the Market Definition if available.]

### Relationship to Product Roadmap
[Where does this release fit in the broader roadmap? What phase of the product vision does it advance?]

### Business Plan Alignment
[How do these requirements support the financial and strategic goals in the business plan?]

### What This Release Is NOT
[Explicitly call out what is out of scope. This is as important as what's in scope — it prevents expectation mismatches.]

---

## 3. Persona Profiles

### Persona: [Name — e.g., "Rachel, Regional Manager"]

**Role:** [Job title and organizational context]
**Goals:** [Top 2-3 things this persona is trying to accomplish]
**Frustrations:** [Top 2-3 pain points relevant to this product]
**Technical Proficiency:** [Low / Medium / High]
**Usage Frequency:** [How often they interact with the product]
**Buyer or User:** [Specify — buyers care about value/ROI; users care about capabilities/usability]

[Repeat for each persona relevant to this release. Typically 2-4 personas.]

**Persona Contact List:**
[For each persona, provide 2-3 real customer/prospect contacts that designers and developers can reach out to directly for clarification.]

| Persona | Contact Name | Company | Email / Phone | Notes |
|---------|-------------|---------|---------------|-------|
| [Persona name] | [Name] | [Company] | [Contact info] | [e.g., "Current customer, very engaged"] |
| [Persona name] | [Name] | [Company] | [Contact info] | [e.g., "Recent loss, willing to talk"] |

---

## 4. Prioritized Requirements

### Priority Tier: Must Have (Score 60-75)

---

#### REQ-[001]: [Short descriptive title]

**Persona:** [Name]
**Priority Score:** [Score] (U:[x] P:[x] W:[x] S:[x] C:[x] E:[x])
**Evidence:** [Number of sites reporting; data sources]

**Use Scenario:**
[The story-format requirement. Write in the persona's voice. Include the problem, context, frequency, and impact. 1-2 paragraphs.]

**Current Workaround:**
[How the persona handles this today, if applicable.]

**Requirement Type:** [Functional | Performance | Constraint | Interface | Security | Other]

**Dependencies:** [Any prerequisite requirements, or "None"]

---

[Repeat the requirement block for each Must Have requirement]

### Priority Tier: Should Have (Score 45-59)

---

[Repeat requirement blocks for Should Have items]

### Priority Tier: Could Have (Score 30-44)

---

[Repeat requirement blocks for Could Have items]

### Committed (Non-Scored)

[Requirements driven by contractual commitments or regulatory deadlines. Include the commitment source and deadline.]

---

## 5. Scoring Methodology

### Dimensions and Weights

| Dimension | Weight | Description |
|-----------|--------|-------------|
| Urgency | ×3 | How pressing is this problem for the persona? |
| Pervasiveness | ×3 | How widespread across the target market? |
| Willingness to Pay | ×3 | Would customers pay to solve this? |
| Strategic Alignment | ×2 | How well does this fit company strategy? |
| Competitive Pressure | ×2 | What is the competitive dynamic? |
| Implementation Effort | ×2 | Effort required (inverted — lower effort = higher score) |

**Formula:** Priority Score = (U×3) + (P×3) + (W×3) + (S×2) + (C×2) + (E×2)

[If weights were adjusted from defaults, document the rationale here.]

### Confidence Notes
[Flag any requirements where the evidence is thin or the scoring is based on limited data. Be transparent about what you know well vs. where you're estimating.]

---

## 6. Requirement Summary Matrix

[A single-page view for quick scanning. Sort by priority score descending.]

| ID | Title | Persona | Type | Priority Score | Tier | Status |
|----|-------|---------|------|---------------|------|--------|
| REQ-001 | [Title] | [Persona] | [Type] | [Score] | Must Have | [Proposed/Committed/etc.] |
| REQ-002 | [Title] | [Persona] | [Type] | [Score] | Must Have | |
| REQ-003 | [Title] | [Persona] | [Type] | [Score] | Should Have | |
| ... | | | | | | |

---

## 7. Out-of-Scope / Deferred Requirements

[List requirements that were considered but deferred, with the rationale for deferral. This is important for transparency with stakeholders who advocated for these items.]

| ID | Title | Score | Reason Deferred | Target Timeframe |
|----|-------|-------|-----------------|-----------------|
| | | | | |

---

## 8. Open Issues

[Track any unresolved questions about requirements. Each issue should have an owner and a target resolution date.]

| Issue # | Description | Owner | Opened | Target Resolution |
|---------|-------------|-------|--------|------------------|
| | | | | |

---

## 9. Change History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Name] | Initial release |
| | | | |

---

## Appendix A: Data Sources

[List all sources used to develop these requirements: customer interviews (anonymized), survey results, support ticket analysis, win/loss reports, competitive intelligence, analytics data, etc. This establishes the evidentiary foundation for the requirements.]

## Appendix B: Glossary

[Define any persona-specific or domain-specific terms used in the requirements to ensure developers and designers share the same vocabulary.]
