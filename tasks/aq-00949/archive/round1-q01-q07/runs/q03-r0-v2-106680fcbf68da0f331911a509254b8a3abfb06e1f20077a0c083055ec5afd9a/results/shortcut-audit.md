role: shortcut-auditor (fresh Agent subagent, shortcut-auditor role, packet shortcut)
received: 2026-10-05
input: workspace root, packet path shortcut, q03 rev 0 question text verbatim (nothing else)
tested_sha256: 106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a
tool_uses: 19 | duration_ms: 267157

--- raw return (verbatim as received) ---

answer: Only 2Q 2025. Net cash from operating activities was $2,032M, against capital expenditures of $1,523M plus dividends paid of $528M, which total $2,051M, so it fell short by $19M. Every other quarter from 1Q 2025 to 2Q 2026 was covered.

verdict: clear

shortest_path:
1. In D01 (the March 16, 2020 release), the headline reads "2020 Capital Expenditures and Dividend Funded with Net Cash from Operating Activities". The body says "Net cash from operating activities is expected to fund both capital expenditures and dividend payments." Capital spending is defined as "Exploration and development expenditures … including facilities and gathering, processing and other expenditures, and excluding acquisitions and non‐cash exchanges."
2. That definition matches EOG's Capital Expenditures (Non-GAAP). D07's endnote 5 says it "exclude[s] Property Acquisitions, Asset Retirement Costs, Non-Cash Exchanges and Transactions and exploration costs incurred as operating expenses". D04 and D05 (endnote 4) and D06 (endnote 5) say the same.
3. D07 (the 2Q 2026 release) carries all six quarters as prior-period comparatives:
   - the cash flow statement, around lines 278 and 297
   - the free cash flow reconciliation, around lines 722 and 744

   Figures are in $M; "need" is capital expenditures plus dividends paid.

   | Quarter | Operating cash | Capital expenditures | Dividends paid | Need | Result |
   |---|---|---|---|---|---|
   | 1Q25 | 2,289 | 1,484 | 538 | 2,022 | +267 |
   | 2Q25 | 2,032 | 1,523 | 528 | 2,051 | **−19** |
   | 3Q25 | 3,111 | 1,648 | 545 | 2,193 | +918 |
   | 4Q25 | 2,612 | 1,639 | 550 | 2,189 | +423 |
   | 1Q26 | 2,966 | 1,636 | 544 | 2,180 | +786 |
   | 2Q26 | 4,669 | 1,587 | 540 | 2,127 | +2,542 |

4. The 2Q25 figures are the same in every edition that reports them: D04, D05, D06 and D07. 4Q25 has no release of its own in the packet; it appears only as a comparative in D06 and D07.

sufficient_documents: D01 plus D07 is the minimum verified set. D01 is needed to identify the measure, and D07 supplies all the figures and repeats the capex definition. Alternatives:
- D01 + D06 + D07
- D01 + D02 + D04 + D05 + D06 + D07 (4Q25 still has to come from D06 or D07)

D03 (the Encino deal announcement and dividend increase) is context only.

searches:
- Terms: fund/funded, dividend payments, "Net Cash Provided by Operating Activities", "Dividends Paid", "Total Capital Expenditures (Non-GAAP)", "Total Expenditures (GAAP)", acquisition costs, "Additions to", "Adjusted Cash Flow", special dividends.
- Read: the manifest and D01–D05 in full, D06 by targeted grep, and D07's cash flow statement, reconciliation and endnotes.
- Only D01 states the funding measure; the 2025–26 exhibits are tables only, with no narrative that reveals the answer. No document states the answer directly. D07 alone is not enough, because it shows both GAAP operating cash and Adjusted Cash Flow from Operations (Non-GAAP) and gives no reason to choose between them.

readings/gaps:
- **Wrong measure (Adjusted Cash Flow from Operations, non-GAAP):** 2Q25 becomes 2,496 against 2,051, so no quarter falls short. D01 rules this out.
- **Capex including acquisitions (Total Expenditures, GAAP):** both 2Q25 (2,411 vs 2,032) and 3Q25 (8,544 + 545 = 9,089 vs 3,111, driven by the $6,736M Encino acquisition) fall short. D01's "excluding acquisitions" rules this out.
- **Alternatives that give the same answer (2Q25 only):**
  - Cash-flow-statement additions: 2Q25 is 1,793 + 528 = 2,321, a shortfall; 3Q25 is 1,663 + 545 = 2,208, covered.
  - Including exploration costs: 2Q25 short by 93; 1Q25 covered by 226.
  - Total Expenditures less only acquisitions.
  - Dividends declared instead of paid.
- **Gap:** the packet never breaks out leasehold acquisitions. If "acquisitions" were read to include them and they exceeded $19M in 2Q25, the result could flip. EOG's own definition keeps leasehold acquisitions inside capital expenditures, so this reading is weak and cannot be computed from the packet.
- **Difficulty risk, not a shortcut:** D07's comparatives make the intermediate quarterly releases unnecessary, and the arithmetic is simple addition. The 2Q25 margin is narrow, at $19M.

Packet files:
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\shortcut\text\D01.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\shortcut\text\D07.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\shortcut\text\D06.txt
- D:\Dev\Docket\tasks\aq-00949\runs\q03-r0-v2-106680fcbf68da0f331911a509254b8a3abfb06e1f20077a0c083055ec5afd9a\shortcut\text\D04.txt
