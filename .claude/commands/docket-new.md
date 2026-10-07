---
description: Scaffold, extract and map one immutable Docket bundle, then author evidence-grounded candidates for an explicit verification target
argument-hint: <slug> [document path] [--target easy|medium|hard]
model: claude-opus-5-5
effort: max
---

Start the bundle in $ARGUMENTS. Slug must be a plain kebab-case directory name; reject traversal
or paths masquerading as slugs. Resolve the exact destination within this workspace first.
New work defaults to difficulty_target: easy under the latest user request; an explicit medium
or hard target overrides that default. Easy is the first measured milestone, never an assumed
property of a local candidate.

1. Read the guide, gate, newer-guide note and applicable memory. If tasks/<slug> already exists,
   resume from its notes/session.md instead of overwriting or merging. Preserve existing
   submitted/accepted questions and any legacy target unless explicitly changed.
2. For a new bundle copy tasks/template-task into tasks/<slug>, remove only its copied q00.md,
   and copy documents into docs/ unchanged with original filenames. Use native PowerShell
   LiteralPath operations on Windows; verify the destination before copying/removing.
   For a captured task page use python tools/split_capture.py <capture.md> tasks/<slug>.
   Carry clipping/incomplete warnings forward. If documents were not supplied, inspect known
   workspace inputs; request only the missing source material instead of inventing it.
3. Run python tools/extract_text.py tasks/<slug>. Record page counts, thin pages, unsupported
   formats and extraction gaps. Preserve originals. Visual-check missing tables/charts and
   resolve deciding evidence before drafting content that depends on it. For every extraction,
   compare page count with the original where applicable, one table and one footnote when
   present. Record absent features as not-applicable; record uninspectable originals as gaps.
4. Replace template slug placeholders in the copied notes. Dispatch bundle-mapper with the
   absolute root, slug and extraction report. Continue incomplete coverage explicitly; do not
   call a skimmed or clipped document fully mapped. Keep chunk/page read and unread ranges;
   inspect all readable text rather than substituting keyword hits for coverage.
5. Dispatch independent question-author with root, slug and target. It returns at most five
   minimal sketches: exact facts/quotes, question, gold, tags, target, necessary dependencies,
   selected levers, applicable lever checks, completeness and independent arithmetic/date
   checks. The caller records cross-document hooks in notes/hooks.md and sketches in
   notes/ideas.md with accurate origin and explicit target.
6. Cheap-screen sketches with /docket-check before full reasoning/components write-up.
   Use evidence, necessity, direct-answer searches and selected-lever attacks. File survivors
   with /docket-add and run
   complete fresh checks. At most three sketch rounds and two revisions per candidate.
   Optionally save minimal notes/sketches/iNN.md and use python tools/docket_agent.py screen
   tasks/<slug> --idea iNN for the mechanical sketch screen. A clean result does not establish
   uniqueness, a model miss, readiness or a tier pass.
   Change a failed dependency structure rather than paraphrasing the same shortcut.
   A platform draft screen is optional only under the current form and existing external
   authorization; retain exact wording/raw feedback as early evidence, not final readiness.
   Review the question set for diverse relationships, shared answer paths and giveaways.
7. Keep notes/session.md under 4,000 characters: target, phase, coverage gaps, candidates,
   statuses, concrete open findings, rounds used and next action. Report evidence established
   locally and the best remaining candidate. No platform pass is established yet.

Local preparation is authorized. Platform tests/submission require the user's existing
authorization or supplied platform results; do not send generated questions externally just
because this command prepares them.
