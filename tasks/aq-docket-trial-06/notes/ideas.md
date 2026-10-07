# aq-docket-trial-06 - lean candidate sketches

Current target: medium (user, 2026-10-06: "at least Medium", one attempt, re-check after reaching
a result); measured platform success pending. Origin of all sketches: claude (Claude Code,
claude-opus-5-5 question-author agents, independent of the caller's drafting).

Design basis (memory, measured): Medium = Low 0/5 then Medium 1-3/5 (aq-00964 q01). Unrelated-
document bundles (trial-01 rebuild): the Medium trap must sit inside one document (a same-label
wrong value ruled out only by close reading); the cross-document step is ordinary arithmetic or a
clean membership condition. Earlier Trial 6 round (2026-10-04): agency-role sets solved locally
and partly recalled closed-book.

Round 1, numeric/inferred author (2026-10-06):

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | w2: credit-union total needs a footnoted remainder (never printed), minus bank total | "How many more credit unions did the United States have at the end of 2002 than it had banks on September 30, 2005?" Gold 2,361 (9,688 + 214 = 9,902; 1,846 + 5,695 = 7,541) | D02 231 (9,688), 233 (212), fn 8 at 239 (two uninsured), 1179 (214, all but two privately insured); D05 191 (1,846; 5,695) | Calculate across documents; bury one item late. Decoys 2,359 (9,688 + 212), 2,147 (federally insured only, overview figure), 2,345/3,059 (rebuilt from 98%/2%), one charter type only | 2002 vs 2005 comparison may look arbitrary; D05 fn 6 body absent; removal probe needed for recalled bank counts | promoted to q01 (checked rev 0): A match (medium; listed 2,359), B match (high), closed-book 2,148, audits ambiguous then clear (replacement), removal probes needed both docs (forced guesses 2,147 and about 2,350), review ready, medium (marginal), Easy the larger risk |
| i02 | w3: 1997 conversions = 223 changes - 158 mergers (never printed), minus credit-union conversions | "How many more state-chartered banks converted to the federal charter in 1997 than credit unions converted from federal to private deposit insurance between 1992 and 2002?" Gold 38 (65 - 27) | D05 641/647-649 (changes = conversions + mergers), 681 (223 in 1997), 689 (158 mergers 1997); D02 509 (27) | Calculate across documents; match then exclude (changes minus mergers). Decoys 196, 131, 312, 40, 39 | arbitrary windows (1 year vs 11) and opposite directions; "1997" search finds 223 and 158 within 8 lines | author predicts Easy; hold |
| i03 | regulated entities per dedicated staff member | Movers per FMCSA household-goods staff member (2001) vs Massachusetts facilities per assisted-living ombudsman (April 2004), nearest whole number. Gold 7 (580 / 86) | D01 79 (2,900), 123 (5 of about 760); D04 521 (three, later two; 172) | Calculate across documents. Decoy 10 (three ombudsmen) | deciding fact in the same sentence as the decoy | Easy/too easy; fallback only |

Round 1, qualitative-lever author (2026-10-06; returned 3 of 5: the rest failed its own checks; it
reports about 25 rejected hooks, chiefly a bridge document that stops being necessary because the
ask identifies its target alone, agency roles recalled from memory, and "include, but are not
limited to" law lists that cannot prove exclusions):

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i06 | state identified in D05 by its regulator's funding detail; D02 counts with the footnoted remainder in numerator and denominator | "At the end of 2002, what percentage of all U.S. credit unions without federal deposit insurance were located in the state whose bank regulator adds a $100 charge per branch office to its asset-based assessment? Answer to one decimal place." Gold 9.8% (21 / 214) | D05 819-821 (Idaho, "$100 per branch office"); D02 467 (Idaho 20), fn 8 at 239 (one uninsured in Idaho), 1179 (214) | Scatter the pieces; who belongs where. Decoys 9.4% (20/212), 9.3% (20/214), 9.9% (21/212, 21/213) | "Idaho" search in D02 reaches fn 8 early; shares q01's deciding fact | promoted to q02, DROPPED rev 0: A/B match 9.8% (both list 9.4%), closed-book 47.2% miss, audit ambiguous (D02 uses "lacking federal deposit insurance" for privately insured credit unions, so 9.4% is defensible), no-D05 probe guessed the gold (Indiana 21/214 = Idaho 21/214) |
| i07 | year bridge (Washington's 1997 law, D04 389) into D05 1997 conversions (223 - 158) | "In the year Washington State's legislature adopted a consultative approach to helping assisted-living providers comply with licensing standards, how many U.S. banks moved from state to national charters by conversion rather than by merger?" Gold 65 | D04 389; D05 681, 689, 641/649/651 | Calculate across documents. Decoys 223, 158, 339, 143 | wording tells the solver to subtract; arbitrary bridge; 1997 is D05's only fully described year (removal risk); Figures 5-7 graphics absent | author predicts Easy/too easy; hold |
| i08 | ordering four 2003 events across D04 and D05 | Order: second 29-state settlement (Jan 2003), Workgroup report (Apr 2003), Massachusetts fund elimination effective (June 30, 2003), OCC MOU proposal (July 2003) | D05 309, 295; D04 175, 525, fn 43 at 541 | Ordered answers; exact footnote date vs "fiscal year 2003" | 49 words; artificial mix; Doc 4 overview prints April 2003 | author predicts Easy/too easy; drop |

Round 2 (2026-10-06, user: "can you make QA like Trial 2's q01 or Trial 6's q02"). Target shape:
the entity or quantity is named only by a description another document resolves; the needed figure
is assembled, never printed; a percentage at a stated precision where each near-miss route rounds
differently; avoid q02's two flaws (a phrase that is the document's own term for a narrower set;
another entity giving the gold). Independent author i09-i12; caller i14-i15. Raw: runs/sketch-round2/.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i09 | California (D05 $2.20 cap) site-visit recount, sites minus repeat visits | share of California's privately insured credit unions that received a GAO site visit: 17 / 22 = 77.3% | D05 805-809; D02 423 (22, 21 sites), notes 429-431, 407 | match then exclude. Decoys 95.5, 81.0, 68.2 | about GAO's own sampling (rule 10); D02 calls the 57 sites "57 privately insured credit unions" (59, 1197), a second reading | author Easy/Medium; not taken |
| i10 | q01 as a two-decimal percentage | "By what percentage did the number of U.S. credit unions at the end of 2002 exceed the number of U.S. banks on September 30, 2005, measured against the bank count? Answer to two decimal places." Gold 31.31% | as q01 | calculate across documents; state the rounding. Decoys 31.28 (9,900), 28.47, 23.84, 31.33 (recalled 7,540), 31.30 (early rounding) | contrived comparison as q01; alternative to q01, never both | promoted to q03, CHECKED rev 0: A/B match 31.31% (both read 1179), closed-book 28.49% miss, audits clear of shortcuts but both answered 31.28% (missed 1179), review ready, medium (marginal); q01 preferred for the single attempt |
| i11 | q02 with California and a privately insured base | 22 / 212 = 10.4% | D05 807-809; D02 467, 469 | scatter the pieces. Decoys 10.3, 12.3 | two lookups and a division | author too easy; not taken |
| i12 | Idaho Web-site base switch (= caller i15) | 5 / 20 = 25.0% | D05 817-821; D02 459-469, 455, 1213-1215 | printed same-row 71% on a different base | GAO's own review; Easy risk | promoted (with i15) to q04: A/B match 25.0% (high), closed-book unknown, audit clear, probes need both docs; review revise (Too easy 55-65%, Easy 30-40%, Medium about 5%): retired |
| i14 | q02 with California (no Indiana coincidence) | "At the end of 2002, what percentage of all U.S. credit unions that were not federally insured were located in the state whose bank regulator caps its assessment at $2.20 per $1,000 of assets?" Gold 10.3% (22/214) | D05 805-809; D02 467, 1179, fn 8 | bury one item late. Decoy 10.4% (22/212) | "not federally insured" still collides with D02's narrower usage (187, 409, 511, 1021, 1179); the no-D05 probe read the wording as pointing at the uninsured pair | blind 10.3% (high, straight to 1179), closed-book 40.6% miss, no-D05 probe 9.8% miss; dropped (term collision, weak trap) |
| i15 | Idaho Web-site share, printed per-site percent as decoy | 5 / 20 = 25.0% | as i12 | as i12 | i15 wording ("as GAO found in 2003") let a solver read 71.4% | blind 25.0% (medium; 71.4% second reading), closed-book 33.3% miss, no-D05 probe 15.1% miss; reworded and promoted to q04 |

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
