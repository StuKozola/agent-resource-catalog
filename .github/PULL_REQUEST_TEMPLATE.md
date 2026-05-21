## Summary

<!-- What does this PR add or change? Use 1-3 bullets. -->

-

## Type

<!-- Check all that apply. -->

- [ ] New plugin
- [ ] New skill(s)
- [ ] New standalone resource
- [ ] Bug fix
- [ ] Documentation
- [ ] CI / tooling

## Checklist

<!-- Complete all items before requesting review. -->

- [ ] `python scripts/validate.py` passes locally with no errors
- [ ] Skill files have required YAML frontmatter (`name`, `description`)
- [ ] Command files include Inputs, Steps, and Output sections (if applicable)
- [ ] Shared skill copies are in sync across all plugins that include them
- [ ] New plugins have at least one skill file under `skills/`
- [ ] `.mcp.json` uses MCP registry IDs, not hardcoded connection strings
- [ ] `catalog.json` will be rebuilt by CI (do not manually edit it)

## Notes

<!-- Optional: reviewer context, tradeoffs, or anything that needs discussion. -->
