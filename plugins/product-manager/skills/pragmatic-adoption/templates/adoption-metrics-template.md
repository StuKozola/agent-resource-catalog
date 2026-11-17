# Adoption Metrics Definition — [Product]

*Adoption focus area (Enablement), 2027 Pragmatic Framework. Plugs into the indicator framework in `pragmatic-measurement`.*

## 1. Units of analysis
- **User:** how a user is identified (and how shared/service accounts are excluded)
- **Account:** how users roll up to customers or (internal) teams/departments
- **Start date:** signup / contract / provisioning / go-live (pick one per segment and state it)
- **Intended population:** licensed seats, or for internal products the target employee group

## 2. Meaningful-use definitions

| Persona | Activation event (exact event + threshold + window) | Core action | Expected rhythm | Why this reflects value |
|---|---|---|---|---|
| e.g., Analyst | `report_shared` ≥1 within 14 days of start | `report_viewed_by_recipient` | Weekly | Sharing = solved "get numbers to team" problem |
| | | | | |

Validation: how was the activation event chosen? (retention comparison, customer interviews, or hypothesis to revisit after first cohorts)

## 3. Metric catalog

| Metric | Formula | Segment cuts | Source | Cadence | Target | Leading or lagging | Owner |
|---|---|---|---|---|---|---|---|
| Activation rate | activated in N days / started | persona, segment, channel | product analytics | weekly | | Leading | |
| Time to value | median days start → activation | segment, onboarding path | | weekly | | Leading | |
| Week-N / month-N retention | cohort still doing core action in period N / cohort size | cohort, persona | | monthly | | Leading | |
| Breadth | active users / intended users | account size | | monthly | | Leading | |
| Depth | key workflows used / relevant workflows | use case | | monthly | | Leading | |
| Frequency / stickiness | WAU/MAU or core actions per user per period | persona | | monthly | | Leading | |
| Feature adoption (key features) | accounts using X / accounts where X relevant | release age | | monthly | | Leading | |
| License utilization | active seats / purchased seats | renewal quarter | | monthly | | Leading (for renewal) | |

## 4. Account adoption health (B2B)
| Input | Weight | Green | Yellow | Red |
|---|---|---|---|---|
| Key personas activated | | | | |
| Breadth | | | | |
| Depth | | | | |
| 90-day trend | | | | |
| Active sponsor | | | | |

## 5. Qualitative signals
- Onboarding survey questions:
- Stalled-user interview cadence and owner:
- Unanticipated-use capture (source, reviewer, routing):

## 6. Data quality notes
- Known gaps in tracking, test accounts to exclude, definition changes and dates.

## 7. Decision rules
- If activation < [x]% for two cohorts → review onboarding path and interview stalled users.
- If cohort curve doesn't flatten by month [n] → review requirements and positioning.
- If breadth < [x]% at day 90 → sponsor review; check old process is retired.
