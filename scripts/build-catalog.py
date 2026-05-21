"""build-catalog.py — Catalog generator for the agent-resource-catalog repo.

Walks the plugins/ and standalone/ directories, reads every manifest, and
writes a single catalog.json at the repo root.  Also rewrites
.claude-plugin/marketplace.json with a lightweight plugin summary.

Usage (run from the repo root):
    python scripts/build-catalog.py
    python scripts/build-catalog.py --ref v1.0.0
    python scripts/build-catalog.py --ref main --repo MyOrg/my-fork --output my-catalog.json

Arguments:
    --ref      Git ref (branch/tag/SHA) used in raw_url_prefix.  Default: "main".
    --repo     Repository slug (owner/name).  Default: auto-detected from
               "git remote get-url origin".
    --output   Output path for catalog.json.  Default: "catalog.json" (repo root).

Exit code:
    0  — success
    1  — any error
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# ---------------------------------------------------------------------------
# Resolve the repo root from the script's own location.
# ---------------------------------------------------------------------------
REPO_ROOT: Path = Path(__file__).resolve().parent.parent

MARKETPLACE_JSON: Path = REPO_ROOT / ".claude-plugin" / "marketplace.json"


# ---------------------------------------------------------------------------
# Git remote helper
# ---------------------------------------------------------------------------

def _detect_repo_slug() -> str:
    """
    Ask git for the 'origin' remote URL and extract the owner/name slug.

    Handles the two common URL forms:
      https://github.com/owner/repo.git
      git@github.com:owner/repo.git

    Returns a best-effort slug or falls back to "unknown/unknown" if git
    is unavailable or the remote is not set.
    """
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode != 0:
            return "unknown/unknown"
        url = result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return "unknown/unknown"

    # Strip trailing .git
    if url.endswith(".git"):
        url = url[:-4]

    # HTTPS form: https://github.com/owner/repo
    if url.startswith("https://") or url.startswith("http://"):
        parts = url.rstrip("/").split("/")
        if len(parts) >= 2:
            return "/".join(parts[-2:])

    # SSH form: git@github.com:owner/repo
    if ":" in url:
        after_colon = url.split(":", 1)[1]
        return after_colon.strip("/")

    return "unknown/unknown"


# ---------------------------------------------------------------------------
# Plugin discovery helpers
# ---------------------------------------------------------------------------

def _list_md_stems(directory: Path) -> list[str]:
    """Return sorted list of stem names for .md files directly in *directory*.

    Only looks one level deep (no glob recursion) — skills/commands are
    expected to be flat lists of .md files in the named subdirectory.
    """
    if not directory.is_dir():
        return []
    return sorted(p.stem for p in directory.iterdir() if p.suffix == ".md" and p.is_file())


def _connectors_from_mcp(plugin_dir: Path) -> list[str]:
    """
    Parse .mcp.json → mcpServers and return the sorted list of top-level keys.

    Returns an empty list if .mcp.json does not exist or is not valid JSON.
    The build script is lenient here — validate.py is responsible for
    surfacing malformed .mcp.json as an error.
    """
    mcp_path = plugin_dir / ".mcp.json"
    if not mcp_path.exists():
        return []
    try:
        data = json.loads(mcp_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return []

    mcp_servers = data.get("mcpServers", {}) if isinstance(data, dict) else {}
    if not isinstance(mcp_servers, dict):
        return []
    return sorted(mcp_servers.keys())


def _build_plugin_entry(plugin_dir: Path, repo: str, ref: str) -> dict | None:
    """
    Read plugins/<name>/.claude-plugin/plugin.json and build the catalog entry.

    Returns None (with a printed error) if the manifest cannot be read.
    """
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    if not manifest_path.exists():
        print(f"[ERROR] Missing plugin manifest: {manifest_path}", file=sys.stderr)
        return None

    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"[ERROR] Cannot read {manifest_path}: {exc}", file=sys.stderr)
        return None

    # Relative POSIX path for cross-platform compatibility in the catalog.
    # catalog consumers (CI, browsers) always expect forward slashes.
    rel_path = plugin_dir.relative_to(REPO_ROOT).as_posix()

    raw_url_prefix = f"https://raw.githubusercontent.com/{repo}/{ref}/{rel_path}"

    return {
        "name": data.get("name", plugin_dir.name),
        "path": rel_path,
        "version": data.get("version", "0.0.0"),
        "description": data.get("description", ""),
        "skills": _list_md_stems(plugin_dir / "skills"),
        "commands": _list_md_stems(plugin_dir / "commands"),
        "connectors": _connectors_from_mcp(plugin_dir),
        "raw_url_prefix": raw_url_prefix,
    }


# ---------------------------------------------------------------------------
# Standalone resource discovery helpers
# ---------------------------------------------------------------------------

def _build_standalone_entry(manifest_path: Path, repo: str, ref: str) -> dict | None:
    """
    Read standalone/<type>/<name>/manifest.json and build the catalog entry.

    Returns None (with a printed error) if the manifest cannot be read.
    """
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"[ERROR] Cannot read {manifest_path}: {exc}", file=sys.stderr)
        return None

    resource_dir = manifest_path.parent
    rel_path = resource_dir.relative_to(REPO_ROOT).as_posix()
    raw_url_prefix = f"https://raw.githubusercontent.com/{repo}/{ref}/{rel_path}"

    return {
        "name": data.get("name", resource_dir.name),
        "type": data.get("type", "tool"),
        "path": rel_path,
        "version": data.get("version", "0.0.0"),
        "description": data.get("description", ""),
        "tags": data.get("tags", []),
        "entry_point": data.get("entry_point", ""),
        "raw_url_prefix": raw_url_prefix,
    }


# ---------------------------------------------------------------------------
# Marketplace.json writer
# ---------------------------------------------------------------------------

def _write_marketplace(plugins: list[dict], generated_at: str) -> None:
    """
    Overwrite .claude-plugin/marketplace.json with a lightweight plugin index.

    Preserves all existing top-level fields that are NOT 'plugins' or
    'generated_at', so metadata like 'name', 'version', 'description' in
    the existing file is kept intact.
    """
    existing: dict = {}
    if MARKETPLACE_JSON.exists():
        try:
            existing = json.loads(MARKETPLACE_JSON.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            existing = {}

    # Build the lightweight plugin list (name, version, description only).
    marketplace_plugins = sorted(
        [
            {
                "name": p["name"],
                "version": p["version"],
                "description": p["description"],
            }
            for p in plugins
        ],
        key=lambda x: x["name"],
    )

    # Merge: keep existing fields, update plugins + generated_at.
    existing["plugins"] = marketplace_plugins
    existing["generated_at"] = generated_at

    MARKETPLACE_JSON.write_text(
        json.dumps(existing, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate catalog.json from plugin and standalone manifests.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--ref",
        default="main",
        help="Git ref (branch/tag/SHA) for raw_url_prefix URLs (default: main).",
    )
    parser.add_argument(
        "--repo",
        default=None,
        help=(
            "Repository slug like 'owner/repo'.  "
            "Auto-detected from git remote origin when omitted."
        ),
    )
    parser.add_argument(
        "--output",
        default=None,
        help="Output path for catalog.json (default: <repo_root>/catalog.json).",
    )
    args = parser.parse_args()

    ref: str = args.ref
    repo: str = args.repo if args.repo else _detect_repo_slug()
    output_path: Path = Path(args.output) if args.output else REPO_ROOT / "catalog.json"

    # Make output_path absolute if it is relative.
    if not output_path.is_absolute():
        output_path = REPO_ROOT / output_path

    # UTC timestamp in ISO 8601 format with explicit 'Z' suffix.
    generated_at: str = (
        datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )

    plugins: list[dict] = []
    standalone: list[dict] = []

    # -----------------------------------------------------------------------
    # Discover plugins/
    # -----------------------------------------------------------------------
    plugins_dir = REPO_ROOT / "plugins"
    if plugins_dir.is_dir():
        for plugin_dir in sorted(plugins_dir.iterdir()):
            if not plugin_dir.is_dir():
                continue
            # Only process directories that contain a .claude-plugin/plugin.json.
            if not (plugin_dir / ".claude-plugin" / "plugin.json").exists():
                continue
            entry = _build_plugin_entry(plugin_dir, repo, ref)
            if entry is not None:
                plugins.append(entry)

    # Sort plugins alphabetically by name for deterministic output.
    plugins.sort(key=lambda p: p["name"])

    # -----------------------------------------------------------------------
    # Discover standalone/
    # -----------------------------------------------------------------------
    standalone_dir = REPO_ROOT / "standalone"
    if standalone_dir.is_dir():
        # Walk two levels deep: standalone/<type>/<resource>/manifest.json
        for type_dir in sorted(standalone_dir.iterdir()):
            if not type_dir.is_dir():
                continue
            for resource_dir in sorted(type_dir.iterdir()):
                if not resource_dir.is_dir():
                    continue
                manifest_path = resource_dir / "manifest.json"
                if not manifest_path.exists():
                    continue
                entry = _build_standalone_entry(manifest_path, repo, ref)
                if entry is not None:
                    standalone.append(entry)

    # Sort standalone entries alphabetically by name.
    standalone.sort(key=lambda s: s["name"])

    # -----------------------------------------------------------------------
    # Build the catalog document.
    # -----------------------------------------------------------------------
    catalog = {
        "version": "1",
        "generated_at": generated_at,
        "repo_url": f"https://github.com/{repo}",
        "plugins": plugins,
        "standalone": standalone,
    }

    # -----------------------------------------------------------------------
    # Write catalog.json
    # -----------------------------------------------------------------------
    try:
        output_path.write_text(
            json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except OSError as exc:
        print(f"[ERROR] Cannot write {output_path}: {exc}", file=sys.stderr)
        sys.exit(1)

    # -----------------------------------------------------------------------
    # Update .claude-plugin/marketplace.json
    # -----------------------------------------------------------------------
    try:
        _write_marketplace(plugins, generated_at)
    except OSError as exc:
        print(f"[ERROR] Cannot write {MARKETPLACE_JSON}: {exc}", file=sys.stderr)
        sys.exit(1)

    n_plugins = len(plugins)
    n_standalone = len(standalone)
    print(
        f"[BUILT] {output_path.relative_to(REPO_ROOT)} "
        f"— {n_plugins} plugin{'s' if n_plugins != 1 else ''}, "
        f"{n_standalone} standalone resource{'s' if n_standalone != 1 else ''}"
    )


if __name__ == "__main__":
    main()
