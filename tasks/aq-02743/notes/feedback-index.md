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
| P1 aq-02743 / q01 | quick test, version unknown / rev 0 / 9592e345... (binding unverified) | difficulty / h3: delayed-schedule benefits minus costs, DOJ over HHS, 524% | user chat 2026-10-10 "q01 i05 too easy, i04 survived, i06 not tested"; no panel or trace | [q01](../questions/q01.md) Feedback log | historical: q01 dropped unsubmitted, h3 closed, no repair |
| P2 aq-02743 / i05 | quick test, version unknown / sketch only | difficulty / h5: procurement-contract exclusion, 351 days | same chat message | [sketches/i05.md](sketches/i05.md) | historical: dropped, h5 closed |
| P3 aq-02743 / i04 -> q02 | quick test, version unknown / q02 rev 0 = 5791249d... (binding unverified) | difficulty / h4: first binding deadline from HHS's effective date, 354 days | same chat message: "survived" (one draw) | [q02](../questions/q02.md), [hand-over](handover-q02.md) | historical: rev 0 superseded (row P4) |
| P4 aq-02743 / q02 | form Checks, version id not visible / rev 0 / 5791249d... (matched by the check's quoted answer and evidence) | ambiguity / "must it first meet" left the choice between two rules' dates to the solver | [screenshot](../verdicts/AQ-02743_q02-r0_form-checks_2026-10-10.png), [transcript](../verdicts/AQ-02743_q02-r0_form-checks_2026-10-10.txt): "One defensible answer" Failed; advisories "No single passage gives the answer", "Answer matches a stated figure" | q02 rev 1 = 73c6cbf6... ("does any federal rule first require it"); alternate q03 rev 0 = d0212279... | resolved by observed platform result on q03 rev 0 (row P5: the stated condition was accepted and the run went ahead); q02 rev 1 itself untested |
| P5 aq-02743 / q03 | difficulty Run 1, Version 90fd80 / rev 0 / d0212279... (22 verbatim quotes of the question, gold 350 days, documents 3 and 4 left out in the Document check) | difficulty / h15: one county's gain from HHS's rule before any federal rule bound it | [capture](../verdicts/AQ-02743_difficulty_2026-10-11_1011.txt): "In band — Easy tier", Low 3/5, "You can submit now."; closed-book and Document check passed. Low wrong x2: 0 days ("DOJ's date controls"); declared traps 365 and 367 caught no one | q03 rev 1 = 22572844... (four counties, one per tier combination, total 1,067 days) | historical: the repair failed its quick test (row P6); rev 0's Easy pass stands on the restored content |
| P6 aq-02743 / q03 | quick test, version unknown / rev 1 / 22572844... (binding unverified) | difficulty / h15 widened to four counties, total 1,067 days | user chat 2026-10-11 "too easy to pass quick test"; no panel or trace | [q03](../questions/q03.md) Revision history and Feedback log; rev 1 lever checks in [q03-rev1-lever-checks.txt](q03-rev1-lever-checks.txt) | redesign not available: family h15/h4 closed for Medium after an Easy result and a too-easy repair; decision returned to the user (Easy slot or release) |
| P7 aq-02743 / q03 | form Checks, version id not visible / rev 0 / d0212279... (matched by "your answer has 350", quoted evidence rows and two checks dated at Run 1's time) | form / three advisories on the measured content | [screenshot](../verdicts/AQ-02743_q03-r0_form-checks_2026-10-11.png), [transcript](../verdicts/AQ-02743_q03-r0_form-checks_2026-10-11.txt): "No single passage gives the answer", "Answer matches a stated figure" (11, 24), "Each description fits one thing" ("50,000 or more people", 2 matches), all "advisory"; user: "can't check difficulty" | no change: Run 1's Document check found both documents needed; the day numbers and the two tier matches are noise; the version already has its final difficulty result | open: user's decision (submit at Easy or release); the top of the Checks list and the footer were not captured |

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
- Candidate rows used: trial full before this bundle (five slots enrolled in the shared ledger); aq-02743 work is timed there as unpromoted (i01 sketch, i03 draft)

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
