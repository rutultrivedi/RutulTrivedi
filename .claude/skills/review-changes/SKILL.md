---
name: review-changes
description: Self-review the uncommitted or staged changes before committing, checking for bugs, leftover debug code, secrets and risky edits. Use when the user wants a quick review or a pre-commit check.
argument-hint: "[staged | branch | file-path]"
---

Review the pending changes and report problems. Do not edit anything unless the user asks. Scope: $ARGUMENTS

## Steps

1. Choose the diff:
   - No argument: `git diff` plus `git diff --cached`.
   - `staged`: `git diff --cached`.
   - `branch`: `git diff <default-branch>...HEAD`.
   - A file path: the diff for that file only.
   If the diff is empty, say so and stop.
2. Read the changed files around each hunk, not only the diff lines, so you judge the change in context.
3. Check for:
   - Bugs: wrong conditions, off-by-one errors, unhandled errors, null or empty cases, broken references.
   - Secrets: keys, tokens, passwords, connection strings, `.env` content, private URLs.
   - Leftovers: debug prints, commented-out code, TODO or FIXME added by this change, test-only shortcuts.
   - Scope: unrelated edits, accidental large or generated files, mixed concerns that should be separate commits.
   - Missing pieces: tests, docs or config that should change along with the code.
4. Report findings ordered by severity: **Must fix**, **Should fix**, **Nit**. For each, give the file and line, what is wrong, and a concrete fix. If something looks fine, do not pad the list.
5. End with a one-line verdict: ready to commit, or fix the listed items first.
