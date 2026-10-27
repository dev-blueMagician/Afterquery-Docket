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
| P1 / aq-02940 / q01, q02 (sketches i01, i02) | form quick tests 2026-10-11; wordings taken as q01 rev 0 (a171d32d...) and q02 rev 0 (66de3e7b...), assumed, panels not pasted | difficulty / a stated response rate (0.39% per 1%) from Doc 8 applied to Doc 1's percentage cut and fee base, in an explicit and a less explicit wording | user chat: "three all too easy for quick test" (questions/q01.md, q02.md Feedback log) | none: both wordings of the hook failed in one pass | historical: q01, q02 dropped, hook h1 closed |
| P2 / aq-02940 / q03 (sketch i06) | form quick test 2026-10-11; wording taken as q03 rev 0 (f1d02a0a...), assumed, panel not pasted | difficulty / a share derived from Doc 16's $1 billion beside Doc 1's printed 19% / 8% look-alike pair | same user message (questions/q03.md Feedback log) | none: the phrase that excludes the decoy is also the phrase that finds the input | historical: q03 dropped, hook h10 closed |
| P3 / aq-02940 / i09 -> q04, q05 | form quick test 2026-10-11; sketch wording (notes/sketches/i09.md, answer "1 April 2027"; panel not pasted) | survived (no panel text) / one dated case run through two banks' timing requests with the rules unnamed | user chat: "i09 survived" (nothing said about i09b or i08) | q05 rev 0 keeps the tested wording (a928e83f...); q04 rev 0 (fa9effab...) asks the same case as a day count from the stated deadline, because the date answer does not need Doc 1 (questions/q04.md Lever checks). Neither wording has a difficulty result | resolved by observed platform result (P4): q04 rev 0 was run; q05 never pasted, dropped |
| P4 / aq-02940 / q04 | difficulty check Run 1, Version 659f9e (current), Oct 11, 2026, 6:26 PM; rev 0, tested_sha256 fa9effab... (question and gold verified from the capture: 14 verbatim quotes, "Your answer: 262 days"; other boxes not captured) | difficulty / one dated case through ASB's eight months and Westpac's separately stated first-of-month request: "Between levels", Low 0/5 (5 x 243, none read the first-of-month sentence), Medium 5/5 (all applied it); closed-book needed the documents; Document check not run | [verdicts/AQ-02940_difficulty_2026-10-11_1834.txt](../verdicts/AQ-02940_difficulty_2026-10-11_1834.txt); user chat: "plz check arrived verdicts by using your feedback skill and fix" | q04 rev 1 (ce4f0fe3...): same anchor, Westpac requests and day count; ASB's single lead time replaced by Mastercard's domestic/cross-border pair, with the caps identified as those exempt from the limiting mechanism; gold 384 days (questions/q04.md Lever checks) | superseded by P5: rev 1 was quick-tested, not run |
| P5 / aq-02940 / q04 | form quick test 2026-10-11 (evening); wording taken as q04 rev 1 (ce4f0fe3...), assumed, panel not pasted | difficulty / the easier solver reached 384 on rev 1, which had replaced rev 0's "first start while satisfying both" with "first take effect, meeting" | user chat: "too easy for quick test" (questions/q04.md Feedback log) | q04 rev 2 (67dd0720...) restores rev 0's phrasing, nothing else changed; sibling sketch i11 names the caps as "the highest of its proposed caps" | superseded by P6 |
| P6 / aq-02940 / q04, i11 | form quick tests 2026-10-11 (late); wordings taken as q04 rev 2 (67dd0720...) and sketch i11, both gold 384 days, assumed, panels not pasted | difficulty / the limiting-mechanism wording was too easy a second time, with "first start" restored; the same question naming the cap as "the highest of its proposed caps" survived | user chat: "q04 too easy, i11 survived" (questions/q04.md Feedback log) | q04 rev 3 (0a5f5f69...) adopts i11's wording; q06 rev 0 (11f51dc8...) is its two-ask sibling (lowest and highest caps, 292 and 384 days), not yet quick-tested | resolved by observed platform result (P7): q06 was run |
| P7 / aq-02940 / q06 | difficulty check Run 2, Version 7017d1 (current), Oct 11, 2026, 10:10 PM; rev 0, tested_sha256 11f51dc8... (question, gold and marked documents verified from the capture) | difficulty / two-ask case through Mastercard's nine and twelve months and Westpac's first-of-month request: "In band — Easy tier", Low 3/5 (two misses 274 and 365, no first of the month); Document check needed Docs 1, 10 and 14; closed-book needed the documents | [verdicts/AQ-02940_difficulty_2026-10-11_2321.txt](../verdicts/AQ-02940_difficulty_2026-10-11_2321.txt); user chat: "easy tier but no slot for that. plz check arrived verdicts by using your feedback skill and fix" | none: with ASB the hook is Between levels (Low 0/5, Medium 5/5), with Mastercard it is Easy; no second gate for the medium solver was found (questions/q06.md Feedback log) | resolved by observed platform result: Easy, below target; hook h13 exhausted for Medium; release recommended unless the user wants the Easy pass |

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
