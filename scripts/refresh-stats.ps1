# Refreshes assets/stats-30d.svg (last 30 days of GitHub activity) and pushes it.
# Uses your existing `gh` login, so no token needs to be created or stored.
# Run it whenever you want fresh numbers:  powershell -File scripts\refresh-stats.ps1
# Add -NoPush to regenerate the card locally without committing or pushing.
param([switch]$NoPush)

$ErrorActionPreference = 'Stop'
Set-Location (Split-Path -Parent $PSScriptRoot)

# Stop if you have other unfinished changes, so they are never committed by accident (scripts/ is ignored here)
if (git status --porcelain -- . ':!scripts') {
    Write-Host 'The repo has other uncommitted changes. Commit or stash them first, then run this again.' -ForegroundColor Yellow
    exit 1
}

Write-Host 'Pulling latest changes...'
git pull --rebase -q

Write-Host 'Fetching your last 30 days of activity...'
$env:GH_TOKEN = (gh auth token)
try { python scripts/generate_stats.py } finally { Remove-Item Env:GH_TOKEN -ErrorAction SilentlyContinue }

if (-not (git status --porcelain assets/stats-30d.svg README.md)) { Write-Host 'Card is already up to date.' -ForegroundColor Green; exit 0 }
if ($NoPush) { Write-Host 'Card regenerated locally (-NoPush: nothing committed or pushed).' -ForegroundColor Green; exit 0 }

git add assets/stats-30d.svg README.md
git commit -q -m 'Update 30-day activity card'
git push -q
Write-Host 'Done. Card updated and pushed. Hard refresh your profile (Ctrl+F5) to see it.' -ForegroundColor Green
