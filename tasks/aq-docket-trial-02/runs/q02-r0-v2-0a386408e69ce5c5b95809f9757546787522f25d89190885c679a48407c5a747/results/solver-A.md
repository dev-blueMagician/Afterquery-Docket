# q02 rev 0 - blind solver A (raw, verbatim)

- Date: 2026-10-06. Fresh blind-solver agent (claude-opus-5-5, omitClaudeMd, scope hook), given only
  the workspace root, the solver-1 packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 0a386408e69ce5c5b95809f9757546787522f25d89190885c679a48407c5a747

## Return

answer: **$132 million**

confidence: high

path:
1. **Latest estimate (D11, 1 May 2026 Q1 release, line 39):** The board approved an expansion on April 30, 2026. The release says "cumulative pretax charges related to the SGPP, once all projects are approved and implemented, are now estimated to be $350 million to $550 million, increased from $200 million to $300 million." The midpoint is (350 + 550) / 2 = **$450M**. D12 (31 July 2026) does not change this estimate. Searching it for "estimat", "expansion", "approved", "incurred" and "savings" only finds the market-share boilerplate on lines 133 and 135. So D11 is the latest estimate both at June 30, 2026 and in the whole packet.
2. **Program start and alias (D07, 1 Aug 2025, line 41):** "the Company today announced a new three-year productivity program … cumulative pre-tax charges … totaling between $200 and $300 million." This is the same "$200 million to $300 million" range that D11 says was replaced. D08 (line 37) calls it the "previously announced Strategic Growth and Productivity Program." So no charges could have come before Q3 2025.
3. **2025 charges (D09, Q4/FY2025 release):**
   - Line 495: Corporate operating profit for the twelve months of 2025 "included … the Strategic Growth and Productivity Program of … $13". Line 491 gives the same $13 for Q4.
   - The full-year income-before-taxes table (line 865) has "Restructuring programs(1) 13 2 11 — 11". Note (1) on line 903 says these charges "relate to the Strategic Growth and Productivity Program in 2025."
   - Check: 3,059 + 919 + 65 + 13 + 9 = 4,065 (non-GAAP), which matches.
   - D08's Q3 2025 tables show no program charges for 2025. 2025 pretax total: **$13M**.
4. **Q1 2026 (D11):** Line 402 gives $171 in operating profit. Line 508 adds a $5 non-service postretirement charge. Line 548: "Strategic Growth and Productivity Program 176 37 139 1 138". Check: 892 + 176 = 1,068, which matches. Pretax: **$176M**.
5. **Q2 2026 and first half (D12):**
   - Line 461: "three and six months ended June 30, 2026 included charges resulting from the Strategic Growth and Productivity Program of $129 and $300."
   - Line 760: postretirement charge of (5).
   - Line 800, six-month income before taxes: "Strategic Growth and Productivity Program 305 61 244 2 242". Check: 1,842 + 305 = 2,147, which matches.
   - Q2 pretax (line 656) is 129. Check: 950 + 129 = 1,079, which matches; and 176 + 129 = 305.
6. **Calculation:**
   - Cumulative pretax charges recorded through June 30, 2026: 13 + 305 = **$318M**.
   - Amount not yet recorded: 450 − 318 = **$132M**.

minimal_documents: D09, D11, D12.
- D11 is the only source of the latest estimate.
- D12 is the only source of Q2 2026.
- D09 is the only source of the full 2025 amount. D10 is a 2025 segment recast that doesn't mention the program, and D08 only runs through Q3 2025.
- D07 and D08 only add support that the program started in Q3 2025 with no charges that quarter. D09 already ties the 2024 restructuring charges to the 2022 Global Productivity Initiative instead.
- As an alternative to D12's six-month row, D11's Q1 $176 plus D12's Q2 $129 gives the same $305.

readings:
- **Operating-profit charges only** (leaving out the $5M postretirement charge, which falls below operating profit): 13 + 300 = 313, leaving **$137M**. This is weaker because the question asks about *pretax* charges, and the pretax reconciliation includes the $5M.
- **Counting only 2026 charges** (ignoring the $13M from Q4 2025): 450 − 305 = **$145M**. This is weaker because the estimate is cumulative for the whole program.
- Using the superseded $200–$300M estimate gives 250 − 318 = −$68M. That doesn't fit "latest estimate."

gaps:
- No documents state a running cumulative total; I built it from the quarterly and annual reconciliations, and they agree with each other.
- I did not read D01–D06 in full. Searches of all 12 text files for the program name, "pre-tax/pretax", "cumulative", "million to $", "$350", "$550" and "substantially all" found nothing relevant in them. They date from 2019 and 2024 to April 2025, before the August 2025 announcement.
- The packet has no layout files or PDFs (the manifest lists method "text" with null pages for every document), so there were no original pages to inspect. The tables I relied on read clearly and their sums check out.

contaminated: no

Packet files used, under `D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q02-r0-v2-0a386408e69ce5c5b95809f9757546787522f25d89190885c679a48407c5a747\solver-1\text\`: D07.txt, D08.txt, D09.txt, D10.txt, D11.txt, D12.txt and manifest.json.
