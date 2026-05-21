# Nurturing Strategy Guide

## Table of Contents

1. [Pragmatic Context for Nurturing](#pragmatic-context)
2. [Lead Lifecycle Stage Design](#lead-lifecycle)
3. [Lead Scoring Frameworks](#lead-scoring)
4. [Content Mapping Methodology](#content-mapping)
5. [Workflow Design Patterns](#workflow-design)
6. [Multi-Channel Nurturing](#multi-channel)
7. [Sales-Marketing Alignment](#sales-marketing-alignment)
8. [Customer and Expansion Nurturing](#customer-nurturing)
9. [Metrics and Optimization](#metrics-optimization)
10. [Common Pitfalls](#common-pitfalls)

---

## 1. Pragmatic Context for Nurturing <a name="pragmatic-context"></a>

### Where Nurturing Sits in the Framework

Nurturing belongs to the **Programs** category alongside Marketing Plan, Revenue Growth, Revenue Retention, Launch, Awareness, Advocacy, and Measurement. It sits on the execution side of the strategy/execution divide. In Pragmatic's model, Nurturing represents the operational machinery that converts the strategic work done in Planning (Positioning, Buyer Personas, Buyer Experience) into active prospect engagement.

### Upstream Dependencies

Effective nurturing requires outputs from these Pragmatic activities:

- **Buyer Personas**: Without defined archetypical buyers, nurture programs default to generic messaging. Each persona has different problems, evaluation criteria, and content preferences.
- **Buyer Experience**: The documented buying process tells you what information buyers need at each stage and what barriers they encounter. Nurture workflows should mirror and smooth this journey.
- **Positioning**: Internal positioning documents supply the messaging pillars for each persona. Nurture content translates positioning into specific communications.
- **Market Problems**: Validated market problems are the foundation of nurture content. Leading with problems the market cares about (not product features) is the Pragmatic way.
- **Content**: The Content activity produces assets for each step of the buying process. Nurturing orchestrates delivery of these assets.
- **Awareness**: Awareness programs fill the top of funnel. Nurturing takes over once a prospect is identified and moves them toward purchase.

### Downstream Connections

- **Measurement**: Nurture KPIs feed into the broader measurement framework to prove program effectiveness.
- **Sales Alignment**: MQL-to-SQL handoff protocols must be co-designed with sales. Nurturing fails if sales doesn't trust or act on the leads passed to them.
- **Revenue Growth**: Nurture programs directly impact new customer acquisition pipeline.
- **Revenue Retention**: Post-sale nurturing drives retention, expansion, and cross-sell.
- **Advocacy**: Successful nurturing that creates delighted customers feeds the advocacy pipeline.

### The Pragmatic Nurturing Philosophy

Pragmatic's approach to nurturing differs from generic demand-gen in several key ways:

1. **Problem-led, not product-led**: Nurture content should educate buyers about their problems and potential solution approaches before introducing your specific product.
2. **Persona-specific**: One-size-fits-all nurture tracks violate the Pragmatic principle that different buyers have different problems, speak different languages, and follow different buying processes.
3. **Buyer-experience aligned**: Nurture workflows should map to the actual steps buyers take, not an idealized marketing funnel. If your buyers consult analysts at stage 3, your nurture should provide analyst-relevant content at that point.
4. **Measured by business outcomes**: Pragmatic measures programs by their contribution to revenue, not vanity metrics like email opens.

---

## 2. Lead Lifecycle Stage Design <a name="lead-lifecycle"></a>

### Standard B2B Lifecycle Model

A well-designed lifecycle provides a shared language between marketing and sales. Each stage should have:

- **Clear definition**: What qualifies someone for this stage (observable criteria, not assumptions)
- **Entry trigger**: The specific action or data combination that moves someone into this stage
- **Owner**: Which team is responsible for engaging the lead
- **Exit paths**: How leads move forward (progression), backward (recycling), or out (disqualification)
- **SLA**: Time-bound commitment for the owning team to act

### Stage Definitions

**Subscriber / Known Contact**
- Has provided contact information (form fill, event registration, content download)
- No significant engagement signal yet
- Owner: Marketing (automated)
- Goal: Move to Engaged through welcome sequence and initial content delivery
- Typical duration: 0–30 days

**Engaged Lead**
- Has taken multiple actions indicating interest beyond initial opt-in
- Examples: Multiple content downloads, webinar attendance, repeat website visits, email click-throughs
- Owner: Marketing (automated + manual review)
- Goal: Qualify through scoring to determine if they meet MQL criteria

**Marketing Qualified Lead (MQL)**
- Meets both fit criteria (right persona, right company profile) AND engagement threshold
- Demonstrated enough interest to warrant targeted nurturing or sales review
- Owner: Marketing hands to sales for review
- SLA: Sales reviews within 24–48 hours
- Goal: Sales accepts or recycles with feedback

**Sales Accepted Lead (SAL)**
- Sales has reviewed the MQL and confirmed it's worth pursuing
- Initial outreach has been made or is in progress
- Owner: Sales (with marketing air cover)
- Goal: Qualify as SQL through discovery conversation

**Sales Qualified Lead (SQL) / Opportunity**
- Active deal with confirmed need, authority, budget, and timeline (BANT or equivalent)
- Formal opportunity created in CRM
- Owner: Sales
- Goal: Progress through sales stages to close

**Customer**
- Closed/won deal
- Transitions from acquisition nurturing to onboarding and retention nurturing
- Owner: Customer Success + Marketing
- Goal: Drive adoption, time-to-value, and satisfaction

**Advocate**
- Engaged customer willing to provide references, testimonials, or case studies
- Connects to the Pragmatic Advocacy activity
- Owner: Marketing + Customer Success
- Goal: Amplify customer voice in market

### Recycling and Disqualification

Not every lead progresses linearly. Design explicit paths for:

- **Recycled leads**: Sales-rejected leads that return to marketing nurture with feedback on why (timing, budget, authority). Use this feedback to place them in the right nurture track.
- **Disqualified leads**: Leads that are genuinely not a fit (wrong industry, too small, wrong geography). Remove from active nurturing to maintain list quality and protect sender reputation.
- **Re-engagement**: Leads that go dormant (no engagement in 60–90 days) enter a re-engagement workflow before being marked inactive.

---

## 3. Lead Scoring Frameworks <a name="lead-scoring"></a>

### Two-Dimensional Scoring

Best practice separates scoring into two axes:

**Axis 1: Fit Score (Who they are)**
Grades how closely the lead matches your ideal customer profile and target buyer personas. Based on firmographic and demographic data.

| Criteria | High Fit (+) | Medium Fit | Low Fit (−) |
|---|---|---|---|
| Company size | In target range | Adjacent range | Outside range |
| Industry | Target segment | Adjacent segment | Non-target |
| Job title/role | Matches buyer persona | Related role | Unrelated |
| Geography | Target market | Serviceable | Not served |
| Company revenue | In range | Near range | Out of range |

**Axis 2: Engagement Score (What they do)**
Measures behavioral signals of interest and intent.

| Action | Points (example) | Signal Strength |
|---|---|---|
| Requested demo or contact | +50 | Very high intent |
| Visited pricing page | +30 | High intent |
| Attended live webinar | +25 | High engagement |
| Downloaded BOFU content (case study, ROI calc) | +20 | Mid-high intent |
| Downloaded MOFU content (whitepaper, guide) | +15 | Mid engagement |
| Multiple blog visits in 7 days | +10 | Growing interest |
| Opened email | +2 | Low signal |
| Clicked email link | +5 | Mild interest |
| Unsubscribed | −20 | Negative signal |
| No activity 30 days | −10 | Decay |
| No activity 60 days | −20 | Significant decay |
| No activity 90+ days | −30 | Dormant |

### Threshold Configuration

- **MQL threshold**: Typically requires minimum fit score (e.g., "B" grade or above) PLUS minimum engagement score (e.g., 50+ points). Neither dimension alone should qualify a lead.
- **Fast-track triggers**: Certain actions override scoring and fast-track to MQL (e.g., demo request, pricing inquiry, "contact sales" form submission).
- **Score decay**: Apply time-based decay so old engagement doesn't inflate scores. Common approach: reduce engagement score by 10–20% per month of inactivity.

### Scoring Model Maintenance

- Review scoring weights quarterly against actual closed-won data
- Compare scored MQLs vs. actual conversion to validate threshold accuracy
- Adjust for changes in market, product, or buyer behavior
- Get regular feedback from sales on lead quality to calibrate

---

## 4. Content Mapping Methodology <a name="content-mapping"></a>

### The Persona × Stage Matrix

Create a matrix for each buyer persona with content mapped to each funnel stage:

**Persona: [Name]**

| Stage | Buyer Questions | Content Type | Available? | Gap? |
|---|---|---|---|---|
| Awareness | "What's causing this problem?" | Blog series, industry report | ✓ / ✗ | |
| Consideration | "What approaches solve this?" | Whitepaper, webinar, comparison | ✓ / ✗ | |
| Evaluation | "Why this vendor?" | Case study, demo, ROI calculator | ✓ / ✗ | |
| Decision | "How do I justify this purchase?" | Business case template, reference call | ✓ / ✗ | |
| Post-Sale | "How do I get maximum value?" | Onboarding guide, best practices | ✓ / ✗ | |

### Content Requirements by Stage

**Top of Funnel (TOFU) — Problem Education**
- Purpose: Help prospects understand and articulate their problem
- Tone: Educational, empathetic, vendor-neutral
- Pragmatic alignment: Rooted in validated market problems
- Formats: Blog posts, short videos, infographics, podcast episodes, social posts
- Call to action: Subscribe, download ungated content, follow on social

**Middle of Funnel (MOFU) — Solution Evaluation**
- Purpose: Help prospects evaluate solution categories and approaches
- Tone: Thought leadership, authoritative, beginning to position
- Pragmatic alignment: Leverages positioning pillars and distinctive competencies
- Formats: Whitepapers, webinars, analyst reports, comparison guides, solution briefs
- Call to action: Download gated content, attend webinar, sign up for assessment

**Bottom of Funnel (BOFU) — Vendor Selection**
- Purpose: Help prospects choose your solution and build internal business case
- Tone: Proof-oriented, specific, confident
- Pragmatic alignment: Uses customer advocacy assets and win/loss insights
- Formats: Case studies, ROI calculators, product demos, testimonials, reference calls
- Call to action: Request demo, start trial, talk to sales, get pricing

**Post-Sale — Adoption and Expansion**
- Purpose: Drive product adoption, satisfaction, and expansion revenue
- Tone: Supportive, success-oriented, community-building
- Pragmatic alignment: Connects to Revenue Retention activity
- Formats: Onboarding sequences, feature guides, user community, advanced training, cross-sell education
- Call to action: Complete onboarding, attend training, explore additional products

### Content Gap Analysis

After mapping, identify gaps and prioritize by:
1. Revenue impact (which gaps affect the most pipeline?)
2. Persona priority (which persona drives the most revenue?)
3. Stage criticality (where do prospects stall most often?)
4. Ease of creation (can existing content be repurposed?)

Feed gaps back to the Content activity for production planning.

---

## 5. Workflow Design Patterns <a name="workflow-design"></a>

### Workflow Architecture

Each nurture workflow follows this structure:

```
[Entry Trigger] → [Touch 1] → [Wait] → [Branch?]
                                           ├── Yes → [Accelerated path]
                                           └── No  → [Touch 2] → [Wait] → [Branch?] ...
                                                                              └── [Exit / Handoff]
```

### Design Principles

1. **Start slow, accelerate with engagement**: Initial touches should be spaced further apart (5–7 days). As engagement increases, reduce intervals (2–3 days).
2. **Behavior-based branching**: If a prospect clicks a case study link, branch them into BOFU content rather than continuing MOFU education.
3. **Progressive profiling**: Each interaction should gather a small additional data point without overwhelming the prospect.
4. **Clear exit conditions**: Every workflow needs defined exits — conversion to next stage, opt-out, disqualification, or dormancy.
5. **Personal touches at key moments**: Insert human outreach (sales email, phone call) at high-engagement moments rather than relying entirely on automation.

### Standard Workflow Templates

**1. New Subscriber Welcome (3–5 touches over 14 days)**
- Touch 1 (Day 0): Welcome email with best educational content
- Touch 2 (Day 3): Share second educational piece; progressive profile question
- Touch 3 (Day 7): Industry-relevant content or data point
- Touch 4 (Day 10): Invite to webinar or community
- Touch 5 (Day 14): Assessment offer or consultation (soft CTA)
- Exit: If scoring threshold reached → MQL track. If no engagement → dormant pool.

**2. Problem Education Track (TOFU → MOFU, 6–8 touches over 30–45 days)**
- Anchored in a specific market problem from the Pragmatic Market Problems activity
- Educates on the problem's impact, prevalence, and urgency
- Introduces solution categories (not your product specifically)
- Bridges to evaluation content with thought leadership
- Exit: High engagement → Solution Evaluation track. No engagement → re-engagement.

**3. Solution Evaluation Track (MOFU → BOFU, 4–6 touches over 21–30 days)**
- Shares comparison frameworks, analyst perspectives
- Introduces your approach and differentiation
- Provides social proof (customer stories, data points)
- Offers self-service evaluation tools (ROI calculator, assessment)
- Exit: Demo request or high-intent action → Sales handoff. Stall → re-engagement.

**4. Sales Acceleration Track (BOFU, 3–4 touches over 10–14 days)**
- Triggered by high-intent actions or sales request
- Delivers decision-support content: case studies, reference details, business case materials
- Coordinates with sales outreach
- Exit: Opportunity created. Or if no response → Stalled deal track.

**5. Stalled Deal Re-engagement (variable, 4–6 touches over 30–60 days)**
- For leads that were in sales process but went cold
- New angle: different content, different problem, peer story
- Lower-pressure CTAs (educational, not sales-focused)
- Exit: Re-engagement → return to appropriate track. No response → long-term dormant.

**6. Customer Onboarding (5–7 touches over 30–60 days post-close)**
- Time-to-value focused: key setup steps, quick wins
- Feature education mapped to the problems they bought to solve
- Community invitation, support resources
- Check-in touchpoints for satisfaction
- Exit: Onboarded → expansion track. At-risk signals → CSM alert.

**7. Expansion / Cross-sell (ongoing, event-triggered)**
- Triggered by usage milestones, contract anniversaries, or product updates
- Educates on adjacent products or premium tiers
- Uses their usage data to personalize (where available)
- Light touch: value-first, not pressure
- Exit: Engagement → sales conversation. No interest → reduce frequency.

### Timing and Cadence Guidelines

- **Welcome / onboarding**: Higher frequency (every 2–3 days) — capitalize on initial interest
- **Education tracks**: Moderate frequency (every 5–7 days) — respect the learning pace
- **Evaluation / decision**: Responsive frequency (triggered by behavior, otherwise every 3–5 days)
- **Re-engagement**: Low frequency (every 10–14 days) — avoid fatigue on cold leads
- **Customer expansion**: Lowest frequency (monthly or event-triggered) — maintain relationship without annoying

---

## 6. Multi-Channel Nurturing <a name="multi-channel"></a>

While email is the backbone, effective nurture programs use multiple channels:

- **Email**: Primary channel for sequenced content delivery, personalized messaging, and progressive profiling
- **Website personalization**: Dynamic content based on lifecycle stage and persona; personalized CTAs
- **Retargeting ads**: Display and social ads that reinforce nurture messaging for engaged leads
- **Social media**: LinkedIn engagement for B2B; direct messaging for high-value prospects
- **Direct mail**: Physical touchpoints for strategic accounts (ABM approach)
- **Events / webinars**: Live interaction that accelerates relationship building
- **Sales outreach**: Personal email and phone at critical moments in the journey

### Channel Orchestration Principles

- Use email as the spine; layer other channels as amplification
- Don't repeat the same message across channels simultaneously — coordinate and complement
- Match channel to prospect preference (some personas prefer phone, others prefer self-service)
- Ensure consistent messaging across channels while adapting format and tone

---

## 7. Sales-Marketing Alignment <a name="sales-marketing-alignment"></a>

### The Handoff Problem

The most common nurturing failure point is the marketing-to-sales handoff. Pragmatic's Sales Alignment activity addresses this, and nurturing must operationalize it.

### Alignment Requirements

1. **Shared definitions**: Marketing and sales must agree on what constitutes an MQL and SQL. Document these in a Service Level Agreement (SLA).
2. **SLA for response time**: Sales commits to reviewing MQLs within a defined window (typically 24–48 hours). Speed of follow-up dramatically impacts conversion.
3. **Feedback loop**: Sales provides structured feedback on every MQL — accepted, rejected (with reason), or needs more information. This data improves scoring accuracy.
4. **Recycling protocol**: Rejected MQLs return to marketing with context, not just a status change. "Not ready yet — interested but no budget until Q3" guides which nurture track to use.
5. **Shared visibility**: Both teams should see the same lead data, engagement history, and scoring in CRM.

### SLA Template

| Commitment | Marketing | Sales |
|---|---|---|
| Lead quality | Deliver leads meeting agreed MQL criteria | Review 100% of MQLs within 48 hours |
| Volume | Deliver [X] MQLs per month | Provide disposition feedback on 100% |
| Feedback | Adjust scoring based on sales feedback quarterly | Share rejection reasons within 5 business days |
| Reporting | Monthly report on MQL volume, source, and quality | Monthly report on MQL-to-SQL conversion and feedback |

---

## 8. Customer and Expansion Nurturing <a name="customer-nurturing"></a>

The Pragmatic definition explicitly includes "upsell or cross-sell existing customers." Post-sale nurturing connects to Revenue Retention.

### Onboarding Nurture

- Time-to-value is the key metric: how quickly does the customer achieve their first meaningful outcome?
- Map onboarding touches to the specific problems the customer bought to solve
- Include both automated sequences and human check-ins
- Monitor engagement: low onboarding engagement = churn risk

### Expansion Nurture

- Triggered by usage milestones, contract renewal timeline, or new product releases
- Content should demonstrate how expanded usage solves additional problems (back to market problems)
- Use customer-specific data where possible: "You've achieved X with Product A — here's how Product B can help you also solve Y"
- Coordinate with account management / customer success

### Churn Prevention

- Monitor engagement signals: declining usage, support ticket volume, missed renewals
- Trigger proactive outreach with value-reinforcement content
- Escalate high-risk accounts to customer success for human intervention

---

## 9. Metrics and Optimization <a name="metrics-optimization"></a>

### Metrics Hierarchy

**Level 1: Business Impact (report to leadership)**
- Revenue influenced by nurture programs
- Nurtured lead win rate vs. non-nurtured
- Average deal size: nurtured vs. non-nurtured
- Customer acquisition cost (CAC) impact
- Pipeline velocity improvement

**Level 2: Funnel Performance (report monthly)**
- Stage-to-stage conversion rates
- Average time in each stage
- MQL-to-SQL conversion rate
- MQL acceptance rate (% sales accepts)
- Lead velocity rate (growth in qualified leads month-over-month)

**Level 3: Engagement (report weekly)**
- Email delivery, open, click, and reply rates by workflow
- Content engagement by asset and stage
- Lead score progression over time
- Unsubscribe and bounce rates
- Workflow completion rates

### Optimization Practices

**Weekly review:**
- Email performance (delivery, opens, clicks)
- Anomaly detection (sudden drops or spikes)
- A/B test results

**Monthly review:**
- Stage conversion rates
- Workflow performance comparison
- Content effectiveness (which assets move leads forward?)
- Lead scoring accuracy (are high-scoring leads actually converting?)

**Quarterly review:**
- Full scoring model audit
- Content gap reassessment
- Workflow refresh (retire underperformers, launch new tracks)
- Sales feedback integration
- SLA compliance review

**Annual review:**
- Full nurture strategy alignment with marketing plan and business goals
- Technology stack assessment
- Competitive nurture benchmarking
- Persona and buyer experience refresh impact on nurture programs

---

## 10. Common Pitfalls <a name="common-pitfalls"></a>

1. **Product-centric messaging**: Leading with features instead of problems. The Pragmatic approach always starts with the market problem.

2. **One-size-fits-all**: Sending the same nurture sequence to all personas. Different buyers have different problems, speak different languages, and follow different evaluation paths.

3. **Scoring without validation**: Setting up lead scoring once and never revisiting. Scoring models drift as markets and buyer behavior change.

4. **Ignoring the middle of funnel**: Over-investing in TOFU content and BOFU sales pushes while neglecting the consideration stage where most leads stall.

5. **No sales feedback loop**: Marketing passes leads and never hears back on quality or outcome. Without feedback, scoring and nurturing can't improve.

6. **Treating nurturing as "just email"**: Effective nurturing is multi-channel and includes human touches at critical moments.

7. **Nurturing only new prospects**: Ignoring customer nurturing for retention and expansion leaves revenue on the table.

8. **Over-nurturing**: Too many emails too frequently causes fatigue and unsubscribes. Respect the prospect's time and attention.

9. **No clear exits**: Leads trapped in perpetual nurture loops with no clear graduation or disqualification path.

10. **Disconnected from buyer experience**: Building nurture workflows based on the internal sales process rather than how the buyer actually buys.
