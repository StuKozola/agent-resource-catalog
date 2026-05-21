---
name: pragmatic-asset-assessment
description: >
  Guides users through the Asset Assessment activity from the Pragmatic Marketing Framework
  (Pragmatic Institute). This skill helps product managers, product marketers, and business
  strategists inventory their organization's assets (technical capabilities, skills, services,
  patents, IP, marketing materials, and other resources) and determine how those assets can be
  leveraged to accelerate product development, reduce costs, and uncover new market opportunities.
  Use this skill whenever the user mentions asset assessment, asset inventory, asset registry,
  asset audit, leveraging existing assets, Pragmatic Framework asset assessment, cataloging
  company capabilities, or wants to identify what internal resources they can reuse for new
  products. Also trigger when users ask about the "Market" category of the Pragmatic Framework
  specifically related to assets, or when they want to build an asset registry or evaluate
  what they already have before building something new.
---

# Pragmatic Marketing Framework — Asset Assessment

## What Is Asset Assessment?

Asset Assessment is one of the core activities in the **Market** category of the Pragmatic Framework (formerly the Pragmatic Marketing Framework) developed by Pragmatic Institute. The official definition is:

> **Inventory your assets (technical, skills, services, patents, other) and determine ways that they can be leveraged.**

The purpose is to catalog everything of value your organization already possesses — technology, knowledge, intellectual property, skills, components, marketing materials, and more — so you can strategically deploy those assets to get to market faster, reduce costs, and discover opportunities that might not be immediately obvious.

Asset Assessment sits alongside four other Market activities: Market Problems, Win/Loss Analysis, Distinctive Competencies, and Competitive Landscape. Together, they ensure the product team deeply understands both the external market and the internal capabilities available to address it.

## Why Asset Assessment Matters

Asset Assessment delivers four key benefits:

1. **Increase Efficiency** — Identifies redundancies and areas where processes can be streamlined. By evaluating current systems, you uncover places where processes can be built or improved.
2. **Reduce Costs** — Ensures resources are used cost-effectively. Existing elements can jumpstart new products, releases, or marketing campaigns rather than building from scratch.
3. **Identify New Opportunities** — Reveals potential areas for growth, new markets to explore, or novel combinations of existing assets that create new value.
4. **Enhance Communication & Collaboration** — Breaks down organizational silos that slow development by making asset information visible and shared across teams.

## When to Conduct Asset Assessment

Pragmatic Institute recommends performing asset assessments on a **quarterly or annual basis**. The assessment should also be consulted whenever:
- Evaluating new product opportunities (to check if existing assets can shorten time to market)
- Initiating new projects (to reduce overall cost by reusing components)
- Entering new markets (to identify transferable capabilities)
- After acquisitions or major organizational changes

## Asset Categories

When conducting an inventory, organize assets into these categories. Read `references/asset-categories.md` for detailed descriptions and example questions for each category.

| Category | Examples |
|---|---|
| **Technology** | Platforms, modules, APIs, SDKs, infrastructure, development tools, internal tools, sandbox prototypes |
| **Intellectual Property** | Patents (granted and pending), trade secrets, proprietary algorithms, copyrights, trademarks |
| **Skills & Expertise** | Domain knowledge, specialized technical skills, process expertise, industry certifications, regulatory knowledge |
| **Products & Components** | Current products, withdrawn products, reusable product components, libraries, microservices |
| **Services** | Professional services capabilities, support infrastructure, consulting methodologies, training programs |
| **Marketing & Content** | Positioning documents, messaging frameworks, case studies, whitepapers, brand assets, customer testimonials, sales tools |
| **Data & Analytics** | Customer data, market research, usage analytics, performance benchmarks, competitive intelligence |
| **Relationships** | Partner ecosystems, channel relationships, customer advisory boards, industry analyst connections |

## How to Conduct the Assessment

### Step 1: Kickoff & Scope

Hold a kickoff meeting to explain the goals and objectives of the assessment. Clarify:
- Which product lines or business units are in scope
- What time frame to cover
- Who the key stakeholders and subject matter experts are
- Where existing asset documentation lives today

### Step 2: Identify Subject Matter Experts

Map out the people who hold deep knowledge of the organization's assets. These include experts in your markets, processes, and technology. Prioritize face-to-face or live meetings over form-filling — interactive conversations uncover assets that might be overlooked on a form.

### Step 3: Inventory Assets

For each asset category, document:
- **Asset Name** — A clear, recognizable identifier
- **Date Added/Created** — When the asset was created or acquired
- **Asset Type** — Which category it belongs to (technology, IP, skills, etc.)
- **Status** — In production, in development, shelved, deprecated, or retired
- **Owner** — The person or team responsible for the asset
- **Description** — What the asset does and what makes it valuable
- **Used In** — Which products, projects, or processes currently use it
- **Last Updated** — When the asset was last modified or reviewed
- **Leverage Potential** — How this asset could be applied to new opportunities

### Step 4: Consolidate into an Asset Registry

All information should be consolidated into a **single asset registry** — typically a spreadsheet or database. This registry should be:
- Shared throughout the organization
- Consulted when new projects are initiated
- Referenced when evaluating new opportunities
- Updated as assets are created, modified, or retired

### Step 5: Analyze & Identify Leverage Opportunities

Once the inventory is complete, analyze the registry to find:
- **Quick wins** — Assets that can be immediately applied to current initiatives
- **Gap analysis** — Areas where the organization lacks assets relative to market needs
- **Combination opportunities** — Assets from different categories that could be combined to create new value
- **Underutilized assets** — Valuable capabilities that are not being fully leveraged
- **At-risk assets** — Assets that are aging, unsupported, or at risk of obsolescence

### Step 6: Prioritize & Create an Action Plan

For each identified opportunity:
- Estimate the impact (time savings, cost reduction, revenue potential)
- Assess feasibility and effort required
- Assign ownership
- Set timelines for action

## Relationship to Other Pragmatic Framework Activities

Asset Assessment does not exist in isolation. It connects to:

- **Distinctive Competencies** — Your assets are the foundation of your distinctive competencies. The assessment reveals what unique abilities you can articulate and leverage.
- **Competitive Landscape** — Understanding your assets helps you identify where you have competitive advantages or disadvantages.
- **Market Problems** — Known assets influence which market problems you are best positioned to solve.
- **Innovation** — The creative combination of existing assets can drive innovation without requiring entirely new development.
- **Buy, Build, or Partner** — The asset registry directly informs make-vs-buy decisions by clarifying what you already have.
- **Business Plan** — Asset assessment feeds into realistic business planning by establishing what resources are available.

## Deliverables

When the skill is triggered, help the user produce one or more of these deliverables:

1. **Asset Registry** (spreadsheet) — The comprehensive inventory. Read `references/asset-registry-template.md` for the recommended column structure and format.
2. **Asset Assessment Summary** (document) — An executive-level narrative summarizing findings, key leverage opportunities, gaps, and recommended actions.
3. **Opportunity Matrix** — A prioritized view of leverage opportunities mapped against impact and feasibility.

## Workflow When User Triggers This Skill

1. **Understand context** — Ask the user about their organization, product line, and what prompted the assessment. Determine if they want a full assessment or are focused on a specific area.
2. **Choose deliverable** — Confirm which deliverable(s) they need (registry, summary, matrix, or all three).
3. **Guide the inventory** — Walk through asset categories one by one, asking targeted questions. Use the detailed prompts in `references/asset-categories.md` to draw out assets the user might not think of.
4. **Build the registry** — Use the xlsx skill (read `/mnt/skills/public/xlsx/SKILL.md`) to create a properly formatted Asset Registry spreadsheet.
5. **Analyze findings** — Help identify leverage opportunities, gaps, and quick wins.
6. **Produce summary** — If requested, use the docx skill (read `/mnt/skills/public/docx/SKILL.md`) to create a professional Asset Assessment Summary document.
7. **Create opportunity matrix** — If requested, build a prioritized matrix as an additional worksheet or standalone visual.

## Important Notes

- Few people start from a completely blank slate. Ask the user about any existing systems, documents, or informal knowledge bases that already capture some asset information.
- The sandbox matters — many organizations have prototype capabilities or experimental technology that never shipped. These are valuable assets to capture.
- Marketing materials and messaging from previous campaigns are often overlooked but can be powerful assets to leverage or update.
- Asset assessment is a team effort. If the user is doing this alone, encourage them to involve subject matter experts from across the organization.
- The registry is a living document. Emphasize that it should be updated regularly, not created once and forgotten.
