"""validate.py — Manifest validator for the agent-resource-catalog repo.

Validates every plugin manifest, standalone manifest, and the root catalog.json
against their corresponding JSON schemas.  Also performs a set of structural
checks on each plugin (directory-name alignment, referenced-file existence,
.mcp.json validity, YAML frontmatter in skill .md files) and a cross-plugin
SHA-256 drift check that warns when two plugins ship identically-named skill
files with divergent content.

Usage (run from the repo root):
    python scripts/validate.py

Exit code:
    0  — no FAILs (warnings are acceptable)
    1  — at least one FAIL was emitted
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

# ---------------------------------------------------------------------------
# jsonschema is the only third-party dependency.
# ---------------------------------------------------------------------------
try:
    import jsonschema
except ImportError:
    print("[FAIL] Missing dependency: install jsonschema  (pip install jsonschema)")
    sys.exit(1)

# ---------------------------------------------------------------------------
# Resolve the repo root.  The script may be invoked from any working
# directory, but it lives at <repo>/scripts/validate.py, so the repo root is
# always two levels up from __file__.
# ---------------------------------------------------------------------------
REPO_ROOT: Path = Path(__file__).resolve().parent.parent

SCHEMA_DIR: Path = REPO_ROOT / "schema"
PLUGIN_SCHEMA_PATH: Path = SCHEMA_DIR / "plugin.schema.json"
STANDALONE_SCHEMA_PATH: Path = SCHEMA_DIR / "standalone.schema.json"
CATALOG_SCHEMA_PATH: Path = SCHEMA_DIR / "catalog.schema.json"

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------
_fail_count: int = 0


def _pass(label: str) -> None:
    print(f"[PASS] {label}")


def _fail(label: str, message: str) -> None:
    global _fail_count
    _fail_count += 1
    print(f"[FAIL] {label}: {message}")


def _warn(message: str) -> None:
    print(f"[WARN] {message}")


# ---------------------------------------------------------------------------
# JSON schema loading helpers
# ---------------------------------------------------------------------------

def _load_json(path: Path) -> dict | list | None:
    """Load a JSON file; emit [FAIL] and return None on any error."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        _fail(str(path), f"invalid JSON — {exc}")
        return None
    except OSError as exc:
        _fail(str(path), f"cannot read file — {exc}")
        return None


def _load_schema(path: Path) -> dict | None:
    """Load a JSON Schema file; emit [FAIL] and return None on any error."""
    data = _load_json(path)
    if data is None:
        return None
    if not isinstance(data, dict):
        _fail(str(path), "schema file must be a JSON object")
        return None
    return data


# ---------------------------------------------------------------------------
# JSON Schema validation helper
# ---------------------------------------------------------------------------

def _validate_against_schema(data: dict, schema: dict, label: str) -> bool:
    """Validate *data* against *schema*.  Emit pass/fail and return bool."""
    try:
        # Use Draft7Validator to match the $schema declaration in our files.
        validator = jsonschema.Draft7Validator(schema)
        errors = sorted(validator.iter_errors(data), key=lambda e: list(e.path))
        if errors:
            for err in errors:
                path_str = " > ".join(str(p) for p in err.path) if err.path else "(root)"
                _fail(label, f"{path_str}: {err.message}")
            return False
        _pass(label)
        return True
    except jsonschema.SchemaError as exc:
        _fail(label, f"schema itself is invalid — {exc.message}")
        return False


# ---------------------------------------------------------------------------
# YAML frontmatter parser (regex-based, no third-party YAML library)
# ---------------------------------------------------------------------------
# We only need to extract the values of the 'name' and 'description' keys
# from simple scalar assignments.  The pattern below handles:
#   key: value
# It does NOT handle block scalars, anchors, or other YAML features, but the
# skill .md convention only uses simple single-line values for these two keys.

_FRONTMATTER_BLOCK_RE = re.compile(
    r"^\s*---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n",
    re.DOTALL,
)
_FRONTMATTER_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.+)$", re.MULTILINE)


def _parse_frontmatter_keys(text: str) -> set[str]:
    """Return the set of top-level key names found in the first YAML frontmatter block."""
    match = _FRONTMATTER_BLOCK_RE.match(text)
    if not match:
        return set()
    block = match.group(1)
    return {m.group(1) for m in _FRONTMATTER_KEY_RE.finditer(block)}


# ---------------------------------------------------------------------------
# SHA-256 helper
# ---------------------------------------------------------------------------

def _sha256(path: Path) -> str:
    """Return the hex SHA-256 digest of the file at *path*."""
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Plugin validation
# ---------------------------------------------------------------------------

def _validate_plugin(plugin_dir: Path, plugin_schema: dict) -> None:
    """Run all checks for a single plugin directory."""
    manifest_path = plugin_dir / ".claude-plugin" / "plugin.json"
    label = str(manifest_path.relative_to(REPO_ROOT))

    # 1. Manifest must exist and be valid JSON.
    data = _load_json(manifest_path)
    if data is None:
        return  # already failed

    # 2. Validate against the JSON schema.
    if not isinstance(data, dict):
        _fail(label, "plugin.json must be a JSON object")
        return

    _validate_against_schema(data, plugin_schema, label)

    # 3. Plugin 'name' field must match the parent directory name.
    plugin_name = data.get("name")
    dir_name = plugin_dir.name
    if plugin_name != dir_name:
        _fail(
            label,
            f"'name' field '{plugin_name}' does not match directory name '{dir_name}'",
        )
    else:
        _pass(f"{label} [name == directory]")

    # 4. Every file listed in skills/ and commands/ must exist on disk.
    for section in ("skills", "commands"):
        file_list = data.get(section)
        if not file_list:
            continue  # field absent or empty — not an error at this layer
        if not isinstance(file_list, list):
            _fail(label, f"'{section}' field must be a list")
            continue
        for entry in file_list:
            target = plugin_dir / entry
            if target.exists():
                _pass(f"{label} [{section}/{entry} exists]")
            else:
                _fail(label, f"referenced file '{entry}' in '{section}' not found at {target}")

    # 5. If .mcp.json exists it must be valid JSON.
    mcp_path = plugin_dir / ".mcp.json"
    if mcp_path.exists():
        mcp_data = _load_json(mcp_path)
        if mcp_data is not None:
            _pass(str(mcp_path.relative_to(REPO_ROOT)) + " [valid JSON]")

    # 6. Every .md file in skills/ must have YAML frontmatter with name + description.
    skills_dir = plugin_dir / "skills"
    if skills_dir.is_dir():
        for md_file in sorted(skills_dir.glob("**/*.md")):
            md_label = str(md_file.relative_to(REPO_ROOT))
            text = md_file.read_text(encoding="utf-8")
            keys = _parse_frontmatter_keys(text)
            missing = {"name", "description"} - keys
            if missing:
                _fail(md_label, f"YAML frontmatter missing required key(s): {sorted(missing)}")
            else:
                _pass(f"{md_label} [frontmatter ok]")


# ---------------------------------------------------------------------------
# Standalone resource validation
# ---------------------------------------------------------------------------

def _validate_standalone(manifest_path: Path, standalone_schema: dict) -> None:
    """Run all checks for a single standalone manifest.json."""
    label = str(manifest_path.relative_to(REPO_ROOT))

    data = _load_json(manifest_path)
    if data is None:
        return

    if not isinstance(data, dict):
        _fail(label, "manifest.json must be a JSON object")
        return

    _validate_against_schema(data, standalone_schema, label)


# ---------------------------------------------------------------------------
# Drift detection across plugins
# ---------------------------------------------------------------------------

def _check_skill_drift(plugins_dir: Path) -> None:
    """
    For every skill filename stem that appears in more than one plugin's
    skills/ directory, compare SHA-256 hashes.  If they differ, emit [WARN].

    We do NOT fail on drift — it may be intentional — but we surface it so
    maintainers can decide whether to deduplicate or diverge deliberately.
    """
    # stem -> list of (plugin_name, path, sha256)
    skill_map: dict[str, list[tuple[str, Path, str]]] = defaultdict(list)

    if not plugins_dir.is_dir():
        return

    for plugin_dir in sorted(plugins_dir.iterdir()):
        if not plugin_dir.is_dir():
            continue
        skills_dir = plugin_dir / "skills"
        if not skills_dir.is_dir():
            continue
        for md_file in sorted(skills_dir.glob("**/*.md")):
            stem = md_file.stem
            try:
                digest = _sha256(md_file)
            except OSError:
                continue
            skill_map[stem].append((plugin_dir.name, md_file, digest))

    for stem, occurrences in sorted(skill_map.items()):
        if len(occurrences) < 2:
            continue
        # Collect unique digests.
        unique_digests = {digest for _, _, digest in occurrences}
        if len(unique_digests) > 1:
            # Build a human-readable diff-friendly summary.
            lines = [
                f"skill file '{stem}.md' has diverged copies across plugins:",
            ]
            for plugin_name, path, digest in occurrences:
                lines.append(f"  {plugin_name}: {digest[:12]}…  ({path})")
            _warn("\n".join(lines))


# ---------------------------------------------------------------------------
# Root catalog.json validation
# ---------------------------------------------------------------------------

def _validate_catalog(catalog_schema: dict) -> None:
    """Validate the root catalog.json against its schema."""
    catalog_path = REPO_ROOT / "catalog.json"
    if not catalog_path.exists():
        _fail("catalog.json", "file not found")
        return

    data = _load_json(catalog_path)
    if data is None:
        return

    if not isinstance(data, dict):
        _fail("catalog.json", "must be a JSON object")
        return

    _validate_against_schema(data, catalog_schema, "catalog.json")


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Discover and validate all manifests in the repo."""
    # -----------------------------------------------------------------------
    # Load schemas up-front so we can fail fast if any are missing/invalid.
    # -----------------------------------------------------------------------
    plugin_schema = _load_schema(PLUGIN_SCHEMA_PATH)
    if plugin_schema is None:
        print("[FAIL] Cannot load plugin schema — aborting")
        sys.exit(1)

    standalone_schema = _load_schema(STANDALONE_SCHEMA_PATH)
    if standalone_schema is None:
        print("[FAIL] Cannot load standalone schema — aborting")
        sys.exit(1)

    catalog_schema = _load_schema(CATALOG_SCHEMA_PATH)
    if catalog_schema is None:
        print("[FAIL] Cannot load catalog schema — aborting")
        sys.exit(1)

    _pass("schema/plugin.schema.json [loaded]")
    _pass("schema/standalone.schema.json [loaded]")
    _pass("schema/catalog.schema.json [loaded]")

    # -----------------------------------------------------------------------
    # 1. Validate every plugins/*/.claude-plugin/plugin.json
    # -----------------------------------------------------------------------
    plugins_dir = REPO_ROOT / "plugins"
    if plugins_dir.is_dir():
        for plugin_dir in sorted(plugins_dir.iterdir()):
            if plugin_dir.is_dir():
                _validate_plugin(plugin_dir, plugin_schema)
    else:
        # Not an error — repo may not have any plugins yet.
        print("[INFO] No plugins/ directory found — skipping plugin validation")

    # -----------------------------------------------------------------------
    # 2. Validate every standalone/*/*/manifest.json
    # -----------------------------------------------------------------------
    standalone_dir = REPO_ROOT / "standalone"
    if standalone_dir.is_dir():
        # The spec says standalone/*/*/manifest.json — two levels of subdirs.
        for type_dir in sorted(standalone_dir.iterdir()):
            if not type_dir.is_dir():
                continue
            for resource_dir in sorted(type_dir.iterdir()):
                if not resource_dir.is_dir():
                    continue
                manifest_path = resource_dir / "manifest.json"
                if manifest_path.exists():
                    _validate_standalone(manifest_path, standalone_schema)
                else:
                    _fail(
                        str(resource_dir.relative_to(REPO_ROOT)),
                        "missing manifest.json",
                    )
    else:
        print("[INFO] No standalone/ directory found — skipping standalone validation")

    # -----------------------------------------------------------------------
    # 3. Validate the root catalog.json
    # -----------------------------------------------------------------------
    _validate_catalog(catalog_schema)

    # -----------------------------------------------------------------------
    # 4. Cross-plugin skill drift check (warnings only)
    # -----------------------------------------------------------------------
    _check_skill_drift(plugins_dir if plugins_dir.is_dir() else REPO_ROOT / "plugins")

    # -----------------------------------------------------------------------
    # Summary and exit code
    # -----------------------------------------------------------------------
    if _fail_count == 0:
        print(f"\nAll checks passed (0 failures).")
    else:
        print(f"\n{_fail_count} failure(s) found.")
        sys.exit(1)


if __name__ == "__main__":
    main()
