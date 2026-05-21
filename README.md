# Agent Resource Catalog

A browsable, installable catalog of agentic plugins, standalone tools, and templates for Claude Cowork and Claude Code. Every plugin follows the Claude Cowork plugin format and is installable with a single `claude plugin install` command. The catalog is versioned in Git and rebuilt automatically on every merge to `main`.

## Quick Start

Register the catalog as a marketplace source:

```bash
claude plugin marketplace add StuKozola/agent-resource-catalog
```

Browse available plugins:

```bash
claude plugin search @agent-resource-catalog
```

Install a plugin:

```bash
claude plugin install product-manager@agent-resource-catalog
```

## Plugins

| Plugin | Description | Skills | Connectors |
|--------|-------------|--------|------------|
| [`product-manager`](plugins/product-manager/) | Pragmatic Framework execution (PRDs, roadmaps, personas, positioning, pricing, launch) combined with Seven Powers competitive strategy. | 21 | Linear, Notion, Slack, Figma, Dovetail |
| [`product-marketing`](plugins/product-marketing/) | Pragmatic Framework go-to-market toolkit (positioning, launch, content, channels, sales tools, measurement) combined with Seven Powers competitive strategy. | 24 | Notion, Slack, Salesforce, Dovetail, Amplitude |

## Skills Library

The `skills/` directory is a standalone library of reusable skill files organized by framework. Skills can be used directly in any plugin or fetched individually via raw URL.

| Category | Skills | What it covers |
|----------|--------|----------------|
| [`pragmatic-framework`](skills/pragmatic-framework/) | 35 | Product management and marketing methodology — market problems, buyer personas, positioning, pricing, launch, roadmap, requirements, and more |
| [`seven-powers-framework`](skills/seven-powers-framework/) | 5 | Competitive strategy and business moats — branding, cornered resource, counter-positioning, network economies, process power |
| [`agentic-systems`](skills/agentic-systems/) | 1 | AI agent operation and meta-reasoning — context management, subagent routing |
| [`matlab`](skills/matlab/) | 1 | MATLAB-specific skills — toolbox packaging and distribution |

## Fetching Without Cowork

Fetch the full catalog index:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/catalog.json
```

Fetch a single skill directly:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/competitive-landscape/SKILL.md
```

Fetch a plugin skill:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/plugins/product-manager/skills/competitive-landscape.md
```

Or use the fetch helper scripts:

```bash
# Bash (Linux/macOS)
./scripts/fetch.sh skill pragmatic-framework/competitive-landscape

# PowerShell (Windows)
.\scripts\fetch.ps1 skill pragmatic-framework/competitive-landscape
```

## Repository Structure

```
agent-resource-catalog/
├── catalog.json               # Auto-generated index of all plugins and standalone resources
├── plugins/                   # Installable Claude Cowork plugins
│   ├── product-manager/
│   └── product-marketing/
├── skills/                    # Reusable skill library (source of truth)
│   ├── pragmatic-framework/
│   ├── seven-powers-framework/
│   ├── agentic-systems/
│   └── matlab/
├── standalone/                # Executable tools and templates (coming soon)
├── scripts/                   # Automation: validate, build-catalog, fetch
└── schema/                    # JSON Schemas for manifests and catalog
```

## Contributing

Contributions are welcome — new plugins, skills, standalone tools, templates, and bug fixes. See [CONTRIBUTING.md](CONTRIBUTING.md) for directory layout, manifest requirements, naming conventions, and the PR checklist.

To validate locally before opening a PR:

```bash
pip install jsonschema
python scripts/validate.py
```

## License

MIT. See [LICENSE](LICENSE).
