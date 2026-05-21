# Switching Costs — Analytical Toolkit

This reference provides the complete set of frameworks, estimation methods, templates, and scoring tools for conducting a rigorous Switching Costs analysis using Hamilton Helmer's 7 Powers methodology.

## Table of Contents
1. Three-Type Switching Cost Mapping
2. Switching Cost Estimation — Step by Step
3. Precondition Validation
4. Follow-On Revenue Assessment
5. Durability and Threat Analysis
6. Competitor Response Assessment
7. Power Scoring Matrix
8. Deliverable Template

---

## 1. Three-Type Switching Cost Mapping

Before quantifying anything, map the switching costs present in the business across all three categories. Each category should be assessed independently.

### Financial Switching Costs — Inventory

Enumerate all direct monetary costs a customer would incur:

- **Replacement purchase costs**: New license fees, hardware, or subscription costs
- **Data migration costs**: Cost of extracting, transforming, and loading data into a new system
- **Customization reproduction**: Cost of rebuilding custom configurations, workflows, integrations, and reports
- **Complementary product replacement**: Cost of replacing add-on products, plugins, or connected tools that are specific to the current vendor
- **Contract penalties**: Early termination fees, minimum commitment shortfalls
- **Parallel running costs**: Period where both old and new systems must operate simultaneously
- **Downtime costs**: Revenue or productivity lost during transition
- **Consultant and implementation fees**: External support for the migration itself

### Procedural Switching Costs — Inventory

Enumerate all process and knowledge-related costs:

- **Retraining costs**: Time and expense to train employees on the new system
- **Productivity loss during learning curve**: Reduced output while employees become proficient
- **Process redesign**: Workflows, SOPs, and reporting built around the current product must be rebuilt
- **Error risk**: Mistakes during transition, especially in data-sensitive systems (finance, healthcare, compliance)
- **Organizational resistance**: The political and cultural cost of forcing change across departments
- **Certification and compliance**: Re-qualifying processes or certifications tied to the current vendor's platform
- **Institutional knowledge loss**: Undocumented expertise about workarounds, optimizations, and edge cases in the current system

### Relational Switching Costs — Inventory

Enumerate all relationship and emotional costs:

- **Vendor relationship loss**: Trust, context, and rapport with account managers, support teams, and consultants
- **Community disruption**: Loss of access to user communities, forums, peer networks, and events
- **Identity and affiliation**: Products that have become part of the customer's professional or personal identity
- **Co-created assets**: Joint projects, shared roadmaps, or collaborative developments with the current vendor
- **Reference and status**: Being a marquee customer of a prestigious vendor carries reputational value
- **Personal relationships**: Individual relationships between employees and vendor staff that provide preferential treatment

### Scoring Each Type

For each switching cost type, rate on a 1-5 scale:

| Category | Intensity (1-5) | Key Evidence | Estimated Cost ($) |
|----------|-----------------|--------------|-------------------|
| Financial | | What are the direct monetary costs? | |
| Procedural | | How deeply embedded is the product in daily workflows? | |
| Relational | | How strong are the interpersonal and community bonds? | |
| **Combined** | | | |

### Intensity Definitions

- **5 — Prohibitive**: Switching would be an existential risk or cost multiple years of operating budget (e.g., core ERP replacement for a Fortune 500)
- **4 — Very High**: Switching is theoretically possible but would cost millions and take 1-2+ years (e.g., migrating a large CRM implementation)
- **3 — Significant**: Switching would be painful and expensive but achievable within a budget cycle (e.g., changing marketing automation platforms)
- **2 — Moderate**: Switching causes meaningful friction but is regularly done (e.g., changing project management tools)
- **1 — Low**: Switching is inconvenient but cheap and fast (e.g., changing a note-taking app)

---

## 2. Switching Cost Estimation — Step by Step

### The Core Calculation

```
Total Switching Cost = Financial SC + Procedural SC + Relational SC
```

Express this as a ratio to the annual relationship value:

```
Switching Cost Ratio (SCR) = Total Switching Cost / Annual Revenue from Customer
```

A high SCR means the customer would spend more to leave than they spend in a typical year. This makes switching economically irrational for the customer.

### Worked Example 1: Enterprise ERP (SAP-class)

A mid-sized manufacturer ($2B revenue) running SAP with 15 years of customization:

**Financial switching costs:**
- New ERP license and implementation: $30M
- Data migration and validation: $8M
- Complementary application replacement: $12M
- Parallel running (6 months): $5M
- Consultant fees: $10M
- Financial subtotal: **$65M**

**Procedural switching costs:**
- Retraining 2,000+ users across all departments: $6M
- Productivity loss during 18-month learning curve: $15M
- Process redesign across 50+ workflows: $4M
- Error risk and remediation: $5M
- Procedural subtotal: **$30M**

**Relational switching costs:**
- Loss of vendor relationship context (harder to quantify): $2M estimated
- Community and ecosystem disruption: $1M
- Relational subtotal: **$3M**

**Total switching cost: ~$98M**
**Annual SAP spend: ~$25M** (licenses, maintenance, add-ons, consulting)
**SCR = 3.9x**

A switching cost ratio of nearly 4x annual spend means the customer would need almost four years just to break even on the switching investment — before any benefit from the new system materializes. This creates very strong Switching Costs Power.

### Worked Example 2: SaaS CRM (Salesforce-class)

A mid-market company ($200M revenue) with 500 Salesforce users and heavy customization:

**Financial switching costs:**
- New CRM license costs (net of Salesforce savings): $200K
- Data migration: $150K
- Custom object and workflow recreation: $400K
- Integration rebuilding (marketing, support, billing): $300K
- Financial subtotal: **$1.05M**

**Procedural switching costs:**
- Retraining 500 users: $250K
- Productivity loss (6-month learning curve): $500K
- Report and dashboard reconstruction: $100K
- Procedural subtotal: **$850K**

**Relational switching costs:**
- Account team relationship loss: $50K estimated
- Salesforce ecosystem knowledge loss: $50K
- Relational subtotal: **$100K**

**Total switching cost: ~$2M**
**Annual Salesforce spend: ~$600K**
**SCR = 3.3x**

Still a strong ratio, though more vulnerable to a competitor offering a well-funded migration program.

### Worked Example 3: Consumer Subscription (Streaming Service)

An individual Netflix subscriber:

**Financial switching costs:**
- New subscription cost (net): ~$0 (may even be cheaper)
- Content library rebuilding: $0 (no sunk cost in content)
- Financial subtotal: **~$0**

**Procedural switching costs:**
- Learning a new interface: Minimal (hours, not days)
- Rebuilding watch history and recommendations: Moderate annoyance
- Procedural subtotal: **~$20 equivalent**

**Relational switching costs:**
- Loss of shared profiles in household: Low-moderate
- Relational subtotal: **~$10 equivalent**

**Total switching cost: ~$30**
**Annual subscription: ~$180**
**SCR = 0.17x**

This is very low. Netflix does not have strong Switching Costs Power — its retention depends on content quality (operational excellence) and habit, not lock-in. This is why streaming services compete fiercely on content spending rather than switching cost creation.

### Interpreting the Switching Cost Ratio

| SCR Range | Power Strength | Interpretation |
|-----------|---------------|----------------|
| > 5.0x | Dominant | Customer is essentially locked in; switching is economically irrational under any scenario |
| 3.0–5.0x | Very Strong | Switching requires major strategic initiative; only justified by transformational improvement |
| 1.5–3.0x | Strong | Meaningful barrier; competitor needs substantially better offering plus migration investment |
| 0.5–1.5x | Moderate | Switching is painful but plausible; a well-funded competitor with migration support can win |
| 0.2–0.5x | Weak | Friction exists but won't prevent switching if a moderately better option appears |
| < 0.2x | Negligible | Customers can switch with minimal cost; no Power from switching costs |

---

## 3. Precondition Validation

### Follow-On Revenue Check

| Question | Answer | Implication |
|----------|--------|-------------|
| Does the customer make repeat purchases? | Y/N | If no, switching costs can't be monetized |
| Are there upgrade or expansion paths? | Y/N | Upsell revenue is a key switching cost monetization vector |
| Does the product have add-on or complementary products? | Y/N | Portfolio breadth multiplies switching cost value |
| Is there a maintenance or subscription stream? | Y/N | Recurring revenue is the most direct switching cost benefit |
| What % of total lifetime revenue comes after initial sale? | _% | Higher = more switching cost value |

**Rule of thumb**: If less than 50% of customer lifetime value comes from post-initial-sale revenue, Switching Costs Power will be limited regardless of how high the switching costs are.

### Pricing Arbitrage Check

| Question | Answer | Implication |
|----------|--------|-------------|
| Do customers negotiate heavily on initial pricing, expecting lock-in? | Y/N | If yes, some switching cost value is already given away upfront |
| Is there a "land and expand" dynamic where initial deal is discounted? | Y/N | Normal in SaaS — assess whether expansion revenue compensates |
| Do competitors offer aggressive migration incentives? | Y/N | If yes, the market is already pricing switching costs into competition |
| Is the switching cost premium publicly understood? | Y/N | Markets that openly discuss lock-in will price it in faster |

---

## 4. Follow-On Revenue Assessment

The value of Switching Costs Power is proportional to the follow-on revenue opportunity. Assess:

### Revenue Surface Mapping

```
Follow-On Revenue Surface = Maintenance + Subscriptions + Upgrades + Add-Ons + Professional Services + Complementary Products
```

Map each revenue stream:

| Revenue Stream | Annual Value | Growth Rate | Protected by SC? | SC Type |
|----------------|-------------|-------------|-------------------|---------|
| Core subscription/license | | | | |
| Maintenance and support | | | | |
| Upgrades and expansions | | | | |
| Add-on modules | | | | |
| Professional services | | | | |
| Complementary products | | | | |
| **Total follow-on** | | | | |

### Portfolio Extension Strategy

SAP's playbook — and the model for maximizing Switching Costs value — is to continuously extend the product portfolio so that more of the customer's spending is captured within the switching cost perimeter. Each new product acquired or built:

1. **Extends financial switching costs** — more products to replace
2. **Deepens procedural switching costs** — more workflows embedded
3. **Strengthens relational switching costs** — more touchpoints between organizations
4. **Expands the revenue surface** — more follow-on revenue to monetize

Assess whether the business is actively pursuing this strategy and how much runway remains.

---

## 5. Durability and Threat Analysis

Switching Costs can erode. Assess each threat:

### Technology Disruption Threats

| Threat | Likelihood (1-5) | Impact on SC (1-5) | Evidence |
|--------|------------------|---------------------|----------|
| Cloud/SaaS migration reducing on-premise lock-in | | | |
| Open standards or data portability mandates | | | |
| API standardization making integrations portable | | | |
| AI-assisted migration tools reducing procedural costs | | | |
| Platform consolidation reducing need for specialized tools | | | |
| New architecture paradigm making current product obsolete | | | |

### Competitive Threat Assessment

| Threat | Likelihood (1-5) | Impact on SC (1-5) | Evidence |
|--------|------------------|---------------------|----------|
| Competitor migration programs (free data migration, etc.) | | | |
| "Translator" or compatibility layers | | | |
| Aggressive pricing to compensate for switching costs | | | |
| Counter-positioned challenger with fundamentally different model | | | |
| Open-source alternative reducing financial switching costs | | | |

### Regulatory Threats

| Threat | Likelihood (1-5) | Impact on SC (1-5) | Evidence |
|--------|------------------|---------------------|----------|
| Data portability regulation (e.g., GDPR-style) | | | |
| Interoperability mandates | | | |
| Anti-lock-in procurement rules (government/regulated industries) | | | |
| Open data format requirements | | | |

### Durability Score

Average the likelihood × impact scores across all threats. Higher = more vulnerable.

| Durability Score | Interpretation |
|-----------------|----------------|
| < 5 | Very durable — threats are low probability or low impact |
| 5–10 | Durable — some threats exist but are manageable |
| 10–15 | Moderately durable — real threats that require active defense |
| 15–20 | Fragile — significant erosion risk within 3-5 years |
| > 20 | Very fragile — switching costs could collapse within 1-3 years |

---

## 6. Competitor Response Assessment

Competitors don't passively accept switching cost barriers. Map their likely responses:

### Migration Strategy Assessment

For each major competitor, assess:

| Competitor | Migration Tools? | Migration Subsidies? | Compatibility Layers? | Estimated SC Reduction |
|------------|-----------------|---------------------|----------------------|----------------------|
| | Y/N | Y/N + amount | Y/N | % reduction |
| | Y/N | Y/N + amount | Y/N | % reduction |
| | Y/N | Y/N + amount | Y/N | % reduction |

### "Net Switching Cost" Calculation

After accounting for competitor migration investments:

```
Net SC = Gross SC - Competitor Migration Subsidies - Value of Compatibility Tools - Value of Migration Services
```

The Net SC is what the customer actually faces when deciding whether to switch. If competitors are aggressively investing in migration support, the effective switching cost may be much lower than the gross estimate.

---

## 7. Power Scoring Matrix

Use this scoring framework to produce an overall assessment of Switching Costs Power.

| Dimension | Weight | Score (1-10) | Weighted Score |
|-----------|--------|--------------|----------------|
| Financial SC Intensity | 15% | | |
| Procedural SC Intensity | 15% | | |
| Relational SC Intensity | 10% | | |
| Switching Cost Ratio (SCR) | 15% | | |
| Follow-On Revenue Breadth | 15% | | |
| Durability Against Threats | 15% | | |
| Net SC After Competitor Response | 15% | | |
| **Total** | **100%** | | |

### Interpretation

| Total Weighted Score | Assessment |
|---------------------|------------|
| 8.0–10.0 | **Dominant Switching Costs** — Customers are deeply locked in. Switching is economically irrational. Multiple switching cost types compound. Follow-on revenue is broad and growing. |
| 6.0–7.9 | **Strong Switching Costs** — Meaningful Power exists. Customers face significant barriers to leaving. Some vulnerability to technology shifts or aggressive competitor migration. |
| 4.0–5.9 | **Moderate Switching Costs** — Friction exists but isn't decisive. Customers can and do switch when sufficiently motivated. Power may depend on complementary Powers. |
| 2.0–3.9 | **Weak Switching Costs** — Some customer inertia but not enough to constitute Power. Competitors can win customers with moderate effort. |
| < 2.0 | **No Switching Costs Power** — Customers can leave freely. Look for Power elsewhere. |

---

## 8. Deliverable Template

When producing a Switching Costs assessment, structure it as follows:

### Switching Costs Power Assessment: [Company/Product Name]

**Executive Summary** (2-3 sentences)
State whether Switching Costs Power exists, how strong it is, and which switching cost type is dominant.

**Business Context**
- Company/product being analyzed
- Customer profile (enterprise/SMB/consumer, typical size, industry)
- Nature of the ongoing customer relationship (subscription, maintenance, add-ons)
- Industry and lifecycle phase

**Precondition Validation**
- Follow-on revenue assessment: does it exist, how broad is it?
- Pricing arbitrage assessment: is the switching cost premium already priced in?

**Switching Cost Analysis — By Type**
- Financial switching costs: inventory and estimated magnitude
- Procedural switching costs: depth of embedding and organizational impact
- Relational switching costs: relationship strength and community bonds
- Combined Switching Cost Ratio (SCR)

**Follow-On Revenue Surface**
- Revenue streams protected by switching costs
- Portfolio extension strategy and runway
- Lifetime value impact

**Durability Assessment**
- Technology disruption threats
- Competitive migration threats
- Regulatory threats
- Overall durability score

**Power Score**
- Completed scoring matrix
- Overall assessment rating

**Strategic Implications**
- What this means for competitive strategy
- Recommendations for strengthening switching costs (if Power exists)
- Recommendations for monetizing the installed base without triggering backlash
- Recommendations for alternative strategy (if Switching Costs are weak)
- Assessment of the win-lose dynamic and customer relationship health
