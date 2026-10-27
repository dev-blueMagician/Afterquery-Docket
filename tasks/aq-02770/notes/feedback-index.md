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
| F1 / aq-02770 / q01 | Version 6f4ab4 (Run 1, Oct 11, 2026, 10:32 AM) / rev 1 / 7df56a5808a0... (question quoted verbatim, "Your answer" 76.0 percent, Docs 2 and 4 left out in the Document check; reasoning and evidence fields not shown in the capture) | difficulty / below target: the date anchor named Doc 2's own determination, so three low attempts read its publication date and the "until January 1, 2023" rule together; the re-weighting step separated no one (5 of 5 low) | [capture](../verdicts/AQ-02770_difficulty_2026-10-11_1119.txt): "In band — Easy tier", Low 3/5, Medium and High not run; closed-book needed the documents (78.7%); every document reached 76.0; without Doc 2 77.0 twice, without Doc 4 76.5 twice. Both wrong low attempts answered 77.0 (81 base). User: no Easy slot on this bundle; "check arrived verdicts ... and fix" | rev 3 / df6c090d374a... ([q01](../questions/q01.md), Lever checks "What Run 1 showed" and "Repair in rev 2 and rev 3"): one change, the anchor is now the day DOE held its public webinar on the proposal to create TE2 (March 29, 2022, dated only in the TE2 documents; rev 2's proposal date also sits in Doc 2 and was never pasted); gold 76.0 and ticked documents unchanged. Local: full solves matched on rev 2 and rev 3; without Doc 2 a solver committed to 77.0. q03 (no-what-if alternate) dropped: its second source was "Doc 3 or Doc 4" | resolved by observed platform result: the repair was measured in F2 and failed in the other direction |
| F2 / aq-02770 / q01 | Version cf23fa (Run 2, Oct 11, 2026, 6:20 PM) / rev 3 / df6c090d374a... (the page's change list is the rev 1 to rev 3 edit, question quoted verbatim, "Your answer" 76.0 percent; no Document check ran) | difficulty / same hook after its one repair: with a plain pre-2023 date the low model looked up the minimum for that date every time (5 of 5 took 80) | [capture](../verdicts/AQ-02770_difficulty_2026-10-11_1829.txt): "Too easy", Low 4/5; closed-book needed the documents (79.0%); the one miss was 76.8 (4.0 points applied as a relative 4 percent); "No specific changes were suggested for this version" | q01 dropped ([Feedback log](../questions/q01.md), Lever checks "What Run 2 showed"); no third wording, as recorded before the run | closed for q01 / q02 followed, see F3 |
| F3 / aq-02770 / q02 | form quick test, version not shown / rev 0 / ae2d8fd247cd... assumed from the hand-over (user chat only, no panel) | difficulty / first screen: member-level matching across three commenter tables | user chat 2026-10-11: "too easy for quick test"; no raw artifact; whether sketch i04 was also tested is not stated | q02 dropped ([Feedback log](../questions/q02.md)); i04 is the same mechanism on two tables | closed / three rounds used, no Medium design found: recommend release, or the Easy result of q01 rev 1 if that slot is usable |

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
