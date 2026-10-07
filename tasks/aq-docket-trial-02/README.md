# Docket bundle template

A non-submittable starter. `/docket-new` copies it to `tasks/<slug>/`, removes
`questions/q00.md` from the copy, and fills `docs/` and `text/`.

```text
docs/                  the bundle's documents as received; never edited
text/                  Dnn.txt per document (=== page N === markers), Dnn.layout.txt for PDFs,
                       manifest.json mapping ids to files - regenerate with tools/extract_text.py
notes/doc-map.md       where things are in each document (bundle-mapper); navigation only
notes/hooks.md         cross-document hook inventory before wording
notes/ideas.md         lean sketch decisions and actual preliminary screen results
notes/sketches/i00.md  optional minimal sketch format, before full components/reasoning
notes/session.md       the checkpoint, replaced at each phase boundary
notes/intake.json      capture warnings, source hashes and recovered-capture history
questions/q00.md       the question format; copy it to qNN.md for each question you write up
runs/                 frozen field/corpus snapshots, isolated packets and actual raw returns
```

Nothing under `notes/` is submitted. From a question file, only the question, gold answer,
step-by-step reasoning, evidence passages, tags and documents reach the submission sheet,
through `python tools/check_questions.py tasks/<slug> --export`.

New questions default to difficulty_target: easy. Follow WORKFLOW.md v2.1: map readable sources,
find hooks and screen lean sketches before full write-up (the docket_agent.py screen helper is optional); run the floor,
prepare isolated packets with tools/docket_agent.py, obtain genuine independent checks and
an explicit exact-content platform pass before setting ready. Preparation does not run models.
