#!/usr/bin/env bash
# =============================================================================
# fetch.sh — Fetch skills, plugins, or standalone resources from the
#            StuKozola/agent-resource-catalog catalog without cloning the
#            entire repository.
#
# Usage:
#   ./scripts/fetch.sh skill  <framework>/<skill-name>
#   ./scripts/fetch.sh plugin <plugin-name>
#   ./scripts/fetch.sh standalone <resource-name>
#   ./scripts/fetch.sh help
#
# Environment variable overrides:
#   CATALOG_REPO   GitHub owner/repo  (default: StuKozola/agent-resource-catalog)
#   CATALOG_REF    Branch or tag      (default: main)
#
# Examples:
#   ./scripts/fetch.sh skill pragmatic-framework/competitive-landscape
#   ./scripts/fetch.sh plugin product-manager
#   ./scripts/fetch.sh standalone pdf-extractor
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration — override via environment variables
# ---------------------------------------------------------------------------
CATALOG_REPO="${CATALOG_REPO:-StuKozola/agent-resource-catalog}"
CATALOG_REF="${CATALOG_REF:-main}"
RAW_BASE="https://raw.githubusercontent.com/${CATALOG_REPO}/${CATALOG_REF}"
REPO_URL="https://github.com/${CATALOG_REPO}.git"

# ---------------------------------------------------------------------------
# Colour helpers (suppressed when stdout is not a terminal)
# ---------------------------------------------------------------------------
if [ -t 1 ]; then
    BOLD="\033[1m"
    GREEN="\033[0;32m"
    CYAN="\033[0;36m"
    YELLOW="\033[1;33m"
    RED="\033[0;31m"
    RESET="\033[0m"
else
    BOLD="" GREEN="" CYAN="" YELLOW="" RED="" RESET=""
fi

info()    { printf "${CYAN}[fetch]${RESET} %s\n"  "$*"; }
success() { printf "${GREEN}[ok]${RESET}   %s\n"  "$*"; }
warn()    { printf "${YELLOW}[warn]${RESET} %s\n" "$*"; }
error()   { printf "${RED}[error]${RESET} %s\n"   "$*" >&2; }
die()     { error "$*"; exit 1; }

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------
check_deps() {
    local missing=()
    command -v curl &>/dev/null || missing+=("curl")
    command -v git  &>/dev/null || missing+=("git")
    if [ ${#missing[@]} -gt 0 ]; then
        die "Required tools not found: ${missing[*]}. Please install them and retry."
    fi
}

# ---------------------------------------------------------------------------
# Print help
# ---------------------------------------------------------------------------
print_help() {
    cat <<EOF
${BOLD}fetch.sh${RESET} — Download resources from the agent-resource-catalog

${BOLD}USAGE${RESET}
  ./scripts/fetch.sh <command> [arguments]

${BOLD}COMMANDS${RESET}
  skill  <framework>/<skill-name>   Fetch a single SKILL.md file
  plugin <plugin-name>              Fetch an entire plugin directory
  standalone <resource-name>        Fetch an entire standalone resource directory
  help                              Show this message

${BOLD}EXAMPLES${RESET}
  ./scripts/fetch.sh skill pragmatic-framework/competitive-landscape
  ./scripts/fetch.sh plugin product-manager
  ./scripts/fetch.sh standalone pdf-extractor

${BOLD}ENV VARS${RESET}
  CATALOG_REPO   GitHub owner/repo  (default: StuKozola/agent-resource-catalog)
  CATALOG_REF    Branch or tag      (default: main)
EOF
}

# ---------------------------------------------------------------------------
# Fetch a single file from the raw GitHub URL into the current directory,
# preserving the relative path structure.
#
# Arguments:
#   $1  path relative to repo root  (e.g. "skills/pragmatic-framework/competitive-landscape/SKILL.md")
#   $2  optional local destination  (default: basename of $1)
# ---------------------------------------------------------------------------
fetch_file() {
    local remote_path="$1"
    local dest="${2:-$(basename "$remote_path")}"
    local url="${RAW_BASE}/${remote_path}"

    info "Fetching ${url}"
    local dest_dir
    dest_dir="$(dirname "$dest")"
    if [ "$dest_dir" != "." ] && [ "$dest_dir" != "" ]; then
        mkdir -p "$dest_dir"
    fi

    if curl -sL --fail --output "$dest" "$url"; then
        success "Saved → ${dest}"
    else
        die "Failed to download '${url}'. Check that the path exists on ref '${CATALOG_REF}'."
    fi
}

# ---------------------------------------------------------------------------
# Fetch a directory from the repo using a blobless sparse checkout so we
# only download the files we actually need (no full clone).
#
# Arguments:
#   $1  repo-relative directory path  (e.g. "plugins/product-manager")
#   $2  local destination directory   (default: basename of $1)
# ---------------------------------------------------------------------------
fetch_directory() {
    local remote_dir="$1"
    local dest="${2:-$(basename "$remote_dir")}"

    info "Sparse-cloning directory '${remote_dir}' from ${REPO_URL} (ref: ${CATALOG_REF})"

    # Use a temp directory so a partial failure doesn't leave a broken dest
    local tmp_dir
    tmp_dir="$(mktemp -d)"
    # Ensure temp dir is cleaned up on exit
    trap 'rm -rf "${tmp_dir}"' EXIT

    info "Running: git clone --no-checkout --filter=blob:none --branch ${CATALOG_REF} ${REPO_URL} ${tmp_dir}"
    if ! git clone \
            --no-checkout \
            --filter=blob:none \
            --branch "${CATALOG_REF}" \
            "${REPO_URL}" \
            "${tmp_dir}" \
            --quiet; then
        die "git clone failed. Verify that CATALOG_REPO='${CATALOG_REPO}' and CATALOG_REF='${CATALOG_REF}' are correct."
    fi

    info "Configuring sparse-checkout for path: ${remote_dir}"
    git -C "${tmp_dir}" sparse-checkout init --cone
    git -C "${tmp_dir}" sparse-checkout set "${remote_dir}"

    info "Checking out files..."
    if ! git -C "${tmp_dir}" checkout "${CATALOG_REF}" --quiet; then
        die "git checkout failed."
    fi

    local src="${tmp_dir}/${remote_dir}"
    if [ ! -d "${src}" ]; then
        die "Directory '${remote_dir}' not found in the repository at ref '${CATALOG_REF}'."
    fi

    # Move to final destination
    mkdir -p "$(dirname "$dest")"
    cp -r "${src}" "${dest}"
    success "Saved → ${dest}/"

    # Clean up temp dir immediately (trap will also fire but this is explicit)
    rm -rf "${tmp_dir}"
    trap - EXIT
}

# ---------------------------------------------------------------------------
# Command: skill
# ---------------------------------------------------------------------------
cmd_skill() {
    if [ -z "${1:-}" ]; then
        die "Usage: fetch.sh skill <framework>/<skill-name>\n  Example: fetch.sh skill pragmatic-framework/competitive-landscape"
    fi

    local skill_path="$1"
    # Normalise: strip a leading "skills/" if the user included it
    skill_path="${skill_path#skills/}"

    local remote_path="skills/${skill_path}/SKILL.md"
    local local_dest="${skill_path}/SKILL.md"

    fetch_file "${remote_path}" "${local_dest}"
}

# ---------------------------------------------------------------------------
# Command: plugin
# ---------------------------------------------------------------------------
cmd_plugin() {
    if [ -z "${1:-}" ]; then
        die "Usage: fetch.sh plugin <plugin-name>\n  Example: fetch.sh plugin product-manager"
    fi

    local plugin_name="$1"
    # Normalise: strip a leading "plugins/" if the user included it
    plugin_name="${plugin_name#plugins/}"

    fetch_directory "plugins/${plugin_name}" "${plugin_name}"
}

# ---------------------------------------------------------------------------
# Command: standalone
# ---------------------------------------------------------------------------
cmd_standalone() {
    if [ -z "${1:-}" ]; then
        die "Usage: fetch.sh standalone <resource-name>\n  Example: fetch.sh standalone pdf-extractor"
    fi

    local resource_name="$1"
    # Normalise: strip a leading "standalone/" if the user included it
    resource_name="${resource_name#standalone/}"

    fetch_directory "standalone/${resource_name}" "${resource_name}"
}

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
main() {
    check_deps

    local command="${1:-help}"
    shift || true   # consume first arg; "shift || true" avoids set -e failure on no args

    case "${command}" in
        skill)      cmd_skill      "${@}" ;;
        plugin)     cmd_plugin     "${@}" ;;
        standalone) cmd_standalone "${@}" ;;
        help|--help|-h) print_help ;;
        *)
            error "Unknown command: '${command}'"
            print_help
            exit 1
            ;;
    esac
}

main "$@"
