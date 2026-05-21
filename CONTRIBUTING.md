# Contributing to Agent Resource Catalog

## Overview

The catalog hosts two types of resources:

- **Plugins** — full Claude Cowork plugins installed with `claude plugin install`. Each plugin lives under `plugins/<name>/` and bundles a manifest, skills, optional slash-commands, and optional MCP connector wiring.
- **Standalone resources** — tools, templates, and configs that can be fetched and used directly without the Cowork plugin system. Each resource lives under `standalone/tools/` or `standalone/templates/` and carries a `manifest.json`.

Both types are validated by `scripts/validate.py` on every PR and indexed into `catalog.json` on merge.

---

## Contributing a Plugin

1. Create a directory under `plugins/` using a kebab-case name that reflects the role or domain (e.g. `plugins/financial-analyst`).
2. Add `.claude-plugin/plugin.json` inside that directory. See [Plugin Manifest](#plugin-manifest-pluginjson) below for the required fields and an example.
3. Add at least one skill file under `skills/`. See [Skill Files](#skill-files) for the required frontmatter format.
4. Optionally add slash-command files under `commands/`. See [Command Files](#command-files).
5. Optionally add `.mcp.json` to wire MCP connectors. See [Connector Wiring](#connector-wiring-mcpjson).
6. Run `python scripts/validate.py` locally and confirm all checks pass.
7. Open a PR. The PR checklist at the bottom of this file must be satisfied before merge.

---

## Plugin Manifest (`plugin.json`)

The manifest lives at `plugins/<name>/.claude-plugin/plugin.json` and must validate against `schema/plugin.schema.json`.

**Example — `plugins/product-manager/.claude-plugin/plugin.json`:**

```json
{
  "name": "product-manager",
  "version": "1.0.0",
  "description": "Product strategy, roadmap planning, PRD authoring, and cross-functional alignment for product managers.",
  "author": "your-name-or-team",
  "category": "role",
  "tags": ["product", "roadmap", "prd", "stakeholders"],
  "min_claude_version": "claude-sonnet-4",
  "homepage": "https://github.com/StuKozola/agent-resource-catalog/tree/main/plugins/product-manager",
  "plugin_format_version": "1"
}
```

**Field reference:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique plugin identifier. Must be kebab-case (`^[a-z][a-z0-9-]*$`). Must match the directory name under `plugins/`. |
| `version` | Yes | Semantic version string (e.g. `1.0.0`). Bump on every meaningful change. |
| `description` | Yes | One or two sentences describing what this plugin does. Minimum 10 characters. |
| `author` | Yes | Author or team name. |
| `category` | No | One of `role`, `workflow`, or `domain`. Used for catalog filtering. |
| `tags` | No | Array of kebab-case strings for search and discovery. |
| `min_claude_version` | No | Minimum Claude model identifier required (e.g. `claude-sonnet-4`). |
| `homepage` | No | Full URI to documentation or source. |
| `plugin_format_version` | No | Cowork plugin format version. Defaults to `"1"`. |

---

## Skill Files

Skills are Markdown files that Claude loads automatically when a matching user intent is detected. They live under `plugins/<name>/skills/` and are named in kebab-case.

**Required frontmatter:**

```markdown
---
name: feature-prd
description: When the user asks to write, draft, or create a Product Requirements Document or PRD, use this skill.
---

# Feature PRD

When the user asks to write a PRD, use this skill to produce a structured requirements document following the Pragmatic Product framework.

## Process

1. Clarify the problem statement and target persona.
2. Draft the context and background section.
3. Define goals and non-goals.
4. Enumerate functional requirements with priority (P0/P1/P2).
5. Identify open questions and risks.
6. Summarize success metrics.
```

The `name` field must match the filename (without `.md`). The `description` field is the auto-trigger sentence Claude uses to decide when to load this skill — write it as "When the user asks about X, use this skill."

Keep skills focused on a single domain or workflow. If a skill file grows beyond approximately 500 lines, split it into more focused skills.

---

## Command Files

Commands are Markdown files that define explicit slash-command invocations. They live under `plugins/<name>/commands/` and are named in kebab-case. Unlike skills, commands are never loaded automatically — the user must type the slash command explicitly.

**Example format:**

```markdown
---
name: write-prd
description: Generates a complete PRD document for a feature or initiative.
---

# /write-prd

## Inputs

- Feature name or brief description (required)
- Target persona (optional — defaults to primary ICP if omitted)
- Deadline or milestone (optional)

## Steps

1. Ask the user for any missing required inputs.
2. Run the `feature-prd` skill to produce a structured PRD draft.
3. Present the draft and ask for feedback.
4. Incorporate revisions and finalize.

## Output

A complete PRD in Markdown, ready to paste into Notion or Linear.
```

If a user would benefit from a behavior running automatically (without typing a command), implement it as a skill instead of a command.

---

## Connector Wiring (`.mcp.json`)

Plugins that need access to external data sources or APIs declare their MCP server dependencies in `.mcp.json` at the plugin root. This file maps logical connector names to MCP registry IDs so that installers can substitute their own server configuration.

**Example — `plugins/financial-analyst/.mcp.json`:**

```json
{
  "mcpServers": {
    "market-data": {
      "registry_id": "mcp-market-data",
      "description": "Real-time and historical market price and fundamentals data.",
      "required": true
    },
    "data-warehouse": {
      "registry_id": "mcp-snowflake",
      "description": "Cloud data warehouse for portfolio and financial data.",
      "required": false
    }
  }
}
```

Server names (e.g. `market-data`) are the logical identifiers that skills and commands reference. The `registry_id` values reference published MCP registry IDs — not hardcoded connection strings or credentials. This allows each installer to wire in their own stack while the plugin code remains portable.

---

## Shared Skills Policy

Some skills (e.g. `stakeholder-comms`, `sql-review`) are useful across multiple plugins. The catalog does **not** use symlinks or shared references — each plugin directory is self-contained and contains its own copy of any shared skill files.

CI runs a drift check (`scripts/check-drift.py`) that flags divergence between copies of the same skill across plugins. When you update a shared skill in one plugin, you must update it in all other plugins that include a copy. The CI check will fail the PR if copies are out of sync.

---

## Contributing a Standalone Resource

1. Create a directory under `standalone/tools/` (for executable scripts or utilities) or `standalone/templates/` (for scaffold and starter files), using a kebab-case name.
2. Add `manifest.json` inside that directory. See [Standalone Manifest](#standalone-manifest-manifestjson) below.
3. Add the entry point file and any supporting files listed in `manifest.json`'s `files` array.
4. Run `python scripts/validate.py` locally and confirm all checks pass.
5. Open a PR.

---

## Standalone Manifest (`manifest.json`)

The manifest lives at `standalone/tools/<name>/manifest.json` (or `standalone/templates/<name>/manifest.json`) and must validate against `schema/standalone.schema.json`.

**Example — `standalone/tools/pdf-extractor/manifest.json`:**

```json
{
  "name": "pdf-extractor",
  "type": "tool",
  "version": "1.0.0",
  "description": "Extracts structured text, tables, and metadata from PDF files into Markdown or JSON.",
  "authors": ["your-name-or-team"],
  "license": "MIT",
  "files": ["pdf_extractor.py", "requirements.txt", "README.md"],
  "entry_point": "pdf_extractor.py",
  "tags": ["pdf", "extraction", "text", "tables"],
  "compatibility": {
    "platforms": ["win32", "darwin", "linux"],
    "runtime": "python>=3.11"
  },
  "dependencies": ["pdfplumber>=0.10", "rich>=13"]
}
```

**Field reference:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique resource identifier in kebab-case. Must match the directory name. |
| `type` | Yes | One of `tool`, `template`, or `config`. |
| `version` | Yes | Semantic version string. |
| `description` | Yes | One or two sentences describing what this resource does. Minimum 10 characters. |
| `authors` | Yes | Array of author or maintainer names. At least one required. |
| `license` | Yes | SPDX license identifier (e.g. `MIT`, `Apache-2.0`). |
| `files` | Yes | Array of filenames included in this resource, relative to its directory. At least one required. |
| `entry_point` | Yes | The primary file to run or reference. Must also appear in `files`. |
| `tags` | No | Array of kebab-case strings for catalog filtering. |
| `compatibility` | No | Object with optional `platforms` (array) and `runtime` (string) fields. |
| `dependencies` | No | Array of runtime dependencies in pip or npm specifier format. |
| `checksum` | No | SHA-256 hex digest of the `entry_point` file for integrity verification. |

---

## Naming Conventions

| Artifact | Convention | Examples |
|----------|------------|---------|
| Plugin directory | Kebab-case, role or domain name | `financial-analyst`, `product-manager`, `data-engineer` |
| Skill file | Kebab-case, describes the capability | `equity-research.md`, `feature-prd.md`, `sql-review.md` |
| Command file | Kebab-case, describes the action | `build-model.md`, `write-prd.md`, `gen-migration.md` |
| Standalone directory | Kebab-case, describes the tool or template | `pdf-extractor`, `data-analysis`, `prd-scaffold` |

---

## Running Validation Locally

Install the required dependency and run the validation script from the repo root:

```bash
pip install jsonschema
python scripts/validate.py
```

The script validates every `plugin.json`, every standalone `manifest.json`, and `catalog.json` against their respective schemas. It also checks that skill frontmatter includes required fields and that `.mcp.json` files do not contain hardcoded connection strings.

---

## PR Checklist

Before opening a pull request, confirm the following:

- [ ] `python scripts/validate.py` passes locally with no errors
- [ ] Skill files have required frontmatter (`name`, `description`)
- [ ] Command files include Inputs, Steps, and Output sections
- [ ] Shared skill copies are in sync across all plugins that include them (or updated in all)
- [ ] New plugins have at least one skill file under `skills/`
- [ ] `.mcp.json` uses MCP registry IDs, not hardcoded connection strings or credentials
