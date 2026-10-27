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
| f1 / aq-02405 / q01 | receipt r1 (form Checks, 2026-10-09, user screenshot); gold "$48.05" = rev 0 (9da80895...), the only q01 version handed over; question text not visible, so not bound with record-checks | ambiguity (form block "too vague"): platform: two form solvers did not reach $48.05 (their answers not visible). Local inference: "ATF's 2026 savings estimates" never says to combine proposals, so Doc 6's own paper-individual estimate ($42; $41.53 at $26.10) reads as the answer; the r1 advisory "Doc 6 on its own may give enough" points the same way | [screenshot](../runs/q01-r0-form-2026-10-09/checks-screenshot-1.png) "This question is too vague to submit: two independent solvers, working from the documents alone, did not reach your gold "$48.05"." | rev 1 (checked, tested_sha256 441a66f47acf7fd1b48f78471d90dd09fb3d9417cf3241f836e6d46bcb771a4e) states the separating condition: "all of ATF's 2026 proposals' savings"; gold, reasoning, evidence, documents unchanged (q01.md Revision history) | historical: rev 1 never got a recorded full-checks result; superseded by f5 (q01 dropped) |
| f2 / aq-02405 / q01 | r1, as f1 | form (admin-controlled own-words check): "Your question reads as AI-generated. Rewrite it in your own words." Accurate: origin claude | screenshot as f1 | not a content defect; the user rewrites the question in their own words (origin becomes user+claude), keeping the listed conditions; no "Report an issue" authorship claim | historical: q01 dropped (f5) |
| f3 / aq-02405 / q01 | r1, as f1 | necessity (advisory warning): "Doc 6 on its own may give enough to compute the answer". Author comparison: Doc 6 alone gives $41.53; Doc 3 alone holds the 0.25 h CLEO copy (Doc 6 has 0 CLEO mentions) | screenshot as f1 | same scope reading as f1; rev 1's "all of ATF's 2026 proposals" names the combination | historical: q01 dropped (f5) |
| f4 / aq-02405 / q01 | r1, as f1 | form (transient): "Needs the documents: Couldn't check · Could not run this check — retry." | screenshot as f1 | no content change | historical: q01 dropped (f5) |
| f5 / aq-02405 / q01 | user chat 2026-10-09 "q01 too easy" (receipt r2); rev 1 (441a66f4...) or the user's own rewording of it, gold $48.05; wording unverified | difficulty (most likely the quick test): solved by the easier solver once the combination of proposals was stated | user chat, no screenshot | none (family closed) | historical: q01 dropped, hook h1 closed |
| f6 / aq-02405 / q02 | receipt r3 (form Checks, 2026-10-09, user screenshot, "3 checks failed in q02"); rev 0 (d9f211b2...) is the only q02 version handed over; question and gold not visible, and "Question in your own words" passed, so the user may have reworded it: identity unverified, not bound | ambiguity (form block "too vague"): platform: "two independent solvers, working from the documents alone, did not reach your [gold, cut off] ... and "cannot be determined"". Author comparison: Doc 5 replaces all of 478.96 ("Revise Sec. 478.96 ... to read as follows"), and Doc 4's 478.96 instructions never say they apply to Doc 5's version (only the matching words imply it), so the order of the two proposals, and with it (c)(4) vs (d)(4), is an inference; "cannot be determined" is defensible. Doc 4 does state that link for 478.124(c)(5) (fn 37, L194) | [screenshot](../runs/q02-r0-form-2026-10-09/checks-screenshot-2.png) | rev 1 (checked, tested_sha256 65b28e8644afab8c987b8a798cdfe1a2fa8ef53109d0c06c6b9a819c34a560d8) moves the same amendment chain to 478.124(c)(5), where Doc 4 fn 37 names Doc 5's rewritten text as the base; gold Paragraph (c)(5)(iv) (q02.md Revision history) | historical: repeat block on rev 1 (f10), hook h2 retired |
| f7 / aq-02405 / q02 | r3, as f6 | form (transient): "No single passage gives the answer: Couldn't check" and "Needs the documents: Couldn't check", both "Could not run this check — retry." | screenshot as f6 | no content change | historical: retries ran on rev 1 (Needs the documents passed; No single passage warned, f11) |
| f8 / aq-02405 / i03 | user chat 2026-10-09 "i03 and i04 are too easy" (receipt r4); sketch wording as handed over (Delaware, Florida, Maryland), not promoted | difficulty (quick test): match-then-exclude across Doc 5's state list and Doc 2's cited statutes, abbreviations included, solved by the easier solver | user chat | none | historical: dropped, hook h4 closed |
| f9 / aq-02405 / i04 | r4, as f8; sketch wording (Local and Tribal), not promoted | difficulty (quick test): Public Law 117-103 ID join with the denial-report decoy solved by the easier solver | user chat | none | historical: dropped, hook h3 closed |
| f10 / aq-02405 / q02 | receipt r5 (form Checks, 2026-10-09, user screenshot "Two checks fail"); gold "Paragraph (c)(5)(iv)" = rev 1 (65b28e86...); question not visible, possibly reworded: not bound | ambiguity (form block "too vague"): "Both answered "27 CFR 478.124(c)(5)(iii)"" = Doc 5's printed position, the declared trap, despite "all finalized as written" and Doc 4 fn 37. Repeat of f6's blocking check on the repaired version | [screenshot](../runs/q02-r1-form-2026-10-09/checks-screenshot-3.png) | none: q02 dropped | historical: hook h2 retired |
| f11 / aq-02405 / q02 | r5, as f10 | necessity (advisory): "This passage in Doc 5 may answer the question on its own." Author comparison: Doc 5 alone gives (c)(5)(iii); the redesignation is only in Doc 4 (L490, fn 37 L194) | screenshot as f10 | none | historical: q02 dropped |

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
