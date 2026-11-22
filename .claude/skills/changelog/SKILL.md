---
name: changelog
description: Generate release notes or a changelog from the commits since the last tag or a given point. Use when the user wants a changelog, release notes, or a summary of what changed since the last release.
argument-hint: "[from-ref] [to-ref]"
---

Build release notes from git history. Optional range: $ARGUMENTS

## Steps

1. Pick the range:
   - If the user gave refs, use them (`<from>..<to>`, with `to` defaulting to `HEAD`).
   - Otherwise use the last tag: `git describe --tags --abbrev=0`. If there are no tags, use the whole history and say so.
2. Run `git log <range> --no-merges --pretty=format:"%h %s (%an)"`. Read the diffs of unclear commits instead of guessing.
3. Group the entries under these headings, skipping empty ones: **Added**, **Changed**, **Fixed**, **Removed**, **Other**.
4. Rewrite each entry as one plain-language line that says what the change means for a user, not the raw commit text. Merge near-duplicates. Drop pure noise (typo fixes, merge commits, formatting) unless that is all there is.
5. Add a heading with the version or date range at the top.
6. Show the notes in chat. Only write or update a `CHANGELOG.md` file if the user asks, and if one exists, add the new section at the top and keep its existing format.
