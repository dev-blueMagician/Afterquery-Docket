---
name: docket-form-automated-checks
description: "Distinguish cited printed inputs from labeled derived calculations; numeric-parser workarounds are observations, not guaranteed rules. A gold answer with commas or 'and' can read as an unordered list."
metadata:
  node_type: memory
  type: feedback
  updated: 2026-10-09 (floor check tools/form_numbers.py)
  originSessionId: 9f128bdc-b5c0-4b21-a95f-f6bdf88cc634
  modified: 2026-10-08
---

## Floor check since 2026-10-09

The floor runs the reasoning number check itself: `tools/form_numbers.py` (tests in
tools/test_docket_tools.py, class FormNumbers), called from `check_questions.py` and so from
`--handover` and `prepare`. Each predicted miss a rewording could fix is a FAIL with its cause. A
figure the cited document states in words or past the read depth, inside an evidence quote from that
document, is an expected false alarm and a WARN; a `ready` question gets WARNs only. Genuine misses
must never reach a hand-over again ([[docket-reasoning-numbers-must-clear]]).
It ports emulator v10 (aq-02157) with page Doc numbers and these changes from recorded results:

- The first bare calculation anywhere in a step is evaluated, also after a label and "=" (aq-01960
  q02 rev 1 "gross profit in billions of dollars = 3.15 × 60.7% = 1.91205" passed; v5-v10 bound it to
  the first "="), and a chain without brackets is evaluated ("1.91205 + 1.9608 + 2.03077 + 2.17074 =
  8.07436" passed, aq-01960 Step 9). "×" and "x" multiply.
- Since 2026-10-10 a calculation step that spells out a number of ten or more ("twelve", "thirty") loses
  its result exemption and FAILs; a chain mixing operators ("a × b + c") is a WARN. Write every
  calculation as one two-operand "a op b = r" and keep number words out of calculation steps. The user
  rewords reasoning before pasting, so say with the hand-over that each "a op b = r" must stay as typed
  (evidence: aq-02626 q03, below).
- Steps start at "Step N" with any punctuation ("Step 1 (Doc 7):", aq-01321 q02, whose Steps 1-8 the
  form passed); step and document references ("Steps 2, 4 and 8", "Docs 10 to 13") are not figures.
- A range still cites only its first document (strict: one-document rules apply) and draws a WARN to
  write "Doc N and Doc M". Recorded results conflict: aq-01960 rev 1/2 Step 9 ("Docs 10 to 13") reused
  earlier results unflagged, while rev 2 Step 13's message named "Doc 10" alone.
- A single digit the document spells out passes (aq-02505 q01 Step 2: "five" -> "(5)"). A number of
  10 or more printed only in words (107, 187), or digits printed only past 60,000 characters, is a
  WARN "expected false alarm" when an evidence quote from the cited document holds it (the user knew
  aq-02505 q01's two were wrong warnings, 2026-10-09), else a FAIL. Digits first printed between
  20,000 and 60,000 characters are a WARN.
- Replay on 2026-10-09: aq-02505 q01 rev 0 gives exactly the form's two flags (as expected false
  alarms); aq-02102 q01 rev 2,
  aq-02028 q02 rev 2 and aq-02157 q01 rev 5 stay clean as on the form; aq-02157 q04 rev 3 and
  aq-02220 q01 give their deep-text flags. Known miss: aq-01321 q02 Step 9 ("Twelve months ended June
  30, 2026: 1,942 + 1,999 = 3,941", flagged by the form, exact by every recorded rule).

The task helper paths below (form_check_v5, v6, v10) are history; do not run them instead of the floor.

## Current arithmetic guidance — 2026-10-08

The user explicitly asks that Step-by-Step Reasoning distinguish what a document prints from
what the author computes. Use numbered steps with these labels:

- **Source fact (Doc N, location):** give the printed value, unit and relevant scope, supported
  by a verbatim quote. Attribute only printed facts to the source.
- **Calculation/derived (from steps X and Y; Doc N and Doc M):** show the equation and its
  result with units. Refer to the source-fact steps or earlier derived steps for every operand,
  retaining the contributing Doc numbers. For example, if sourced inputs are 5 units per group
  and 10 groups, write `5 units/group × 10 groups = 50 units` as a calculation; never say that
  a document prints 50 merely because it supplies an operand.

The form evaluates only a bare `a op b = r` (operators + - * /, operands written as numbers, no words
such as "million TEU" or "TEU per trip" between an operand and `=`; units go after the result), and
it accepts `r` only when it equals the value exactly (float noise allowed; a result written with "%"
passes when it rounds correctly). Otherwise it reads `r` as a figure claimed from the cited documents
("Step 5: Docs 1 and 8 don't mention 1.152 million"). So: no scale words inside expressions, no
rounded results ("= 329,000 (to the nearest thousand)" failed), and pick inputs whose quotients
terminate (2.88 / 3.5 never does). Before every hand-over, run the reasoning through
tasks/aq-01543/notes/helpers/form_check_v5.py, which reproduced aq-02028 q02 rev 0's three flags
exactly (user screenshot, 2026-10-08); rev 1 passed it after the rewrite. v5 missed one rule the form applies: in a
step citing exactly one document, an earlier step's result is not accepted (aq-02102 q01 rev 1, user screenshot
2026-10-08: "Step 10: Doc 4 doesn't mention 112. Check the document number." for "Calculation (Doc 4) ... 112 / 117 =
95.7265%", 112 and 117 being Steps 7-8 results, while steps citing "Doc 2 and Doc 4" used the same results unflagged).
So put a calculation with derived operands in a step citing every contributing document, or drop it. Use
tasks/aq-02102/notes/helpers/form_check_v6.py (v5 plus this rule; reproduces that flag and still clears aq-02028 q02).
Blind spot and reuse rules (aq-02157, user screenshots 2026-10-08): the check uses the task page's Doc numbering
(aq-01543 q01 Step 2 passed with "37,963", printed only in page Doc 1). It reported printed numbers as missing when they
sat far into a long document (Doc 2 "£8.46" at character 80,370; Doc 4's "122." and "£262.90" near 84,000, still flagged
when written "8.46 pounds"); numbers up to character 19,581 have passed. Bulleted lists are read: q01 rev 3's Steps 1-2
passed with rates printed only in dash-led lists ("-  14.8% in Scotland"), which disproved the list blind spot inferred
from rev 2. A step citing two or more documents accepts a number mentioned in any earlier step only as the identical
string (q04 rev 1 Steps 3 and 5 reused "347.86" and "8.46"; q01 rev 2's "13.8" after "13.8%" was flagged, and passed in
rev 3 once Step 1 wrote "13.8 per cent"). A result written "= 15.6 per cent" was not accepted later as 15.6 (q01 rev 3
Step 13, the only flag), nor was one described before its expression ("The rate for Northern Ireland in 2030 in %:
14.0 + 1.6 = 15.6 (the highest...)", the user's rewording of rev 4, 2026-10-09: "Step 5: Docs 3 and 1 don't mention
15.6.", the label matching no step of the box), while results followed by "percentage points" or "pounds" were reused
unflagged, as was a plain result whose operand carried "%" (aq-01960 q02 "3.15 x 60.7% = 1.91205"). Glued commas
("paragraph 3.7,", aq-02102) and currency signs ("$3.15", aq-01960) passed, so the comma and currency rules first
guessed from q04 rev 0 are refuted. So: write a source number once, in the form every later step will repeat ("14.8 per
cent", reused as 14.8); never reuse a result typed as a percentage (by "per cent" or "%" after it, or "in %" before its
expression), and never subtract two such results: route the last steps through plain or percentage-point quantities
(aq-02157 q01 rev 5: 2022 gap 14.0 - 13.9 = 0.1 plus widening 1.6 + 7.2 = 8.8 gives the 2030 gap 8.9, instead of
15.6 - 6.7; aq-01543 q01 needed the same restructure after revs 2-5); expect a flag per source step whose numbers sit
deep in a long document (not fixable by wording); prefer inputs printed near the start of their documents. Emulator:
tasks/aq-02157/notes/helpers/form_check_v10.py (v6 plus deep-text truncation, the identical-string and percent-typing
rules; reproduces the flagged numbers of q01 rev 3, the user's q01 rev 4 and q04 rev 1, and keeps aq-02102 q01 rev 2
clean; the 60,000-character truncation is an assumption). It does not explain q01 rev 2's Step 1-2 flags or its passes on plain 12.7, 14.0 and 13.9
(that pasted text was the user's rewording and was not captured). A gold with a
decimal, even an exact one ("8.9 percentage points"), drew the Gold answer box's "Say the rounding (e.g. 'to one
decimal place').": state the precision in the question (aq-02157 q01 rev 1).

Keep one calculation per numbered step and put its result directly after `=`. A calculation
step whose head cites no Doc reads its step references ("Steps 3 to 5") as numbers that no cited
document prints: cite the contributing Doc numbers in the head, or name the inputs instead
(aq-01937 q04/q05 rev 0, local emulation, 2026-10-08). Label ordinary
mathematical constants, such as 100 for conversion of a ratio to percent, as conventions rather
than sourced figures. Retain exact intermediates or full calculation precision and round the
final answer once to the precision requested in the question; do not invent source precision.

Quotes and evidence support the printed operands, scope and other necessary conditions. A
computed gold need not appear verbatim in any document. Do not fabricate a quotation or force
all operands into one document to appease a warning. Every necessary document must remain
indispensable to the derivation. The reported behavior below is historical evidence, with some
unconfirmed parser hypotheses; this format makes provenance explicit but guarantees no platform
result. It adds no mandatory local model diagnostics.

## Recorded form behavior and historical workarounds

- The form's full quality-check list (captured 2026-10-04) is in
  `reference/platform-quality-checks.md` and is mirrored by the floor and gate Q14. It adds
  answer components (1-10 pieces of the answer; every number in the answer in one; every
  component backed by a quote of 12+ characters), no semicolon in the answer, and a separator
  between answer parts.
- Reasoning field: the form checks every number in every step.
  - In a step that names a document ("Doc N"), a number must occur in that document, or be the
    result straight after "=" in a calculation, e.g. "979 / 9,671 = 10.1% (to one decimal
    place)". A restatement such as "or 10.1%" or "which rounds to 10.1%" is flagged: "Step 1:
    Doc 2 doesn't mention 10.1%. Check the document number."
  - In a step that names no document, a number must occur in some document or earlier in the
    reasoning. A new calculated value there is flagged: "Step 3: Which document says 10.123%?
    Add 'Doc N'."
  - Earlier workaround: compute each value once, at the precision the question states, straight
    after "=", in the step that cites the document its inputs come from. The conclusion step may reuse values
    already derived. A decoy line cites its document and puts its computed value after "=".
  - Do not put an unnumbered line restating a result ("Conclusion: total debt grew 53.2%.") right
    after the calculation step, and keep each calculation a simple a-op-b. aq-00949 q04's
    "(7,926 - 5,175) / 5,175 = 53.2%" was flagged citing Doc 1 and Doc 7 ("Step 3: Docs 1 and 7
    don't mention 53.2%") and again citing Doc 7 alone. Two explanations fit and are not yet
    separated: the form attaches the unnumbered conclusion to the step, so its restated 53.2% is
    flagged like "or 10.1%"; or the parenthesised subtraction blocks the "=" exemption ("979 /
    9,671 = 10.123%" and "1,484 + 538 = 2,022" passed). Rev 2 drops the conclusion and divides once.
  - Put one "=" calculation in each numbered step. A step holding five semicolon-joined sums had
    its first result accepted and its second flagged: "Step 3: Doc 7 doesn't mention 2,193.
    Check the document number." plus "Step 3 needs a document reference."
  - Write the result as a plain number right after "=" and each operand exactly as the cited Doc
    prints it. aq-01960 q02 rev 0 (2026-10-08, user screenshot) was flagged "Step 2: Doc 10 doesn't
    mention $1.91205 billion" for "implied first-quarter gross profit = $3.15 billion × 60.7% =
    $1.91205 billion" (Steps 4 and 6 alike), and "Step 8: Doc 13 doesn't mention 0.6072" once 60.72%
    was rewritten as a decimal. In the same field "fiscal 2026 GAAP gross profit = 13,579,476 -
    5,255,060 = 8,324,416 thousand dollars", "8.07436 billion dollars = 8,074.36 million dollars" and
    a step citing "Docs 10 to 14" passed. Rev 1 ("... in billions of dollars = 3.15 × 60.7% =
    1.91205") cleared those steps. It then flagged "Step 13: Which document says 8,074.36 million?
    Add 'Doc N'." for the uncited "8.07436 billion dollars = 8,074.36 million dollars", while the
    uncited "8,324,416 thousand dollars = 8,324.416 million dollars" passed. Give every step whose
    result is new a document citation; a range ("Docs 10 to 13") worked in Steps 9 and 14. Rev 2 did
    that for Step 13 and the next run flagged both conversions: "Step 12: Which document says 8,324.416
    million? Add 'Doc N'." (it had passed the run before) and "Step 13: Doc 10 doesn't mention 8,074.36
    million." So a range is read as its first document, and a pure unit conversion ("A = B", no
    operator) gets no "=" exemption anywhere. Avoid conversion steps: rev 3 ends with one cross-unit
    subtraction, "8,324,416 thousand dollars - 8.07436 billion dollars = 250 million dollars" (form
    result pending). The check is not fully stable between runs.
- Derive the rest (components, documents, tags) works from the reasoning's quoted text. When the
  quoted words were not verbatim, it missed that document, proposed another one ("Document 6 is
  marked as needed but has no quote from it") and the wrong component ("2Q 2026" for a "2Q 2025"
  answer). Keep every quoted phrase verbatim and check its proposals by hand. A reasoning step that
  names a decoy's printed figures can also come back as a proposed evidence row for the answer
  component, which the form's "Evidence supports its component" advisory then flags ("does not seem to
  support that component ... the reasoning explicitly notes this is not the value used"). Untick such
  proposals: evidence rows carry only the component's value or its inputs (aq-01650 q01, 2026-10-08).
  The page keeps an accepted row through later pastes, even after the reasoning stops naming the decoy
  (aq-01543 q01, 2026-10-08), so after each paste compare the form's quote count with the hand-over's.
- Gold answer: the form reads commas and "and" as list separators. When the question gives no
  order, it warns: "The answer lists several items, but the question does not say what order to
  give them in." Write a two-part answer (a name plus a value) as one item. "Rheumatoid
  arthritis/lupus dataset (10.1%)" did not trigger it. For a real list, state the order in the
  question. For an unordered set, write "in any order" rather than imposing alphabetical order,
  because a name variant can reorder an alphabetical list without changing the set. Write names
  that contain "and" as abbreviations ("SEC", not "Securities and Exchange Commission"). Seen
  2026-10-11 (aq-02750 q06): with the tail "List them in any order." the advisory "Answer format stated"
  passed, and the advisory "Asks about the world, not the set" warned instead ("an answer-protocol tail
  ("in any order") ... Ground rule 10"). The two advisories pull against each other for an unordered set;
  neither blocks. Default now: no order tail on an unordered list, since the grader accepts any order when
  none is asked. 2026-10-12 (aq-03170 q01 rev 0): that default drew the order warning again on a three-name
  list, and the user sent the panel as "2 checks failed" (the other was Reasoning tags, failed because the
  ticks were not on the page; whether the user counted the advisory as the second failure is my reading). So
  before hand-over look for an order the facts themselves give, without ties, and ask for it in the question
  (rev 1: "Earliest second letter first.", by each commenter's second-letter date). Observed the same day on
  rev 1: the format advisory still warned (that sentence was not read as an order), "Asks about the world, not
  the set" passed, and the Question box added "\"second letter\" points to where the answer is ... name the thing
  you mean instead" (an ordinal read as a pointer). So write the order with the check's own words ("in date
  order", "alphabetically", "in any order") and keep ordinals out of the question; rev 2 uses "List them
  alphabetically", result pending.
  2026-10-12 (aq-03169 q02 rev 1): a two-ask gold written as two labelled sentences ("Less concentration: a, b, c.
  Lower audit quality: d, e") failed the blocking "Short answer" check and drew "Answer length" ("Answer is 32 words,
  4 items"): the form splits on commas only, so a label and a sentence break fold into the neighbouring items (13 and
  12 words). The tail "Give each list in any order." drew the rule-10 warning again while "Answer format stated"
  passed. The local floor had shown only WARN list-items ("cannot determine every list boundary"), which I explained
  away: treat that WARN as a predicted "Short answer" failure and rewrite the gold as one plain comma list (a short
  parenthetical tag per item when two asks share the list) before hand-over. Rev 2 does that with "List each group
  alphabetically.": the difficulty runs went ahead on that gold and it was submitted at Hard (Run 5), so a
  five-item comma list with a two-word bracketed tag per item clears "Short answer". The floor now WARNs
  `short-answer` on a colon label or a sentence break inside a list gold.
- Components must cover every number in the answer as a whole number. An answer "8 CFR 1003.42, 1208.13, ..."
  with components "1003.42", "1208.13", ... failed the blocking check "Components match the answer"
  ("Your answer includes 8, but no component contains it", aq-02750 q06, 2026-10-11). Put a citation prefix
  inside a component ("8 CFR 1003.42") or leave it out of the answer. The floor compared digits as
  substrings and let it through; fixed the same day to compare whole numbers. A two-ask answer with a comma counts as a list
  too, and an order given only as "Give the Bahrain quarter first." did not clear the warning:
  use the word "order" ("Give the two quarters in that order", "in date order"; whether "in that
  order" clears it is still unconfirmed). The local floor misses this: its order check runs only
  for list answer types and accepts the bare word "first".
- Hand-over: give every form field in its own labelled block each time, question first. A field
  pasted into the wrong box produces warnings that are not about the question. Reasoning in the
  Question box gave "Over 80 words" and, on the gold answer, "Say the rounding". Since 2026-10-07,
  `python tools/check_questions.py tasks/<slug> --handover --q qNN` writes them all, in the form's order,
  to notes/handover-qNN.md: Question, Number of asks, Gold answer, Step-by-step reasoning, Answer
  components, Evidence rows, Necessary documents with roles, Reasoning tags and Targeted failure modes.
  It uses the task page's Doc numbers, one evidence row per component, and fenced boxes with wrapped lines
  joined. See [[docket-handover-all-form-fields]].
- Comparison wording (rule 9c, the platform's "PIN3"): "which ... fell by the largest
  percentages" was flagged: "'largest' could be read as largest absolute drop or largest
  relative drop. You may want to specify which." The flag came even though both readings give
  the same ranking. Name the measure and its base, e.g. "the largest percentage declines from
  their February 2020 levels". The local floor's superlative check misses this wording.
- When: every question with a calculation or a two-part answer. The local floor checks none of
  this, so emulate it on the reasoning before handing fields over.
- Unconfirmed: the rule is inferred from two form reports on one question. Look at the form
  after pasting. Also open: a calculation whose inputs come from two documents has no
  single-document home; aq-docket-trial-04 q03 puts it in a step naming both ("Doc 3 and Doc 8:
  a / b = result"). In aq-00949 q04 the form flagged a two-document step's result, but also the same
  calculation citing one document, so the expression shape was the likelier cause; prefer one cited
  document whose text prints every operand of a simple calculation.
- Timetable rows in Federal Register agendas print dot leaders ("End of Extended Comment
  Period...... 04/05/24"). Quote the label, the leader and the date as one verbatim span; a quote
  that starts at the date runs into the next row ("04/05/24 Final Rule"), which a reviewer read
  as a final-rule date. The local floor treated any "..." as an ellipsis join until 2026-10-05;
  it now accepts dots that occur contiguously in the cited document. Whether the platform's
  verbatim check accepts the leaders is not yet seen.
- Treat a date as one value and check it whole: "March 21, 2023" needs a cited document that
  prints that date (or 03/21/23), not one that merely holds "21" and "2023" somewhere. A month
  restated from a day date ("April 2024" for a printed 04/26/24) counts as unprinted, like "or
  10.1%"; write the printed value ("from 11/00/23 to 04/26/24 = 5 calendar months"). Do not
  spell out derived counts ("seven rulemakings", "the other four") in a cited step; list the
  items or put the count after "=". This comes from local review, not from the form.

**Why:** the form flagged q01 of aq-docket-trial-01 twice after the floor, blind solves and
reviews had passed it. The first fix (moving calculations to an uncited step) was itself
flagged. See also [[docket-platform-guide-newer-than-instruction]].

**Historical application advice (superseded by the current arithmetic guidance above):**
structure reasoning as one step per document, each giving the document's
figures and then "a / b = result (precision)". Then a conclusion that reuses the derived values,
then the decoy citing its document. Before handing over, emulate the check: for each line, every
number is in the cited document, follows "=", or (in an uncited line) is in a document or
already derived.

## Evidence and history

- 2026-10-10, aq-02626 q03 rev 0 (user screenshot of the form; the box held the user's reworded steps, Step 4 out of
  view): "Step 4: Docs 2 and 6 don't mention 365. Check the document number." Rev 0's Step 4 read "days in a common
  year, taken as twelve 30-day months plus the calendar's net 5 extra days: 12 × 30 + 5 = 365". No line appeared for
  Step 5 ("365 × 3 + 1 = 1,096", a mixed chain with no number word), Step 6 ("180 − 5 = 175"), Step 7 ("1,096 + 175 =
  1,271") or Step 1's 18, 19 and 2022, which Doc 2 prints only at characters 30,362 to 55,122. My reading (inference):
  the spelled "twelve" is the likelier cause, because the one earlier unexplained flag, aq-01321 q02 Step 9, also
  began "Twelve months ended June 30, 2026: 1,942 + 1,999 = 3,941", and the mixed chain in Step 5 passed. The floor
  had predicted no flag; tools/form_numbers.py now FAILs a number word of ten or more in a calculation step and
  WARNs on a mixed chain. Not yet known: whether Step 1's deep numbers passed (that would put the form's read depth
  past 55,000 characters) or the form simply showed one line; ask for the whole orange block next time.

- 2026-10-09, aq-02505 q01 rev 0 (user screenshot, tasks/aq-02505/runs/q01-r0-form-2026-10-09/form-screenshot-1.png): totals
  printed only in words were flagged ("Step 1: Doc 2 doesn't mention 107." for "One hundred and seven entities" at character
  36,837 of 47,676; "Step 7: Doc 6 doesn't mention 187." for "One hundred and eighty-seven entities" at character 39,816),
  while the same paste's Step 2 "five entities (5)" and "twenty-five entities (25)" (Doc 2 characters 1,040-1,111; no
  standalone 5 anywhere in Doc 2) drew no flag, contrary to emulator v10. Not separated: number words read but deep text
  unread (the limit would lie between 19,581 and 36,837), small numbers skipped, or substring matching. Calculation steps
  reusing 107 and 187 as identical strings passed. When a design's only source of a figure is a spelled-out total late in
  its document, expect one unfixable flag per such step; prefer designs whose inputs a document prints as digits or early.
- 2026-10-09, aq-02486 q01 rev 0 (user screenshot, tasks/aq-02486/runs/q01-r0-form-2026-10-09/form-screenshot-1.png): a
  number the question itself supplies (a hypothetical request of 225 photocopied pages), stated in an uncited Step 1, drew
  "Step 1: Which document says 225? Add 'Doc N'." although unticked Doc 4 prints "$225"; the ticked Docs 5 and 7 never
  print 225. So "occurs in some document" is not enough for an uncited step, and no wording passes a scenario number that
  no ticked document prints. Fix used (rev 1): choose the scenario number among values a ticked document prints (216, Doc
  5's "p. 216."), introduce it in a step citing that document, and reuse it as the identical string in steps citing two
  documents. Emulator v10 reproduces the flag (it treats uncited steps as accepting only earlier strings). When designing a
  hypothetical-request question, pick the request size from the cited documents' printed numbers at sketch time.
  Read depth, same paste: the form showed only that one flag, so Steps 2-5's printed inputs passed, including Doc 5's
  0.10 and 25 (first printed at characters 43,740 and 44,330) and Doc 7's 100 and 25.00 (50,573 and 50,854). The live
  check therefore reads to at least about 50,900 characters; tools/form_numbers.py (OBSERVED_PASS 19,581, written the
  same afternoon by another session) still WARNs on such inputs, a false alarm until its bound is raised.
- 2026-10-08, aq-01543 q01 (user screenshot of the same panel; tasks/aq-01543/runs/q01-platform-unbound-2026-10-08/):
  "1. 22.8 percentage points · 5 quote(s)" where every hand-over had four. The fifth quoted Doc 1's decoy paragraph
  ("From September 2024 to August 2025, electricity consumption..."), which only revs 0-5's reasoning Decoy line had
  named; revs 6-8 had no Decoy line. Orange: "... does not seem to support that component. The quote covers
  September 2024 to August 2025 and gives a nuclear share of 40.38%, which is a different period and figure than
  the 2024 annual 41.6% used in the calculation. It is not used by the component. ..." Fix: delete the row in the
  form; no question-file change. Second observation, after aq-01650 q01.

- 2026-10-08, aq-01650 q01 rev 1 (user screenshot of the "Components, evidence, documents and tags"
  panel): an evidence row for component 1 quoted Doc 5's decoy row "Financial literacy|15,228|15.2|6.6||"
  (complete cases), which the hand-over's seven rows never contained. Reasoning Step 9 names that decoy
  ("the descriptive table's financial literacy mean of 15.2 covers only the 15,228 complete cases"), so the
  row most likely came from "Derive the rest". Orange advisory: "The quote from document 5 for component 1
  ... does not seem to support that component ... Use a quote that gives the value, or a figure or fact you
  used to work it out." Fix: delete the row in the form; no question-file change. One observation.

- 2026-10-06, aq-01321 q02 (form screenshot from the user): "Step 9: Docs 7, 8 and 9 don't mention 3,941.
  Check the document number." Step 9 read "(Doc 7, Doc 8, Doc 9): Twelve months ending June 30, 2026:
  1,942 + 1,999 = 3,941", a result straight after "=" from derived operands. Steps 7 and 8 had the same
  shape (results 1,999 and 1,942, printed in no document; labels "First half of 2026", "July to December
  2025") and passed, and the later "3,941 / 19,453 = 20.26%" passed. Working explanation: the label named
  the exact period the cited document reports as a rounded figure ("$3.9 billion" over the past 12
  months; its "For 12 Months Ended June 30" table), so the checker treated 3,941 as a claimed document
  figure. Fix offered: relabel the step as a sum of half-years, or compute it in one step whose operands
  are all printed values. Result of the fix pending.

- 2026-10-04, first paste (rev 3): "Doc 2 doesn't mention 10.1%" and "Doc 5 doesn't mention
  43.6%". "= 10.123%" in the same steps passed, while the "or 10.1%" restatements were flagged.
  The answer "…dataset, 10.1%" triggered the order warning.
- 2026-10-04, second paste (rev 4): the uncited calculation step was flagged ("Which document
  says 10.123%? Add 'Doc N'"), so the earlier advice to move calculations to an uncited step was
  wrong and is replaced above. The order warning was gone. The Question box held the reasoning
  by mistake. The form's words are verbatim in q01's Feedback log. One question so far.
- 2026-10-04, third paste: no reasoning warning under the rev 4 rule. "Say the rounding (e.g. 'to
  one decimal place')" still showed under the gold answer while the Question box held a 31-word
  text instead of the 36-word question ending ", to one decimal place?". The check looks for
  the precision in the Question box, not the answer.
- 2026-10-04, aq-docket-trial-03 (local review): a token-level emulation passed two slips that
  question-review caught. One was a hearing date in a step citing Doc 1 and Doc 4; only Doc 3, 6
  and 7 print it. The other was the derived counts "seven" and "four". A stricter scratch
  emulation (whole dates in any printed form; spelled-out counts flagged) reproduced both. These
  are local reviewer findings and are unconfirmed on the form.
- 2026-10-04, aq-docket-trial-06 q03 (local review and blind solve): the reviewer flagged the
  same two slips, "February 2004" in a step citing a testimony printed as "February 24, 2004",
  and derived counts ("the other two", "Of the four rejected agencies"). Asking for an
  alphabetical answer backfired: the blind solver noted that "Board of Governors of the Federal
  Reserve System" would sort first. "List them in any order" replaced it. All local; nothing
  from the form yet.
- 2026-10-05, aq-00949 q01 rev 0 (form quality check pasted by the user): a two-ask gold of two
  quarters joined by a comma (answer_type date) drew "The answer lists several items, but the
  question does not say what order to give them in. Say how to order them (for example "in
  date order" or "alphabetically"), or say that any order is fine." The question ended "Give the
  Bahrain quarter first." The floor showed no format WARN. Rev 1 says "Give the two quarters in
  that order."; the form's reaction is pending.
- 2026-10-05, aq-docket-trial-03 q01 rev 2 (local review): the c2 quote "04/05/24 Final Rule"
  ran into the next timetable row; the fix needed the dot-leader span, which the floor's
  ellipsis rule rejected. tools/check_questions.py gained verbatim_found() (contiguous match,
  dots included) and test_dot_leader_quote_is_one_passage; both suites passed (25 and 19).
- 2026-10-05, aq-00949 q03 (form panels pasted by the user; question and answer of rev 1, with the
  user's own rewording of the reasoning). Step 3 held five sums joined by semicolons: the form
  flagged the second result (2,193) and asked for a document reference, while the first (2,022)
  passed. Step 1's quotes were not verbatim, and Derive the rest proposed Doc 6 instead of Doc 1
  and the component "2Q 2026". Rev 2 put one sum per step and verbatim quotes; the form's reaction
  to rev 2 is pending. One question; the exact parsing rule is inferred, not documented.
- 2026-10-05, aq-00949 q04 (two screenshots of the form's reasoning box): "(7,926 - 5,175) / 5,175 =
  53.2%" was flagged citing Doc 1 and Doc 7, then again citing Doc 7 alone. In q03's paste a first "="
  result printed in no document (2,022, from "1,484 + 538") had passed. Rev 1 asks for a ratio
  ("7,926 / 5,175 = 153.2%") and rev 2 also drops the unnumbered conclusion line, which the
  rev 1 review suggested as the likelier cause; the form's reaction is pending.
- 2026-10-06, aq-00949 q05 rev 0 (form screenshot from the user): "Step 1: Doc 1 doesn't mention 5,175" and
  "Step 2: Doc 7 doesn't mention 7,926", although both documents print those figures. Only the figures
  written straight after the quoted table label "Current and Long-Term Debt (GAAP) - (b)" were flagged;
  plain "cash of 2,028" / "cash of 4,907" passed. Step 3, citing "Doc 1 and Doc 7", passed with derived
  operands from steps 1-2 ("61.91% - 39.19% = 22.7 percentage points"): derived operands in a cited
  step are accepted, at least when the step names the documents they came from. Working rule: write
  table figures as plain text ("current and long-term debt of 5,175"), not right after a quoted label
  (especially one ending in a parenthesised letter); rev 1's result on the form is pending.
- 2026-10-06, aq-01320 q01 rev 2 (user screenshot of the form after pasting): a signed computed answer
  ("-$0.28 per share", question "what was the actual full-year figure minus that range's midpoint?")
  drew the advisory "Doc 12 states $10.44; your answer has -$0.28. Use it, or say in the question to
  compute it from the other figures" plus the same for Doc 11's adjusted range and "1 more stated figure
  differ": the stated-figure matcher keys on the line-item words even when the question asks for a
  difference no document prints, so treat it as a false positive. "= -0.28" in a step citing "Doc 10 and
  Doc 12" (derived operand 10.72) showed no number warning. Derive the rest proposed "Cross-document
  join, Aggregation" for a date-in-force edition question (Temporal alignment is the accurate tag) and
  the note "Doc 12 on its own may give enough to compute the answer", although Doc 12 lacked both
  outlook figures and a removal probe without Doc 10 could not determine the answer (forced guess was
  the decoy). Unlike aq-00949 q01, where the same note was a real guessability signal, check the named
  document's content and run a removal probe before acting on it.
- 2026-10-08 (aq-01937 q04/q05, local emulation only, no platform paste): the aq-01543 form_check_v5
  emulator read "-66 / 401 = -16.5%" as 66 / 401 (its first-operand pattern had no unary minus, and "-?"
  bound only to the comma-number alternative), so it flagged a correct signed result. The bundle copy
  tasks/aq-01937/notes/helpers/form_check_v5.py groups "-?(?:OPERAND)"; a wrong control result is still
  flagged. Whether the live form accepts a negative first operand is unconfirmed; mathjs does.
- 2026-10-10 (aq-02673 q03, floor only, no platform paste): tools/form_numbers.py reads a decimal figure that is
  directly followed by a comma as its integer part ("0.15 times 3,446.1, giving" was read as 3,446 and FAILed
  "Docs 3 and 6 don't mention 3,446"), because its token pattern refuses a comma after the number. Put a unit or
  word after every figure in a reasoning step ("3,446.1 mt dw to give"). Whether the live form splits the same
  way is unobserved.
- 2026-10-10 (aq-02686 q02, user screenshot of the form): "Quote 12 does not appear word for word in document 4.
  Copy it exactly from the document." for an evidence quote that occurs exactly once, character for character,
  in the saved capture and in docs/ (156 characters, starting mid-sentence, at character 67,193 of 85,760). The
  eleven other quotes passed. Cause not established: the page reports 85,767 characters for that document and
  the capture normalises whitespace, so the live text may be spaced differently there, or the paste was altered.
  The floor's verbatim check runs on the capture and cannot see this. The user did not know what "quote" meant:
  say "evidence row N" and give the row's opening words. Practical rule: when the form rejects a quote the floor
  accepts, drop that row if another row carries the point, or have the user copy the passage from the page.

## Verbatim check rejected a byte-identical quote (2026-10-14, open)

aq-04807 q02 rev 0, user screenshot: "Quote 1 does not appear word for word in document 4. Copy it exactly from
the document." The quote ("the EPA interprets the CAA not to require the state to have EPA-approved contingency
measures ... approved section 179B(b) demonstration") is byte-identical in the saved capture of Doc 4 (offset
215,717 of the capture) and in docs/. The other six quotes, including the same sentence's twin in Doc 7 without a
hyphen ("EPA approved"), drew no message. Cause not established; the quote's one unusual feature is the hyphen in
"EPA-approved". Rev 1 used a hyphen-free span of the same sentence, and its difficulty run (Run 2) started, so the
blocking checks passed on it (inferred; the Checks panel was not captured); until then, prefer quote spans without hyphenated compounds when a shorter span carries the input, and if
the message recurs ask the user to compare the form's row text with the hand-over block (a "Derive the rest" row can
differ from what was pasted).
