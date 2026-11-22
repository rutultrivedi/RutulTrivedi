---
name: branch-cleanup
description: List merged or stale local and remote git branches and delete them only after the user confirms. Use when the user wants to clean up, prune or tidy their branches.
disable-model-invocation: true
---

Clean up branches in the current repo. Never delete anything without explicit confirmation.

## Steps

1. Run `git fetch --prune` so remote information is current.
2. Identify the default branch (`git symbolic-ref refs/remotes/origin/HEAD`) and the current branch. These two are never candidates for deletion.
3. Collect candidates:
   - Local branches already merged into the default branch: `git branch --merged <default>`.
   - Local branches whose upstream is gone: `git branch -vv` entries marked `gone`.
   - Remote branches already merged: `git branch -r --merged origin/<default>`.
   - Local branches with unmerged commits, listed separately as "has unmerged work" with the commit count and last commit date.
4. Present one table: branch, local or remote, status, last commit date. Group it as Safe (merged or gone), and Unmerged (needs a decision).
5. Ask which to delete. Do not assume.
6. Delete local branches with `git branch -d`. Use `-D` only for an unmerged branch the user named explicitly, after warning that the commits will be lost.
7. Delete remote branches with `git push origin --delete <branch>` only after a separate explicit confirmation, because it affects other people and cannot be undone easily.
8. Report what was deleted and what was kept.
