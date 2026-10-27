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
| P1 / aq-03120 / q01 | difficulty check Run 1, Version 2dbdc7 (current), Oct 11, 2026, 10:45 PM; rev 0, tested_sha256 ec5f8e4c... (question, gold and ticked documents verified from the capture; other boxes not captured) | difficulty / a dated event from another bank's submission (ANZ's April 2023 pilot) selecting the half whose growth no document prints: "In band — Easy tier", Low 1/5. All four wrong low attempts gave $0.6 billion. Author's reading of their full answers: three had placed the pilot in the second half and still returned the printed first-half figure, one never placed it (the platform's notes on attempts 1 and 4 say they failed to place it). Closed-book needed the documents; Docs 2, 3 and 4 each needed | [verdicts/AQ-03120_difficulty_2026-10-11_2321.txt](../verdicts/AQ-03120_difficulty_2026-10-11_2321.txt); user chat: "plz check arrived verdicts by using your feedback skill and fix" | q01 rev 1 (8ea00ff3...): the dating event is now Kiwibank's own first-half announcement (labelled first half, dated 23 February 2023, inside the second); Doc 2 dropped; gold and subtraction unchanged (questions/q01.md Lever checks) | superseded by P2: rev 1 was stopped by the form before any run |
| P2 / aq-03120 / q01 | form Checks on rev 1 (user screenshot 2026-10-12, run "33 min ago"); rev 1, tested_sha256 8ea00ff3... (question quoted in the failed check; gold named in the advisory) | form / "One defensible answer" Failed (block): its text places the announcement in the second half and then says the documents "do not explicitly state the second-half growth figure, leaving" (cut off). "Answer matches a stated figure" Warning (advisory): "Use it, or say in the question to compute it from the other figures" for Doc 3's $1.1 billion and Doc 4's $0.6b. Eight other visible checks passed. No run spent | [platform-feedback/checks-rev1-2026-10-12.png](platform-feedback/checks-rev1-2026-10-12.png); user chat: "two checks failed" | q01 rev 2 (4e4615e2...): same hook, documents and quotes; asks for a percentage of the year's growth on "Kiwibank's reported figures" (gold 45%, wrong half 55%), so a calculation is called for whichever half is picked (questions/q01.md Lever checks) | superseded by P3: rev 2 was blocked by the same check, with both solvers on 55% |
| P3 / aq-03120 / q01 | form Checks on rev 2 (user screenshot 2026-10-12, run "16 min ago"); rev 2, tested_sha256 4e4615e2... (gold "45%" named in the failed check) | ambiguity as the form scores it / "One defensible answer" Failed (block): "two independent solvers ... did not reach your gold \"45%\". Both answered \"55%\"." Both took the first half for "the half in which it announced first-half results". "No single passage gives the answer" Warning (advisory): "Doc 4 on its own may give enough to compute the answer" (it prints no full-year figure). "Answer matches a stated figure" Passed. No run spent | [platform-feedback/checks-rev2-2026-10-12.png](platform-feedback/checks-rev2-2026-10-12.png); user chat: "two checks failed" | q01 rev 3 (4bfe9546...): the announcement is dropped as the dating event after two blocks; the half is named by ANZ's Simple Switch pilot again (Run 1's event, Docs 2, 3, 4), asked in rev 2's percentage form, gold 45% (questions/q01.md Lever checks) | superseded by P4: rev 3 was too easy at the quick test |
| P4 / aq-03120 / q01 | form quick test 2026-10-12; wording taken as rev 3 (4bfe9546...), assumed, panel not pasted | difficulty / the measured dating event (ANZ pilot) asked as a percentage on "reported figures": the easier solver reached 45% | user chat: "too easy for quick test" (questions/q01.md Feedback log) | none on q01: dropped. Against rev 0 (same event, dollar amount, no call for a calculation: quick test survived, then Low 1/5) the only change is the form of the ask, so the unprompted subtraction was the holding step. Sketch i07 keeps rev 0's form with a heavier dating step | historical: q01 dropped after four versions. i07 offered for a quick test only; if it does not survive, the hook is closed |
| P5 / aq-03120 / q02 | difficulty check Run 2, Version cf8658 (current), Oct 12, 2026, 2:35 PM; rev 0, tested_sha256 a4f09e88... (question quoted 13 times, gold shown, platform diff names only the question; ticked documents not shown) | unsupported gold as the gate scores it / "Answer not supported": Low 0/5 · Medium 2/5 (the Medium band) but the high model with every document gave $0.6 billion three times. Author's reading of the traces: one high attempt took the December 2022 half; one derived $0.5 billion and dropped it ("this is a calculation, not stated directly"); one saw the June 2023 half was last completed, found no figure for it and chose "completed and reported". Low and medium misses: the half with its own half-year results taken as the last completed one | [verdicts/AQ-03120_difficulty_2026-10-12_1447.txt](../verdicts/AQ-03120_difficulty_2026-10-12_1447.txt); user chat: "plz check arrived verdicts by using your feedback skill and fix" | q02 rev 1 (64ce77d2...): the question adds "stated or implied"; nothing else inside the fingerprint changes (questions/q02.md Lever checks) | superseded by P6: rev 1 was too easy at the quick test |
| P6 / aq-03120 / q02 | form quick test 2026-10-12; wording taken as rev 1 (64ce77d2...), assumed, panel not pasted | difficulty / "stated or implied" added to rev 0's question: the easier solver reached $0.5 billion | user chat: "too easy for quick teset" (questions/q02.md Feedback log) | rev 0 and rev 1 bracket the wording: with no licence the high model read "financial half-year" as the interim reporting period and the gate failed; with a licence the easier solver solves it. Sketch i08 names the half as "the half of its financial year that last ended before" the announcement, which has one reading, and adds no licence | historical for rev 1. i08 survived its quick test (user chat 2026-10-12) and became q02 rev 2 (e0d20bd4...): resolved by P7 |
| P7 / aq-03120 / q02 | difficulty check Run 3, Version 6243da (current), Oct 12, 2026, 5:22 PM; rev 2, tested_sha256 e0d20bd4... (question quoted 37 times, gold shown, platform diff names only the question, Document check left out Docs 3 and 4) | difficulty / "In band — Medium tier": Low 0/5 · Medium 2/5; closed-book needed the documents; high model reached the gold on its second every-document attempt; Docs 3 and 4 each needed. Advisory, non-blocking: "This question may be too vague: several solvers agreed on an answer that is not your gold" ($0.6 billion) | [verdicts/AQ-03120_difficulty_2026-10-12_1742.txt](../verdicts/AQ-03120_difficulty_2026-10-12_1742.txt); user chat: "submitted as medium tier. plz check arrived verdicts by using your feedback skill and upgrade your skill" | none needed: q02 rev 2 is the submitted content (questions/q02.md, frozen) | resolved by observed platform result: Medium pass, submitted 2026-10-12; acceptance pending; later observations in [feedback-q02.md](feedback-q02.md) |

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

- Summary: accepted 0 / enrolled 0 in the five-slot trial (all five slots were taken by earlier bundles; this
  bundle's work is tracked as unpromoted: candidate i01, one sketch interval of 27.6 minutes on 2026-10-11, mapping
  and reading before it unmeasured, so timing is partial); three difficulty attempts recorded (Run 1 on q01, Easy, below target; Run 2 on q02 rev 0, gate failed; Run 3 on q02 rev 2, Medium, submitted); acceptance outcomes pending 0; revisions 3 (q01 rev 1, rev 2, rev 3);
  ambiguity/necessity returns 0.
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
