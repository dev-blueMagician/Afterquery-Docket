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
| F1 / aq-02686 / q01 | Version bac61b (Run 1, Oct 10, 2026, 3:19 PM) / rev 1 / 2aa1d89ecd4f... (question quoted verbatim, "Your answer" $45,708, Docs 4 and 7 left out in the Document check) | difficulty / below target: one separating step, and the question printed its deciding share | [capture](../verdicts/AQ-02686_difficulty_2026-10-10_1539.txt): "In band — Easy tier", Low 3/5, Medium and High not run; closed-book and both documents needed; advisory "may be too vague" quoting the two wrong low answers. User: "passed easy tier but no open slot for easy" | rev 3 / 3c37e0b3ad5a... (rev 2 9c6a00148a1c... plus a two-word clarity fix; [q01](../questions/q01.md), Lever checks "What Run 1 showed" and "Repair in rev 2"): the three prospects replaced so both look-alikes need Doc 4's comment-response clarifications and a derived share; gold $45,602 | repaired in rev 2-3; superseded by F2 |
| F2 / aq-02686 / q01 | form quick test, version not shown / rev 3 / 3c37e0b3ad5a... assumed from the hand-over (user chat only, no panel) | difficulty / same hook after its one repair | user chat 2026-10-10: "too easy for quick test"; no raw artifact | q01 dropped ([Feedback log](../questions/q01.md)); round 2 sketch i03 in [ideas](ideas.md) changes the dependency structure (per-chemical, per-country notice bill) | closed for q01; i03 quick-tested, see F3 |
| F3 / aq-02686 / q02 | form quick test, version not shown / rev 0 / 1f910fbd56b1... assumed from the chat sketch (user chat only, no panel) | difficulty / first screen | user chat 2026-10-10: "quick test survived"; no raw artifact | [q02](../questions/q02.md) written up with the tested wording and gold $45,920 | open / run the form's checks and the difficulty check; send the tier line and panel verbatim |
| F4 / aq-02686 / q02 | form evidence check, no version shown / rev 0 / 1f910fbd56b1... (fields pasted by the user, reasoning reworded) | form / Evidence 12 (Doc 4) rejected as not word for word | user screenshot 2026-10-10: "Quote 12 does not appear word for word in document 4. Copy it exactly from the document." | local quote matches the capture exactly; live-page spacing or an altered paste suspected, unconfirmed ([q02 Feedback log](../questions/q02.md)) | closed in rev 1: the local evidence row was dropped (F5) |
| F5 / aq-02686 / q02 | Version a9ec06 (Run 2, Oct 10, 2026, 6:12 PM) / rev 0 / 1f910fbd56b1... (question quoted verbatim, "Your answer" $45,920; reasoning reworded by the user) | ambiguity / the question's phrase "Barring FEOCs" read as "FEOC status aside" | [capture](../verdicts/AQ-02686_difficulty_2026-10-10_1904.txt): "Answer not supported", Low 2/5; high model with every document $46,026 three times; closed-book needed the documents | rev 1 ([q02](../questions/q02.md), "What Run 2 showed", "Repair in rev 1"): "It refuses FEOC buyers. Orders: ..."; gold unchanged | repaired / quick-test first; every attempt in Run 2 completed each document step, so if the quick test says too easy, release the bundle |

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
- Candidate rows used: 0 / 5 (not enrolled: all five workspace slots were taken before this bundle; measured events for aq-02686 i01 are still recorded in the shared ledger)

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
