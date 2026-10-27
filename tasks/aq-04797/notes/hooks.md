# aq-04797 - cross-document hooks

Target: medium (user, 2026-10-14: "there is no slot for Easy Tier for this bundle, we should target
medium and high"). Page slots then: Hard 0/5 · Medium 0/1 · Easy 1/0, so the check may start at High.
No earlier captures exist for these bytes. Doc numbers are the page's; local ids in `doc-map.md`.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | Doc 5 lines 186, 389 (test set used for fine-tuning), 212 (R² 0.959 before, 0.977 after); Doc 6 line 215 (held-out Batch1 cells, R² 0.977) | R² on cells each model never saw: 0.977 - 0.959 = 0.018 | Same label, different scope; calculate across documents | Lazy: Doc 5 headline 0.977 -> 0.000; line 188's 0.986/0.998 -> -0.009/-0.021 | Doc 5 contradicts itself (line 188 vs Table 4); "the model" could be read as the final network only | sketch i01 -> q02 rev 0: Too easy, High 3/3 (2026-10-14); retired for the high model: the scope phrase "never saw" sent every attempt to the deciding passage |
| h2 | Doc 1 line 65 (four NASA cells, 2 Ah and B0018 1.35 Ah); Doc 4 lines 31, 221 (B0005 only) vs 316-320 (B0007 added) | Nominal capacity of NASA cells Doc 1 models and Doc 4 does not: 3.35 Ah | Bury one list item late; match, then exclude | Without the late B0007: 5.35; B0018 at 2 Ah: 4.00 | Doc 4's generic "2Ah" (line 23) | sketch i02 |
| h3 | Doc 4 lines 27, 290 (0.7462% of 2.0 Ah nominal); Doc 6 lines 139, 145, 231 (1.025% of 1.35 Ah rated) | MAE in amp-hours, B0005 / CX2 = 14.92 / 13.84 = 1.08 | Unit normalization (ranking flips) | Percent ratio 0.73; CX2 at Doc 7's 1.1 Ah 1.32 | Doc 4's "MAE (%)" could be read as a relative error | sketch i03 (0 unpointed) |
| h4 | Doc 6 lines 5, 139, 231 (per-dataset MAEs, 8/15/4 cells, printed mean 0.561%); Doc 4 line 290 | Per-cell mean 0.4254%; 0.7462 - 0.4254 = 0.32 | Calculate across documents (average of averages) | Printed 0.561 -> 0.19 | Dataset MAEs assumed to be per-cell means | sketch i04 (0 unpointed) |
| h5 | Doc 1 line 65 (NASA 20 mA; 2 Ah; B0018 1.35 Ah); Doc 7 line 191 (#3 hold at 4.2 V until below 0.03 A; #5 below 1.35 A), Table 1 lines 49, 51 (3.03 Ah, 27 Ah), line 41 (C-rate vs nominal) | Cells ending CV charge at or below B0005's C/100: B0006, B0007, PANASONIC NCA | Bury one list item late; calculate across documents (normalise) | NASA only -> B0006, B0007; absolute -> + B0018; decoys Doc 5 C/50, GOTION C/20, CS2 0.05 A | Doc 1's B0018 1.35 Ah vs public recall | sketch i05 -> q01 rev 0: Too easy, High 3/3 (2026-10-14); retired for the high model: a member found by sweeping one named property across every paper |

Rejected or held (2026-10-14, caller):
- End-of-life comparisons (Doc 5 80% of nominal vs Doc 2 20% loss of BoL, Doc 9 50% of initial): the
  20%/80% convention is guessable without Doc 2, so delete-and-guess reaches the gold; Doc 9's coin-cell
  stopping rule applied to LFP cells is contrived.
- SOH-basis membership list (initial: Docs 1, 2, 7; nominal/rated: Docs 4, 6, 8): answer would be
  papers (rule 10), and Docs 5 and 9 have borderline membership.
- B0005 cathode reconciliation (NCA in Doc 1, NCM in Doc 4 line 23, "e.g., lithium cobalt oxide" in
  Doc 4 line 348): the LCO member rests on an "e.g." aside; a second reading stays open.
- Oxford = KOKAM joins (Doc 3 740 mAh, Doc 7 0.74 Ah): the bundle never states the identity; recallable.
- CALCE capacity questions: Doc 1's CS2 capacity is not stated; Doc 6 CX2 and Doc 7 CALCE are
  different series.
- Cross-paper comparisons of Doc 1's NASA errors: Doc 1 labels 0.0038-type values "(%)".
- Doc 3 ablation figures: its two D4->D3 ablations disagree; Tsinghua temperatures conflict.
- C-rate / CV cut-off conversions (Doc 5 C/50 of 1.1 Ah vs Doc 7 1.35 A; NASA 20 mA): every step named.
- Parameter counts (Doc 1 119,617; Doc 5 ~22,000 vs table 20,000; Doc 6 ~0.45 M): table-vs-prose
  only, pointed once the table is named; LSTM re-sizing with Doc 4's six features is textbook.
- Doc 3 calibration shares vs Doc 7's "at least 25-30%": two lookups, count of 4 printed as "half".
- Sampling and inference-time joins (Doc 8 100 ms vs Doc 2 1 Hz, Doc 6 1/30 Hz, 17.55 ms): two lookups.

Independent author A (results and evaluation protocols; question-author run, 2026-10-14; full read of
all nine texts): no fair design with an unpointed step outside h1-h4. Closest candidates, all dropped
(ids A1-A5 here, not sketch ids):
- A1 Doc 5's lowest RMSE on the 39 test cells is 0.00462 Ah, only in the sampling-interval paragraph
  (line 285), beside the headline 0.00479: single-document; partners are h3- or h1-type only.
- A2 Doc 4's best-model training share (70% of 166 cycles minus 32) vs Doc 1's 60%: 0 unpointed; the
  denominator (166 vs 169 cycles) decides the answer.
- A3 samples per cell, Doc 7 (10,757 / 65) vs Doc 9 (695 / 105) = 25.0: unqualified "samples" also
  fits 71,588 ("collected from 65 cells", Doc 7 line 21), so a second defensible reading.
- A4 Doc 5's 202 modelled cells vs Doc 9's 105: 0 unpointed; "validated on 222" (line 7) is a second reading.
- A5 B0007's discharge cut-off (Doc 1 2.2 V vs Doc 4's dataset-wide 2.7 V): recallable NASA figures.
Extra hazards it logged: Doc 5 "average MAPE of 0.481 Ah" (line 212) and Table 5 schemes that do not
sum to 100%; Doc 3's B1->B2 (line 189) vs B2->B1 (line 241) and D4 RMSE 0.0029 (line 215) vs
D3->D4 0.010683 (line 245); Doc 9 MSE units never given; Doc 6 "iterations" vs epochs (line 151).

Independent author B (definitions, criteria and rules; question-author run, 2026-10-14; full read):
one design with an unpointed step, adopted as h5 / i05. Below the bar (ids B1-B4 here):
- B1 B0007's charge-to-discharge cut-off span, 4.2 - 2.2 = 2.0 V (Doc 4 line 316 + Doc 1 line 65;
  lazy 1.5 V from Doc 4's dataset-wide 2.7 V): semi-pointed only; NASA cut-offs are recallable; Doc 4's
  2.7 V threatens one defensible answer.
- B2 Doc 3's scored share 22.5% (7:3, then 75% of the 30%) vs Doc 4's 30%: 7.5 pp; the correction
  closes the same sentence.
- B3 Doc 9's stop at 50% of initial vs Doc 2's LFP 86%: 36 points; both named.
- B4 Doc 3's calibration rule on other papers' cells: CS2's 3712 cycles conflicts with "several hundred
  cycles"; B0005's 166 makes the 80-cycle floor and the 35% cap clash; 1057 cycles needs rounding.
Numeric sibling of h5 (highest relative end current / B0005's = 5.00) fails delete-and-guess.

After two runs (2026-10-14), both starting at the High level: no remaining hook or sketch has a deciding step that is
neither a lookup, a sweep of a named property, nor an inference the wording asks for. Checked again: Doc 5's
prose-only lowest RMSE (0.00462 at sampling interval 20, l285) is reached by any lookup of "RMSE"; i02's B0007
is a cell-ID sweep; i03 and i04 name every step.
