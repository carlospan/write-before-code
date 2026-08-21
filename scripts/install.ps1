# Install write-before-code into Cursor personal skills (Windows).
param(
  [string]$Destination = ""
)
$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
if (-not $Destination) {
  $Destination = Join-Path $env:USERPROFILE ".cursor\skills\write-before-code"
}
$destParent = Split-Path -Parent $Destination
New-Item -ItemType Directory -Force -Path $destParent | Out-Null
if (Test-Path $Destination) {
  Remove-Item -Recurse -Force $Destination
}
New-Item -ItemType Directory -Force -Path $Destination | Out-Null

Get-ChildItem -Force $Root | Where-Object {
  $_.Name -notin @('.git', '.github')
} | ForEach-Object {
  Copy-Item -Recurse -Force $_.FullName -Destination (Join-Path $Destination $_.Name)
}

Write-Host "Installed to: $Destination"
Write-Host "Restart Cursor or start a new agent chat, then say: use write-before-code"
