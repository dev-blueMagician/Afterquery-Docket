# Docket agent

This workspace builds fair, difficult questions from a named bundle of real documents. The
agent writes the question, gold answer, evidence and reasoning for platform validation.

**Current objective (user, 2026-10-14): a Hard platform pass.** Easy and Medium slots are full on
the user's bundles, so the difficulty check starts at the High model: "two solvers try up to 3 times
each. Ready when both get it wrong at least once, even if every attempt is wrong." (run page of
2026-10-18, aq-06835; pages up to 2026-10-15 ended "and not every attempt is wrong"; updated at the
user's request, 2026-10-19). New questions use
`difficulty_target: hard`. If the user names a lower open tier for a bundle, the target is the lowest
tier named. The 2026-10-05 Easy objective is history. Since 2026-10-17 (user: "Improve your engine for
hitting hard", with the guide of 2026-10-15/16) a Hard design stacks two or three levers on the path to
one answer, mined from the bundle first (playbook section 4): one deciding step per question went 138
of 138 right locally and eight of eight Too easy at High.

Read [hard-playbook.md](.claude/memory/reference/hard-playbook.md) first. It is the current design
rulebook, at most two pages. The other memory notes are frozen history: open one only for a specific
case, and the playbook wins where they differ. Read [WORKFLOW.md](WORKFLOW.md) for the procedure and
[question-gate.md](.claude/memory/reference/question-gate.md) for acceptance checks. The current
platform guide/form governs quality requirements; [instruction.md](instruction.md) is the
local guide, supplemented by the newer-guide memory note and by the guide's sections 4-7 of
2026-10-15/16, saved verbatim in [platform-guide-2026-10-16.md](.claude/memory/reference/platform-guide-2026-10-16.md)
(task shapes, Hard shapes, where solvers fail, the lever table, the Hard bank, send-back reasons).
Never relax fairness for difficulty.

## Ownership and boundaries

- The caller owns generation, revisions and accurate records. Do routine fixes autonomously.
  Keep the workflow lean: arithmetic verification, the strong-solver screen for a Hard target,
  one mechanical preflight and a full handover. The platform handles validation.
- Strong-solver screen (user-approved 2026-10-14): before a Hard sketch is offered for a quick test
  or a run, three fresh `blind-solver` agents solve its exact sentence from a packet made by
  `docket_agent.py packet`, and the author records the result with `record-screen`. The screen ranks;
  it never withholds. Every fair sketch reaches the user, paste-ready, with its result and lure, and
  the user decides what to test or run (user, 2026-10-14, aq-05049: "you even didn't give me any
  questions ... and let me release, without trying even once?"). All three right ranks a sketch last,
  marked as likely Too easy at High. Never reword or re-screen a sentence to find a miss. The floor
  FAILs a live Hard question with no screen record and WARNs on an all-right screen. No other local
  model check runs by default.
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
  `tools/docket_agent.py prepare --local-checks` creates isolated packets and binds the read guard
  only when an optional diagnostic is needed. Read the applicable role prompt explicitly.
- Never invent a solve, review, platform result or independence claim. A solver miss is not a
  correctness proof or a tier pass. Do not simulate platform difficulty or give local tier guesses:
  a screen with a miss permits a run and predicts nothing.

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
The user's preferred shape is one clearly defined numerical answer derived across documents,
with supported units/precision. Start there when the sources allow it. For a Hard target, run
`docket_agent.py mine` and stack two or three levers on the path to the number, each with its own wrong
answer, over three dependent steps, with no word of the question leading to a settling passage
(playbook section 4; the sketch's `## Lever stack`, which `screen` checks). One deciding step has not
held the High model: 46 screened sentences were right in 138 of 138 local solves and all eight screened
runs came back Too easy (2026-10-14 to 16). In Step-by-Step Reasoning,
label printed inputs and calculations separately using WORKFLOW section 5; quote inputs as evidence
for the derived component, without presenting a calculated value as a document's statement.
Never hand over a reasoning mistake the form's number check catches ("Step N: Doc X doesn't mention
Y"; user, 2026-10-09). The floor emulates that check (`tools/form_numbers.py`) and FAILs every number
a step's cited documents do not print in digits near their start, unless it is the step's exact "="
result or, in a step citing two or more documents, an earlier step's identical string. A figure the
cited document states only in words or deep, inside an evidence quote, is an expected false alarm
(WARN): say so with the hand-over, and prefer digit inputs at sketch time (the screen warns).

Default to two active sketches, each with concise ambiguity and necessity checks before full
write-up (WORKFLOW sections 2-4). Reuse maps bound to unchanged sources and inspect the relevant
passages. After one focused repair, a repeated failure calls for another hook, not weaker wording.
Triage exact-version feedback once in notes/feedback-index.md before editing an already-fixed draft.

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

For final questions use `python tools/docket_agent.py prepare tasks/<slug> --q qNN` to freeze the
form fields and one corpus copy, without solver packets or scope binding. Then run the mechanical
preflight once at the phase boundary, combined with handover below. Fix FAILs and fix/explain WARNs;
repeat only after a relevant change or unresolved failure. No edit hook runs this automatically.

Apart from the strong-solver screen, blind solves, shortcut audits, closed-book/removal probes
and independent review are optional diagnostics for an explicit user request or a concrete
unresolved issue. Use only the diagnostic needed. Stale local records remain history and never
trigger fresh solves merely to renew them.

Learning from verdicts (user-approved 2026-10-14): after each platform verdict, record it in the
question file, add one row to the workspace ledger [notes/hard-runs.md](notes/hard-runs.md) and
decide that question's next action. Do not add a rule, memory note or tool check because of one run.
A run is three tries by one or two solvers, so its lesson is often noise. Every five new platform
results in the ledger, or when the user asks, review the batch and update the playbook, keeping it to two pages. Name the
rows each change rests on, and compare the screen's results with the platform's.

Every hand-over is the whole form, from `python tools/check_questions.py tasks/<slug> --handover
--q qNN`. It covers Question, Number of asks, Gold answer, Step-by-step reasoning, Answer components,
Evidence, Necessary documents with roles, Reasoning tags, and 1-3 Targeted failure modes. Each mode has
a trap and a cause from the form's lists; since 2026-10-08 one shared "Why these are traps" box of at
most 50 words covers all modes (where each trap sits, the wrong answer, why the gold avoids it). The form
blocks Submit without them or above 50 words. Declare only traps whose wrong answers Lever checks recompute.

Every new record contains `rev: N` and the `tested_sha256` printed by prepare. The fingerprint
binds tested form fields and source bytes. Changed fields or documents invalidate the checks
even if someone forgets to increment the revision. Keep raw returns beside the snapshot.

Status `checked` means mechanical preflight done and platform pending. Status `ready` requires
a clean floor and an explicit recorded platform pass at or above the target on the same fingerprint.
Use `## Platform validation` for new platform records; legacy `## Blind solve` records remain readable.
Tier execution counts alone do not establish survival; do not invent the platform's numeric cutoff. Preserve its
labels and words verbatim. No platform access means that measurement remains pending.

Track all 39 platform Checks separately from difficulty readiness. Once the capture's exact tested
content is verified, use `docket_agent.py record-checks` with its prepared revision/fingerprint
(WORKFLOW section 10). Unknown bindings stay pending; save times and task titles do not establish
identity. Report blocking results, advisories and admin-controlled own-words checks accurately.
Stale/reload warnings and explicit footer blockers prevent recorded submission clearance even if
many checks passed. Clearance is not acceptance, and neither changes the actual writer's origin.

Assess missing ranges for their actual effect on the candidate. Relevant/unknown gaps and missing
necessary/cited material block readiness; a substantive author assessment or supplied platform
evidence can show known gaps irrelevant while preserving the incomplete-corpus warning and exact
gap binding. Independent model review is not required.

The configured Claude model/effort remain pinned in `.claude/settings.json` and role files.
If an optional diagnostic runs, use fresh, isolated roles; if isolation is unavailable, use
separate document-only chats instead of claiming contaminated results are blind checks.

## State and files

- `tasks/template-task/` is the only source for a new bundle's scaffold.
- Workspace `notes/efficiency.json` is the single measured-work ledger for the prospective five
  promotions; `notes/feedback-index.md` links it. Use `docket_agent.py efficiency` at phase boundaries
  (WORKFLOW section 11); stop timers before waits and keep missing usage/outcomes unknown.
- `notes/mine.md`: generated by `docket_agent.py mine` (tools/lever_mine.py), mechanical lever
  candidates with `text/Dnn.txt` line numbers and the corpus hash; navigation only, regenerated after
  re-extraction, never hand-edited.
- `notes/doc-map.md`: readable-source coverage and navigation; `notes/hooks.md`: cross-document
  opportunities; `notes/ideas.md`: lean sketch decisions; `notes/sketches/iNN.md`: input quotes for
  the lightweight screen and, for a Hard target, its `## Strong-solver screen` records. Screen packets
  live in `runs/iNN-screen-<hash>/`. Full lever/evidence records follow promotion.
- Workspace `notes/hard-runs.md`: one row per Hard-target screen or platform run, the input to the
  batch review.
- `notes/session.md`: checkpoint under 4,000 characters, updated at phase boundaries.
- `questions/qNN.md`: checked fields plus revision/fingerprint-bound records. Targeted failure modes
  sit outside the fingerprint; written `## Necessary documents` roles sit inside it.
- `notes/handover-qNN.md`: the generated paste-ready form; regenerate after any edit.
- `questions/qNN.json`: generated platform input values only, alongside Markdown. Handover writes
  it when encodable; `check_questions.py tasks/<slug> --json --q qNN` regenerates without validation.
- `notes/platform-checks-qNN.json`: append-only raw platform Checks records and verified snapshot bindings.
- `runs/`: form/corpus snapshots and actual platform returns; optional isolated diagnostic packets
  and raw returns are created only when needed. Never submitted.
- Keep UTF-8 file bytes. Use editing tools, not PowerShell text redirection.
- After tool changes run both `python tools/test_docket_tools.py` and
  `python tools/test_docket_agent.py` (it also runs the miner's tests, tools/test_lever_mine.py).
  These test the machinery, not platform difficulty.
- Read the playbook before feedback. `.claude/memory/MEMORY.md` indexes the frozen notes; preserve
  their dated evidence and its limited scope.

@instruction.md
