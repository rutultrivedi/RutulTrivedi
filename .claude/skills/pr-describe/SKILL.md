---
name: pr-describe
description: Write a pull request title and description from the current branch's commits and diff. Use when the user wants a PR description, PR summary, or help opening a pull request.
argument-hint: "[base-branch]"
---

Write a pull request description for the current branch. Base branch (optional): $ARGUMENTS

## Steps

1. Find the base branch. Use the argument if given. Otherwise run `git symbolic-ref refs/remotes/origin/HEAD` and fall back to `main` or `master`.
2. Run `git log <base>..HEAD --oneline` and `git diff <base>...HEAD --stat`, then read the actual diff for anything important. If there are no commits ahead of the base, say so and stop.
3. Write the result in this shape:

   **Title**: under 70 characters, imperative, describes the outcome.

   **Summary**: 2 to 4 sentences on what changed and why.

   **Changes**: a short bullet list grouped by area (not one bullet per commit).

   **How to test**: concrete steps or commands a reviewer can run.

   **Notes**: breaking changes, migrations, follow-ups, or risks. Leave this out if there are none.

4. Keep the tone plain and factual. Do not invent test results or claims the diff does not support.
5. Show the result in chat. Only if the user asks, create the PR with `gh pr create --title ... --body ...`, and confirm the base and head branches first. End any PR body with the attribution line the session instructions specify, if any.
