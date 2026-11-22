---
name: handoff-here
description: Write a handoff prompt in the chat itself that the user can paste into a new session to continue the work. Use when the user wants to hand off, continue in a new chat, or save context before stopping.
argument-hint: "[extra note]"
---

Produce a handoff as one copy-paste block, printed here in chat. Extra note from the user (optional): $ARGUMENTS

## Steps

1. Gather facts from this conversation and, if the work is in a repo, from `git status --short`, `git branch --show-current` and `git log -5 --oneline`. Do not guess anything you cannot support.
2. Print a single fenced code block, written as a prompt addressed to a fresh assistant, with these sections:

   ```
   You are continuing work from a previous session. Read this fully before acting.

   GOAL
   <what the user is trying to achieve, in one or two sentences>

   STATE
   <what is done and verified; what is done but untested>

   PENDING
   <the remaining tasks, in order; mark the very next step>

   KEY FILES AND PLACES
   <absolute paths, repo, branch, scripts, commands that matter>

   DECISIONS AND RULES
   <choices already made, user preferences and constraints, things not to redo or undo>

   OPEN QUESTIONS AND RISKS
   <unresolved items, known problems, things that need the user's input>

   FIRST ACTION
   <exactly what to do first, and any confirmation needed before it>
   ```

3. Never put secrets, tokens, passwords or personal data in the block. Refer to them by name only (for example, "the GH_TOKEN env var").
4. Keep it tight: enough that a new session needs no re-explaining, nothing that only mattered to the old session.
5. Add one line after the block telling the user to paste it as the first message of the new chat.
