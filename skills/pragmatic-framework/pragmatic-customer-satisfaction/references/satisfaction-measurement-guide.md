# Satisfaction Measurement Guide

How to measure customer satisfaction, trust and relationship health; spot issues early; and close the loop. Used in Steps 2–5 of `pragmatic-customer-satisfaction`.

## Table of Contents

1. [What You Are Measuring](#what-you-are-measuring)
2. [Core Measures](#core-measures)
3. [Relationship Health Scores](#relationship-health-scores)
4. [Qualitative Feedback](#qualitative-feedback)
5. [Survey Design and Cadence](#survey-design-and-cadence)
6. [Issue Detection and Triage](#issue-detection-and-triage)
7. [Closing the Loop](#closing-the-loop)
8. [Common Measurement Mistakes](#common-measurement-mistakes)

---

## What You Are Measuring

Customer satisfaction is the customer's **own judgment** of two things after purchase, adoption or continued use:

- **Their experience with the product** — does it work well, is it easy, does it do what they expected?
- **Their relationship with your organization** — do they trust you, feel heard, get good service, find you easy to work with?

Keep three distinctions clear:

| It is not… | Because… | Where that lives |
|---|---|---|
| Whether they achieved their outcomes | A customer can be satisfied without results yet, or get results and still be unhappy with you | Customer Value Realization (`pragmatic-customer-value-realization`, Operations) |
| Whether they keep using the product | Usage is behavior; satisfaction is judgment. They diverge (locked-in but unhappy; happy but low-need) | Adoption (`pragmatic-adoption`, Enablement), Retention (`pragmatic-retention`, Go-to-Market) |
| Whether they'll recommend you or give a reference | Recommendation is one signal of satisfaction, shaped by company policy, personality and opportunity | Advocate and reference program (`references/advocacy-program-guide.md`) |

## Core Measures

| Measure | Question it answers | Typical form | Best used | Watch out for |
|---|---|---|---|---|
| **CSAT** (Customer Satisfaction Score) | How satisfied were you with this interaction / this product? | 1–5 scale; % scoring 4–5 | After specific touchpoints: onboarding, support case, release, renewal | Measures moments, not the whole relationship |
| **NPS** (Net Promoter Score) | How likely are you to recommend us? | 0–10; % promoters (9–10) minus % detractors (0–6) | Relationship survey, quarterly or semiannually | A recommendation-intent proxy, not satisfaction itself; noisy in small B2B samples; cultural scoring differences |
| **CES** (Customer Effort Score) | How easy was it to get done what you needed? | 1–7 agreement scale | After support, setup, billing, renewal | Narrow; pair with CSAT |
| **Relationship health score** | Is this account's relationship healthy? | Composite (see below), green/yellow/red | Account-level, monthly | Only as good as its inputs; validate against churn and expansion |
| **Trust indicators** | Do they believe what we tell them and expect us to deliver? | Survey items ("I trust [company] to…"), escalation tone, contract behavior | Annual relationship survey, executive reviews | Easy to skip; often the first thing to erode |
| **Qualitative feedback** | Why do they feel this way? | Interviews, verbatims, CSM notes, reviews | Always, alongside scores | Anecdotes without counts mislead |

**B2B note:** measure at both the **person** level (each persona: buyer, admin, end user, executive sponsor) and the **account** level. A happy end user and an unhappy economic buyer is a renewal risk.

## Relationship Health Scores

A composite, account-level indicator. Build it from inputs you already have, weight them, and validate the weights against what actually happened (renewals, churn, expansion).

| Input | Example signal | Example weight |
|---|---|---|
| Survey sentiment | Latest CSAT/NPS from key contacts, trend | 25% |
| Support experience | Open critical cases, escalations, CES, time to resolve | 20% |
| Engagement with you | Exec sponsor engagement, QBR attendance, responsiveness | 20% |
| Product experience | Usage trend, reliability incidents affecting them | 20% |
| Commercial signals | Payment issues, renegotiation requests, budget cuts | 15% |

Rules:
- Publish the definition so CS, sales and product read it the same way.
- Re-validate weights at least yearly.
- A score change should trigger a named action, not just a color change.

## Qualitative Feedback

Scores tell you *that*; conversations tell you *why*.

- **Sources:** open-text survey answers, CSM and account notes, support tickets, executive business reviews, advisory boards, user communities, third-party reviews, churn and win/loss interviews.
- **Interviews:** a small number of structured conversations each quarter across satisfied, neutral and unhappy customers. NIHITO (Nothing Important Happens In The Office) applies after the sale too.
- **Coding:** tag verbatims by theme (product quality, ease of use, support, account management, billing, trust) and by persona; count them so themes can be prioritized.

## Survey Design and Cadence

- Keep surveys short: one score, one "why", optionally one "what should we do differently?"
- Separate **transactional** surveys (after a touchpoint) from **relationship** surveys (periodic, whole-relationship).
- Sample deliberately: every persona, every segment, not just your friendliest contacts.
- Cap survey frequency per contact (e.g., one relationship survey per half-year, transactional surveys suppressed after a recent one).
- Track response rate; falling response rates are themselves a relationship signal.

| Cadence | What |
|---|---|
| Continuous | Transactional CSAT/CES after support, onboarding, key releases |
| Monthly | Relationship health score refresh; issue review |
| Quarterly | Relationship survey wave (or rolling); theme analysis; satisfaction review with product, CS, sales |
| Annually | Full relationship and trust study; re-validate health score weights; reset targets |

## Issue Detection and Triage

Look for issues that could damage the relationship before they become churn or escalations:

- Score drops (individual or account) beyond a set threshold
- Detractor responses or negative verbatims from key personas
- Repeated support contacts on the same problem; rising effort scores
- Executive sponsor change, silence or missed meetings
- Negative public reviews or community posts
- Advocacy requests declined without a clear reason

Triage each into: **fix for this customer now** (CS/support owns), **systemic issue** (route to product, operations or policy owners; may become an Escalation, `pragmatic-escalations`, or a requirement), or **watch**.

## Closing the Loop

**Inner loop (the customer):** acknowledge feedback quickly, especially detractors (target: contact within 2–5 business days), agree what will happen, follow up when it's done.

**Outer loop (the organization):** aggregate themes monthly or quarterly, assign owners, decide actions, and report back — to the teams who own the fix and to customers ("you told us…, we did…"). Systemic themes should feed Market Problems (`pragmatic-market-problems`) and Requirements (`pragmatic-requirements`).

Track loop closure: % detractors contacted within target, % themes with an owner and action, time from theme to fix.

## Common Measurement Mistakes

1. **Equating NPS with satisfaction.** It's a recommendation-intent signal; use it alongside CSAT, CES, health and qualitative feedback.
2. **Surveying only champions.** Inflates scores and hides risk in other personas.
3. **Scores without action.** Measuring without closing the loop teaches customers not to respond.
4. **Account averages that hide individuals.** One unhappy sponsor outweighs many happy users at renewal.
5. **Confusing satisfaction with outcomes.** Satisfied customers can still fail to get value; check Customer Value Realization separately.
6. **Gaming.** Asking for scores ("please give us a 10") destroys the signal.
