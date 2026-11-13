# Escalation Management Guide

Deeper guidance for the Escalations focus area (Operations) of the 2027 Pragmatic Framework. Draws on SRE incident management, customer success and support practice.

## 1. Designing severity levels

Good severity definitions are:
- **Impact-based** — defined by what customers and the business experience, not by which team is involved.
- **Observable** — a frontline person can apply them in minutes with partial information.
- **Tied to action** — each level specifies response time, who's engaged, who's notified and update cadence.

Impact dimensions to combine:
- **Scope:** one user / one account / a segment / all customers
- **Harm:** inconvenience / blocked work / financial loss / data loss or exposure / safety or regulatory
- **Workaround:** easy / painful / none
- **Strategic risk:** key account, renewal in progress, public visibility, regulator involved

Rule of thumb: when in doubt, declare higher and downgrade later. Downgrading is cheap; a slow start isn't.

Watch for severity inflation. If more than a small share of escalations are top severity, the definitions or the culture need attention.

## 2. Roles

| Role | Responsibility |
|---|---|
| **Escalation owner / incident commander** | Coordinates; makes sure the right people are engaged; tracks decisions and actions; doesn't fix the problem personally |
| **Technical lead** | Diagnoses and resolves; proposes options and risks |
| **Communications lead** | Writes and sends customer and stakeholder updates on cadence |
| **Customer owner** (account manager or CSM) | Owns the relationship with affected key accounts; brings customer context |
| **Product lead** | Supplies product and market context; makes or brokers product trade-offs; owns the learning loop into requirements and roadmap |
| **Executive sponsor** (top severities) | Unblocks resources, makes business calls (credits, contractual commitments), engages peer executives at the customer |
| **Scribe** (major incidents) | Keeps the timeline for the review |

## 3. RACI example

| Activity | Support | CS / Account | Engineering | Product | Sales | Leadership |
|---|---|---|---|---|---|---|
| Triage and declare severity | R | C | C | C | I | I |
| Coordinate response | A/R (owner) | C | R | C | I | I |
| Technical fix | I | I | A/R | C | I | I |
| Product trade-off (rollback, hotfix scope, flag) | I | C | R | A | I | C |
| Customer updates | R | A (key accounts) | C | C | I | I |
| Executive updates | C | C | C | C | I | A (sponsor) |
| Commercial remedy (credits, terms) | I | R | I | C | C | A |
| Post-escalation review | R | R | R | A (learning loop) or shared | C | I |
| Roadmap and requirements follow-up | I | C | C | A/R | I | I |

Adapt to your organization; what matters is that each row has exactly one "A."

## 4. Product's role in more detail

- **Before:** contribute to severity definitions; maintain a list of known limitations and workarounds; make sure support and CS know product scope (link to `pragmatic-assets`).
- **During:** identify affected personas and use cases; judge the impact of options on customers; decide on product changes in the moment; avoid making roadmap promises under pressure without checking capacity.
- **After:** own or co-own the review's product findings; write requirements with evidence; argue for preventive work on the roadmap; tell customers what changed.

## 5. Communication principles

- **Lead with impact and next update time.** "Some customers can't export reports. We're working on it. Next update by 14:30 UTC."
- **Be specific and honest.** Say what you know and don't know. Don't speculate on cause publicly.
- **Keep cadence even with no news.** "No change; still investigating; next update at…" is better than silence.
- **One voice.** All external updates come from the communications lead or customer owner.
- **Close properly.** Final update: what happened, impact, resolution, what's next (review summary to follow for major incidents).

### Customer update template
> **[Status: Investigating / Identified / Monitoring / Resolved]** — [Product/feature] — [time, timezone]
> **Impact:** who is affected and how
> **What we're doing:**
> **Workaround:** (if any)
> **Next update:** by [time]

### Executive summary template (3–6 lines)
> **Sev[n] — [short name]** — started [time], status [state]
> Impact: [customers/segments, revenue or SLA exposure]
> Cause (if known) and current action:
> Decisions needed from leadership:
> Customer communications sent:
> Next update:

### Internal talk track
For sales and CS: what to say, what not to say, who to route questions to, and what has been promised.

## 6. Customer escalations (non-incident)

Some escalations aren't outages: a stalled implementation, a long-running unresolved problem, a key account threatening to leave. Treat them with the same structure:
- Name an owner and an executive sponsor.
- Write down what the customer needs to see to consider the issue resolved (connect to `pragmatic-customer-value-realization`).
- Agree a joint recovery plan with dates; share it with the customer.
- Review weekly until resolved; then run a review like any other escalation.

## 7. Blameless post-escalation review

Principles:
- Assume people acted reasonably given what they knew. Ask "what made this the sensible action at the time?"
- Look for contributing factors, not a single root cause: product design, missing monitoring, process gaps, unclear ownership, training, scaling limits.
- Separate facts (timeline) from analysis.
- Review timing: within 5 business days for top severities while memory is fresh.

Useful questions:
- How did we find out? Could we have known sooner? Did the customer tell us first?
- Was severity right? Was the right owner engaged quickly?
- What slowed diagnosis or resolution?
- Did communication meet the cadence? What did customers say about it?
- What product capability, requirement or limitation contributed?
- Has this, or something like it, happened before?

Action items must be specific, owned, dated and routed (requirements, roadmap, operations, enablement). Track completion; report it in the quarterly trend review.

## 8. Trend analysis

Quarterly, look at:
- Volume by severity and type; time to detect, acknowledge, resolve
- Repeat causes and repeat customers
- Segments, personas and product areas most affected
- Action-item completion rate and age
- Customer outcomes after escalations (renewed, churned, satisfaction change)

Turn recurring themes into problem statements for `pragmatic-market-problems` and `pragmatic-requirements`; use reliability themes to justify `pragmatic-scaling` investments.

## 9. Internal products and platforms

- Define severity by business process impact (payroll blocked, close process delayed, regulatory filing at risk).
- Publish one intake path; discourage escalation through personal networks.
- Include the affected business owner as the "customer owner."
- Share reviews with the consuming teams; trust in an internal platform depends on visible learning.
