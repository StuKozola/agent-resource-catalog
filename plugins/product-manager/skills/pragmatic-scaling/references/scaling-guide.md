# Scaling Guide

Deeper guidance for the Scaling focus area (Operations) of the 2027 Pragmatic Framework. Draws on product operations, SRE and customer success practice.

## 1. Three dimensions of scaling

| Dimension | Question | Examples of strain |
|---|---|---|
| **Reach** | Can more customers, users, segments and regions get and use the product? | Onboarding queue, localization, compliance per region, partner coverage |
| **Reliability** | Does the product keep working as load and complexity grow? | Latency, outages, data errors, integration failures, slow releases |
| **Efficiency** | Does the cost and effort to deliver value grow slower than demand? | Tickets per account rising, headcount growing with customers, margin squeeze |

A good assessment covers all three. Teams usually over-index on reliability and miss efficiency.

## 2. Demand drivers

Scale each driver separately; they rarely grow together.
- Number of customers/accounts
- Users per account
- Transactions, events or data volume per user
- Number of integrations and configurations in use
- Customer size and complexity (enterprise, regulated)
- Geographic and language coverage
- Number of products/SKUs and partners

## 3. Capacity math for human processes

For any recurring human process:

- **Workload** = volume per period × effort per unit
- **Capacity** = people × productive hours per period × utilization (plan at 70–80%, not 100%)
- **Breakpoint volume** = capacity / effort per unit

Example: onboarding takes 12 hours per customer. Two onboarding specialists at 130 productive hours/month at 75% utilization → ~195 hours → ~16 customers/month. If sales forecasts 30/month next half, the breakpoint arrives the month bookings exceed 16.

Add **lead time**: hiring (2–4 months) + ramp (1–3 months). Action must start lead-time months before the breakpoint.

For queues, remember that wait times grow sharply as utilization approaches 100%. A team "almost keeping up" is already giving customers long waits.

## 4. Leading indicators of strain

| Area | Leading indicator |
|---|---|
| Onboarding | Time from contract to go-live; backlog of accounts waiting; activation rate falling (see `pragmatic-adoption`) |
| Support | Tickets per account or per 1,000 users; first-response time; reopen rate; share of "how do I" tickets |
| Reliability | Error rates, latency percentiles, incident frequency, change failure rate, error-budget burn |
| Delivery team | Overtime, on-call load, single-person dependencies, time spent on unplanned work (toil) |
| Commercial | Cost to serve per account; gross margin by segment; discounting to offset service issues |
| Customer | Satisfaction trend (`pragmatic-customer-satisfaction`), escalation rate (`pragmatic-escalations`), value realization (`pragmatic-customer-value-realization`) |

Set a threshold for each that triggers action (e.g., "onboarding backlog > 3 weeks").

## 5. Common breakpoints by function

- **Product:** hard-coded configuration, no bulk operations, no self-service admin, performance limits on large accounts, single-tenant assumptions.
- **Onboarding/implementation:** bespoke project for every customer; data migration by hand; custom integrations.
- **Support:** knowledge in a few heads; no deflection content; tiering absent; product gaps handled as tickets.
- **Billing and contracts:** custom terms per deal; manual invoicing; usage metering in spreadsheets.
- **Sales and presales:** custom demos and POCs per deal; security questionnaires answered from scratch.
- **Engineering operations:** manual deployments; no capacity monitoring; on-call burnout.
- **Partners:** no certification or standard playbook, so partner quality varies (`pragmatic-channel-support`).

## 6. Standardize, automate or productize: decision criteria

| Signal | Likely choice |
|---|---|
| Same outcome done many different ways | Standardize first |
| Standard process, high volume, internal effort only | Automate (internal tooling) |
| Customers wait on us for something they could do themselves | Productize (self-service) |
| Work happens because the product lacks a capability many customers need | Productize via `pragmatic-requirements` |
| Requires judgment, relationships or expertise | Staff, train, or use partners; standardize the parts around the judgment |
| Serves a small, low-value variant | Consider stopping; raise with `pragmatic-product-strategy` |

Score candidates by **annual effort removed** (hours × cost), **customer impact** (wait time, error risk), **breakpoint urgency** and **cost to implement**. Productization usually has the highest payoff but the longest lead time, so start it early.

## 7. Toil (from SRE practice)

Toil is work that is manual, repetitive, automatable, tactical, has no lasting value and grows linearly with scale. Track the share of each team's time spent on toil. A common guideline is to keep it below about half; rising toil is an early warning that growth is being absorbed by people, not systems.

## 8. Planning capacity ahead of demand

1. Take the demand forecast from `pragmatic-growth` / `pragmatic-adoption` and the roadmap.
2. Translate into load on each process and component.
3. Compare to current capacity; mark breakpoint dates.
4. Subtract lead times to get "start by" dates.
5. Choose actions (section 6) and assign owners.
6. Set leading-indicator thresholds to confirm or accelerate the plan.
7. Revisit quarterly; forecasts move.

Plan for upside: if growth beats the forecast, which breakpoint comes first, and what is the fastest mitigation?

## 9. Internal platforms

- Treat each newly onboarded team as a customer with its own onboarding and support load.
- Publish standard interfaces, templates and self-service paths early; bespoke integrations per team don't scale.
- Formalize governance (access, data ownership, change management) before the third or fourth team, not after an incident.
- Track platform-team capacity versus demand like any other process.

## 10. Making the case

Frame scaling investments as:
- **Customer impact avoided** — wait times, outages, failed onboardings
- **Cost avoided** — hires not needed, margin protected
- **Growth enabled** — segments or volumes the business can now take on

Pair each with evidence from the inventory and the leading indicators.
