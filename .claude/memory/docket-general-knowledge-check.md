---
name: docket-general-knowledge-check
description: "The platform returns a question a model can answer without the documents (\"answerable from general knowledge\"), a separate verdict from \"too easy\"; anchor on facts only the bundle holds and run a local closed-book solve before hand-over."
metadata:
  node_type: memory
  type: feedback
  updated: 2026-10-05
  originSessionId: 9e8d8c8c-aa4d-457b-a7c1-04fe73680640
  modified: 2026-10-07T02:16:14.248Z
---

## Current rule

- The platform checks whether a question can be answered from general knowledge, without the
  documents, and returns it if so. This verdict is separate from "too easy". Widely reported
  public facts count as general knowledge even when every one of them is quoted from the bundle.
  Examples: a notable rule's Federal Register publication date and comment period, famous event
  dates, and headline company or survey figures.
- Published regulation text is general knowledge too. A condition that restates the Code of Federal
  Regulations (aq-02501 q01 rev 0: which discharges VA accepts automatically, 38 CFR 3.12) failed the form's
  "Needs the documents" although its quick test had survived; quick-test survival says nothing about this
  check. Rest the deciding condition on what only the bundle's document says, such as a rule preamble's own
  statement of which cases it does not apply to, impacts or helps (rev 1 and rev 2 then read "Needed the
  documents ✓").
- Anchor the answer on at least one fact a model cannot know:
  - a document published after likely model cutoffs (in late 2026, documents from late 2025
    and 2026; the local closed-book model recalled headline company guidance issued as late as
    January 2026 and headline quarterly revenue reported as late as April 22, 2026 (aq-01321),
    so treat facts first printed before about May 2026 as possibly known);
  - a planned or internal value, such as an agenda's target month, a footnote's docket citation,
    a comment tally or a document-specific classification;
  - a bridge only the bundle states.
  A public fact may still sit on the path, but it cannot be the whole path. A statutory
  cross-reference that is the Act's standard provision for the topic is guessable too (aq-02360
  q01: "Section 95(2)" of the Pension Schemes Act 1993 for a transfer-payment rule failed the form's
  blocking "Needs the documents" check, although its trap needed two documents); add a part only the
  documents hold, such as the citing regulation's paragraph number.
- A scenario question can fail this check by arithmetic coincidence, with nothing recalled. When the
  question prints the counts of a stated case, a solver with no documents applies a plausible naive rule
  and adds them. aq-02780 q01 rev 0 (2026-10-11, "Answerable without the documents"): the gold, 9
  approvals, equalled the sum of the three branch-opening counts in the question (2 + 3 + 4); the
  closed-book attempt guessed "only new branches need approval" and landed on it, although its rule was
  wrong on five of seven cells. Before prepare, list the sums a guesser would form from the question's
  own numbers (each category alone, every category, natural pairs, one party's items) next to the
  document-based wrong routes, and change the counts until none equals the gold or any part of it. Keep
  answer parts off the numbers the question prints. Asking for a count per regulator or party, at most two
  asks, also stops one coincidence carrying the whole answer. Tool gap, not yet built: the floor could
  flag a numeric gold equal to a sum of numbers printed in the question.
- A gold with few possible values fails the same way, with nothing recalled and nothing printed to add up. The
  platform's closed-book check is one attempt by the low model, and that attempt always commits to a value.
  aq-03169 q01 rev 0 (2026-10-12, "Answerable without the documents", run spent, no solver with documents
  measured): the gold was "7 years", asked "to the nearest whole year"; the attempt wrote "This suggests the
  result is not an integer, maybe 7.2 rounds to 7" and committed 7. Before prepare, count the answers a
  guesser could give at the asked form. A lone whole number under about twenty (years, a count, a rank, a
  step number) or a round value at a coarse precision (a multiple of ten percent) is too few: add a second
  ask whose answer is a number only the documents hold (rev 1: "260 audits and 7 years"), or use a form with
  more digits. A coarse precision chosen so that several stated inputs agree does not excuse this; pair it
  with the document-only part. Check that the added part does not point at the trap (aq-02360 q01 rev 2).
  Tool gap, not yet built: the floor could warn on a one-component numeric gold that is a whole number under
  twenty.
- A difference of two partly recalled public figures is reachable even when neither figure is recalled
  correctly, because a shared error cancels. aq-03570 q03 (2026-10-13): the letters print $3.45 trillion and
  $1.8 trillion (gold 1.65); the closed-book attempt of Run 3 recalled 3.44 and 1.74 (1.70, "Needed the
  documents") and the one of Run 4 recalled 3.41 and 1.76 and committed 1.65 ("Answerable without the
  documents", run spent, no solver with documents measured). A closed-book answer within a few percent of the
  gold counts as reached: change the asked form before the next run instead of writing the risk down (the
  author noted it at two hand-overs and changed nothing). Prefer a form in which a shared error does not
  cancel, such as a ratio or percentage at one decimal place (the two recalled pairs give 93.8% and 97.7%
  against a gold of 91.7%), and write the delete-and-guess line with the recalled values actually seen. The
  form's "Needs the documents" row had passed on the previous wording with the same gold: that row and the
  run's closed-book check are separate single samples, and neither clears the other.
- Before hand-over, run a closed-book solve. Give a fresh agent the question alone, tell it to
  answer from memory without tools, and count a correct or near answer as a fail. The floor
  cannot test this, and neither can the blind solver, which reads the documents.
- When: every question about real public entities (agencies, companies, papers, courts).
- The same question-only probe also tests self-contained scope. If the solver cannot tell which
  region, company or program the question means, a scope word is missing. aq-docket-trial-04 i01
  ("which countries saw the requested aid decline", bundle = Latin America reports only) drew
  "I couldn't work out which document or region this question refers to" (2026-10-06); the
  sibling q01 had the same gap. Name the region or entity whenever the bundle covers one slice of
  a broader program.

**Why:** aq-docket-trial-03 q01 passed the floor, three blind solves and two reviews. It asked
how many days after the FRA train crew rule's extended comment period closed the final rule was
published (475 days). The platform returned it: "The question can be answered from general
knowledge, without the documents. Ask something only the documents can answer." That reply came
with "This is your last attempt."

**How to apply:** at sketch time, mark each fact as public or bundle-only, and prefer sketches
whose deciding fact is bundle-only. Run the closed-book solve on every write-up alongside the
blind solve. See also [[docket-local-solver-calibration]] (the "too easy" verdicts, including a
common-knowledge bridge) and [[docket-series-editions-necessity]] (common knowledge counts as a
duplicate).

## Evidence and history

- 2026-10-13: aq-03570 q03 rev 2 (US SIF 2022 fund assets by issue, climate change stand-alone minus the
  runner-up, gold $1.65 trillion), difficulty Run 4, Version 730996, raw
  tasks/aq-03570/verdicts/AQ-03570_difficulty_2026-10-13_1553.txt: "Answerable without the documents"; only the
  closed-book check ran (11 of 15 runs left). The attempt, read in full as far as the page records it, listed
  candidate figures in billions for climate change/carbon, tobacco and military/weapons, wrote "if second is
  tobacco 1,756, diff = 1,651B = 1.65T" and committed about 3.41 and 1.76. Its runner-up was the wrong issue
  and neither figure matched the letters. Rev 3 asks the same gap as a percentage of the runner-up's figure
  (91.7%); it was quick-test too easy the same day, so the percentage form has no closed-book sample. Scope: one
  hook, two closed-book samples.

- 2026-10-13: aq-03993 q01 rev 0 (average grant from a public pilot fund, gold "158 applications and about
  £50,000"; the count had been paired in as the document-only part). The closed-book attempt recalled the
  fund's published figures (£2 million, 178 applications, 20 projects), produced 158 from memory and answered
  £100,000 for the average: "Needed the documents ✓". Two things to carry: a count taken from a government or
  committee report about a public scheme is not document-only, so it protects nothing; and when the gold
  departs from what the headline public figures imply, the closed-book attempt lands on that implied value
  (here the question's own wrong route), which is what kept the gold out of reach. Check the paired part
  against "would a model know this from the news" before relying on it. One run, one bundle.

- 2026-10-12: aq-03169 q01 rev 0 (years of tender wins, at the rate one consultation response assumes, to bring the
  Big Four within another response's per-firm cap; gold "7 years", chosen at whole-year precision because the
  present base is stated four ways), difficulty Run 1, Version 4e4850, raw
  tasks/aq-03169/verdicts/AQ-03169_difficulty_2026-10-12_1034.txt: "Answerable without the documents"; only the
  closed-book check ran and the run was spent (14 of 15 left). The attempt, read in full, recalled none of the inputs,
  called the question "too ambiguous without the source", guessed 7 from the rounding instruction and then wrote
  figures to fit (8-10 wins a year, 50-65 audits, "approximately 6.5 years, which rounds to 7 years"). The author's
  checks had covered recall of the inputs and the overview, not the size of the answer space, although this note
  already listed small-integer counts (aq-01430). Rev 1 adds a first ask, gold "260 audits and 7 years". Scope: one
  run, one question; the platform result on rev 1 is pending.
- 2026-10-11: aq-02780 q01 rev 0 (a three-institution branch plan counted against the OCC's 2026 rule and the
  FDIC's 2025 proposal, gold "9 changes"), difficulty Run 1, Version 5d70b5, raw
  tasks/aq-02780/verdicts/AQ-02780_difficulty_2026-10-11_1137.txt: "Answerable without the documents"; only the
  closed-book check ran (Low, Medium and High not run) and the run was spent (9 of 10 left). The one closed-book
  attempt committed "2 + 3 + 4 = 9", the question's three opening counts; the documents' route is 3 + 1 + 5. The
  author's wrong-route table had ten document-based slips and no sum of the question's own numbers. Rev 1 changed
  two counts (gold 4 for the OCC and 6 for the FDIC, total 10 of 21; naive sums 14, 17, 21, 7, 3, 18) and asks per
  agency; a local closed-book run of rev 1 answered "OCC 3; FDIC 5" (a miss; minor context contamination
  reported). Scope: one run, one question; the platform result on rev 1 is pending.

- 2026-10-09: aq-02501 q01 rev 0 (DoD DARB's "less than honorable" set filtered by VA's automatic acceptance: general
  discharges and entry-level separations) survived the free quick test but failed the form's blocking "Needs the documents"
  (user screenshot, tasks/aq-02501/notes/platform-feedback/q01-rev0-checks-2026-10-09.png): both VA facts are public
  38 CFR 3.12 text, so a quick-test survival says nothing about closed-book answerability. Rev 1 moved the VA side to the
  2024 rule preamble's own statements of effect (dropped-from-the-rolls separations "favorably impacted"); a local
  closed-book probe then answered OTH and special-court-martial BCD only (miss). Regulation text that is public, even
  quoted from the bundle, counts as general knowledge; a rule's preamble clarification of its own scope did not.
- 2026-10-09: aq-02360 q01 rev 0 (user screenshot of the form's Checks panel,
  tasks/aq-02360/notes/platform-feedback/q01-rev0-checks-2026-10-09.png): "Needs the documents Failed"
  ("Answerable without the documents: This question is answerable without the documents. Ask something
  that can only be worked out from them.") for a gold of "Section 95(2)", while "Needs two or more
  documents" and "One defensible answer" passed and the sketch had survived a quick test. The form's
  blocking closed-book check is now on the Checks list itself, before any difficulty run. Rev 1 added
  "Regulation 142(4)" to the gold; rev 2 (order wording added) was then reported too easy (user, same day): the
  paragraph number points the solver to the document sentence that defeats the trap. Check that a non-guessable
  addition does not tie the trap before filing it.

- 2026-10-06: aq-01321 (ADI, Microchip, TI and onsemi releases, Jan-Aug 2026), closed-book sketch
  screens. Combined revenue of the four companies' quarters ended January 1-March 31, 2026 (gold
  $9.3B) was REACHED at low confidence: ADI fiscal Q1 "about $3.16B" (reported Feb 18), TI Q1 "about
  $4.83B" (reported April 22), and onsemi excluded because "its quarters end on the Friday nearest the
  calendar quarter end" (Q1 ended April 3). The same frame for April-June 2026 quarters (reported May
  to August) missed, as did inventory and twelve-month expense-ratio answers built on June 2026
  figures (golds deliberately not stated here: those questions are still under check). Removal
  probes did not recall TI's Q1 2026 or Q3-Q4 2025 R&D/SG&A line items, but did recall TI quarterly
  revenue for 2024-2025. Headline actuals are recallable into late April 2026; line items less so.
- 2026-10-06: aq-01322 (six Cencora releases, Q2 FY2025-Q3 FY2026), closed-book sketch screens.
  A guidance range from the February 2026 update ("7% to 9%" consolidated revenue growth) was reached
  at low confidence by a model that believed it was the November 2025 initial range; the same row in
  other editions (5% to 7%, 4% to 6%) would have been guessable the same way. A word-valued row of the
  same February edition (Other's adjusted operating income "Flat") and table-derived quarter or
  carve-out figures all missed (guesses 3% to 7%, 8% to 10%, 9% to 11%, about 10%, about 15%). A
  calendar-2025 free-cash-flow build drew "about $3.40 billion" against $3.38 billion (near). Prefer
  word-valued or derived answers over a mid-cycle percentage range a model can pattern-match.
- 2026-10-04: aq-docket-trial-03 q01 rev 1, platform reviewer, returned (last attempt).
  Criterion: general knowledge. The rule's NPRM (07/28/22), extended comment close (12/21/22)
  and final rule (04/09/24, 89 FR 25052) are all public record. This is one verdict, but it bears
  on any bundle of public documents (Federal Register, earnings releases, published papers). It
  also bears on this bundle's q02 and q03, which concern the 2024 airline refund rule and
  PHMSA's 2023 gas distribution proposal. The floor could not have caught it; a closed-book solve
  step in /docket-check would have.
- 2026-10-04: local closed-book calibration (Opus 5.5, no tools, question text only).
  - Returned train crew question: the solver recalled every date (07/28/22 NPRM, 09/26/22
    deadline, 12/14/22 hearing, 04/09/24 final rule) and answered 561 days, the pre-extension
    figure. This confirms the facts are general knowledge.
  - q01 rev 2 (a 2026 footnote's docket bridge plus a July 2023 agenda target): "4 months",
    marked a guess, against a key of 5.
  - q02 (the refund rule plus the same agenda target): "10 months", marked a guess, against a key
    of 5. The solver knew the April 26, 2024 publication but not the agenda target.
  - q03 (PHMSA gas distribution): the solver's pick was wrong, but it named the key as a close
    alternative, so q03 is at medium risk.
  - Planned or internal values (agenda target months) and post-cutoff documents defeated the
    closed-book solver. Well-known proposals and final rules did not.
- 2026-10-04: aq-docket-trial-06 (six 2001-2007 GAO reports), local closed-book solves. GAO-level
  detail about agency roles is general knowledge:
  - q01, the enforcer of the Expedited Funds Availability Act at privately insured credit unions:
    key recalled (medium confidence). It was dropped.
  - Sketch i10, the regulators with no formal predatory-lending action minus those GAO tied to a
    conflict of interest: key reconstructed (low confidence), citing OCC's 2003 Clear Lake action.
    It was dropped.
  - q03 and sketch i9 held: answers "FDIC, Federal Reserve, NCUA" and "HUD", both wrong. Their
    deciding facts were a rejection GAO makes only in its reply to agency comments, a
    document-specific list of preemption claimants, and a document statement that contradicts
    the statute as models remember it.
  - Correct at low confidence still counts as a fail. Run the check on every write-up and on
    sketches before spending platform quick tests.
- 2026-10-05: aq-00964 q03 (actual FY2025 Adjusted EBITDA minus the pre-April 2025 outlook
  midpoint reconstructed from the April raise; gold $240M), local closed-book solve: "About $240
  million" at low confidence. Both remembered inputs were wrong (~$7.19B, ~$6.95B) but their
  difference hit the gold. A beat-versus-guidance gap for a large public company sits near a
  guessable size (a few percent of the base), so estimation can land on it. Dropped; switching
  the metric keeps the exposure. Prefer answers whose size has no natural prior (a named item,
  a sign flip, a bundle-only date). Local evidence, one bundle.
- 2026-10-05: aq-00949 sketch screens (closed-book, question only). An investor-contact question
  (the person listed as an investor contact in both a March 2020 and a May 2025 release) was
  answered from memory, "Neel Panchal", medium confidence, with the media-only decoy correctly
  set aside: boilerplate names in large companies' press releases are recallable, so dropped.
  A debt-growth sketch recalled the end-2019 debt exactly ($5,175M) but missed the June 2026
  figure; a funding-test sketch recalled the wrong measure and missed. Local evidence only.
- 2026-10-05: aq-00949 q01 (two asks: the first quarter in which a company's crude output
  included each of two newly added countries; the later quarter is the bundle's latest), two
  local closed-book runs. Rev 0 hit the later half by a recency bound ("the last result out
  before today") and missed the earlier one; rev 1 hit the earlier half from the publicly
  announced deal's timeline and missed the later one. Neither produced the gold pair, and the
  reviewer counted both as misses with moderate exposure. A "first time" answer equal to the
  bundle's latest period is guessable by recency, and a start shortly after a public deal is
  guessable from its timeline; here protection rested only on the pair. Local evidence, one
  bundle; no platform result yet. (Gold deliberately not stated here.)
- 2026-10-06: aq-00949 q07. The question asked for dividends declared per share in the four
  quarters after the quarter that declared the dividend with an October 17, 2025 record date. A
  closed-book run reached the gold, at low confidence. It recalled the deal-day declaration
  (May 30, 2025) of the dividend payable in October, inferred that no dividend was declared in
  3Q 2025, and assumed the same $1.02 for the post-cutoff quarters.
  - A constant per-share rate is guessable after the cutoff, so a window of constant values
    protects nothing.
  - A mega-cap's pre-cutoff timing quirks (an early declaration) are recallable.
  - The same assumption would defeat the platform's document check for the post-cutoff edition.
  - Anchor post-cutoff steps on values that move (amounts, volumes, prices), not on a stable rate.
  Local evidence; dropped before platform test.
- 2026-10-05: aq-00998 q01 rev 1 (earlier, later-deleted bundle folder; the rebuilt bundle's q01 is different content) (change in Chevron's total assets over the quarter of a dated
  April 2025 discovery; gold −$5,577M), local closed-book solve: "About −$5,570 million", low
  confidence, from recalled quarter-end total assets (about $256.4B and $250.8B). Quarter-end
  balance-sheet levels of a mega-cap for pre-cutoff quarters are recallable, so a change between
  two of them is not a bundle-only fact even when each value sits in a different release.
  Dropped (the same bridge's growth-rate question, q02, stayed). Prefer post-cutoff periods or
  values no headline database carries. Local evidence, one bundle.
- 2026-10-05: aq-00745 (Abbott releases, January 2025 to August 2026), local closed-book screens
  on five sketches before write-up. The solver recalled the full-year 2025 guidance history (the
  July 2025 range at high confidence) and the January 22, 2026 full-year 2026 range (medium
  confidence), so three sketches whose answer was the guidance range in force at a dated event
  were reached and dropped. It said it did not know the April 16, 2026 update or anything later.
  Write-ups whose answers needed the July 2026 range (q01, a midpoint change; guess "-$0.20"
  against the gold), the Q2 2026 actual (q02) or first-half 2026 sub-business sales (q03,
  "unknown") all missed. Late-2025 and January 2026 headline figures are not bundle-only for this
  local model. Local evidence, one bundle; no platform result yet.
- 2026-10-05: aq-00745 round 3 (complete capture; table-derived sketches), local closed-book
  screens. Answers computed only from the tables still drew near estimates when their size follows
  from known economics or habits: the adjusted gross margin change across the Exact Sciences closing
  (gold +0.9 pp) drew "+0.8" from Exact's ~70% gross margin and its share of sales; the adjusted
  operating margin change (gold -3.27 pp) drew a forced "-2.50" from Q4 seasonality plus dilution;
  the EPS beat over the guided midpoint in the quarter the close was expected (gold +$0.03) drew
  "+$0.02" from "Abbott's usual pattern". All three were dropped or held. Sub-business dollar
  changes (q03, -$318M) and a post-cutoff guidance midpoint change (q01) drew "unknown" or a wrong
  guess. Prefer table answers with no economic or habitual prior. Local evidence, one bundle.
- 2026-10-05: aq-00998 (rebuilt from the complete capture), local closed-book sketch screens.
  Two more guessable shapes. (1) Extending a public streak count: D11's "16th consecutive quarter over
  $5 billion" plus D12's dividends and buybacks gave 17; the solver reached "17" (medium confidence)
  from the public "13 straight quarters" (2Q 2025) by assuming the streak continued. (2) Ordering
  events where public dates and logic fix most positions: the four-event 2025 chronology was
  reached (low confidence) from the public Hess closing date, the inference that the
  Malaysia-Thailand interest came with Hess and was sold after closing, and a coin flip on the rest.
  Answers built on 2026 balances, a 2Q 2025 growth-rate gap, a 2023-to-2026 refinery difference and
  a later-defined free-cash-flow measure all missed. Avoid answers a model can extrapolate from a
  stated public count or a known event order.
- 2026-10-06: aq-00745 q06/q07 (low end of the FY2026 EPS range, closing day -> June 30 / May;
  gold -$0.17 = January 5.55 -> April 5.38), fresh local closed-book solves: both answered -$0.17 at
  low confidence ("a faint recollection that guidance ... was later cut to about $5.38–$5.58"). The
  local model does recall the April 16, 2026 update at least faintly (q01's rev 1 closed-book also
  put the April midpoint at "roughly $5.47–5.48"), contrary to the earlier note. Both dropped. For
  this model, treat facts printed through about April-May 2026 as possibly known; the July 16, 2026
  range and later were still unknown. The platform's low model missed q01 closed-book (-$0.05).
- 2026-10-06: aq-00998 q06 (which quarters from 1Q 2024 to 2Q 2026 had Chevron's total debt down
  and net debt up; a two-item list, gold deliberately not stated here), two fresh local closed-book
  runs on the same text. Each committed a different answer at low confidence; both contained the one
  qualifying quarter that recalled 2024-2025 debt and cash balances reach (the second run named a
  further quarter only as possible), and neither could place quarters reported from January 2026 on.
  As with the earlier q01 total-assets case, a mega-cap's pre-cutoff quarter-end debt and cash are
  recallable; the misses rested on the items in 2026 releases. The reviewer rated the exposure
  moderate. Local evidence; no platform result yet.
- 2026-10-06: aq-00745 q09. The same January -> July guidance pair was asked two ways. As a
  low-end change (gold -$0.10), one closed-book run estimated "-$0.10" from the recalled January
  range plus "roughly $0.15–$0.20 of Exact Sciences dilution" (reached); another run on that form
  (q08 rev 1) guessed -$0.17. As the percentage change of the midpoint (gold -2.6%), the closed-book
  solver answered "unknown"; q01's dollar midpoint form had missed three times (-$0.20, -$0.175,
  -$0.20). When a known starting value and a remembered adjustment (here the $0.20 dilution)
  bracket the gold, re-express the answer (midpoint, percentage) so the estimate band misses it.
- 2026-10-05: aq-docket-trial-03 q03 (which FHWA Section 610 group was in its analysis year when
  OST's July 31, 2026 UDP final rule took effect; gold, a CFR part range, deliberately not stated
  here). In four of four local closed-book runs (sketch screen, rev 0, rev 1, rev 2) the model
  recalled, with no documents, that OST rules cite FHWA's 23 CFR 771.117(c)(20) exclusion, that
  DOT's plan years run fall to fall from 2018, and that the window was "Year 8"; one run recalled
  FHWA's actual part ranges but on the wrong row. A "which group" ask was creditable as "Year 8"
  until rev 2 asked for the CFR part range. Lesson: plan or appendix tables that agencies reprint in
  every edition are partly in memory; ask for the printed content (ranges, values), not a label a
  known cycle start yields. Review rated the "Needs the documents" risk moderate; no platform result.
- 2026-10-05: aq-01188 (nine unrelated 2003-2008 GAO reports), four caller sketch screens, question
  text only. Every miss on the answer still exposed the bridge: the model recalled GAO-06-8's
  date (October 17, 2005) and that it was the 2005 bankruptcy law's effective date; was "fairly
  sure" NAIC adopted its LTC model act in 1986; inferred Hurricane Rita from "OCC's Houston"
  office and recalled Rita's average NFIP payment as about $49-50K (gold: more than $47,000); and
  answered NAIC's pre-2000 LTC loss ratio (60%) outright, with the 2000 standards (58%/85%). The
  fine-grained counts (Trustee-approved providers at the effective date; PERF yearly force
  incidents) were not recalled. So in older public-report bundles a "period identified by a fact"
  bridge built on a famous institutional date fails the platform's removal test for the bridging
  document even when the target count is safe; use bridges only the bundle states (here a
  regulator's program described in one testimony). Local evidence; no platform result yet.

- 2026-10-06: aq-01428 (Eni 2026 releases), closed-book probes on first-half vs full-year guidance asks. The
  share of FY CFFO guidance earned in H1 (gold 53%) drew "about 55%", citing a habitual 53-55% H1 share;
  the second-half amount still needed (gold €6.45 bln, two decimals) drew €6.30 bln and "about €6.5 billion"
  from guessed guidance minus a roughly even first half. Splits of a full-year figure into halves have a
  half-year prior; only a fine precision protects them. A stated guidance figure asked at a dated event
  (GGP about €1.3 bln) drew "about €1 billion" (the superseded initial level) twice: clean misses.
- 2026-10-06: aq-01320 (restaurant earnings releases), sketch-stage closed-book probes. A cost ratio with
  an industry prior was reached: Chipotle's first-half 2026 labor share excluding a legal accrual (gold
  25.3%) drew "25.3% (an estimate)" from a recalled ~24.6% 2025 level plus drift; dropped. A Darden
  tax-rate difference (gold -0.4 pp) drew -0.5 from a remembered ~12% guidance habit. Outlook-vs-actual
  per-share differences built from a reconciliation-table range missed every time (+$0.02, $0.08,
  $0.20 against -$0.28), although each probe recalled the adjusted guidance and dated the edition.
  Ratios and rates that sit near a well-known level are estimable; prefer per-share or dollar answers
  whose size depends on a bundle-only figure. Local evidence.
- 2026-10-06: aq-01431 (SEC comment letters, 2022-2024), sketch-stage closed-book probes. Reached: the
  climate rule's Federal Register proposal-to-final gap (717 days; both FR dates, Apr 11, 2022 and Mar
  28, 2024, recalled at medium confidence) and a commenter's first letter after a reopening (68 days:
  the March 15, 2023 cybersecurity reopening plus its May 22, 2023 reopened deadline, assumed to be
  the letter date). The securities-loan proposal's FR date (Dec 8, 2021) was recalled "fairly sure"
  although the target date (a March 3, 2022 staff meeting) missed, so the dating letter would fail the
  platform's removal test. Missed: US SIF 2022 issue-level AUM figures (only the $8.4T total and
  "climate change/carbon is the top issue" recalled). SEC rulemaking dates, reopenings and reopened
  deadlines are general knowledge; a commenter's filing on a public deadline is guessable from it.
- 2026-10-06: aq-01430 (Ember electricity reports to June 2026), closed-book screens. Reached: a
  small-integer count difference (countries above a tenth solar, 2025 vs 2024 = 8, a "best guess" from a
  7-10 a year trend) and a near-zero change at whole-TWh precision (China fossil July-December 2025, +3,
  "roughly flat", from recalled monthly NBS thermal data). Recall covered Ember's October 2025 mid-year
  details (China first-half fossil -58.7, solar +306 TWh, China 55%) but not the April 2026 review's
  full-year figures; asking one decimal (+2.8) turned the reach into misses (+8, +55). Avoid small
  integers and near-zero answers at coarse precision.
- 2026-10-06: aq-01432 (eleven FTC and CMA consumer-protection guidance documents, 2013-2025), closed-book
  screens. Statute-level facts were recalled: which UK banned practices are civil-only (advertorials and
  direct appeals to children, carried over from the CPUTRs 2008; fake reviews at low confidence). Over the
  CMA's canonical list of six hidden-advertising provisions, a question-only model reached both the count
  and the exact set (two runs, low confidence), rebuilding the list from memory. Universes taken from a
  guidance document's own list all missed: the short guide's seven pressure-selling behaviours ("All of
  them", "4", "5"), CMA208's commissioning examples ("None", generic) and the after-sales theme's paragraph
  numbers ("8, 24, 28", old numbering shifted). The same recall let a removal probe without the document
  that states offence status forced-guess the gold (p 0.55). In public-law bundles, anchor the universe on
  a list only one guidance document prints; expect the law document's platform necessity to depend on
  whether the high model recalls the rule. (Golds deliberately not stated here: questions still under check.)
- 2026-10-08: aq-01431 restart (SEC comment letters), closed-book screens. Reached: the climate rule's lag
  behind the Fall 2022 agenda target (11 months; recalled the April 2023 target and the Mar 6, 2024
  adoption) and the courts of two co-signers' climate-rule petitions (Sierra Club D.C. Circuit, NRDC Second
  Circuit, recalled; the co-signers inferred from the question's own framing). Three closed-book runs on
  the new q01 recalled all four December 2022 equity-market-structure proposals' Federal Register dates
  exactly (Dec 29, Jan 3, Jan 20, Jan 27; one run also S7-29-22 = Rule 605 and its release number) but
  not a commenter letter's date or which files it covered, so they missed (83.7, 90.7). SEC proposals'
  Federal Register dates and file numbers are general knowledge for strong models; a document whose
  only input is one of them is a removal-check risk even when the closed-book solve misses.
- 2026-10-10: aq-02673 (NOAA Atlantic HMS quota proposal and final rule), three closed-book diagnostics (each
  reported minor contamination from an auto-attached git status; none answered correctly). Recalled exactly: the
  ICCAT North Atlantic swordfish TAC for 2025-2027 (14,769 t, hedged beside the older 13,200 t), the U.S.
  swordfish baseline (3,907 t ww, 2,937.6 mt dw) and its 15 percent carryover (440.6 mt dw); the 2025 U.S.
  bluefin baseline (1,316.14 mt), the 25 mt longline allowance and that it came out of the western TAC (2,726 t
  less 40 t), and the 2026 bluefin TAC (3,081.6 t). Not recalled: the lowest TAC the swordfish management
  procedure allows (4,764 t), any 2025 U.S. catch or underharvest figure, and the 2026 rule that the U.S. gets
  49 percent of the whole TAC. In quota-rule bundles, headline TACs and baseline quotas are general knowledge
  even when recent; a ticked document whose only input is one of them is a document-check risk. Anchor on the
  final rule's catch data and on procedure parameters instead.
- 2026-10-10 (aq-02673 q05, platform Document check, Run 3): the local closed-book diagnostic had recalled the
  2025 U.S. bluefin baseline (1,316.14 mt) exactly, so the final rule looked replaceable. The platform's high
  model, with that document left out, did not recall it: it rebuilt the old baseline from the proposal's
  subquotas (1,341.11 with the set-aside, answer 168.87) or took the wrong rows (231.38), and both were graded
  different from 168.84, so the document was "needed". A local recall of a public figure overstated the platform
  risk here, and a two-decimal gold kept a rebuilt figure from matching. State such a risk; do not drop a design
  on it alone.
