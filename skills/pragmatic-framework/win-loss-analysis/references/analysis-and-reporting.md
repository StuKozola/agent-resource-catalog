# Win/Loss Analysis & Reporting Framework

This reference covers how to analyze interview data, calculate metrics, identify patterns,
and structure findings into reports that drive action.

## Table of Contents

1. Coding Interview Data
2. Quantitative Metrics & Formulas
3. Pattern Recognition
4. Perception Gap Analysis
5. Report Structure — Executive Summary
6. Report Structure — Detailed Findings
7. Report Structure — Flash Report (Monthly)
8. Report Structure — Single-Deal Debrief
9. Presenting to Stakeholders
10. Action Tracking

---

## 1. Coding Interview Data

After each interview, code the conversation against a consistent taxonomy so you can
aggregate findings across interviews. Every meaningful insight should be tagged with:

**Primary category:** The top-level domain the insight relates to.
- Product / Solution Fit
- Pricing / Commercial Terms
- Sales Experience
- Marketing / Brand / Messaging
- Competitive Positioning
- Implementation / Onboarding
- Support / Customer Success
- Company Reputation / Viability

**Sentiment:** Whether the buyer's perception was positive, negative, or neutral.

**Impact level:** Whether this factor was a primary decision driver, a contributing
factor, or background context (high / medium / low).

**Competitor mentioned:** If the insight involves a specific competitor, tag it.

**Buyer role:** Tag the seniority and function of the interviewee (e.g., VP Engineering,
Procurement Manager, End User) — different stakeholders have different concerns.

**Verbatim theme:** Capture a short paraphrase (not a full quote) that captures the
essence of the insight. Example: "Demo felt generic — didn't address their specific
healthcare compliance requirements."

### Coding Example

| Interview | Category | Sentiment | Impact | Competitor | Theme |
|---|---|---|---|---|---|
| Win #4 | Sales Experience | Positive | High | — | Sales team deeply understood buyer's industry |
| Loss #7 | Pricing | Negative | High | Acme Corp | Usage-based model preferred; per-seat penalized seasonal teams |
| Loss #7 | Product Fit | Negative | Medium | Acme Corp | Missing native integration with buyer's ERP system |
| Win #2 | Competitive Positioning | Positive | High | Beta Inc | Buyer perceived our roadmap as more aligned with their growth |
| No-Dec #3 | — | Neutral | High | — | Budget reprioritized; project deferred to next fiscal year |

---

## 2. Quantitative Metrics & Formulas

Calculate these metrics on a regular cadence (monthly or quarterly) that mirrors your
sales cycle.

### Win Rate
```
Win Rate (%) = Wins / (Wins + Losses) × 100
```
Segment this by: product line, deal size, industry vertical, competitor, sales rep,
region, and time period. The overall number matters less than the segmented trends.

### Win/Loss Ratio
```
Win/Loss Ratio = Wins : Losses
```
Express as a ratio (e.g., 2:1 means you win twice as often as you lose).
A ratio above 1:1 means you win more than you lose. Context matters — a 3:1 ratio
in your core segment and a 0.5:1 ratio against a specific competitor tells a clear
story about where to focus.

### Loss Rate by Reason
```
Loss Rate by Reason (%) = Losses for Reason X / Total Losses × 100
```
Example: If 50 total losses and 12 were primarily attributed to pricing →
Loss Rate for Pricing = 24%.

Track this over time. If "product gaps" was your top loss reason at 30% last quarter
and drops to 18% after a release, you have evidence that product investment is paying
off.

### Competitive Win Rate
```
Competitive Win Rate vs. Competitor X (%) = Wins vs. X / (Wins + Losses vs. X) × 100
```
The most actionable metric for competitive strategy. Track per-competitor and watch
for trends.

### Interview Participation Rate
```
Participation Rate (%) = Completed Interviews / Interview Requests Sent × 100
```
Benchmark: 30–50% is typical. Below 20% suggests your outreach approach needs work
(timing, incentive, messaging). Track this to ensure your sample doesn't develop
selection bias.

### Average Deal Cycle (Won vs. Lost)
Compare the average sales cycle length for won deals vs. lost deals. Longer-than-average
cycles that end in losses may indicate deals that should have been disqualified earlier.

---

## 3. Pattern Recognition

Individual interviews are anecdotal. Patterns across interviews are intelligence. Look
for:

**Frequency patterns:** What themes appear in 30%+ of interviews? These are systemic,
not one-off. If 4 out of 12 loss interviews mention a specific missing feature, that's
a pattern worth escalating to product.

**Segment patterns:** Do certain loss reasons cluster by industry, deal size, or buyer
persona? Example: you may win consistently in financial services but lose in healthcare
due to compliance requirements.

**Temporal patterns:** Are loss reasons changing over time? A new competitor entering
the market might shift your loss reasons from "product fit" to "competitive pricing"
over two quarters.

**Perception gaps:** Where does the sales team's explanation for a loss diverge from
what the buyer actually said? These gaps are among the most valuable findings.
Common gaps:
- Sales says "price" → buyer says "demo didn't address my use case"
- Sales says "political decision" → buyer says "your team was unresponsive for 2 weeks"
- Sales says "they liked the competitor's brand" → buyer says "competitor showed a
  clear implementation plan and yours felt vague"

**Win patterns:** Don't only analyze losses. Understanding why you win is equally
important — it tells you what to protect and amplify. If buyers consistently cite your
professional services team as a differentiator, that's a strategic asset to invest in.

---

## 4. Perception Gap Analysis

This is one of the highest-value analyses in a win/loss program. For each deal where
you have both an internal sales debrief and a buyer interview, compare:

| Dimension | Sales Team Perception | Buyer Perception | Gap? |
|---|---|---|---|
| Why we won/lost | "Price" | "Demo didn't address our specific use case" | YES — root cause misidentified |
| Competitive threat | "Competitor X is strongest" | "Actually, Competitor Y was our close second" | YES — wrong competitor focus |
| Product strengths | "Our analytics are best-in-class" | "Analytics were table stakes; your onboarding was the differentiator" | YES — wrong differentiator emphasized |
| Sales experience | "Relationship was strong" | "Sales team was knowledgeable but slow to respond" | YES — responsiveness issue masked |

Perception gaps directly inform sales coaching, enablement content, and messaging
adjustments. When you present these to leadership, the contrast between "what we think"
and "what buyers say" is often the most compelling part of the report.

---

## 5. Report Structure — Executive Summary

Use this structure for quarterly presentations to leadership. Keep it to 2–3 pages or
5–8 slides maximum.

### Template:

**Title:** Win/Loss Analysis — [Quarter/Period] Executive Summary

**Program overview:**
- Interviews conducted: [X wins, Y losses, Z no-decisions]
- Interview period: [date range]
- Segments covered: [list]
- Competitors encountered: [list]

**Key metrics:**
- Overall win rate: [X%] (change from prior period: [+/- Y%])
- Win rate by segment: [table]
- Competitive win rates: [table]
- Top loss reasons: [ranked list with percentages]

**Top 3 findings:**
For each finding, state:
1. The insight (one sentence)
2. The supporting evidence (how many interviews, which segments)
3. The recommended action
4. The proposed owner

**Perception gaps:** Highlight the 1–2 most significant divergences between internal
assumptions and buyer feedback.

**Trend watch:** Note any emerging themes that aren't yet statistically significant
but warrant monitoring.

**Actions from prior period:** Status update on previously recommended actions.

---

## 6. Report Structure — Detailed Findings

The detailed report is for practitioners (product managers, product marketers, sales
enablement) who need to act on the findings. It supplements the executive summary with
depth.

### Template:

**Section 1: Methodology & Sample**
- How interviews were conducted, by whom, over what period
- Sample composition (wins/losses/no-decisions, segments, deal sizes)
- Any sampling limitations or biases to note

**Section 2: Quantitative Analysis**
- Win rate trends (overall and segmented)
- Loss reason breakdown with period-over-period comparison
- Competitive win rate per competitor
- Deal cycle analysis

**Section 3: Qualitative Findings by Category**
For each primary category (Product, Pricing, Sales, Marketing, Competitive, etc.):
- Summary of findings
- Number of interviews where this theme appeared
- Representative buyer perspective (paraphrased, anonymized)
- Recommended actions

**Section 4: Competitive Intelligence**
- Per-competitor profile based on buyer perceptions
- Competitive strengths and weaknesses as perceived by the market
- Messaging gaps where competitor positioning is resonating and yours isn't

**Section 5: Perception Gap Analysis**
- Table of significant gaps (see Section 4 above)
- Implications for sales coaching and enablement

**Section 6: Recommended Actions**
- Prioritized action list with owner, timeline, and success metric
- Separate actions for: Product, Marketing, Sales, Pricing, Customer Success

**Appendix:** Individual interview summaries (anonymized)

---

## 7. Report Structure — Flash Report (Monthly)

A lightweight, rapid-fire update for stakeholders who want the latest signal without
waiting for the quarterly deep dive.

### Template (1 page / 2–3 slides):

**[Month] Win/Loss Flash Report**

- Interviews completed: [X]
- Win rate this month: [X%]
- Emerging themes: [2–3 bullet points]
- Notable quote (paraphrased, anonymized): [one impactful buyer perspective]
- Action items flagged: [any urgent findings that can't wait for quarterly review]

---

## 8. Report Structure — Single-Deal Debrief

Use this when analyzing one specific important deal, often immediately after a
significant win or loss.

### Template:

**Deal overview:** Company name, deal size, segment, sales cycle length, competitor(s),
outcome, date of decision.

**Internal perspective:** Summary of the sales team's debrief — what they believe drove
the outcome.

**Buyer perspective:** Summary of the buyer interview — what the buyer says drove the
outcome.

**Perception gaps:** Where do the two perspectives diverge?

**Key takeaways:** 2–3 specific, actionable insights from this deal.

**Recommended actions:** What should change as a result?

---

## 9. Presenting to Stakeholders

**To executives:** Lead with metrics and business impact. Show win rate trends, top loss
reasons, and 3 concrete actions that will improve competitive position. Keep it short.
Execs want the "so what" — not the methodology.

**To product teams:** Lead with product-specific findings. What features are buyers
asking for? Where are product gaps driving losses? Include buyer language about pain
points. Product teams respond to hearing the voice of the buyer.

**To sales teams:** Handle with care. Position findings as enabling sales, not evaluating
individual reps. Lead with win patterns (what's working) before loss patterns (what to
improve). Focus on systemic issues (demo quality, response time, pricing communication)
not individual blame. Share competitive intelligence — sales teams find this immediately
useful.

**To marketing:** Focus on messaging effectiveness, content gaps, brand perception, and
competitive positioning. Share how buyers described your company vs. competitors — the
language they use reveals whether your messaging is landing.

---

## 10. Action Tracking

Maintain a simple tracking system to ensure insights lead to changes:

| # | Finding | Category | Owner | Action | Status | Target Date | Impact Metric |
|---|---|---|---|---|---|---|---|
| 1 | 35% of losses cite missing ERP integration | Product | PM Lead | Evaluate ERP integration for Q3 roadmap | In Progress | Q3 | Competitive win rate vs. Acme |
| 2 | Demos perceived as generic by healthcare buyers | Sales | SE Manager | Create healthcare-specific demo script | Not Started | Month 2 | Healthcare segment win rate |
| 3 | Buyers can't find pricing on website | Marketing | Web Lead | Add transparent pricing page | Complete | — | Inbound lead quality score |

Review this tracker at each quarterly readout. Celebrate completed actions and their
measured impact — this sustains the program's credibility and funding.
