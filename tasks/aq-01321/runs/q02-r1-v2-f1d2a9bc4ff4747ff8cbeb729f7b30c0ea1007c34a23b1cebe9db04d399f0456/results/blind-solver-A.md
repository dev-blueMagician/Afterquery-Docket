# q02 rev 1 blind solver A (fresh blind-solver agent, packet solver-1), 2026-10-06

tested_sha256: f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456
Prompt: workspace root, packet path solver-1, question verbatim. Return copied verbatim from the task notification.

---

**Answer: 20.26%.** Texas Instruments' R&D plus SG&A for the twelve months ended June 30, 2026 was $3,941M, against revenue of $19,453M.

answer: 20.26%
confidence: high
path:
1. **Window:** TI reports on a calendar year, so the twelve months ended June 30, 2026 are Q3'25 + Q4'25 + Q1'26 + Q2'26. The method is: full year 2025, minus Q1'25 and Q2'25, plus Q1'26 and Q2'26.
2. **D12, full year 2025 (income statement, lines 62–63):** "|Research and development (R&D)|521|491|2,083|1,959|" and "|Selling, general and administrative (SG&A)|446|446|1,860|1,794|". So FY2025 R&D was 2,083 and SG&A was 1,860.
3. **D10, Q1 (lines 62–63):** "|Research and development (R&D)|510|517|" and "|Selling, general and administrative (SG&A)|464|472|". Q1'26 was 510 / 464; Q1'25 was 517 / 472.
4. **D11, Q2 (lines 62–63):** "|Research and development (R&D)|535|527|" and "|Selling, general and administrative (SG&A)|490|485|". Q2'26 was 535 / 490; Q2'25 was 527 / 485.
5. **Trailing-12-month (TTM) R&D:** 2,083 − 517 − 527 + 510 + 535 = 2,084. This implies Q3'25 R&D of 518.
6. **TTM SG&A:** 1,860 − 472 − 485 + 464 + 490 = 1,857. This implies Q3'25 SG&A of 457.
7. **Combined:** 2,084 + 1,857 = $3,941M.
8. **Revenue:** D11's non-GAAP reconciliation, in the column "For 12 Months Ended June 30," 2026 (line 220), reads "|Revenue||$19,453|$16,675||". Cross-check: 17,682 (D12) − 4,069 − 4,448 + 4,825 + 5,463 = 19,453.
9. **Ratio:** 3,941 / 19,453 = 0.2025909, which is 20.259% and rounds to **20.26%**. Separately, R&D is 10.71% and SG&A is 9.55% of revenue.
10. **Corroboration:**
    - D11 line 17 says "Over the past 12 months we invested $3.9 billion in R&D and SG&A", which matches 3,941.
    - Every quarter's operating profit reconciles (gross profit − R&D − SG&A − other charges): Q1'25 1,324, Q2'25 1,563, Q4'25 1,473, Q1'26 1,808, Q2'26 2,310. So none of the comparative columns appear to have been restated.

minimal_documents: D10, D11 and D12 are all needed, and nothing can replace any of them.
- D12 is the only source for Q3'25 and Q4'25 R&D/SG&A (through the full-year figures).
- D10 is the only source for the Q1 figures.
- D11 gives Q2 and the TTM revenue.
- The packet has no Q3 2025 TI release. D01–D09 (Analog Devices, Microchip, onsemi) have no TI data.

readings:
- **Rounded headline:** "$3.9 billion" ÷ $19,453M gives 20.05%. This is less precise than the income-statement build-up, so it is a weaker reading at two decimals.
- **Broader expense set:** adding the other operating charges (derived Q3'25 restructuring of 85, Q4'25 of 32, and acquisition charges of 17 + 17) gives 4,092 / 19,453 = 21.04%. The question names only R&D and SG&A, so this doesn't fit.
- **Wrong window:** calendar 2025 would give 3,943 / 17,682 = 22.30%. That is not the requested period.

gaps:
- Q3'25 figures are derived by subtraction; no Q3 2025 release is in the packet. The derivation is internally consistent and matches the $3.9 billion headline.
- Coverage: I read D10, D11 and D12 in full. I did not read D01–D09 line by line. A search of all text files for "Texas Instruments|TXN|\bTI\b" matched only D10–D12.
- I checked the decisive rows against the docs/ source files and they match. The sources are .txt (no PDFs or layout files), so there were no extraction problems.

contaminated: no

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\solver-1\text\D10.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\solver-1\text\D11.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\solver-1\text\D12.txt
