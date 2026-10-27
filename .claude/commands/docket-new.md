---
description: Scaffold, extract and map one immutable Docket bundle, then author evidence-grounded candidates for an explicit verification target
argument-hint: <slug> [document path] [--target easy|medium|hard]
model: claude-opus-5-5
effort: max
---

Start the bundle in $ARGUMENTS. Slug must be a plain kebab-case directory name; reject traversal
or paths masquerading as slugs. Resolve the exact destination within this workspace first.
New work uses difficulty_target: hard: since 2026-10-14 the user's bundles have Easy and Medium
full and the check starts at the High model. If the user names a lower open tier for this bundle,
use the lowest one named. Read .claude/memory/reference/hard-playbook.md before any hook work; it
is the current rulebook and wins over older notes.

1. Read the guide, gate, newer-guide note and applicable memory. If tasks/<slug> already exists,
   resume from its notes/session.md instead of overwriting or merging. Preserve existing
   submitted/accepted questions and any legacy target unless explicitly changed.
2. For a new bundle copy tasks/template-task into tasks/<slug>, remove only its copied q00.md,
   and copy documents into docs/ unchanged with original filenames. Use native PowerShell
   LiteralPath operations on Windows; verify the destination before copying/removing.
   For a captured task page use python tools/split_capture.py <capture.md> tasks/<slug>.
   Carry clipping/incomplete warnings forward. If documents were not supplied, inspect known
   workspace inputs; request only the missing source material instead of inventing it.
3. Run python tools/extract_text.py tasks/<slug>, then python tools/docket_agent.py mine tasks/<slug>
   (notes/mine.md: the guide's cross-document comparisons, done mechanically; rerun after any
   re-extraction). Record page counts, thin pages, unsupported formats and extraction gaps. Preserve originals. Visual-check missing tables/charts and
   resolve deciding evidence before drafting content that depends on it. For every extraction,
   compare page count with the original where applicable, one table and one footnote when
   present. Record absent features as not-applicable; record uninspectable originals as gaps.
4. Replace template slug placeholders in copied notes. Reuse an existing map when recorded
   source/extraction hashes match. Read promising relationships with their source context;
   refresh only changed inputs/dependent claims. Search the entire bundle for direct answers
   and substitute facts. Keep exact read/unread ranges; never label keyword hits as a full
   read. Expand coverage for relevant lists/exclusions or unresolved facts; a mapper is optional.
5. Author at most two minimal sketches: exact facts/quotes, question, gold, target,
   competing answers and the wording condition each fails, each document's unique input and
   searched substitutes (still indispensable after clarifying wording),
   selected levers, applicable lever checks, completeness and independent arithmetic/date
   checks. The caller records cross-document hooks in notes/hooks.md and sketches in
   notes/ideas.md with accurate origin and explicit target.
   Design each sketch by the playbook's section 4: start from notes/mine.md, pick a shape, and stack
   two or three levers on the path to one answer, each with its trap, its settling passage and its own
   wrong answer, over three dependent steps, with the decoy named; write them in the sketch's
   `## Lever stack`. No rare word of the question may sit in a settling passage. A single step of the
   kinds the playbook lists as cleared by the High model is a component of a stack, never a sketch.
   Keep the fairness checks before anything is offered: search the bundle for each phrase naming the
   asked period or population and name it by its structure if a document uses it as a label for
   something else; search recitals and footnotes before recording that a text is silent; run
   delete-and-guess on each ticked document (with it gone, what would a solver answer from the rest
   and from recall?) and redo it after any narrowing of the ask.
   Time prospective candidate work with `docket_agent.py efficiency start/stop` (WORKFLOW section 11),
   keeping the sketch ID on later promotion. Stop before platform/idle waits and turn end.
6. Cheap-screen sketches with /docket-check before full reasoning/components write-up. For a Hard
   target, then run the strong-solver screen on each (WORKFLOW section 4: `docket_agent.py packet`,
   three fresh blind solves, `record-screen`). The first hand-over is every fair sketch, paste-ready
   (sentence and short answer), with its screen result, lure and each miss's step, ranked by the
   screen: no question file, prepare or full form before the user picks one. The screen ranks and
   never withholds: a 3/3 sketch goes in, ranked last (aq-05049). A quick test is the user's option;
   the task page runs it against the high model and it never sets a tier (quick-test survivors still
   went Too easy at High: ledger rows 4, 17, 21, 25, 34). Set difficulty_target to the lowest tier the user named as
   open; the field is inside the fingerprint.
   Use evidence, necessity, direct-answer searches and selected-lever attacks. File survivors
   with /docket-add, verify arithmetic and prepare the snapshot, then run one mechanical
   preflight combined with the full handover for platform validation. Apart from the strong-solver
   screen, do not dispatch local model validators by default. Optional diagnostics need an explicit
   request or concrete unresolved issue. One focused repair per distinct observed failure; change the hook if the
   same failure recurs. After three unproductive sketch rounds report the supported options.
   Optionally save minimal notes/sketches/iNN.md and use python tools/docket_agent.py screen
   tasks/<slug> --idea iNN for the mechanical sketch screen. A clean result does not establish
   uniqueness, a model miss, readiness or a tier pass. The screen also prints the wording notes the
   full floor would raise at promotion (no "if any" on a which-items sentence, no order for a list,
   no stated precision, a cue clause): settle each in the sketch sentence before the strong-solver
   screen, because the screened sentence goes onto the form word for word and any change needs a
   new screen (aq-03707 q03: ", if any," was added between the quick test and the run).
   Change a failed dependency structure rather than paraphrasing the same shortcut.
   Use the earliest available platform screen only with existing external authorization and
   all fields that screen requires; defer optional prose, not required fields. Capture exact
   tested wording/raw feedback as early evidence, not final readiness. Triage feedback by
   platform version and issue before revising; a repeated old panel is not a new failure.
   Review the question set for diverse relationships, shared answer paths and giveaways.
7. Keep notes/session.md under 4,000 characters: target, phase, coverage gaps, candidates,
   statuses, concrete open findings, rounds used and next action. Report evidence established
   locally and the best remaining candidate. No platform pass is established yet.

Local preparation is authorized. Platform tests/submission require the user's existing
authorization or supplied platform results; do not send generated questions externally just
because this command prepares them.
