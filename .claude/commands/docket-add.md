---
description: File a Docket draft, preserve provenance, verify evidence and prepare a full handover for platform validation
argument-hint: <slug> [qNN] [path or pasted content] [--target easy|medium|hard]
model: claude-opus-5-5
effort: max
---

Read the guide, gate, newer-guide note and applicable memory. File or revise content in the
active bundle only. Preserve supplied wording if verbatim transcription was requested.
Never edit any byte of a submitted or accepted question, including metadata and logs.
Record later findings separately in notes/feedback-qNN.md.

1. Use a viable sketch with ambiguity and document-necessity checks (WORKFLOW section 4),
   or perform those concise author checks before expanding missing content with the active
   slug and target. New questions default to hard (2026-10-14); a lower open tier the user names is
   honored. Missing
   targets on existing legacy questions retain their prior hard requirement until an explicit
   target revision. Do not claim an unmeasured candidate will pass.
2. For a new question copy q00.md to the next free qNN.md, status draft, revision 0. Record
   difficulty_target: easy|medium|hard and accurate origin: user, claude, codex or gpt,
   with user+<agent> for collaboration. Record the actual runtime writer, not a configured model.
   AI revisions to user wording produce collaborative origin; never change provenance merely
   to pass export. For an editable revision increment revision, set draft and log the actual
   change. Changes to submitted fields, components, sources, target or reasoning invalidate
   old platform validation, even if wording changes look small. Old local records remain history;
   their staleness does not require new solves.
3. Carry the screened sentence (and, if the user quick-tested it, the survivor) and its short answer
   into the question file word for word; the strong-solver screen binds to those words. If any word
   seems to need changing (a frame shared with another task's question, a local warning on the order
   phrase, a cue to remove), stop: the changed sentence is a new sketch, needs a new packet and screen,
   and goes back to the user with the reason in one line, before components, reasoning, prepare or a
   hand-over. Do not change a tested sentence to get ahead of a form check that has not fired on it
   (aq-04112 q03, 2026-10-13: the opening and the order phrase were changed at write-up and the
   changed sentence failed the quick test the user ran on it).
   Reuse the promoted sketch's verified facts/calculation. For a Hard target carry its
   `## Lever stack` over: list each stacked lever's guide name in `levers:` (semicolon-separated; the
   floor warns below two), recompute each lever's "missed gives" answer in Lever checks, and declare
   failure modes only for those traps. Fill question, short answer,
   1-10 answer components, reasoning, tags, required documents
   and exact evidence quotes. Each necessary document supplies at least one quote; every
   answer number appears in a component. Tag each 12+ character single-passage quote with
   its component ids, for example - D03 (p. 2) [c1]: "...". No invented evidence or ellipses.
   Give a document that is not an answer component its form role in ## Necessary documents.
   Prefer a precise derived numerical gold. Follow WORKFLOW section 5 for reasoning: cited source
   inputs -> explicit arithmetic with units -> labelled derived result and requested rounding.
   Quote printed operands/scope as evidence for a computed component; do not invent a quote of the result.
   Fill ## Targeted failure modes: 1-3 traps from the form's list, each once, each with its cause
   and one shared "Why these are traps" reason of at most 50 words (form of 2026-10-08, replacing
   three boxes per mode). Declare only traps whose wrong answer Lever checks
   recompute (gate Q15). They sit outside the fingerprint, so adding or fixing them needs no new
   revision; record the change in Lever checks.
4. In Lever checks record the indispensable fact lost by removing each source after searching
   all remaining documents for replacements, concrete concept-search results, alternate
   printed figures at requested precision and attacks applicable to selected levers. Require
   a plausible decoy for "which items" questions; record rounded-prose/exclusion counterfactuals
   only when those levers are claimed. Remove inactive lever claims or revise the mechanism.
   Record independent numeric/date recalculation and any date-counting convention.
   Ordinary necessary cross-document arithmetic, dates and identifier joins are allowed;
   reject demonstrated direct-answer shortcuts rather than simplicity alone.
5. Update the sketch link and notes/session.md. Continue /docket-check <slug> qNN to freeze a
   single corpus snapshot, then run one mechanical preflight combined with the full handover.
   Do not duplicate the preflight here or dispatch solvers/reviewers beyond the strong-solver screen.
   Optional diagnostics need an explicit request or concrete unresolved issue.
   Enroll a newly promoted candidate with `docket_agent.py efficiency promote` using its existing
   sketch/timer ID; resume/revision keeps that slot. Record actual revision events and available
   usage once, with their evidence, in the shared ledger (WORKFLOW section 11).
6. Filing or a clean floor is not a platform pass. `checked` means mechanical preflight done,
   platform pending; `ready` needs a clean floor and a recorded exact-content platform pass at
   or above target. Preserve old records, never copy their hashes onto new tests.
