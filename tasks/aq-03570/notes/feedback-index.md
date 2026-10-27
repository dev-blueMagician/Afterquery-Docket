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
| aq-03570-q01-F1 | Version 7b44dd / rev 0 / dbcfd8306a6f...7054 (question quoted verbatim and gold equal; ticked documents and pasted reasoning not shown in the capture) | difficulty / the clause "Counting co-signed letters" carried every medium attempt past the co-signed letter; four of five low attempts dropped the letter that is not itself a document | [capture](../verdicts/AQ-03570_difficulty_2026-10-12_2036.txt): "Between levels", Low 0/5 · Medium 5/5 · High —; Coach not loaded; no document-check section | rev 1 / db98a2b9ef83...56e3: clause removed, set named as letters "that the Sierra Club signed"; routes and the added-gate check in [q01 Lever checks](../questions/q01.md) | historical: rev 1 was run (row F2) |
| aq-03570-q01-F2 | Version 2bc3fb / rev 1 / db98a2b9ef83...56e3 (the page's change list is exactly rev 1's question edit; question quoted verbatim, gold equal; pasted reasoning not shown) | ambiguity, with difficulty behind it / "letters that the Sierra Club signed" read as the letters that are themselves documents (266 days) by 2 of 4 medium and all 3 every-document attempts; with that reading fixed either way, the one remaining step (the co-signature) was cleared by every medium and every-document attempt (7 of 7) and by no low attempt (0 of 5) | [capture](../verdicts/AQ-03570_difficulty_2026-10-13_0007.txt): "Answer not supported", Low 0/5 · Medium 2/4 · High —; Document check "With every document · Did not reach your answer ✗" three times; no Coach text | q01 dropped at rev 1, no rev 2; routes and decision in [q01 Lever checks](../questions/q01.md); replacement [q02](../questions/q02.md) rev 0 / a16ab823ea8a...3974 (Justice Department letter, 84.3 days) | redesign: q02 platform pending (quick test, full checks, read "One defensible answer", then one difficulty run) |
| aq-03570-q02-F1 | quick test, no platform version shown / rev 0 / a16ab823ea8a...3974 (bound only by the user's message after the same day's hand-over; no panel or capture) | difficulty / the question named the identifier that decides the set ("under whose file numbers it was filed") | user, 2026-10-13, verbatim: "too easy for quick test"; logged in [q02 Feedback log](../questions/q02.md) | rev 1 / 4e215aee48bf...8bcc6: that phrase replaced by "it covered", nothing else changed | historical: rev 1 went to the form's Checks (row F2) |
| aq-03570-q02-F2 | form Checks, no difficulty run / rev 1 / 4e215aee48bf...8bcc6 (the screenshot shows rev 1's question in full and the gold; other fields not shown) | ambiguity / with no identifier named, both form solvers took the three proposals ICI names before its citation (91.7 days) | screenshots [1](platform-feedback/q02-rev1-checks-2026-10-13-1.png) [2](platform-feedback/q02-rev1-checks-2026-10-13-2.png) [3](platform-feedback/q02-rev1-checks-2026-10-13-3.png): "One defensible answer" Failed (blocking); advisories "No single passage gives the answer" and "Each description fits one thing"; "Needs two or more documents" and "Reasoning reaches the answer" Passed | rev 2 / 83bfa42a0c76...a71d: opens "Judging by all these letters together,"; nothing else changed | historical: rev 2 went to a quick test (row F3) |
| aq-03570-q02-F3 | quick test, no platform version shown / rev 2 / 83bfa42a0c76...a71d (bound only by the order of the messages; no panel or capture) | difficulty / with the evidence named ("Judging by all these letters together") the easier solver reaches the gold | user, 2026-10-13, verbatim: "too easy for quick test"; logged in [q02 Feedback log](../questions/q02.md) | q02 dropped at rev 2, no rev 3: file numbers named = too easy, nothing named = blocked, evidence named = too easy; replacement [q03](../questions/q03.md) rev 0 (US SIF, $1.65 trillion) | historical: q03 rev 0 was run (row aq-03570-q03-F1) |
| aq-03570-q03-F1 | Version 4ea612 / rev 0 / 27c7844eb83e...ef82 (the page's change list gives rev 0's question and the gold; document ticks not shown) | difficulty, between the medium and high solvers, with the page's "may be too vague" advisory / every recorded wrong attempt took Doc 7's combined $4.8 trillion for the climate figure (3.00); one medium attempt read Doc 12 and set the split aside as a reading of "climate change" | [capture](../verdicts/AQ-03570_difficulty_2026-10-13_1133.txt): "Between levels", Low 0/5 · Medium 0/6 · High 5/6; new gate wording; "What to change" proposes the exact label; no Document check for this run | rev 1 / 09cf2eea13ee...5151: scope named, "In US SIF's 2022 figures for ESG fund assets by issue"; no label added; routes in [q03 Lever checks](../questions/q03.md) | historical: rev 1 went to the form's Checks (row F2) |
| aq-03570-q03-F2 | form Checks, no difficulty run / rev 1 / 09cf2eea13ee...5151 (the screenshot shows rev 1's question in full; other fields not shown) | ambiguity / the form holds two answers defensible for "funds addressing climate change": the stand-alone $3.45 trillion (1.65) and Doc 7's combined $4.8 trillion (3.00) | screenshots [1](platform-feedback/q03-rev1-checks-2026-10-13-1.png) [2](platform-feedback/q03-rev1-checks-2026-10-13-2.png): "One defensible answer" Failed (blocking); advisory "Each description fits one thing", 2 matches; nine other rows Passed | rev 2 / ed666c624b74...f419: "funds addressing climate change as a stand-alone issue"; the exact label is still not used | historical: rev 2 went to difficulty Run 4 (row F3) |
| aq-03570-q03-F3 | Version 730996 / rev 2 / ed666c624b74...f419 (the change list and the closed-book attempt's quoted question give rev 2's wording and the gold; reasoning and document ticks not shown) | necessity, general knowledge / with no documents the low model committed 1.65 from recalled figures of about 3.41 and 1.76 (the letters print 3.45 and 1.8; its runner-up was tobacco); no solver with documents ran | [capture](../verdicts/AQ-03570_difficulty_2026-10-13_1553.txt): "Answerable without the documents", Run 4, Low — · Medium — · High —; run spent, 11 of 15 left; "Your last 3 runs were not in band. Ask the Coach before running again."; the page's three "What to change" items are not adopted | rev 3 / e04413be595f...22be: the two issues named as in rev 2, the gap asked as a percentage of the second-ranked issue's figure to one decimal place (gold 91.7%; the two recalled pairs give 93.8% and 97.7%); routes in [q03 Lever checks](../questions/q03.md) | historical: rev 3 went to a quick test (row F4) |
| aq-03570-q03-F4 | quick test, no platform version shown / rev 3 / e04413be595f...22be (bound only by the order of the messages; no panel or capture) | difficulty / with the term given one reading ("as a stand-alone issue") the easier solver answered | user message 2026-10-13: "too easy for quick test" | none: q03 dropped at rev 3, hook h4 closed; sketches [i05](sketches/i05.md), [i06](sketches/i06.md), [i07](sketches/i07.md) offered | closed / quick tests of i05 to i07 |
| aq-03570-q04-F1 | Version a37904 / rev 0 / 7bc2b8bb5b6b...8ad4 (the attempts quote the question in full and the page shows the gold; reasoning and ticks not shown) | difficulty / the medium solver cleared both steps: every recorded attempt took MFA's joint letter, and the co-signature held one of six (251) | [capture](../verdicts/AQ-03570_difficulty_2026-10-13_2032.txt): "Too easy", Run 5, Low — · Medium 5/6 · High —; "Too easy, so you got an extra run", 11 of 16 left; four "What to change" items, none adopted | none: q04 dropped, h2 and h3 closed, i06 retired; q05 rev 0 / 1a6e81ed3329...9601 (sketch i07, another family) handed over | closed / form Checks on q05, then one difficulty run |
| aq-03570-q05-F1 | Version 97008e / rev 0 / 1a6e81ed3329...9601 (change list and one attempt give the question; "Your answer" is the gold; ticks not shown) | difficulty / five of nine medium attempts swept the signers through the other letters; two right ones quote the opening as the reason; misses: authors only, IAA added, SIFMA AMG missed | [capture](../verdicts/AQ-03570_difficulty_2026-10-13_2325.txt): "Too easy", Run 6, Low — · Medium 5/9 · High —; extra run granted, 11 of 17 left | sketch [i09](sketches/i09.md): "Judging by all these letters together" out, "do these letters show" in; nothing else changed | historical: rev 1 went to Runs 7 and 8 (row F2) |
| aq-03570-q05-F2 | Version 2858b2 / rev 1 / facb345967f0...1d72 (the page reports no change to question or answer since Run 7; reasoning and ticks not shown) | difficulty / the high solver matched the signer list against the citations, 3 of 3; Run 7 not in the capture | [capture](../verdicts/AQ-03570_difficulty_2026-10-14_0938.txt): "Too easy", Run 8, Low — · Medium — · High 3/3; "Your last 3 runs all came back Too easy"; 11 of 18 left | none: q05 dropped, h8 closed (same failure after the focused repair) | closed / every hook on these bytes has a result; release recommended |

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

- Summary: not enrolled. The workspace ledger reported "All five prospective promotion slots are already
  enrolled" when aq-03570 i02 was promoted to q01 on 2026-10-12, so this bundle adds no trial rows.
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
