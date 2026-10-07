# q04 rev 2, shortcut auditor (raw return, verbatim)

- Recorded: 2026-10-06. Fresh shortcut-auditor agent (Claude Code, claude-opus-5-5), packet
  shortcut, input = workspace root, packet path and exact question only.
- tested_sha256: 8572d4023085944a5d6a29249b7f0ef0028c7affa2f7ccae708db952d0cc2484

answer: **Peru, +26%.** Without the American Rescue Plan Act (ARPA) money, Peru's FY2021 State Department- and USAID-managed aid was $85.535M. The FY2024 request was $107.635M, a change of +25.8%, which rounds to **+26%**.

verdict: clear

shortest_path:
1. D06 Table 2 (`D:/Dev/Docket/tasks/aq-docket-trial-04/runs/q04-r2-v2-8572d4023085944a5d6a29249b7f0ef0028c7affa2f7ccae708db952d0cc2484/shortcut/text/D06.txt`, lines 325-489) gives FY2021 actual and FY2024 request, in thousands. Its note says "a. FY2021 sums include some supplemental assistance appropriated in the American Rescue Plan Act of 2021 (P.L. 117-2)." The FY2021 figures are Peru 98,885 (FY2024 request 107,635), Colombia 478,192, Brazil 27,950, Paraguay 9,600, Ecuador 28,750, Bolivia 4,000 and Uruguay 900.
2. D05 Table 2 (`.../text/D05.txt`, lines 541-1087) says FY2021 totals "do not include assistance made available through supplemental emergency appropriations (P.L. 116-123, P.L. 116-136, or P.L. 117-2)." Its FY2021 figures are Peru 85,535, Colombia 465,092, Brazil 19,450, Paraguay 4,400, Ecuador 23,750 and Uruguay 400. Bolivia has no row, so it counts as 0.
3. The ARPA amount per country is D06 minus D05:

| Country | ARPA (thousands) |
|---|---|
| Peru | 13,350 |
| Colombia | 13,100 |
| Brazil | 8,500 |
| Paraguay | 5,200 |
| Ecuador | 5,000 |
| Bolivia | 4,000 |
| Uruguay | 500 |
| Argentina, Chile, Guyana, Suriname, Venezuela | 0 |

   Haiti's 14,800 is larger than Peru's, but Haiti is not in South America.
4. Cross-check: the differences across all rows add up to 97,150, matching D06 Table 1 note a, "$97.2 million of supplemental assistance appropriated in the American Rescue Plan Act." Then 1,794,345 (D05 total) + 97,150 + 5,000 (OAS contribution, which only D06 counts) = 1,896,495, exactly D06's total. FY2021 Economic Support Fund is 480.7 in D06 against 378.5 in D05, a gap of 102.2 = 97.2 + 5.0. Every other account is identical in both reports.
5. The calculation is (107,635 − 85,535) / 85,535 = 22,100 / 85,535 = +25.84%, which rounds to +26%. Using millions gives the same result: Peru's ARPA is 13.4 against Colombia's 13.1, and (107.6 − 85.5) / 85.5 = +25.8%.

sufficient_documents: D05 and D06 together. Neither works alone: D05 has no FY2024 request and no ARPA breakdown, and D06 includes ARPA in FY2021 without giving per-country amounts.
- D05 Table A-1 (lines 1383-2109, in millions) can stand in for Table 2: Peru 85.5, with ESF "—"; Colombia 465.1.
- D06 Table A-3 (line 1076) confirms Peru's FY2024 request as 107.6.
- D08 Table A-1 (lines 675-812) is optional corroboration. It marks "a" on exactly the 18 rows with nonzero differences, including "Peru 98,885a" and "Colombia 478,192a". It gives no ARPA amounts, and its columns are FY2021, FY2022, FY2023 and the FY2025 request, so it has no FY2024 request.

searches:
- Terms searched: "American Rescue Plan", "ARPA", "P.L. 117-2", "Rescue" (case-insensitive), "supplemental assistance", "Peru", "Bolivia", "Table A-", "FY2024 Request", and the candidate amounts "13.4 million", "13,350", "13.1 million" and "13,100".
- Read in full: the openings of all eight documents and the manifest; D05 Tables 1, 2 and A-1; D06 Tables 1 and 2 plus the A-3 header; D08 Table 1 and Table A-1.
- Ruled out:
  - D01-D04 and D07 are off-topic.
  - The D07 "Rescue" hit refers to the International Rescue Committee.
  - D05 line 517's "13.4 million" is about Mexico's FY2023 change and only coincidentally matches.
  - No document states Peru's ARPA amount or its percentage change directly, and no text passage ranks countries by ARPA money.

readings/gaps:
- Keeping ARPA in the FY2021 base gives (107,635 − 98,885) / 98,885 = +8.85%, or +9%. The question's "without that money" rules this out.
- Picking Colombia, the near-tie and obvious guess, gives 465,092 → 444,025 = −4.5%, or −5%.
- Ignoring "South American" picks Haiti: 189,577 → 291,455 = +53.7%, or +54%.
- Other fiscal years are distractors: the FY2025 request (D08, 94,800) and the FY2023 request (D05, 109,870).
- Assumption: each country's D06−D05 gap is entirely ARPA money. The exact reconciliation, the absence of any negative gaps and D08's flags all support this, but no document states per-country ARPA amounts.
- Difficulty risk: the route is a simple cross-document join followed by a ratio. That is allowed and is not a shortcut. The 250K gap between Peru and Colombia makes it easy to pick the wrong country.
- Extraction: D05's tables are split into one value per line, but the values line up and match the Table A-1 totals. I found no material unread gaps.
