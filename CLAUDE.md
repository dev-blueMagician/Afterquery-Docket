# Docket agent

This workspace builds fair, difficult questions from a named bundle of real documents. The
agent writes the question, gold answer, evidence and reasoning, then tests them independently.
The latest user objective (2026-10-05) is **at least an Easy platform pass**. New questions use
`difficulty_target: easy`; `medium` and `hard` are explicit optional targets. Older maximum-only
notes are historical calibration, not the current acceptance policy.

Read [WORKFLOW.md](WORKFLOW.md) for the complete procedure and
[question-gate.md](.claude/memory/reference/question-gate.md) for acceptance checks. The current
platform guide/form governs quality requirements; [instruction.md](instruction.md) is the
local guide, supplemented by the newer-guide memory note. Never relax fairness for difficulty.

## Ownership and boundaries

- The caller owns generation, revisions and accurate records. Delegate evidence mapping,
  independent blind solving, shortcut attacks and review. Do routine fixes autonomously.
- Work on one named bundle. Never manually edit `docs/` originals. Re-ingesting a supplied
  complete capture may replace a clipped input through the splitter, preserving provenance history
  and invalidating all old checks. `text/` is regenerated only
  by the extraction tool. Questions use only that bundle, arithmetic and ordinary word meanings.
- Record `origin: claude`, `gpt`, or `codex` for the actual writer; `user` only for user writing,
  and `user+<agent>` for collaboration. Preserve wording when verbatim transcription is requested.
  The current export tool accepts `user` only. Never change origin to bypass it.
- Never edit submitted or accepted questions. Log subsequent findings separately.
- Blind checks get only the exact question and document packet, in a fresh context without
  writer history, project memory, answer, tags, selected document IDs or proposed levers.
  `tools/docket_agent.py prepare` creates isolated packets and binds the read guard.
- Never invent a solve, review, platform result or independence claim. A solver miss is not a
  correctness proof or a tier pass. Two independent supported matches are required for readiness.

## Generation policy

Find evidence relationships before writing questions: a definition applied to an instance,
an amendment changing an operative rule, a scope exception, a classification inferred from
facts in different documents, or reconciled observations whose consequence is not printed.
Find hooks across forecasts/actuals, proposed/final rules, editions/tables, amendments, hedge
scope and the Guide's other mechanisms. Draft lean sketches from neutral fact notes, reopen
sources to verify terms/premises, and screen them before full write-up. Ordinary cross-document
arithmetic/date/identifier joins are eligible. Require decoys for which-items questions and
answer-changing counterfactuals only for claimed levers; otherwise record not applicable.
For lists/counts keep a complete candidate universe and prove exclusions.

Search the **entire** bundle for alternative routes, including synonyms, identifiers,
repeated comparative tables and overview summaries. Necessary documents must remain necessary
even when another document repeats their facts. A long retrieval path, obscure fact or paraphrase does not establish difficulty.
Reject direct whole-answer lookup or one-source sufficiency. A short valid cross-document
calculation is a difficulty risk to measure, not a reason to reject a Guide-compliant question.

Treat historical D1-D7 as risk prompts, not a calibrated predictor. Reject a demonstrated
shortcut. Do not reject a legitimate join solely because it uses a shared identifier, or invent
complex wording to manufacture difficulty. Distinct question families matter more than volume.

## Verification and reporting

Use `python tools/docket_agent.py screen tasks/<slug> --idea iNN` for an optional read-only
sketch screen. Independently recompute numeric/date results with a script/calculator for one
check; record units/rounding/counting convention. Review sets for shared answer paths and hints.

For final questions use `python tools/check_questions.py tasks/<slug>` for the floor. Fix every FAIL;
fix or explain every WARN. Then prepare the snapshot, launch two fresh blind solvers, a fresh
shortcut auditor and a no-access closed-book solver, and request independent review.

Every hand-over is the whole form, from `python tools/check_questions.py tasks/<slug> --handover
--q qNN`. It covers Question, Number of asks, Gold answer, Step-by-step reasoning, Answer components,
Evidence, Necessary documents with roles, Reasoning tags, and 1-3 Targeted failure modes. Each mode has
a trap and a cause from the form's lists, and three boxes of 150+ words together. The form blocks Submit
without them. Declare only traps whose wrong answers Lever checks recompute.

Every new record contains `rev: N` and the `tested_sha256` printed by prepare. The fingerprint
binds tested form fields and source bytes. Changed fields or documents invalidate the checks
even if someone forgets to increment the revision. Keep raw returns beside the snapshot.

Local review can establish a defensible candidate, not measured difficulty. Status `checked`
means locally checked and platform pending. Status `ready` additionally requires an explicit
recorded platform pass at or above the target on the same fingerprint. Tier execution counts
alone do not establish survival; do not invent the platform's numeric cutoff. Preserve its
labels and words verbatim. No platform access means that measurement remains pending.

Assess missing ranges for their actual effect on the candidate. Relevant/unknown gaps and missing
necessary/cited material block readiness; a substantive independent source assessment can show
known gaps irrelevant while preserving the incomplete-corpus warning and exact gap binding.

The configured Claude model/effort remain pinned in `.claude/settings.json` and role files.
Use a runtime that supports fresh, isolated roles; if isolation is unavailable, use separate
document-only chats instead of claiming contaminated results are blind checks.

## State and files

- `tasks/template-task/` is the only source for a new bundle's scaffold.
- `notes/doc-map.md`: readable-source coverage and navigation; `notes/hooks.md`: cross-document
  opportunities; `notes/ideas.md`: lean sketch decisions; optional `notes/sketches/iNN.md`: input
  quotes for the lightweight screen. Full lever/evidence records follow promotion.
- `notes/session.md`: checkpoint under 4,000 characters, updated at phase boundaries.
- `questions/qNN.md`: checked fields plus revision/fingerprint-bound records. Targeted failure modes
  sit outside the fingerprint; written `## Necessary documents` roles sit inside it.
- `notes/handover-qNN.md`: the generated paste-ready form; regenerate after any edit.
- `runs/`: snapshots, question-only check packets and actual raw check returns; never submitted.
- Keep UTF-8 file bytes. Use editing tools, not PowerShell text redirection.
- After tool changes run both `python tools/test_docket_tools.py` and
  `python tools/test_docket_agent.py`. These test the machinery, not platform difficulty.
- Read `.claude/memory/MEMORY.md` before feedback; preserve dated evidence and its limited scope.

@instruction.md
