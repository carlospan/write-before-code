# Install write-before-code into one or more Agent Skills directories.
# Compatible with the open Agent Skills layout (SKILL.md at skill root).
param(
  [ValidateSet("cursor", "codex", "trae", "claude", "all")]
  [string]$Agent = "all",

  [ValidateSet("user", "project")]
  [string]$Scope = "user",

  # Only used when Scope=project (defaults to current directory)
  [string]$ProjectRoot = "",

  # Override a single destination (skips Agent matrix)
  [string]$Destination = ""
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
$SkillName = "write-before-code"

function Get-Home {
  if ($env:USERPROFILE) { return $env:USERPROFILE }
  return $HOME
}

function Resolve-Targets {
  param([string]$AgentName, [string]$ScopeName, [string]$ProjRoot)

  $home = Get-Home
  $mapUser = @{
    cursor = Join-Path $home ".cursor\skills\$SkillName"
    codex  = Join-Path $home ".agents\skills\$SkillName"
    trae   = Join-Path $home ".trae\skills\$SkillName"
    claude = Join-Path $home ".claude\skills\$SkillName"
  }
  $mapProject = @{
    cursor = Join-Path $ProjRoot ".cursor\skills\$SkillName"
    codex  = Join-Path $ProjRoot ".agents\skills\$SkillName"
    trae   = Join-Path $ProjRoot ".trae\skills\$SkillName"
    claude = Join-Path $ProjRoot ".claude\skills\$SkillName"
  }

  $map = if ($ScopeName -eq "project") { $mapProject } else { $mapUser }
  if ($AgentName -eq "all") {
    return @($map.cursor, $map.codex, $map.trae, $map.claude)
  }
  return @($map[$AgentName])
}

function Install-One {
  param([string]$Dest)

  $parent = Split-Path -Parent $Dest
  New-Item -ItemType Directory -Force -Path $parent | Out-Null
  if (Test-Path $Dest) {
    Remove-Item -Recurse -Force $Dest
  }
  New-Item -ItemType Directory -Force -Path $Dest | Out-Null

  Get-ChildItem -Force $Root | Where-Object {
    $_.Name -notin @('.git', '.github')
  } | ForEach-Object {
    Copy-Item -Recurse -Force $_.FullName -Destination (Join-Path $Dest $_.Name)
  }

  if (-not (Test-Path (Join-Path $Dest "SKILL.md"))) {
    throw "Install failed: SKILL.md missing at $Dest"
  }
  Write-Host "Installed -> $Dest"
}

if ($Destination) {
  Install-One -Dest $Destination
} else {
  if ($Scope -eq "project") {
    if (-not $ProjectRoot) { $ProjectRoot = (Get-Location).Path }
    $ProjectRoot = (Resolve-Path $ProjectRoot).Path
  }
  $targets = Resolve-Targets -AgentName $Agent -ScopeName $Scope -ProjRoot $ProjectRoot
  foreach ($t in $targets) {
    Install-One -Dest $t
  }
}

Write-Host ""
Write-Host "Restart the agent (or open a new session), then invoke write-before-code:"
Write-Host "  Cursor / Trae / Claude Code:  /write-before-code   or say 'use write-before-code'"
Write-Host "  Codex:                        `$write-before-code  or say 'use write-before-code'"
Write-Host ""
Write-Host "Examples:"
Write-Host "  .\scripts\install.ps1 -Agent cursor"
Write-Host "  .\scripts\install.ps1 -Agent codex"
Write-Host "  .\scripts\install.ps1 -Agent trae"
Write-Host "  .\scripts\install.ps1 -Agent claude"
Write-Host "  .\scripts\install.ps1 -Agent all"
Write-Host "  .\scripts\install.ps1 -Agent all -Scope project"
