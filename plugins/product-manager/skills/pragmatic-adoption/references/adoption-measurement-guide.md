# Adoption Measurement Guide

Deeper guidance for the Adoption focus area (Enablement) of the 2027 Pragmatic Framework. Use with `pragmatic-measurement` (Business), which owns the overall indicator framework.

## 1. The adoption ladder

Think of adoption as a sequence. Each step has its own metric and its own failure mode.

| Stage | Question | Typical metric | Common failure |
|---|---|---|---|
| Access | Can they get in? | Accounts provisioned, seats assigned | SSO, permissions, procurement delays |
| Setup | Is it configured for their work? | Setup steps completed, integrations connected | Admin stalls; no data loaded |
| Activation | Have they experienced the core value once? | Activation rate, time to activation | Value is buried; first session confusing |
| Habit | Do they repeat the core action at the expected rhythm? | Core-action frequency, week-N retention | No trigger to return; old process still there |
| Breadth | Are the intended people using it? | Active users / intended users | Champion-only usage |
| Depth | Are they using the capabilities that solve their problem? | Workflows or key features used per account | Using a fraction; value capped |

## 2. Defining meaningful use

**Activation event.** Choose an action that (a) represents the customer experiencing the value they bought, (b) happens early, and (c) correlates with retention.

Method to choose an activation threshold when you have data:
1. List 5–10 candidate early actions (e.g., "imported data," "created 3 dashboards," "invited a teammate").
2. For each, compare 90-day (or renewal) retention of users/accounts who did it in their first N days versus those who didn't.
3. Vary the count (1, 3, 5) and window (7, 14, 30 days). Prefer the simplest action/threshold with a large retention gap and a meaningful share of users reaching it.
4. Sanity-check with customers: does this action actually mean they solved a piece of their problem? Correlation alone can mislead.

Without data (pre-launch): derive the activation event from `pragmatic-requirements` and `pragmatic-user-personas`: "the first time the persona completes the job they hired the product for." Revisit after 1–2 cohorts.

**Core action and frequency.** Set expected frequency from the natural rhythm of the problem. Examples: expense approval (weekly), payroll (per pay cycle), quarterly planning (quarterly), incident response (when incidents happen). For irregular problems, measure use *when the trigger occurs* rather than calendar frequency.

## 3. Metric formulas

- **Activation rate** = users (or accounts) reaching the activation event within N days / users (or accounts) that started in the period.
- **Time to value (TTV)** = median time from start (signup, contract, provisioning) to activation event. Track median and 75th percentile.
- **Breadth** = active users in period / licensed or intended users. For internal products, use the target population (e.g., all field reps).
- **Depth** = key workflows used / key workflows relevant to the account's use case. Define "key" from requirements, not from the feature list.
- **Stickiness** = DAU/MAU or WAU/MAU, only when daily/weekly use is the expected rhythm.
- **Cohort retention (week N / month N)** = share of a start cohort still performing the core action in period N.
- **Feature adoption** = accounts using feature X / accounts for which X is relevant. Report alongside time since release.
- **License utilization** = assigned seats actively used / purchased seats. Low utilization is a renewal risk signal for `pragmatic-retention`.

## 4. Reading cohort curves

- A curve that **flattens** means a durable core of users found value; work on raising the plateau and reaching it faster.
- A curve that **keeps declining** toward zero means no durable value for that cohort; look at requirements and positioning, not just onboarding.
- **Newer cohorts higher than older** means onboarding or product changes are working.
- Segment cohorts by persona, company size, channel, onboarding path (self-serve vs. guided) and use case. The average curve often blends a healthy segment with a failing one.

## 5. Account-level adoption health

For B2B, roll user metrics into an account view: activation of key personas, breadth, depth, trend over last 30/90 days, and presence of an active sponsor. Share with customer success and `pragmatic-retention`. Keep the scoring simple and explainable; a score nobody trusts won't drive action.

## 6. Diagnosing low adoption

1. **Locate the drop.** Which stage of the ladder loses the most people? Which segment?
2. **Talk to stalled users.** 5–10 short conversations usually reveal the pattern. Ask what they expected, what they tried, what they did instead.
3. **Classify the cause:**
   - *Value gap* — the product doesn't solve the problem well enough → `pragmatic-requirements`
   - *Usability or path gap* — value exists but is hard to reach → onboarding, in-product guidance, design
   - *Expectation gap* — positioning promised something else, or the wrong segment bought → `pragmatic-positioning`, `pragmatic-market-definition`
   - *Organizational gap* — no sponsor, no time, competing process, no incentive → change management with the customer
   - *Enablement gap* — partners or internal teams onboard customers inconsistently → `pragmatic-channel-support`, `pragmatic-assets`
4. **Pick one or two changes**, define the metric they should move, and recheck in the next cohort.

## 7. Unanticipated uses

Sources: support tickets, CS notes, community forums, unusual event sequences, exports, API usage, integration requests, sales calls mentioning "we also use it for…".

For each, record: who, what they're doing, what problem it solves, how many accounts, and whether it creates risk (security, data quality, performance, support load). Route new value to `pragmatic-market-problems`; route gaps and risks to `pragmatic-requirements` and, if they create one-off requests, `pragmatic-exceptions`.

## 8. Internal products and platforms

- **Population, not market.** Define the target population and measure breadth against it.
- **Mandates aren't adoption.** A mandate gets logins; meaningful use still needs the product to solve the job better than the workaround.
- **Retire the old path.** Plan when the legacy tool or spreadsheet is turned off, and what support exists at cutover.
- **Manager sponsorship.** Adoption follows what managers inspect. Give managers simple usage views for their teams.
- **Value to the organization.** Pair adoption with an outcome (cycle time, error rate, cost) so it connects to `pragmatic-business-outcomes`.

## 9. Behavior change basics

People change behavior when the new way is clearly better for *them*, easy to start, and reinforced. Practical levers:
- Reduce first-session effort (templates, sample data, defaults).
- Give a clear next step after each milestone.
- Build a trigger to return that fits the work (a scheduled report, an integration into tools they already use).
- Show progress and results ("you saved 4 hours this month").
- Reinforce socially: team visibility, champions, peer examples.
