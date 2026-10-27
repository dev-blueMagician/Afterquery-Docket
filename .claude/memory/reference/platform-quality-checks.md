# Platform quality checks (task form)

Current checklist: all 39 items captured on 2026-10-08 in
[AQ-01650 Checks](../../../tasks/aq-01650/archive/round1-q01/verdicts/AQ-01650_checks_2026-10-08_1657.txt).
This supersedes the 2026-10-04 exclusion of the two own-words checks. The saved capture warns
that its results may be stale and retains a difficulty blocker; it is evidence of the form,
not a current pass for a local snapshot.

Kinds: **block** stops Submit; **advisory** never blocks by itself; **model** is a platform
judgment without an advisory label; **admin** can be cleared only by the platform administrator.
Local floor checks are structural or heuristic, never proof of semantic validity or authenticity.
Author/source checks use the existing workflow; extra model diagnostics remain optional only
for an explicit request or concrete unresolved issue. See [question-gate.md](question-gate.md).

| check | kind | requirement | current local coverage / owner |
| --- | --- | --- | --- |
| Question, answer & components | block | Filled question/answer; 8-80 question words; no answer semicolon; 1-10 distinct components; documents plus question fit token window. | floor: fields, lengths, components; token window remains platform-only |
| Reasoning tags | block | At least two allowed tags. | floor: allowed names/count; author verifies actual reasoning |
| Solution explanation | block | Explanation is filled in. | floor: presence; author/platform verify derivation |
| Necessary documents | block | At least two necessary documents exist. | floor: selections/existence; necessity itself needs author/platform review |
| Verbatim evidence | block | Each quote appears in the cited document and has 12+ characters. | floor: normalized extracted-text matching; author verifies against source |
| Necessary documents cited | block | Each necessary document has a quote. | floor: document groups; alternative-document omissions can warn |
| Component coverage | block | Each component has evidence; one bare count may go uncited. | floor: associations; semantic support remains author/platform |
| Question length | advisory | Aim concise; warns above 60 words, blocks above 80. | floor: whitespace word count |
| Answer length | advisory | Up to 10 words, or up to 12 list items of up to 10 words each. | floor: answer-item parsing independent of component count; ambiguous segmentation warns |
| Answer not given away | block | Neither the answer nor its parts appears in the question. | floor: literal matching with exceptions; author/platform check semantic hints |
| Short answer | block | Short value or list, up to 250 characters; no semicolon, sentence or explanation. | floor: length, parsed items and wording heuristics; Q5 |
| Components match the answer | block | Components are answer pieces and cover every answer number. | floor: approximate substring/numeric coverage; author verifies meaning |
| Answer parts can be told apart | block | Parts have clear separators. | floor: component spans and answer separators; author resolves ambiguity |
| Restricted names | block | No restricted names, model/vendor names or internal links in fields, evidence or documents. | platform; full restricted list unavailable locally |
| Original question | block | Not a near copy of another task's question. | platform cross-task comparison; author avoids copied sentence frames |
| Sibling question | advisory | No duplicate fact, giveaway or reused wording within the bundle. | floor: same-bundle literal/similarity warnings; author compares answer paths |
| Writing style | advisory | Avoid em-dashes and stock phrasing. | floor: wording heuristics; author reads for clarity |
| Label for items in only one document | advisory | Comparison labels cover present-in-one/absent-in-other items. | author/source check; Q12; platform |
| Answer format stated | advisory | Specify needed order and empty case; avoid tangled asks. | floor: wording/declared-asks heuristics; author/platform |
| Partial answers | advisory | An "at least" request must not reject a valid shorter answer. | floor: parsed answer-item count and wording heuristic; author/platform |
| Asks about the world, not the set | advisory | Ask for a world fact rather than a document. | floor: wording heuristic; author/platform; ground rule 10 |
| Question length spread | advisory | Avoid an unnecessarily uniform pattern across questions. | author set review; platform portfolio check; no local aggregate measurement |
| Question in your own words | admin | Question reads as written by you; only an admin can clear it. | record platform outcome; accurate origin is required and is not certification |
| Reasoning in your own words | admin | Reasoning reads as written by you; only an admin can clear it. Short reasoning is flagged for review instead of blocking Submit. | record platform outcome/explicit nonblocking review state; never relabel agent authorship |
| One defensible answer | model | Exactly one defensible short answer, matching the gold. | author alternatives/source check; Q4; platform |
| Needs two or more documents | model | At least two documents contribute indispensable information. | author dependency/substitute search; Q2; platform Document check |
| Reasoning reaches the answer | model | Source-to-answer steps reach the gold. | author source verification and arithmetic/date recomputation; platform |
| Evidence supports its component | advisory | Quote supports its component or a required input. | author/source check; Q14; platform |
| Question does not hint the answer | advisory | No answer part is paraphrased or indirectly revealed. | author wording/source check; Q8; platform |
| No single passage gives the answer | advisory | No passage or document provides the whole answer. | floor: literal co-occurrence heuristic; author whole-bundle substitute search; platform |
| Left-out items do not qualify | advisory | No omitted candidate meets the conditions. | author complete-universe/exclusion check; Q11; platform |
| Answer matches a stated figure | advisory | Use a directly stated figure unless the question specifies another calculation. | author alternative-input check; Q4; [precision note](../docket-one-clear-answer-precision.md); platform |
| Each description fits one thing | advisory | Descriptions resolve to one entity/input. | author identity/source check; Q4; platform; repeated mentions alone do not prove ambiguity |
| Answer covers every ask | block | Cover every actual ask, at least as many parts as declared. | floor: declared asks/components approximation; author/platform verify actual asks |
| Needs the documents | block | Cannot answer correctly without the documents. | author bundle-dependence check; Q1; platform; closed-book diagnostic optional |
| Question mix | advisory | Avoid an unnecessarily repetitive question shape. | author set review; platform portfolio check; no local aggregate measurement |
| List contract | advisory | More than three items requires a stated count, unless one value is requested. | floor: parsed answer-item count and wording heuristic; ambiguous parsing warns |
| Which period | advisory | Specify the intended period when several occur. | floor: limited fiscal/calendar wording heuristic; author/source check; Q9; platform |
| Not a duplicate | block | Saved question is not a duplicate among existing questions. | platform cross-task comparison |

## Recording current Checks without local model runs

After verifying that the platform tested the existing prepared snapshot, record its raw capture:

```powershell
python tools/docket_agent.py record-checks tasks/<slug> --q qNN --capture <capture.txt> --revision N --tested-sha256 HASH
```

The explicit revision/hash asserts a verified content match; a task title, save time or matching
answer is not enough. If that identity is unavailable, preserve the capture as historical/unbound
feedback and leave current Checks pending. Never guess a binding. The command records raw captures
append-only in `notes/platform-checks-qNN.json`; it runs no models.

Report/handover separates all 39 recorded outcomes/currentness from difficulty readiness.
`ready` still means a clean floor plus an exact-content difficulty pass at/above target.
Recorded submission clearance additionally needs current platform blocking checks and no explicit
footer blocker. Missing/unknown blocking results, stale/reload warnings or a retained difficulty
blocker prevent clearance. An advisory warning or retry stays advisory, and an explicit nonblocking
admin review state is reported accurately. Clearance is not acceptance or proof of authorship.

The dated sections below preserve historical observations. Their references to required local
reviews/probes are superseded by the current author/source checks and platform-first workflow.

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

Later page (aq-01543 q04 Run 1, saved 2026-10-08, tasks/aq-01543/verdicts/): the document check showed two
attempts per left-out document (two "Without document 12", two "Without document 4"), each marked "Needed
document N", besides one "With every document". The budget line read "7 of 8 runs left · 3 of 40 runs used in
the last 24 h (all tasks)" (25 in the 2026-10-07 capture). Each wrong attempt carries a platform note comparing
it with the author's reasoning ("Where it left your evidence: It included Kori-3 and Kori-4 ... whereas the
expert excluded them"), and the summary counts attempts quoting the same passage. "Ready when 1–3 attempts at
a level are right, out of up to 5. A level can settle early, for example at 1 right out of 3."

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

Second instance (aq-01650 q01, platform version 1923ac, Run 1, 2026-10-08; saved page
tasks/aq-01650/archive/round1-q01/verdicts/AQ-01650_difficulty_2026-10-08_1000.txt): "Answer not supported", "Low 3/5 · Medium — ·
High —". Later runs on the same family (archive README): Run 2 "Did not finish" and Run 3 "Too hard" (version
288215, Low 0/5 · Medium 0/5 · High 0/5, condition clause removed), Run 4 "Answer not supported" (version 61debd,
Low 1/5, two attempts quoting "Descriptive statistics for complete cases."); bundle restarted 2026-10-08. The low model reached the gold 3 of 5 times, but all three "With every document" attempts answered the
printed decoy (13.7). The gold's only input sat in a decomposition table's header cell ("Men: 14.719 (0.067)Women:
13.480 (0.060)"), which the high model never consulted (no mention of it in any of its three attempts); it saw that
the question's population differed from the decoy's yet concluded the needed mean was not reported. So the
high-model final check can fail where a weaker model succeeds, when the gold's input is in a non-descriptive table
(decomposition, regression header) and a same-label descriptive figure exists. Local Opus solvers found that cell
in every run, so local checks cannot see this risk; prefer golds whose inputs sit in descriptive tables or prose.

## Form check: "too vague to submit" (observed 2026-10-06)

The form's model check "One defensible answer" blocks submission when two solvers agree on a non-gold
answer: "This question is too vague to submit: two independent solvers, working from the documents alone,
did not reach your gold ... Both answered ... Tighten the question so only one answer fits, or correct the
gold." Seen on aq-01321 q02 (rounded same-window prose) and aq-01428 q01 rev 1 (an edition trap with a soft
timing anchor; both solvers took the event release's own later guidance). It runs before any difficulty run,
so a trap that catches both form solvers costs no run but cannot be submitted. Keep the anchor firm enough
for a strong reader ("then in force", "in force when"), and paste exactly the tested question: an extra
precision sentence changes the content and the solvers' reading.
Also seen on aq-01431 old q01 rev 1 (label dropped; both took a grouped figure despite "single") and
aq-01650 q01 rev 0 (2026-10-08; both took a complete-case table mean that the question's "non-student
respondents" also fits). Current rule and evidence: [form block](../docket-form-vague-block.md). A printed
figure the question's words fit is a second answer unless a condition the question states excludes it, and
local Opus matches did not predict any of the blocks.

Second message, same box (aq-01543 q01, 2026-10-08, user screenshot): red, "Working the question from the
documents does not give this answer. Check which figure, period and entity the question asks for, and that each
value comes from the right row and column." No solver answers were shown, and which listed check it belongs to is
not stated. The design matched the blocks above (a built gold beside a printed coal share for a window starting
in the asked year). Handle it with the same rule: [form block](../docket-form-vague-block.md).

## Necessary documents: roles and exclusion notes (observed 2026-10-06)

Seen 2026-10-12 (aq-03170 q01): the blocking form check "Needs two or more documents" now names marked documents it
rejects: "You marked documents 3, 13 as necessary, but the answer does not need them. Unmark them, or change the
question so they are needed.", with a "Remove document" button per document. It rejected the two documents that
each carried one list member alone (members named in no other document) and kept the two that combine for the third
member. The same marks passed one revision earlier, while the form's own solvers were missing the gold, so a pass
before "One defensible answer" passes proves nothing. How the check reaches a single-source member without its
document is not shown; unresolved. For a list, expect only documents that combine for a member to survive this check.
With the two documents unticked (kept as evidence rows) the check passed, and the difficulty run's document check
tested only the two still marked and found both needed (Run 1, Version bbce17).

Seen 2026-10-12 (aq-03170 q01 rev 4): a check row can read "Couldn't check" with "Could not run this check — retry."
(here the blocking "Needs the documents"). That is the platform failing to run the check, not a verdict on the
content: retry it, reloading the page if the page has asked for a reload. The user reported it, together with an
advisory Warning, as "two checks failed", so read each row's own label before changing anything.

Outcome on aq-03170 q01 (submitted at Hard, 2026-10-12): "Each description fits one thing" stayed a Warning on
every revision of this three-name list and did not stop the difficulty run or Submit. The question went in with
Docs 3 and 13 unticked (the form's blocking check had refused them) while the explanation still names and quotes
both. The floor now WARNs on exactly that; the "Exclusion / condition source" role with its reviewer note was
not tried there, so whether it keeps such a tick is unknown. The reviewer returned that submission the next day
for exactly this ("Necessary documents list only Docs 6 and 8, but Doc 3 is the sole source ... so both must be
tagged"): when this check and the sole-source rule disagree, the reviewer follows the sole-source rule. Also learned: the form did not read "Earliest
second letter first." as an order and flagged "second letter" as a pointer; "List them alphabetically." was
accepted. The floor now WARNs on both patterns (codes format and pointer) and on cue clauses (code cue).

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

Observed 2026-10-13 (aq-02749 q02 rev 2, Run 3, four screenshots in tasks/aq-02749/verdicts/): two documents ticked
as "Exclusion / condition source" at a reviewer's request, each with the panel's reviewer note. The Document check
still reached the answer without each, the run was labelled "A marked document is not needed" although its counts
were in band (Low 0/5, Medium 2/6), and Submit was blocked: "The difficulty check found the answer can still be
reached without one of the documents you marked necessary. If that document is needed, name it as excluded in your
reasoning ("Document 4 is excluded because..."), or leave a one-line note for the reviewer in the difficulty check."
The difficulty panel has its own box for that note: "Is documents 3 and 4 needed? Say why in one line. The note goes
to the reviewer, and any edit to the question, answer, reasoning or necessary documents clears it." (0 / 200
characters, "Save note"). The banner says either route "clears submit without a new run, and the reviewer checks it".
So the panel's reviewer note is not enough by itself: hand the one-line note over with the ticks and have it saved
last. The same page shows the medium gate in a new form: "Medium model: three solvers try up to 3 times each. Ready
when at least two get it wrong twice and one gets it right twice. A level stops as soon as more attempts could not
change the result." Advisory rows drawn by a bare-digit two-part answer ("10, 12"): "Left-out items do not qualify"
matched the digits in a date and a page number of other documents, and "Each description fits one thing" matched a
phrase that spans several documents; both are "Warning · advisory".

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

Slots: the Edit Task page has a standing line "Still open on this set: ..." above "Question slots". It was
already on aq-01333's 2026-10-06 capture, beside "Hard 0/2 · Medium 0/3 · Easy 0/1". On 2026-10-08, with q01
returned for revision, the line still listed Easy, a tier with one slot, so the returned question filled none.
Whether a question in review shows its held slot as open is unknown.

Re-sent panels: the user has sent an already-logged panel again, once with "check carefully and fix"
(aq-01278 q02, 2026-10-07) and once with no message (aq-01333 q01, 2026-10-08). A re-sent panel is not a new
review.
- Log it as a dated re-send. Note any line the earlier capture lacked, after checking whether it is a standing
  page line (crops differ).
- Check the pending revision against the panel field by field.
- Bring the revision up to the hand-over rules in force now. On 2026-10-08 that meant adding the targeted
  failure modes and one removal probe per ticked document.
- Hand over the whole form again.
- If the ticks changed, say that the platform needs a new difficulty result first.

## Targeted failure modes (observed 2026-10-07)

Update 2026-10-08 (from tools/check_questions.py, changed by another session that day): the form now takes,
per mode, only the trap and "How a careless solver fails", then one shared "Why these are traps" box for all modes,
at most 50 words; its counter reads whitespace-separated words (a 95-word box showed "95 / 50 words"). The floor
FAILs files that keep the old per-mode boxes. aq-02028 q01 rev 4 uses a 43-word shared reason naming Doc 2 and Doc 6.
The rest of this section describes the 2026-10-07 layout.

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

### Changed 2026-10-08: one shared reason, at most 50 words

User screenshot, aq-01937 task form, 2026-10-08. The three boxes per mode are gone. "How to fill this in",
verbatim: "Pick the trap. The thing in the documents a careless reader trips on, such as a look-alike measure
or an older figure inside a newer report. Each trap once per task." / "Pick how they fail. The first step
where a careless answer goes wrong, such as taking the wrong line item." / "Say why in one short reason.
One box for all your picks: where the trap sits (the document and passage), the wrong answer a careless
solver would give, and why your answer avoids it. At most 50 words." / "Ideas fill in a pick. Using a
question idea or a harder direction adds the trap it sets. Change it, remove it, or pick from the full
list." / "Spread your traps. Your recent mix is shown so you can vary it."

Each "Failure mode N" block keeps only "Trap" and "How a careless solver fails"; a cause option can carry
an "Under-covered" badge (e.g. "Takes the wrong line item (under-covered)": "Finds the right source but
takes the wrong line item, measure, denominator or a sibling figure."), a mix hint, not part of the label.
A mode saved under the old layout keeps its old boxes in a collapsed "Your earlier justification" (aq-01543 q04
screenshot, 2026-10-08); the picks carry over, and only the shared reason box needs filling.
After the blocks: "Why these are traps (at most 50 words)", "One short reason for all your picks, at most
50 words: where the trap sits, the wrong answer a careless solver would give, and why the correct answer
avoids it." Over the limit the counter reads "95 / 50 words — shorten it to submit": that box held aq-01937
q01's old first box, 95 whitespace-separated words, so the counter splits on whitespace.

### Changed 2026-10-09: Submit checks each pick against the trap's definition

User screenshot, aq-02208 q02 (after a difficulty pass at Easy), red box at Submit, verbatim: "Submit failed Fix
these before submitting: failure mode 1 ("Figure that must be computed"): The reason describes counting and
comparing items between two lists, but the trap definition is about computing a metric by subtracting one period
from another (full year minus first half). The question asks for a difference between two lists, not a time-period
subtraction, so the trap definition does not fit.; failure mode 2 ("Part vs total"): The reason describes counting
specific items across two lists and does not identify a subset_vs_total trap; it does not show how a careless solver
would mistake a headline total or different part for the requested transmitter-characteristic difference, nor does
it tie the failure to a misapplied rule or false premise." Raw: tasks/aq-02208/notes/platform-feedback/.

So Submit now reads the shared reason against each picked trap's own definition and against the picked cause.
Definitions seen so far: "Figure that must be computed" (derived_or_computed_metric) = a figure derived by
subtracting one period from another (full year minus first half), not any count or calculation; "Part vs total"
(subset_vs_total) = taking a headline total or a different part for the asked figure. The only other description
saved is Look-alike company's ("The documents include another company, or one with a similar name. The answer must use
only the target company's figures."). "Look-alike measure" (similar_metric_confusion), from the aq-02562 q01 Submit block
(user screenshot, 2026-10-10), verbatim: "failure mode 1 ("Look-alike measure"): The reason describes a threshold/eligibility
confusion (66.66 percent vs 75 percent crop income, and $900,000 AGI bar), not a similar-metric confusion where a solver takes
a sibling line item. The wrong answers cited ($1,125,000 and $1,500,000) arise from misapplying eligibility exceptions, not
from substituting one measure for another." So a misapplied eligibility rule or threshold is not a look-alike measure; in the
same submission "Wrong jurisdiction or scope" with "Misapplies a rule or premise" was not flagged for carrying one program's
exception into another program's rule. Pick the trap whose definition names the actual wrong route, name each trap
in the reason ("Look-alike measure: ...; Linking: ..."), give its wrong answer and say how the chosen cause produces
it. One well-fitting mode is safer than an extra loosely fitting one: any mode that fails blocks Submit. The modes are
outside the fingerprint; the Easy pass stood while they were edited. aq-02208 q02's replacement (Look-alike measure /
Takes the wrong line item; Linking across documents / Picks the wrong entity or section) passed the Submit check on the retry (user, 2026-10-09: "Passed with your first option"): "Look-alike measure" with "Takes the wrong line item" was accepted for a sibling count in the prose taken for the asked change, and "Linking across documents" with "Picks the wrong entity or section" for matching an item to the wrong section of another document. The rejected first picks had included an unobserved trap (per-station counts under "Part vs total"), against this note's own rule to declare only measured traps.

Local use:
- Write the modes in the question file's `## Targeted failure modes` (template q00.md): one
  `### Failure mode N` block per trap with `Trap:` and `How a careless solver fails:`, then one
  `Why these are traps:` line (or heading) for all modes. The floor checks the lists, at most three,
  each trap once, a reason present and at most 50 words, and fails a file that still has the old
  per-mode boxes; it warns when the reason names no Doc N. A draft or checked file without modes gets a
  WARN, and a ready file a FAIL. `--handover` prints the modes and the reason with its word count;
  JSON carries `targeted_failure_modes` ({trap, how_a_careless_solver_fails}) and `why_these_are_traps`.
- Fifty words fit one sentence per trap: Doc N and passage, the wrong answer as a number, the gold.
- Since 2026-10-09 the floor WARNs when "Figure that must be computed" sits on a question with no period word, or
  "Part vs total" on a reason that names no total or part (tools/check_questions.py TRAP_DEFINITION_CUES, from the
  aq-02208 q02 Submit block). A cue match is not a fit: still pick the trap whose definition names the wrong route.
  Verified on q02's rejected picks (both WARN) and submitted picks (none). Both suites pass with the new cases
  (2026-10-09: test_docket_tools.py 42 OK after the user had pymupdf, python-docx and beautifulsoup4 installed;
  test_docket_agent.py 45 OK).

Earlier local use (2026-10-07 form, superseded):
- The floor checked the lists, at most three, each trap once, the boxes filled and 150+ words, and
  warned when fewer than 150 words held a letter. `--handover` printed them box by box.
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

## Difficulty page after a content change (observed 2026-10-08)

The difficulty panel keeps showing the last run after the form's question changes: "Your question, answer or
documents changed after this result. Run the check again before you submit.", "Last result: Too hard", "This result is
for an earlier version of your question.", and the run's summary gains "measured on an earlier version" (aq-01937
13:59 capture, still "7 of 8 runs left"). A page saved after pasting another question is therefore not that question's
result: the user attached it as q05's "too hard" verdict, but every attempt and the run's version (d017fd) were q01's
old wording. Before recording, match the run's version, date and gold to the pasted question; check the runs-left count.

## Question length spread: live advisory (observed 2026-10-08)

The Question box showed it in orange as soon as aq-02028 q01 rev 1 (47 words) was pasted, before any full-check run
(user screenshot, tasks/aq-02028/notes/platform-feedback/q01-rev1-question-box-length-advisory-2026-10-08.png):
"Your questions so far all come out about the same length — 6 of them between 28 and 47 words, and this one is 47. A
good question can be much shorter: it only has to need more than one document, and a sharp twelve-word question does
that as well as a fifty-word one. There is no minimum to hit. This is only a warning and does not block submitting."
It measures the user's recent questions across tasks, not this question's quality. Only a length outside that band
would clear it; for a question whose exactness needs an anchor, a full universe and a rounding instruction, a
sub-28-word wording needs real compression. q01 was first kept; when the user re-sent the advisory, rev 2 cut it to
27 words (kept: the anchor's exact name, "last day", the measure, the count and the five ports; dropped: the copied
source phrase, "stevedore", "per full container"), gold unchanged. The user then answered "too easy. the previous
state was better" (no panel supplied), and rev 3 restored the 47-word wording. The advisory came back with the
band "35 and 47", and the user asked to "keep everything else and just shorten the question length": rev 4 keeps
rev 3's measure and terminal list verbatim and shortens only the opening anchor and the units, 34 words. Rev 4 at 34 words
still drew it ("6 of them between 35 and 47 words, and this one is 34"), so leaving the band does not clear it:
it reflects the user's recent questions, and leaving the band by a few words does not remove it. The earlier rule
here ("say it is non-blocking; do not compress a checked, exact question to escape it") is withdrawn. The user,
2026-10-08, after q02 rev 0 (34 words) drew it again: "it actually blocks our way when other tests all passed
... If you don't change your attitude, we can't pass forever." Rule now: treat it as a requirement. Draft new
questions at about 12-20 words, well below the lowest number it names; cut setup phrases and copied source wording,
keep the conditions that pin the answer, and simplify the design when they cannot fit. q02 rev 1 is 20 words; the
form's reaction is pending. Current rule: docket-question-length-must-clear.md.

### Difficulty gate wording seen 2026-10-13 (aq-03570, Run 3 capture)

Under the level counts the page now prints, verbatim: "Medium model: three solvers try up to 3 times each. Ready
when at least two get it wrong twice and one gets it right twice. High model: two solvers try up to 3 times each.
Ready when both get it wrong at least once and not every attempt is wrong. A level stops as soon as more attempts
could not change the result." Earlier captures said "Ready when 1–3 attempts at a level are right, out of up to 5".
Changed by 2026-10-18 (aq-06835 Run 1 capture, tasks/aq-06835/verdicts/AQ-06835_difficulty_2026-10-18_2010.txt):
"High model: two solvers try up to 3 times each. Ready when both get it wrong at least once, even if every
attempt is wrong." Captures through 2026-10-15 still read "and not every attempt is wrong".
That run read Low 0/5 · Medium 0/6 · High 5/6 and was "Between levels": "Too hard for the medium model but too easy
for the high model. Make it a little harder, so the high model reaches your answer only some of the time". So
"Between levels" also occurs between Medium and Hard, attempt counts above five appear, and some attempts are listed
with "This attempt's text was not recorded" (only right or wrong is kept). The same page carried a line "Your last 3
runs were answered from Doc 1 each time. Ask the Coach before running again." although no attempt in that run
answered from Doc 1. Raw: tasks/aq-03570/verdicts/AQ-03570_difficulty_2026-10-13_1133.txt. The same day the "One defensible answer" row showed a second failure text (aq-03570 q03 rev 1, screenshots in
tasks/aq-03570/notes/platform-feedback/q03-rev1-checks-2026-10-13-*.png): "Two materially different answers are
defensible." followed by the two readings, instead of "two independent solvers ... did not reach your gold". It came
on a label that the previous wording had carried through the same check to a difficulty run. Run 4 the same day
(tasks/aq-03570/verdicts/AQ-03570_difficulty_2026-10-13_1553.txt): "Answerable without the documents" ends the run
after the one closed-book attempt ("Low — · Medium — · High —") and still costs a run (12 to 11 of 15 left). The
page then shows "Your last 3 runs were not in band. Ask the Coach before running again." and a three-item "What to
change: Make it harder" list built from that one attempt, including "The gold answer ($1.65 trillion) is not
supported by any document in the set", which the high model's five right attempts of six on the same gold in Run 3
contradict. The form's "Needs the documents" row had passed on the previous revision with the same gold.

One question measured under both gates (aq-03170 q01, identical question, answer and reasoning; only two
necessary-document ticks changed between the runs): Run 2, 2026-10-12, five-attempt gate, Low 0/5 · Medium 0/5 ·
High 1/5, "In band — Hard tier"; Run 3, 2026-10-13, three-solver gate, Low 0/5 · Medium 2/6, "In band — Medium
tier". In Run 3 the recorded medium attempts pair up by layout (1 with 4, 2 with 5, all wrong) and attempts 3 and 6
are "Right" with no text recorded, so the result rested on a solver whose route cannot be read. The same pattern
(3 and 6 right, unrecorded) placed aq-03950 q02 at Medium; on aq-03993 the unrecorded 3 and 6 were wrong. Raw:
tasks/aq-03170/verdicts/AQ-03170_difficulty_2026-10-13_1511.txt.

## Difficulty check: "Checker unavailable" runs are not counted (observed 2026-10-13/14)

aq-04421 q01 rev 0 (platform version 4fcc5d), user screenshots, 2026-10-14. With every Check passed, Run 1
read "Did not finish" and Runs 2-10 "Checker unavailable" over about seven and a half hours, each row
showing "Medium ●●○○○" and no solver counts. The panel said, verbatim: "The checker is unavailable right
now. Nothing was counted; try again later." After Run 10 the page still read "15 of 15 runs left · 11 of
60 runs used in the last 24 h (all tasks)", so neither the task's runs nor the 24-hour count had moved.
The next attempt started ("Running", "Starting...") and was counted ("14 of 15 runs left · 12 of 60").
So a "Checker unavailable" row, and a "Did not finish" row that the runs-left line does not count, is
the platform's checker being down, not a verdict on the question: tell the user to retry later without
changing content, and to save the page so the task clock does not lapse. Contrast aq-01650 Run 2
("Did not finish", Low 0/5 · Medium 0/5 · High 0/4): that run had solver counts and was counted.
