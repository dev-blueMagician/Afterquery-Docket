---
name: docket-form-automated-checks
description: "The task form checks every number in the reasoning: in a 'Doc N' step it must be in that doc or come straight after '='; in an uncited step it must be in some doc or already derived. A gold answer with commas or 'and' reads as an unordered list."
metadata:
  node_type: memory
  type: feedback
  updated: 2026-10-04
  originSessionId: 9f128bdc-b5c0-4b21-a95f-f6bdf88cc634
  modified: 2026-10-07T13:40:38.144Z
---

## Current rule

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
  - So compute each value once, at the precision the question states, straight after "=", in
    the step that cites the document its inputs come from. The conclusion step may reuse values
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
- Derive the rest (components, documents, tags) works from the reasoning's quoted text. When the
  quoted words were not verbatim, it missed that document, proposed another one ("Document 6 is
  marked as needed but has no quote from it") and the wrong component ("2Q 2026" for a "2Q 2025"
  answer). Keep every quoted phrase verbatim and check its proposals by hand.
- Gold answer: the form reads commas and "and" as list separators. When the question gives no
  order, it warns: "The answer lists several items, but the question does not say what order to
  give them in." Write a two-part answer (a name plus a value) as one item. "Rheumatoid
  arthritis/lupus dataset (10.1%)" did not trigger it. For a real list, state the order in the
  question. For an unordered set, write "in any order" rather than imposing alphabetical order,
  because a name variant can reorder an alphabetical list without changing the set. Write names
  that contain "and" as abbreviations ("SEC", not "Securities and Exchange Commission"). Whether
  the form accepts "in any order" is not yet seen. A two-ask answer with a comma counts as a list
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

**How to apply:** structure reasoning as one step per document, each giving the document's
figures and then "a / b = result (precision)". Then a conclusion that reuses the derived values,
then the decoy citing its document. Before handing over, emulate the check: for each line, every
number is in the cited document, follows "=", or (in an uncited line) is in a document or
already derived.

## Evidence and history

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
