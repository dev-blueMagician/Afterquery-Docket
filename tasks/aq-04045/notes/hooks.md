# aq-04045 - cross-document hooks

New bundle (no earlier capture of these documents; checked 2026-10-13 against 10.6, 10.7 and 10.8 by file
name, FR number and source hash). No measured misses exist for these bytes, so designs start from the family
record in `.claude/memory/docket-local-solver-calibration.md`: a step the question's words point at is cleared
by the easier solver; a carve-out under a printed share, a remainder nobody prints and a scope sentence in
another document are the shapes that have held it.

Single-source facts first (the inputs a second document cannot replace):

- FY 2024 fee units: D05 para 28 only (16 small satellite, 140 GSO, 6 less complex, 11 other).
- FY 2024 per-unit fees: D06 para 40 only ($964,200 NGSO-Other, $441,925 NGSO-Less Complex).
- GSO per-unit fee for FY 2024: printed nowhere. Any GSO or all-category figure has to come through the
  60% GSO / 40% NGSO allocation (D05 paras 9 and 34; D06 para 8).
- Small-satellite fees come out of the NGSO share: D02 III.A and D06 para 40 (two sources, so D02 is
  replaceable for this rule).
- Provider counts: D03 (2020), D02 (2021), D07 (2023), one year each.
- Petitioner list: D01 only. Named fee commenters: D05 only.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D05 para 28 units (11, 6, 16); D06 para 40 fees ($964,200, $441,925) and the "after subtracting ... Small Satellites" clause; $12,215 (D06 para 7); 60/40 for FY 2024 (D05 paras 9, 34) | Share of all FY 2024 space station fees that fell on NGSO-Other: 10,606,200 / (13,453,190 / 40%) = 31.5% | Calculate across documents; exact figures vs the rule's round shares; state the rounding | Rule shares 40% x 80% = 32.0%; leaving small-satellite fees out of the NGSO share also gives 32.0%; small satellites outside the split 31.8%; old 80/20 allocation 15.8% | Both key figures sit past character 20,000 (form number check will show false alarms). Derived gold; "One defensible answer" must be looked at before a run | i01, written up as q01 |
| h1b | same inputs | GSO stations' FY 2024 fees as a group: 13,453,190 x 60/40 = $20,179,785, $20.2 million | same, dollar form | Without small-satellite fees $19.9 million; 80/20 $53.8 million | Same; no printed figure to mistake for it, so the only gate is the small-satellite placement | i02 sketch (sibling of i01, one of them at most) |
| h1c | same inputs | Share on the two NGSO categories charged per system: 13,257,750 / 33,632,975 = 39.4% | Carve-out under a printed share | Printed 40%; 39.8% with small satellites outside the split | The printed 40% fits a loose reading: the form may block it as too vague | i03 sketch (sibling of i01) |
| h2 | D03 FRFA: 71 providers, about 48 with 1,500 or fewer employees, as of December 31, 2020; D07 FRFA: 57 and about 40, as of December 31, 2023; D02: 65 and 42 for 2021 (the middle edition) | Change in the small-provider share between the earliest and latest counts: 70.18% - 67.61% = +2.6 points | Same series, right edition; exact figures under identical prose ("a little more than half" in all three) | Publication order (D02 to D07) gives +5.6; D03 to D02 gives -3.0 | Plain lookups and one subtraction; all six figures past character 20,000 | i04 sketch |
| h3 | D01 para 1 petitioners; D05 paras 39, 50, 53 named proposals | Petitioners against the 2020 debris rules that the 2025 fee notice names with a fee proposal: Kuiper, SpaceX, Telesat | Who belongs where; match, then exclude | Maxar (proposes with Telesat, only commented in D01), Kepler (in both, opposed petitions) | Two short printed lists; this family has tested too easy elsewhere (aq-02102 q02) | i05 sketch |
| h3b | D01 para 1 (Combined Petition = six companies; its subjects include persistent liquids) and para 22 ("The Combined Petition asserted"); D05 named companies | The one company named in the 2025 fee notice that had sought reconsideration of the persistent-liquids rule: Telesat | Who belongs where; mentions it vs does it | SpaceX and Kuiper (petitioned on other rules), Maxar and Kepler (commented only) | Single-name answer; one unpointed step (resolving the collective label) | i06 sketch |
| h4 | D02 old small-satellite formula; D06 FY 2024 fees | Small-satellite fee the old formula would have given for FY 2024 | Calculate across documents | - | Rejected: D02 says the formula uses the "calculated" rates before the small-satellite deduction; the assessed rates give $35,155 and the pre-deduction rates $35,670, two defensible answers | rejected |
| h5 | D05 11 and 6 units; D06 60/40 and 24 / 3 constellations | What the 2025 categories would charge on FY 2024's pool | Calculate across documents | 60% given to large constellations | Rejected for now: a what-if that mixes operational units (FY 2024) with authorized-basis estimates; every step is named by the question | held, not offered |
| h6 | D01 April 23, 2020 adoption; D03 Sept 9, 2024 effective date | 1,600 days from adoption to effect | Calculate across documents | Publication date (1,476), compliance date (1,620) | Date gaps between named events have tested too easy on every earlier bundle | not offered |
| h7 | D03 five-year disposal; D06 paras 23, 27-31 fees on TT&C-only stations | Fiscal years of fees while a satellite awaits re-entry | Rule applied to a case | - | Rejected: needs assumptions the documents do not state (licence in force until re-entry) and has an edge case at October 1 | rejected |
| h8 | D04 9A515.a.4 kinds of spacecraft; D02 small satellite category | Which kind the FCC kept out of its small-satellite fee category | Who belongs where | - | Rejected: one of three, guessable without the documents | rejected |
| h9 | D03 five-year disposal and end-of-mission definition; D06 paras 23, 29, 31 | Last fiscal year a system is assessed while its satellite awaits re-entry | Rule applied to a case | - | Rejected again in round 2: the deadline and the definition are codified public text and the scenario's dates sit in the question, so a solver without D03 can reach the answer; 57 words | rejected |
| h10 | D03 event dates; D02/D03/D07 provider counts | Provider share at the year-end picked by a dated event | Same series, right edition | The event document's own count | Rejected in round 2: any date in the event's year picks the same year-end, so the dating document can be replaced by a guess; adds nothing to i04 | rejected |
| h11 | D05 50/50 proposal; D06 60/40 rule | Large constellations' share of NGSO fees under proposal and rule (40% both) | Proposal against final | 50% | Rejected: D05 para 52 floats a second variant (all NGSO split 50/50), so the proposal side has two defensible answers unless the base is named, and naming it gives the step away | rejected |
| h12 | D05 more than 1,000 against D06 1000 or more | Class of a constellation of exactly 1,000 | Proposal against final | - | Rejected: the boundary is what anyone would guess without the documents | rejected |

Measured on these bytes, 2026-10-13 (quick tests, user chat "1, 3 too easy, 2 survived. others not tested",
no panels, so every route is unread):

- h1 share of all fees on NGSO-Other (31.5%): too easy. The easier solver reached the gold, so it built the
  total through the 40% share and put the small-satellite fees inside it.
- h1c share on per-system payors under the printed 40% (39.4%): too easy. A printed look-alike one step
  from the gold did not hold it.
- h1b GSO stations' dollars as a group ($20.2 million): survived the quick test, then difficulty Run 1 "Too easy",
  Low 5/5 (2 not scored), Version ce30ee. Routes read from the attempts: four did the whole chain (units in D05,
  fees in D06, small-satellite fees inside the NGSO share, 60/40); one multiplied 140 units by a per-station fee
  it remembered (about $144,000). Closed-book missed ($14.5 million). Hook h1 closed: every step of the chain is
  of a kind the easier solver cleared, so no repair adds a holding step. Never use the per-station GSO fee as a gold.

- h2 change in the small-provider share between the earliest and latest year-end counts (2.6 points): survived the
  quick test, then difficulty Run 2 "Too easy", Low — · Medium 5/8, Version 84ce0b (the check started at the Medium
  level). Routes read: three attempts (4, 5, 8) answered 5.6 after finding the 2021 and 2023 counts and reporting
  that the other documents had none; three found all three counts; attempt 2 missed the 2023 count, got -3.0, and
  looked again because the question said "rise"; two attempts have no recorded text. Design consequence: the end
  editions in the off-topic rules are a real gate for the medium solver (three of six recorded attempts), and a
  direction word in the question is a check that undoes it. Repair i07 asks for the signed change. Do not add
  arithmetic: every attempt that had the right editions computed correctly.

- h2 rev 1 (the same question asking for the signed change): difficulty Run 3 "Too easy", Low — · Medium 4/8,
  Version 790376. Misses as before (the 2021 count taken as the earliest); the direction word's removal moved one
  attempt, not the band. By the page's rule the misses were spread over all three solvers with only one of them
  wrong twice, in both runs. Hook h2 closed after its one repair; no second unpointed step exists for it in a
  different passage (Doc 3's other boilerplate edition sits in the same analysis).
- h3c (sketch i08): the deployment-device section of D01 names five arguers and omits Telesat; D01 para 1 says the
  six-member Combined Petition asked about deployment devices; D05 names Telesat. The section's explicit list is
  the lure ("none").

- h3c (i08): quick-test too easy (user chat 2026-10-14). The easier solver resolved the six-company petition from
  D01's first paragraph past the deployment section's five-name list and matched Telesat in D05. Family h3 closed:
  i05 and i06 need a subset of those steps.

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
