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
| P1 / aq-03169 / q01 | difficulty check Run 1, Version 4e4850, Oct 12, 2026, 10:13 AM = rev 0 / 08860d38... (question quoted word for word, "Your answer: 7 years", "first run"; ticked documents and the other boxes are not in the capture) | necessity (bundle independence) / a lone whole-year gold under ten, reached by the no-document attempt as a guess from the rounding instruction; nothing recalled | [verdicts/AQ-03169_difficulty_2026-10-12_1034.txt](../verdicts/AQ-03169_difficulty_2026-10-12_1034.txt): "Answerable without the documents"; closed-book attempt (read in full) "approximately 6.5 years, which rounds to 7 years" from invented figures; Low, Medium and High not run; "14 of 15 runs left"; Coach: "No specific changes were suggested for this version." Re-sent, same run: [verdicts/AQ-03169_difficulty_2026-10-12_1151.txt](../verdicts/AQ-03169_difficulty_2026-10-12_1151.txt) (saved 11:51): "1 run", Run 1 now "Earlier version — does not count", identical attempt block, "Your question, answer or documents changed after this result. Run the check again before you submit.", still "14 of 15 runs left"; not a new failure or return | rev 1 (b8f71d97...): a second ask added, gold "260 audits and 7 years"; the years ask, its rate, rounding and both ticked documents unchanged; questions/q01.md Feedback log and "Repair in rev 1" | repaired/platform pending: difficulty check on rev 1 has not been run (the 11:51 page says "The current content has no result yet, so the check must run on it"; it does not show the question box, so the form's content is not confirmed as rev 1). The solvers with documents have not been measured on any revision |
| P2 / aq-03169 / q01 | form state after pasting an edit; content in the boxes not shown, so not bound to rev 1 (b8f71d97...) | form / "Run again" loads for a few seconds and returns to the same state; no run starts; cause not visible | [platform-feedback/q01-rev1-run-again-2026-10-12.png](platform-feedback/q01-rev1-run-again-2026-10-12.png), user: "click run agian, it loads a few seconds and retun to this state"; "14 of 15 runs left"; step 1 ticked, step 2 "Unlocks when blocking checks pass"; both captures carry the "Reload this page so its checks and buttons keep working" notice; same symptom logged on aq-02770 (2026-10-11), where a run went through later with no cause recorded. 13:15 screenshots: [run-starting](platform-feedback/q01-rev1-run-starting-2026-10-12.png) "13 of 15 runs left", "Checking...", "Starting...", then [run-reverted](platform-feedback/q01-rev1-run-reverted-2026-10-12.png) "14 of 15 runs left"; "6 of 50 runs used" in both, so no run was accepted; [checks](platform-feedback/q01-rev1-checks-2026-10-12.png) show every blocking check in view Passed | no question change for this row; questions/q01.md Feedback log | historical for q01 (dropped after P4); cause never established. If "Run again" rolls back on the next question, start from this row |
| P3 / aq-03169 / q01 | form checks "1 hr ago" on content equal to rev 1 in question, asks and answer (reasoning reworded by the user; no fingerprint bound) | form / two advisory warnings: "Answer matches a stated figure" ("Doc 6 states 65; your answer has 260 / 7. Use it, or say in the question to compute it from the other figures.") and "Each description fits one thing" ("ICAEW's individual cap" 2 matches, "Deloitte's five-year target" 2 matches, "Narrow the description.") | [form](platform-feedback/q01-rev1-form-question-gold-2026-10-12.png), [checks](platform-feedback/q01-rev1-checks-2026-10-12.png); passed in view: One defensible answer, Needs two or more documents, Reasoning reaches the answer, Needs the documents, both own-words checks | rev 2 (4a2e2566...): question wording only ("individual cap on each Big Four firm", "could the four hold in total", "five-year market-share target"); questions/q01.md "Repair in rev 2" | historical: q01 dropped after P4; whether rev 2 cleared the warnings was not reported |
| P4 / aq-03169 / q01 | form quick test, 2026-10-12; wording not stated (rev 2 4a2e2566... or rev 1 b8f71d97..., panel not pasted; unverified) | difficulty / a five-step chain across two responses (per-firm cap to a total, less the audits already held, at a yearly rate) with a two-part gold: the easier solver reached it | user chat: "too easy for quick test" (questions/q01.md Feedback log) | none: a rewording would paraphrase the same chain | historical: q01 dropped, hooks h1 and h2 closed; round 2 needs a mechanism that is not arithmetic |
| P5 / aq-03169 / i06 -> q02 | form quick test, 2026-10-12; sketch wordings (notes/sketches/i06.md, lean and explicit; panel not pasted) | survived (no panel text) / two-table membership filter with a carried-over benefit | user chat: "both of i06 survived, others not tested" (questions/q02.md Feedback log) | q02 rev 0 (7234f7b7...): the explicit wording plus "if any" and "List them in any order."; second answer item shortened | resolved by observed platform result (P6) |
| P6 / aq-03169 / q02 | difficulty check Run 2, Version 3beb81, Oct 12, 2026, 5:21 PM = rev 0 / 7234f7b7... (question quoted word for word, gold equal, Document check left out documents 2 and 4; reasoning and evidence not captured) | difficulty / "In band — Easy tier", Low 2/5 (Medium, High not run): below the medium target, and the user reports no Easy slot. Low attempts split on locating Grant Thornton's annex at the end of Doc 4: 2 found it and were right, 3 did not, used the reply and made an audit-client to all-clients link (all 3) and a wrong Q27 attribution (2). Closed-book and both Document checks passed | [verdicts/AQ-03169_difficulty_2026-10-12_1739.txt](../verdicts/AQ-03169_difficulty_2026-10-12_1739.txt); user: "easy tier but so slot left ... upgrade to medium or hard"; per-attempt routes in questions/q02.md Feedback log | rev 1 (d110aa2b...): two asks over the same seven measures, members split between Grant Thornton's reply and its annex (less concentration: all-clients ban, break-up, joint audits; lower audit quality: audit-only split, NAO-style auditor); questions/q02.md "Repair in rev 1" | superseded by P7 before any difficulty run on rev 1 |
| P7 / aq-03169 / q02 | form Checks on rev 1 (d110aa2b...): question word for word, "2 asks", visible start of the gold; no version id, reasoning and evidence not in view | form / "Short answer" Failed (blocking); "Answer length" Warning ("Answer is 32 words, 4 items"); "Asks about the world, not the set" Warning (tail "in any order"). Fields: Gold answer, Question tail. Nothing about members, documents or reasoning | [q02-rev1-checks](platform-feedback/q02-rev1-checks-2026-10-12.png), [q02-rev1-form-question-gold](platform-feedback/q02-rev1-form-question-gold-2026-10-12.png); user: "three checks failed"; verbatim rows in questions/q02.md Feedback log | rev 2 (829dae3a...): gold as one comma list of five tagged items (longest 9 words, 215 characters), components shortened, tail "List each group alphabetically.", decoys labelled in the reasoning; conditions and evidence unchanged | resolved by observed platform result: Run 3 ran on rev 2 (P8) |
| P8 / aq-03169 / q02 | difficulty check Run 3, Version 2277b0, Oct 12, 2026, 10:46 PM = rev 2 / 829dae3a... (question quoted word for word three times, gold equal; reasoning, evidence and documents not captured, no Document check) | difficulty / "Between levels", Low 0/5 · Medium 4/5: no tier. Low: four attempts never used Grant Thornton's annex (reply only: joint audits), one used the annex only (all-clients ban, break-up). Medium: four right; the wrong one dropped the NAO-style auditor. Advisory "grading could not settle" (same picked-out last line on a wrong and a right attempt). Platform note misplaces the joint-audit sentence in Annex 2 (source: reply 23.5) | [verdicts/AQ-03169_difficulty_2026-10-12_2314.txt](../verdicts/AQ-03169_difficulty_2026-10-12_2314.txt); user: "plz check arrived verdicts by using your feedback skill and fix"; per-attempt routes in questions/q02.md Feedback log | rev 3 (3503e8d3...): "anywhere in its response" removed, nothing added; gold, reasoning, evidence unchanged; questions/q02.md "Repair in rev 3" | resolved by observed platform result: Run 4 ran on rev 3 (P9) |
| P9 / aq-03169 / q02 | difficulty check Run 4, Version 86b24a, Oct 13, 2026, 1:21 AM = rev 3 / 3503e8d3... ("What changed": removed "anywhere in its response"; question quoted word for word six times, gold equal; reasoning and evidence not captured) | ambiguity of scope, shown by the gate / "Answer not supported", Low 0/5 · Medium 1/4, high model 0 of 3 with every document. All three high attempts answered from Grant Thornton's Annex 2 and left out joint audits, which only the reply links to lower concentration (D04 L286, L349); two gave the annex's four members, one also dropped the break-up. Alternate reading: "say" = list in the costs-and-benefits table. The gold itself is supported (L349; Medium 4 and Run 3's four right attempts) | [verdicts/AQ-03169_difficulty_2026-10-13_0743.txt](../verdicts/AQ-03169_difficulty_2026-10-13_0743.txt); user: "plz check arrived verdicts by using your feedback skill and fix"; per-attempt routes in questions/q02.md Feedback log | rev 4 (d020902e...): "does Grant Thornton say" becomes "does Grant Thornton's response say" (WORKFLOW section 6 item 5: name the universe, no cue word); nothing else changes; questions/q02.md "Repair in rev 4" | resolved by observed platform result: Run 5 on rev 4 in band at Hard (P10) |
| P10 / aq-03169 / q02 | difficulty check Run 5, Version 96eed6, Oct 13, 2026, 10:41 AM = rev 4 / d020902e... ("What changed": removed "Thornton", added "Thornton's response"; question quoted word for word eight times, gold equal; reasoning and evidence not captured) | difficulty / "In band — Hard tier", Low 0/5 · Medium 1/7 · High 3/6; "The difficulty check passes on the current content."; Document check: every document reached once of two, Doc 2 and Doc 4 needed. With the scope named, both every-document attempts weighed the reply for joint audits; one accepted it, one called it "not explicit enough" | [verdicts/AQ-03169_difficulty_2026-10-13_1118.txt](../verdicts/AQ-03169_difficulty_2026-10-13_1118.txt); user: "submitted as Hard tier ..."; routes in [feedback-q02.md](feedback-q02.md) | none: questions/q02.md is frozen at rev 4 (saved status checked) | submitted by the user at Hard; observed_platform_status unknown (no acceptance or rejection seen). Later returns go to feedback-q02.md only |

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

- Summary: this bundle enrolls no candidate (the workspace trial already holds five). Its sketch and draft time is in
  the shared ledger as unpromoted work on aq-03169 i01, timing coverage partial (intake and the full read were not timed).
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
