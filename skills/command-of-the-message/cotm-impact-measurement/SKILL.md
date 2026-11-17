---
name: cotm-impact-measurement
description: >
  Measure the impact of a Command of the Message rollout: setting baselines before training, choosing
  leading indicators (certification, CRM value-field completion, call scorecard ratings, coaching cadence,
  discovery quality) and lagging indicators (win rate, average deal size, sales cycle length, discounting,
  ramp time, forecast accuracy, net revenue retention), comparing cohorts, building a sales methodology
  dashboard, and reporting ROI to executives and boards. Use this skill whenever the user asks how to
  measure a sales methodology, prove the ROI of CotM or value selling, build a value selling scorecard or
  dashboard, set KPIs for sales enablement, compare certified vs. uncertified reps, or report methodology
  results to leadership.
---

# Impact Measurement — Command of the Message, Step 8

Command of the Message is an investment in time, training and process change. Measuring it shows whether behavior is changing (leading indicators) and whether that change is moving revenue (lagging indicators), so leaders can keep investing and fix what isn't working.

**Output:** a measurement plan with baselines and targets, a dashboard specification, and a reporting cadence.

## Workflow

### 1. Capture baselines before training

Pull at least two to four quarters of history for the lagging indicators below, segmented by team, region, segment and deal type. Without a baseline the program can't show its impact. If data quality is poor, say so and agree on the best available proxy.

### 2. Choose indicators

**Leading indicators (behavior; visible in weeks):**

| Indicator | Source | Why it matters |
|---|---|---|
| Certification rate by team | Enablement records | Readiness to use the message |
| Opportunities with confirmed PBO and metric | CRM | Value captured in real deals |
| Value-field completion at each stage | CRM | Process adoption |
| Average call scorecard rating | Call reviews / conversation intelligence | Quality of execution |
| Coaching sessions completed | Manager logs | Reinforcement is happening |
| Economic buyer engagement rate | CRM | Message reaching decision makers |

**Lagging indicators (results; visible in quarters):**

| Indicator | Definition |
|---|---|
| Win rate | Closed-won ÷ (closed-won + closed-lost), overall and in competitive deals |
| Average deal size | Average contract value of closed-won deals |
| Sales cycle length | Median days from opportunity creation to close |
| Discount rate | Average discount off list on closed-won deals |
| Ramp time | Days for new hires to reach a set productivity milestone |
| Forecast accuracy | Actual vs. forecast at a fixed point in the quarter |
| Pipeline conversion | Stage-to-stage conversion rates |
| Net revenue retention | For teams where CS uses PBOs and metrics in renewals |

Pick a handful that match the goals in the rollout charter (`cotm-executive-alignment`). Too many metrics dilute attention.

### 3. Set targets and attribution approach

Set realistic targets per quarter. Because many factors affect revenue, use comparisons that make attribution more credible:

- **Before vs. after** for the same teams, adjusted for seasonality.
- **Certified vs. not-yet-certified** reps or teams in a staggered rollout.
- **Deals with confirmed PBO and metric vs. deals without** — win rate, size and cycle.

Report correlations honestly; don't claim causation the data can't support.

### 4. Specify the dashboard

Use `templates/measurement-plan.md`. A useful dashboard has three views: adoption (leading), outcomes (lagging), and the link between them (e.g. win rate for deals with vs. without confirmed metrics). Work with RevOps to build it in the CRM or BI tool.

### 5. Report and act

- **Monthly:** leading indicators to sales leadership and managers; act on adoption gaps through coaching (`cotm-coaching-reinforcement`).
- **Quarterly:** lagging indicators and the leading-to-lagging link to the executive sponsor; decide on refreshes and investment.
- **Annually:** program ROI to the executive team or board.

A simple ROI view: incremental revenue (e.g. change in win rate × pipeline × average deal size, plus deal-size uplift) and reduced discounting, compared with program cost. State assumptions clearly.

## Common mistakes

- Skipping the baseline.
- Reporting only activity (sessions attended) instead of behavior and results.
- Claiming all revenue growth for the methodology.
- Measuring once at the end instead of tracking trends.
- Ignoring data quality in value fields.

## Related skills

- `cotm-executive-alignment` for goals and targets in the charter.
- `cotm-sales-process-integration` for the CRM fields that feed the dashboard.
- `pragmatic-measurement` and `pragmatic-business-outcomes` for broader measurement design.

## Using AI in this step

- Analyze CRM exports to compare deals with and without confirmed value elements.
- Draft monthly and quarterly reports from dashboard data.
- Detect copy-paste or low-quality value fields that inflate adoption numbers.

Check AI calculations against the source data and keep revenue data in approved tools.

## Template files

- `templates/measurement-plan.md` — Baselines, targets, dashboard views and reporting cadence.
