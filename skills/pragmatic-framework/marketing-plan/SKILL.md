---
name: marketing-plan
description: >
  Guides creation of Marketing Plan documentation aligned with the Pragmatic Institute Framework.
  The Marketing Plan activity involves articulating strategies and tactics for generating awareness
  and leads for an upcoming fiscal period — including programs, events, campaigns, and channels —
  with measurements and goals tied to positioning and buyer personas. Use this skill whenever the
  user mentions marketing plan, marketing strategy, go-to-market plan, GTM plan, annual marketing
  plan, marketing programs, marketing budget, awareness and lead generation strategy, marketing
  calendar, campaign planning, or Pragmatic Framework Programs-category planning. Also trigger
  for building market-driven marketing plans, aligning programs with personas and positioning,
  planning demand generation, or creating fiscal-period marketing strategy. Suited to B2B and
  B2C product marketing.
---

# Marketing Plan — Pragmatic Framework Skill

## What This Skill Does

This skill helps you produce a **Marketing Plan** as defined by the Pragmatic Institute Framework. The Marketing Plan activity lives in the **Programs** category of the framework and is defined as:

> Articulate the strategies and tactics for generating awareness and leads for the upcoming fiscal period, including key programs and events with measurements and goals.

The output is a strategic marketing plan document that connects upstream market knowledge (positioning, buyer personas, buyer experience, competitive landscape) to downstream program execution (awareness, nurturing, launch, revenue growth, revenue retention). It gives marketing teams a market-driven roadmap that replaces inside-out guesswork with outside-in strategy.

## Context Within the Pragmatic Framework

Marketing Plan is one of 37 activities across 7 categories (Market, Focus, Business, Planning, Programs, Enablement, Support). It sits in **Programs** alongside Revenue Growth, Revenue Retention, Launch, Awareness, Nurturing, Advocacy, and Measurement.

The Marketing Plan is the strategic umbrella for the entire Programs category. While each sibling activity (Launch, Awareness, Nurturing, etc.) focuses on a specific execution area, the Marketing Plan ties them together into a cohesive, fiscally bounded strategy with shared goals and measurements.

### Key Dependencies (Inputs to Marketing Plan)

- **Positioning** — The foundation of all messaging. Every program in the marketing plan should trace back to positioning statements that describe the product by its ability to solve market problems. If the user hasn't completed positioning, prompt them to do so first or help create a lightweight positioning statement.
- **Buyer Personas** — Programs must target defined buyer archetypes. Without personas, marketing degenerates into generic messaging. The plan should specify which personas each program targets.
- **Buyer Experience** — Understanding the buying process tells you *where* in the journey to deploy each program. Awareness programs reach buyers at the top; nurturing programs move them through evaluation; sales tools support decision-stage buyers.
- **Competitive Landscape** — Knowing competitive strengths and weaknesses shapes differentiation messaging and helps prioritize competitive programs (battle cards, comparison content, displacement campaigns).
- **Market Definition** — Segment targeting determines where to invest marketing resources. The plan should align programs with the market segments identified as worth pursuing.
- **Business Plan** — The financial model and investment thesis constrain marketing budgets and set revenue expectations the marketing plan must support.
- **Product Roadmap** — Upcoming releases and milestones determine launch timing and campaign sequencing.

### What Marketing Plan Feeds Into

- **Revenue Growth** — The marketing plan's new-customer acquisition programs become Revenue Growth's detailed plans and budgets
- **Revenue Retention** — Customer marketing and loyalty programs flow into Revenue Retention
- **Launch** — Product launch strategies get their strategic framing from the marketing plan
- **Awareness** — Top-of-funnel brand and thought-leadership programs are defined in the plan
- **Nurturing** — Lead nurturing sequences and conversion programs originate here
- **Measurement** — Goals and KPIs established in the plan become Measurement's tracking targets
- **Sales Alignment** — Marketing programs must align with how sales sells; the plan bridges the gap
- **Content** — The plan identifies content needs mapped to buyer personas and journey stages

## Workflow

Before jumping to tactics, ground the plan in market knowledge. A Pragmatic marketing plan is market-driven, not activity-driven. The question is never "what programs should we run?" — it's "what do our buyers need to hear, see, and experience in order to recognize their problem, evaluate solutions, and choose us?"

### Step 1: Audit Available Inputs

Before building the plan, check what strategic inputs already exist. Read `references/input-audit.md` for a checklist of what to look for and how to work with incomplete inputs.

Ask the user:
- Do you have defined positioning by segment/persona?
- Do you have documented buyer personas?
- Do you have a buyer experience (journey) map?
- Do you have competitive landscape analysis?
- What's your fiscal period (annual, semi-annual, quarterly)?
- What's your approximate marketing budget or resource level?

If critical inputs are missing (especially positioning and buyer personas), help the user create lightweight versions before proceeding. A marketing plan built without positioning is just a list of activities.

### Step 2: Define Strategic Context

Read `references/strategic-foundation.md` for guidance on establishing the strategic context.

Work with the user to articulate:
1. **Market context** — What's happening in the market that shapes this plan? Market trends, competitive moves, customer behavior shifts.
2. **Business objectives** — What revenue, growth, or market share targets must the marketing plan support?
3. **Target segments and personas** — Which market segments and buyer personas are highest priority?
4. **Positioning pillars** — What are the core messages by persona and segment?
5. **Key challenges** — What competitive, internal, or market challenges must the plan address?

### Step 3: Map Programs to the Buyer Experience

Read `references/program-mapping.md` for the detailed methodology.

The heart of a Pragmatic marketing plan is mapping programs to the buyer's journey, not to an internal activity calendar. For each target persona:

1. **Awareness stage** — How will buyers become aware they have a problem and that solutions exist? Programs: thought leadership, content marketing, brand campaigns, analyst relations, events, SEO/SEM, social media.
2. **Education stage** — How will buyers learn enough to evaluate options? Programs: webinars, whitepapers, case studies, comparison guides, demo programs, nurturing sequences.
3. **Selection stage** — How will buyers make their final decision? Programs: ROI calculators, proof-of-concept support, reference programs, sales enablement, competitive displacement campaigns.
4. **Loyalty/Expansion stage** — How will existing customers deepen engagement? Programs: customer events, user groups, upsell/cross-sell campaigns, advocacy programs, renewal marketing.

### Step 4: Build the Program Portfolio

For each program in the plan, define:
- **Program name and description**
- **Target persona(s) and segment(s)**
- **Buyer journey stage**
- **Positioning message(s) it reinforces**
- **Channels and tactics**
- **Timeline and key milestones**
- **Budget allocation**
- **Success metrics (leading and lagging indicators)**
- **Owner and dependencies**

Read `references/metrics-measurement.md` for guidance on choosing the right metrics.

### Step 5: Assemble the Marketing Plan Document

Use the template in `templates/marketing-plan-document.md` for the complete plan structure.

Use the template in `templates/program-brief.md` for individual program briefs that detail each program.

### Step 6: Review and Align

The marketing plan is not a marketing-department document. It's a cross-functional alignment tool. Review with:
- **Product management** — Validate positioning, roadmap alignment, and launch timing
- **Sales leadership** — Confirm programs support how buyers buy and how sales sells
- **Executive leadership** — Validate budget, goals, and strategic alignment
- **Customer success** — Ensure retention and expansion programs reflect customer reality

## Output Formats

Depending on the user's needs, this skill can produce:

1. **Full Marketing Plan Document** — Comprehensive strategic document using `templates/marketing-plan-document.md`
2. **Program Brief** — Detailed brief for an individual program using `templates/program-brief.md`
3. **Executive Summary** — Condensed version for leadership alignment
4. **Marketing Calendar** — Timeline view of programs and milestones
5. **Budget Allocation Matrix** — Investment by segment, persona, journey stage, or program type

## Common Pitfalls

1. **Activity-driven instead of market-driven** — The plan lists tactics (blog posts, webinars, trade shows) without connecting them to positioning, personas, or the buyer experience. Every program should answer: "What persona does this reach, at what journey stage, with what message?"

2. **No connection to positioning** — Programs that don't trace back to positioning produce scattered, inconsistent messaging. If the plan can't point to a positioning statement for each program, the foundation is missing.

3. **Inside-out thinking** — The plan reflects what the company wants to say rather than what buyers need to hear. Pragmatic marketing demands outside-in: start with buyer problems and the buying process, then design programs to meet buyers where they are.

4. **Missing measurement** — A plan without metrics is a wishlist. Every program needs leading indicators (reach, engagement, pipeline contribution) and lagging indicators (revenue attribution, win rate impact).

5. **Ignoring existing customers** — Plans that focus exclusively on new-customer acquisition miss the revenue retention and expansion opportunity. The Pragmatic Framework explicitly separates Revenue Growth (new) and Revenue Retention (existing) for this reason.

6. **Disconnected from sales** — Marketing programs that don't align with the sales process create friction. The plan should map to Sales Alignment and include programs that equip sales with the right content and tools at each stage.

7. **Static plan syndrome** — A marketing plan that's written once and shelved is useless. Build in quarterly review cadences and clear criteria for adjusting programs based on performance data.

8. **Budget without strategy** — Allocating budget by channel ("40% digital, 30% events, 30% content") instead of by strategic priority (persona, segment, journey stage) leads to activity sprawl.
