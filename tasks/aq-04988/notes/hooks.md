# aq-04988 - cross-document hooks

Caller's inventory, 2026-10-14 (all ten texts read in full). Doc N = page number; Dnn = local id (doc-map.md).
Target in files: medium (user: no Easy slot, "target medium and high"). Slots at capture: Hard 1/5 · Medium 0/1 ·
Easy 0/0. Every run on 2026-10-14 with "Medium 0/1" started at the High level (aq-04797, aq-04421, aq-04807), so each
hook is audited against the high solver: two solvers x 3 tries, ready only if both miss at least once.

Audit rule (memory): a step is pointed when a lookup of any word in the question reaches it; a sweep of one named
property across every paper is pointed for the high model. Count only unpointed steps.

| Hook | Inputs (location) | Possible ask | Lever | Unpointed steps / high-model default | Decision |
| --- | --- | --- | --- | --- | --- |
| h1 | Doc 9 D05 l157/l177 (Argentina target <5 g; 11 g in 2011) + Doc 7 D01 l211 (Argentina 11.2 -> 9.2, 2011-2015) | gap between Argentina's latest measured intake and its national target | scatter, right edition | 0: "Argentina" sweeps to both rows; delete-and-guess fails Doc 9 (target = WHO 5 g, recalled) | drop |
| h2 | Doc 9 Table 2 (Mongolia 10.5 g 2019, Vietnam 9.4, SA 6.8, Argentina 11 g 2011) + Doc 7 (Argentina 9.2 in 2015) | order the four countries by most recently measured mean salt intake | ordered answer, late member | 1 at most: Argentina's 2015 value sits only in Doc 7's table; but the country name is in the question and the high model sweeps it | sketch candidate (quick test only) |
| h3 | Doc 1 D10 l84 (2020 targets, 4-year time frame) + Doc 10 D02 l222 (released May 2020) | month/year companies were to meet HFP targets | date join | 0; real-world date may be recalled | drop |
| h4 | Doc 3 D08 Table 2 HeartSAFE targets + Doc 4 D03 Table 1 medians (bacon, ham, sausages) | countries whose median meets the NZ target | calc across docs | 0: both named | drop |
| h5 | Doc 8 D07 l165 (SA 2019 limits) + Doc 3 D08 Table 2 (NZ crisps 520, extruded 770, S&V 740) | strictest limit for a product sold in both | posed case | 0; S&V/extruded mapping ambiguous in NZ table | drop |
| h6 | Doc 5 D06 l53 (8, <6, <5 g scenarios) + Doc 7 D01 l234 (Japan 9.9 g 2011) | scenarios meeting a 30% cut from 2011 | rule applied | 0; Doc 5's own 9.7 gives the same answer, so Doc 7 not needed | drop |
| h7 | Doc 1 D10 l194 (107 mg/d, nondiscretionary = 85%) + Doc 3 D08 l231 (260 mg/d; total 3100-3500) | share of TOTAL intake cut, NZ vs Australia | basis reconciliation | NZ total is a range: no single gold | drop |
| h8 | Doc 1 D10 Table 2 + Doc 7 D01 l24 (2017 event) | Australia's 2017 CVD deaths from % averted | event-dated period | Doc 1 states 2017 itself; Doc 7 not needed; table vs text gives 50,238 vs 52,500 | drop |
| h9 | Doc 2 D04 l166 (Turkey 1.2 g/day sodium) + Doc 7 D01 l247 (Turkey 18.0 -> 15.0 salt) | Turkey vs Brazil reduction | sodium vs salt basis | Doc 2 alone has both Brazil and Turkey; Doc 7 not needed | drop |
| h10 | Doc 5 D06 l88-90 (10-year cumulative) + Doc 2 D04 Table 2 (20-year cumulative) | annualised deaths averted, Japan 8 g vs Brazil | per-year vs cumulative | 0: high model annualises; Brazil 2,600 vs 2,500 conflict | drop |
| h11 | Doc 4 D03 Table 2 daggers (average targets) + Doc 1 D10 l343 (modelled UK MAXIMUM targets) | meat/fish categories benchmarked on a target type the Australian model did not use | definition applied | "would not have used" is speculative; pointed | drop |
| h12 | Doc 8 D07 l146 SA 2016 67% (Doc 9 D05 l146) vs Durban 96% | compliance gap | calc across docs | 0; trivially pointed | drop |

Conflicts noted for avoidance (doc-map.md): Doc 5 <5 g components; Doc 2 2,600/2,500; Doc 7 vs Doc 9 on Argentina's
reduction; Doc 3 vs Doc 7 on Portugal's tax; SA regulation year 2012 vs 2013; Doc 1 107 vs Doc 3's "Australian study" 50.

Structural finding: no forecast/actual, proposal/final or amendment pair across papers; no paper analyses another's
data. Cross-paper links are shared countries (salt-intake series), shared target systems (UK 2017, HeartSAFE, SA Reg 214)
and repeated counts (32/75/96 initiatives).

## Independent authors (2026-10-14, origin claude; both read all ten texts)

Neither author found a design with two unpointed steps in different passages.

| Hook | Inputs | Ask / gold | Unpointed steps | Decision |
| --- | --- | --- | --- | --- |
| A-h1 (i01) | Doc 7 D01 l211 Argentina 11.2->9.2 g salt; Doc 2 D04 l167 "Mandatory reformulation alone ... 0.58g/day" (sodium: l166 and l168 say sodium; Turkey 1.2 = Doc 7's 3.0 g salt / 2.5) | ratio 1.4 (lazy 3.4) | 1 (units), cue adjacent | sketch i01 |
| B-i01 (i02) | Doc 7 Table 1 24-h urine rows + footnote; Doc 9 D05 l177, l248-249 (Argentina regional) | largest whole-country % fall = Turkey 16.7% (lazy Argentina 17.9%) | 1 half-pointed (exclusion in another paper) | sketch i02, lead |
| A-h2 | Doc 1 D10 l15/l264 (optimistic +1,065 over 514); Doc 10 D02 l32 (22,000 diet deaths 2019) | 7.2% | 1, cue in-sentence ("additional") | not offered: figures no document connects |
| A-h3 | Doc 8 D07 l165 (C2 40/40 met 2016) vs swapped l252-256; Doc 9 D05 l146 (67%) | 33 pp | contradiction resolved by explicit counts first | not offered |
| B-i02 | Doc 6 D09 l99 (five table-salt policies, two in cities); Doc 9 D05 l222-223 (Argentina national) | 4 countries | none effective | not offered |
| B-i03 | Doc 3 D08 l38 (17 categories); Doc 1 D10 l143 (12 major categories) | 5 | none | not offered |
| A-h7 | Doc 8 D07 l312 (Africa-Predict -1.2 g/day sodium, 20-30-year-olds) + Doc 9 SA 6.8 g, <5 g | units | sodium named in-sentence; subpopulation | dropped |
| rejected by both | Australian HFP cut 107 (Doc 1) vs "Australian study" 50 (Doc 3); Portugal tax (Doc 3 vs Doc 7); May 2024 deadline (Doc 1 + Doc 10); SA regulation year; Doc 5 <5 g sums; Doc 2 case-years vs Doc 5 events; NZ targets vs other thresholds | - | - | closed |

## Round 2 (2026-10-14, after q02's High 3/6 and q01's screen 3/3)

Author C (fresh, origin claude) read all ten texts under the hard playbook and found no new fair Hard sketch.
Closest candidates, all dropped: i06 (Doc 4 Table 2: six categories where another country beats the UK, against the
prose's "except for bacon"; single document); i07 (Doc 7: Samoa and Switzerland rises against the prose's "1 country had
a slight increase"; single document); i08 (Doc 4's average-target daggers against Doc 1's "maximum (rather than average)";
Doc 1 never says what it did where no maximum existed, so nothing settles it); i09 (Doc 1's 3.7% of nondiscretionary vs
3.13% of total; NZ's total is a range, no single gold). Other joins: lookups, unit conversions or date spans (playbook
section 3), already-cleared families, unmatched populations or inconsistent data (Doc 8's S&V means: 9 x 722 + 1036
gives 753.4 against the printed 799). Screens this round: i03, i04, i05 each 3/3 right (ledger rows 20, 18, 19).
