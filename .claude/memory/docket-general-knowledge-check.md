---
name: docket-general-knowledge-check
description: "The platform returns a question a model can answer without the documents (\"answerable from general knowledge\"), a separate verdict from \"too easy\"; anchor on facts only the bundle holds and run a local closed-book solve before hand-over."
metadata:
  node_type: memory
  type: feedback
  updated: 2026-10-05
  originSessionId: 9e8d8c8c-aa4d-457b-a7c1-04fe73680640
  modified: 2026-10-06T17:10:24.569Z
---

## Current rule

- The platform checks whether a question can be answered from general knowledge, without the
  documents, and returns it if so. This verdict is separate from "too easy". Widely reported
  public facts count as general knowledge even when every one of them is quoted from the bundle.
  Examples: a notable rule's Federal Register publication date and comment period, famous event
  dates, and headline company or survey figures.
- Anchor the answer on at least one fact a model cannot know:
  - a document published after likely model cutoffs (in late 2026, documents from late 2025
    and 2026; the local closed-book model recalled headline company guidance issued as late as
    January 2026 and headline quarterly revenue reported as late as April 22, 2026 (aq-01321),
    so treat facts first printed before about May 2026 as possibly known);
  - a planned or internal value, such as an agenda's target month, a footnote's docket citation,
    a comment tally or a document-specific classification;
  - a bridge only the bundle states.
  A public fact may still sit on the path, but it cannot be the whole path.
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

- 2026-10-06: aq-01320 (restaurant earnings releases), sketch-stage closed-book probes. A cost ratio with
  an industry prior was reached: Chipotle's first-half 2026 labor share excluding a legal accrual (gold
  25.3%) drew "25.3% (an estimate)" from a recalled ~24.6% 2025 level plus drift; dropped. A Darden
  tax-rate difference (gold -0.4 pp) drew -0.5 from a remembered ~12% guidance habit. Outlook-vs-actual
  per-share differences built from a reconciliation-table range missed every time (+$0.02, $0.08,
  $0.20 against -$0.28), although each probe recalled the adjusted guidance and dated the edition.
  Ratios and rates that sit near a well-known level are estimable; prefer per-share or dollar answers
  whose size depends on a bundle-only figure. Local evidence.
