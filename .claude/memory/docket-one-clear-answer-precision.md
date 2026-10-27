---
name: docket-one-clear-answer-precision
description: "The platform returns a numeric question as 'answered inconsistently' when, at the precision it asks for, the gold depends on which of two figures the documents state for the same input (a rounded table or summary value vs an exact appendix value); recompute with every stated figure and pick a precision at which all agree."
metadata:
  node_type: memory
  type: feedback
  updated: 2026-10-04
  originSessionId: 04463fcb-d077-4beb-9e5d-9d667b38a14a
  modified: 2026-10-06T12:42:51.360Z
---

## Current rule

- Before hand-over, list every figure the bundle states for each input of a calculation:
  summary, tables at different scales (millions vs thousands), appendix, component sums. Then
  recompute the gold with each combination. If the results differ at the precision the question
  asks, the question has two defensible answers. Change the precision, or the quantity, until
  every combination gives the same answer.
- The guide's "exact table vs rounded prose" lever is safe only when the rounded figure is
  visibly approximate: "about", "nearly", "roughly", "more than", or "$2.2 billion" standing in
  for 2,205.2. Then the exact route is the only careful one. A document may instead state the
  rounded value as the figure itself, such as a table cell "53.8" or a summary's
  "$53.8 million", beside an exact appendix value of 53,750 thousand. Then both are honest
  readings, solvers split, and the platform returns the question.
- In a blind solve, a reading that uses another stated figure for the same input and lands on
  a different answer at the asked precision is `ambiguous` (gate Q4), not the lever biting (Q11).
- A gold that depends on reading a deadline word strictly ("received ... before 30 September 2024" -> last day 29
  September) is judged "Answer not supported" when the gate's final check (high model, every document) takes the
  stated date as the last day, even when the medium model and the platform's per-attempt notes agree with the strict
  reading (aq-02360 q02, 2026-10-09). The loose reading then matches the low model, so a deadline-boundary trap
  cannot place a question in the Medium band. Do not build a gold on "before"/"after" exclusivity.
- When: every numeric question with a stated precision. Take most care with percentages built
  from figures reported at different scales, within one document or across documents.
- Rounding order can split a gold too, with no second stated figure (aq-docket-trial-01 q05, local,
  2026-10-06). A ratio of two derived shares was 2.6967, which is 2.70 at two decimals, but only
  0.0017 above 2.695: shares rounded coarsely first (0.56 / 0.21, or 56% / 21%) give 2.67. Both a
  fresh solver and the auditor listed it. A percentage-point difference of the same shares split
  under half-even rounding (35.46 exact, 35.45 from two-decimal shares, so 35.4). Recompute the gold
  from shares rounded to 0-3 decimals, half-up and half-even, and pick a precision where every
  route agrees (q05 rev 1: one decimal, 2.7 on every reasonable path).
- State a ratio's direction in the question. "A was what percentage of B?" has the standard
  reading A / B, and every local reader took it that way. Even so, a platform reviewer returned
  it as ambiguous and proposed the reversed ratio (aq-00949 q04). Write "A divided by B,
  expressed as a percentage", or name the base ("taking B as 100%"). Before accepting a
  reviewer's proposed answer, recompute it. That proposal, 65.2%, is not the reversed ratio at
  one decimal place (5,175 / 7,926 = 65.29%, so 65.3%). It is either that figure truncated or a
  wrong-column ratio (5,175 / 7,936 = 65.21%).

- A vague tie phrase makes the decoy defensible to the platform reviewer, even when the documents'
  arithmetic rules it out (aq-01278 q02, 2026-10-06, "Revision requested" after a Medium-tier difficulty
  pass). The question quoted Chubb's Q1 "2.8% in commercial insurance" and asked for Q2 "On that same
  basis"; only commercial plus agriculture reproduces 2.8%, but the reviewer wrote: ""On the same basis"
  is undefined ... Doc 9 states "North America Commercial was down 2.3%", so -2.3% is defensible; most model
  attempts gave it." The local review had called -2.3% indefensible by that very arithmetic. The fix the
  reviewer proposed names the scope with a concrete noun: "Asking for the business lines behind the 2.8%
  keeps Doc 4 necessary and makes -1.3% the only answer." The difficulty check had already printed "This
  question may be too vague: several solvers agreed on an answer that is not your gold". Treat that
  advisory, with the wrong attempts clustered on one printed figure, as a likely revision request: before
  submitting, replace the tie phrase with the concrete scope and re-measure. The reviewer also flagged
  "change" ("percentage points vs percent, absolute vs relative, which line item"): write "percentage
  change in net premiums written ... from a year earlier".
  The advisory is a count of clustered wrong answers, not a judgment of defensibility. On aq-01543 q04
  (2026-10-08, Easy pass, "You can submit now") it named 7.20% and 7.04%, the two declared traps. The
  solvers giving them had themselves noted that they contradicted the printed "23 of which are currently in
  operation". No tie phrase there, so no rewording was made; review outcome pending. Before submitting,
  check whether the clustered answer survives a careful reading of the question's own words (aq-01278's
  did) or contradicts a printed fact (aq-01543's does).
- A document's own working term creates a defensible reading. aq-docket-trial-06 q02 (local,
  2026-10-06) asked about "all U.S. credit unions without federal deposit insurance", with a gold
  that counted two uninsured credit unions. GAO-03-971 uses "depository institutions lacking federal
  deposit insurance" as its name for privately insured credit unions (its scope note and an
  appositive, D02 157 and 285), so the privately-insured-only reading (9.4% against the gold 9.8%)
  was defensible: the audit returned ambiguous and both blind solvers listed it. Any rewording that
  excluded it would have named the uninsured credit unions and given the trap away, so q02 was
  dropped. Before a trap relies on the broad literal reading of a phrase, search the documents for
  that phrase's own usage. Prefer a plain noun whose ordinary meaning is the whole set ("credit
  unions" in q01, where the narrower counts are labelled "federally insured" and "privately insured").

**Why:** aq-docket-trial-04 q03 asked for a percentage change "to one decimal place". Doc 8
states the FY2025 request as $53.8 million (summary and Table 2) and as 53,750 thousand
(Table A-1), so the change came out at -2.2% or -2.3%. Every local blind solve gave the key
(-2.3%) but listed -2.2% as a reading, and the local review counted that as the lever biting.
The platform returned it on the last attempt.

**How to apply:** in `## Lever checks`, add a "One clear answer" line that lists each input's
stated figures and the range of results at the asked precision. Prefer a precision at which the
whole range rounds to one value: trial-04 q03 moved to the nearest whole percent, where -2.18%
to -2.27% all give -2%. Keep a real decoy (a different base, period or edition) rather than a
rounding choice. See also [[docket-local-solver-calibration]] (numeric levers and the local
solver) and [[docket-form-automated-checks]] (how to write the calculation step).

## Evidence and history

- 2026-10-09: aq-02360 q02 rev 1 (raw tasks/aq-02360/verdicts/AQ-02360_difficulty_2026-10-09_0825.txt), gold 514 days to
  29 September 2024 under "before 30 September 2024": Run 2 "Answer not supported" with Low 0/5 (all 515), Medium 3/5;
  the Document check's three every-document attempts gave 515, an unfinished "4 May 2023" and 515, never weighing
  "before". Run 1 on the earlier anchor had been "Between levels" (Medium 4/5). Across both runs the medium model read
  the cutoff strictly 7 times in 10, the low model 0 in 10, the gate's high model 0 in 3.
  Rev 2 asked for "the last day an opted-out service election could still be received" to steer the high model; its
  quick test was "too easy" (user, same day): the cue that serves the high model also serves the low one. Dropped.

- 2026-10-06, aq-01321 q02 (form model check, screenshot from the user): a twelve-month (R&D + SG&A) /
  revenue ratio to two decimals, whose exact numerator exists only as a three-release rebuild, while the
  latest release says "Over the past 12 months we invested $3.9 billion in R&D and SG&A". With the
  user's wording ("total amount spent on research & development and selling, general, and administrative
  expenses"), the form blocked it: "This question is too vague to submit: two independent solvers ...
  Both answered "20.05%"" (the rounded-prose route) and listed the prose phrase among "3 matches" for the
  description ("Narrow the description."). So a rounded figure stated for exactly the asked quantity and
  window counts as a second answer even at a precision it cannot support; the rounding lever only works
  when the question's description cannot match the rounded statement (e.g. it names the income-statement
  lines), which also removes most of the pull. Mirroring the document's own verb ("spent" for "invested")
  strengthens the competing reading.

- 2026-10-04: aq-docket-trial-04 q03 rev 1, platform reviewer, returned with "This is your last
  attempt". Verbatim: "The question was answered inconsistently. Make sure it has exactly one
  clear answer that follows from the documents." Criterion: rule 4 (one correct answer). Change:
  rev 2 asks for the nearest whole percent and the gold becomes -2%; the allocation-base decoy
  (-6.3%) is kept. This is one verdict on one question, but the mechanism applies to any
  precision-sensitive gold. It qualifies the gate card's Q11 reading of "the rounded route gives
  a different answer". The floor could only flag candidates, for example a decimal-precision
  answer whose evidence holds a rounded and an exact form of one figure. A recompute across all
  stated figures, in the review step, is what catches it.
- 2026-10-05: aq-00964 q07 (2026 expected straight-line revenue minus the 2025 actual, gold
  -$167M at $1M precision), local review: the 2025 input was a visible footnote ($101.0M), but a
  cut segment-table row in the same release probably restates it "translated at prior-period
  foreign currency exchange rates" (the table's own footnote), so it could print 99-102 and give
  -165 to -168. A cut row can state a differently measured figure for the same input, not only a
  duplicate. Held out of quick tests until a complete capture or a re-pinned quantity. Local
  reviewer finding, one bundle; see also [[docket-series-editions-necessity]] (cut rows).
- 2026-10-05: aq-00949 q04 rev 2, after its Easy-tier difficulty pass and submission. The platform
  page showed "Revision requested" ("Add clarity for the order of mathematical operation." /
  ""was what percentage of its total debt" can be interpreted to put Q2 2026 numbers in numerator
  or denominator. This is ambiguous"). It also showed "The reviewer proposes a different answer",
  YOURS 153.2% against PROPOSED 65.2%. The proposal was wrong at the asked precision (5,175 /
  7,926 = 65.29%; 65.2% is that figure truncated, or the December 2025 column's 65.21%). Rev 3
  states the division ("... divided by ..., expressed as a percentage"). Its fresh checks: two
  matches (one solver ruled out percent change because of "divided by"), audit clear, review ready.
  The review noted that rev 2's Low 3/5 was at the top of the window, and clearer wording may
  remove a miss route.
  Platform reviewer feedback, one question. Possible floor WARN (not built): a "was what
  percentage of" ask.
- 2026-10-06, aq-01321 q02 follow-up (user report): the narrowed version passed the difficulty check
  "evaluated as Easy Tier", so narrowing the description to the income-statement lines cleared the
  "too vague" block. Exact tested wording not supplied.
- 2026-10-10 (aq-02686 q02 rev 0, platform Run 2, Version a9ec06, "Answer not supported"): a condition attached
  as an opening phrase, "Barring FEOCs, it exports both to ... and one to a Thai buyer [a FEOC]", was read by the
  gate's high model in all three every-document attempts as "FEOC status aside": the sentence asserts the export,
  and FEOC status does not change the other regime's notice duty, so the buyer stayed in ($46,026 against the gold
  $45,920). The intended reading was "except to FEOCs". How to apply: when a scenario's rule comes from one regime
  and the counted obligation from another, say what the actor does in its own sentence ("It refuses FEOC buyers")
  and describe the candidates as orders or prospects, not as completed actions.
