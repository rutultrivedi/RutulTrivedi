---
name: explore-this
description: Explain in plain, complete detail what a given link is, such as a website, GitHub repo, article, docs page, or tool. Use when the user gives a URL and wants to know what it is and what it does.
argument-hint: "<link>"
---

Explain what this link is: $ARGUMENTS

## Steps

1. If no link was given, ask for one and stop.
2. Fetch the content:
   - GitHub repo link: use `gh` (`gh repo view <owner/repo>`, the README via `gh api repos/<owner>/<repo>/readme`, the top-level file list, languages, recent commits and release info). Fall back to fetching the page if `gh` fails.
   - Any other link: fetch the page with the web fetch tool and follow one or two important internal links (about, docs, pricing, getting started) if the first page is thin.
3. If the link cannot be opened (login wall, private repo, blocked site, error), say clearly that it could not be read and why, then stop. Do not guess what the page contains and do not substitute information from memory.
4. Explain it so a non-expert can follow it. Use this shape:
   - **What it is**: one or two sentences, no jargon.
   - **Who it is for and the problem it solves**.
   - **How it works**: the main parts and how they fit together. For a repo, include the tech stack and the layout of the important folders.
   - **What you can do with it**: main features and a typical way to use it or get started.
   - **Maturity and trust signals**: activity, license, maintainers, stars or users, last update. Report only what the page shows.
   - **Caveats**: limits, costs, and anything unclear.
5. Define any technical term the first time you use it. Keep it complete but not padded, and say plainly where the source did not give an answer.
