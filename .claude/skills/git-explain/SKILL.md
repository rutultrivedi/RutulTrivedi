---
name: git-explain
description: Explain what changed, why, and who touched a file, function, commit or time range using git history. Use when the user asks what happened to some code, why it is the way it is, or what changed recently.
argument-hint: "<file | file:function | commit | 'last 2 weeks'>"
---

Explain the history of: $ARGUMENTS

## Steps

1. Work out what the target is:
   - A commit hash: `git show <hash>`.
   - A file: `git log --follow --stat -n 15 -- <file>` and `git blame` on the parts that matter.
   - A function: `git log -L :<function>:<file>`.
   - A time range or "recent changes": `git log --since="<range>" --stat --no-merges`.
   - Nothing given: summarize the last 10 commits.
2. Read the diffs of the important commits so the explanation is about the actual change, not only the message.
3. Answer in this shape:
   - **What changed**: the story in order, in plain language.
   - **Why**: the reason, taken from commit messages and context. If the reason is not recorded, say that and mark any inference as a guess.
   - **Who and when**: authors and dates for the key changes.
   - **Worth knowing**: anything that matters now, such as a later fix, a revert, or code that depends on it.
4. Keep it short and concrete. Quote hashes (short form) so the user can look further.
