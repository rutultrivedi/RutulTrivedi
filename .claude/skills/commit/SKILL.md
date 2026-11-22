---
name: commit
description: Stage the current changes, write a clear commit message in the repo's own style, commit, and push. Use when the user says commit, commit and push, or save my changes to git.
disable-model-invocation: true
---

Commit the current work and push it. Optional extra instruction from the user: $ARGUMENTS

## Steps

1. Run `git status --short`, `git diff` and `git diff --cached` to see everything that changed. If there is nothing to commit, say so and stop.
2. Run `git log -8 --oneline` to learn the message style used in this repo (tense, length, prefixes) and match it.
3. Decide what belongs in the commit. Stage files by name, not with `git add -A`. Never stage `.env` files, keys, tokens, credentials, or large generated or binary files that look accidental. If you skip something, tell the user.
4. If the changes are really two unrelated things, make two commits.
5. Write the message:
   - Subject line in the imperative mood, about 50 to 72 characters, no trailing period.
   - Add a short body only when the why is not obvious from the subject.
   - If the user gave extra instructions in the arguments, follow them.
   - End the message with the attribution trailer that the session instructions specify, if any.
6. Commit. Never use `--no-verify`, and never amend an existing commit unless the user asked. If a hook fails, fix the cause and make a new commit.
7. Push to the current branch's upstream. If there is no upstream, use `git push -u origin <branch>`. If the push is rejected, run `git pull --rebase` once and push again. Never force push.
8. Report the commit hash, the subject line, the files included, and the branch it was pushed to.
