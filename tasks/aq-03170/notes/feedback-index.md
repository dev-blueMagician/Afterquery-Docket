# Feedback index

Keep concise rows linking raw returns, current fixes and status. Raw platform words stay in
the linked artifacts/feedback notes; this index does not replace exact-content records.
Never edit submitted/accepted question files to maintain it.

## Active issues

Triage each exact tested version once. Key by bundle/question + platform version + issue;
record revision/fingerprint when established. Distinguish platform observations from the
author's inference. Categories: ambiguity, necessity, unsupported gold, form, difficulty,
identity. One mechanism per row is enough; use short phrases and links, not essays.

| Issue id / bundle / question | Tested platform version / rev / fingerprint | Category / mechanism | Raw feedback links / platform observation | Current version / author comparison or fix link | Status / next action |
| --- | --- | --- | --- | --- | --- |
| aq-03170-q01-F1 / aq-03170 / q01 | rev 0 presumed (tested_sha256 69b9929f...); screenshot shows no question text, identity not verified | form / (a) Reasoning tags not ticked or not saved on the page; (b) list answer with no order stated in the question | [q01-rev0-checks-2026-10-12.png](platform-feedback/q01-rev0-checks-2026-10-12.png): "Reasoning tags Failed" "Choose at least two reasoning tags"; "Answer format stated Warning ... advisory" "the question does not say what order to give them in"; user words "2 checks failed"; checks above and below the screenshot not seen | rev 1 (10c16cb0...): question orders the list by each commenter's second-letter date, gold reordered (IAA, MFA, Blockchain Association); (a) needs no content change, the file and JSON carry three tags | repaired/platform pending: tick and save the tags, paste rev 1, Re-run all; confirm whether the second failed check was the order warning |
| aq-03170-q01-F2 / aq-03170 / q01 | rev 1 (10c16cb0...): Question box shows rev 1's wording and the check quotes rev 1's gold; other fields not visible | ambiguity as the platform scores it (blocking) / the question did not say a letter counts when only another commenter mentions it, so both form solvers stopped at two names; plus form: order sentence not accepted, "second letter" flagged as a pointer | [question box](platform-feedback/q01-rev1-question-box-2026-10-12.png), [checks](platform-feedback/q01-rev1-checks-2026-10-12.png): "One defensible answer Failed", solvers "MFA, then Blockchain Association" and "Managed Funds Association (second earlier letter July 24, 2023), then Blockchain Association (second earlier letter October 27, 2023)."; "Answer format stated Warning"; "Each description fits one thing Warning ... 3 matches"; solver reasoning not shown (route unread) | rev 2 (1445e7fd...): counting rule stated ("including letters only others mention"), "List them alphabetically", gold alphabetical | repaired/platform pending: paste rev 2 and re-run; a second block on this point means changing the hook |
| aq-03170-q01-F3 / aq-03170 / q01 | rev 2 presumed (1445e7fd...) for question, answer, components; reasoning reworded by the user on the form | necessity (form check "Needs two or more documents") / the check rejects Doc 3 and Doc 13 as necessary without giving a route; neither commenter is named in any other letter; mechanism unresolved. F2's block is resolved by observed platform result: "One defensible answer Passed" | [reasoning box](platform-feedback/q01-rev2-reasoning-box-2026-10-12.png), [checks](platform-feedback/q01-rev2-checks-2026-10-12.png): "You marked documents 3, 13 as necessary, but the answer does not need them. Unmark them, or change the question so they are needed."; "Each description fits one thing Warning ... 3 matches" (the gold's own three) | rev 3 (bdafada1...): Doc 3 and Doc 13 unticked, kept as evidence; nothing else changed | repaired/platform pending: resolved by observed platform result: Run 1's document check found Doc 6 and Doc 8 needed |
| aq-03170-q01-F4 / aq-03170 / q01 | rev 3 (bdafada1...), platform Version bbce17: question quoted verbatim, gold equal, documents 6 and 8 removed in turn | difficulty / "In band — Medium tier", Low 0/5 · Medium 1/5; nine wrong attempts took each commenter's own account and never registered Doc 8's sentence; the right one re-read the others-mention clause. User: Medium slots full | [verdicts/AQ-03170_difficulty_2026-10-12_1700.txt](../verdicts/AQ-03170_difficulty_2026-10-12_1700.txt); the page's per-attempt "Final answer" and "Where it left your evidence" lines misstate the five low attempts (each lists both the Blockchain Association and MFA) | rev 4 (97502e9f...), target hard: clause replaced by "Judging by all these letters together"; answer and marks unchanged | open: form checks on rev 4, then one difficulty run; resolved by observed platform result: Run 2 (row F6) |
| aq-03170-q01-F6 / aq-03170 / q01 | rev 4 (97502e9f...), platform Version 4e9f31: change list equals rev 3 to rev 4, question quoted verbatim, gold equal, documents 6 and 8 removed in turn | difficulty / "In band — Hard tier", Low 0/5 · Medium 0/5 · High 1/5; fourteen wrong attempts on the own-account pair, one of them (High 1) after quoting the deciding sentence; submitted by the user at Hard | [verdicts/AQ-03170_difficulty_2026-10-12_2028.txt](../verdicts/AQ-03170_difficulty_2026-10-12_2028.txt) (sha256 07e85655c39d4364b61fd64f743714f6e1f898370ee31b24d4a86ff2e836915a) | q01 frozen at rev 4; later observations in [feedback-q01.md](feedback-q01.md) | returned by the reviewer on that point (row F7) |
| aq-03170-q01-F7 / aq-03170 / q01 | rev 4 (97502e9f...), the submitted version; the panel shows no version id and describes rev 4's marks ("only Docs 6 and 8") | necessity (reviewer) / two answer items each rest on one document that was not ticked; the form's own check had refused those ticks on rev 2 (row F3) | [q01-rev4-revision-requested-2026-10-13.png](platform-feedback/q01-rev4-revision-requested-2026-10-13.png) (sha256 1fdff716408e88cd18f8def8817d671e0b3d02b8084830ac43e8a2dcad89cd46): "Question and gold are sound ... The only fix is tagging Docs 3 and 13, which each uniquely support an answer item; then re-run the checks." | rev 5 (7bc64057...): Doc 3 and Doc 13 ticked as answer components; nothing else changed | repaired/platform pending: tick the two, re-run the checks, new difficulty run, capture before Submit; if "Needs two or more documents" refuses the ticks again, keep them and take the row to the reviewer |
| aq-03170-q01-F8 / aq-03170 / q01 | rev 5 (7bc64057...), platform Version a6c99b: question and gold quoted, change line "the documents or the documents marked necessary changed", documents 8, 6, 13, 3 removed in turn | difficulty / Medium where the user reports Medium full; the third medium solver (text not recorded) right twice under the three-solver gate, the two recorded medium solvers and four of five low attempts on the own-account pair | [AQ-03170_difficulty_2026-10-13_1511.txt](../verdicts/AQ-03170_difficulty_2026-10-13_1511.txt) (sha256 0b604e9e...): "In band — Medium tier", Low 0/5 · Medium 2/6 | no new revision: one unpointed step and no fair untested wording; sketches i04, i06, i02 screened | open: user quick-tests the sketches; the reviewer can be told that only the two requested ticks changed since the Hard run |
| aq-03170-q01-F5 / aq-03170 / q01 | rev 4 presumed (97502e9f...); question box not in the screenshot | form / (a) advisory "Each description fits one thing", 3 matches = the gold's three names, same issue as on rev 1-3 (rows F2, F3: not a new failure); (b) "Needs the documents" could not be run by the platform | [q01-rev4-checks-2026-10-12.png](platform-feedback/q01-rev4-checks-2026-10-12.png): "Warning ... advisory"; "Couldn't check" "Could not run this check — retry."; user words "two checks failed" | rev 4 unchanged: no content issue shown | open: retry the check, confirm "One defensible answer" on rev 4, then one difficulty run |

Statuses may be unresolved identity, open, repaired/platform pending, resolved by observed
platform result, historical, or redesign. A local repair is not a platform pass. Preserve
prior raw feedback and fixes through links when updating a row.

- Re-sent screenshots of the same version/issue link to the same row, with no new failure or
  return count. Compare the tested content with the current draft before changing it.
- Unknown versions get distinct receipt ids and stay unresolved. Do not group unrelated
  returns under a shared `unknown` key; merge only with evidence of the same tested version
  and issue, or an identical re-sent artifact. Never infer a current fingerprint from a qNN.
- Make one focused repair for a mechanism. If the same failure is demonstrated on that
  repaired exact version, redesign the hook; stale/duplicate/unknown feedback does not show
  recurrence. No automatic local model validation follows intake or repair.

## Next five newly promoted candidates

Use one owner index for the five-candidate trial, including if it spans bundles; link it from
other bundle sessions. Add each newly promoted candidate once. Resume/revision keeps its row;
a genuinely new hook promoted as a new candidate gets a new row. Do not enroll old candidates
retrospectively or reset the count when changing bundles. Stop enrolling after five.

- Trial owner index / start: [workspace owner](../../../notes/feedback-index.md); start recorded in the shared ledger
- Candidate rows used: 0 / 5

| Slot / bundle / candidate | Promoted date / question link | Actual authoring minutes / timing coverage | Reported tokens / coverage | Distinct platform attempts | Revision rounds | Ambiguity / necessity returns | Observed acceptance / raw link |
| --- | --- | --- | --- | --- | --- | --- | --- |

Record actual active candidate authoring/revision minutes as work happens, including any
already timed sketch work; exclude idle/platform waiting. Keep brief dated increments in the
minutes cell or a linked session note and mark coverage complete or partial/unknown. Never
estimate missed time afterward. A promotion does not make unrecorded earlier work known.
Revision rounds count distinct edits after first promotion, not duplicate screenshots or
resumptions. Count each distinct platform return once per applicable ambiguity/necessity
category, linked to its issue row; unknown identity stays uncounted/pending until resolved.
Acceptance records the actual platform observation (accepted, rejected or pending) with its
raw link; a difficulty pass or local repair is not acceptance. A candidate retired before any
submission is recorded as not submitted/retired: zero acceptances, no platform verdict claimed.
Retirement after submission does not settle a pending platform outcome.

- Summary: accepted TODO / enrolled TODO; known authoring minutes TODO; timing complete TODO
  of TODO; acceptance outcomes pending TODO; revisions TODO; ambiguity/necessity returns TODO.
- Accepted questions per known authoring hour: pending. Once all five have complete timing
  and settled outcomes (including retired before submission), compute accepted count / (total recorded minutes / 60), including
  time spent on unsuccessful candidates. No rate claim while either is incomplete or the
  denominator is zero; report known counts/minutes without treating partial time as a total.

## Measured events

Use the single workspace `notes/efficiency.json` ledger; this table links its report, rather than
maintaining a second set of totals. Start/stop timers and promote candidates through
`python tools/docket_agent.py efficiency` (WORKFLOW section 11). Keep stable candidate IDs across
work sessions and revisions. Do not enroll pre-existing questions or reconstruct their history.

For `record --event PATH`, save a JSON object with `kind`, a stable `event_id`, the bundle slug in
`bundle`, the tracked `candidate`, and `source` pointing to the actual trace/return/session evidence.
Add the fields below. Illustrative field names are a contract, not recorded measurements.

| Kind | Additional fields |
| --- | --- |
| `usage` | `total_tokens`: nonnegative integer reported by the runtime/API |
| `platform_attempt` | `attempt_id`: identified platform run; `stage`: `quality`, `difficulty` or `review`; `revision`: nonnegative integer; `tested_sha256`: verified prepared fingerprint |
| `revision` | `revision`: actual post-promotion revision number; `tested_sha256`: content fingerprint |
| `outcome` | `outcome`: `accepted`, `rejected`, `pending` or `retired_before_submission` |
| `coverage` | `timing` and `tokens`: each `complete`, `partial` or `unknown`; source explains coverage |

One usage event represents one non-overlapping reported usage interval/request; use its stable
receipt ID and do not record overlapping session and request totals. Missing usage stays unknown;
zero requires a reported zero. Do not substitute document-token counts or estimates. Repeated event
IDs with the same data are harmless; conflicting reuse is rejected. Duplicate identified runs or
revision snapshots do not increase counts. Keep unresolved run identity in feedback notes until known.

The `source` records provenance, not an independent verification of the supplied value. Acceptance
must be an observed platform outcome, not inferred from a difficulty pass. Confirm timing/token
coverage only when the measured records cover the relevant work; future work needs reconfirmation.
Stop timers before waits and turn end; discard an interrupted interval whose active time is unknown.
Unpromoted work and incomplete coverage remain visible. No metric triggers new model validation.
