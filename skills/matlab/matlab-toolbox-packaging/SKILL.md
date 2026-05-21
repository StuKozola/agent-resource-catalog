---
name: matlab-toolbox-packaging
description: Package MATLAB code into a distributable toolbox (.mltbx file). Use this skill whenever the user wants to create, package, distribute, or publish a MATLAB toolbox — including setting up the folder structure, writing the packaging script, configuring toolbox metadata (version, author, description, platform support), adding a Getting Started guide, managing path entries, or preparing code for MATLAB Central File Exchange. Trigger on any mention of "MATLAB toolbox", ".mltbx", "package toolbox", "share MATLAB code", "distribute MATLAB functions", "toolbox packaging", "ToolboxOptions", "packageToolbox", "MATLAB add-on", "toolbox project", "File Exchange submission", or any request to bundle MATLAB .m files, apps (.mlapp), or data into a single installable package. Even casual requests like "how do I share my MATLAB code as a toolbox" or "make this installable" should use this skill.
---

# MATLAB Toolbox Packaging

This skill helps users package MATLAB code, data, apps, examples, and documentation into a distributable `.mltbx` toolbox file. It covers both the **GUI workflow** (Package Toolbox dialog / toolbox task) and the **programmatic workflow** (`ToolboxOptions` + `packageToolbox`).

## When to use this skill

- User wants to bundle MATLAB functions into a single installable package
- User wants to share code via MATLAB Central File Exchange
- User wants to create a `.mltbx` file
- User needs help structuring a toolbox folder
- User needs a packaging script they can run from CI or the command line

## Decision: GUI vs Programmatic

Ask the user (or infer from context) which workflow they need:

| Signal | Workflow |
|--------|----------|
| "script", "automate", "CI", "command line", "programmatic" | **Programmatic** — generate a MATLAB script using `ToolboxOptions` + `packageToolbox` |
| "dialog", "UI", "interactive", "click", no strong signal | **GUI** — walk them through the Package Toolbox task UI |
| User provides a folder of .m files and wants a ready-to-run script | **Programmatic** |

Default to **programmatic** unless the user explicitly wants the GUI walkthrough — scripts are reproducible and versionable.

---

## Step 1: Establish the recommended folder structure

Before packaging, help the user organize their code. Recommend this layout:

```
myToolbox/
├── +myToolbox/          % (optional) namespace package
│   ├── func1.m
│   └── func2.m
├── myFunc.m             % top-level functions (added to path)
├── apps/
│   └── MyApp.mlapp      % (optional) installable apps
├── data/
│   └── sampleData.mat   % (optional) bundled data
├── doc/
│   └── GettingStarted.mlx  % (optional) Getting Started live script
├── examples/
│   └── exampleScript.mlx   % (optional) example live scripts
├── tests/               % (optional) unit tests — typically EXCLUDED from toolbox
└── resources/
    └── toolbox_image.png % (optional) 200×200 icon
```

Key guidance:
- Only folders that should be on the user's MATLAB path go into `ToolboxMatlabPath`. Typically the root folder (and maybe a subfolder for utilities), but NOT `tests/`, `doc/`, `data/`, or `examples/`.
- If a P-code file and its .m source share the same name in the same folder, MATLAB auto-excludes the .m file from the package.
- Exclude source-control files (`.git/`, `.svn/`), build artifacts, and test fixtures.

## Step 2: Generate the packaging script (Programmatic workflow)

Generate a MATLAB script the user can run to produce the `.mltbx`. Use the `ToolboxOptions` object (available since R2023a) for full control.

### Template

```matlab
%% package_toolbox.m — Packages <ToolboxName> into an .mltbx file
% Run this script from the repository root.
% Requires MATLAB R2023a or later (for ToolboxOptions).

%% --- Configuration (edit these) -------------------------------------------
toolboxFolder   = fullfile(pwd, 'myToolbox');          % folder containing toolbox files
toolboxUUID     = '<GENERATE-A-UUID>';                 % RFC 4122 UUID — must stay constant across versions
toolboxName     = 'My Toolbox';
toolboxVersion  = '1.0.0';
authorName      = '';
authorEmail     = '';
authorCompany   = '';
summary         = 'One-line summary of the toolbox.';
description     = 'Longer description of the toolbox and its capabilities.';
outputFile      = fullfile(pwd, 'release', [toolboxName '.mltbx']);

%% --- Create ToolboxOptions ------------------------------------------------
opts = matlab.addons.toolbox.ToolboxOptions(toolboxFolder, toolboxUUID);

opts.ToolboxName    = toolboxName;
opts.ToolboxVersion = toolboxVersion;
opts.AuthorName     = authorName;
opts.AuthorEmail    = authorEmail;
opts.AuthorCompany  = authorCompany;
opts.Summary        = summary;
opts.Description    = description;
opts.OutputFile     = outputFile;

% --- Path management -------------------------------------------------------
% Only list folders that should be added to the user's MATLAB path on install.
opts.ToolboxMatlabPath = toolboxFolder;  % or a string array of subfolders

% --- (Optional) Getting Started guide --------------------------------------
% gettingStarted = fullfile(toolboxFolder, 'doc', 'GettingStarted.mlx');
% if isfile(gettingStarted)
%     opts.ToolboxGettingStartedGuide = gettingStarted;
% end

% --- (Optional) Toolbox image ----------------------------------------------
% opts.ToolboxImageFile = fullfile(toolboxFolder, 'resources', 'toolbox_image.png');

% --- (Optional) App gallery files ------------------------------------------
% opts.AppGalleryFiles = fullfile(toolboxFolder, 'apps', 'MyApp.mlapp');

% --- (Optional) Platform & release compatibility ---------------------------
% opts.SupportedPlatforms.Win64        = true;
% opts.SupportedPlatforms.Mac          = true;
% opts.SupportedPlatforms.Glnxa64      = true;
% opts.SupportedPlatforms.MatlabOnline = true;
% opts.MinimumMatlabRelease = 'R2020a';
% opts.MaximumMatlabRelease = '';        % empty = no upper bound

% --- (Optional) Required add-ons ------------------------------------------
% opts.RequiredAddons = struct( ...
%     'Name',            'Some Toolbox', ...
%     'Identifier',      'uuid-of-addon', ...
%     'EarliestVersion', '1.0', ...
%     'LatestVersion',   '', ...
%     'DownloadURL',     '');

%% --- Package --------------------------------------------------------------
if ~isfolder(fileparts(outputFile))
    mkdir(fileparts(outputFile));
end

matlab.addons.toolbox.packageToolbox(opts);
fprintf('Toolbox packaged: %s\n', outputFile);
```

### UUID generation

Every toolbox needs a stable RFC 4122 UUID that stays the same across all versions. Generate one for the user if they don't have one:

```matlab
% Quick UUID generator (paste in MATLAB Command Window once)
uuid = lower(strjoin(string(dec2hex(randi(255,16,1),2))',''));
uuid = [uuid(1:8) '-' uuid(9:12) '-4' uuid(14:16) '-' ...
        char(randi([8 11],1,1)+48) uuid(18:20) '-' uuid(21:32)];
disp(uuid)
```

Or in many environments: `java.util.UUID.randomUUID().toString()`.

Tell the user: **save this UUID and reuse it for every future version** of the toolbox. If the UUID changes, MATLAB treats it as a completely different toolbox.

## Step 3: Walk through the GUI workflow (if chosen)

If the user wants the interactive workflow instead:

### R2025a+ (project-integrated)
1. Open or create a MATLAB Project containing the toolbox files.
2. Go to **Project** tab → **Package Toolbox**.
3. MATLAB creates a toolbox task. Configure:
   - **Toolbox Folder** — point to the root folder.
   - **Toolbox Information** — name, version (`major.minor.bug.build`), author, summary, description, image.
   - **Toolbox Requirements** — review auto-detected add-on and file dependencies; resolve warnings.
   - **Output Settings** — filename and destination for the `.mltbx`.
   - **Install Actions** — which folders go on the MATLAB path, Java classpath entries, apps to register, Getting Started guide.
   - **Toolbox Portability** — supported platforms, min/max MATLAB release.
   - **Third-Party Software** — optional ZIP bundles with license URLs.
4. Click **Reanalyze** to check for issues, then **Package Toolbox**.

### Pre-R2025a
1. **Home** tab → **Add-Ons** → **Package Toolbox**.
2. Click the **+** button, select the toolbox folder.
3. Fill in metadata and click **Package**.

## Step 4: Verify the toolbox

After packaging, suggest the user verify the `.mltbx`:

```matlab
% Install the toolbox
tbx = matlab.addons.toolbox.installToolbox('release/My Toolbox.mltbx');

% Check version
matlab.addons.toolbox.toolboxVersion(tbx)

% List installed toolboxes
matlab.addons.toolbox.installedToolboxes

% Uninstall when done testing
matlab.addons.toolbox.uninstallToolbox(tbx)
```

## Step 5: Distribute

Help the user choose a distribution channel:

- **Email / shared drive** — just send the `.mltbx` file.
- **MATLAB Central File Exchange** — upload at https://www.mathworks.com/matlabcentral/fileexchange/. Note: File Exchange prohibits MEX files, DLLs, and binary executables inside submissions.
- **GitHub releases** — attach the `.mltbx` as a release asset. Users download and double-click to install.
- **Internal package manager** — for enterprise distribution.

---

## Common pitfalls to warn about

1. **Changing the UUID between versions** — MATLAB will treat it as a brand-new toolbox instead of an upgrade. Always reuse the same UUID.
2. **Putting too many folders on the path** — only add folders the user needs to call functions from. Don't add `tests/`, `doc/`, `examples/`, or internal helper folders.
3. **Forgetting to exclude `.git/`** — the default exclusion handles most source-control files, but double-check if using a non-standard SCM layout.
4. **Not testing on a clean MATLAB** — always verify the `.mltbx` installs and runs on a MATLAB instance that doesn't have the toolbox source on its path.
5. **Missing dependencies** — run the Dependency Analyzer (`Project` tab → toolbox task → **View Analysis**) to catch references to other toolboxes or files outside the toolbox folder.
6. **Version format** — use `major.minor.bug.build` (bug and build are optional). Non-numeric or arbitrarily formatted versions will cause errors.

---

## API quick reference

For full details on properties and methods, read `references/api-reference.md`.

| Function | Purpose |
|----------|---------|
| `matlab.addons.toolbox.ToolboxOptions(folder, uuid)` | Create options object (R2023a+) |
| `matlab.addons.toolbox.packageToolbox(opts)` | Package using options object |
| `matlab.addons.toolbox.packageToolbox(prjFile)` | Package from .prj file |
| `matlab.addons.toolbox.packageToolbox(prjFile, outFile)` | Package with custom output name |
| `matlab.addons.toolbox.installToolbox(mltbxFile)` | Install a toolbox |
| `matlab.addons.toolbox.uninstallToolbox(tbx)` | Uninstall a toolbox |
| `matlab.addons.toolbox.toolboxVersion(tbx)` | Get version string |
| `matlab.addons.toolbox.installedToolboxes` | List all installed toolboxes |

## Pre-R2023a fallback

If the user is on R2020a–R2022b (no `ToolboxOptions`), they must use the `.prj` file approach:

1. Create the `.prj` via the GUI (**Home** → **Add-Ons** → **Package Toolbox**).
2. Package programmatically:
   ```matlab
   matlab.addons.toolbox.packageToolbox('myToolbox.prj')
   matlab.addons.toolbox.packageToolbox('myToolbox.prj', 'output/myToolbox.mltbx')
   ```
3. The `.prj` is an XML file that can be version-controlled, but editing it by hand is fragile — prefer the GUI for changes.
