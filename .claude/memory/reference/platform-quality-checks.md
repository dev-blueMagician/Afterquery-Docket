# Platform quality checks (task form)

The task form's quality-check list, pasted by the user on 2026-10-04 ("this is Quality check
gate's copied text. we need to update quality gate"). Check names and descriptions are the
form's words; the per-question status lines ("Not started", "Passed · 9 hr ago") are left out.
Kind: **block** stops Submit; **advisory** is "a warning, never a block"; **model** checks run on
the platform ("Re-run") and carry no advisory label. "Local" says where this workspace checks
it: a floor code from `tools/check_questions.py`, a gate check from
[question-gate.md](question-gate.md), or a step of `question-review`. The form's two own-words
checks ("Question in your own words", "Reasoning in your own words") are not part of this
workspace's quality check (user, 2026-10-04), so they are not listed.

| check | kind | the form's description | local |
| --- | --- | --- | --- |
| Question, answer & components | block | The question (8+ words, no more than 80) and answer are filled in, the answer has no semicolon, there are 1–10 distinct components, and the documents plus question fit the token window. | floor: fields, question-length, short-answer, components (token window not checked) |
| Reasoning tags | block | At least two reasoning tags from the list. | floor: tags |
| Solution explanation | block | The explanation of how the answer follows from the documents is filled in. | floor: fields |
| Necessary documents | block | At least two documents are marked necessary and each exists. | floor: documents |
| Verbatim evidence | block | Every quote appears word for word in the document it cites (12+ characters). | floor: evidence |
| Necessary documents cited | block | Every necessary document is cited by at least one verbatim quote. | floor: evidence |
| Component coverage | block | Every component has evidence (one bare count may go uncited). | floor: components |
| Question length | advisory | Aim as short as it can be and stay exact; warns above 60, blocks above 80. Shorter is never a fault. | floor: question-length |
| Answer length | advisory | Keep the answer to 10 words, or a list of up to 12 items of up to 10 words each. | floor: answer-length |
| Answer not given away | block | Neither the answer nor any of its parts appears in the question. | floor: giveaway; Q8 |
| Short answer | block | The answer is a short value (up to 10 words, or a list of up to 12 items and 250 characters, no semicolon), not a sentence or an explanation. | floor: short-answer; Q5 |
| Components match the answer | block | Every component is a piece of the answer (a value or a name from it, not a note or a sentence), and every number in the answer is in a component. | floor: components; Q14 |
| Answer parts can be told apart | block | A multi-part answer keeps a separator between its parts, so a grader can tell where one part ends and the next begins. | floor: components |
| Restricted names | block | The question, answer and reasoning use none of the names on the restricted list. (2026-10-07 wording: "The question, answer, reasoning, components, evidence quotes and the documents’ names, links and text contain no restricted name, model or vendor name, or internal link — the same rules the delivery scrub applies.") | not checked: the list is not captured |
| Original question | block | The question is not a near copy of another task's question. | not checked locally |
| Sibling question | advisory | The question does not ask for the same fact as another question on this bundle, give its answer away, or reuse its wording. | floor: sibling |
| Writing style | advisory | The question and reasoning avoid em-dashes and stock phrasing. | floor: style |
| Label for items in only one document | advisory | A question that compares documents and asks for labels offers a label for an item present in one document and absent from the other. | review: Q12 |
| Answer format stated | advisory | The question says how to give the answer: an order for a list, one question rather than two, and what to answer when nothing qualifies. | floor: format, asks; Q5 |
| Partial answers | advisory | A question that asks for "at least" some number of items does not have an answer listing more, which would mark a correct partial answer wrong. | floor: partial |
| Asks about the world, not the set | advisory | The question asks about what the documents describe rather than about the documents themselves, and the answer is a fact rather than a document (ground rule 10). | floor: world; review |
| Question length spread | advisory | Your questions are not all coming out the same length. A warning on your own pattern, never about this question being wrong. | hand-over: vary lengths across questions |
| One defensible answer | model | Given the documents, the question has exactly one defensible short answer, and your answer is that answer. | blind solves, review: Q4 |
| Needs two or more documents | model | Answering the question needs information from at least two of the documents. | review: Q2 removal test |
| Reasoning reaches the answer | model | Followed step by step, your reasoning arrives at the answer you gave. | review: key against the evidence |
| Evidence supports its component | advisory | Each quote gives the value of the component it is attached to, or a figure or fact used to work it out. | review: Q14 |
| Question does not hint the answer | advisory | The question does not point to or name any part of the answer in other words. | review: Q8 |
| No single passage gives the answer | advisory | No one passage or document in the bundle states the complete answer by itself. | floor: single-passage; review: Q2, D2 |
| Left-out items do not qualify | advisory | For a list or count answer, no item of the same kind that the answer leaves out meets the question's condition. | review: Q11 |
| Answer matches a stated figure | advisory | When a document states the figure the question asks for, the answer gives that figure, or the question says how to work it out instead. | review: Q4; [precision note](../docket-one-clear-answer-precision.md) |
| Each description fits one thing | advisory | Each thing the question describes ("the company whose …") matches only one thing in the documents. | review: Q4 |
| Answer covers every ask | block | The answer has at least as many parts as the question asks for (your number of asks, or what the question asks, whichever is more). | floor: components; review |
| Needs the documents | block | The question cannot be answered correctly without the documents. | closed-book solve: Q1, D1 |
| Question mix | advisory | Your questions are not mostly lists of items that meet several conditions. A warning on your own pattern, never about this question being wrong. | hand-over: mix shapes across questions |
| List contract | advisory | A list answer of more than three items says how many items to expect, or the question asks for one value instead. | floor: list-contract |
| Which period | advisory | When the documents cover several periods, the question says which period the answer is for. | floor: period; review: Q9 |
| Not a duplicate | block | Your saved question, compared with existing questions. Runs after you edit the question, and with Re-run all. | not checked locally |

## Difficulty check: removal flag (observed 2026-10-06)

Not in the pasted list above. aq-00998 q05 Run 2 (screenshot supplied by the user) showed, beside the
tier line, a blocking flag: "A marked document may not be needed. Your answer can still be reached
without document 10. Either that document is not needed, or the question does not yet depend on it.
If the document is needed (for example, it holds the item your question excludes), leave a one-line
note for the reviewer below. Otherwise fix the question or the documents you marked necessary, then
run the check again." The note box takes 200 characters, and "any edit to the question, answer,
reasoning or necessary documents clears it." Run history: "The result on the current content is still
answerable without a document marked necessary, so the gate does not pass." Local: gate Q2 removal
test, including rounded-figure approximations; see
[docket-series-editions-necessity](../docket-series-editions-necessity.md).

Run 3 on the revised question (2026-10-06, pasted text) passed and printed the check definitions:
"Document check: The high model answers with every document, then once with each document you marked
necessary left out. A document is needed when the answer without it is wrong, or changes from the
every-document answer, or when it is the only document naming an item you marked it as excluding.
Reaching the same answer without it means that document is not needed." "Closed-book check: The low
model answers with no documents at all. Reaching your answer here means the question does not depend
on the documents." A pass reads "The difficulty check finished: In band — Easy tier." and "You can
submit now." The page also shows "Question slots" per difficulty (aq-00998: Hard 0/2 · Medium 0/3 ·
Easy 0/1): "A slot is filled when a question is accepted; a question in review holds its slot until
then."

## Original question: templated wording (local review, 2026-10-06)

The blocking "Original question" check compares a saved question with other tasks' questions. A
draft that reused a measured pass's sentence frame almost word for word (aq-01322 q01 rev 1 against
aq-00964 q01: "When X completed the sale of its Y, what ... was its then-current outlook projecting
for the segment that included ...") was flagged by local review as a near-copy risk and restructured
(rev 2). Reuse a mechanism, not a sentence frame. Platform behaviour for such cases is not yet seen.

Second instance (aq-01333 q01 rev 0, local review, 2026-10-06): a question built on aq-00745 q09's
mechanism also copied its sentence ("By what percentage did the midpoint of ... change from the range
in force when ... to the range it ... Give the sign, to one decimal place."): token ratio 0.70, longest
shared run 8 tokens, identical closing sentence. Rev 1 restructured it (ratio 0.27, longest run 5).
Practical check before prepare: compare the question's lower-cased word tokens with every
tasks/*/questions/q*.md question (difflib SequenceMatcher); restructure when the ratio is above about
0.4, a shared run is 6+ tokens, or the closing sentence repeats one already in the bundle.
Restructuring must keep the anchor's strength: rev 1's softer anchor ("the forecast it was guiding
to when it finished selling") came back "Answer not supported" (see the next section).

## Difficulty check: "Answer not supported" (observed 2026-10-06)

aq-01333 q01 rev 1, Run 2 (user paste; raw in tasks/aq-01333/runs/q01-r1-v2-b98e240c.../results/):
"The difficulty check finished: Answer not supported." "In the final check, the high model was given
every document and still did not reach your answer. Check that the documents support it." Tier line
"Low 0/5 · Medium 0/5 · High 1/5"; run history "The result on the current content is not reachable
even with every document, so the gate does not pass." The document check's three "With every
document" runs all gave the decoy (11.8%). It carried an advisory: "This question may be too vague:
several solvers agreed on an answer that is not your gold ... Tighten the question so only one answer
fits, or check the gold." So a High 1/5 does not pass by itself. The every-document answer of the
high model must reach the gold, or the run fails whatever the tier counts. A trap must stay beatable
by the high model with all documents.

## Form check: "too vague to submit" (observed 2026-10-06)

The form's model check "One defensible answer" blocks submission when two solvers agree on a non-gold
answer: "This question is too vague to submit: two independent solvers, working from the documents alone,
did not reach your gold ... Both answered ... Tighten the question so only one answer fits, or correct the
gold." Seen on aq-01321 q02 (rounded same-window prose) and aq-01428 q01 rev 1 (an edition trap with a soft
timing anchor; both solvers took the event release's own later guidance). It runs before any difficulty run,
so a trap that catches both form solvers costs no run but cannot be submitted. Keep the anchor firm enough
for a strong reader ("then in force", "in force when"), and paste exactly the tested question: an extra
precision sentence changes the content and the solvers' reading.

## Necessary documents: roles and exclusion notes (observed 2026-10-06)

The form's "Necessary documents" panel (aq-01333 q01, two screenshots supplied by the user) gives each
ticked document a role: "Answer component" or "Exclusion / condition source". It also has an "or..."
control to group alternative documents. An exclusion source opens a reviewer note: "What rule or condition
in Doc N ... rules something out? The reviewer sees this note. If the needs-document check still finds this
document not needed, a note of at least 20 letters or digits and 3 different words, not just repeated sends
that warning to the reviewer instead of blocking Submit. You still need a quote from the document showing
what it rules out." Footer: "Mark at least 2 — the documents the question cannot be answered without. If
another document carries the same fact, group them as alternatives instead of leaving a note."
Derive the rest then ran its own needs check and printed "Doc 5 is needed: removing it reportedly moves
58.3% → 56.3%" plus "The check contradicted itself on the documents above. This does not block Submit; the
reviewer sees it." The 56.3% came from a run that took the September low end instead of the midpoint, so
the "needed" sample was noise. Derive also proposed the tags "Cross-document join, Aggregation"; set the
tags by hand to the reasoning actually needed.
Use (corrected 2026-10-07 by a platform review): do not tick an edition trap's decoy-carrying release
as "Exclusion / condition source" when another necessary document already dates the event.

aq-01333 q01 rev 4 did tick it. It passed the difficulty check at the Easy tier with no removal flag and
was submitted. The platform reviewer then returned it ("Revision requested"): "Doc 5 is marked as an
"Exclusion / condition source", but the answer doesn't depend on it. The document check reached the gold
without it ("Without document 5 — 58.3%") ... Doc 5's role in the note is only to rule out its own June 1
range ($3.35 to $3.45), and without Doc 5 that range doesn't exist to rule out. So the note doesn't make
Doc 5 necessary."

So the printed rule ("the only document naming an item you marked it as excluding") covers a document
that rules out an item which exists without it, such as an item named in another document or a scope
exception to another document's list. It does not cover a document that rules out only its own content.
Passing the difficulty check with the role does not mean the reviewer accepts the role.

The reviewer also asked that the explanation and evidence not rely on the unmarked document: drop its
evidence rows and date the event from a marked document (rev 5; result pending). Changing the ticks
changes the local fingerprint (documents metadata), so re-prepare and re-run the checks.

## Review panel: "Revision requested" (observed 2026-10-06 and 2026-10-07)

A platform reviewer can return a submitted question with a "Revision requested" panel at the top of the
Edit Task page. The panel has:
- bullets with "Go to Necessary documents" / "Go to Evidence" links;
- a summary paragraph;
- "Issues the reviewer found" cards labelled by field and kind, for example "Other · Other",
  "Evidence · Wrong / missing evidence" (aq-01333 q01), or "Question · Ambiguous wording" and
  "Question · Undefined term" (aq-01278 q02).

Reading the panel:
- "step N" means step N of the Solution explanation.
- "evidence row N" counts the form's own rows. Their order can differ from the local Evidence list:
  aq-01333's "your own evidence row 4" was local row 1.
- The "Go to Evidence" link sits beside a step-rewrite bullet. One user pasted the step text into
  Evidence row 2, and the form flagged "NOT VERBATIM".

Hand-over: give the full target state of every field the request touches (the whole evidence list and
the whole explanation), not only the changed lines.

Local handling: log the panel verbatim in notes/feedback-qNN.md, then revise in place as a new revision
(see [docket-accepted-question-is-finished](../docket-accepted-question-is-finished.md)).

## Targeted failure modes (observed 2026-10-07)

This is a new form section that must be filled before submitting. It appeared on the aq-01333 q01 rev 5
resubmission (two screenshots from the user). The form's text:

> Targeted failure modes. Before you submit, name the 1 to 3 traps your question sets for a careless
> solver, and how that solver goes wrong. Pick only traps your question really sets: the reviewer reads
> your reasons.

Until one is chosen, the form shows: "Declare at least one before you submit (at most 3)."

Full structure (task page saved by the user, aq-01278, 2026-10-07; task.html, copied to
tasks/aq-01278/runs/q02-platform-a75c90/). "How to fill this in", verbatim:
- "Pick the trap. The thing in the documents a careless reader trips on, such as a look-alike measure
  or an older figure inside a newer report. Each trap once per task."
- "Pick how they fail. The first step where a careless answer goes wrong, such as taking the wrong line
  item."
- "Justify it in three boxes. Where the trap sits (the document and passage), the exact wrong answer it
  produces, and why your answer avoids it. At least 150 words across the three boxes for each trap."
- "Spread your traps. Traps marked under-covered are the ones the collection needs most right now. Your
  recent mix is shown so you can vary it." (No under-covered marks or recent mix were in that page.)

Each "Failure mode N" block has:
- "Trap": a dropdown. Its options (form value in brackets) are Look-alike company
  (wrong_company_in_bundle), Wrong jurisdiction or scope (wrong_jurisdiction_or_scope), Wrong kind of
  entity (entity_type_mismatch), Fiscal vs calendar period (fiscal_calendar_offset), Trailing-period
  total (trailing_window_assembly), Older figure inside a newer report
  (historical_data_in_current_report), Out-of-range period (out_of_scope_period_exclusion), Wrong year
  or edition (wrong_year_or_edition), Superseded date or version (superseded_or_latest_deadline),
  Look-alike measure (similar_metric_confusion), Part vs total (subset_vs_total), Unit or basis
  (unit_or_basis_mismatch), Linking across documents (cross_document_entity_linking), Document
  convention (recording_or_format_convention), Figure that must be computed (derived_or_computed_metric).
  The selected trap's description shows below it. For Look-alike company: "The documents include another
  company, or one with a similar name. The answer must use only the target company's figures."
- "How a careless solver fails": a dropdown, "Choose…" first. Options: Picks the wrong entity or section
  (wrong_entity_or_scope), Uses the wrong period or date (wrong_period_or_anchor), Takes the wrong line
  item (metric_substitution), Misapplies a rule or premise (rule_or_premise_misapplication), Calculation
  slip (computation_or_arithmetic_error), Wrong members in a list (set_boundary_membership_error), Right
  content, wrong form (output_form_or_presentation_error), Rounding, scale or sign
  (precision_rounding_or_sign_error).
- Three text boxes, each up to 6,000 characters, with these placeholders:
  - "Where the trap sits": "The document and the passage that sets the trap, e.g. Doc 4, the segment
    table…"
  - "The wrong answer a careless solver gives": "The exact answer they would write, and how they get
    to it."
  - "Why the correct answer avoids it": "What a careful reader notices, and where, that leads to the
    right answer."
- A counter, "0 / 150 words across the three boxes".

The "Add another…" dropdown leaves out traps already chosen. Submit lists the requirement as a block
reason: 'Complete "Targeted failure modes": 1 to 3 traps, each with how a careless solver fails, all
three boxes filled and at least 150 words across them.' It is not one of the Checks rows. The
aq-01278 difficulty run (Run 2) has a result while the section is still empty, so it seems not to gate
the difficulty check. The run history names only question, answer and necessary-document edits as
needing a new result, so failure-mode edits probably do not, though the page does not say so outright.

Local use:
- Write the modes in the question file's `## Targeted failure modes` (template q00.md). The floor
  checks the lists, at most three, each trap once, the boxes filled and 150+ words. It also warns when
  fewer than 150 words hold a letter, in case the counter skips bare figures. A draft or checked file
  without them gets a WARN, and a ready file a FAIL. `--handover` prints them box by box.
- Declare only traps that Lever checks already prove, each with the wrong answer it gives, recomputed.
  Cite measured attempts when they exist, naming the run and counting equivalent forms. For aq-01278
  q02, Run 2 had 9 of 10 attempts at -2.3 in some form, while the platform's summary counted "4 of 10" by
  exact text.
- One measured trap is stronger than adding an unobserved one. The independent review, 2026-10-07,
  advised withdrawing aq-01278 q02's second mode, a rounded-rate route (-1.4%) that no attempt produced,
  whose wrong-base half the wording already ruled out.
- Pick the cause by the first wrong step. When the solver uses the right document and table but skips
  the premise's scope, "Misapplies a rule or premise" fits; the review said "Takes the wrong line item"
  also fits, and "Picks the wrong entity or section" is the weakest option, since the entity and
  section are right.
- Map the "Same series, right edition" lever to "Wrong year or edition", and an earlier version the
  bundle later replaced to "Superseded date or version". A segment-only figure printed under a
  look-alike label of a wider grouping is "Part vs total".
- In "Where the trap sits", describe the labels exactly: "look-alike labels", not "the premise's own
  label", when the wording differs.
- Do not declare a slip that the question's wording already rules out, such as GAAP vs non-GAAP when
  the question names non-GAAP, range ends when it says midpoints, or a wrong base when it says "from a
  year earlier".
- The declarations are outside the fingerprint. The independent review checks each claim.

## Other form changes seen on 2026-10-07 (aq-01278 task page)

- Necessary documents: each ticked document's role has three options: "Answer component", "Exclusion /
  condition source", and the new "Used to identify". The "or…" box ("Doc 4 or another document") offers
  only other ticked documents. Local: `## Necessary documents` (optional; Answer component when absent).
- "Number of asks": radio buttons "1 ask" / "2 asks", with "How many separate things the question asks
  for. At most 2: split a question with three or more asks." Local: front matter `asks`.
- Restricted names (block) now reads: "The question, answer, reasoning, components, evidence quotes and
  the documents’ names, links and text contain no restricted name, model or vendor name, or internal
  link — the same rules the delivery scrub applies."
- Difficulty budget: "6 of 8 runs left" for the task and "3 of 25 runs used in the last 24 h (all
  tasks)". Run history: "Only the result on the current question, answer and documents counts, and any
  edit to the question, answer or necessary documents needs a new result. Since 2026-09-27 a result is
  final for its version: the same version is not measured again."
- Submit steps: "Re-run the failed checks", "Check difficulty" ("Unlocks when blocking checks pass"),
  "Submit for review". A model check that "Couldn't check" ("Could not run this check — retry.") blocks
  Submit as "Fix or re-run: Needs the documents."
- Slots: "In review: Medium 1. 8 submissions left on this document set."
- The page saves checkbox ticks and evidence quotes, but not the Question, Gold answer and reasoning box
  values or any dropdown choice. A saved page therefore cannot show which reasoning or roles were tested.
- The page can conflict with itself. The run history said "The difficulty check passes on the current
  content." with "Version a75c90 (current)". The difficulty panel said "This result is for an earlier
  version of your question." and "Your question, answer or documents changed after this result. Run the
  check again before you submit.", and the solver summary said "measured on an earlier version". Record
  such a result as platform_verdict: unknown, and ask the user to check the panel once the hand-over is
  pasted.
- A run's "What changed before this run" list identifies the tested wording better than local guesses.
  It showed that aq-01278's version 4093c3, recorded as "rev 0 wording", was a wording no local revision
  had.

## Rule 10 warning trigger (observed 2026-10-06)

The form's question box flagged "the group of businesses that then included the unit" (aq-01322 q01 rev 2) with: "Your question refers to the document set itself — a phrase naming the document set itself (for example \"the group of\"). Name the things themselves and drop the count ... Ground rule 10. This is only a warning and does not block submitting." The trigger is lexical, broader than the local floor's world check (which matches "the bundle", "set of documents" and similar): avoid "the group of", and likely "the set of" and "the collection of", even for world things. "The reporting category that then included the unit" replaced it (rev 3).
