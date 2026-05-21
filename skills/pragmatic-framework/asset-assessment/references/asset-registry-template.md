# Asset Registry Template — Reference

This reference describes the recommended structure for the Asset Registry spreadsheet, which is the primary deliverable of the Asset Assessment activity.

## Registry Structure

The Asset Registry should be created as an Excel (.xlsx) file with multiple worksheets.

### Worksheet 1: Asset Registry

This is the main inventory. Use the following columns:

| Column | Description | Example Values |
|---|---|---|
| **Asset ID** | Unique identifier (auto-increment or category prefix) | TECH-001, IP-003, SKILL-012 |
| **Asset Name** | Clear, recognizable name | "FTP Transfer Module", "Customer Segmentation Algorithm" |
| **Category** | One of the 8 asset categories | Technology, IP, Skills, Products, Services, Marketing, Data, Relationships |
| **Subcategory** | More specific classification within the category | "API", "Patent", "Domain Expertise", "Case Study" |
| **Date Added** | When the asset was first created or acquired | 2024-03-15 |
| **Status** | Current state of the asset | In Production, In Development, Shelved, Deprecated, Retired |
| **Owner** | Person or team responsible | "Data Engineering Team", "Jane Smith" |
| **Description** | What the asset is and why it's valuable | "Module supporting FTP file transfers with encryption" |
| **Currently Used In** | Products, projects, or processes using this asset | "Product A, Product C" |
| **Last Updated** | When the asset was last modified or reviewed | 2025-01-10 |
| **Leverage Potential** | How this could be applied to new opportunities | "Could be adapted for cloud-to-cloud data transfer" |
| **Leverage Score** | 1-5 rating of reuse potential (5 = highest) | 4 |
| **Notes** | Additional context | "Requires modernization of authentication layer" |

### Worksheet 2: Opportunity Matrix

A prioritized view of leverage opportunities identified during the assessment.

| Column | Description |
|---|---|
| **Opportunity ID** | Unique identifier |
| **Opportunity Description** | What could be done with the asset(s) |
| **Related Asset(s)** | Asset IDs from the registry |
| **Impact** | High / Medium / Low — estimated business impact |
| **Feasibility** | High / Medium / Low — how easy to execute |
| **Priority Score** | Calculated or assigned priority (e.g., Impact × Feasibility) |
| **Estimated Time Savings** | How much time reuse could save |
| **Estimated Cost Savings** | How much cost reuse could save |
| **Recommended Action** | What to do next |
| **Assigned To** | Owner of the action item |
| **Target Date** | When to complete the action |
| **Status** | Not Started, In Progress, Complete |

### Worksheet 3: Gap Analysis

Areas where the organization lacks assets relative to market needs.

| Column | Description |
|---|---|
| **Gap ID** | Unique identifier |
| **Category** | Which asset category the gap falls in |
| **Description** | What's missing |
| **Market Need** | The market problem or opportunity this gap relates to |
| **Severity** | Critical / Important / Nice-to-Have |
| **Recommended Action** | Build, Buy, Partner, or Accept |
| **Estimated Investment** | Rough cost to close the gap |
| **Notes** | Additional context |

### Worksheet 4: Summary Dashboard

A high-level summary worksheet with:
- Total assets by category (counts)
- Assets by status (In Production vs Shelved vs Deprecated, etc.)
- Top leverage opportunities
- Critical gaps
- Last assessment date and next scheduled assessment

## Formatting Guidelines

When creating the registry using the xlsx skill:
- Use a header row with bold text and a colored background
- Freeze the top row for easy scrolling
- Apply data validation for Status and Category columns (dropdown lists)
- Use conditional formatting on Leverage Score (green for 4-5, yellow for 3, red for 1-2)
- Auto-fit column widths
- Add the organization name and assessment date at the top of each worksheet
- Include a "Last Review" date field prominently displayed

## Naming Convention

Name the file: `Asset_Registry_[CompanyName]_[YYYY-MM-DD].xlsx`

If the company name is not known, use: `Asset_Registry_[YYYY-MM-DD].xlsx`
