# aq-00745 - lean candidate sketches

Current target: easy; measured platform success pending.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

Round 1 (2026-10-05), origin claude (Claude Code, Opus 5.5 caller). Sketch files in notes/sketches/.
Mechanical screen (docket_agent.py screen): all five eligible, 0 failures, gap warning only
(128 table-only capture gaps; none in guidance, highlight, dateline or dividend text).
Overview exposure (capture l.35-148): the overview lists the bridge dates (Doc 8 "March 23, 2026",
"February 20, 2026"; Doc 4 "September 19, 2025") and the full-year ranges (Doc 3, 4, 7, 8, 10), and
the quarterly actuals; it never ties an event to an edition, and no quarterly range is listed.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h1 edition bridge (aq-00964 q01 shape) | When Abbott completed its acquisition of Exact Sciences, what full-year 2026 adjusted diluted EPS range was its then-current guidance projecting? -> $5.55 to $5.80 | D08 l.27 closing March 23, 2026; D08 l.21 dated April 16, 2026; D07 l.19/283 Jan 22, 2026 range | Same series, right edition; Scatter. Decoys: D08 5.38-5.58 (same doc), D10 5.45-5.60, expected-Q2-close route -> 5.38-5.58 | D10 repeats the closing date; D08 needed to date the April range | screen pass; closed-book REACHED "$5.55 to $5.80" (medium; recalled the January 2026 range) -> dropped (general knowledge) |
| i02 | h2 edition bridge, D08-only bridge fact | When Abbott's board declared the quarterly dividend payable in May 2026, what full-year 2026 adjusted diluted EPS range was the company's guidance projecting at that time? -> $5.55 to $5.80 | D08 l.211 declared Feb. 20, payable May 15, 2026; D08 l.21/203; D07 l.19/283 | Same series, right edition. Decoys: D08 5.38-5.58 (same doc), D10; May 2025 dividend ruled out by year | Arbitrary link; same gold as i01 (at most one written up) | screen pass; closed-book REACHED "$5.55 to $5.80" (medium) -> dropped |
| i03 | h3 edition bridge, 2025 series | When Abbott's board declared the quarterly dividend payable in November 2025, what full-year 2025 adjusted diluted EPS range was the company's guidance projecting at that time? -> $5.10 to $5.20 | D04 l.293 declared Sept. 19, payable Nov. 17, 2025; D04 l.21/287 Oct 15 range; D03 l.21/299 Jul 17 range | Same series, right edition. Decoys: D04 5.12-5.18 (same doc), D01/D02 5.05-5.25, FY actual 5.15; midpoint inert (ask the range) | 2025 guidance public (closed-book risk); arbitrary link | screen pass; closed-book REACHED "$5.10 to $5.20" (high; recalled 2025 guidance history) -> dropped |
| i04 | h4 forecast/actual pairs, six quarters | From Q1 2025 through Q2 2026, in which quarters did Abbott's adjusted diluted EPS equal the top of the range it had projected in advance for that quarter? Chronological. -> Q1 2025 and Q2 2026 | ranges D01 l.319, D02 l.201, D03 l.299, D07 l.283, D08 l.205; actuals D02, D03, D04, D07, D08, D10 l.17/23 | Scatter; Ordered answers. Which-items decoys Q2 2025 (1.26 vs top 1.27), Q3 2025/Q1 2026 (midpoint), Q4 2025 (no range; implied 1.47-1.53 still not top) | Labelled lookups (low-model risk) | screen pass; closed-book missed ("Q1 2025 and Q1 2026", low; Q2 2026 after its cutoff) -> promoted q02 (wording pinned: quarters ended ..., "if any") |
| i05 | h5 on the h1 bridge | Midpoint change from the range in force at the Exact closing to July 2026, signed -> -$0.15 | D08 l.27/21; D07 l.283; D10 l.289 | Same series, right edition; Calculate. Wrong route +0.045 (D10 "raises ... previous range"; April range taken as in force) | Sibling of i01; bridge-free first-to-July reading also -0.15 | screen pass; closed-book missed ("about -$0.175", low; July 2026 range after its cutoff) -> promoted q01 (adds "in dollars to the nearest cent") |

| i06 | definition applied to instances (2026 Rapid and Molecular Diagnostics = Rapid + Molecular + Point of Care) | Using the 2026 business structure, change in reported Rapid and Molecular Diagnostics sales from 2H 2025 to 1H 2026, $M signed -> -$318 million | D10 l.183 footnote, l.171 1H26 1,567; D07 l.153 4Q25 141/158/697; D04 l.157 3Q25 131/158/600 (or D03 1H25 with D07 FY) | Who belongs where; Calculate. Wrong routes: omit Point of Care -2, Rapid only +270, Q2 26 vs Q4 25 -241, 1H vs 1H -125 | D03/D04 interchangeable (unlisted); "business structure adopted in 2026" mildly signals the regrouping | round-2 author (origin claude); caller verified sums; promoted q03 |
| i07 | mentions vs actions on dated announcements | Between January and June 2026, which Abbott products did the company announce had received a regulatory approval or CE Mark? Date order -> TactiFlex Duo ablation catheter and Libre Duo sensor | D07 l.19/39 (January 2026), l.37 Volt (December 2025); D10 l.21/35 Libre Duo (May), l.37 Amulet 360 submission; D08 l.33-37 none | Mentions it vs does it. Decoys Amulet 360 submission, Volt December 2025, ACS guidelines | Per-item keyword filter risk (memory signal 5); year inferred from datelines | round-2 author; promoted q04 (window reworded to avoid q02 phrase) |
| i08 | implied second-half growth from July midpoint | H2 2026 vs H2 2025 adjusted EPS growth if FY lands at the July midpoint, one decimal -> 9.5% | D10 l.289, l.411; D07 l.27/409 | Calculate; State the rounding. Wrong routes 7.9 (April range), 14.8 (January), 7.3 (full year) | Printed figures plus standard steps (signal 3); closed-book near ~10% | held (too-easy, shares July range with q01) |
| i09 | segment comparable growth change Q1 -> Q2 2026, ranked | Rank four segments by pp change, largest increase first -> Nutrition, Diagnostics, Medical Devices, Established Pharmaceuticals | D08 l.93/131/163/191; D10 l.111/157/209/253 | Ordered answers. Reported-growth route reorders | Prose lookups; table rows in capture gaps | held |

Round 2 (2026-10-05): question-author sketches i06-i09 anchored on April 2026+ facts; its full return is
in notes/sketches/round2-author-return.md. It found no post-April edition bridge (D10 prints the April range as
"previous range").

Closed-book lesson (2026-10-05, local Opus 5.5): headline guidance ranges issued through January 2026
(and the 2025 history) are general knowledge; answers must depend on April 2026 or later facts.

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.

Round 3 (2026-10-05, complete capture), origin claude (Claude Code, Opus 5.5 caller). Hooks t1-t4 in
hooks.md. Each sketch got a fresh closed-book screen on its exact wording before any write-up.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i10 | t1 computed adjusted gross margin across the Exact closing | By how many percentage points did Abbott's adjusted gross margin change from the last full calendar quarter before it completed its acquisition of Exact Sciences to the first full calendar quarter after? Sign, one decimal -> +0.9 | D07 l.395, 521; D10 l.389, 501; closing D08 l.27 / D10 l.49 | Calculate; Temporal alignment. Decoys Q1 2026 -0.8, GAAP -0.9, 2Q25 +1.1 | computed only; sign follows deal economics | closed-book "+0.8" (low; from Exact's ~70% margin) -> near hit, dropped |
| i11 | t2 computed adjusted operating margin across the closing | same frame, adjusted operating margin, two decimals -> -3.27 | D07 l.395, 521-523; D10 l.389, 501-503 | Calculate; Temporal alignment. Decoys Q1 2026 -5.48, GAAP -6.20, 3Q25 prose -0.42 | one decimal splits -3.3/-3.2 | closed-book forced guess "-2.50" (low; Q4 seasonality plus dilution) -> held (moderate exposure, same family as i12) |
| i12 | t3 FY2025 adjusted operating margin vs most recent outlook | By how many percentage points did Abbott's full-year 2025 adjusted operating margin differ from the figure in its most recent outlook for that margin? Sign, one decimal -> -0.3 | D03 l.349 (approximately 23.5%); D04 l.339 (no margin); D07 l.553-565, 377 | Same series, right edition; Calculate. Decoys midpoint -0.5, adjusted EBT +0.8 (sign), GAAP -5.3 | D01/D02 low end equals D03's figure; quotes from pipe-rendered rows | closed-book "+0.2" (low; wrong sign) -> promoted q05 |
| i13 | t4 EPS beat in the quarter the close was expected | In the calendar quarter in which Abbott said, when it announced the deal, that it expected to complete its acquisition of Exact Sciences, by how much did adjusted diluted EPS exceed the midpoint of its projected range? -> +$0.03 | D05 l.49; D08 l.225; D10 l.413 | Same series, right edition. Decoy actual closing quarter $0.00 | beat size habitual | closed-book "+$0.02" (low; "usual pattern") -> near hit, dropped |

Round 4 (2026-10-06), target MEDIUM (user: "this bundle have no easy slot. we need to target at
Medium"). Measured basis: q01 rev 1 platform difficulty check "In band — Easy tier", Low 1/5
(4 wrong low attempts took Doc 8's own post-closing range); user reports q03 and q05 did not
survive the quick test. Medium needs Low 0/5 then Medium 1-3/5 (aq-00964 q01: Low 0/5, Medium 1/5
on one trap). Design: keep q01's proven trap and chain a second independent same-document trap so
an attempt must resolve both; each trap path gives a distinct wrong answer; endpoints exact cents.

| ID | Mechanism | Question and gold | Inputs | Traps (answers) | Risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| i14 | two chained edition traps; second anchor a plain date | low end of FY2026 range, closing day -> June 30, 2026 -> -$0.17 | D07 l.335 (5.55); D08 l.21/27/223 (Apr 16, closing, 5.38); D10 l.21/29 (Jul 16, previous range) | D08 range at closing 0.00; D10 range at June 30 -0.10; both +0.07 | platform may judge D08 replaceable (D10's undated previous range plus a cadence assumption); 0.00 path may prompt a re-check | promoted q06; A/B matched, audit clear, but closed-book REACHED -$0.17 (recalls the April range faintly) -> dropped |
| i15 | same, second anchor an event reported only in D10 (ACS reaffirmed Cologuard, May) = aq-00964 structure | -> -$0.17 | as i14 plus D10 l.39 | same three | both traps strong: risk Medium 0/5 (overshoot to High); less natural anchor | promoted q07; A/B matched, audit clear, closed-book REACHED -$0.17 -> dropped |
| i16 | two chained edition traps ending on the post-cutoff July range; second anchor = payment date of the dividend declared in June 2026 (Aug 17), whose sentence also prints the June 12 declaration and July 15 record dates (both before the July 16 raise) | low end, closing day -> dividend payment day -> -$0.10 | D07 l.335; D08 l.21/27/223; D10 l.21/29/329/337 | D08 range at closing +0.07; declaration/record date -0.17; both 0.00 | arbitrary second anchor (dividend); D08 platform necessity (recommend marking Doc 7 and Doc 10 as for q01) | promoted q08; reworded on the form and measured Too hard (0/5 all levels; Coach: ambiguous anchors); rev 1 (explicit anchors) fair but reviewed easy (pinned end anchor has no decoy) -> dropped |
| i17 | one same-document edition trap with no stated link between the anchor event and the guidance change (aq-00964 structure): FreeDM2 results "In March" (D08 only) beside D08's own April range; endpoint the post-cutoff July range | low end, range in force when FreeDM2 results announced -> July range -> -$0.10 | D07 l.335; D08 l.21/37/223; D10 l.21/29/329 | D08 range in March +0.07 (= D10's own previous-vs-new comparison) | arbitrary anchor; "No single passage" advisory likely (D10 alone gives +0.07); first/latest editions | promoted q09 |
