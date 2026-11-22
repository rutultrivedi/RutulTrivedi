---
name: disk-check
description: Check C drive storage, find what takes the most space, and list unnecessary items that are safe to delete, with manual steps. Never deletes anything. Use when the user's C drive is filling up or they want a storage review.
disable-model-invocation: true
---

Analyze C drive usage and report. This skill is read-only.

## Hard rule

Never delete, move, rename, empty, or clean anything. Do not run `Remove-Item`, `del`, `rd`, `rmdir`, `cleanmgr`, `npm cache clean`, `docker system prune`, `Clear-RecycleBin`, or any similar command. Only measure and report. The user performs every deletion themselves.

## Steps

1. Get the totals: `Get-PSDrive C` (used and free) and report them as GB and percent used.
2. Measure the biggest top-level folders under `C:\` and under the user profile (`C:\Users\<name>`, including `AppData\Local`, `AppData\Roaming`, `Downloads`, `Documents`, `Desktop`, `Videos`, `Pictures`). Use `Get-ChildItem -Force -ErrorAction SilentlyContinue` and sum file sizes. Folders that need admin rights will be skipped; list them as "could not read" instead of ignoring them. This can be slow, so show partial results if a folder takes too long.
3. Check these usual space users (report size and whether it exists):
   - Temp: `%TEMP%`, `C:\Windows\Temp`
   - Windows Update download cache: `C:\Windows\SoftwareDistribution\Download`
   - `C:\Windows.old`, hibernation file `hiberfil.sys`, page file
   - Recycle Bin
   - Browser caches (Chrome, Edge) and the Downloads folder
   - Dev caches: npm (`%AppData%\npm-cache` or `%LocalAppData%\npm-cache`), pip cache, NuGet, Gradle, Docker and WSL disk images (`ext4.vhdx`), `node_modules` folders
   - The largest individual files (top 20 over 500 MB)
4. Present a table: item, path, size, rating, and why. Ratings:
   - **Safe**: rebuilds itself and deleting it breaks nothing (temp files, caches, Recycle Bin contents the user has looked at).
   - **Check first**: could hold something the user wants (Downloads, old installers, large videos, `Windows.old`, Docker or WSL images, project `node_modules`).
   - **Never touch**: system files and anything Windows or an app needs (`System32`, `WinSxS`, `hiberfil.sys` and the page file unless the user changes the setting deliberately, `Program Files`).
5. Order the table by size within each rating and add a total of how much the Safe group could free.
6. For each Safe and Check first item, give the manual steps in plain words, using the Windows tools the user clicks through: Settings, System, Storage, Temporary files, or Storage Sense; Disk Cleanup (including "Clean up system files"); emptying the Recycle Bin from its window; clearing browser data from the browser's own settings; uninstalling apps from Settings, Apps; and so on. Do not write delete commands.
7. Finish with the top 3 actions that would free the most space with the least risk.
