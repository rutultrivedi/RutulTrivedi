---
name: readme-sync
description: Bring a repo's README in line with the repo's current state (features, setup, scripts, structure), show the diff, and commit only after approval. Use when the README is outdated or the user wants it synced with the code.
argument-hint: "[extra instruction]"
disable-model-invocation: true
---

Sync the README of the current repo with what the repo actually contains. Extra instruction from the user (optional): $ARGUMENTS

## Steps

1. Read the existing `README.md` fully. Note its structure, voice, formatting and any rules the user has set (for example, a profile README with no emojis or no mention of employers). Keep all of that.
2. Inspect what the repo really contains:
   - Layout: top-level folders and main files (`git ls-files` or a directory listing).
   - Manifests and config: `package.json`, `pyproject.toml`, `requirements.txt`, `*.csproj`, `Dockerfile`, workflow files, scripts.
   - How to install, run and test, taken from real files and scripts, not guessed.
   - Recent history: `git log -20 --oneline`, for new features or removed ones.
   - Referenced assets: every image or link in the README should point to something that exists.
3. Compare README against reality and list the gaps: missing or outdated sections, commands that no longer work, features that were added or removed, broken asset paths, stale version numbers or dates.
4. Edit only what is out of date, matching the README's current voice and style. Do not rewrite sections that are still correct, do not invent features, and do not add badges or sections the user did not ask for.
5. Show the result with `git diff README.md` and summarize the changes in a short list.
6. Ask for approval. Only after an explicit yes, commit just the README (and any asset files the change depends on), using the repo's commit message style. Do not push unless the user asks. If the user wants changes, revise and show the diff again.
