"""sync-plugin-skills.py — Refresh plugin skill copies from the skills/ library.

Each plugin skill is a folder, plugins/<plugin>/skills/<skill>/, laid out the
way Claude Code loads it: a SKILL.md plus any supporting files (references/,
templates/ ...). For every plugin skill folder whose <skill> matches a library
skill skills/<framework>/<skill>/, this script:

  1. Copies the library skill folder (SKILL.md and every supporting file) into
     the plugin, and deletes plugin files the library no longer has.
  2. Rewrites relative links to references/ and templates/ files in the copied
     Markdown so they still resolve inside the plugin:
       - a link to the skill's own files, or to a skill the plugin also
         ships, becomes a relative path within the plugin;
       - a link to a library skill the plugin does not ship becomes a raw
         GitHub URL, so the agent can still fetch it.

Plugin membership is whatever skill folders exist under plugins/<plugin>/skills/.
To add a skill to a plugin, create an empty placeholder
plugins/<plugin>/skills/<skill>/SKILL.md and run this script.

Usage (from the repo root):
    python scripts/sync-plugin-skills.py            # write changes
    python scripts/sync-plugin-skills.py --check    # exit 1 if any copy is stale
    python scripts/sync-plugin-skills.py --ref v2.0.0
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LIBRARY = REPO_ROOT / "skills"
RAW_BASE = "https://raw.githubusercontent.com/StuKozola/agent-resource-catalog"

# A link inside backticks or parentheses to a references/ or templates/ file:
#   `references/x.md`  (../other-skill/templates/x.md)  `../../s/references/x.md`
#   (other-skill/references/x.md)
LINK_RE = re.compile(
    r"(?P<open>[`(])"
    r"(?P<link>(?:\./|(?:\.\./)+)?(?:[a-z0-9][a-z0-9-]*/)?"
    r"(?:references|templates)/[A-Za-z0-9._-]+\.md)"
    r"(?P<close>[`)#])"
)
IGNORED = {".DS_Store"}


def skill_index() -> dict[str, Path]:
    """Map skill folder name -> library skill directory across all frameworks."""
    return {p.parent.name: p.parent for p in LIBRARY.glob("*/*/SKILL.md")}


def resolve(link: str, src_file: Path, index: dict[str, Path]) -> Path | None:
    """Find the library file a relative link in *src_file* points to."""
    candidate = (src_file.parent / link).resolve()
    if candidate.is_file() and LIBRARY in candidate.parents:
        return candidate
    # `other-skill/references/x.md`, naming a skill rather than a path.
    head, _, rest = re.sub(r"^(?:\./|(?:\.\./)+)", "", link).partition("/")
    if head in index and (index[head] / rest).is_file():
        return index[head] / rest
    return None


def render(src_file: Path, dst_file: Path, plugin_skills: Path,
           index: dict[str, Path], ref: str) -> str:
    """Return *src_file*'s text with links rewritten for its plugin copy at *dst_file*."""
    text = src_file.read_text(encoding="utf-8")

    def repl(m: re.Match) -> str:
        target = resolve(m.group("link"), src_file, index)
        if target is None:
            return m.group(0)
        rel = target.relative_to(LIBRARY)          # <framework>/<skill>/<path...>
        skill = rel.parts[1]
        if (plugin_skills / skill).is_dir():
            in_plugin = plugin_skills / skill / Path(*rel.parts[2:])
            new = Path(os.path.relpath(in_plugin, dst_file.parent)).as_posix()
        else:
            new = f"{RAW_BASE}/{ref}/skills/{rel.as_posix()}"
        return f"{m.group('open')}{new}{m.group('close')}"

    return LINK_RE.sub(repl, text)


def wanted_files(plugin_skill: Path, source: Path, index: dict[str, Path],
                 ref: str) -> dict[Path, bytes]:
    """Plugin path -> expected bytes for every file in the library skill."""
    out: dict[Path, bytes] = {}
    for src in sorted(p for p in source.rglob("*") if p.is_file() and p.name not in IGNORED):
        dst = plugin_skill / src.relative_to(source)
        if src.suffix == ".md":
            out[dst] = render(src, dst, plugin_skill.parent, index, ref).encode("utf-8")
        else:
            out[dst] = src.read_bytes()
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="report stale copies, don't write")
    parser.add_argument("--ref", default="main", help="git ref used in raw URLs (default: main)")
    args = parser.parse_args()

    index = skill_index()
    changed: list[str] = []
    unknown: list[Path] = []
    for skill_md in sorted((REPO_ROOT / "plugins").glob("*/skills/*/SKILL.md")):
        plugin_skill = skill_md.parent
        source = index.get(plugin_skill.name)
        if source is None:
            unknown.append(plugin_skill)
            continue

        wanted = wanted_files(plugin_skill, source, index, args.ref)
        present = {p for p in plugin_skill.rglob("*") if p.is_file() and p.name not in IGNORED}

        for dst, data in wanted.items():
            if not dst.exists() or dst.read_bytes() != data:
                changed.append(str(dst.relative_to(REPO_ROOT)))
                if not args.check:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    dst.write_bytes(data)
        for extra in sorted(present - set(wanted)):
            changed.append(f"{extra.relative_to(REPO_ROOT)} (not in library)")
            if not args.check:
                extra.unlink()
        if not args.check:
            for d in sorted((p for p in plugin_skill.rglob("*") if p.is_dir()), reverse=True):
                if not any(d.iterdir()):
                    d.rmdir()

    for p in unknown:
        print(f"[SKIP] {p.relative_to(REPO_ROOT)} — no matching skill in skills/ (plugin-only skill)")
    verb = "stale" if args.check else "updated"
    for p in changed:
        print(f"[{verb.upper()}] {p}")
    print(f"{len(changed)} {verb} file(s), {len(unknown)} skipped")
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
