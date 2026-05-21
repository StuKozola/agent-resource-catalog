# Agent Resource Catalog

A browsable, installable catalog of agentic plugins, standalone tools, and templates for Claude Cowork and Claude Code. Every plugin follows the Claude Cowork plugin format and is installable with a single `claude plugin install` command. The catalog is versioned in Git and rebuilt automatically on every merge to `main`.

## Quick Start

Register the catalog as a marketplace source:

```bash
claude plugin marketplace add StuKozola/agent-resource-catalog
```

Browse available plugins and tools:

```bash
claude plugin search @agent-resource-catalog
```

Install a plugin:

```bash
claude plugin install product-manager@agent-resource-catalog
```

## Plugins

| Plugin | Description | Skills | Commands | Connectors |
|--------|-------------|--------|----------|------------|
| `financial-analyst` | Equity research, portfolio analysis, and financial modeling. Pairs with market-data and accounting MCP servers. | `equity-research`, `earnings-analysis`, `portfolio-review` | `/build-model`, `/run-comps` | `boosted-insights`, `market-data` |
| `product-manager` | Product strategy, roadmap planning, PRD authoring, and cross-functional alignment. | `feature-prd`, `roadmap-planning`, `stakeholder-comms` | `/write-prd`, `/status-update` | `linear`, `notion`, `slack` |
| `data-engineer` | Data pipeline design, SQL optimization, schema migration, and dbt workflow support. | `pipeline-design`, `sql-review`, `schema-migration` | `/gen-migration`, `/profile-table` | `dbt`, `bigquery`, `postgres` |

## Standalone Tools & Templates

| Name | Type | Description |
|------|------|-------------|
| `pdf-extractor` | tool | Extracts structured text, tables, and metadata from PDF files into Markdown or JSON. |
| `data-analysis` | template | Starter template for exploratory data analysis with pandas, summary stats, and chart scaffolding. |
| `prd-scaffold` | template | Opinionated PRD document scaffold following the Pragmatic Product framework. |

## Fetching Without Cowork

You can fetch catalog metadata or individual skill files directly via raw GitHub URLs without installing anything.

Fetch the full catalog index:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/catalog.json
```

Fetch a specific skill file:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/plugins/product-manager/skills/feature-prd.md
```

Fetch a standalone tool manifest:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/standalone/tools/pdf-extractor/manifest.json
```

## Contributing

Contributions are welcome — new plugins, standalone tools, templates, and bug fixes. See [CONTRIBUTING.md](CONTRIBUTING.md) for directory layout, manifest requirements, naming conventions, and the PR checklist.

## License

MIT. See [LICENSE](LICENSE).
