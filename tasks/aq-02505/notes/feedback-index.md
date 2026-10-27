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
| f1 / aq-02505 / q01 | form paste 2026-10-09; rev 0 fields with Steps 8-9 reworded by the user; Steps 1-7 not visible, not bound to 2917dbde... | form / reasoning number check on totals that Doc 2 and Doc 6 print only in words, late in the text ("One hundred and seven" at character 36,837; "One hundred and eighty-seven" at 39,816) | [form-screenshot-1.png](../runs/q01-r0-form-2026-10-09/form-screenshot-1.png): "Step 1: Doc 2 doesn't mention 107. Check the document number." / "Step 7: Doc 6 doesn't mention 187. Check the document number."; Step 2's 5 and 25 and Steps 4-6, 8-9 unflagged | rev 0 unchanged: no wording clears them, because every route to the base or end count needs a list total printed only in words (q01 Feedback log). Same screenshot re-sent 2026-10-09 with the user's "Don't make such mistakes anymore" (no new return); the floor (tools/form_numbers.py) reproduces both and reports them as expected false alarms, since evidence quotes 5 and 7 hold the spelled-out totals | resolved: the user knew both were wrong warnings ("this time, it is not your fault", 2026-10-09); q01 kept unchanged; next: quick test |
| f2 / aq-02505 / q01 | difficulty Run 1, Version 95fd92, Oct 9, 2026, 4:11 PM = rev 0 (2917dbde...), bound by question, gold and documents (user-reworded reasoning Steps 8-9 are not read by the check) | difficulty / landed Easy below the medium target: 4 of 5 low-model attempts took Doc 2's 30 named additions as new (base 77, 142.9%); the right one counted Doc 2's lists after Doc 4's 107 + 39 = 144 mismatch; every attempt found the base edition by matching the question's "November 1, 2024" to Doc 2's supersession sentence | [verdict](../verdicts/AQ-02505_difficulty_2026-10-09_1639.txt): "In band — Easy tier", "Low model: 1 of 5 attempts right (the question landed here)", "2 of 5 gave the same wrong answer: “**142.9%**”"; closed-book 84.6% (recalled ~78 on Nov 1, 2024); Document check: Doc 2 and Doc 6 both needed | rev 1 f58099e1...: start date November 15, 2024, printed nowhere, so the base edition must be placed (Doc 2's 107 dates from November 25); gold, documents and Daqo step unchanged; one focused repair | repaired; rev 1 measured Too hard (f3) |
| f3 / aq-02505 / q01 | difficulty Run 2, Version 4200aa, Oct 9, 2026, 5:09 PM = rev 1 (f58099e1...; the page: "question: removed “1,”; added “15,”") | difficulty / overshoot: the bare "November 15, 2024", printed nowhere, was read as a typo for November 25 by all 5 high, 2 medium and 2 low attempts (107 as base, 74.8%); the other 6 placed it in the November 1 version and missed Daqo (142.9%) | [verdict](../verdicts/AQ-02505_difficulty_2026-10-09_1719.txt): "Too hard", "Low 0/5 · Medium 0/5 · High 0/5"; Coach "Make it solvable" (misreads the November 1 count as unavailable); closed-book 84.6%; Docs 2 and 6 needed | rev 2 36ff520a...: "the list in force on November 15, 2024" (date kept, intent stated); one focused repair for this distinct failure | repaired; rev 2 measured Easy (f4) |
| f4 / aq-02505 / q01 | difficulty Run 3, Version 0b7d6e, Oct 9, 2026, 11:46 PM = rev 2 (36ff520a...) | difficulty / repeat of f2: with the date's intent stated, every low attempt placed it; 3 of 5 missed Daqo (142.9%), 1 cleared it, 1 miscounted (251.2%) | [verdict](../verdicts/AQ-02505_difficulty_2026-10-10_0019.txt): "In band — Easy tier", "Low model: 1 of 5 attempts right (the question landed here)"; closed-book 34.6%; Docs 2 and 6 needed | none: the family lands Easy (Low ~1 in 5 clears Daqo) or Too hard (harder anchor); medium missed Daqo 3/3, so no wording separates medium from low | redesign: q01 dropped; new hooks searched with two independent question-author agents (2026-10-10) |
| f5 / aq-02505 / q02 | difficulty Run 4, Version b94f39, Oct 10, 2026, 2:35 AM = rev 0 (ae90f7cd...) | difficulty / new mechanism (directed "first placed" exclusion, one member per notice), same landing: 2 low attempts included Ashele, 2 were incomplete, 1 cross-checked the appendices and was right | [verdict](../verdicts/AQ-02505_difficulty_2026-10-10_0256.txt): "In band — Easy tier", "Low model: 1 of 5 attempts right (the question landed here)"; closed-book wrong; Docs 2, 4 and 6 all needed | none: three of four runs settled at exactly Low 1/5 across two mechanisms; the low model's thorough attempt (about 1 in 5) clears any fair cross-check here | redesign by the user's choice ("option 3", 2026-10-10): q02 dropped; q03 rev 0 e2278b31... widens to copper or lithium (five names, two added mentions-vs-does decoys), platform pending |
| f6 / aq-02505 / q03 | difficulty Run 5, Version 704f4c, Oct 10, 2026, 4:17 AM = rev 0 (e2278b31...; the page's change list matches q02 -> q03) | difficulty / between levels: the medium model took each notice's "adds" sentence as first placement (Ashele in four printed final answers; attempt 2 never read Doc 4's (v) descriptions) and the high model checked Doc 2's list every time (5 of 5 right); low 0 of 5 (three with Ashele, two truncated) | [verdict](../verdicts/AQ-02505_difficulty_2026-10-10_0750.txt): "Between levels", "Too hard for the medium model but too easy for the high model. Make it a little harder, so the high model reaches your answer only some of the time", "Low 0/5 · Medium 0/5 · High 5/5"; Coach: full legal names, one more near-miss (its example, Xinjiang Zijin Nonferrous, smelts zinc); closed-book wrong | q04 rev 0: the same set asked as a percentage of all entities first placed in the window (5 of 109, 4.6%), so two independent already-listed checks must both be cleared (Ashele in the set, Daqo in the base); one focused repair | repaired; q04's quick test was "too easy" (f7) |
| f7 / aq-02505 / q04 | form quick test, 2026-10-10; q04 by the user's naming, no panel or version, so not bound to e5563dcd... | difficulty (preliminary) / the low model reached 4.6% with both already-listed checks stacked; route unseen | user chat (verbatim): "q04 too easy for quick test"; no raw artifact | none: q04 was the one focused repair for f6; with a hidden already-listed check the low model clears it in some attempts, the medium model never, the high model always (Easy or Between levels); without one the low and medium models read the notices alike (Run 5, Ashele aside: 2 of 5 each) | redesign exhausted (hooks.md rounds 1-4): decision returned to the user; q04 dropped, 5 difficulty runs unspent |

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
