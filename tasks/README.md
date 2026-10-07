# Tasks

Each document bundle gets its own self-contained directory:

```text
tasks/<bundle-slug>/
  docs/        the bundle's documents, unchanged
  text/        extracted text (Dnn.txt) and manifest.json, from tools/extract_text.py
  notes/       doc-map.md, ideas.md, session.md - working memory, never submitted
  questions/   qNN.md - one question per file, form fields plus evidence and checks
```

Start a bundle with `/docket-new <slug> <path to documents>`, which copies
`template-task/` and extracts the text. Never copy another bundle's directory.
Submission sheets are generated into the repository-level `dist/` directory.
