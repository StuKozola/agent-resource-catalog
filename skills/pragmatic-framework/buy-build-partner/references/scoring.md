# BBP Scoring Matrix & Evaluation Templates

This reference contains the weighted scoring matrix for Buy, Build, or Partner decisions, along with detailed rubrics for each criterion and a partnership-specific evaluation template.

## Table of Contents
1. [7-Criteria Weighted Scoring Matrix](#main-matrix)
2. [Scoring Rubrics (1-5 Scale)](#rubrics)
3. [Quick-Decision Heuristics](#heuristics)
4. [Partnership Candidate Evaluation](#partnership-eval)
5. [Acquisition Target Evaluation](#acquisition-eval)
6. [Cost Comparison Template](#cost-template)

---

## 7-Criteria Weighted Scoring Matrix <a name="main-matrix"></a>

### Default Weights

| # | Criterion | Weight | What It Measures |
|---|-----------|--------|------------------|
| 1 | Time-to-Value | 15% | How quickly the capability reaches customers |
| 2 | Total Cost of Ownership | 20% | 3-year fully loaded cost (development, integration, maintenance, licensing) |
| 3 | Strategic Differentiation | 20% | Whether this strengthens competitive moat and distinctive competence |
| 4 | Integration Risk | 15% | Technical complexity of integrating with existing product/infrastructure |
| 5 | Control & IP | 10% | Degree of control over roadmap, code, data, and intellectual property |
| 6 | Scalability | 10% | Ability to scale with business growth without proportional cost increase |
| 7 | Risk & Dependencies | 10% | External risks, vendor/partner dependencies, single points of failure |

### Weight Customization Guide

Adjust weights based on your strategic context:

- **Speed is critical** (competitive threat, closing market window): Increase Time-to-Value to 25%, reduce Control & IP to 5%
- **Regulated industry** (healthcare, finance, government): Add a Compliance/Security criterion at 15%, reduce others proportionally
- **Early-stage startup** (capital constrained): Increase TCO to 25%, reduce Strategic Differentiation to 15%
- **Platform play** (building an ecosystem): Increase Scalability to 20%, add an Ecosystem/Network Effects criterion
- **IP-sensitive** (deep tech, patents matter): Increase Control & IP to 20%, reduce Time-to-Value to 10%

Weights must sum to 100%. Cap at 7 criteria to prevent diffusion. If adding a criterion, remove or merge another.

---

## Scoring Rubrics (1-5 Scale) <a name="rubrics"></a>

### Criterion 1: Time-to-Value

| Score | Description |
|-------|-------------|
| 5 | Deliverable to customers in ≤ 4 weeks |
| 4 | Deliverable in 1-3 months |
| 3 | Deliverable in 3-6 months |
| 2 | Deliverable in 6-12 months |
| 1 | Deliverable in 12+ months |

### Criterion 2: Total Cost of Ownership (3-Year)

| Score | Description |
|-------|-------------|
| 5 | Lowest cost option by significant margin (>30% cheaper than alternatives) |
| 4 | Below average cost with predictable expense profile |
| 3 | Average cost, comparable to alternatives |
| 2 | Above average cost or unpredictable expense profile |
| 1 | Highest cost option by significant margin, or major cost uncertainty |

**TCO should include:** development/acquisition cost, integration cost, ongoing maintenance (15-20% of build cost/year for internal), licensing fees, support staff, infrastructure, training, and eventual migration/sunset cost.

### Criterion 3: Strategic Differentiation

| Score | Description |
|-------|-------------|
| 5 | Directly strengthens core competitive advantage; creates defensible IP; adds to distinctive competence |
| 4 | Strengthens product positioning; creates moderate differentiation |
| 3 | Table-stakes capability; necessary but not differentiating |
| 2 | Minimal strategic value; commodity capability |
| 1 | Could dilute focus from core differentiation; distracts from distinctive competence |

### Criterion 4: Integration Risk

| Score | Description |
|-------|-------------|
| 5 | Minimal integration needed; ≤ 2 systems affected; no data migration |
| 4 | Moderate integration; 2-3 systems; standard APIs available |
| 3 | Significant integration; 3-5 systems; some custom work needed |
| 2 | Complex integration; 5+ systems; data migration required; custom connectors |
| 1 | Extremely complex; fundamental architecture changes; high failure risk |

### Criterion 5: Control & IP

| Score | Description |
|-------|-------------|
| 5 | Full ownership of code, data, IP, and roadmap |
| 4 | Significant control; own most IP; strong contractual protections |
| 3 | Shared control; joint IP or licensed with favorable terms |
| 2 | Limited control; dependent on vendor/partner roadmap; restrictive licensing |
| 1 | Minimal control; fully dependent on external party; no IP ownership |

### Criterion 6: Scalability

| Score | Description |
|-------|-------------|
| 5 | Scales linearly or better; costs grow sub-linearly with usage |
| 4 | Scales well with minor incremental investment |
| 3 | Scales adequately but requires proportional investment |
| 2 | Scaling requires significant additional investment or rework |
| 1 | Does not scale; fundamental redesign needed beyond current capacity |

### Criterion 7: Risk & Dependencies

| Score | Description |
|-------|-------------|
| 5 | No external dependencies; risk fully within internal control |
| 4 | Minor external dependencies; multiple fallback options available |
| 3 | Moderate dependencies; some single points of failure but mitigable |
| 2 | Significant dependencies; limited alternatives; partner/vendor concentration |
| 1 | Critical dependency on single external party; existential risk if relationship fails |

---

## Quick-Decision Heuristics <a name="heuristics"></a>

Use these rules of thumb for quick initial triage. They are not substitutes for the full scoring, but they help frame the starting hypothesis.

### Strong signals for BUILD:
- The capability IS your product's core differentiation
- Nothing like it exists in the market
- Tight integration with proprietary systems is essential
- You have the talent and capacity available now
- IP ownership is a strategic imperative

### Strong signals for BUY:
- Proven solutions exist with mature capabilities
- You need the capability immediately (< 3 months)
- The target company has talent/customers you also want
- The capability is adjacent to your core but not your distinctive competence
- Build estimates exceed 18 months

### Strong signals for PARTNER:
- A provider already does this well and would benefit from your distribution
- You need to test market demand before committing to build or buy
- The capability requires specialized domain expertise you don't have
- Both companies' customers would benefit from the integration
- You're entering a new market and need a credible local/domain partner

### Red flags — STOP and reconsider:
- No customer has asked for this (are you solving a real problem?)
- The gap is a "nice-to-have" that won't move revenue or win rates
- You're building because engineers want to, not because the market needs it
- You're buying/partnering to avoid the hard work of saying "not now" to a request

---

## Partnership Candidate Evaluation <a name="partnership-eval"></a>

When the BBP analysis points toward "Partner," use this template to evaluate specific partner candidates.

### Partner Evaluation Criteria

| # | Criterion | Weight | Score (1-5) | Weighted |
|---|-----------|--------|-------------|----------|
| 1 | Product/Capability Fit | 20% | | |
| 2 | Technical Integration Ease | 15% | | |
| 3 | Business Model Alignment | 15% | | |
| 4 | Market Reputation & Stability | 15% | | |
| 5 | Cultural & Strategic Alignment | 10% | | |
| 6 | Mutual Value Creation | 10% | | |
| 7 | Contractual Flexibility | 10% | | |
| 8 | Support & SLA Quality | 5% | | |
| | **Total** | **100%** | | |

### Partner Evaluation Rubric Details

**Product/Capability Fit:**
- 5: Solves the exact need out-of-the-box; demonstrated success with similar use cases
- 3: Solves most of the need; some customization required
- 1: Significant gaps between their capability and our requirements

**Technical Integration Ease:**
- 5: Well-documented APIs, SDKs, standard protocols; sandbox available
- 3: APIs exist but documentation is limited; some custom work needed
- 1: No API; requires deep custom integration or screen scraping

**Business Model Alignment:**
- 5: Commercial model naturally fits ours (e.g., usage-based aligns with our usage-based)
- 3: Workable but requires negotiation and creative deal structure
- 1: Fundamentally misaligned incentives (e.g., they want per-seat, we need unlimited)

**Market Reputation & Stability:**
- 5: Established company with strong financials, customer references, and growing
- 3: Growing company with decent traction but some financial uncertainty
- 1: Early-stage, high burn rate, limited references, or declining trajectory

**Cultural & Strategic Alignment:**
- 5: Shared vision, complementary strategy, strong executive relationship
- 3: Generally aligned but some strategic tension
- 1: Competing in adjacent areas; risk of becoming direct competitors

**Mutual Value Creation:**
- 5: Clear, quantifiable value for both parties; strong WIIFT (What's In It For Them)
- 3: Value exists but is unbalanced; one party benefits significantly more
- 1: Primarily one-sided; the other party has little incentive to invest

### Partnership Governance Checklist

For any partnership you proceed with, ensure these are defined:
- [ ] Dedicated partner product manager assigned
- [ ] Joint KPIs and success metrics agreed
- [ ] Integration roadmap with milestones
- [ ] SLA with escalation procedures
- [ ] Data sharing and privacy agreement
- [ ] IP ownership for co-developed features
- [ ] Exit clause with data portability terms
- [ ] Regular business review cadence (quarterly recommended)
- [ ] Customer support handoff procedures
- [ ] Co-marketing and go-to-market plan

---

## Acquisition Target Evaluation <a name="acquisition-eval"></a>

When the BBP analysis points toward "Buy," assess targets with these additional criteria:

| Criterion | Assessment Questions |
|-----------|---------------------|
| Product Maturity | Is the product production-ready? What's the tech debt level? |
| Customer Base | How many customers? Revenue? Churn rate? Overlap with ours? |
| Team & Talent | Key engineers and leaders? Retention risk? Cultural fit? |
| Technology Stack | Compatible with ours? Modern? Maintainable? |
| IP Portfolio | Patents? Trade secrets? Unique algorithms or data? |
| Financial Health | Revenue trajectory? Burn rate? Existing investors/debt? |
| Integration Complexity | How long to integrate into our product? What breaks? |
| Regulatory/Legal | Any IP disputes? Customer contracts that limit transfer? |

---

## Cost Comparison Template <a name="cost-template"></a>

Use this structure for a 3-year TCO comparison:

### Year 0 (Setup/Acquisition)

| Cost Category | Buy | Build | Partner |
|---------------|-----|-------|---------|
| Acquisition/License cost | $ | — | — |
| Development cost | — | $ | — |
| Integration/Setup cost | $ | $ | $ |
| Legal/Contracting | $ | — | $ |
| Training/Onboarding | $ | $ | $ |
| **Year 0 Total** | **$** | **$** | **$** |

### Annual Recurring (Years 1-3)

| Cost Category | Buy | Build | Partner |
|---------------|-----|-------|---------|
| Maintenance/Engineering | $ | $ | — |
| License/Subscription fees | — | — | $ |
| Revenue share | — | — | $ |
| Infrastructure | $ | $ | $ |
| Support staff | $ | $ | $ |
| **Annual Total** | **$** | **$** | **$** |

### 3-Year TCO Summary

| | Buy | Build | Partner |
|---|-----|-------|---------|
| Year 0 | $ | $ | $ |
| Year 1 | $ | $ | $ |
| Year 2 | $ | $ | $ |
| Year 3 | $ | $ | $ |
| **3-Year Total** | **$** | **$** | **$** |
| **NPV (10% discount)** | **$** | **$** | **$** |

Apply a 10% discount rate for NPV calculations unless the user specifies a different rate. Include a sensitivity analysis showing how the comparison shifts if costs are ±20% from estimates.
