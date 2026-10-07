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
| Restricted names | block | The question, answer and reasoning use none of the names on the restricted list. | not checked: the list is not captured |
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
