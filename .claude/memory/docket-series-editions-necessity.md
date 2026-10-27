---
name: docket-series-editions-necessity
description: "Bundles with several editions of one series repeat facts across editions; each listed document needs an edition-unique fact, planned dates cannot prove something did not happen in a window, and repeated boilerplate is not evidence of edition order. Rows cut from a capture count as duplicates too (comparative columns)."
metadata:
  node_type: memory
  type: feedback
  updated: 2026-10-04
  originSessionId: 9e8d8c8c-aa4d-457b-a7c1-04fe73680640
  modified: 2026-10-07T08:32:23.919Z
---

## Current rule

- A document that only defines or labels the asked population is not necessary when a reader would assume
  the same set without it. Removal test at sketch time: delete the document and name the gold component
  that becomes unreachable, not merely unconfirmed. Each ticked document must supply its own gold component
  or an exclusion that changes the answer (aq-02501 q01: DoD's "less than honorable" list is every
  characterization but honorable, so the other document's own list already gave the whole answer).
- When the difficulty page says "A marked document may not be needed", repair the dependency before
  submitting. The page's one-line reviewer note unblocks Submit ("an admin must sign it off"), but the
  reviewer returned aq-02501 q01 the next day: "Only document 3 is necessary." What worked: keep the measured
  ask word for word and add a parallel second ask whose value only the weak document states; the next run
  read "Needed document 3 ✓" and "Needed document 5 ✓" and stayed in the Medium band.
- When a fact appears in more than one document (repeated editions of a series, or a footnote
  repeated in a proposal and its final rule), none of those documents is individually necessary.
  List only documents whose removal leaves the question unanswerable. Quote a repeated fact from
  one source, leave that document unlisted, and explain in `## Lever checks` (the floor WARNs
  "quoted but not listed"; answer it). Do not rely on the form's "or..." alternatives to rescue
  such a document: in the one observed case the check still left out the marked document alone and
  reached the gold from its twin (aq-02147 q01, below). If the needed input sits in two documents,
  change the input, not the ticks.
- Updated 2026-10-13 (aq-03950 q02, page text): the Document check now states "Documents you marked as
  alternatives of one another are left out together, and are needed when the answer without all of them is
  wrong or changes." A witness's title printed word for word in the report and in her own transcript was
  ticked as Doc 1 with Doc 7 in its "or" box; the check ran "Without documents 1 and 7" twice and returned
  "Needed document 1 or 7 ✓" both times. So when one input is printed in two documents and the answer still
  needs one of them, tick one and put the other in its "or" box; that is what the box is for. The aq-02147
  observation above predates this text. The bullet above still holds when the answer needs neither twin.
  Do not warn the user about such a tick or prepare a repair for it before the form has refused it.
- Give every listed document an edition-unique fact. Good examples are a value a later edition
  supersedes (an unextended deadline beside a stated extension), the only actual date beside
  earlier planned months, or the only edition that covers the whole window.
- Planned dates (month-only, no citation) cannot show that something did not happen inside a
  question's window, because editions can be stale. End a "between X and Y" window inside the
  period the latest edition demonstrably covers, with every still-planned date after it.
- Boilerplate repeated word for word across editions (a preamble sentence) is not evidence of
  which edition came before which. Use dated headers and explicit cadence statements.
- Cut rows count as duplicates too. In a capture with "[... N characters not shown on the
  page ...]" markers, the platform shows the full documents. A cut table may repeat a fact you
  quote from another document, because earnings-release tables carry prior-period comparatives
  (year-to-date cash flow for both years, the year-ago quarter in segment tables). Treat a likely
  cut duplicate like a visible one. Prefer facts that stay edition-unique even counting
  comparatives, such as current-period highlights. Never build on a figure that a cut table
  could state outright (a full-year segment table answers a sum-the-quarters question). When the
  risk can't be avoided, flag it in `## Lever checks` and at hand-over.
- Year-to-date tables can stand in for a quarter. When a question turns on a quarter's sign
  (grew or fell), a later release's six-, nine- or twelve-month figure can force that sign: a
  first half of -0.7% with a second quarter of +2.5% makes the first quarter negative. That
  makes the earlier quarter's release not individually necessary. Run the removal test against
  the year-to-date tables too. List only the releases whose quarter no other table can pin, and
  quote the rest as unlisted sources.
- Common knowledge counts as a duplicate. A document whose only contribution is a fact strong
  models know without the bundle (official recession dates, famous event dates) is not
  necessary in practice: the solver answers from the other document plus memory. The local
  removal test passes such a question; the platform does not. Anchor the cross-document step on
  a fact only the bundle states, such as a document-specific date, threshold, classification or
  count. See [[docket-local-solver-calibration]].

- The platform's difficulty check runs its own removal test, the "Document check": "The high model
  answers with every document, then once with each document you marked necessary left out. A
  document is needed when the answer without it is wrong, or changes from the every-document answer,
  or when it is the only document naming an item you marked it as excluding. Reaching the same answer
  without it means that document is not needed." (two attempts per left-out document were shown). A
  failure shows "A marked document may not be needed" and the gate does not pass. An approximation
  from a rounded figure in the remaining documents counts when it lands on the gold at the stated
  precision; a bound that merely leaves the gold possible is not enough. Apply the guide's
  rounded-figure test to every listed document: recompute without it, using the remaining documents'
  rounded figures at face value, and pick a precision at which that gives a different answer. Grading
  was strict at three decimals: 10.871 against a gold of 10.869 counted as a different answer. The
  platform also offers a one-line reviewer note (200 characters) for a needed document, and the form
  apparently lets a necessary document carry an excluded item; any edit to the question, answer,
  reasoning or necessary documents clears the note. Exclusion-only documents in a list question are
  the expected case for both. In a list question, also expect the high model to rebuild an item from
  another document's flows or year-to-date columns when its own document is left out.
- The form names the role explicitly (aq-01333 q01, 2026-10-06): each ticked document is an "Answer
  component" or an "Exclusion / condition source". An exclusion source takes a reviewer note and needs a
  quote of what it rules out.
- The role is not for an edition trap's decoy-carrying release when another marked document dates the
  event. The platform reviewer returned aq-01333 q01 rev 4 for exactly that, although its difficulty
  check had passed (2026-10-07): "Doc 5's role in the note is only to rule out its own June 1 range ...
  without Doc 5 that range doesn't exist to rule out. So the note doesn't make Doc 5 necessary."
- Leave such a release unticked and quote it nowhere in the evidence. The rev 5 resubmission still names
  the release in the reasoning's decoy line, without quotes (result pending).
- Use the role only for a document that rules out an item which exists without it. Details are in
  reference/platform-quality-checks.md.

- Local removal probe (aq-docket-trial-01, 2026-10-06): give a fresh blind-solver a prepared packet,
  the verbatim question and the instruction to treat one marked document as absent, answer if it can,
  and otherwise commit to a forced guess with its probability. It caught guessable inputs that the
  removal reasoning had passed: a top-3,000 variability screen (guessed at p 0.8 as "a common
  round-number screen") and a leukemia cluster count equal to the dataset's three labelled subtypes
  (p 0.3). Since 2026-10-08 (user instruction) it is required for every ticked document before any
  hand-over or platform run, not only for round numbers or default class counts: see
  [[docket-removal-probe-required]]. A closed-book reach fails it for every marked document.
  Build the probe packet as a byte copy of a prepared packet minus one document, bound to the read
  guard as its own run, and give it a neutral folder name: a folder named "removal-noD02" told the
  probe which document was missing (aq-docket-trial-06, 2026-10-06). The id gap tells too: probes
  on aq-docket-trial-04 q03 and q04 noted "the manifest skips D05" / "has no D05" and guessed its
  subject, so renumber the remaining ids (and manifest keys) contiguously in the probe copy.
- Entity coincidence (aq-docket-trial-06 q02, 2026-10-06, local probe): when a bridge document only
  picks one entity from another document's per-entity table, check every entity's value under the
  same computation. q02 asked for one state's share of credit unions without federal insurance
  (Idaho, picked by a regulator's fee in Doc 5: 21 / 214 = 9.8%); Indiana's 21 / 214 gave the same
  9.8%, so the probe without Doc 5 forced-guessed the gold (p 0.2). The platform's document check
  would count that as Doc 5 not needed. q02 was dropped.
- Loose event verbs (aq-01322 q01, 2026-10-06, local probes): "When Cencora divested its U.S.
  Consulting Services business" let a probe without the only dating document (Doc 6, "divested in
  April 2026") forced-guess the gold (p 0.5). It read "divested" as the held-for-sale classification
  that the gold edition's own release disclosed and tied to its guidance change. "Completed/closed
  the divestiture" moved the same probe off the gold (best answer the next edition, gold only 0.25).
  When the gold edition's release mentions an earlier step of the same event (agreement, held for
  sale, impairment), anchor on the completion and probe without the dating document.
- Year-to-date rebuilds make restated-quarter carve-outs lose a document (aq-01322 q03, 2026-10-06):
  an originally reported quarter is rebuildable from the full-year release (year minus Q4) and the
  half-year release (minus six months), so the quarter's own release was not individually needed.
  Pick a period whose original and restated sides each come from one irreplaceable document (there:
  calendar January-June 2025, needing the original March quarter and the restated June quarter), list
  only those, and leave the replaceable inputs quoted but unlisted.
- In a run of quarterly earnings releases only the latest quarter's actuals are single-source: every
  earlier quarter reappears as a prior-quarter or year-ago column, or rebuilds from neighbouring
  year-to-date columns. Next-quarter guidance is edition-unique (a revenue range may be restated in the
  following release's highlights), but compare the neighbouring editions' midpoints first: a guided value
  that repeats across adjacent quarters lets a leave-one-out solver reach the gold by assuming the
  guidance was unchanged. Pick a quantity, form or precision at which every such proxy answer differs.

- Two-edition edition traps (aq-01428 q01, 2026-10-06, local probes): when the question asks for the
  value in force at an event printed only in the later release, removing that release leaves the earlier
  release's value as the only candidate. Two forced-guess probes said "not determined" and then chose it
  (the gold, p 0.6). The platform's document check does not force a guess (aq-00964 q01 refused twice), so
  this is a residual risk; to remove it the later release must contribute a number to the answer, which
  brings its own priors (see [[docket-general-knowledge-check]]).

**Why:** in aq-docket-trial-03 the local question-review sent q02 and q03 back for exactly these
points, costing two revision rounds each.

**How to apply:** at sketch time, name for each listed document the fact only it holds. For a
date window, check every planned date against the window's end and against the latest
edition's coverage.

## Evidence and history

- 2026-10-09: aq-02501 q01 rev 1 difficulty Run 1 (Low 0/5 · Medium 2/5, Medium band) failed the gate with "A marked document may not
  be needed": a qualifier naming another document's definition (DoD DARB's "less than honorable" set) that excludes nothing
  from the answer is decorative to the high model, which assumed the membership (uncharacterized separations) the defining
  document alone supplies. The page then offers "a one-line note for the reviewer" (200 characters) that "clears submit without a
  new run"; any later edit to question, answer, reasoning or necessary documents clears the note. Design lesson: a defining
  document is mechanically necessary only when its definition changes the answer (excludes an item the other document supplies,
  or includes one the usual sense would drop and the solver cannot otherwise reach).
  Outcome: with the 190-character note saved, the page allowed submit ("an admin must sign it off (waive the check for
  this content) before the task can be approved") and kept the Medium label ("+$20 Medium+ bonus if accepted"); the user
  submitted. Reviewer outcome (2026-10-10): "Sent back for revision ... Only document 3 is necessary. Ensure at least two docs are
  necessary for the solver to get the "gold answer"." So the note buys a submission, not an acceptance: when the document
  check says a marked document is not needed, fix the dependency before submitting. A defining document whose set equals
  "everything but the obvious exclusion" (here every characterization but honorable) can never be necessary through that
  definition; give the second document its own gold component (rev 2: a second ask for a value only it states).
  Result (2026-10-10, Run 2, Version 432875): "In band — Medium tier", Low 0/5 · Medium 1/5; document check
  "Needed document 3 ✓" and "Needed document 5 ✓" (without Doc 5 the high model gave the wrong board's 15-year
  window); resubmitted the same day. Raw: tasks/aq-02501/verdicts/AQ-02501_difficulty_2026-10-10_2103.txt.

- 2026-10-09, aq-02367 (aq-02220's bytes; local, caller plus two independent authors, no platform run): the June 2022
  government response reprints each 2021 proposal beside its response table (Option 3 with its refurbishment group, the
  trigger points, the 10-year grace period, the one-day familiarisation estimate), so no proposal-versus-final design had an
  indispensable proposal document. In consultation/response bundles, list which proposal facts the response does not
  restate before designing on the consultation; here almost none survived outside the impact assessment's own numbers.

- 2026-10-08, aq-02198 (local, no platform run): a consultation and its response can reprint the same annex word for
  word. Both 2021-22 McCloud papers carry the identical equality assessment (Table 1 protection counts, 419,000, age, sex,
  ethnicity and disability figures), so a question built on any of them has a twin and neither paper is individually
  necessary; this ruled out the bundle's richest bundle-only numbers. At intake, diff each proposal/response pair's annexes
  before treating their figures as single-source.
- 2026-10-04: aq-docket-trial-03 (three DOT semiannual agendas). q02: the refund hearing date was
  in D03, D06 fn 11 and D07 fn 24, so documents became D01 and D04 only; step 2 had misread a
  repeated Section 610 sentence as "citing the previous edition". q03: a window ending at the
  August 2024 agenda left AK77's planned 07/00/24 inside it; ending at the February 2024 agenda
  let D03 answer alone. "Before April 2024" passed, because D04 records April 2024 actions and
  re-plans the open items for later. q01, built on a superseded deadline (D04) and its stated
  extension (D03), passed at once. These are local reviewer findings, not platform feedback.
  They apply to any bundle with repeated editions or duplicated facts.
- 2026-10-04: aq-docket-trial-02 (Colgate earnings releases; segment, cash-flow and balance-sheet
  rows cut in D02-D12). q01's Q3 2024 cash flow comes from the D03 and D04 highlights. But D07
  and D08's cut cash-flow statements, headed "2025 and 2024", probably repeat those figures. The
  local review warned that D03 and D04 may then not be necessary on the platform. The cut segment
  tables, which hold recast year-ago quarters, also ruled out several recast questions. These are
  local reviewer findings, not platform feedback; they apply to any capture with cut tables.
- 2026-10-04: aq-docket-trial-07 q01 (platform verdict "Too easy", pasted by the user). The
  question took the NBER start and end months of the 2020 recession from Doc 1 and ranked rail
  occupational groups from Doc 5's chart over those months. The platform's explanation: "the
  entire answer lives in one document ... The low model found it all in Doc 5 without needing
  any other document." It misplaced the dates (they are only in Doc 1's note 8), but the
  outcome stands, because February-April 2020 is widely known. Local checks had passed Q2 on
  the removal test. Platform feedback, one question; it applies to any bridge built on a widely
  known date or fact.
- 2026-10-04: aq-docket-trial-02 q05 (count of quarters in which Hill's organic volume fell, Q1 2024-Q2 2026; answer 7). The local review found that D02, D04, D08 and D11 fail the removal test, because the D03, D05, D09 and D12 year-to-date tables force those quarters' signs. A second review found that D06 and D07 fail too: D07's six-month, D08's nine-month and D09's full-year tables pin the first two 2025 quarters. That leaves D05, D09 and D12 as the only individually necessary releases. Local reviewer finding, not platform feedback; it applies to any count over quarters in an earnings-release series. Run the year-to-date check on every listed quarter at once, not one review round at a time.
- 2026-10-04: aq-docket-trial-03 q05 (new gate), dropped at local review. It asked for the analysis year in DOT's 10-year plans (D03) of the regulation holding the categorical exclusion that the 2026 final rule (D07) relied on: 23 CFR 771, inside FHWA's "parts 710 to 924" row, 2024. Two blind solves matched and the closed-book solve missed, but the proposal (D06) prints the same exclusion sentence, so D07 was not individually necessary. The closed-book solve also recalled the citation and FHWA, so the hop cost a model nothing ("found it all in Doc N"). A range inference that no passage prints (D4) did not rescue it. Local reviewer finding, not platform feedback. It applies to any bridge taken from a proposal/final pair or from a citation models know.
- 2026-10-05: aq-00998 q01 rev 0 (local review; earlier, later-deleted bundle folder). Chevron's releases moved the cash-flow
  attachment from billions to millions in 2026, and the cut financing rows of the 2Q 2026 release
  sit beside a three-months-ended June 30, 2025 column, so they may state that quarter's net change
  in debt in millions, duplicating or competing with a balance-sheet difference built from two
  earlier releases. Unresolvable without a complete capture; the question was moved to a line no
  flow statement reports. Check later editions' cut rows for restated earlier periods in finer
  units, not only the period's own releases.
- 2026-10-05: aq-00745 (complete capture of seven Abbott releases). The Q2 2026 release alone
  reproduces every Q1 2026 dollar cell (first half minus second quarter) and the restated 2025
  comparatives (Exact Sciences pre-acquisition sales, multi-year payments, recast Structural
  Heart), so the Q1 2026 release is individually necessary only for its growth rates, its
  quarterly EPS range and its dated events. Cross-document questions on 2026 figures had to pair
  the latest release with the FY2025 release (Q4/FY tables), a guidance edition, the deal release
  or a 2025 release. Check the latest half-year or nine-month release first when listing an
  earlier quarter's release as necessary. Caller and mapper finding (pass C maps), local only.
- 2026-10-05: aq-00949 (complete capture of five EOG quarterly supplements plus a 2020 plan
  release and a 2025 deal release). Each supplement reprints every quarter of the current and
  prior year in its statements, and no figure is restated between editions (only a 2026
  balance-sheet "Other" recast and relabels). So the 2Q26 edition alone holds every 2025 and
  2026 quarter, and the per-quarter EPS bridges are rebuildable from it. Individually necessary
  inputs were limited to the two press releases and the latest edition's own quarter. Name the
  necessity anchor (a press-release fact plus the latest-only quarter) before drafting.
  Caller and mapper finding, local only.
- 2026-10-05: aq-00998 complete capture confirmed that review: D12's cash-flow statement prints a
  three-months-ended June 30, 2025 "Net change in debt" of (299) in $ millions, against a
  balance-sheet change of -214 built from D06 and D08. A cut row did hold a competing measure for
  the same quarter. Prefer quantities that no flow statement reports (net debt, balance levels).
- 2026-10-06: aq-00998 q05 rev 3 (twelve-month ROCE to June 30, 2026 by Chevron's full-year method,
  two decimals; documents Doc 10 and Doc 12), platform difficulty check Run 2, screenshot supplied by
  the user: "Low model 2/5 right" (inside the stated 1-3 window) but "A marked document may not be
  needed ... without document 10", so "the gate does not pass". Doc 11's highlights print 4Q 2025
  ROCE as a rounded 5.4%; at face value it gives 10.8707%, the gold 10.87 at two decimals. Local
  reviews had shown that the 5.4% only bounds the answer to 10.856-10.885% and called D10
  indispensable; the platform counts the face-value route. At three decimals the exact answer is
  10.869% and the face-value route 10.871%. Platform evidence, one question.
- 2026-10-05: aq-00949 q04 rev 2 (end-2019 to June 30, 2026 total debt ratio, documents Doc 1 and
  Doc 7), user report "You passed in Easy tier, low model solve 3/5 attempt". Doc 1's only input
  (end-2019 debt 5,175, a pre-cutoff public figure) was recalled exactly by every local closed-book
  run, and local review rated the removal-test risk moderate under the common-knowledge rule above.
  The reported pass suggests the platform did not count that recall against Doc 1, unlike widely
  known dates (trial-07 q01). Provisional: the document-check line itself was not supplied. The
  fixed wording (rev 5, 2026-10-06) failed as "Too easy", Low 5/5, and its pasted panel showed no
  removal-test line, so the question stays open.
- 2026-10-05: aq-00949 q06 (local review): a press-release date anchor fails the removal test in
  practice when (1) the series' own cost footnotes first show the deal in that quarter, (2) models
  recall the public announcement date, or (3) a year-later window ending at the latest edition's
  quarter leaves only one possible start. Separately, volumes rebuilt from daily rates (MBoed x days)
  can split a cent-level per-share answer; EOG's bridges compute with the printed one-decimal MMBoe
  (D05 221, D06 (76)), so cite that evidence or pick a precision both routes share.
- 2026-10-06: aq-00998 q05 rev 4 (the same question at three decimals, 10.869%), platform difficulty
  check Run 3, pasted by the user: "In band — Easy tier", "Low 3/5 · Medium — · High —", "You can
  submit now." Document check: without Doc 10 the high model answered 10.871% twice ("Needed document
  10 ✓"), the predicted face-value route; without Doc 12, 8.080% and "Cannot be determined". The
  precision change fixed the removal flag. Platform evidence, one question.
- 2026-10-06 (aq-01430 sketch c02, local probe): China's share of world demand growth 2000-2025
  (55.9% at one decimal) took China's 2000 demand (1,347 TWh) from the 2024-data review only. A probe
  without that review recalled the official statistic (about 1,347-1,356 TWh) and forced 55.9% at
  p 0.4; any recall within about 1,344-1,360 lands on the gold. A long-run baseline that matches an
  official national statistic is common knowledge for the document check, even inside a 0.1-point
  window. Dropped before write-up.
- 2026-10-08: aq-00949 q07 rev 0 (dividends declared over the four quarters after the quarter that
  declared the October 17, 2025 record-date dividend, $3.06; Doc 3 and Doc 7), run by the user after the
  local drop. Platform Run 5: "Low model ●●○○○ 2/5 right" but "Your answer can still be reached without
  documents 3 and 7", so "the gate does not pass". Locally the closed-book run had already reached
  $3.06, and Lever checks had named both risks: Doc 3's declaration quarter is recalled or inferred from
  Doc 7 (2Q 2025 1.9950, 3Q 2025 a dash; the window is exactly Doc 7's last four quarters), and Doc 7's
  2Q 2026 equals the unchanged $1.02 an assumption supplies from Doc 6. No probe was run. Per-document
  answers were not supplied, so the routes are inferred. Platform evidence, one question; it led to the
  required-probe rule.
- 2026-10-08: aq-00949 q06 (local removal probe under the new rule): without Doc 3, the only document
  dating the Encino agreement, a fresh solver answered the gold $0.94 unforced with high confidence. It
  dated the deal from the supplements' Encino acquisition-related costs (first in 2Q 2025, none in
  1Q 2025 by the full-year total) and the acquisition cash in 3Q 2025. The first acquisition-cost
  quarter in a later edition dates a deal announcement, so an announcement date fails as a bridge
  whenever the series reports deal costs. Dropped before any run. Local evidence, one question.
- 2026-10-08, aq-01960 (14 KLA releases, local design analysis, platform pending). Only Q4 FY26 actuals
  (D14) had no substitute; Q1-Q3 FY26 rebuild from D12/D13/D14 year-to-date columns. Non-GAAP gross
  margin guidance midpoints repeat (62.0, 62.0, 61.75, 61.75; EPS $8.28 for Q4 FY25 and Q1 FY26), so a
  margin-beat question (gold 0.6) also came out 0.6 with the March quarter's guidance assumed for June.
  The product form (non-GAAP gross profit vs revenue midpoint x margin midpoint, q01, 3.3%) moved that
  proxy to 10.2; a fiscal-year GAAP form in dollars (q02, $250 million) left every neighbour proxy at a
  different value, where a one-decimal percent form would have collided twice.
- 2026-10-08, aq-01543 q04 (platform Run 1, version a39f39; raw tasks/aq-01543/verdicts/): a recall test had rebuilt
  Doc 4's exact 23,500 MWe (26,050 - 2,550) when its prompt listed the exclusions (offline, under construction, shut
  down), so the Document check on Doc 4 was stated as a risk. The platform's high model, given the bare question
  without Doc 4, used its own stale fleet list (25 reactors, about 25,374 and 25,321 MW: 7.21% and 7.23%), and both
  documents were judged needed. A recall prompt that spells out the filter overstates the risk; ask the bare question.
- 2026-10-08, aq-02147 q01 (platform Run 1, version 8b4bdc; raw tasks/aq-02147/verdicts/AQ-02147_difficulty_2026-10-08_1706.txt):
  "A marked document may not be needed ... without document 3". The question asked for the 2024 SSP consultation's
  break-even point (its £123, five-day employee) at a rate only the government response prints. The equality analysis's
  case study 1 is the same employee with the same flat rate and waiting days; with the consultation left out, the high
  model took that case study and computed the gold (week 12). The hand-over had grouped the two as "Doc 3 or Doc 4"; the
  capture does not show whether the "or..." box was set, and no "Without document 4" attempt ran. Without the response
  both attempts answered 3 weeks (the median of the 60/70/80% illustrations), so that document was needed. Hook retired;
  the replacement uses inputs printed in one document each.
- 2026-10-10, aq-02686 q01 (local design and one removal probe; platform pending): a proposal/final pair
  (DOE's "foreign entity of concern" interpretation, Doc 2 and Doc 4) where the final reprints nearly every
  rule of the proposal, so a rule application rests on either. The question stayed dependent on the final by
  resting one step on a clarification printed only in the final's responses to comments (a board seat is
  valued at its board voting power, so two of five seats with 20% of the votes is 20%, not 40%). A fresh
  solver given the proposal without the final counted seats and answered $45,602 against the gold $45,708,
  and the full-packet solver said the proposal "cannot replace" the final. How to apply: in an edition pair,
  diff the operative text and the comment responses, and let one scenario fact turn on a point the earlier
  edition answers differently, not merely omits. Two side notes from the same bundle. (1) A second document's
  only input can be boilerplate a model recalls (EPA's "approximately $106" export-notice cost appears in
  many notices); adding that document's 2026-only figure ($45,496) to the total removes the doubt. The
  natural partner document was not used because its only unique inputs were the $7,500 / $3,750 clean
  vehicle credit amounts. (2) The probe's readings list caught "Korean" as possibly North Korean in a
  bundle that names North Korea as a covered nation; name countries unambiguously in scenario questions.
