---
description: File an independently authored Docket draft, preserve provenance, verify evidence and invalidate validation after content changes
argument-hint: <slug> [qNN] [path or pasted content] [--target easy|medium|hard]
model: claude-opus-5-5
effort: max
---

Read the guide, gate, newer-guide note and applicable memory. File or revise content in the
active bundle only. Preserve supplied wording if verbatim transcription was requested.
Never edit any byte of a submitted or accepted question, including metadata and logs.
Record later findings separately in notes/feedback-qNN.md.

1. Use a viable tested sketch or dispatch question-author for missing content with the active
   slug and target. New questions default to easy; explicit medium/hard is honored. Missing
   targets on existing legacy questions retain their prior hard requirement until an explicit
   target revision. Do not claim an unmeasured candidate will pass.
2. For a new question copy q00.md to the next free qNN.md, status draft, revision 0. Record
   difficulty_target: easy|medium|hard and accurate origin: user, claude, codex or gpt,
   with user+<agent> for collaboration. Record the actual runtime writer, not a configured model.
   AI revisions to user wording produce collaborative origin; never change provenance merely
   to pass export. For an editable revision increment revision, set draft and log the actual
   change. Changes to submitted fields, components, sources, target or reasoning invalidate
   old independent and platform validation, even if wording changes look small.
3. Fill question, short answer, 1-10 answer components, reasoning, tags, required documents
   and exact evidence quotes. Each necessary document supplies at least one quote; every
   answer number appears in a component. Tag each 12+ character single-passage quote with
   its component ids, for example - D03 (p. 2) [c1]: "...". No invented evidence or ellipses.
   Give a document that is not an answer component its form role in ## Necessary documents.
   Fill ## Targeted failure modes: 1-3 traps from the form's list, each once, each with its cause
   and three boxes of 150+ words together. Declare only traps whose wrong answer Lever checks
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
5. Run python tools/check_questions.py tasks/<slug> --q qNN. Fix supported FAILs and rerun;
   explain remaining WARNs with evidence. Run python tools/docket_agent.py report
   tasks/<slug> --q qNN for current validity/fingerprint status. Preserve old records as history,
   never copy their hashes onto new tests or relabel them current.
6. Update the sketch link and notes/session.md. Continue /docket-check <slug> qNN to prepare
   isolated packets and run independent checks. Filing or a clean floor is not readiness,
   export eligibility, submission or successful platform verification.
