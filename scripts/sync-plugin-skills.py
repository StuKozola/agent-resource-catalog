"""sync-plugin-skills.py — Refresh plugin skill copies from the skills/ library.

Plugins ship each skill as one flat file (plugins/<plugin>/skills/<skill>.md),
so they can't carry a skill's references/ and templates/ folders. This script:

  1. Finds every plugins/*/skills/<name>.md whose <name> matches a skill folder
     skills/<framework>/<name>/SKILL.md.
  2. Overwrites the plugin copy with that SKILL.md.
  3. Rewrites relative links to supporting files (references/x.md,
     templates/x.md, ../<other-skill>/references/x.md, <other-skill>/templates/x.md)
     into raw GitHub URLs so the agent can still fetch them from inside a plugin.

Plugin membership is whatever .md files exist under plugins/<plugin>/skills/.
To add a skill to a plugin, create an empty placeholder file with the skill
name and run this script.

Usage (from the repo root):
    python scripts/sync-plugin-skills.py            # write changes
    python scripts/sync-plugin-skills.py --check    # exit 1 if any copy is stale
    python scripts/sync-plugin-skills.py --ref v2.0.0
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_BASE = "https://raw.githubusercontent.com/StuKozola/agent-resource-catalog"

# `references/x.md`, `../skill/templates/x.md`, (skill/references/x.md) etc.
LINK_RE = re.compile(
    r"(?P<open>[`(])"
    r"(?:\./|\.\./)?"
    r"(?:(?P<skill>[a-z0-9][a-z0-9-]*)/)?"
    r"(?P<path>(?:references|templates)/[A-Za-z0-9._-]+\.md)"
    r"(?P<close>[`)])"
)


def skill_index() -> dict[str, Path]:
    """Map skill folder name -> SKILL.md path across all frameworks."""
    index: dict[str, Path] = {}
    for skill_md in (REPO_ROOT / "skills").glob("*/*/SKILL.md"):
        index[skill_md.parent.name] = skill_md
    return index


def render(skill_md: Path, index: dict[str, Path], ref: str) -> str:
    text = skill_md.read_text(encoding="utf-8")
    framework = skill_md.parent.parent.name

    def repl(m: re.Match) -> str:
        target = m.group("skill") or skill_md.parent.name
        if target not in index:
            return m.group(0)
        fw = index[target].parent.parent.name if m.group("skill") else framework
        url = f"{RAW_BASE}/{ref}/skills/{fw}/{target}/{m.group('path')}"
        return f"{m.group('open')}{url}{m.group('close')}"

    return LINK_RE.sub(repl, text)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="report stale copies, don't write")
    parser.add_argument("--ref", default="main", help="git ref used in raw URLs (default: main)")
    args = parser.parse_args()

    index = skill_index()
    stale, unknown = [], []
    for copy in sorted((REPO_ROOT / "plugins").glob("*/skills/*.md")):
        source = index.get(copy.stem)
        if source is None:
            unknown.append(copy)
            continue
        wanted = render(source, index, args.ref)
        current = copy.read_text(encoding="utf-8") if copy.exists() else ""
        if current != wanted:
            stale.append(copy)
            if not args.check:
                copy.write_text(wanted, encoding="utf-8", newline="\n")

    for p in unknown:
        print(f"[SKIP] {p.relative_to(REPO_ROOT)} — no matching skill in skills/ (plugin-only skill)")
    verb = "stale" if args.check else "updated"
    for p in stale:
        print(f"[{verb.upper()}] {p.relative_to(REPO_ROOT)}")
    print(f"{len(stale)} {verb}, {len(unknown)} skipped")
    return 1 if (args.check and stale) else 0


if __name__ == "__main__":
    sys.exit(main())
