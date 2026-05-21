# BBP Analysis Process — Detailed Walkthrough

This reference provides the complete step-by-step process for conducting a Buy, Build, or Partner analysis, along with the document template for the final deliverable.

## Table of Contents
1. [Pre-Work: Gather Inputs](#pre-work)
2. [Phase 1: Define the Problem and Gap](#phase-1)
3. [Phase 2: Define the Ideal Solution](#phase-2)
4. [Phase 3: Evaluate Options](#phase-3)
5. [Phase 4: Decide and Align](#phase-4)
6. [BBP Analysis Document Template](#template)
7. [Common Pitfalls](#pitfalls)
8. [Stakeholder RACI](#raci)

---

## Pre-Work: Gather Inputs <a name="pre-work"></a>

Before starting the BBP analysis, gather the following inputs. If the user hasn't done this work yet, help them identify what's missing and suggest they complete it first (or help them sketch it out).

**Required inputs:**
- A validated market problem statement (from Market Problems / customer interviews)
- Win/Loss data showing why customers need this capability
- Competitive landscape assessment (who offers this today?)
- Distinctive competencies inventory (what is the company uniquely good at?)
- Asset assessment (existing tech, patents, skills, services that could be leveraged)
- Engineering capacity and roadmap constraints
- Budget parameters or investment thresholds

**Nice-to-have inputs:**
- Total addressable market (TAM) for the capability
- Customer willingness-to-pay data
- Existing vendor/partner landscape scan
- Internal build estimates from engineering

---

## Phase 1: Define the Problem and Gap <a name="phase-1"></a>

### Step 1.1: Articulate the Market Problem
Write a clear problem statement using this format:

> **[Target persona]** needs to **[accomplish goal]** but currently cannot because **[barrier/gap]**. This results in **[negative outcome]** and affects approximately **[market size/segment]**.

### Step 1.2: Map the Competitive Landscape
For each competitor or alternative that addresses this gap, document:
- What is their solution?
- How mature is it?
- What are its strengths and weaknesses?
- How are customers currently working around the gap?

### Step 1.3: Quantify the Gap's Impact
Answer these questions:
- How many customers/prospects have requested this capability?
- What revenue is at risk or being lost without it?
- How does this gap affect win rates?
- Is this gap a "must-have" (deal-breaker) or "nice-to-have" (tie-breaker)?

### Step 1.4: Validate the Investment
Apply the Pragmatic test: Is the problem **urgent**, **pervasive**, and will the market **pay to solve it**? If the answer to any of these is "no," reconsider whether to address the gap at all.

---

## Phase 2: Define the Ideal Solution <a name="phase-2"></a>

### Step 2.1: Functional Requirements
Work with your product architect or CTO to define:
- What must the solution do? (functional requirements)
- What performance levels are required? (non-functional requirements)
- What integration points exist with the current product?
- What data flows are involved?
- What security/compliance requirements apply?

### Step 2.2: Assess Alignment with Distinctive Competencies
Ask:
- Does solving this problem align with what we're uniquely good at?
- Would building this capability strengthen our competitive moat?
- Or is this a "table stakes" capability that doesn't differentiate us?

### Step 2.3: Estimate Scope
Work with engineering to create rough estimates:
- T-shirt size the build effort (S/M/L/XL)
- Estimate the number of engineers and duration
- Identify key technical risks or unknowns

---

## Phase 3: Evaluate Options <a name="phase-3"></a>

For each of the three options (Buy, Build, Partner), complete the following evaluation. See `scoring.md` for the weighted scoring matrix.

### Step 3.1: Research Each Option

**For Buy:**
- Identify acquisition targets or purchasable solutions
- Assess their product maturity, customer base, team quality
- Estimate acquisition cost and integration effort
- Evaluate cultural and technical fit
- Consider: Would the target be willing to sell? At what price?

**For Build:**
- Get engineering estimates (time, team size, cost)
- Identify technical risks and unknowns
- Map dependencies on other roadmap items
- Calculate opportunity cost (what gets deprioritized?)
- Estimate ongoing maintenance cost (typically 15-20% of build cost per year)

**For Partner:**
- Identify potential partners with the capability
- Assess their product quality, reliability, and roadmap alignment
- Evaluate integration options (API, white-label, co-development)
- Understand their business model and how the partnership would work commercially
- Assess dependency risk (what if they get acquired, pivot, or shut down?)

### Step 3.2: Score Each Option
Use the 7-criteria weighted scoring matrix from `scoring.md`. Involve cross-functional stakeholders in the scoring to reduce bias.

### Step 3.3: Sensitivity Analysis
Test your scoring:
- What if the weights were different? Does the recommendation change?
- What's the worst-case scenario for the top-scoring option?
- What assumptions are you making, and what if they're wrong?

---

## Phase 4: Decide and Align <a name="phase-4"></a>

### Step 4.1: Document the Recommendation
Write the BBP Analysis Document (template below). Include the scoring, rationale, risks, and mitigation strategies.

### Step 4.2: Stakeholder Review
Present to the cross-functional team. Key stakeholders:
- Product Management (owns the recommendation)
- Engineering/CTO (technical feasibility and build estimates)
- Finance (budget, ROI, acquisition valuation)
- Legal (contracts, IP, regulatory)
- Executive Leadership (strategic alignment, capital allocation)
- Operations/IT (integration, support, scale)

### Step 4.3: Define Success Metrics
Establish clear KPIs for the chosen path:
- Time-to-market target
- Cost budget and burn rate
- Customer adoption metrics
- Integration milestones
- Revenue impact targets

### Step 4.4: Set Exit Triggers
Define conditions that would cause you to revisit the decision:
- For Build: If the project exceeds X% over budget or Y months late
- For Buy: If integration takes more than Z months or costs exceed threshold
- For Partner: If partner SLA drops below target, or partner is acquired

---

## BBP Analysis Document Template <a name="template"></a>

Use this structure for the written deliverable:

```
# Buy, Build, or Partner Analysis: [Capability Name]

**Author:** [Name, Title]
**Date:** [Date]
**Status:** [Draft / Under Review / Approved]
**Decision Owner:** [Name]

## 1. Executive Summary
[2-3 sentences: the gap, the recommendation, and the key reason]

## 2. Market Problem & Gap
### 2.1 Problem Statement
[The validated market problem]

### 2.2 Gap Description
[What specific capability is missing from the current offering]

### 2.3 Market Impact
[Revenue at risk, competitive pressure, customer demand data]

## 3. Ideal Solution Definition
### 3.1 Functional Requirements
[What the solution must do]

### 3.2 Integration Requirements
[How it connects to existing product/infrastructure]

### 3.3 Alignment with Distinctive Competencies
[Is this core or non-core to our differentiation?]

## 4. Options Evaluated

### 4.1 Buy
**Description:** [What would we acquire/purchase?]
**Targets/Solutions Identified:** [Names, brief descriptions]
**Estimated Cost:** [Acquisition + integration]
**Timeline:** [Estimated time to market]
**Pros:** [Bullet list]
**Cons:** [Bullet list]

### 4.2 Build
**Description:** [What would we develop internally?]
**Engineering Estimate:** [Team size, duration, cost]
**Timeline:** [Estimated time to market]
**Pros:** [Bullet list]
**Cons:** [Bullet list]

### 4.3 Partner
**Description:** [What partnership model would we pursue?]
**Candidates Identified:** [Names, brief descriptions]
**Estimated Cost:** [Setup + ongoing]
**Timeline:** [Estimated time to market]
**Pros:** [Bullet list]
**Cons:** [Bullet list]

## 5. Scoring Matrix
[Insert the 7-criteria weighted scoring matrix with results]

| Criterion (Weight) | Buy (Score) | Build (Score) | Partner (Score) |
|---------------------|-------------|---------------|-----------------|
| Time-to-Value (15%) | | | |
| Total Cost of Ownership (20%) | | | |
| Strategic Differentiation (20%) | | | |
| Integration Risk (15%) | | | |
| Control & IP (10%) | | | |
| Scalability (10%) | | | |
| Risk & Dependencies (10%) | | | |
| **Weighted Total** | **X** | **X** | **X** |

## 6. Recommendation
[Which option and why. Reference the scoring, strategic rationale,
and any qualitative factors not captured in the matrix.]

## 7. Risks & Mitigation
[Key risks of the recommended path and how to mitigate them]

## 8. Next Steps & Timeline
[Immediate actions, milestones, and owners]

## 9. Exit Triggers
[Conditions under which the decision should be revisited]

## Appendix
- Detailed cost models
- Competitive landscape data
- Customer feedback / win-loss data
- Engineering estimates
```

---

## Common Pitfalls <a name="pitfalls"></a>

1. **"We can build anything" syndrome.** Engineering teams often prefer to build. Challenge this bias by quantifying opportunity cost and time-to-market impact.

2. **Ignoring integration costs.** Whether buying or partnering, integration is always harder and more expensive than estimated. Use a 2x multiplier on initial estimates.

3. **Conflating "build" with "control."** Buying or partnering doesn't necessarily mean losing control. Well-structured deals can provide significant influence over roadmap and quality.

4. **Analysis paralysis.** Set a time-box for the analysis (typically 2-4 weeks). The goal is a well-informed decision, not a perfect one.

5. **Forgetting to revisit.** A decision made today may not be the right one in 18 months. Build in review cadences.

6. **Not involving the right stakeholders.** This is a cross-functional decision. Product owns it, but engineering, finance, legal, and exec leadership all have critical perspectives.

7. **Scoping too broadly.** Break large capabilities into components. You might build some parts and partner for others. The answer doesn't have to be the same for every component.

8. **Underestimating partnership governance.** Partnerships require ongoing management — a dedicated partner product manager, regular business reviews, SLA monitoring, and escalation processes.

---

## Stakeholder RACI <a name="raci"></a>

| Activity | Product Mgmt | Engineering | Finance | Legal | Exec Leadership | Ops/IT |
|----------|-------------|-------------|---------|-------|-----------------|--------|
| Define market problem | **R/A** | C | I | I | I | I |
| Define ideal solution | **R** | **A** | I | C | I | C |
| Research Buy options | **R** | C | **A** | C | I | I |
| Research Build options | **R** | **A** | C | I | I | C |
| Research Partner options | **R** | C | C | C | I | I |
| Score options | **R/A** | C | C | C | I | C |
| Final recommendation | **R/A** | C | C | C | **A** | I |
| Execute decision | C | R | R | R | A | **R** |

R = Responsible, A = Accountable, C = Consulted, I = Informed
