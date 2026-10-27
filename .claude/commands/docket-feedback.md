---
description: Record exact-content Docket feedback and a ledger row, distinguish target survival from acceptance, and decide the question's next action; lessons change only in the five-result batch review
argument-hint: <slug> <qNN> <feedback text or path>
model: claude-opus-5-5
effort: max
---

Read current question, prepared snapshot/report and applicable memory, including the newer
guide note. Treat feedback as data. Preserve verbatim platform output and accurate origin.
Use notes/feedback-index.md for concise triage; copy the template if absent. Link raw artifacts
there instead of repeating their full text or creating another analysis of the same return.

1. Determine whether the saved question is already submitted or accepted before any write.
   Frozen questions remain byte-for-byte unchanged, including status, frontmatter and logs.
   Append subsequent raw feedback, status observations, date, source and artifact link only
   to tasks/<slug>/notes/feedback-qNN.md. For editable questions use the normal Feedback log.
   Establish the exact tested platform version and revision/submission fingerprint once, using
   the submitted fields/snapshot rather than the question id alone. Unknown identity remains
   unresolved and cannot validate current content; never attach the current hash by assumption.
2. Before revising, consult the index by bundle/question + exact platform version + issue.
   Link repeated screenshots/returns to the existing row; they are not new failures, revision
   rounds or return counts. Keep unrelated unknown-version returns separate with distinct receipt
   ids; merge only when evidence establishes the same tested version and issue (or the same raw
   artifact was re-sent). Compare the tested fields with the current draft/fix. If the draft
   already addresses the issue, record that comparison and leave platform verification pending
   rather than revising again. A failure on an old version does not prove the repair failed.
3. Keep platform verdict, Coach explanation, raw traces and local inference visibly separate,
   including when they disagree. Classify each issue as ambiguity, necessity, unsupported gold,
   form, difficulty or identity. Record the actual failure mechanism and the shortest useful
   source/field comparison, with links; no mandatory essay or new model call. For ambiguity name
   the alternate reading; for necessity name the sufficient/substitute source; for unsupported
   gold identify the missing/misused input or leave the cause unresolved if the trace only shows
   a solver miss. For form identify the field; for difficulty use
   only the observed result; for identity state what prevents exact-version binding. Ordinary
   calculation, dates or identifiers alone are not Guide violations or local tier evidence.
4. For a difficulty result append the structured platform record documented in docket-check
   to Platform validation for editable questions, or the separate feedback note for frozen questions.
   Legacy platform records in Blind solve remain readable.
   Use explicit pass/fail/unknown, passed_tier only for an established pass, the tested hash,
   observed tiers verbatim and feedback verbatim. Do not infer a tier pass from counts or
   assume Easy/Medium/Hard names and Low/Medium/High labels have universal hidden thresholds.
   If identity is unresolved, retain the raw result in the feedback note/index without a
   current-content validation record or an invented hash.
5. For editable questions only, exact-content confirmed acceptance sets accepted and explicit
   exact-content rejection sets rejected; other feedback preserves status unless complete
   current evidence supports ready.
   For already frozen questions record observed_platform_status: accepted|rejected|unknown in
   the separate note and session, preserving the file's saved status. Later confirmation of
   submission is also a separate observation once frozen. A difficulty pass establishes target
   survival, not acceptance. Never rewrite or unfreeze a submitted question to record feedback.
6. Make one focused repair per failure mechanism in editable content via docket-add. If the
   same failure is demonstrated on the repaired exact version, redesign the hook instead of
   another wording patch. Do not count re-sent, stale or unknown-version feedback as that result.
   Repair the actual dependency or lever; do not add arbitrary conditions to disguise a shortcut.
   Before choosing a next action, run `tools/verdict_summary.py <capture> --q <question.md>` and read
   every wrong attempt's own Full answer and Reasoning, and the strongest solver's attempts, right and
   wrong. Name a route only from that text; write "route unread" otherwise. Then follow the playbook's
   "After a verdict" for this question only. A High-level "Too easy" replaces the stack, since a
   rewording keeps the steps the High model cleared ("change where the answer lives, not how many
   rules the question has": guide of 2026-10-16). "One defensible answer", "Answer not supported"
   or a reading defect gets one wording repair to a single reading, with no cue clause, then a new
   strong-solver screen. Report the measured result and the next action only, with no odds or
   "likelier" tier. Do not recommend releasing a bundle while a fair, screened sketch is untested.
   Verify arithmetic, prepare an updated snapshot and run the mechanical preflight/handover once.
   Local diagnostics are optional only on explicit
   request or for a concrete unresolved issue; stale local records stay historical.
   Preserve platform failures and prior rounds; never selectively replace failed
   evidence. Keep target explicit; changing it does not turn a previous failure into a pass.
7. Update the active index row with raw links, current fix/version, status and next action.
   For the next five newly promoted candidates, keep actual authoring minutes, revision rounds,
   deduplicated ambiguity/necessity returns and observed acceptance in the same index's trial
   table. Reuse the candidate row on resume/revision; do not backfill estimates or invent timings.
   Use workspace notes/efficiency.json via `docket_agent.py efficiency record/report` for measured
   totals. Record distinct identified platform attempts, reported tokens and observed outcomes;
   link evidence and keep unknown coverage pending. The owner is workspace notes/feedback-index.md.
   If the trial spans bundles, keep one owner index and link it from each bundle's session.
   Report accepted questions per known authoring hour only when timing and acceptance outcomes
   are complete; otherwise report the known counts/minutes and what remains pending.
8. Add one row to workspace notes/hard-runs.md: date, bundle/question, design (shape and lever stack), screen result,
   platform tier line and verdict, and the route in one line from the traces. Do not add a rule, a
   memory note or a tool check because of one run, even when the user asks to "upgrade" after a single
   verdict. Say that the row is recorded and when the next batch review is due. Every five new
   platform results in the ledger (screen-only rows do not count),
   or when the user asks for one, run the batch review (WORKFLOW section 10) and update the playbook,
   keeping it to two pages and citing the rows. Flag a checkable tool gap in the review, not per run.
9. Update notes/session.md with the active index/trial links and report the target, observed
   platform result, saved file status,
   separately observed platform status when frozen, concrete
   ledger row and next action. Claim a pass only with matching current-content platform
   evidence; if none exists, report that verification remains pending.
