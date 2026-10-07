# Docket lessons: historical evidence

**V2.1 policy, 2026-10-05:** New target Easy minimum, optional Medium/Hard. Use the current
instructions/playbook. Previous maximum-only rules and D1-D7 claims below are historical;
no saved positive result calibrates them. Generate evidence dependencies, run a separate
question-only shortcut audit, require two supported matching fresh solves and exact-content
fingerprints, and report a tier pass only from explicit platform evidence. Capture gaps receive candidate-specific impact review; relevant/unknown gaps and missing
needed material block readiness. Concrete unaffected-gap assessments preserve incomplete warnings.
Generate lean hook sketches before full write-up; use applicable lever checks, original phrasing
from factual notes, independent calculation/date checks and set review. Ordinary valid
cross-document arithmetic/ID joins remain eligible; historical simplicity warnings are not bans. Do not reinstate obsolete rules from these historical entries.

Knowledge file for the Docket Writer project: the rules the workspace has learned, mostly from
platform verdicts, each with its evidence. Read it before sketching, checking or handling feedback.
The playbook cites these as L1-L11.

Origin and calibration. These lessons come from eight bundles worked in the Claude workspace
(aq-docket-trial-01 to -07 and aq-00745, 2026-10-04 and 2026-10-05). The local solver then was
Claude Opus 5.5 at max effort. How GPT-6.1 Sol behaves as the local solver is not yet measured, so
record every platform verdict beside the local results (playbook §12) to recalibrate. One verdict
on one question is evidence, not yet a universal rule.

New lessons use the block format in playbook §12. Update this file and upload it again after each
change.

## L1. Historical maximum-only policy

Historical rule: `ready` meant maximum difficulty, judged against the platform's reviewer model (the
"high model"), not survival and not our own solver. Ready needs the gate's Q1-Q12 and Q14 (fair) and
Q13: D1-D7 hold in the documents and in both blind solves' paths, on one or two levers with at most
two conditions in the wording; two fresh blind solves reach the key or miss only on the lever; the
closed-book solve misses; the review rates difficulty `maximum`; and the platform's difficulty check
on that exact wording reached the High tier without "Too easy" (a low, medium, high ladder, five
attempts each). A local `maximum` is a prediction: report it as "passes the local gate",
never as maximum difficulty. A blind-solve `match` is the fairness proof, not a failure; a
`wrong-lever` is a bonus, not a requirement. A failed D-check means below maximum: status
`checked`. Harden through the evidence, never by stacking conditions. Before the first sketch
round, scan for item sets that span documents; if the only shared entities are agencies, programs
and dates, say so then, not after three numeric rounds.

Why: the user, 2026-10-04: "I want maximum level", then "not maximum model. if high model can't
solve, it's good design for Q/A", then "the high model is not the claude model. it's the Docket
platform reviewer model."

Platform results so far, all quick tests by the low model:
- Every question quick-tested was solved: trial-07 q05 and trial-03 q04 (both rated maximum
  locally) and trial-04 q05 (rated below maximum, failing D3, D4 and D7).
- trial-03 q04 was reported to the user as clearing the full gate. The user: "hey, you told me it's
  maximum. but in platform it's too easy". Its deciding date sat in another agenda under the same
  RIN (a direct link, not a bridge), and the naive reading of a projected date already gave the key.
  Since then: ready needs a survived quick test, D3 works out every naive reading, and a shared
  identifier fails D4.
- D4 was briefly made a preference, then restored in full after two of two questions that failed
  it were solved ("no decoy to trip on"). Lesson: do not relax a check that targets decoys before a
  platform result supports it.
- trial-04 q05, the user's reaction: "is this your max difficulty?" Never hand over or quick-test a
  below-maximum question as a candidate; report it as below maximum and keep designing or stop.
- aq-00745 q01 (2026-10-05): "Too easy", tiers "Low 5/5 · Medium — · High —".
  - The check is a ladder: the medium and high models run only if the low model fails often
    enough. So ready needs the High tier reached without "Too easy", and the tier line is
    recorded verbatim.
  - The Coach: the wording "increase Abbott's taxes" maps to the documents' "net tax expense", so
    "a simple keyword match ... surfaces the two correct quarters immediately". The platform
    matches meaning, not tokens.
  - The five saved tracks went through every release, read each quarter's own note, and set
    aside the year-to-date totals and comparatives. A filter over statuses each item prints in its
    own entry is a lookup filter (D7).
  - The local review had predicted below maximum (D3, D4, D7 failed).

## L2. "Too easy" signals and the local solver

Current rule: the local blind solver is the fairness check, not the difficulty target. Its `match`
shows the documents settle the key; its path is the difficulty evidence. The Claude solver solved
about fifty sketches across seven bundles, numeric and qualitative levers alike: it found scattered
dates, read flattened chart tables, recomputed by hand, checked prose against tables and named the
decoys. Expect a strong solver to solve fair sketches, and read the path for these platform "too
easy" signals:

1. A lookup-only path: every fact one plainly stated sentence, the lever labelled in the text ("we
   treat X as our main analysis"), one obvious calculation. Platform (trial-01 q01): "too easy: it
   can be answered without careful work across the documents".
2. A common-knowledge bridge, such as official recession dates, which a model supplies without the
   bridging document (trial-07 q01: "the low model found it all in Doc 5").
3. A passage that names, ranks or lists the answer's items, even for an overlapping period.
4. Labelled figures plus one standard transformation (year-to-date to quarter), even with a trap
   that flips the sign (trial-02 q01: "a clean two-step subtraction with no ambiguity in the
   figures, no decoy, and no tricky alignment").
5. Single readable cells in exhaustive tables, even across two documents with a chart extreme
   deciding which cell (trial-07 q05, the Coach: "no prose to parse, no rounding to reconcile, no
   decoy to trip on").
6. A bridge fact printed in any single passage, even in a document the question does not point at,
   or an edition choice that is simply the earliest or latest (trial-03 q01: "Answered from one
   passage in Doc 6. That's the shortcut to close.").
7. A shared identifier (RIN, docket number, citation, table code, unchanged title) that links the
   item across documents (trial-03 q04).
8. A naive reading that already lands on the key (trial-03 q04's projected date).
9. A decoy disproved beside itself, or one the question's own wording excludes. Example
   (aq-00998 q03 rev 0, local): "how many points higher was A than B" fitted only the gold pair,
   so the same-release decoy (A < B) was flagged by the question itself. Ask "A minus B" when a
   decoy flips direction; a "which of A or B" wording fails the form's giveaway block.

What reads as close work: a bridge, where a fact in one document decides which fact to take from
another; facts put together from two passages (an appendix number, a figure label read against the
prose); a decoy a quick reader takes. The Coach's suggested levers: an exact table figure against a
visibly approximate prose figure, and pieces scattered so no single passage has the answer.
Stacking three or more conditions does not raise the bar; it makes a rulebook.

First platform pass (aq-00964 q01, 2026-10-05, "In band — Medium tier", Low 0/5 · Medium 1/5):
an event reported only in the latest release (a June 15 sale) selects the forecast current at that
date, which sits in the previous, middle edition (April 28); the latest release prints its own
later forecast (July 28) with a different value. All nine wrong attempts took that same-document
later forecast. The local Claude solvers matched and the local review called it marginal, so the
local path underestimated it. One result, evidence for this mechanism only.

Tier tuning (aq-00745, 2026-10-06): tiers are Low 1-3/5 right = Easy; Low 0/5 then Medium 1-3/5 =
Medium. One closing-day edition trap (the range "in force when it completed its acquisition" vs the
reporting release's own later range) drew Low 1/5 = Easy. Adding a second date trap (a dividend's
payment vs declaration date) drew 0/5 at every level = "Too hard": low fell for the first trap 5/5,
medium and high passed it 9/10 but fell for the second 9/10. The release's "Updates Guidance to
Reflect Acquisition" headline tipped careful models off. For Medium, use one same-document trap
without such a tip-off, and keep anchors that cannot move when the question is reworded.
Then the same single-trap layout with an event the release never ties to its guidance change
(trial results announced "In March", printed beside the April release's own later range) passed
at the High tier (user report, aq-00745 q09). Tied event = Easy; untied = High: for exactly Medium,
weaken the untied trap slightly rather than strengthening the tied one.

Platform gate wording (difficulty check, 2026-10-06): "Ready when 1–3 attempts at a level are
right, out of up to 5. A level can settle early, for example at 1 right out of 3." An Easy result needs
the low model to miss at least two of five. aq-00998 q03 (an April 2025 event reported in the previous
quarter's release, with that release's own same-label figures as the decoy) was "Too easy", Low 5/5:
the printed month made the period step trivial, and both inputs sat in one sentence.
aq-00949 q03 (2026-10-05) was "Too easy", Low 5/5: a rule stated in one plain sentence (the 2020
plan's "Net cash from operating activities is expected to fund both capital expenditures and
dividend payments") applied to six quarters of labelled rows in the latest supplement. A
free-cash-flow decoy in the same table caught no attempt, and removing the question's cues did not
help. When a definition selects the answer, the definition itself has to need close reading.
aq-00998 q05 (2026-10-06) reached the window, "Low model 2/5 right": a stated full-year method
applied to a period no release reports (twelve months ended June 30, 2026), to two decimals, where
about ten near-miss methods give a different value. The gate still failed on the removal test (L4); at
three decimals it passed, "In band — Easy tier" (Low 3/5), the first Easy pass on that bundle.
Rounded prose beside its own exact table is no trap (aq-00949 q04). Rev 2 ("total debt at June 30,
2026 was what percentage of its total debt at the end of 2019?", one decimal) reached Easy, Low 3/5
(user report). The platform reviewer then returned that wording as ambiguous about which figure to
divide by. Rev 5 ("end-2019 debt divided by June 30, 2026 debt", two decimals) was "Too easy", Low
5/5 (2026-10-06): three of five attempts quoted the rounded "$5.2 billion" sentence and still used
the exact 5,175 printed beside it. The Easy result most likely came from the misreading, not the
lever. Re-measure after any wording fix. The rounding lever needs the exact figure somewhere a quick
reader does not look.

Wording: when the documents report year-to-date figures, say "three months ended". The Coach
flagged "quarter ended September 30" as open to a year-to-date reading.

User preference (2026-10-06, trial-02 and trial-05): the user asks for questions shaped like
trial-02 q01 and trial-06 q02. Those are numeric answers that no document prints, derived over three
or more dependent steps through a carve-out, a definition or a footnoted remainder, with a printed
same-label decoy in the reader's path. Try that shape before list or filter questions. When no fair
one exists, say so plainly; fairness rules still win.

## L3. General-knowledge check

Current rule: the platform returns a question a model can answer without the documents ("The
question can be answered from general knowledge, without the documents. Ask something only the
documents can answer."). This verdict is separate from "too easy". Widely reported public facts
count even when every one is quoted from the bundle: a notable rule's publication date and comment
period, famous event dates, headline company or survey figures. Anchor the answer on at least one
fact a model cannot know: a document from after likely model cutoffs; a planned or internal value
(an agenda's target month, a footnote's docket citation, a comment tally, a document-specific
classification); a bridge only the bundle states. A public fact may sit on the path but cannot be
the whole path. Run a closed-book solve on every sketch and write-up; a correct or near answer, at
any confidence, is a fail.

Evidence:
- 2026-10-04 (trial-03 q01, returned on its last attempt): days from a train crew rule's extended
  comment close to its final rule. The local closed-book solver recalled every date.
- Planned or internal values and post-cutoff documents defeated the closed-book solver; well-known
  proposals and final rules did not. In trial-06, GAO-level detail about agency roles was general
  knowledge (two sketches dropped); deciding facts only in a report's reply to agency comments held.
- 2026-10-05 (aq-00964 q03, local): a closed-book solver estimated an actual-versus-initial-guidance
  gap from wrong inputs and still hit the gold ($240M). Gaps of a predictable size (a few percent of
  a known base) are guessable; prefer answers with no natural prior.
- 2026-10-05 (aq-00745, local): a closed-book solver recalled a company's 2025 guidance history and
  its January 2026 full-year range, so three sketches answered by the range in force at a dated event
  were dropped. Answers needing facts first printed from April 2026 on all missed. Treat headline
  figures printed before about April 2026 as possibly known.
- 2026-10-06 (aq-00745, local): two more closed-book solves reached a gold built from the January
  and April 2026 guidance ranges ("a faint recollection" of the April range). Anchor on facts
  printed from about July 2026 for this company; the July range stayed unknown.
- 2026-10-05 (aq-00745 round 3, local): answers computed only from tables were still estimated
  when economics or habit sets their size: a gross margin change across an acquisition closing
  (gold +0.9 pp, guess +0.8 from the target's margin), an operating margin change (gold -3.27 pp,
  guess -2.50) and an EPS beat over the guided midpoint (gold +$0.03, guess +$0.02, "the company's
  usual pattern"). Sub-business dollar changes drew "unknown". Prefer table answers with no
  economic or habitual prior.
- 2026-10-05 (aq-00998, local): a closed-book solver extended a public streak count ("13 straight
  quarters" in 2Q 2025, so 17 by 2Q 2026) and ordered four 2025 events from a public closing date
  plus the inference that an asset acquired with it was sold afterwards. Avoid answers a model can
  extrapolate from a public count or a known event order.
- 2026-10-05 (trial-03 q03, local): four closed-book runs recalled DOT's Section 610 plan
  conventions (fall-to-fall years from 2018, the "Year 8" window, the FHWA exclusion OST rules cite)
  and once FHWA's real part ranges on the wrong row. Tables an agency reprints in every edition are
  partly in memory: ask for the printed content (a part range), not a label a known cycle yields.
- 2026-10-05 (aq-00949, local): a closed-book solver named the investor-relations contact listed in
  both a March 2020 and a May 2025 company release (medium confidence), and set the media-only decoy
  aside. Boilerplate names in a large company's press releases are recallable.
- 2026-10-06 (aq-00998, local): for a which-quarters list over 2024-2026 debt balances, two
  closed-book runs each held the one item that recalled 2024-2025 debt and cash reach, and missed
  the rest, which sat in 2026 releases. A mega-cap's pre-cutoff quarter-end balances are
  recallable; keep at least one deciding item in post-cutoff documents.
- 2026-10-06 (aq-00949 q07, local): a closed-book run reached a dividends-declared total over
  3Q 2025-2Q 2026 ($3.06) by recalling the early (deal-day) declaration and assuming the constant
  $1.02 rate continued. A constant post-cutoff value is guessable: the deciding post-cutoff item
  must be one that moves.
- 2026-10-06 (aq-01322, local): a closed-book run reached a February 2026 guidance range ("7% to 9%"
  revenue growth) while believing it was the November 2025 initial range. Word-valued rows ("Flat")
  and derived quarter or carve-out figures missed. Prefer word-valued or derived answers over a
  mid-cycle percentage range a model can pattern-match.

## L4. Series editions and necessity

Current rule:
- A fact in more than one document (repeated editions, a footnote repeated in a proposal and its
  final rule) makes none of them individually necessary. List only documents whose removal leaves
  the question unanswerable. Quote a repeated fact from one source, leave that document unlisted, and
  explain in Lever checks (the floor WARNs "quoted but not listed").
- Give every listed document an edition-unique fact: a value a later edition supersedes, the only
  actual date beside earlier planned months, the only edition covering the whole window.
- Planned dates (month only, no citation) cannot show that something did not happen in a window.
  End a "between X and Y" window inside the period the latest edition demonstrably covers.
- Boilerplate repeated word for word across editions is not evidence of edition order. Use dated
  headers and explicit cadence statements.
- Cut rows count as duplicates. A capture with "[... N characters not shown on the page ...]"
  markers lacks text the platform shows. Earnings-release tables carry prior-period comparatives, so
  a cut table may state the fact you build from other documents. Never build on a figure a cut table
  could state outright; flag unavoidable risk at hand-over.
- Year-to-date tables can stand in for a quarter: a six-, nine- or twelve-month figure can force a
  quarter's sign, making that quarter's release unnecessary. Run the removal test against the
  year-to-date tables for every listed quarter at once.
- Common knowledge counts as a duplicate: a document whose only contribution is a fact strong
  models know is not necessary in practice.
- The platform's difficulty check runs its own removal test ("Document check": "The high model
  answers with every document, then once with each document you marked necessary left out"); if
  the answer is still reached, it shows "A marked document may not be needed" and the gate does
  not pass. A rounded figure in the remaining documents taken at face
  value counts when it lands on the gold at the stated precision; a bound that merely leaves the
  gold possible is not enough. Recompute without each listed document using the rounded figures
  and pick a precision where that differs. For a needed document the platform offers a one-line
  reviewer note (200 characters; its example: the document "holds the item your question
  excludes"); any edit to the question, answer, reasoning or necessary documents clears it.
  Grading was strict at three decimals: 10.871 against a gold of 10.869 counted as a different answer.
  In a list question, expect the high model to rebuild an item from another document's flows or
  year-to-date columns when its own document is left out.
- Local removal probe: give a fresh solver a copy of the document packet with one marked document
  removed (a neutral folder name: "removal-noD02" told one probe what was missing), the verbatim
  question, and the instruction to answer or commit to a forced guess with its probability. It
  catches guessable inputs (a habitual top-3,000 screen at p 0.8; a dataset's three labelled
  classes at p 0.3) and entity coincidences: when a bridge document only picks one entity from a
  per-entity table, check every entity's value under the same computation (trial-06 q02: Indiana's
  21 / 214 equalled Idaho's 21 / 214 = 9.8%, so the probe without the bridge guessed the gold).
- Anchor an event on its completion ("closed the divestiture", "completed the sale"). A loose verb
  ("divested") let a probe without the only dating document reach the gold (p 0.5) by reading the
  verb as an earlier step (held for sale) that the gold edition's own release disclosed and tied to
  its guidance change (aq-01322 q01, 2026-10-06); the completion wording moved the probe off the gold.
- Year-to-date rebuilds make an original-quarter release replaceable in a restatement carve-out:
  full-year minus Q4 minus six months rebuilds the original third quarter (aq-01322 q03, 2026-10-06).
  Choose a period whose original and restated sides each come from one irreplaceable document (there:
  calendar January-June 2025) and list only those.

Evidence: trial-03 q02 and q03 (two revision rounds each), trial-02 q01 and q05, trial-03 q05, and
trial-07 q01 (platform: "the entire answer lives in one document"). aq-00745 (2026-10-05, local):
the latest half-year release reproduced every first-quarter dollar cell (half minus quarter) and the
restated prior-year comparatives, so the first-quarter release was necessary only for its growth
rates, quarterly EPS range and dated events; check the latest year-to-date release first.
aq-00998 q05 (2026-10-06, platform difficulty check, screenshot): a twelve-month ROCE to two
decimals scored "Low model 2/5 right" (inside the window) but was flagged "without document 10":
another release's rounded 5.4% quarterly ROCE, taken at face value, gave 10.8707%, the gold 10.87.
At three decimals the exact answer is 10.869% and that route 10.871%. The three-decimal revision passed
("In band — Easy tier", Low 3/5); without Doc 10 the high model answered 10.871%, so Doc 10 was needed.
aq-00949 q04 (2026-10-05, user report of an Easy pass): Doc 1's only input, a pre-cutoff public
figure (end-2019 debt 5,175), was recalled exactly by every local closed-book run, yet the platform
reported a pass; provisionally, an exact recalled figure did not count against its document the way
widely known dates did (trial-07 q01). The document-check line itself was not supplied, and the
later wording fix (rev 5) failed as "Too easy" before any removal-test line appeared, so this
stays unconfirmed.

## L5. One clear answer: figure choice and precision

Current rule: before hand-over, list every figure the bundle states for each input of a calculation
(summary, tables at different scales, appendix, component sums) and recompute the gold with each
combination. If the results differ at the asked precision, the question has two defensible answers:
change the precision or the quantity until every combination agrees. The "exact table vs rounded
prose" lever is safe only when the rounded figure is visibly approximate ("about", "nearly", "more
than", "$2.2 billion" for 2,205.2). A rounded value stated as the figure itself (a table cell
"53.8" beside an appendix 53,750 thousand) is an honest reading, so solvers split. In a blind
solve, a reading that uses another stated figure and lands on a different answer is `ambiguous`,
not the lever biting. Record the figures and the range in a "One clear answer" line.
State a ratio's direction: write "A divided by B, expressed as a percentage" (or "taking B as
100%"), not "A was what percentage of B?". The standard reading of the latter is A / B, but a
platform reviewer returned it as ambiguous (aq-00949 q04, 2026-10-05: "can be interpreted to put
Q2 2026 numbers in numerator or denominator") and proposed the reversed ratio as 65.2%, which is
wrong at one decimal place (5,175 / 7,926 = 65.29%, so 65.3%; 65.2% is that figure truncated, or a
wrong column's 65.21%). Recompute any proposed answer before accepting it.
A document's own working term creates a defensible reading: before a trap relies on the broad
literal reading of a phrase, search the documents for that phrase's own usage. Trial-06 q02 asked
about "all U.S. credit unions without federal deposit insurance" (gold counting two uninsured ones),
but GAO-03-971 names privately insured credit unions "depository institutions lacking federal
deposit insurance", so 9.4% (privately insured only) was defensible against the gold 9.8%; it was
dropped. Prefer a plain noun whose ordinary meaning is the whole set ("credit unions").

Evidence: 2026-10-04 (trial-04 q03, returned on its last attempt): "The question was answered
inconsistently. Make sure it has exactly one clear answer that follows from the documents." The
gold flipped between -2.2% and -2.3% "to one decimal place"; rev 2 asked for the nearest whole
percent (-2%) and kept a real decoy (a different base).
- 2026-10-05 (aq-00964 q07, local review): a visible footnote gave the input ($101.0M), but a cut
  segment-table row probably restates it at prior-period exchange rates (99-102), moving a
  $1M-precision gold. A cut row can hold a differently measured figure for the same input.

## L6. Overview exposure

Current rule: at sketch time, read the capture's "## Bundle overview" for the documents a sketch
relies on: summaries, date lists, names and figures. If they yield the answer, both conditions of a
filter, a named survivor, a needed figure, a bridge date or a deciding date, the question is
exposed and D2 fails. Prefer a sketch whose deciding fact the overview leaves out or blurs (an
unnamed party, a state-versus-federal distinction, the scope of a motion, a buried list item).
Exposure breaks no rule; use it to choose between fair sketches. Whether the platform's solvers see
the overview is unknown. Record exposure in Lever checks and at hand-over.

Evidence: trial-05 q02 (the whole filter was in exactly the qualifying summaries); aq-00745 q02 and
q03 (bridge dates printed in overview summaries, counted as D2 failures).

## L7. Local ids and platform Doc numbers

Current rule: `extract_text.py` numbers documents D01, D02, ... alphabetically by file name; the
task page numbers them Doc 1, Doc 2, ... in its own order. Build the mapping at intake (manifest
against the capture's "### Doc N · <file>" headings) and record it in the doc map and session file.
Everything typed into the form uses Doc N: the reasoning's citations (the form checks each step's
numbers against the document it names) and the evidence passages. Local files keep Dnn. Check even
when the orders look the same.

Evidence: trial-07, where D01 = Doc 3, D03 = Doc 1, D04 = Doc 5 and D05 = Doc 4.

## L8. The form's automated checks on reasoning, answers and wording

Current rule:
- Reasoning: in a step naming "Doc N", every number must be in that document or come straight after
  "="; "or 10.1%" or "which rounds to 10.1%" is flagged ("Step 1: Doc 2 doesn't mention 10.1%.
  Check the document number."). In an uncited step, a new calculated value is flagged ("Step 3:
  Which document says 10.123%? Add 'Doc N'."). So compute each value once, at the stated
  precision, straight after "=", in the step citing its inputs' document.
- Dates are whole values, and derived counts are not spelled out in cited steps (local review
  findings; unconfirmed on the form).
- Gold answer: commas and "and" read as list separators. Without a stated order the form warns:
  "The answer lists several items, but the question does not say what order to give them in."
  Write a name plus a value as one item; use "in any order" for unordered sets; write names that
  contain "and" as abbreviations. Whether the form accepts "in any order" is not yet seen.
  A two-ask answer with a comma counts as a list too; "Give the Bahrain quarter first." did not
  clear the warning, so name the order with the word "order" ("in that order", "in date
  order"); whether "in that order" clears it is unconfirmed.
- Precision: the form looks for the rounding in the Question box ("Say the rounding (e.g. 'to one
  decimal place')").
- Hand-over: every field in its own labelled block, question first. Reasoning pasted into the
  Question box gave "Over 80 words" and a rounding warning on the gold answer.
- Comparison wording (the platform's "PIN3"): "which ... fell by the largest percentages" was
  flagged: "'largest' could be read as largest absolute drop or largest relative drop. You may want
  to specify which." It was flagged even though both readings gave the same ranking. Name the
  measure and its base, e.g. "the largest percentage declines from their February 2020 levels". The
  local floor's superlative check misses this wording, so check it by hand.
- Unconfirmed: the reasoning rule is inferred from two form reports on one question. Look at the
  form's warnings after pasting, and log them.
- Evidence quotes from table rows: a complete page capture renders the table blocks that an
  earlier capture hid as Markdown pipe tables ("| Gross Margin | 23,327 | 1,824 | 25,151 |"), but
  the platform's own text shows such rows without pipes (a form warning quoted one as "Other
  International (C) - - - - - - - 4 1"). Quote prose or plain rows where they carry the input;
  otherwise copy the row with the page's Save passage and use that exact text (inference,
  unconfirmed on the form). The local floor accepts such a row quoted with or without the pipes
  (tool change, 2026-10-05).
- No unnumbered conclusion line restating a result right after the calculation step, and one
  simple a-op-b calculation per step: "(7,926 - 5,175) / 5,175 = 53.2%" followed by "Conclusion:
  total debt grew 53.2%." was flagged whether the step named two documents or one. Either the
  restated 53.2% or the parenthesised subtraction caused it; not yet separated (aq-00949 q04).
- One "=" calculation per numbered step: a step holding five semicolon-joined sums had its first
  result accepted and its second flagged ("Step 3: Doc 7 doesn't mention 2,193. Check the document
  number." and "Step 3 needs a document reference.").
- Derive the rest builds components, documents and tags from the reasoning's quoted text. With
  quotes that were not verbatim it missed Doc 1, proposed Doc 6 ("Document 6 is marked as needed
  but has no quote from it") and the component "2Q 2026" for a "2Q 2025" answer. Keep quoted
  phrases verbatim and check its proposals by hand.
- Write table figures as plain text, not straight after a quoted table label: "shows "Current and
  Long-Term Debt (GAAP) - (b)" of 5,175" drew "Step 1: Doc 1 doesn't mention 5,175" (and the same
  for 7,926 in Doc 7) although both documents print the figure, while "cash of 2,028" passed.
  A final step citing "Doc 1 and Doc 7" passed with operands derived in the earlier steps
  ("61.91% - 39.19% = 22.7 percentage points"). The plain-text fix's result is pending (aq-00949 q05).

Evidence: trial-01 q01, three form pastes on 2026-10-04 (the first fix, moving calculations to an
uncited step, was itself flagged). aq-00949 q05 rev 0 (2026-10-06): a step citing two documents
with derived operands passed.
aq-00745 / aq-00949 (2026-10-05): pipe-table rendering of formerly hidden table blocks. aq-00949 q03
(2026-10-05, form panels pasted by the user): the one-calculation-per-step and Derive the rest
observations; the parsing rule is inferred from one paste.

## L9. An accepted question is finished

Current rule: a question with status `submitted` or `accepted` never changes: not its question,
answer, documents, tags or reasoning, and it is never exported again with changes. Later findings go
into its Feedback log or the bundle's notes, and into a lesson if they generalise. A `rejected`
question is revised in place, with the platform's words logged first. Read the status before any
edit.

Why: in an earlier workspace, asked to make a passed bundle "pass all validations", an edit changed
the submission and sent a passed item back through review for no gain.

## L10. Bundle patterns from local reviews

Current rule: patterns that decided whether a bundle could reach maximum. Each comes from local
review of one bundle unless marked; check the intake scan against them.

- Date-only joins: when only dates join the documents, a date bridge is two lookups (D7) and is
  usually printed in the overview (D2). (aq-00745: three write-ups, all below maximum)
- Earnings-release series: post-cutoff facts are printed outright, and two-statement inferences rest
  on pre-cutoff facts, so D1 and D7 pull against each other. (trial-02)
- Collections of unrelated documents (articles, rulings) where each series or ruling lives in one
  document: every decoy is refuted inside its own document, so D4 cannot hold. Stop and report.
  (trial-05, trial-07; trial-07 q05's low-model solve is platform evidence)
- Agency sets: the deciding fact tends to be printed beside a searchable name, and a stated reason
  can reach past the named items, so D4 and one defensible answer pull against each other. Check
  where each candidate is first named in the document that excludes it. When an exclusion names who
  did something, reword it so the condition applies to every candidate the evidence touches.
  (trial-06)
- Agenda series: the projected-vs-published lever works only when the question's time anchor is the
  named edition itself; anchoring on a later date hands the reader the right edition. (trial-03)
- A decoy works only if the wording admits it: year-to-date or level figures that the question's
  unit word rules out are not decoys. A peak at the first or last period is an edition shortcut.
  (aq-00745 round 3)
- Shared item sets are necessary but not sufficient: a strong solver reads every candidate and
  checks the companion documents. (trial-03)

## L11. Authorship

Current rule: record origin accurately (`gpt`, `user`, `claude`, or a join) and update it when
authorship changes. The paste-ready sheet takes only `origin: user` questions; report other locally
ready questions as not exportable rather than relabelling them. The form's "Before you submit" list
includes "I wrote this question myself."; at hand-over, say plainly that it cannot be ticked
truthfully for gpt-written content, and leave that decision and the platform's AI-use terms to the
user. The form's own-words checks are not part of this workspace's quality check (the user,
2026-10-04): do not report them at hand-over, and never restyle text to get past them. Keep
explicitly requested verbatim content as given.

Evidence: all seven trial captures list "I wrote this question myself." among the 11 items, and the
form tells the contributor to "write the question, answer and reasoning yourself".
