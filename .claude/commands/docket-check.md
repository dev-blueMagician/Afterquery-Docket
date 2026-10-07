---
description: Falsify Docket candidates with fresh isolated blind solves, closed-book checking, shortcut attack and independent gold review
argument-hint: <slug> [iNN | qNN ...]
model: claude-opus-5-5
effort: max
---

Check $ARGUMENTS within one active bundle. No ids means draft/checked questions. Read the
gate, newer-guide note and applicable memory. Honor difficulty_target easy|medium|hard;
new work defaults to easy, missing legacy targets retain hard. Never revise submitted/accepted
content. The caller records results and owns fixes; author, solver, auditor and reviewer are
separate fresh roles. Local work predicts suitability; the actual Docket verdict measures a pass.

An editable legacy question needs an explicit hard target before prepare can run. Add that
metadata through docket-add, incrementing revision and invalidating prior records; do not
silently lower its target to easy. Submitted/accepted legacy questions get read-only reports.

Sketches: inspect minimal exact facts/quotes, question, gold, tags, target, selected levers,
necessity, completeness and independent arithmetic/date checks before spending full solves.
Try direct whole-answer lookup, sufficient single documents, alternate readings and attacks
applicable to selected levers. Require decoys for "which items" questions; remove ineffective
lever claims or revise the hook. Ordinary cross-document arithmetic/date/identifier joins
are allowed; a simple valid route is a difficulty risk to measure, not automatic rejection.
File a viable sketch as draft through /docket-add for full reasoning/components/evidence and
complete isolation/checks;
do not pretend a partial sketch test validates a final question. Stop after three unproductive
sketch rounds, reporting concrete bundle limitations.
If an actual platform draft screen is available in the current form and already authorized,
preserve its exact input/feedback as an early screen. It does not transfer automatically to
full-field fingerprint readiness or replace the independent final checks below.
Optionally save a minimal notes/sketches/iNN.md (id, difficulty_target and documents metadata;
Question, Answer and exact Evidence sections) and run python tools/docket_agent.py screen
tasks/<slug> --idea iNN. This mechanical screen does not require components/full reasoning;
it is neither a model solve nor evidence of uniqueness, difficulty or a platform tier pass.

The scope binding is shared across sessions: prepare adds its run without evicting other
active runs (12-hour expiry), so runs for several questions or bundles may be active at once.
Independent workers for the same run may execute concurrently.

1. Run python tools/check_questions.py tasks/<slug> --q qNN. Fix content FAILs before tests.
   A missing readiness record while status checked is not evidence of a content error.
2. Run python tools/docket_agent.py prepare tasks/<slug> --q qNN. Save its exact fingerprint,
   revision, run id and solver-1, solver-2 and shortcut packet paths. It snapshots submitted
   fields and copies only immutable docs/text into packets. Never place the key, notes,
   answers, reasoning, audit findings or earlier results in a blind packet.
   Record source_gaps and source_gaps_sha256 verbatim. Needed/cited missing originals/text,
   unsupported formats or unknown provenance block readiness and cannot be waived. A known
   gap may be assessed as irrelevant only with the independent review below, concrete
   evidence across all six impact dimensions and matching snapshot/gap fingerprints.
   Never turn an irrelevant-gap assessment into a claim of complete corpus coverage.
3. Read each applicable role prompt explicitly, then dispatch fresh blind-solver A and B
   and fresh shortcut-auditor, optionally in parallel.
   Their task messages contain exactly root, their own prepared packet path and Question
   text verbatim. No target, source ids, proposed decoy, gold, fingerprint metadata, notes,
   hints or author conversation. Each role searches only its packet docs/text. Dispatch fresh
   closed-book-solver with Question text only and no usable tools.
   Use non-fork instances, never resume prior workers; Codex uses fork_turns: none.
   omitClaudeMd requires Claude Code
   2.1.271+. If unavailable, use isolated question-only sessions with equivalent read limits;
   if clean context cannot be established, mark contaminated and withhold validation.
4. Capture unabridged answers, paths, quotes, search coverage, gaps and tool/runtime errors.
   Missing/cut-off/contaminated execution is an invalid test, never a miss. If any submitted
   field changes or report shows fingerprint drift, invalidate the run and prepare fresh.
5. Dispatch fresh question-review with frozen fields, source corpus, revision, fingerprint,
   target and raw returns, without the writer's conversation. Reviewer independently
   recomputes the gold and falsifies necessity over
   the entire bundle. Two uncontaminated matches are required; wrong-lever is design evidence
   only. Replace one ordinary solver-error with a fresh run, but preserve the failure and
   never discard defensible alternative interpretations.
6. Append records below, using this run's exact revision and fingerprint, and preserve full
   returns under the run's results/ directory, outside all sealed solver packets. Escape literal
   pipe characters/newlines within record
   values or use indented following lines so they cannot impersonate fields.
   Blind solve section:
   - <date> | rev: N | solver: A | tested_sha256: <hash> | outcome: <match|wrong-lever|ambiguous|not-answerable|solver-error|contaminated> | confidence: <...> | docs: <...> | answer: <verbatim> | readings: <...>
   - <date> | rev: N | solver: B | tested_sha256: <hash> | outcome: <...> | confidence: <...> | docs: <...> | answer: <verbatim> | readings: <...>
   - <date> | rev: N | closed-book solve | tested_sha256: <hash> | result: <misses|reaches|contaminated> | answer: <verbatim>
   Shortcut audit section:
   - <date> | rev: N | tested_sha256: <hash> | verdict: <clear|shortcut|ambiguous> | findings: <verified route and coverage>
   Review section:
   - <date> | rev: N | tested_sha256: <hash> | verdict: <ready|revise|drop> | difficulty: <easy|medium|hard> | findings: <evidence>
   If the reviewer supports all current known gaps as irrelevant, Source assessment section:
   - <date> | rev: N | reviewer: <id> | tested_sha256: <hash> | source_gaps_sha256: <gap hash> | verdict: unaffected | findings: <JSON object mapping each exact gap to substantive premises, gold, exclusions, uniqueness, necessity and shortcut explanations>
   Preserve the reviewer return; missing assessments or unresolved dimensions block readiness.
   Contaminated auditors have no clear record; retain their full report as invalid evidence.
7. Set checked for local ready or revise; dropped for drop. Run floor and report again.
   Report target, fingerprint, gold validation, shortest verified route and unresolved findings.
   A local ready review is described as locally checked, awaiting platform verification.
   For a checked question, run python tools/check_questions.py tasks/<slug> --handover --q qNN
   and hand over notes/handover-qNN.md whole. It carries every form field in the form's order,
   failure modes included, with Doc N numbers. Say which form fields it replaces. Say whether the
   platform needs a new difficulty result: question, answer and necessary-document edits do.
   Revise editable content through /docket-add, increment revision and repeat the entire
   process with fresh contexts. After two ineffective revisions drop or develop a different
   dependency rather than retrying until a preferred result appears.
8. Record actual platform output only after the user supplies it or has authorized running
   that external test. Preparing a run gives no external authorization. Link evidence to the
   exact tested snapshot; a platform result on different wording is stale.
   Blind solve section:
   - <date> | rev: N | platform difficulty check | tested_sha256: <hash> | platform_verdict: <pass|fail|unknown> | passed_tier: <easy|medium|hard, pass only> | tiers: <verbatim observed tier line> | feedback: <verbatim platform verdict>
   Preserve the raw output/source in Feedback log or a linked saved artifact, including
   actual attempt counts. Use Low/High aliases only when quoting observed labels. Do not
   derive pass from counts, a reached tier, absent tiers, a local miss or an invented threshold.
   Mark unknown unless the platform explicitly establishes the tier passed.
9. Set ready only after this exact revision/fingerprint meets local requirements and observed
   passed_tier equals/exceeds the requested target. Run floor/report to confirm. Export is a
   separate provenance check; medium/hard are later targets, not preconditions for an Easy pass.

A scope denial means prepare/binding or explicit packet paths need repair. Never widen scope,
paste excerpts/key into prompts or grant shell/write tools to make a blind test succeed.
Keep notes/session.md under 4,000 characters with target, run, status, findings and next action.
