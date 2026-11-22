---
name: summarize
description: Summarize a local file in simple, easy-to-follow language, in a short or detailed mode. Use when the user gives a file path and wants it explained or summarized.
argument-hint: "<file-path> [short | detailed]"
---

Summarize this file: $ARGUMENTS

## Steps

1. Parse the arguments: the first value is the file path, the optional second value is the mode. The default mode is **short**. If no path was given, ask for one and stop. If the file does not exist, say so and stop.
2. Read the file by type:
   - Text, Markdown, code, logs, CSV, JSON: read it directly. For very large files, read the start, the end, and a spread of the middle, and say that you did.
   - PDF: read it with the Read tool, page ranges for long documents.
   - DOCX: extract the text with pandoc if installed, otherwise with Python's `docx` package or by reading `word/document.xml` from the archive.
   - XLSX: read it with pandas and openpyxl, and summarize the sheets and what the data shows.
   - Images and other binary files are out of scope. Say so instead of guessing.
3. Write the summary in plain, simple words. Explain any technical term the first time. Do not copy long passages, and do not add facts that are not in the file.
4. **Short mode**: a one-line TL;DR, followed by 3 to 5 bullets with the main points.
5. **Detailed mode**: a TL;DR, then a section-by-section explanation, the key points, important numbers, dates or names, any decisions or action items, and open questions or things that are unclear. For code, explain what it does, how the parts connect, and how to run it. For data files, describe the columns, row count, and notable patterns.
6. State the file name, type and size at the top, and say if you could only read part of it.
