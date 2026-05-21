# MATLAB Toolbox Packaging — API Reference

This reference covers the programmatic API for creating and managing MATLAB toolboxes. All functions live under the `matlab.addons.toolbox` namespace.

## Table of Contents
1. [ToolboxOptions — Object Creation](#toolboxoptions)
2. [ToolboxOptions — Properties](#properties)
3. [packageToolbox — Package the toolbox](#packagetoolbox)
4. [Install / Uninstall / Query functions](#lifecycle)

---

## 1. ToolboxOptions (since R2023a) <a name="toolboxoptions"></a>

### Construction

```matlab
opts = matlab.addons.toolbox.ToolboxOptions(toolboxFolder, identifier)
opts = matlab.addons.toolbox.ToolboxOptions(toolboxFolder, identifier, Name=Value)
opts = matlab.addons.toolbox.ToolboxOptions(projectFile)   % R2025a+
```

**toolboxFolder** — Path to the folder containing toolbox files (string or char).

**identifier** — RFC 4122 UUID string. Must remain constant across all versions of the toolbox. If the folder contains a package definition file, the identifier must match the one defined in the package.

To retrieve the UUID of an already-installed toolbox:
```matlab
addons = matlab.addons.installedAddons;
% The Identifier column contains the UUID
```

**projectFile** (R2025a+) — Path to a `.prj` file. The project must contain exactly one toolbox task.

---

## 2. ToolboxOptions Properties <a name="properties"></a>

### Metadata

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `ToolboxName` | string | derived from folder name | Display name of the toolbox |
| `ToolboxVersion` | string | `"1.0"` | Version in `major.minor.bug.build` format (bug/build optional) |
| `Description` | string | `""` | Detailed description |
| `Summary` | string | `""` | Short one-line summary |
| `AuthorName` | string | `""` | Author's name |
| `AuthorEmail` | string | `""` | Author's email |
| `AuthorCompany` | string | `""` | Author's company |
| `ToolboxImageFile` | string | `""` | Path to a representative image (e.g., 200×200 PNG) |

### File Control

| Property | Type | Description |
|----------|------|-------------|
| `ToolboxFiles` | string array | Files included in the toolbox (auto-populated from toolboxFolder) |
| `ToolboxMatlabPath` | string array | Folders added to the user's MATLAB path on install |
| `AppGalleryFiles` | string array | `.mlapp` files registered in the Apps gallery |
| `ToolboxGettingStartedGuide` | string | Path to `GettingStarted.mlx` (must be in a `doc/` subfolder) |
| `ToolboxJavaPath` | string array | JAR files added to the Java classpath on install |
| `OutputFile` | string | Path and filename for the `.mltbx` output |

### Compatibility

| Property | Type | Default | Description |
|----------|------|---------|-------------|
| `MinimumMatlabRelease` | string | `""` | Earliest compatible MATLAB release (e.g., `"R2020a"`) |
| `MaximumMatlabRelease` | string | `""` | Latest compatible release (empty = no upper bound) |
| `SupportedPlatforms` | struct | all `true` | Fields: `Win64`, `Mac`, `Glnxa64`, `MatlabOnline` |

### Dependencies

| Property | Type | Description |
|----------|------|-------------|
| `RequiredAddons` | struct array | Add-ons auto-installed with the toolbox. Fields: `Name`, `Identifier`, `EarliestVersion`, `LatestVersion`, `DownloadURL` |
| `RequiredAdditionalSoftware` | struct array | Third-party ZIP packages. Fields: `Name`, `Platform` (`"win64"`, `"maci64"`, `"glnxa64"`, `"common"`), `DownloadURL`, `LicenseURL` |

---

## 3. packageToolbox <a name="packagetoolbox"></a>

```matlab
matlab.addons.toolbox.packageToolbox(projectFile)
matlab.addons.toolbox.packageToolbox(projectFile, outputFile)
matlab.addons.toolbox.packageToolbox(opts)
```

- **projectFile** — `.prj` file path (string or char). In R2025a+ this can be a MATLAB project file containing a toolbox task.
- **outputFile** — Custom output path. Extension `.mltbx` is appended if missing.
- **opts** — A `ToolboxOptions` object (R2023a+).

The toolbox root folder and files must be in the same location as when the project or options object was created.

---

## 4. Install / Uninstall / Query <a name="lifecycle"></a>

### installToolbox
```matlab
tbx = matlab.addons.toolbox.installToolbox(mltbxFile)
tbx = matlab.addons.toolbox.installToolbox(mltbxFile, agreeToLicense)
```
Installs the `.mltbx` file. Returns a toolbox object that can be passed to other functions.

### uninstallToolbox
```matlab
matlab.addons.toolbox.uninstallToolbox(tbx)
```
Uninstalls a previously installed toolbox.

### toolboxVersion
```matlab
ver = matlab.addons.toolbox.toolboxVersion(tbx)
```
Returns the version string of the installed toolbox.

### installedToolboxes
```matlab
tbl = matlab.addons.toolbox.installedToolboxes
```
Returns a table listing all installed toolboxes with columns: `Name`, `Version`, `Enabled`, `Identifier`.

---

## Full example: Package with all options

```matlab
toolboxFolder = fullfile(pwd, 'src');
uuid = 'e5af5a78-4a80-11e4-9553-005056977bd0';

opts = matlab.addons.toolbox.ToolboxOptions(toolboxFolder, uuid);

% Metadata
opts.ToolboxName    = 'Signal Tools';
opts.ToolboxVersion = '2.1.0';
opts.AuthorName     = 'Jane Doe';
opts.AuthorEmail    = 'jane@example.com';
opts.AuthorCompany  = 'Acme Corp';
opts.Summary        = 'Advanced signal processing utilities.';
opts.Description    = 'Provides filtering, FFT helpers, and visualization tools for time-series data.';
opts.ToolboxImageFile = fullfile(toolboxFolder, 'resources', 'icon.png');

% Path — only the root and a utils subfolder
opts.ToolboxMatlabPath = [
    string(toolboxFolder)
    fullfile(toolboxFolder, 'utils')
];

% Apps
opts.AppGalleryFiles = fullfile(toolboxFolder, 'apps', 'SignalViewer.mlapp');

% Getting Started
opts.ToolboxGettingStartedGuide = fullfile(toolboxFolder, 'doc', 'GettingStarted.mlx');

% Compatibility
opts.SupportedPlatforms.Win64        = true;
opts.SupportedPlatforms.Mac          = true;
opts.SupportedPlatforms.Glnxa64      = true;
opts.SupportedPlatforms.MatlabOnline = true;
opts.MinimumMatlabRelease = 'R2020a';
opts.MaximumMatlabRelease = '';

% Required add-on
opts.RequiredAddons = struct( ...
    'Name',            'Signal Processing Toolbox', ...
    'Identifier',      'SL_Signal_Processing_Toolbox', ...
    'EarliestVersion', '', ...
    'LatestVersion',   '', ...
    'DownloadURL',     '');

% Output
opts.OutputFile = fullfile(pwd, 'release', 'SignalTools.mltbx');

% Package
mkdir(fullfile(pwd, 'release'));
matlab.addons.toolbox.packageToolbox(opts);
```

---

## File Exchange restrictions

When uploading to MATLAB Central File Exchange, the `.mltbx` must NOT contain:
- MEX files
- Binary executables (DLLs, ActiveX controls, .exe files)

Data files and images are generally acceptable.
