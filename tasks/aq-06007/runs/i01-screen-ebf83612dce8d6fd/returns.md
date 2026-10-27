# i01 strong-solver screen: raw returns (2026-10-16)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i01-screen-ebf83612dce8d6fd/solver-1 and the exact sentence. Gold: 59.0%.
Returns kept verbatim in substance (harness indentation removed).

## Solve 1: 59.0% (right), confidence high

answer: 59.0%
confidence: high
path:
1. The ministers' three-year goal is a 50% cut. D11 (ATA), para 27, around "Page 5 of 12": "although ITMM set the target of 50% permit reduction in three years and 95% in five years, three years in, the activity has not delivered against the goal of reduced permit applications". D16 line 19 defines ITMM as the "Infrastructure and Transport Ministers' Meeting (ITMM)". D10 lines 220–226 and 902 (ALRTA) give the same three-year figure, "a 50% reduction in permits within three years", but call it a Kanofski recommendation. Its five-year figure is 90%, not 95%, which does not matter here.
2. D11 ¶27's own series is not the count of applications lodged by operators: "(with 196,629 in 2024-25, 172,000 in 2023/24, 151,000 in 2022/23, and 143,000 in 2021/22)". These numbers match the "NHVR cases" column of the NHVR's table in D02, not the industry column.
3. D02, "Table 3: Access permit statistics over time", lines 389–396, header "Year Industry applications NHVR cases Road manager consent requests": FY2022 77,141 / 143,951 / 233,843; FY2025 94,088 / 196,629 / 318,027. D02 line 380: "There are now over 90,000 access permit applications submitted by industry every year."
4. Year mapping from the documents: D11 labels the FY2025 NHVR-cases figure (196,629) as "2024-25" and the FY2022 figure (143,951, given as 143,000) as "2021/22". D10 line 182 gives "over 172,000 in 2023–24", which is FY2024 (172,862). So FY2022 = 2021–22 and FY2025 = 2024–25.
5. Calculation: target 77,141 × 0.5 = 38,570.5; required fall (94,088 − 38,570.5) / 94,088 = 55,517.5 / 94,088 = 0.590059 -> 59.0%.
minimal_documents: D02 + D11. D10 can't fully replace D11, because it presents the 50%/3-year figure as a Kanofski recommendation and urges "that ministers publicly commit to these targets". D10 line 219 has a ministerial "around 90%" intention, and D09 line 113 a 90% cut, but neither sets a three-year horizon.
readings:
- D11's "permit applications" series (actually NHVR cases): 143,000 -> target 71,500; (196,629 − 71,500) / 196,629 = 63.6%. With 143,951: 63.4%. These don't fit "applications operators lodged".
- Road manager consent requests: 63.2%. Not an operator-lodged count.
- Reading FY2021 as 2021–22: (86,532 − 34,945.5) / 86,532 = 59.6%. D11's own year labels contradict this mapping.
- Gap against the 2021–22 base: 55,517.5 / 77,141 = 72.0%. Doesn't fit "the number … lodged in 2024–25 have had to fall".
gaps: No document says when the three-year target clock started; the question's "measured from 2021–22" supplies this; D11 ("three years in") is consistent. Plain-text sources only; Table 3 rows extracted cleanly. Searched all 16 documents for minister/ITMM/Kanofski/NatRoad, permit terms, target/reduction, three-year phrasing, 50%/half, year forms. Read D02 L70–99, 312–419, 526–538; D10 L176–330, 890–909; D11 L1–20, 95–174; D14 L94–193; D05 L70–91. Other permit counts: D02's OSOM subsets (L529) and the HVAMS/SPV figures in D10 (L203).
contaminated: no. Did not read question.txt or anything outside text/.

## Solve 2: 59.0% (right), confidence high

answer: 59.0%
confidence: high. The question's wording points clearly to D02's "Industry applications" column. The main risk is that a solver uses D11's mislabelled figures instead, which gives 63.6%.
path:
1. The ministers' three-year goal is a 50% cut: D11 para 27 (line 124) "although ITMM set the target of 50% permit reduction in three years and 95% in five years, three years in, the activity has not delivered against the goal of reduced permit applications (with 196,629 in 2024-25, 172,000 in 2023/24, 151,000 in 2022/23, and 143,000 in 2021/22)". ITMM is the Infrastructure and Transport Ministers' Meeting (D14 line 183; D16 line 19).
2. D02 Table 3 (lines 389–396; checked against docs/ lines 387–394): "Year | Industry applications | NHVR cases | Road manager consent requests"; "FY2022 77,141 143,951 233,843"; "FY2025 94,088 196,629 318,027". Line 380: "There are now over 90,000 access permit applications submitted by industry every year." Line 384: NHVR cases measure "NHVR administrative effort (cases) triggered per application".
3. Year mapping: FY2022 = 2021–22 and FY2025 = 2024–25; D11's "196,629 in 2024-25" equals the FY2025 NHVR-cases figure and its "143,000 in 2021/22" is roughly 143,951. So D11 (and NatRoad's "over 172,000 in 2023–24", D10 line 182) quote NHVR cases, not applications.
4. Target = 50% × 77,141 = 38,570.5; required fall = 55,517.5 / 94,088 = 0.590059 -> 59.0%.
minimal_documents: D02 + D11. D02 the only source of industry-application counts (94,088 and 77,141 found only in D02). D10 gives the same 50%-in-three-years (lines 220–224, 320, 902) but credits it to the 2022 Kanofski recommendations and asks the Commission to "Recommend that ministers publicly commit to these targets"; D11 is the only document that credits the goal to ministers (ITMM).
readings:
- D11's figures at face value: 63.6%; with 143,951: 63.4%.
- Fall vs the 2021–22 baseline: 72.0% (weak reading).
- D10's Kanofski 50%/three-year target: same 59.0%.
- The "around 90%" NAAS replacement (D10 line 219, D15 line 40, D16 line 69) and D09 line 113's 90%: no three-year timeframe.
gaps: Conflicting attribution: D11 says ministers (ITMM) set the target, while D10 calls it Kanofski recommendations that ministers have not yet adopted; the three-year figure is 50% in both. Greps across all 16 files; targeted reads D10 L176–329, 894–905; D11 L100–179; D02 L372–416, 527–530; D15 L36–46; D16 L64–71; D14 L181–192. One broad "target|goal" grep output was saved outside the packet and not read; re-ran limited to terms within 120 characters of "permit". Table 3 rows match docs/ exactly.
contaminated: no

## Solve 3: 59.0% (right), confidence high

answer: 59.0%
confidence: high
path:
1. The three-year goal is a 50% cut: D11 para 27, line 124 "ITMM set the target of 50% permit reduction in three years and 95% in five years, three years in, the activity has not delivered against the goal of reduced permit applications". ITMM: D16 line 19 "Infrastructure and Transport Ministers' Meeting (ITMM)"; D14 line 183 (NAAS "was introduced at the ... (ITMM) in 2022"). D10 lines 220–224: "a 50% reduction in permits within three years", attributed to "the 2022 Kanofski recommendations, as summarised by NatRoad".
2. D02 Table 3 (lines 389–396; docs/ lines 388–394): "Year Industry applications NHVR cases Road manager consent requests"; "FY2022 77,141 143,951 233,843"; "FY2025 94,088 196,629 318,027". Line 380 "over 90,000 … applications submitted by industry every year" fits 94,088; line 384 says cases and consent requests are "triggered per application".
3. Year mapping: FY2022 = 2021–22, FY2025 = 2024–25; D11's dated series lines up exactly with D02's NHVR-cases column.
4. Target = 0.5 × 77,141 = 38,570.5; required fall = 55,517.5 / 94,088 = 0.590059 -> 59.0% (38,570 or 38,571 also give 59.0%).
minimal_documents: D02 + D11; add D16 or D14 if the "ITMM = ministers" expansion has to come from the bundle (D11 never expands ITMM). D10 can replace D11 for the arithmetic but attributes the figure to Kanofski/NatRoad (and line 320 urges "that ministers publicly commit to these targets"). No replacement for D02.
readings:
- D11's figures as printed: 63.6%; with 143,951: 63.4%. Rejected: D02 Table 3 identifies them as "NHVR cases"; the question's "applications operators lodged" matches "Industry applications" / "submitted by industry".
- Fall as a share of the 2021–22 base: 72.0% (less natural).
- Consent requests: 63.2% (not operator-lodged).
- Five-year conflict (95% vs 90%): irrelevant to the three-year goal; D10 line 219 and D15 line 40 "about 90%" with no three-year timeframe.
gaps: Text-method only; Table 3 alignment supported by header order, D02 lines 380 and 384, and D11's 196,629 matching the middle column. Searched all 16 documents; read D11 L100–174, D10 L172–252 and the L320/902 hits, D02 L90–99, 372–441, 520–541, D14 L181–188; D01, D03–D09, D12, D13, D15 not end to end. Did not open question.txt.
contaminated: no
