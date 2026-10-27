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
| P1 / aq-02780 / q01 | Version 5d70b5 = rev 0 / f6541c05... (verbatim question quote, "Your answer: 9 changes", "first run") | necessity (bundle independence) / the gold equalled the sum of the question's three branch-opening counts, so a naive guess reached it with no documents | verdicts/AQ-02780_difficulty_2026-10-11_1137.txt: "Answerable without the documents"; closed-book attempt "2 + 3 + 4 = 9"; Low, Medium and High not run; 9 of 10 runs left | rev 1 (1c342b41...): counts changed (association seven, State bank five), ask split by agency, gold 4 by the OCC and 6 by the FDIC; no naive sum of the question's numbers gives it; questions/q01.md Feedback log and Revision history | resolved by observed platform result: Run 2 on rev 1 read "Needed the documents" in the closed-book check |
| P2 / aq-02780 / q01 | Version fb0985 = rev 1 / 1c342b41... (verbatim question quote 7 times, gold match, change list equals the rev 0 -> rev 1 edit) | difficulty / below the medium target: one step separated the solvers (the savings association's no-application rule for branches) and one low attempt in five read it | verdicts/AQ-02780_difficulty_2026-10-11_1351.txt: "In band — Easy tier", Low 1/5, "You can submit now."; four low attempts OCC 12 and FDIC 6; every attempt right on the FDIC side; Document check: every-document attempt right, both documents needed; closed-book needed the documents; 8 of 10 runs left | rev 2 (8d0a0160...): the bank forms four qualifying operating subsidiaries (notice, no approval) and the association one (application), so the notice-or-application distinction is read twice in opposite directions; gold 3 by the OCC and 7 by the FDIC of 27 changes; questions/q01.md Feedback log and Revision history | repaired/platform pending: paste rev 2 whole, run the checks and a difficulty run; a second Easy result means this hook's level is Easy and it is not patched again |
| P3 / aq-02780 / q01 | form state with the rev 2 question pasted verbatim (user screenshot in chat, 2026-10-11; "59 words"); no run, no version id | form / the Question box's own-words check | red message under the Question box (verbatim): "Your question reads as AI-generated. Rewrite it in your own words. Re-running the same text gives the same result. If you wrote it yourself, report it from Help (bottom left) → "Report an issue" so an admin can review it." | rev 2 text is the caller's (origin claude), so the message is accurate and the admin-report route does not apply; no agent rewording was supplied to get past the check | repaired/platform pending: the user sent their own wording in chat; recorded verbatim as rev 3 (3d92ec69..., origin user+claude), then replaced by a second wording of their own, rev 4 (2dbe139a..., 61 words), shortened by them to rev 5 (9a1c7f69..., 59 words, current); each checked against the gold (unchanged, 3 by the OCC and 7 by the FDIC), hand-over regenerated. Observed next: row P5 |
| P4 / aq-02780 / q01 | Checks list, user screenshot in chat 2026-10-11 ("two checks failed"), then a second screenshot of the Question box showing the rev 5 wording verbatim (59 words, 2 asks) with both red messages under it: bound to rev 5's question (9a1c7f69...); other fields not shown | ambiguity or unsupported gold / cause unresolved: the message is cut off before it says what it disputes | "One defensible answer · Failed · 11 min ago" (verbatim, as far as visible): "The reference answer of '3 by the OCC and 7 by the FDIC' is not fully supported. For the OCC: the 4 qualifying operating subsidiaries by the covered community bank require only after-the-fact notice (no approval), the 1 operating sub[...] association requires an application (expedited review, but still an approval), and the 2 head office moves require applications. Th[...]" | the visible part matches the gold's OCC count (0 + 1 + 2 = 3); nothing visible on the association's branches or the FDIC side | unresolved: the Question box shows the message cut at the same point ("... require applications. Th"), so the form itself truncates it; a page capture or the Question Coach may hold the rest; no repair until the disputed step is known |
| P5 / aq-02780 / q01 | same screenshots; the Question box shows the rev 5 wording verbatim with the message under it, so it is bound to rev 5's question | form / own-words check on the Question field, second observation | "Question in your own words · Failed · 28 min ago" with the same message as P3; beside it "Reasoning in your own words · Passed · 4 hr ago" (that time predates the rev 2 reasoning, so its currentness is unknown) | the check reads the user's rev 5 wording as AI-generated; the scenario and most of the phrasing come from the caller's draft, and no agent rewording was or will be supplied to get past the check | open: the user's decision (write it afresh in their own way with the caller checking facts only, or ask an admin with an accurate account of how it was produced, or stop); blocks Submit and the difficulty run until cleared |

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

- Summary: not enrolled. The five-candidate trial is owned by the workspace index
  (../../../notes/feedback-index.md); a peer session held the workspace's single timer on 2026-10-10, so no
  authoring time was recorded for aq-02780 (timing unknown, not estimated).
