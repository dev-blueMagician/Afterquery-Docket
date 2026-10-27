# aq-docket-trial-06 - cross-document hooks

Caller's inventory, 2026-10-08 rebuild (target medium, hard where a design supports it). Built from a
full read of text/D01-D06 (all lines). Six unrelated GAO products (2001-2007); no document cites
another. Cross-document links are shared agencies (FTC, NCUA, FDIC, FRB, OCC, OTS, HUD, DOJ,
Treasury, HHS), shared states, and shared depository-institution concepts (credit unions in D02,
banks in D05). Prior trial-06 work (2026-10-04 and 2026-10-06 rounds, folder removed before this
session; recoverable from git HEAD) is listed at the end so new hooks do not repeat measured failures.

Medium mechanism wanted (calibration): an untied, answer-shaped printed decoy that only a fact
needing close reading rules out (no keyword in the question points at that fact), joined to a clean
second-document input. One trap, not two (two chained traps overshot to Too hard on aq-00745 q08).

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D02 231 (9,688 federally insured, Dec 2002; "98 percent"), 233 (212 privately insured, "about 2 percent of all credit unions"), 239 fn 8 (two uninsured, Idaho and NH), 1179 (214 lacked federal insurance, all but two privately insured); D05 191 (1,846 federal + 5,695 state banks, Sept 30, 2005) | all U.S. credit unions end-2002 (9,902) vs banks Sept 30, 2005 (7,541) | Figure that must be computed; Part vs total | 9,688 or 9,900 (missing the two uninsured) | dates differ (2002 vs 2005), contrived; this is the old q01/q03 hook | candidate (re-check wording only if no new design beats it) |
| h2 | D02 407 (57 locations: 49 main, 8 branch), 411/423-431 (Table 1: California 22 privately insured, 21 sites; note b: one CU main + 3 branches, another main + 1 branch), 59/1197 ("57 privately insured credit unions"); D05 805-809 (California regulator's assessment: minimum $5,000, maximum $2.20 per $1,000 of assets) | share of California's privately insured credit unions that got at least one unannounced GAO visit: 17/22 = 77.3% | Linking across documents; Part vs total (sites vs credit unions) | 21/22 = 95.5% (sites taken as credit unions), 17/21 = 81.0% | D05 used only to identify California; removal probe for D05 is the risk; GAO fieldwork as subject (rule 10 borderline) | sketch i01 |
| h3 | D02 Table 1 notes a-c: distinct credit unions visited 51 (57 - 2 - 3 - 1); D02 59 and 1197 print "57 privately insured credit unions" | distinct credit unions visited overall | Part vs total | 57 | single-document unless a second document supplies a needed input | not standalone |
| h4 | D05 641-649 (changes = conversions + mergers), 681 (223 changes to the federal charter in 1997, 2.4% of banks), 689 (158 mergers into the federal charter in 1997, 1.73%) | 1997 state-to-federal conversions = 65 | Look-alike measure (changes vs conversions) | 223, 158 | year bridge needed from another document (D04 389 Washington 1997 law; D01 137 June 1997 due date); old i02/i07 predicted Easy | hold |
| h5 | D06 119/181 ("the other 20 regional U.S. Trustees and ... their 1,342 case trustees"; 33 case trustees in the Texas region) | case trustees under the U.S. Trustee Program = 1,375 | Part vs total | 1,342 | single-document; "their" reading may be disputed | not standalone |
| h6 | D02 231-233, fn 8, 1179 | federally insured share of all credit unions, one decimal: 97.8% (9,688/9,902) vs 97.9% (9,688/9,900) vs prose 98% | State the rounding; Part vs total | 97.9, 98.0 | single-document | not standalone |
| h7 | D02 Table 3 467 (per-state Web sites analyzed / noncompliant, percent of sites) | per-credit-union share vs printed per-site percent (base switch) | Unit or basis | printed site percent | old q04 (Idaho 25.0% vs 71%) reviewed Too easy | low priority |
| h8 | D03 211 (First Alliance, March 2002, FTC + six states + AARP); D05 309 (national bank settlement with 29 states, March 2002) | two March 2002 settlements, different parties | Look-alike event | 29 vs 6 | each fact one lookup; second document only a decoy | rejected (one-source answer) |
| h9 | D05 393 ("OCC oversees about 1,900 national banks", Dec 2004 context) vs 191 (1,846 federally chartered banks, Sept 30, 2005) | national bank count by date | Older figure inside a newer report | 1,900 vs 1,846 | needs a date anchor from another document; both approximate/dated plainly | hold |
| h10 | D05 711-737 (OCC semiannual assessment formula, Table 1) | apply the formula to an asset size from another document | Calculate across documents | n/a | no other document gives a national bank's assets | rejected (no input) |
| h11 | (numeric author) D02 407, 423-431 + D05 803-809 | California's share of all distinct credit unions visited: 17/51 = 33.3%; decoys 36.8 (21/57), 29.8, 34.7 (17/49 drops Illinois' branch-only), 37.3, 41.2 | Who belongs where; Part vs total | per-state values AL 5.9, CA 33.3, IL 19.6, IN 9.8, OH 31.4 | same single-state bridge as h2 (design-intent probe risk) | sketch i04 (author's i01) |
| h12 | (numeric author) = h2 with "counting each credit union once" | 17/22 = 77.3% | as h2 | as h2 | cue narrows to AL/CA without D05 | covered by i01 family |
| h13 | (numeric author) D02 239, 467, 1179, 1207 | 213 credit unions without federal insurance inside the eight private-insurance states (212 + Idaho's uninsured one; New Hampshire's is outside) | Part vs total | 212, 214 | single-document; working-term reading of 212 | rejected (no partner) |
| h14 | D06 119, 181 | 1,375 case trustees (1,342 + 33), 21 regions | Part vs total | 1,342 | single-document | rejected (no partner) |
| h15 | (numeric author) D05 397-399, 669, 725-735 | OCC formula on JPMorgan Chase's ~$649B = $22,363,720 semiannual, about 98% of the ~$23 million jump | n/a | n/a | approximate inputs | not a question |
| h16 | = h4 | 1997 conversions 65 | as h4 | as h4 | 1997 is the only year with both figures printed, so a bridge document is replaceable by inference | rejected (Q2) |
| h17 | (numeric author) D05 487 | alternative California bridge (June 2000 OCC/California restitution floor) | n/a | n/a | recall (well-known 2000 case) | rejected |
| h18 | caller, after the i01 probes: D05 183/533/797 (six interviewed states: CA, GA, NY, NC, ID, IA) + D02 Table 3 467 (CA 22, ID 20) + Table 1 423 and note b | share of privately insured credit unions in those states that got at least one 2003 visit: (17 + 0)/(22 + 20) = 40.5% | Linking across documents (set membership); Part vs total | 50.0 (sites), 77.3 (Idaho dropped), 24.1 (all eight) | D05 defines a set; a probe must reconstruct {CA, ID} to reach the gold | sketch i03 |


Prior trial-06 designs and outcomes (git HEAD, notes/ideas.md and session.md of the removed folder):
- 2026-10-04: agency-role sets (preemption claimants minus deposit-insurance objectors; mentions vs does on
  OCC's two rules; agencies GAO ruled out in its reply to comments; Fed bridge into the App II table) all
  solved locally; agency roles partly recalled closed-book (Expedited Funds Availability Act enforcer).
- 2026-10-06: q01 h1 as a difference (2,361), checked, review ready, medium (marginal), Easy ~45%, Medium ~40%;
  q03 h1 as 31.31% (two decimals), checked, same odds; q02 Idaho share of credit unions without federal
  insurance dropped (D02's working term "lacking federal deposit insurance" = privately insured; Indiana 21/214
  = Idaho 21/214 coincidence); q04 Idaho Web-site base switch reviewed Too easy; i09 California site-visit
  recount (17/22) authored but not taken (GAO-sampling subject; "57 privately insured credit unions" reading);
  i02/i07 1997 conversions predicted Easy; i03 per-staff ratios and i08 2003 event ordering Easy/too easy.

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
