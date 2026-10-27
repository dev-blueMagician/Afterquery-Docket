# aq-01541 - lean candidate sketches

Current target: medium (Easy slot full on this set; Hard optional); measured platform success pending.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 (claude, caller) | h1: settlement groups defined by Jaffe's April 22, 2025 report; Doc 6 prints the superseded March split first | "If every class member in Trans Union's preliminarily approved settlement filed a valid claim, what percentage of the money set aside for valid-claim payments would go to the members who also get the automatic payment? Answer to one decimal place." -> 63.3% | D03 l.63-73, fn 2-3; D07 l.41, 47, 49, 61 | Same series, right edition; Calculate across documents. Wrong routes: 65.0 (March), 64.0 (920 from no-record), 65.5, 63.5, 72.3, 36.5, 75.0 | 57,233 vs 57,208 harmless at one decimal; approximate reserves cancel | mechanical screen passed (sketch_sha256 eeae1825...); promoted to q01; rev 1 checked 2026-10-08 (review ready, easy-leaning) |
| i05 (claude, caller; first logged as i02, renumbered to avoid the author's ids) | h1 variant: value of one pro rata point if every member claims | "... how many dollars would one pro rata point be worth?" -> $29.1 | as i01 plus D03 l.66 reserve | right edition; printed "$350" expectation as a decoy | shares i01's answer path | superseded by i06 |
| i06 (claude, caller) | h1 + printed estimate on a different claim-rate basis | "Suppose every member of the class in Trans Union's preliminarily approved settlement filed a valid claim. Taking the court's figure for the money set aside for valid-claim payments, how many dollars of it would go to each claimant who gets no automatic payment? Give one decimal place." -> $29.1 | D03 l.63-75, fn 2-3; D07 l.41-61 | Same series, right edition; look-alike printed "$350" (typical claim rates). Wrong routes 350, 28.1, 28.9, 28.4, 29.0, 50.4, 87.3 | reserve pinned to the court's figure; gold window 2,875,660-2,885,558 | promoted to q02; rev 0 checked 2026-10-08 (review revise, fixed outside the fingerprint; easy-leaning) |
| i02 (claude, independent author round 1) | h2: no-record share of class members, list in place at the decertification motion (D07) minus the June 2022 test month at certification (D05) | author: "... on the plaintiff's expert's final class list, minus ..." -> -10.0 pp; caller anchor: "the class list in place when Trans Union moved to decertify" | D05 l.312, l.316, fn 30 l.322; D07 l.41, 47, 49, 67 | Unit or basis (printed 27.7% is a share of 973 searched files) +8.8; superseded March count -7.7 / -8.3; 1,100 base +12.0 | fragile route: 57,208 base with two-decimal shares gives -9.95 exactly (float/half-down -9.9) | promoted to q03; rev 0 checked 2026-10-08 (review ready, easy-leaning) |
| i03 (claude, independent author round 1) | h1 variant: automatic-payment member's total if every member claims, nearest dollar | -> $187 | as q01 plus reserve | printed $1,000 + $100 expectation | version trap weak at dollar precision (920 route and reserve routes also give $187) | not promoted (q02 keeps the version trap biting at one decimal) |
| i04 (claude, independent author round 1) | h3: Wodzinski report date (D04) to class-certification motion filing (D05) | -> 51 days | D04 l.36; D05 l.66/70 | Calculate across documents | plain two-lookup date gap (measured Too easy pattern) | not promoted |

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
