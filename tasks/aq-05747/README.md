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
notes/feedback-index.md concise version/issue triage and the prospective five-candidate trial
notes/intake.json      capture warnings, source hashes, the task page's Doc numbers, capture history
notes/handover-qNN.md  every form field, ready to paste (tools/check_questions.py --handover)
notes/platform-checks-qNN.json  saved Checks history with explicit revision/fingerprint binding
notes/platform-checks/qNN/     preserved raw Checks captures; no local model validation
questions/q00.md       the question format; copy it to qNN.md for each question you write up
questions/qNN.json     generated form input values only, alongside the source Markdown
runs/                 frozen fields and one corpus copy, actual platform returns;
                      isolated local diagnostic packets only when explicitly needed
```

Nothing under `notes/` is submitted. From a question file, only the form's fields reach the hand-over
and the submission sheet, in the form's order: question, number of asks, gold answer, step-by-step
reasoning, answer components, evidence, necessary documents with their roles, reasoning tags and
targeted failure modes. `python tools/check_questions.py tasks/<slug> --handover --q qNN` writes
`notes/handover-qNN.md` for any live question, with the task page's Doc numbers; `--export` writes the
same fields for ready user-origin questions to `dist/<slug>.md`.

## JSON input values

`--handover` also generates `questions/qNN.json` when the floor is clean and all fields/mappings
are encodable. To generate only JSON without question validation or changing Markdown:

```powershell
python tools/check_questions.py tasks/<slug> --json --q qNN
```

The UTF-8 object contains only these form inputs:

| Key | Value |
| --- | --- |
| `question` | Question text |
| `number_of_asks` | Integer 1 or 2 |
| `gold_answer` | String preserving units, signs and decimal precision |
| `step_by_step_reasoning` | Reasoning text with step/newline structure preserved |
| `answer_components` | Array of strings in form order |
| `evidence` | Array of `{document_number, component_number, quote}`; numbers start at 1 |
| `necessary_documents` | Array of `{document_numbers, role, reviewer_note}` groups |
| `reasoning_tags` | Array of selected exact option labels |
| `targeted_failure_modes` | Array of `{trap, how_a_careless_solver_fails}`, one per declared mode (1-3) |
| `why_these_are_traps` | The form's one shared reason for all modes, at most 50 words (since 2026-10-08; it replaced the three per-mode boxes) |

Doc numbers come from intake, not the digits of local Dnn ids. Evidence referencing several
components becomes one row per component. In each necessary-document group, tick every listed
document; the first is the anchor and remaining numbers are its "or..." alternatives. Roles,
tags, traps and causes use the form's display labels. Selected arrays describe the complete intended
selection, so an importer should replace existing rows/selections rather than append to them.
No local IDs, notes, origin, statuses, hashes, diagnostics or authorship confirmations are exported.

Missing mappings or required inputs stop JSON generation; existing JSON is left unchanged and
reported as not refreshed. Regenerate successfully after every source-question edit. Explicit
`--q` may serialize a frozen question without editing it; bulk generation skips frozen questions.
The existing `--export` submission-sheet rules remain separate. JSON generation runs no models
and makes no readiness, submission or authorship claim.

## Authoring workflow

New questions default to difficulty_target: hard (since 2026-10-14; the lowest tier the user names as
open, if lower). Design by .claude/memory/reference/hard-playbook.md and screen Hard sketches first. Follow WORKFLOW.md: map readable sources,
find hooks and screen lean sketches before full write-up (the screen helper is optional).
Verify arithmetic/date results, run `python tools/docket_agent.py prepare tasks/<slug> --q qNN`
to freeze fields and one corpus copy, then run the mechanical preflight/full handover once.
`checked` means preflight done/platform pending; `ready` requires a clean floor and a recorded
exact-content platform pass at/above target in `## Platform validation`.
Track the 39 Checks separately with `docket_agent.py record-checks tasks/<slug> --q qNN
--capture PATH --revision N --tested-sha256 HASH` only after verifying which prepared content
the capture tested. `report` and handover distinguish difficulty readiness from recorded platform
clearance. Missing/stale blocking results and explicit submission blockers leave clearance pending;
advisories stay advisory. No saved capture establishes platform acceptance or authorship.

No default local model validation or tier prediction. Optional diagnostics need an explicit
request or concrete unresolved issue; `prepare --local-checks` creates their isolated packets
and scope binding. Missing/stale local records do not require fresh solves. Known gaps need a
substantive author assessment or supplied platform evidence tied to the candidate and gap hashes.

Triage feedback once by bundle/question, exact tested platform version and issue. Preserve raw
returns, keep local inference separate, and compare the current fix before revising again.
Unknown versions remain unresolved; do not merge unrelated unknown returns. Make one focused
repair per mechanism, then redesign if that failure recurs on the repaired exact version.
Keep submitted/accepted question files unchanged and link their separate feedback notes.

Use one notes/feedback-index.md owner for the next five newly promoted candidates, even across
bundles, and link it from each session. Record actual authoring minutes, revisions, deduplicated
ambiguity/necessity returns and observed acceptance there. Resume/revision reuses the row; no
retrospective timing estimates. Report acceptance per known authoring hour only after timing
and acceptance outcomes are complete. These are short author records, not extra model checks.
Workspace `notes/feedback-index.md` is the shared owner, with `notes/efficiency.json` as the
measurement ledger. `python tools/docket_agent.py efficiency report` shows measured phase time,
reported tokens and coverage, distinct platform attempts/revisions, and observed outcomes.
Use start/stop and source-backed record events as described in WORKFLOW section 11; stop before
platform waiting or yielding a turn. Missing measurements stay unknown. JSON form inputs remain
free of telemetry and question/source files stay unchanged.
