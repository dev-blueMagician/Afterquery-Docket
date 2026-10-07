# q02 rev 0 blind solver A (fresh blind-solver agent, packet solver-1), 2026-10-06

tested_sha256: 0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b
Prompt: workspace root, packet path solver-1, question verbatim. Return copied verbatim from the task notification.

---

**answer:** 20.26%

**confidence:** high

**path:**
1. **TTM revenue.** D11 (TI Q2 2026 release), non-GAAP reconciliation table, lines 213–220: the column "For 12 Months Ended June 30, 2026" shows "|Revenue||$19,453|$16,675||". So revenue for the twelve months is $19,453M.
   - Cross-check from quarters: FY2025 $17,682 (D12 line 59) − Q1'25 $4,069 (D10 line 59) − Q2'25 $4,448 (D11 line 59) + Q1'26 $4,825 + Q2'26 $5,463 = 19,453. This matches the printed figure.
2. **Q2 2026 and Q2 2025 expenses.** D11, income statement for the three months ended June 30, lines 62–63: "|Research and development (R&D)|535|527|" and "|Selling, general and administrative (SG&A)|490|485|".
3. **Q1 2026 and Q1 2025 expenses.** D10, income statement for the three months ended March 31, lines 62–63: "|Research and development (R&D)|510|517|" and "|Selling, general and administrative (SG&A)|464|472|".
4. **Q4 2025 and full-year 2025 expenses.** D12, lines 62–63, columns are Q4'25, Q4'24, FY25, FY24: "|Research and development (R&D)|521|491|2,083|1,959|" and "|Selling, general and administrative (SG&A)|446|446|1,860|1,794|".
5. **Q3 2025 (no Q3 release in the packet), derived:**
   - R&D: 2,083 − 517 − 527 − 521 = 518
   - SG&A: 1,860 − 472 − 485 − 446 = 457
6. **Twelve months ended June 30, 2026 (Q3'25 + Q4'25 + Q1'26 + Q2'26):**
   - R&D: 518 + 521 + 510 + 535 = 2,084
   - SG&A: 457 + 446 + 464 + 490 = 1,857
   - Combined: 3,941
   - Check by a second route: FY25 − H1'25 + H1'26 = (2,083 − 1,044 + 1,045) + (1,860 − 957 + 954) = 2,084 + 1,857 = 3,941.
7. **Consistency check.** D11 line 17 says: "Over the past 12 months we invested $3.9 billion in R&D and SG&A". 3,941 rounds to $3.9B. Adding the acquisition charges (3,975) would round to $4.0B, which suggests TI's own figure is R&D plus SG&A only.
8. **Ratio.** 3,941 / 19,453 = 0.2025909, which is 20.26%.
   - Component check: R&D 10.71% + SG&A 9.55% = 20.26%.
   - Bracket check: 19,453 × 0.2025 = 3,939.23 and 19,453 × 0.2026 = 3,941.18, so the value falls between them and rounds to 20.26.
9. **Other checks.**
   - Q3 2025 restructuring charges/other are 117 − 32 = 85. Q1 2025 and Q2 2025 operating profit reconcile without any restructuring line (2,313 − 517 − 472 = 1,324; 2,575 − 527 − 485 = 1,563), so the derived Q3 figures are internally consistent.
   - The decisive rows in the docs/ originals (D10–D12 sources, lines 67–68 and the TTM revenue row) match the text/ extraction.

**minimal_documents:** D10, D11, D12. All three are needed:
- D10 has Q1'26 and Q1'25 R&D/SG&A.
- D11 has Q2'26 and Q2'25 figures plus the TTM revenue.
- D12 has the FY2025 and Q4'25 figures needed to derive Q3'25.

No replacements exist in the packet. D01–D09 cover Analog Devices, Microchip and onsemi and contain no TI data.

**readings:**
- **Rounded narrative figure:** $3.9B / $19,453M = **20.05%**. This is less precise than two decimals warrants, so I rejected it.
- **Including acquisition charges** ($17M in Q1'26 and $17M in Q2'26): 3,975 / 19,453 = **20.43%**. The question asks only for R&D and SG&A.
- **All operating expenses below gross profit** (adding restructuring 85 + 32 and acquisition charges 34): 4,092 / 19,453 = **21.04%**. This is not what was asked.

**gaps:**
- There is no TI Q3 2025 release in the packet, so Q3 2025 R&D and SG&A are derived by subtraction rather than printed. This assumes the prior-period comparatives in D10 and D11 were not restated. The internal reconciliations above support that.
- I did not fully read D01–D09. I searched them for "Texas Instruments|TXN|\bTI\b" and found no matches.
- The sources are plain text, with no PDFs or layout files, so there were no extraction problems.
- I did not read question.txt.

**contaminated:** no. The task gave only the workspace root, packet path and question, with no answer, reasoning or source hints. I can't confirm from inside the session how it was launched.

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\solver-1\text\D10.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\solver-1\text\D11.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\solver-1\text\D12.txt
