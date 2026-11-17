# Severity Matrix and Escalation Runbook — [Product / Organization]

*Escalations focus area (Operations), 2027 Pragmatic Framework. Keep this to a few pages so it can be used under pressure.*

## Part 1: Severity matrix

| Level | Definition (customer and business impact) | Examples | Response time (acknowledge / engage) | Engaged | Notified | Customer update cadence | Leadership update |
|---|---|---|---|---|---|---|---|
| **Sev 1 — Critical** | Widespread outage or data loss/exposure; safety, security or regulatory impact; no workaround; or strategic account at immediate risk | Core service down for all; data breach; key renewal blocked by failure | 15 min / 30 min, 24×7 | Escalation owner, tech lead, comms lead, product lead, customer owners, exec sponsor | Exec team, Sales/CS leaders | Every 30–60 min until resolved | Immediately, then every 1–2 h |
| **Sev 2 — High** | Major function impaired for many customers or a key account; painful or no workaround | Reporting broken for a segment; key account cannot go live | 1 h / 2 h, business hours + on-call | Escalation owner, tech lead, customer owner, product lead | Function heads | Every 2–4 h | Daily summary |
| **Sev 3 — Medium** | Limited impact; workaround exists; single account or minor function | Integration failing for one customer with manual workaround | 1 business day | Support + owning team | Customer owner | Daily or on change | Weekly report |
| **Sev 4 — Low / concern** | Risk or stakeholder concern needing coordinated answer, no current customer harm | Exec raises concern about upcoming change; partner flags risk | 2 business days | Named owner | Relevant stakeholders | As agreed | As needed |

**Upgrade triggers:** spreading scope, data involvement, regulator or media attention, key renewal at risk, SLA breach imminent.
**Who can declare:** any support engineer, CSM, account owner, engineer on call, or product manager. Anyone can raise; the escalation owner confirms.

## Part 2: Roles and contacts

| Role | Primary | Backup | How to reach |
|---|---|---|---|
| Escalation owner (on-call rotation) | | | |
| Technical lead(s) by area | | | |
| Communications lead | | | |
| Product lead | | | |
| Executive sponsor (Sev 1) | | | |
| Legal / security (data, regulatory) | | | |

## Part 3: Runbook

1. **Raise.** Open an escalation in [tool] with: what's happening, who's affected, since when, evidence, suspected severity.
2. **Triage (≤ 15 min for suspected Sev 1).** Escalation owner confirms severity, opens coordination channel/bridge [location], assigns roles.
3. **Notify.** Per the matrix. First customer update within [x] min for Sev 1/2, even if cause is unknown.
4. **Work the problem.** Technical lead drives diagnosis; escalation owner tracks actions and decisions in the channel; scribe keeps timeline.
5. **Decide.** Decision rights:
   - Rollback / feature flag / hotfix scope: [technical lead + product lead]
   - Customer credits or commercial remedies: [exec sponsor / finance]
   - Temporary exceptions: per `pragmatic-exceptions` approval matrix (log them)
   - Public statement: [comms + legal]
6. **Communicate.** On cadence, using templates (status, impact, action, workaround, next update).
7. **Resolve and monitor.** Confirm fix with affected customers; monitor for recurrence for [period].
8. **Close.** Final update to customers and leaders; schedule review (Sev 1/2 within 5 business days).
9. **Review.** Use `post-escalation-review-template.md`; route action items.

## Part 4: Customer escalation (non-incident) path

1. Customer owner logs the escalation with the customer's desired resolution in their words.
2. Assign escalation owner and, for strategic accounts, an executive sponsor.
3. Joint recovery plan with milestones shared with the customer within [x] days.
4. Weekly internal review until resolved; product attends when a capability gap is involved.
5. Close with the customer's confirmation; run a review; update the account plan (`pragmatic-retention`).

## Part 5: Communication templates

**Customer update:** Status — Impact — What we're doing — Workaround — Next update by [time].
**Executive summary:** Severity and name — Impact and exposure — Current action — Decisions needed — Next update.
**Internal talk track:** What to say / What not to say / Where to route questions / Commitments made.
