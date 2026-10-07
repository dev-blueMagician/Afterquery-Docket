---
name: docket-gpt-port
description: "gpt-project/ ports this workflow to GPT-6.1 Sol in ChatGPT projects (Writer, Solver, optional Review); it copies the gate, form checks, floor list and lessons, so it goes stale whenever those change."
metadata:
  node_type: memory
  type: project
  updated: 2026-10-04
  originSessionId: 2b1db9f7-7728-46d3-9d3f-86ff03c2072b
  modified: 2026-10-05T05:50:00.584Z
---

## V2 synchronization

The local and portable prompts now follow WORKFLOW.md v2: Easy minimum, independent shortcut
audit and exact-content platform evidence. Historical workflow section numbers below refer to
the former playbook and are no longer navigation links.

## Historical rule

`gpt-project/` runs this workflow on GPT-6.1 Sol in ChatGPT projects, built at the user's request
on 2026-10-04. `instructions.md` is the Writer project's instructions (keep it under 8,000
characters). `playbook.md` and `lessons.md` are its knowledge files. `solver-instructions.md` is for
a separate Solver project that holds only the bundle texts. `README.md` is the user's setup guide.
The port restates the gate (Q1-Q14, D1-D7), the form's quality checks, `check_questions.py`'s FAIL
and WARN list (playbook section 7) and the memory notes' current rules (lessons L1-L11).
GPT-written questions carry `origin: gpt`. By design, the floor WARNs on that origin (it is not in
ORIGINS) and export refuses it.

**Why:** the port is a copy, not a link. A change to the gate card,
`reference/platform-quality-checks.md`, `tools/check_questions.py` or a `docket-*.md` current rule
leaves the GPT project applying the old rule.

**How to apply:** whenever you change any of those, make the same change in
`gpt-project/playbook.md` or `lessons.md`, and in `instructions.md` if a hard rule changes. Keep
`instructions.md` under 8,000 characters, and tell the user to upload the changed files again. If
the user brings back lessons from GPT (playbook section 12 blocks), fold them into the matching
memory note as well. See [[docket-opus-ownership]] for the authorship rules the port mirrors.

## Evidence and history

- 2026-10-04: built from every source. An independent audit found eight gaps, all fixed before
  hand-over: memory that let blind solves see each other, a hand-run floor standing in for the
  script, a retyped sheet, components counted as list items, "Answer covers every ask" wording,
  field order, and dropped caveats.
