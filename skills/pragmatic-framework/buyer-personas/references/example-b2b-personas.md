# Example: B2B Buyer Personas for Cloud Infrastructure Monitoring Platform

This example demonstrates what completed buyer personas look like for a fictional B2B SaaS product — "CloudWatch Pro," a cloud infrastructure monitoring and observability platform sold to mid-market and enterprise companies.

These personas were developed for the primary market segment: mid-market SaaS companies (200–2,000 employees) with hybrid cloud infrastructure.

---

## Buying Committee Overview

| Persona | Buying Role | Decision Authority | Entry Point |
|---|---|---|---|
| The Platform Engineering Lead | Champion / Lead Evaluator | Strong influencer; leads evaluation | Early — triggers evaluation |
| The VP of Engineering | Economic Buyer | Final decision maker | Mid — joins at shortlist |
| The Security & Compliance Lead | Technical Buyer / Gatekeeper | Blocker (veto power on security) | Mid — joins during technical evaluation |

---

## Persona 1: The Platform Engineering Lead

**Persona label:** The Platform Engineering Lead
**Typical job titles:** Senior Platform Engineer, Staff SRE, Infrastructure Team Lead, DevOps Lead
**Seniority level:** Senior IC or Team Lead
**Department:** Platform Engineering / SRE / DevOps
**Market segment:** Mid-market SaaS companies, 200–2,000 employees

### Role in the Buying Process

- **Buying role type:** Champion / Lead Evaluator
- **Decision authority:** Strong influencer — leads the evaluation, recommends the shortlist, and presents findings to the VP of Engineering. Does not hold budget authority.
- **When they enter the process:** Early. Typically the person who identifies the problem and initiates the search for solutions.
- **Who they report to:** VP of Engineering or Director of Platform Engineering
- **Who they influence:** The entire evaluation committee. Their technical recommendation carries significant weight.
- **Veto power:** Effective veto — if they recommend against a product, it rarely moves forward.

### Professional Context

- **Company size:** 200–2,000 employees, $20M–$500M revenue
- **Team size:** Manages or leads 3–8 engineers
- **Key responsibilities:** Maintaining infrastructure reliability; defining observability strategy; managing monitoring tool stack; on-call rotation coordination; capacity planning
- **KPIs:** Uptime (99.9%+), mean time to detection (MTTD), mean time to resolution (MTTR), infrastructure cost per transaction
- **Tools used daily:** Terraform, Kubernetes, Grafana, PagerDuty, Slack, Datadog or Prometheus (incumbent tools they may be replacing)
- **Budget authority:** No direct budget. Submits purchase recommendations with justification to VP.

### Problems and Pain Points

1. "We have six different monitoring tools and none of them talk to each other. When something breaks at 2 AM, I'm flipping between dashboards trying to piece together what happened."
2. "Our current setup generates so many false alerts that the team has started ignoring them. We missed a real outage last month because it looked like noise."
3. "Every time we spin up a new service, it takes two days just to get monitoring configured. It should take ten minutes."
4. "We're growing fast and our monitoring costs are scaling linearly with infrastructure. The bill is getting hard to justify."

- **Status quo:** A patchwork of open-source tools (Prometheus, Grafana, ELK stack) with some commercial point solutions. Maintained by 1–2 engineers who have become bottlenecks.
- **Cost of inaction:** Increasing MTTR, engineer burnout from on-call noise, risk of customer-impacting outages that damage trust and revenue.

### Goals and Success Criteria

- **Functional:** Unified observability across metrics, logs, and traces. Auto-instrumentation for new services. Intelligent alerting that reduces noise by 80%+.
- **Emotional:** Confidence that when something breaks, the team will know about it before customers do.
- **Career:** Be recognized as the person who modernized the company's observability practice.
- **Success metrics:** MTTD < 2 minutes, false alert rate < 5%, new service instrumentation in < 30 minutes.
- **Timeline:** Expects to see measurable improvements within the first 60 days of deployment.

### Buying Behavior

- **Triggers:** Major outage that exposed monitoring gaps; team scaling event (new hires overwhelmed by tool complexity); existing vendor price increase at renewal; mandate from VP to improve reliability metrics.
- **Research behavior:** Starts with peer recommendations (Slack communities, Reddit r/devops, HackerNews). Reviews G2 and Gartner reports. Attends vendor-sponsored webinars if the topic is educational, not salesy. Signs up for free trials immediately.
- **Evaluation approach:** Runs a 2–4 week POC with real production data. Evaluates 2–3 shortlisted vendors simultaneously. Writes an internal evaluation document comparing features, performance, and cost.
- **Sales cycle:** 4–8 weeks from first trial to signed contract.

### Decision Criteria

- **Must-haves:** Kubernetes-native, OpenTelemetry support, sub-minute alerting, SSO integration
- **Differentiators:** Ease of setup (time-to-value), intelligent alert correlation, cost predictability
- **Risk tolerance:** Moderate. Willing to try newer vendors if the technology is sound, but wants to see it handle production-scale data before committing.

### Information Sources

- **Trusted:** Peer engineers, CNCF community, DevOps conferences (KubeCon), engineering blogs from respected companies
- **Preferred formats:** Technical documentation, architecture diagrams, hands-on trials, short demo videos (< 10 min)
- **Vernacular:** "observability," "SLOs," "cardinality," "traces," "OTEL," "toil reduction"
- **Avoid:** Enterprise sales jargon, "AI-powered" without substance, slideware without a working demo

### Objections

1. "We've tried commercial monitoring before and ended up locked into a vendor with unpredictable pricing."
2. "My team has built custom tooling around our current stack. Migrating will be painful."
3. "How do I know this will scale when we 10x our infrastructure next year?"

### Day in the Life

They start the morning reviewing overnight alerts in Slack — most are noise, which they triage and dismiss before standup. After standup, they spend two hours helping a team debug a latency spike, bouncing between three dashboards to correlate metrics with logs. After lunch, they review a pull request for a new service and realize they need to manually add monitoring configuration — again. By 4 PM, they're in a meeting with their VP presenting last month's reliability metrics and fielding questions about why MTTR increased. They leave the office knowing they're on-call tonight.

### Key Quotes

- *"I don't want another dashboard. I want one place that tells me what's broken and why."*
- *"If I can't get it running in under an hour, I'm not going to champion it internally."*
- *"Show me it works with our actual data. I don't trust vendor benchmarks."*

### Messaging Guidance

- **Value prop:** "See everything, fix faster — unified observability that your platform team will actually want to use."
- **Proof points:** Architecture diagram, 15-minute quickstart guide, case study from a similar-sized SaaS company showing MTTR reduction
- **Use:** Technical precision, specific numbers, open standards references
- **Avoid:** "Enterprise-grade," "AI-driven insights" (without specifics), ROI projections (save those for the VP)

### Validation Status

- **Data sources:** [EXAMPLE — in a real persona, list actual sources]
- **Confidence:** Medium — based on 6 win/loss interviews and internal product team knowledge. Needs validation with broader market interviews.
- **Last validated:** [Date]
- **Next review:** [Quarterly]
- **Open questions:** How does this persona differ at companies with dedicated SRE teams vs. those where developers own their own monitoring?

---

*The VP of Engineering and Security Lead personas would follow the same structure, with different emphases — the VP would focus more on budget, strategic alignment, and team productivity metrics; the Security Lead would focus on data residency, compliance frameworks, and access controls.*
