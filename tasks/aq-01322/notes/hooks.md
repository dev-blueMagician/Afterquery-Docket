# aq-01322 - cross-document hooks

Bundle: six Cencora, Inc. quarterly earnings releases (fiscal year ends September 30).
Local ids vs task page: D01=Doc 4 (Q1 FY26, 2026-02-04), D02=Doc 1 (Q2 FY25, 2025-05-07),
D03=Doc 5 (Q2 FY26, 2026-05-06), D04=Doc 2 (Q3 FY25, 2025-08-06), D05=Doc 6 (Q3 FY26,
2026-08-05), D06=Doc 3 (Q4/FY25, 2025-11-05). Target: medium (user, 2026-10-06: "at least medium").

Structural facts behind the hooks:
- FY2026 guidance editions: E1 D06 (Nov 5, 2025), E2 D01 (Feb 4, 2026), E3 D03 (May 6, 2026),
  E4 D05 (Aug 5, 2026). Non-EPS rows never restate the prior edition's value, except D01's prose
  "previous range of growth of 8% to 10%" for adjusted operating income. EPS: E1=E2 $17.45-17.75
  (printed in D06, D01 and D03 "previous range"), so EPS rows are never individually necessary.
- D05 prose calls the range it replaced "$17.70 to $17.90", but D03 set $17.65 to $17.90: any
  window between May 6 and Aug 5, 2026 has an uncertain EPS edition (possible unseen update). Avoid.
- FY2025 editions (D02 May, D04 Aug) print every "previous range" themselves: one-document risk.
- Segment reorganization effective Oct 1, 2025 (D06): Other = MWI Animal Health, Profarma,
  U.S. Consulting Services, other PharmaLex components. FY2025 quarters exist on both bases:
  original (D02 Q2 + 6M, D04 Q3 + 9M, D06 Q4 + FY) and restated (D01 Q1, D03 Q2 + 6M, D05 Q3 + 9M).
  Restated FY2025 full-year segment values are printed only rounded ($285.0B, $28.3B, $8.2B,
  $3.3B, $588M, $352M) and repeat in every FY2026 table (never individually necessary).
- Dated events: RCA acquisition Jan 2, 2025 (D02/D04/D06/D01 footnotes); OneOncology completed
  (D01 headline, no date) on Feb 2, 2026 (D03/D05 cash-flow footnotes; "February 2026" prose);
  U.S. Consulting Services held for sale (D01, Q1 FY26 impairment), "divested in April 2026"
  (D05 only, three places); MWI held for sale (D03, Mar 31, 2026 balance sheet); MWI-Covetrus and
  EyeSouth agreements (D03, undated); $1B repurchases in Q3 FY26 (D05); CFO change (D05, undated).
- Adjusted FCF = operating cash flow - capex - antitrust settlement gains (stated method). Printed:
  6M FY25 $176.0M (D02), 9M FY25 $92.5M (D04), FY25 $2,970.8M (D06), Q1 FY26 $(2,436.7)M (D01),
  6M FY26 $(1,280.2)M (D03), 9M FY26 $1,142.3M (D05). Q1 FY25 is printed nowhere; only D01's
  comparative column and footnote hold its inputs.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| h1 | D05 L81/L269/L393 "divested in April 2026"; D01 L17 date, L107-114 table (E2); D03 L15, L116-123 (E3); D05 L111-118 (E4); D06 L131-138 (E1) | FY2026 guidance in force when U.S. Consulting was divested (Other AOI: Flat; revenue: 7-9%) | Same series, right edition; scatter | E4 in the event's own release and E3 (issued May 6, after April) both carry the same label; only timing rules them out | No tie between any guidance update and the divestiture (D03 ties Other's change to MWI held for sale) | sketch i01 (Other), i02 (revenue) |
| h2 | D03 L639 "February 2, 2026 acquisition of OneOncology", L686 6M adj FCF; D01 L469 Q1 adj FCF | Adjusted FCF in the fiscal quarter OneOncology closed (Q2 FY26 = +$1,156.5M) | Period identified by a fact; exact derivation | D01, the release announcing completion, prints Q1 $(2,436.7)M; D03 prints six-month $(1,280.2)M with the same label | YTD de-cumulation is a known transform; event date plainly printed in D03 | sketch i05 |
| h3 | D06 FY25 adj FCF prose; D01 L404/L406 comparatives + L200 footnote ($22.9M gains); D01 L469 | Adjusted FCF over calendar 2025 by the stated method ($3,381.6M) | Method applied to an unreported period; temporal alignment | FY25 printed $2,970.8M; Jan-Sep only; unadjusted Q1 FY25 | Q1 recall by closed-book model; arithmetic-only path | sketch i04 |
| h4 | D04 L423/L431 Q3 FY25 original US revenue/OI; D05 L456/L465 restated Q3 FY25 US revenue/OI, L490 Other margin | Operating margin of the operations the restatement removed from U.S. Healthcare Solutions (4.44%) | Calculate across documents; carve-out | D05 prints Other's own Q3 FY25 margin 4.13% (Other also holds International-origin operations: combined 4.21%) | Intersegment elimination shift makes "removed operations" a difference measure; must be worded as such | sketch i03 |
| h5 | D01/D03/D05 OneOncology; D06 E1 table | Guidance in force at OneOncology closing (E1) | edition | D01 ties its update to the completed acquisition (aq-00745 q01 tie: Easy) | E1 is Nov 2025, recall risk | not pursued (predicted Easy) |
| h6 | D03 6M - D01 Q1 acquisitions spend | Cash spent on acquisitions in the OneOncology quarter ($4,712.4M) | period by fact | D01 Q1 $219.7M | Total near the public deal price: closed-book risk | replaced by h2 |
| h7 | Guidance tables E1-E4 | Metrics changed in every FY26 update | list | many near misses | exhaustive table lookup; list shape the user disfavours | not pursued |
| h8 | D05 prose "$17.70 to $17.90" vs D03 $17.65 | documents disagree on the replaced EPS range | reconcile | n/a | two lookups; possible unseen update | not pursued; recorded as ambiguity source |
| h9 | FY25 calendar/TTM revenue or AOI | additive rebuilds | arithmetic | n/a | every quarter is rebuildable from two releases: only one document individually necessary | rejected (necessity) |
| h10 | D04 Aug FY25 guidance vs D06 FY25 actuals | segment OI beat/miss vs guidance | forecast/actual | n/a | "approximately" edges; two lookups; pre-cutoff facts | not pursued |

The map is navigation; quotes come from originals/extracted sources. A short valid calculation
or ID join is eligible. Prior failures suggest tests/priority, not a universal veto.
