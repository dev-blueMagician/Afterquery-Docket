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
| aq-02501-q01-N1 / aq-02501 / q01 | rev 0 presumed (tested_sha256 e23be069...); screenshot shows no question text, identity not verified | necessity (closed-book) / VA side = public 38 CFR 3.12 text (general binding, entry-level considered other than dishonorable) | [q01-rev0-checks-2026-10-09.png](platform-feedback/q01-rev0-checks-2026-10-09.png): "Needs the documents Failed", "Answerable without the documents"; advisory "Each description fits one thing" warning | rev 1 (3c537469...): VA side moved to the 2024 rule's own effect statements (dropped from the rolls "favorably impacted"); local closed-book probe misses (OTH + special-court-martial BCD) | resolved by observed platform result: rev 1's difficulty Run 1 closed-book check "Needed the documents ✓" (row N2) |
| aq-02501-q01-N2 / aq-02501 / q01 | Run 1, Version f1d195 (Oct 9, 2026, 4:58 PM) = rev 1 (3c537469...) for question, answer, documents | necessity / Doc 5 only confirms that uncharacterized (dropped-from-the-rolls) separations are in the board's set; the without-Doc-5 high attempt assumed it | [verdict file](../verdicts/AQ-02501_difficulty_2026-10-09_1737.txt): "A marked document may not be needed", Low 0/5 · Medium 2/5 · High —, closed-book "Needed the documents ✓" | no content change; reviewer note for Doc 5 (190 chars): "Doc 5 needed: only its DARB definition counts uncharacterized separations as less than honorable, admitting dropped-from-the-rolls ones; usual usage (OTH, BCD, dishonorable) leaves them out." | note saved (capture [17:59](../verdicts/AQ-02501_difficulty_2026-10-09_1759.txt): "That allows submit, but an admin must sign it off (waive the check for this content)", "+$20 Medium+ bonus if accepted"); submitted 2026-10-09 (user) at Medium; admin waiver and acceptance pending, later observations in [feedback-q01.md](feedback-q01.md); reviewer did not accept the note (row N3, 2026-10-10); historical |
| aq-02501-q01-N3 / aq-02501 / q01 | reviewer return on the submitted rev 1 (Version f1d195, 3c537469...); "Show what you submitted" not expanded, bound as the only submission | necessity (reviewer) / Doc 5's less-than-honorable set is every characterization but honorable, so it excludes nothing from Doc 3's list | [screenshot](platform-feedback/q01-rev1-revision-requested-2026-10-10.png), verbatim in [feedback-q01.md](feedback-q01.md): "Sent back for revision", "Only document 3 is necessary. Ensure at least two docs are necessary for the solver to get the "gold answer"." | rev 2 (e0593b76...): first ask unchanged, second ask added whose value only Doc 5 states (discharge-date eligibility test, December 20, 2019), fourth component, two Doc 5 evidence rows | resolved by observed platform result: Run 2, Version 432875 = rev 2, "In band — Medium tier" (Low 0/5 · Medium 1/5), document check "Needed document 3 ✓" and "Needed document 5 ✓" ([capture](../verdicts/AQ-02501_difficulty_2026-10-10_2103.txt)); resubmitted 2026-10-10 (user); reviewer outcome and acceptance pending in [feedback-q01.md](feedback-q01.md) |

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
