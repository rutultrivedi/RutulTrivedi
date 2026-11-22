---
name: startup-audit
description: List everything that launches when Windows starts, judge which items are worth keeping, and explain how to disable the rest manually. Read-only. Use when boot is slow or the user wants to trim startup apps.
disable-model-invocation: true
---

Audit Windows startup items. This skill is read-only.

## Hard rule

Do not disable, delete or edit any startup entry, scheduled task, service or registry value. Only read and report. The user changes things themselves.

## Steps

1. Collect startup entries with PowerShell:
   - `Get-CimInstance Win32_StartupCommand` (name, command, location, user)
   - Registry run keys: `HKCU:\Software\Microsoft\Windows\CurrentVersion\Run` and `HKLM:\Software\Microsoft\Windows\CurrentVersion\Run` (read values only)
   - Startup folders: `shell:startup` and `shell:common startup` (list the files)
   - Scheduled tasks with logon or boot triggers that are not from Microsoft: `Get-ScheduledTask` filtered to enabled tasks with `LogonTrigger` or `BootTrigger`
   - Automatic-start services that are not from Microsoft (`Get-CimInstance Win32_Service` with `StartMode = Auto`, skipping paths under `C:\Windows`)
2. For each item identify the publisher and what it is. If you cannot identify it from its name and path, say "unknown, verify before changing" instead of guessing.
3. Rate each item:
   - **Keep**: security software, drivers and hardware utilities the laptop needs (audio, touchpad, graphics), cloud sync the user relies on.
   - **Optional**: apps that are fine to start manually instead (chat apps, launchers, updaters, game clients, helpers for apps the user rarely opens).
   - **Review**: unknown, unsigned, or in an unusual location such as a Temp folder. Suggest scanning with Windows Security if it looks suspicious.
4. Present a table: name, what it is, where it starts from, rating, and why. Include an estimate of impact where Windows exposes it (Task Manager shows "Startup impact"; mention that the user can read it there).
5. Give the manual steps: Task Manager, Startup apps tab, right-click, Disable; or Settings, Apps, Startup. For scheduled tasks, mention Task Scheduler. Tell the user that disabling an item is reversible and does not uninstall it.
6. End with a short list of the top items most worth disabling.
