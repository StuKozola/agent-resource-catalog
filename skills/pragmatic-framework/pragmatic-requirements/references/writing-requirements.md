# Writing Market Requirements

This guide covers how to transform market problems and persona insights into well-structured, implementation-free requirements that development teams can act on.

## Table of Contents
1. The Fundamental Rule: Problem, Not Solution
2. The Use Scenario Format
3. Crafting Individual Requirements
4. Requirement Types Beyond Functional
5. The SMART Test
6. Common Writing Mistakes
7. Worked Examples

---

## 1. The Fundamental Rule: Problem, Not Solution

A requirement is a statement of the problem — implementation-free and absent design. This is what separates market requirements from specifications and prevents product managers from overstepping into design territory.

**The test:** If your requirement describes buttons, screens, algorithms, data models, or architecture, it has crossed into specification territory. Strip it back to the underlying problem.

**Why this matters:**
- Developers cannot and should not program to marketing-flavored specs
- Prescribing solutions robs the development and design team of the opportunity to innovate
- Combined "ReqSpecs" create blame-sharing dysfunction instead of clear accountability
- When questions arise about implementation, the team should find the answer in the use scenario — not in a prescribed solution

---

## 2. The Use Scenario Format

The Pragmatic preferred format for requirements uses storytelling to put the reader in the customer's chair.

### Core Format

**[Persona] has this [problem] with [frequency]**

This simple structure forces three essential elements:
- **Who** experiences the problem (specific persona, not "the user")
- **What** the problem is (in the persona's business/personal terms)
- **How often** it occurs (frequency establishes urgency and business impact)

### Expanding the Story

The tone is always "imagine if you will..." followed by a description of the situation and the problem. Good use scenarios answer:

- What is the persona doing when this problem occurs?
- How does the persona handle it today (current workaround)?
- What is the cost or impact of the current situation?
- How might the persona prefer things to work? (This is directional, not prescriptive — it gives the designer intent without dictating implementation)

### Guiding Questions for Story Creation

When interviewing the user or constructing the scenario:
- "What is the persona trying to achieve?"
- "What goes wrong or gets in the way?"
- "How do they handle it now?"
- "How often does this happen?"
- "What does it cost them (time, money, risk, frustration)?"

---

## 3. Crafting Individual Requirements

### Length and Structure

Each requirement should be:
- **Short** — one to two paragraphs, never more than a page or two
- **Written in the persona's language** — business or personal terms, not technical jargon
- **Self-contained** — a reader should understand the problem without needing to read other requirements
- **Linked to a persona** — every requirement must specify which persona experiences the problem

### Anatomy of a Well-Written Requirement

1. **Persona identification** — who experiences this problem
2. **Problem statement** — what is going wrong, in the persona's terms
3. **Context / use scenario** — the story of when and how the problem occurs
4. **Frequency** — how often the problem manifests
5. **Impact** — what the problem costs the persona (time, money, risk, missed opportunity)
6. **Current workaround** (optional but valuable) — how the persona copes today
7. **Supporting evidence** — number of sites/customers reporting this problem, source of the data

### What NOT to Include in the Requirement

- Proposed solutions, UI mockups, or wireframes
- Technical implementation details
- Database schemas, API definitions, or architecture
- Specific product feature names (use problem language instead)
- Marketing copy or sales positioning

---

## 4. Requirement Types Beyond Functional

Most product managers naturally write functional requirements — the observable capabilities a persona needs. But a complete MRD also considers non-functional requirement types:

### Standard Types (IEEE-recognized)

**Functional:** Observable capabilities needed for the persona to complete goals or perform the task in the use scenario.
Example: "Regional managers need to compare performance across their 15-20 store locations on a single view, which they do every Monday morning."

**Performance:** Capacity, speed, and concurrency characteristics.
Example: "During month-end close, the accounting team of 40 people all access the reconciliation module simultaneously, and the current 30-second load time causes them to lose an estimated 2 hours per person."

**Constraints:** Conditions that legitimately limit the design.
Example: "Field technicians work in areas with intermittent connectivity, so any solution must work offline for periods of up to 4 hours."

**Interface:** Defined interactions with other hardware or software.
Example: "Warehouse operators scan items with Zebra TC52 handhelds, which must communicate with the inventory system in real time."

**Security:** Compliance and privacy requirements.
Example: "Healthcare administrators must ensure that patient data access is logged per HIPAA audit requirements, which are subject to annual compliance reviews."

### Additional Types for Software Products

Consider also capturing requirements related to:
- **Standardization** — industry or format standards the product must support
- **Certification** — regulatory certifications required for the target market
- **Installation** — how the product is deployed and configured
- **Implementation** — professional services needs for customer onboarding
- **Customization** — how customers need to tailor the product
- **Localization** — language, currency, date format, and cultural requirements
- **Documentation** — what written guidance users and admins need
- **Education** — training needs for users and administrators

---

## 5. The SMART Test

Before finalizing a requirement, evaluate it against the SMART criteria:

**Specific:** Does the requirement specify what it aims to achieve? Can the reader clearly understand what problem needs solving?

**Measurable:** Does the requirement provide a metric by which all stakeholders can determine if objectives are being met? How will we know when this problem is solved?

**Achievable:** Are the objectives achievable given current technology, skills, and constraints?

**Realistic:** Are the objectives realistic with respect to available resources and timeline?

**Time-bound:** When will the team achieve the objectives? Is there a release or timeframe associated?

A requirement that passes SMART gives the designer enough information to make decisions without turning to the product manager continuously throughout the day.

---

## 6. Common Writing Mistakes

### Mistake: Solution Masquerading as Requirement
- **Bad:** "Add a CSV export button to the reports page"
- **Good:** "Sales managers need to share weekly pipeline data with their VPs who use Excel for analysis. This happens every Friday and currently requires manual re-typing of 50+ rows."

### Mistake: Vague Problem Statement
- **Bad:** "Users need better reporting"
- **Good:** "Regional managers (persona: Rachel) spend 3+ hours each Monday manually aggregating data from 5 separate screens to build their weekly performance summary for leadership."

### Mistake: Missing Persona
- **Bad:** "The system should support single sign-on"
- **Good:** "IT administrators (persona: Derek) manage SSO across 40+ enterprise applications. Adding each new application requires a separate configuration process that takes 2-3 hours. They onboard 5-10 new applications per quarter."

### Mistake: No Frequency or Impact
- **Bad:** "Customers want mobile access"
- **Good:** "Field sales reps (persona: Marcus) visit 6-8 client sites per day and need to check inventory availability before making promises. Currently they call the office, wait on hold for an average of 12 minutes, and sometimes lose the sale."

### Mistake: Embedded Design Decisions
- **Bad:** "Implement a drag-and-drop dashboard builder with widget library"
- **Good:** "Marketing analysts (persona: Priya) need to create custom views of campaign performance tailored to different stakeholders. Each stakeholder cares about different metrics, and Priya currently creates 5-7 separate static reports per week manually."

---

## 7. Worked Examples

### Example 1: B2B SaaS — Data Integration Problem

**Persona:** Alex, Integration Engineer at a mid-market retail company

**Requirement:**
Alex manages data connections between the company's e-commerce platform, inventory system, and accounting software. When a new data source is added — which happens roughly quarterly as the company acquires new brands — Alex must write custom transformation scripts from scratch because the current system has no mapping templates. Each new integration takes 3-4 weeks of development time and introduces errors that take another 1-2 weeks to resolve. The company has 3 new brand acquisitions planned for next year.

**Evidence:** Reported by 8 out of 12 integration-focused customers interviewed. Also cited as primary loss reason in 3 of last quarter's 7 competitive losses.

### Example 2: Consumer Product — Onboarding Problem

**Persona:** Jamie, first-time user of a personal finance app

**Requirement:**
Jamie downloads the app after hearing about it from a friend. During first-time setup, Jamie needs to connect bank accounts to see a consolidated view of spending. The current account-linking process requires Jamie to locate routing numbers and enter them manually, which Jamie doesn't know how to find. Jamie tries for about 5 minutes before abandoning setup. This happens at the critical moment of first use — there is no second chance at first impression.

**Evidence:** Analytics show 62% of new users drop off during the account-linking step. Support tickets for "how do I connect my bank" are the #1 category at 340/month.

### Example 3: Existing Product — Performance Problem

**Persona:** Dana, Accounting Manager overseeing month-end close

**Requirement:**
Dana's team of 12 accountants all access the reconciliation module during the last 3 days of each month. During this period, page load times increase from 2 seconds to over 30 seconds, and the system occasionally times out entirely. Each timeout costs approximately 15 minutes of rework as unsaved entries are lost. Dana estimates the team loses a collective 20+ hours per month-end cycle to performance issues, extending the close process by a full day.

**Evidence:** Reported by 15 of 20 enterprise customers in the most recent feedback survey. 4 customers listed this as their primary reason for evaluating competitors.
