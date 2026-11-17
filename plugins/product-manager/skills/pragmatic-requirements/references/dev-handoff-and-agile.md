# Handing Off Requirements to Development and Working with Agile

This guide covers how to communicate market requirements to development teams effectively, including how the Pragmatic requirements approach integrates with agile development processes.

## Table of Contents
1. The Handoff Problem
2. Clean Role Boundaries
3. Making Requirements Developer-Friendly
4. Requirements in an Agile Context
5. Managing Requirements Through the Development Cycle
6. Closing the Loop

---

## 1. The Handoff Problem

The handoff from market requirements to development is where many products fail. Common failure modes:

**The late MRD:** Development is already underway before the MRD arrives. The team builds based on assumptions while the product manager is still gathering market data. Requirements become retroactive justification rather than forward guidance.

**The incomprehensible MRD:** The document is so bloated with meeting notes, tangential analysis, and marketing language that developers can't find the actual requirements. It reads like committee minutes.

**The ReqSpec hybrid:** The MRD prescribes both the problem AND the solution, preventing developers from innovating and creating blame-sharing when the design doesn't work.

**The missing MRD:** No formal requirements exist. Product decisions are made in hallway conversations, Slack threads, and executive whims. No one agrees on what's being built or why.

All of these are solved by good requirements management practices: a living, prioritized, persona-centered MRD delivered before development begins and maintained throughout the cycle.

---

## 2. Clean Role Boundaries

The Pragmatic Framework defines three distinct roles in the requirements-to-product pipeline:

### Product Manager
- Finds and quantifies market problems through customer contact
- Articulates problems in the form of requirements (the MRD)
- Prioritizes requirements based on market evidence
- Provides customer/prospect contact information for designer access
- Does NOT attend design meetings (unless market context is needed for a specific question)
- Does NOT write specifications

### Product Architect / Designer
- Reads the MRD and understands the persona problems
- Contacts the customers/prospects listed in the MRD for clarification
- Writes a functional specification describing the approach to solving each problem
- Makes design trade-off decisions based on understanding the persona's context
- Presents the specification to the product manager for validation against market intent

### Product Developer
- Reads the functional specification
- Creates a technical specification for implementation
- Builds the solution
- Raises issues when requirements are unclear, contradictory, or technically impossible

### Why Product Managers Should Not Be in Design Meetings

Product managers attending design meetings creates dysfunction:
- It signals that the MRD is insufficient (which means the MRD should be improved, not supplemented with meeting attendance)
- It creates shared blame for design decisions that should belong to the design/dev team
- It pulls the product manager away from their primary job: being in the market
- If product managers have time for design meetings, it should only be after they have completed their customer visits

The one exception: brief clarification sessions where development has a specific question about market context that isn't adequately captured in the MRD.

---

## 3. Making Requirements Developer-Friendly

Developers are the primary consumers of the MRD. Respect their time and information needs:

### Do
- Write in clear, jargon-free language
- Keep individual requirements short (1-2 paragraphs)
- Include the persona, the problem, and the frequency in every requirement
- Provide contact information for 2-3 real customers/prospects per requirement so developers can reach out directly
- Categorize requirements so each development group sees only what's relevant to them
- Highlight recently modified requirements in each update
- Include supporting evidence (number of sites reporting, data sources)

### Don't
- Bury requirements in pages of boilerplate and background
- Use marketing buzzwords or sales language
- Prescribe UI layouts, algorithms, or architecture
- Force developers to read the entire document to find what's relevant to them
- Submit the MRD without prioritization (everything is equally important = nothing is important)

### Providing Requirements to QA

QA teams should receive requirements alongside use scenarios. The ideal test plan verifies that the *problem was solved* for the persona, not merely that the design was implemented as specified. This is a subtle but important distinction — testing against the requirement (was the problem solved?) produces better products than testing against the specification (was the design built correctly?).

---

## 4. Requirements in an Agile Context

### The MRD Is Not Anti-Agile

A common misconception is that market requirements documents are a waterfall artifact incompatible with agile development. This is false. The MRD in a Pragmatic context is:
- **Living, not static** — updated as new market data arrives
- **Short and focused** — not a 100-page tome but a prioritized list of problems
- **Compatible with backlogs** — requirements feed the product backlog; they don't replace it

Whether you call it an MRD, a PRD, a backlog, or index cards wrapped in a rubber band, the core need is the same: a prioritized set of market problems to guide what gets built.

### How Requirements Map to Agile Artifacts

| Pragmatic Artifact | Agile Equivalent | Notes |
|---|---|---|
| Individual requirement (persona + problem + frequency) | Epic or User Story | A requirement may spawn one or many user stories during sprint planning |
| Use scenario | Acceptance criteria / Story context | The use scenario helps the team understand "done" in terms of the persona's problem being solved |
| MRD priority score | Backlog priority | The MRD scoring provides strategic prioritization; the product owner translates to sprint-level ordering |
| Persona definition | Persona reference | Shared artifact used by both the Pragmatic process and agile teams |

### The Product Manager as Customer Representative

In agile development, the concept of an "onsite customer" exists but is impractical for vendor-model companies. The product manager serves as the market representative — not by attending every standup, but by:
- Maintaining the prioritized MRD as the source of truth for what problems matter
- Being available for clarification when development has questions about market context
- Providing customer contact information so developers can go directly to the source
- Participating in sprint reviews to validate that solutions address the underlying market problems

### Agile-Friendly MRD Practices

- Keep the MRD as a living backlog-feeder, not a one-time delivery
- Write requirements that can be decomposed into sprint-sized stories by the development team
- Accept that requirements will be refined during sprint planning — the MRD provides direction, not exact specifications
- Maintain a vision for future product generations alongside the current release requirements
- Use the MRD priority scoring to inform sprint priority, but accept that technical dependencies and capacity will also influence sprint-level ordering

---

## 5. Managing Requirements Through the Development Cycle

### Tracking Requirement Status

Each requirement should have a tracked status:
- **Proposed** — identified from market data, not yet scored
- **Scored** — prioritized and ready for roadmap consideration
- **Committed** — included in the current release plan
- **In Progress** — actively being designed or developed
- **Delivered** — shipped in a release
- **Validated** — confirmed to solve the market problem (post-release)
- **Deferred** — pushed to a future release with rationale documented
- **Declined** — removed from consideration with rationale documented

### Handling Requirement Changes

When requirements change mid-cycle:
1. Document what changed and why (new market data, executive override, technical constraint discovered)
2. Assess the impact on committed requirements (what gets displaced?)
3. Communicate the change to all stakeholders
4. Update the MRD and priority scores

### Issue Resolution

When developers raise issues with requirements (unclear, contradictory, technically infeasible):
- Track every issue formally
- The product manager owns resolving scope-related issues
- Close issues promptly — open issues create uncertainty and slow development
- If resolution requires market context the product manager doesn't have, go get it from customers rather than guessing

---

## 6. Closing the Loop

After a release, close the loop on requirements:

### Validation Questions
- Did the delivered solution actually solve the market problem?
- Are personas using the capability as expected?
- Has the workaround behavior changed?
- Did the problem frequency decrease?
- Are customers reporting satisfaction with the solution?

### Feeding Back into the Process
- Problems that weren't fully solved become refined requirements for the next cycle
- New problems discovered during validation enter the requirement pipeline
- Win/Loss data post-release reveals whether requirements decisions improved competitive position
- Customer satisfaction data validates or challenges the prioritization model

This closed-loop process is what makes requirements management a continuous discipline rather than a one-time document exercise.
