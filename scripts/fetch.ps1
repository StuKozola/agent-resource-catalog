#Requires -Version 7.0
<#
.SYNOPSIS
    Fetch skills, plugins, or standalone resources from the
    StuKozola/agent-resource-catalog catalog without cloning the whole repo.

.DESCRIPTION
    Downloads individual SKILL.md files or entire plugin/standalone directories
    from the catalog using either Invoke-WebRequest (single files) or a
    blobless git sparse-checkout (directories).

.PARAMETER Command
    One of: skill, plugin, standalone, help

.PARAMETER Argument
    For "skill":      <framework>/<skill-name>  (e.g. pragmatic-framework/competitive-landscape)
    For "plugin":     <plugin-name>             (e.g. product-manager)
    For "standalone": <resource-name>           (e.g. pdf-extractor)

.EXAMPLE
    .\scripts\fetch.ps1 skill pragmatic-framework/competitive-landscape

.EXAMPLE
    .\scripts\fetch.ps1 plugin product-manager

.EXAMPLE
    .\scripts\fetch.ps1 standalone pdf-extractor

.NOTES
    Environment variable overrides:
        $env:CATALOG_REPO   GitHub owner/repo  (default: StuKozola/agent-resource-catalog)
        $env:CATALOG_REF    Branch or tag      (default: main)
#>

[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [string] $Command = 'help',

    [Parameter(Position = 1, ValueFromRemainingArguments)]
    [string[]] $Arguments = @()
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# ---------------------------------------------------------------------------
# Configuration — override via environment variables
# ---------------------------------------------------------------------------
$CatalogRepo = if ($env:CATALOG_REPO) { $env:CATALOG_REPO } else { 'StuKozola/agent-resource-catalog' }
$CatalogRef  = if ($env:CATALOG_REF)  { $env:CATALOG_REF  } else { 'main' }
$RawBase     = "https://raw.githubusercontent.com/$CatalogRepo/$CatalogRef"
$RepoUrl     = "https://github.com/$CatalogRepo.git"

# ---------------------------------------------------------------------------
# Colour helpers
# ---------------------------------------------------------------------------
function Write-Info    ([string]$Msg) { Write-Host "[fetch] $Msg" -ForegroundColor Cyan   }
function Write-Ok      ([string]$Msg) { Write-Host "[ok]   $Msg"  -ForegroundColor Green  }
function Write-Warn    ([string]$Msg) { Write-Host "[warn] $Msg"  -ForegroundColor Yellow }
function Write-Err     ([string]$Msg) { Write-Host "[error] $Msg" -ForegroundColor Red    }
function Exit-WithError([string]$Msg) { Write-Err $Msg; exit 1 }

# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------
function Assert-Dependencies {
    $missing = @()
    if (-not (Get-Command 'curl.exe' -ErrorAction SilentlyContinue) -and
        -not (Get-Command 'curl'     -ErrorAction SilentlyContinue)) {
        $missing += 'curl'
    }
    if (-not (Get-Command 'git' -ErrorAction SilentlyContinue)) {
        $missing += 'git'
    }
    if ($missing.Count -gt 0) {
        Exit-WithError "Required tools not found: $($missing -join ', '). Please install them and retry."
    }
}

# ---------------------------------------------------------------------------
# Print help
# ---------------------------------------------------------------------------
function Show-Help {
    Write-Host @"

fetch.ps1 — Download resources from the agent-resource-catalog

USAGE
  .\scripts\fetch.ps1 <command> [argument]

COMMANDS
  skill  <framework>/<skill-name>   Fetch a single SKILL.md file
  plugin <plugin-name>              Fetch an entire plugin directory
  standalone <resource-name>        Fetch an entire standalone resource directory
  help                              Show this message

EXAMPLES
  .\scripts\fetch.ps1 skill pragmatic-framework/competitive-landscape
  .\scripts\fetch.ps1 plugin product-manager
  .\scripts\fetch.ps1 standalone pdf-extractor

ENV VARS
  `$env:CATALOG_REPO   GitHub owner/repo  (default: StuKozola/agent-resource-catalog)
  `$env:CATALOG_REF    Branch or tag      (default: main)
"@
}

# ---------------------------------------------------------------------------
# Fetch a single file from the raw GitHub URL.
#
# Parameters:
#   RemotePath   Path relative to repo root
#                e.g. "skills/pragmatic-framework/competitive-landscape/SKILL.md"
#   LocalDest    Local file path to write to
#                (default: basename of RemotePath)
# ---------------------------------------------------------------------------
function Invoke-FetchFile {
    param(
        [Parameter(Mandatory)] [string] $RemotePath,
        [string] $LocalDest = ''
    )

    if (-not $LocalDest) {
        $LocalDest = Split-Path -Leaf $RemotePath
    }

    $Url = "$RawBase/$RemotePath"
    Write-Info "Fetching $Url"

    # Ensure destination directory exists
    $DestDir = Split-Path -Parent $LocalDest
    if ($DestDir -and -not (Test-Path $DestDir)) {
        New-Item -ItemType Directory -Force -Path $DestDir | Out-Null
    }

    try {
        # Prefer Invoke-WebRequest; fall back to curl.exe
        Invoke-WebRequest -Uri $Url -OutFile $LocalDest -UseBasicParsing -ErrorAction Stop
        Write-Ok "Saved -> $LocalDest"
    }
    catch {
        # Try curl.exe as fallback (ships with Windows 10+)
        Write-Warn "Invoke-WebRequest failed, trying curl.exe..."
        $CurlExit = 0
        curl.exe -sL --fail -o $LocalDest $Url
        $CurlExit = $LASTEXITCODE
        if ($CurlExit -ne 0) {
            Exit-WithError "Failed to download '$Url'. Check that the path exists on ref '$CatalogRef'."
        }
        Write-Ok "Saved -> $LocalDest"
    }
}

# ---------------------------------------------------------------------------
# Fetch a directory using a blobless git sparse-checkout.
#
# Parameters:
#   RemoteDir    Repo-relative directory path  (e.g. "plugins/product-manager")
#   LocalDest    Local directory to write to   (default: basename of RemoteDir)
# ---------------------------------------------------------------------------
function Invoke-FetchDirectory {
    param(
        [Parameter(Mandatory)] [string] $RemoteDir,
        [string] $LocalDest = ''
    )

    if (-not $LocalDest) {
        $LocalDest = Split-Path -Leaf $RemoteDir
    }

    Write-Info "Sparse-cloning directory '$RemoteDir' from $RepoUrl (ref: $CatalogRef)"

    # Use a temp directory so a partial failure doesn't leave a broken dest
    $TmpDir = [System.IO.Path]::Combine([System.IO.Path]::GetTempPath(), [System.IO.Path]::GetRandomFileName())
    New-Item -ItemType Directory -Force -Path $TmpDir | Out-Null

    try {
        Write-Info "Running: git clone --no-checkout --filter=blob:none --branch $CatalogRef $RepoUrl <tmpdir>"
        git clone `
            --no-checkout `
            --filter=blob:none `
            --branch $CatalogRef `
            $RepoUrl `
            $TmpDir `
            --quiet

        if ($LASTEXITCODE -ne 0) {
            Exit-WithError "git clone failed. Verify CATALOG_REPO='$CatalogRepo' and CATALOG_REF='$CatalogRef'."
        }

        Write-Info "Configuring sparse-checkout for path: $RemoteDir"
        git -C $TmpDir sparse-checkout init --cone
        if ($LASTEXITCODE -ne 0) { Exit-WithError "git sparse-checkout init failed." }

        git -C $TmpDir sparse-checkout set $RemoteDir
        if ($LASTEXITCODE -ne 0) { Exit-WithError "git sparse-checkout set failed." }

        Write-Info "Checking out files..."
        git -C $TmpDir checkout $CatalogRef --quiet
        if ($LASTEXITCODE -ne 0) { Exit-WithError "git checkout failed." }

        $Src = Join-Path $TmpDir $RemoteDir
        if (-not (Test-Path $Src)) {
            Exit-WithError "Directory '$RemoteDir' not found in the repository at ref '$CatalogRef'."
        }

        # Ensure parent of destination exists, then copy
        $DestParent = Split-Path -Parent $LocalDest
        if ($DestParent -and -not (Test-Path $DestParent)) {
            New-Item -ItemType Directory -Force -Path $DestParent | Out-Null
        }

        Copy-Item -Recurse -Force -Path $Src -Destination $LocalDest
        Write-Ok "Saved -> $LocalDest\"
    }
    finally {
        # Always clean up temp dir
        if (Test-Path $TmpDir) {
            Remove-Item -Recurse -Force $TmpDir -ErrorAction SilentlyContinue
        }
    }
}

# ---------------------------------------------------------------------------
# Command: skill
# ---------------------------------------------------------------------------
function Invoke-SkillCommand {
    param([string[]] $Args)

    if ($Args.Count -eq 0 -or -not $Args[0]) {
        Exit-WithError "Usage: fetch.ps1 skill <framework>/<skill-name>`n  Example: fetch.ps1 skill pragmatic-framework/competitive-landscape"
    }

    # Normalise: strip leading "skills/" if the user included it
    $SkillPath = $Args[0] -replace '^skills[\\/]', ''
    # Normalise backslashes to forward slashes for URL construction
    $SkillPath = $SkillPath -replace '\\', '/'

    $RemotePath = "skills/$SkillPath/SKILL.md"
    $LocalDest  = "$SkillPath/SKILL.md"

    Invoke-FetchFile -RemotePath $RemotePath -LocalDest $LocalDest
}

# ---------------------------------------------------------------------------
# Command: plugin
# ---------------------------------------------------------------------------
function Invoke-PluginCommand {
    param([string[]] $Args)

    if ($Args.Count -eq 0 -or -not $Args[0]) {
        Exit-WithError "Usage: fetch.ps1 plugin <plugin-name>`n  Example: fetch.ps1 plugin product-manager"
    }

    # Normalise: strip leading "plugins/" if the user included it
    $PluginName = $Args[0] -replace '^plugins[\\/]', ''

    Invoke-FetchDirectory -RemoteDir "plugins/$PluginName" -LocalDest $PluginName
}

# ---------------------------------------------------------------------------
# Command: standalone
# ---------------------------------------------------------------------------
function Invoke-StandaloneCommand {
    param([string[]] $Args)

    if ($Args.Count -eq 0 -or -not $Args[0]) {
        Exit-WithError "Usage: fetch.ps1 standalone <resource-name>`n  Example: fetch.ps1 standalone pdf-extractor"
    }

    # Normalise: strip leading "standalone/" if the user included it
    $ResourceName = $Args[0] -replace '^standalone[\\/]', ''

    Invoke-FetchDirectory -RemoteDir "standalone/$ResourceName" -LocalDest $ResourceName
}

# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
Assert-Dependencies

switch ($Command.ToLower()) {
    'skill'      { Invoke-SkillCommand      -Args $Arguments }
    'plugin'     { Invoke-PluginCommand     -Args $Arguments }
    'standalone' { Invoke-StandaloneCommand -Args $Arguments }
    { $_ -in 'help', '--help', '-h', '' } { Show-Help }
    default {
        Write-Err "Unknown command: '$Command'"
        Show-Help
        exit 1
    }
}
