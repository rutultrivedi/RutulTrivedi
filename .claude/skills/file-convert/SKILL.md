---
name: file-convert
description: "Convert a file between formats: PDF and DOCX, images (PNG, JPG, WebP, SVG), CSV, JSON and Excel, and Markdown and HTML. Use when the user wants to convert, export or change a file's format."
argument-hint: "<file-path> <target-format>"
disable-model-invocation: true
---

Convert a file. Arguments: $ARGUMENTS

## Steps

1. Parse the arguments into a source path and a target format (for example `report.docx pdf`). If either is missing or unclear, ask. Confirm the source file exists. If the format pair is not supported below, say so instead of improvising.
2. The output goes next to the original with the new extension. Never overwrite an existing file: if the name is taken, add `-1`, `-2` and so on. Never modify or delete the original.
3. Check which converters are installed before choosing one, using `Get-Command` for `pandoc`, `soffice` (LibreOffice), `magick` (ImageMagick) and `python`, and `python -c "import <module>"` for `pandas`, `openpyxl`, `PIL`, `docx`, `markdown`, `pypdf`. If a needed tool is missing, name it, say what it is for, and ask before installing anything. Prefer a tool that is already present.
4. Pick the method by format pair:
   - DOCX to PDF, and other Office to PDF: LibreOffice (`soffice --headless --convert-to pdf --outdir <dir> <file>`); fall back to pandoc if it has a PDF engine.
   - PDF to DOCX or text: text extraction only (pypdf or pandoc where it works). Warn that layout, tables and images may not carry over well, and that scanned PDFs need OCR, which this skill does not do.
   - Images (PNG, JPG, WebP, SVG): ImageMagick or Pillow. Warn when a conversion loses something (transparency to JPG, vector to raster). Ask for a size if the user mentions resizing.
   - CSV, JSON, XLSX: pandas with openpyxl. For JSON, state how nested data was handled (flattened or kept as text). Tell the user the sheet name used for Excel.
   - Markdown to HTML, DOCX or PDF, and HTML to Markdown: pandoc, or the Python `markdown` package for Markdown to HTML.
5. Run the conversion, then check that the output file exists and is not empty. For text-like outputs, glance at the start to confirm it is sensible.
6. Report the full output path, the size, the tool used, and any loss or caveat. If it failed, show the real error and what you would try next.
