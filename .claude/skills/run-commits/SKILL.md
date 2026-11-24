---
name: run-commits
description: Run a lightweight Git maintenance session, make legitimate small improvements, commit changes, and optionally push them to the current branch.
disable-model-invocation: true
---

# Run Commits

You are running the `run-commits` workflow.

## Objective

Perform a lightweight repository maintenance session to keep the project active and maintained.

## Workflow

### 1. Inspect the repository

- Run `git status`.
- Identify the current branch.
- Check the latest commits.
- Never overwrite, discard, or modify existing uncommitted user changes.
- Never switch branches without permission.

### 2. Generate a random session number

Randomly select an integer between 10 and 100.

Use this number as the maximum number of maintenance checks to consider during this session.

### 3. Find maintenance opportunities

Inspect the repository and look for genuine improvements, such as:

- README corrections.
- Documentation improvements.
- Typographical fixes.
- Markdown formatting.
- Broken internal references.
- Small code-quality improvements.
- Test coverage improvements.
- Configuration cleanup.
- Outdated comments.
- Minor consistency fixes.

Do not invent bugs or make unnecessary modifications.

### 4. Make changes

- Make only changes that provide actual value.
- Keep changes small and focused.
- Never modify secrets, credentials, or environment files.
- Never introduce meaningless whitespace changes.
- Never create artificial changes just to increase commit counts.
- Never revert legitimate project changes simply to restore an earlier appearance.

### 5. Review changes

Before committing:

- Run `git diff`.
- Check that changes are relevant.
- Run appropriate tests when applicable.
- Ensure no secrets or sensitive information are included.

### 6. Commit changes

Create meaningful commits corresponding to actual changes.

Use descriptive commit messages, for example:

- docs: improve README structure
- docs: correct installation instructions
- chore: improve configuration consistency
- test: add missing documentation checks

Do not create empty commits or duplicate commits.

### 7. Push changes

Before pushing:

- Confirm the current branch.
- Confirm the remote destination.
- Check that the remote branch is correct.
- Ask for confirmation before pushing.

Never force-push, rewrite shared history, or push to another branch without permission.

### 8. Final report

Provide a summary containing:

- Random session number.
- Number of maintenance checks performed.
- Files changed.
- Commits created.
- Tests executed.
- Push status.
- Current Git status.

If no meaningful changes are available, finish without creating artificial commits.