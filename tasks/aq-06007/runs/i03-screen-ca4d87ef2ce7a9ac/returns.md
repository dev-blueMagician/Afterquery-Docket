# i03 strong-solver screen: raw returns (2026-10-16)

Three fresh blind-solver contexts (claude-opus-5-5, effort max), each given only the workspace root,
the packet path runs/i03-screen-ca4d87ef2ce7a9ac/solver-1 and the exact sentence. Gold: 5.3.
Returns kept verbatim in substance (harness indentation removed). Numbered by launch order.

## Solve 1: 5.3 (right), confidence high

answer: 5.3 (billion dollars)
confidence: high
path:
1. 2024 estimate (D07, Australian Industry Group submission, Dec 2025; text/D07.txt line 63; same text in docs/...sub015... line 61): "The Australian Local Government Association reports that the replacement cost of sealed roads in poor condition is $19.2bn and the replacement cost of unsealed roads in poor condition, many of which are in regional, rural, and remote areas, is $3.9bn. 5". Footnote 5 (line 75): "ALGA, National State of the Assets Report 2024". The roads are local roads: the sentence just before says "Local governments manage around 80% of Australia's road network by length", and the section is headed "Funding certainty for local government".
2. 2021 estimate (D10, ALRTA; text/D10.txt lines 259-263; docs/...sub019... line 261): "ALGA's 2021 State of the Assets–backed analysis shows that: about 8% of sealed local roads and 14% of unsealed local roads are in poor condition, function and capacity, close to the end of their useful life, and the estimated replacement cost of these roads is $17.8 billion". "These roads" means both the sealed and the unsealed poor-condition roads, so $17.8bn is a single combined figure. Footnote 33 "Ibid." -> footnote 32 "Australian Local Government Association (ALGA) 2022, Pre-Budget Submission 2022–23".
3. Matching: 2024 sealed + unsealed = 19.2 + 3.9 = 23.1 billion.
4. Difference: 23.1 − 17.8 = 5.3 billion. Check: 17.8 + 5.3 = 23.1.
minimal_documents: D07 + D10. Neither can be swapped out.
readings:
- Sealed only for 2024: 19.2 − 17.8 = 1.4. Not a fair comparison: D10's $17.8bn covers both sealed and unsealed roads.
- Unsealed only: nonsensical comparison (3.9 against 17.8). Rejected.
- Source of the 2021 figure: D10 cites it to ALGA's 2022 Pre-Budget Submission while calling it "2021 State of the Assets–backed"; the only 2021-era ALGA figure in the packet; answer stays 5.3.
gaps: The ALGA reports themselves are not in the packet; could not check whether they use the same scope or definition of "poor condition" (D10 "poor condition, function and capacity"; D07 "poor condition"). D07 says "sealed roads" and "unsealed roads" without "local"; relied on context and the ALGA source. Plain-text sources; decisive lines match docs/ word for word. Searched all 16 for State of the Assets/SOTA, ALGA, poor/very poor condition, replacement cost, billion/bn, 17.8/19.2/3.9/23.1, local road(s), unsealed, backlog, renewal, infrastructure gap, end of useful life, asset condition; checked every "billion" hit in context (D02, D06, D08, D10, D11, D12, D13, D14, D15). Full reads: D07 L1-12, 40-99; D10 L1-12, 150-344; D08 L90-139; D15 L30-54.
contaminated: no

## Solve 2: 5.3 (right), confidence high

answer: 5.3 (the 2024 estimate was about $5.3 billion higher: $23.1bn against $17.8bn)
confidence: high
path:
1. D07 line 63: "The Australian Local Government Association reports that the replacement cost of sealed roads in poor condition is $19.2bn and the replacement cost of unsealed roads in poor condition, many of which are in regional, rural, and remote areas, is $3.9bn. 5"; footnote 5 (line 75) "ALGA, National State of the Assets Report 2024"; context line 63 "Local governments manage around 80% of Australia's road network by length."
2. D10 lines 259-263: "ALGA's 2021 State of the Assets–backed analysis shows that: about 8% of sealed local roads and 14% of unsealed local roads are in poor condition, function and capacity, close to the end of their useful life, and the estimated replacement cost of these roads is $17.8 billion"; footnote 33 "Ibid." -> footnote 32 (line 286) ALGA 2022 Pre-Budget Submission 2022–23. "These roads" covers both sealed and unsealed.
3. 19.2 + 3.9 = 23.1; 23.1 − 17.8 = 5.3 (rechecked).
4. Confirmed in docs/: sub015 line 61 "$19.2bn" and "$3.9bn"; sub019 line 261 "$17.8 billion".
minimal_documents: D07 + D10; each the only source for its year.
readings: A (adopted) 2024 total vs 2021 total: 5.3. B (weaker) 2024 sealed vs 2021 total: 1.4, not like for like. Wording difference ("poor condition, function and capacity" vs "poor condition"): both ALGA poor-condition replacement-cost estimates. Citation note: 2021 analysis cited through the 2022 Pre-Budget Submission; matches the question.
gaps: Searched all 16 for State of the Assets/SOTA, ALGA and other LGA bodies, poor/very poor, sealed/unsealed, replacement cost/replace/renew/backlog/funding gap, billion/bn amounts incl. 17.8/19.2/3.9/23.1, local road(s), road condition. Only D07 and D10 contain the estimates; irrelevant hits D05:83, D06:17, D06:286, D09 LGA lines, D10:361, D14:155. Did not open question.txt.
contaminated: no

## Solve 3: 5.3 (right), confidence high

answer: 5.3 (billion dollars: the 2024 estimate of $23.1bn minus the 2021 estimate of $17.8bn)
confidence: high
path:
1. D07 (Ai Group), text/D07.txt line 63, "Funding certainty for local government": "Local governments manage around 80% of Australia's road network by length. 4 The Australian Local Government Association reports that the replacement cost of sealed roads in poor condition is $19.2bn and the replacement cost of unsealed roads in poor condition, many of which are in regional, rural, and remote areas, is $3.9bn. 5". Footnote 5 (line 75) "ALGA, National State of the Assets Report 2024". docs/ sub015 lines 61 and 73 match.
2. D10 (ALRTA), lines 259–263: "ALGA's 2021 State of the Assets–backed analysis shows that: - about 8% of sealed local roads and 14% of unsealed local roads are in poor condition, function and capacity, close to the end of their useful life, and - the estimated replacement cost of these roads is $17.8 billion". Footnote 33 "Ibid." -> footnote 32 ALGA 2022 Pre-Budget Submission 2022–23. docs/ sub019 lines 257 and 261 match.
3. "These roads" refers to the 8% sealed and 14% unsealed, so the 2024 figures must be added: 19.2 + 3.9 = 23.1.
4. 23.1 − 17.8 = 5.3 (checked: 23.1 − 17 = 6.1; 6.1 − 0.8 = 5.3; 17.8 + 5.3 = 23.1).
minimal_documents: D07 + D10. Neither can be replaced.
readings: Sealed only for 2024: 1.4 (weak; compares a sealed-only figure with a combined one). Unsealed only: no separate 2021 unsealed figure, unanswerable. 2021 figure as a 2022 estimate (cited to the 2022 pre-budget submission): number unchanged; D10 calls it the 2021 State of the Assets analysis. Wording "poor condition, function and capacity" vs "poor condition": treated as the same measure.
gaps: Read D07 L1–12, 40–89; D10 L1–12, 230–289; regex searches of all 16 for State of the Assets, poor/very poor condition, ALGA, replac, billion/bn, 17.8/19.2/3.9/23.1, local road, sealed/unsealed/SoA/asset condition/road condition; searched docs/ for the decisive figures. Plain text only. The original ALGA reports are not in the packet; neither excerpt gives a price basis (nominal or real).
contaminated: no. Only the workspace root, packet path and question were provided; question.txt not opened. The automatic context listed modified .claude/ and CLAUDE.md files in git status as file names only; no content was shown.
