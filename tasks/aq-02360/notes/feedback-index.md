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
| F1 / aq-02360 / i01 -> q01 | quick test of sketch i01 (question + answer only), before promotion; q01 rev 0 has the same question and answer (tested_sha256 6f8b3e9c...) | difficulty screen / superseded draft (95(2A)) | user, 2026-10-09: "both of i01 and i02 survived quick test" (no screenshot; low-model answer not captured) | q01 rev 0 checked, 0 FAIL | preliminary only; next: form free checks, then a difficulty run on rev 0 exactly |
| F2 / aq-02360 / i02 -> q02 | quick test of sketch i02 (question + answer only), before promotion; q02 rev 0 has the same question and answer (tested_sha256 371d27d4...) | difficulty screen / exclusive end date (574) | same user message as F1 | q02 rev 0 checked, 0 FAIL | preliminary only; next: form free checks, then a difficulty run on rev 0 exactly |
| F3 / aq-02360 / q01 | rev 0 (tested_sha256 6f8b3e9c...; binding by the user's context, panel shows no question text) | general knowledge / gold guessable closed-book | notes/platform-feedback/q01-rev0-checks-2026-10-09.png: "Needs the documents Failed" "Answerable without the documents ..."; advisory "No single passage gives the answer" "Doc 1 on its own may give enough to compute the answer."; "Needs two or more documents" and "One defensible answer" passed | rev 1 (tested_sha256 fff19017...): gold adds regulation 142(4), which cannot be named closed-book | repaired, platform pending; next: free checks and a quick test on rev 1 |
| F4 / aq-02360 / q01 | rev 1 (tested_sha256 fff19017...; question and gold visible in the screenshot) | form / list-order advisory | notes/platform-feedback/q01-rev1-question-box-2026-10-09.png: orange "The answer lists several items, but the question does not say what order to give them in ..." ("only a warning and does not block submitting") | rev 2 (tested_sha256 ac260ba1...): adds "Give them in that order." | repaired, platform pending; next: full checks + quick test on rev 2 |
| F5 / aq-02360 / q02 | platform "Version 6009d1", Run 1, Oct 9 2026 5:26 AM; tested question (verbatim from attempts) "In how many days since the opening of the 2023 remedy consultation was the last day for submitting opted-out elections?", gold "573 days": the user's paraphrase of rev 0, so not bound to rev 0 (tested_sha256 371d27d4...) | difficulty / exclusive end date | [raw](../verdicts/AQ-02360_difficulty_2026-10-09_0531.txt): "The difficulty check finished: Between levels." "Low model: 0 of 5 attempts right" "Medium model: 4 of 5 attempts right"; advisory "This question may be too vague ... '574'". Traces: low 5/5 = 574 (6 March 2023 to 30 September 2024); medium 4/5 = 573 (29 September), 1/5 = 574. Coach blames an endpoint convention and calls 30 September the last day; the per-attempt notes say "did not apply the rule that 'before 30 September 2024' excludes that date" | rev 1 (tested_sha256 a1fc3019..., checked, 0 FAIL): start anchor becomes the last union meeting (4 May 2023, Doc 4), end unchanged (29 September 2024, Doc 3): 514 days; wording keeps "How many days after" | repaired, platform pending; next: paste rev 1 verbatim (precision words), free checks, quick test, difficulty run |
| F6 / aq-02360 / q01 | rev 2 (tested_sha256 ac260ba1..., as handed over; binding by user report) | difficulty / tied superseded-draft trap | user, 2026-10-09: "q01 too easy" (quick test presumed; no screenshot) | rev 2's paragraph part names regulation 142, which leads to Doc 2's drop (tied trap); rev 0's untied form failed "Needs the documents" | redesign: no fair wording satisfies both; retire unless the platform's Harder variations offer a fair route |
| F7 / aq-02360 / q02 | rev 1 (tested_sha256 a1fc3019...; question verbatim in the capture, answer diff 573 -> 514), platform Version 72102a, Run 2, Oct 9 2026 8:17 AM | unsupported gold / exclusive deadline reading | [raw](../verdicts/AQ-02360_difficulty_2026-10-09_0825.txt): "Answer not supported" "In the final check, the high model was given every document and still did not reach your answer." Low 0/5 (all 515), Medium 3/5; Document check 515, unfinished "4 May 2023", 515; per-attempt notes back 29 September | rev 2 (tested_sha256 c309acd2..., checked, 0 FAIL; user request "prepare reworded q02"): ask becomes "the last day an opted-out service election could still be received" so the high model tests dates against the rule; risk Medium above 3/5 or Low above 0/5 | repaired at the user's request, platform pending; if Run 3 is Between levels, Easy or unsupported again, drop q02; Platform validation record bound to rev 1 |
| F8 / aq-02360 / q02 | rev 2 (tested_sha256 c309acd2...; binding by user report) | difficulty / cue lifts the low model | user, 2026-10-09: "q02 too easy" (quick test, no screenshot) | rev 1's wording failed the gate's high model (F7); rev 2's cue let the low model through | dropped (q01 dropped too, F6); recommend releasing the bundle |

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
