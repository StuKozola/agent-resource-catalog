# Roadmap Formats for Stakeholder Communications
## Pragmatic Framework: Stakeholder Communications

The product roadmap is one of the most common and consequential forms of stakeholder communication. This reference covers format choices, audience-specific views, and Pragmatic Framework guidance on presenting the roadmap without creating false commitments.

---

## The Core Tension

Different audiences interpret roadmap information differently — which is one of the primary sources of stakeholder misalignment:

> "For most technical teams, the second quarter is when they work on a project from April to June, hoping to deliver it by late June or early July. For executives and marketing teams, second quarter means the project will be available on April 1 at 8:00am so they can start promoting it. And for sales teams, the second quarter means availability in mid-February so they can close deals April-June."
> — Steve Johnson, Pragmatic Institute

The implication: **the same roadmap creates different expectations in different audiences**. Stakeholder Communications must account for this.

---

## Format 1: Date-Driven Roadmap

**Structure**: Items organized by calendar period (Q1, Q2, H1, specific months).

**When to use**:
- Near-term releases where dates are well-understood and unlikely to change
- Internally, with engineering teams coordinating delivery schedules
- When executives need to align marketing or sales timelines to release windows

**Advantages**:
- Familiar and easy to read
- Enables timeline-dependent planning (campaigns, conferences, sales cycles)

**Risks**:
- Creates implicit commitments — dates become expectations
- When dates slip, credibility suffers
- Encourages stakeholders to plan to exact dates, which amplifies the impact of changes

**Best practices**:
- Add a clear disclaimer: *"Dates are estimates and subject to change."*
- Use quarter-level granularity rather than specific dates when possible
- Reserve date-driven views for near-term (current quarter) items only

---

## Format 2: Phase-Driven (Theme-Driven) Roadmap

**Structure**: Items organized into phases such as Now / Next / Later, or by named themes.

**When to use**:
- Communicating direction to external audiences (customers, partners)
- Executive or sales views where strategic direction matters more than specific dates
- Any roadmap where items beyond the current quarter are uncertain

**Advantages**:
- Communicates direction without locking to dates
- Resilient to change — reprioritization within a phase doesn't break stakeholder expectations
- Keeps conversation focused on strategy, not schedule

**Phase definitions** (common Pragmatic-aligned model):
| Phase | Meaning |
|---|---|
| **Now** | In active development; shipping in the near term (typically current quarter) |
| **Next** | Planned for the following period; requirements being finalized |
| **Later** | On the roadmap; timing not yet committed — will work on it in the future |
| **Future / Considering** | Not yet planned; gathering input / exploring |

**Always include**: *"This roadmap represents plans, not commitments. Phases and priorities may shift as we learn more from the market."*

---

## Audience-Specific Roadmap Views

The same underlying roadmap data should be presented differently for each audience. Creating multiple views from one source maintains consistency while serving each audience's actual needs.

### Executive View
**Focus**: Strategic themes and business outcomes
**Include**:
- Major release themes (not feature lists)
- Business goals each theme addresses
- Investment areas for the coming period
- Key milestones (GA, major betas)
**Omit**: Feature-level detail, sprint schedules, implementation approach
**Format**: Theme-based slide or 1-page summary; phase-driven preferred

---

### Sales View
**Focus**: What can be sold, and when
**Include**:
- Upcoming features with persona and problem context
- Target segments who benefit
- Rough timing (phase-driven or current-quarter dates)
- Competitive implications where relevant
- What to say and not say to customers asking about the roadmap
**Omit**: Features not yet ready to discuss externally, speculative future items
**Format**: Release-by-release overview; include talking points

---

### Engineering View
**Focus**: What's being built and in what sequence
**Include**:
- Initiatives and their dependencies
- Priority order for the upcoming release
- Market context for top priorities
- Known constraints or external dependencies
**Omit**: Executive business strategy, sales pipeline impact
**Format**: Initiative-level list with priority order; current quarter detail + next quarter themes

---

### Customer View
**Focus**: Problems being solved, not features being built
**Include**:
- Market problems (pains, jobs-to-be-done) the roadmap addresses
- General themes for upcoming work
- Areas where customer input is welcome
**Omit**: Specific dates, competitive information, internal features not customer-facing
**Format**: Theme-driven, conversational — best used in a roadmap dialogue, not a static document
**Always say**: *"This represents our current plans. We want your feedback to help us prioritize."*

---

### Customer Success / Support View
**Focus**: What's changing and how it affects current customers
**Include**:
- Features or changes that affect existing workflows
- Release timing (near-term only)
- Known limitations or transition considerations
- Talking points for customer questions
**Format**: Release notes format, internal-facing; ahead of public release notes

---

## Roadmap Communication Best Practices

**1. Separate the roadmap from the release plan**
The roadmap shows direction and themes. The release plan shows what is committed for a specific release. Don't conflate them.

**2. Never let the roadmap become a contract**
Every roadmap presentation — internal or external — should include a clear statement that it represents plans, not commitments. Normalize this disclaimer so it doesn't feel like a hedge.

**3. Communicate changes proactively**
When priorities shift, communicate to affected audiences *before* they discover the change on their own. Surprise erodes trust more than the change itself.

**4. Keep external roadmaps problem-focused**
When sharing the roadmap with customers or partners, describe the problems being solved, not the features being built. This protects against over-promising specifics and keeps the conversation strategic.

**5. Use phase-driven views for anything beyond one quarter**
As Pragmatic Institute teaching establishes: you know what you're working on now (you've seen it), you know what you're working on next (you've started it), and you know what's coming later (but not when). Communicate accordingly.

**6. Avoid the FUTURE trap**
When stakeholders ask "when will FUTURE items be delivered?" the honest answer is: "We don't know yet. When we begin working on them, we'll have better timing." Commit to communicating when that happens — not to a date that doesn't exist yet.
