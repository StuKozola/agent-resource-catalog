# Customer Satisfaction Program Plan

> **Pragmatic Framework focus area:** Customer Satisfaction (Go-to-Market)
> **Focus-area question:** *How do customers judge their experience with the product and their relationship with us?*
> Instructions: Replace bracketed placeholders. Keep the plan to a few pages; detail lives in the dashboards and issue tracker it points to. Delete this block before use.

---

## 1. Overview

| | |
|---|---|
| **Product(s) / portfolio** | [ ] |
| **Customer segments in scope** | [ ] |
| **Program owner** | [Name, role] |
| **Contributors** | [Customer success, support, product, sales, marketing] |
| **Plan period** | [ ] |
| **Date / version** | [ ] |

### Why this program, now
[2–3 sentences: what we know or suspect about satisfaction today, and what decisions this program will inform.]

---

## 2. What We Measure and Why

### Satisfaction dimensions
| Dimension | What it means for our customers | How we'll know |
|---|---|---|
| Product experience | [e.g., reliability, ease of use, fit to workflow] | [CSAT after release, CES, verbatims] |
| Service experience | [support, onboarding, account management] | [CSAT/CES after cases, onboarding survey] |
| Trust | [we deliver what we promise, are transparent] | [relationship survey items, escalation tone] |
| Relationship health | [overall account health] | [health score] |

### Personas surveyed
| Persona | Role in account | Survey type | Notes |
|---|---|---|---|
| [Executive sponsor / economic buyer] | | Relationship | |
| [Admin / technical owner] | | Relationship + transactional | |
| [End user] | | Transactional / in-product | |

### Boundaries
- Outcome achievement is tracked in Customer Value Realization (`pragmatic-customer-value-realization`): [link to success plans].
- Usage and renewal are tracked in Adoption / Retention: [link].
- Recommendations, references and reviews are signals we track below; they are not our satisfaction measure.

---

## 3. Measurement Plan

| Measure | Definition | Trigger / cadence | Sample | Baseline | Target | Data owner |
|---|---|---|---|---|---|---|
| CSAT — support | % 4–5 on 5-point scale | After case close | All cases | | | |
| CSAT — onboarding | | At onboarding complete | | | | |
| CES | | After support / setup | | | | |
| NPS (relationship) | % promoters − % detractors | [Quarterly / semiannual] | [All key contacts] | | | |
| Relationship health score | [Inputs and weights] | Monthly | All accounts | | | |
| Trust index | [Survey items] | Annual | Key contacts | | | |
| Qualitative interviews | Structured, satisfied/neutral/unhappy mix | [N per quarter] | | — | | |

**Survey fatigue rules:** [max surveys per contact per period; suppression rules]

---

## 4. Issue Detection and Triage

| Signal | Threshold | Who is alerted | Response time | First action |
|---|---|---|---|---|
| Detractor response | NPS 0–6 | CSM | [2 business days] | Personal follow-up call |
| Health score drop | [e.g., green → yellow or ↓15 pts] | CSM + manager | [5 days] | Account review |
| Repeated support contacts | [3+ on same issue in 30 days] | Support lead | | Root cause review |
| Exec sponsor change or silence | | Account owner | | Re-establish sponsor |
| Negative public review | | Marketing + CS | | Respond; contact customer |

**Routing:** customer-specific fixes → CS/support; systemic issues → [product / operations / policy owner]; critical issues → Escalations (`pragmatic-escalations`).

---

## 5. Closing the Loop

**Inner loop (individual customers):** [who contacts, within what time, how actions are recorded]

**Outer loop (organization):**
| Step | Cadence | Owner | Output |
|---|---|---|---|
| Theme analysis of scores and verbatims | Monthly | | Top themes by persona/segment |
| Satisfaction review (CS, product, support, sales) | Quarterly | | Actions with owners |
| Feed systemic themes to Market Problems / Requirements | Quarterly | Product | Logged problems |
| "You said, we did" communication to customers | [Quarterly] | | Customer update |

---

## 6. Signals of Satisfaction: Advocates, References and Reviews

| Signal | Current | Target | Source |
|---|---|---|---|
| Active advocates / reference customers | | | Advocacy tracker |
| Reference requests fulfilled within SLA | | | |
| Third-party review rating and volume | | | [G2, Peer Insights, etc.] |
| Advocacy requests declined (investigate reasons) | | | |

Advocate program detail: `templates/advocacy-scorecard-template.md`. Case studies are produced with Assets (`pragmatic-assets`).

---

## 7. Reporting

| Audience | Format | Cadence | Contents |
|---|---|---|---|
| CS and support teams | Dashboard | Weekly | Open issues, detractor follow-up status |
| Product and leadership | Satisfaction review | Quarterly | Trends, themes, actions, loop closure |
| Executive team | Summary | Semiannual | Satisfaction, trust and health trends vs. targets |

---

## 8. Risks and Dependencies

| Risk / dependency | Impact | Mitigation |
|---|---|---|
| [Low response rates from executive sponsors] | | |
| [Health score inputs incomplete] | | |
| [No owner for systemic themes] | | |

---

## 9. Next Review

[Date and what will be decided at that review.]
