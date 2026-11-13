# Agent Resource Catalog

A browsable, installable catalog of agentic plugins, standalone tools, and templates for Claude Cowork and Claude Code. Every plugin follows the Claude Cowork plugin format and is installable with a single `claude plugin install` command. The catalog is versioned in Git and rebuilt automatically on every merge to `main`.

**Browse online:** https://stukozola.github.io/agent-resource-catalog/
**Catalog JSON:** https://stukozola.github.io/agent-resource-catalog/catalog.json

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
| [`product-manager`](plugins/product-manager/) | 2027 Pragmatic Framework from market problems and product strategy through requirements, roadmaps, business outcomes and post-launch operations, combined with Seven Powers competitive strategy. | 35 | Linear, Notion, Slack, Figma, Dovetail |
| [`product-marketing`](plugins/product-marketing/) | 2027 Pragmatic Framework go-to-market and enablement toolkit (positioning, buyer journey, launch, growth, retention, engagement, content, assets, channel support, measurement) combined with Seven Powers competitive strategy. | 31 | Notion, Slack, Salesforce, Dovetail, Amplitude |

## Skills Library

The `skills/` directory is a standalone library of reusable skill files organized by framework. Skills can be used directly in any plugin or fetched individually via raw URL.

| Category | Skills | What it covers |
|----------|--------|----------------|
| [`pragmatic-framework`](skills/pragmatic-framework/) | 38 | The 2027 Pragmatic Framework: one skill for each of the 37 focus areas across Market, Focus, Business, Planning, Go-to-Market, Enablement and Operations, plus an overview and router. See the [folder README](skills/pragmatic-framework/README.md) for skills renamed in 2027. |
| [`seven-powers-framework`](skills/seven-powers-framework/) | 7 | Competitive strategy and business moats — branding, cornered resource, counter-positioning, network economies, process power, scale economies, switching costs |
| [`agentic-systems`](skills/agentic-systems/) | 1 | AI agent operation and meta-reasoning — context management, subagent routing |
| [`matlab`](skills/matlab/) | 1 | MATLAB-specific skills — toolbox packaging and distribution |

## Fetching Without Cowork

Fetch the full catalog index:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/catalog.json
```

Fetch a single skill directly:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/skills/pragmatic-framework/pragmatic-competitive-landscape/SKILL.md
```

Fetch a plugin skill:

```bash
curl https://raw.githubusercontent.com/StuKozola/agent-resource-catalog/main/plugins/product-manager/skills/pragmatic-competitive-landscape.md
```

Or use the fetch helper scripts:

```bash
# Bash (Linux/macOS)
./scripts/fetch.sh skill pragmatic-framework/pragmatic-competitive-landscape

# PowerShell (Windows)
.\scripts\fetch.ps1 skill pragmatic-framework/pragmatic-competitive-landscape
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
