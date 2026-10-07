# q02 rev 1 shortcut audit (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

tested_sha256: f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456
Prompt: workspace root, packet path shortcut, question verbatim. Return copied verbatim from the task notification.

---

**answer:** 20.26% (R&D plus SG&A of $3,941M divided by revenue of $19,453M, for the 12 months ended June 30, 2026)

**verdict:** clear

**shortest_path:**
1. **D11 (Q2 2026 release), non-GAAP reconciliation table, "For 12 Months Ended June 30" column:** "|Revenue||$19,453|$16,675||". The quarterly income statement gives Q2 2026 R&D of 535 and SG&A of 490. The same table gives the prior-year Q2 2025 figures: R&D 527 and SG&A 485.
2. **D10 (Q1 2026 release), income statement:** Q1 2026 R&D is 510 and SG&A is 464. The prior-year Q1 2025 figures are R&D 517 and SG&A 472.
3. **D12 (Q4 2025 release), "For Years Ended December 31" column:** FY2025 R&D is 2,083, SG&A is 1,860 and revenue is 17,682.
4. **Roll forward** using FY2025 minus Q1 2025 and Q2 2025, plus Q1 2026 and Q2 2026:
   - R&D: 2,083 − 517 − 527 + 510 + 535 = 2,084
   - SG&A: 1,860 − 472 − 485 + 464 + 490 = 1,857
   - Combined: 3,941
   - Revenue check: 17,682 − 4,069 − 4,448 + 4,825 + 5,463 = 19,453. This matches D11's stated trailing-12-month figure.
   - The implied Q3 2025 figures (R&D 518, SG&A 457, revenue 4,742) are consistent with D12's statement that Q4 revenue "decreased 7% sequentially."
5. **Ratio:** 3,941 / 19,453 = 0.202591, which rounds to **20.26%**. This is robust: the 20.255% boundary corresponds to 3,940.2 and the 20.265% boundary to 3,942.2.

**sufficient_documents:** All three of D10, D11 and D12 are needed, and no alternative set works.
- D10 is the only source of Q1 2026 and Q1 2025 R&D/SG&A.
- D12 is the only source of the second-half 2025 data (via FY2025 and Q4 2025).
- D11 is the only source of Q2 2026 and Q2 2025, plus the stated trailing-12-month revenue.
- No document gives six-month year-to-date or trailing-12-month R&D/SG&A as exact figures.

**searches:**
- I read the manifest and D10, D11 and D12 in full, and checked the key R&D, SG&A and revenue lines against the original docs/ files. They match.
- I searched all 12 text files for these terms:
  - "Texas Instruments|TXN|TI": found only in D10–D12.
  - "R&D and SG&A": only the rounded narrative "$3.9 billion" (D10–D12).
  - Answer-shaped values ("3,941", "3,94x", "20.26", "20.2x", "20.3%"): no TI matches. The only hits were other companies' margin figures.
  - "operating expenses as a percent": only Microchip and ADI ratios.
  - Trailing-period phrases ("trailing", "12/twelve months ended June 30", "19,453", "2,084", "1,857"): only cash-flow trailing-12-month tables and D11's revenue line.
- D01–D09 (Analog Devices, Microchip, onsemi) were checked only by these searches, which found nothing relevant to TI.
- I did not read question.txt, notes or any other packet. No contamination was found.

**readings/gaps:**
- **Main trap (not a shortcut):** D11's CEO quote says "Over the past 12 months we invested $3.9 billion in R&D and SG&A." That gives 3,900 / 19,453 = 20.05%. The figure is rounded to $0.1B, so it only bounds the ratio between about 19.79% and 20.31%. It can't support an answer to two decimal places.
- **Near-miss proxy:** using full-year 2025 R&D+SG&A (3,943) against trailing-12-month revenue gives 20.27%. That mixes periods, and it is off by one basis point.
- **Other wrong-period readings:** FY2025 on its own gives 3,943 / 17,682 = 22.30%. Q2 2026 on its own gives 1,025 / 5,463 = 18.76%.
- Adding acquisition or restructuring charges falls outside "R&D and SG&A."
- **Difficulty risk:** this is a routine three-document trailing-12-month roll-forward, and D11 supplies the denominator directly. That is ordinary cross-document arithmetic, not a whole-answer lookup.
- No extraction gaps.

Relevant files:
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\shortcut\text\D10.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\shortcut\text\D11.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\shortcut\text\D12.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\shortcut\text\manifest.json
