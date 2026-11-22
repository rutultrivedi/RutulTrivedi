---
name: handoff-md
description: Create a handoff markdown file on the user's Desktop that summarizes the current work so a new session or person can continue. Use when the user wants a handoff file saved to disk.
argument-hint: "[extra note]"
disable-model-invocation: true
---

Write a handoff file to the Desktop. Extra note from the user (optional): $ARGUMENTS

## Steps

1. Find the real Desktop path, since it may be redirected to OneDrive. Run in PowerShell: `[Environment]::GetFolderPath('Desktop')`. Use exactly what it returns.
2. Pick the project name: the repo folder name if inside a git repo (`Split-Path -Leaf (git rev-parse --show-toplevel)`), otherwise the current folder name. Replace characters that are not safe in file names with `-`.
3. The file name is `HANDOFF-<project>-<yyyy-MM-dd>.md`. If that file already exists, add the time (`-HHmm`) instead of overwriting. Never overwrite an existing file.
4. Gather facts from this conversation and, if in a repo, from `git status --short`, `git branch --show-current` and `git log -5 --oneline`. Do not guess anything you cannot support.
5. Write the file with these sections:

   - `# Handoff: <project>` with the date and the working directory
   - `## Goal`
   - `## Current state` (done and verified, done but untested)
   - `## Pending tasks` (ordered, the very next step marked)
   - `## Key files and commands` (absolute paths, branch, how to run or test)
   - `## Decisions and rules` (choices made, user preferences, things not to redo)
   - `## Open questions and risks`
   - `## How to continue` (the exact first action for the next session)

6. Never write secrets, tokens, passwords or personal data into the file. Refer to them by name only.
7. Tell the user the full path of the file you created, and a one-line way to use it: start the new chat by asking the assistant to read that file and continue.
