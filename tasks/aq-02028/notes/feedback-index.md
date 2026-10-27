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
| F1 / aq-02028 / q01 | platform version not visible; Question box text = rev 1 question exactly (47 words); other fields not shown | form / advisory "Question length spread" (pattern across the user's questions: "6 of them between 28 and 47 words") | [screenshot](platform-feedback/q01-rev1-question-box-length-advisory-2026-10-08.png); verbatim in [q01 Feedback log](../questions/q01.md) | first kept rev 1; the user re-sent the same advisory text (a re-send, not a new return), so rev 2 (cd1bad0a...) cut the question to 27 words; the user then preferred the original (F2), so rev 3 restores rev 1; re-captured on rev 3 with band "35 and 47"; user asked to keep everything else and shorten only the question: rev 4 (5007fa6a...) is 34 words | rev 4 still drew it (F3); q01 dropped. Closed; the user's rule since then: questions of about 12-20 words (q02 revs 1-2: 20) |
| F2 / aq-02028 / q01 | unresolved: user words after the rev 2 hand-over; no panel, tier line or run number, so not bound to cd1bad0a... | difficulty (reported, unverified): "too easy. the previous state was better" | user message 2026-10-08, verbatim in [q01 Feedback log](../questions/q01.md); no artifact | rev 3 restores the rev 1 wording exactly (tested_sha256 9a845dfe..., same as rev 1); gold and mechanism unchanged | open: ask for the panel text; if a platform run measured "too easy", record it and redesign the mechanism rather than reword |
| F3 / aq-02028 / q01 | Question box text = rev 4 exactly (34 words); quick test run on it per the user; panel not shown | difficulty (quick test "Too easy": the easier solver reached $117.39) and form (length advisory fires even at 34 words) | [screenshot](platform-feedback/q01-rev4-question-box-and-quick-test-2026-10-08.png); user words "and Too easy to pass quick test"; verbatim in [q01 Feedback log](../questions/q01.md) | second too-easy on the family (F2 rev 2, F3 rev 4): hook retired, q01 dropped; new hook i03 -> [q02](../questions/q02.md) rev 0 (9d1e4488...) | closed for q01; next: quick-test q02 |
| F4 / aq-02028 / q02 | Question box = rev 0 question (34 words); reasoning box = rev 0 with Steps 6-7 lightly reworded by the user, so not byte-bound to 9d1e4488... | form: length warning ("6 of them between 28 and 47 words, and this one is 34") and three reasoning-number flags (Steps 5-7: "Docs 1 and 8 don't mention 1.152 million / 0.822857 million / 329,000") | [screenshot a](platform-feedback/q02-rev0-question-and-reasoning-2026-10-08a.png), [screenshot b](platform-feedback/q02-rev0-question-and-reasoning-2026-10-08b.png); user: "it actually blocks our way when other tests all passed"; verbatim in [q02 Feedback log](../questions/q02.md) | rev 1 (1d3d4551...): 20-word question; 4 TEU scenario so every result is exact (gold 432,000 truck trips); each step a bare "a op b = r"; aq-01543's emulator reproduces the three rev 0 flags and finds none on rev 1 | repaired in rev 1; the reasoning box raised no new flag before the rev 1 difficulty run (F5), so closed for the form numbers |
| F5 / aq-02028 / q02 | platform difficulty check Run 1, 2026-10-08 1:39 PM, version cdda71 ("first run"); every attempt restates rev 1's question; gold "432,000 truck trips": rev 1 (1d3d4551...); ticks, reasoning and evidence not in the capture | difficulty: Too hard (Low 0/5 · Medium 0/5 · High 0/5) with "This question may be too vague"; ambiguity: "the port throughput [the terminal] states" also reads as the terminal's own throughput (Doc 1's 800,000 TEU, 9 of 15 attempts, 120,000); 5 took Doc 8's printed 450,000 (the declared trap); none used 2.88 million | [verdicts/AQ-02028_difficulty_2026-10-08_1348.txt](../verdicts/AQ-02028_difficulty_2026-10-08_1348.txt); verbatim verdict, Coach and trace summary in [q02 Feedback log](../questions/q02.md). Coach's "No document yields 432,000" is contradicted by Doc 1 L33 | rev 2 (c9e651b9...): "whole-port throughput" (20 words) and "as a whole, not VICT alone" in Step 2; gold, arithmetic, evidence and documents unchanged; Coach's 120,000 / 450,000 golds rejected (they are the declared traps) | repaired in rev 2, platform pending; next: user pastes rev 2 and runs the difficulty check (7 of 8 runs left); the same failure again retires the hook |

One difficulty-check return (F5, q02 rev 1: Too hard); no Checks returns yet (2026-10-08). Also one quick test (F3, q01) and one
form-field capture (F4, q02 rev 0). At intake the capture AQ-02028_2026-10-08_0734.txt showed no drafts, "Quick tests used: 0 of
10" and "0 runs". q02 rev 2 (tested_sha256 c9e651b9...) awaits its difficulty check.

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
- Candidate rows used: workspace slot 3 of 5 is this bundle's (i01, retired); the trial filled all five slots, so q02 (i03) is not enrolled

| Slot / bundle / candidate | Promoted date / question link | Actual authoring minutes / timing coverage | Reported tokens / coverage | Distinct platform attempts | Revision rounds | Ambiguity / necessity returns | Observed acceptance / raw link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3 / aq-02028 / i01 | 2026-10-08 / [q01](../questions/q01.md) (dropped) | unknown: no timer (another session's timer held the single global timer; not stopped by this session) | unknown (no usage report) | unknown (F2 report not identified as a run) | 4 (rev 1 polish; rev 2 length advisory; rev 3 restores rev 1; rev 4 shortens only the question at the user's request; ledger events -rev1-9a845dfe, -rev2-cd1bad0a, -rev3-9a845dfe, -rev4-5007fa6a) | 0 | retired before submission (ledger event aq-02028-i01-retired-2026-10-08) |

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

- Summary (this bundle, 2026-10-08): accepted 0 / enrolled 1; known authoring minutes unknown; timing complete 0
  of 1; acceptance outcomes pending 1; revisions 4; ambiguity/necessity returns 0. Workspace totals: run
  `python tools/docket_agent.py efficiency report`.
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
