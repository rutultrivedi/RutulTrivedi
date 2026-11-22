---
name: system-health
description: "Report the laptop's health: CPU, memory, disk, battery, uptime and the heaviest processes, with a verdict and manual fixes. Read-only. Use when the laptop feels slow, hot, or the user wants a health check."
disable-model-invocation: true
---

Check the health of this Windows laptop. This skill is read-only.

## Hard rule

Do not stop processes, change settings, edit the registry, or install anything. Only read and report. Give the user manual steps for anything they should change.

## Steps

1. Collect these with PowerShell (`Get-CimInstance`, `Get-Counter`, `Get-Process`, `Get-PSDrive`). Take a short CPU sample (a few seconds), not a single reading.
   - OS, model, uptime (time since last boot)
   - CPU: name, cores, current load
   - Memory: total, used, free, percent used
   - Disks: each drive's size, free space, percent used, and the disk health status from `Get-PhysicalDisk` if available
   - Battery (if present): charge percent, charging state, estimated runtime, and design versus full-charge capacity if it can be read without admin rights
   - Top 8 processes by CPU and top 8 by memory, with names and sizes
   - Number of pending reboots or updates if readable
2. Rate each area **OK**, **Watch** or **Problem**, with the number that justifies it. Use sensible thresholds: memory above 85 percent, any drive above 90 percent full, sustained CPU above 80 percent, battery capacity under 70 percent of design, uptime above 14 days are all worth flagging.
3. Present one compact table of areas and ratings, then a short list of the heaviest processes in plain language (what each one is, and whether it is normal).
4. Give a verdict in one or two sentences, then manual steps for each Watch or Problem item, using Windows tools the user clicks through (Task Manager, Settings, Storage, Startup apps, Windows Update, power settings). Do not give commands that change the system.
5. Say plainly if any reading was unavailable and why (for example, needs administrator rights).
