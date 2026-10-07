# q02 rev 0 blind solver B (fresh blind-solver agent, packet solver-2), 2026-10-06

tested_sha256: 0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b
Prompt: workspace root, packet path solver-2, question verbatim. Return copied verbatim from the task notification.

---

answer: 20.26%

confidence: high

path:
1. **Revenue for the 12 months ended June 30, 2026.** D11 (TI Q2 2026 release), non-GAAP reconciliation, column "For 12 Months Ended June 30, 2026", line 220: "|Revenue||$19,453|$16,675||". So revenue is $19,453M. I checked it with D12, D10 and D11: FY2025 $17,682 (D12 line 59) − Q1'25 $4,069 (D10 line 59) − Q2'25 $4,448 (D11 line 59) + Q1'26 $4,825 + Q2'26 $5,463 = **19,453**, which matches.
2. **R&D for the same 12 months.** The packet has no TTM figure, so I built it from the income statements:
   - FY2025: D12 line 62, "|Research and development (R&D)|521|491|2,083|1,959|", giving 2,083.
   - Q1 2026 and Q1 2025: D10 line 62, "|Research and development (R&D)|510|517|".
   - Q2 2026 and Q2 2025: D11 line 62, "|Research and development (R&D)|535|527|".
   - TTM R&D = 2,083 − 517 − 527 + 510 + 535 = **2,084**.
3. **SG&A for the same 12 months.**
   - FY2025: D12 line 63, "|Selling, general and administrative (SG&A)|446|446|1,860|1,794|", giving 1,860.
   - Q1: D10 line 63, "|…(SG&A)|464|472|".
   - Q2: D11 line 63, "|…(SG&A)|490|485|".
   - TTM SG&A = 1,860 − 472 − 485 + 464 + 490 = **1,857**.
4. **Combined R&D + SG&A** = 2,084 + 1,857 = **$3,941M**. This agrees with D11 line 17: "Over the past 12 months we invested $3.9 billion in R&D and SG&A".
5. **Quarter check.** Q3 2025 is implied by subtraction: R&D 518 and SG&A 457.
   - Quarters summed: R&D 518 + 521 + 510 + 535 = 2,084; SG&A 457 + 446 + 464 + 490 = 1,857.
   - Q3'25 operating profit cross-checks: gross profit 2,723 − 518 − 457 − 85 restructuring = 1,663, and 6,023 − 1,324 − 1,563 − 1,473 = 1,663. Both agree.
6. **Ratio.** 3,941 / 19,453 = 0.2025909, which is 20.259% and rounds to **20.26%**.
   - Bounds: 19,453 × 0.2025 = 3,939.23 and 19,453 × 0.2026 = 3,941.18, so the ratio sits between them.
   - Sensitivity: $1M less in the numerator (3,940) would give 20.25%. I therefore re-read every input row in both text/ and the original docs/ sources (docs lines 64/67/68 and 233), and they are identical.

minimal_documents: D10, D11, D12. All three are needed for the exact TTM R&D and SG&A. D11 alone gives the TTM revenue directly, and the revenue can also be rebuilt from D10, D11 and D12. No replacement exists in the rest of the packet: D01–D09 cover Analog Devices, Microchip and onsemi, and a search found no "Texas Instruments", "TXN" or "TI" in them.

readings:
- **Management's rounded figure.** Using "$3.9 billion in R&D and SG&A" (D11 line 17) with revenue of $19,453M gives 3,900 / 19,453 = **20.05%**. That figure is only precise to $0.1B, so it can't support two decimal places. I treat it as inferior.
- **Including other operating charges.** Adding acquisition charges (17 + 17) and restructuring/other (Q3'25 85 + Q4'25 32) gives 4,092 / 19,453 = 21.04%. Those charges are not R&D or SG&A, so this reading doesn't fit the question.
- **Wrong period.** Calendar 2025, (2,083 + 1,860) / 17,682 = 22.30%, is not the period asked about. Listed only to rule it out.

gaps:
- The packet has no TI Q3 2025 release. Q3 2025 R&D and SG&A are derived from the FY2025 totals.
- The Q1 and Q2 2025 figures come from the comparative columns of the 2026 releases. No restatement note appears, so I assumed they are consistent with the FY2025 totals; the operating-profit checks support this.
- I read D01–D09 only by search, not in full; they do not concern TI.
- The packet has no PDFs or layout files (the manifest shows method "text", pages null), so there were no extraction problems.

contaminated: no

Files used:
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\solver-2\text\D10.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\solver-2\text\D11.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\solver-2\text\D12.txt
- The matching sources in the packet's docs\ directory.
