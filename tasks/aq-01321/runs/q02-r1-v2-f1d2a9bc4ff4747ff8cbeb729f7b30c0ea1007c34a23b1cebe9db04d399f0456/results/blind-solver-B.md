# q02 rev 1 blind solver B (fresh blind-solver agent, packet solver-2), 2026-10-06

tested_sha256: f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456
Prompt: workspace root, packet path solver-2, question verbatim. Return copied verbatim from the task notification.

---

answer: 20.26%

confidence: high

path:
1. **Revenue, twelve months ended June 30, 2026.** D11 (TI Q2 2026 release), non-GAAP reconciliation table headed "For 12 Months Ended June 30," shows "|Revenue||$19,453|$16,675||", i.e. $19,453 million for 2026. Rebuilding it from the quarters gives the same number: FY2025 $17,682 (D12) − Q1'25 $4,069 (D10) − Q2'25 $4,448 (D11) + Q1'26 $4,825 (D10) + Q2'26 $5,463 (D11) = $19,453 million.
2. **R&D and SG&A by period, from the income statements ($ millions):**
   - D12, FY2025: "|Research and development (R&D)|521|491|2,083|1,959|" and "|Selling, general and administrative (SG&A)|446|446|1,860|1,794|". So FY2025 R&D was 2,083 and SG&A was 1,860; Q4'25 R&D was 521 and SG&A 446.
   - D10, three months ended March 31: "|Research and development (R&D)|510|517|" and "|Selling, general and administrative (SG&A)|464|472|". Q1'26 is 510 / 464 and Q1'25 is 517 / 472.
   - D11, three months ended June 30: "|Research and development (R&D)|535|527|" and "|Selling, general and administrative (SG&A)|490|485|". Q2'26 is 535 /490 and Q2'25 is 527 / 485.
3. **Twelve-month totals** (FY2025 − H1 2025 + H1 2026):
   - R&D: 2,083 − 517 − 527 + 510 + 535 = 2,084
   - SG&A: 1,860 − 472 − 485 + 464 + 490 = 1,857
   - Combined: 3,941
   - Cross-check by quarter: Q3'25 R&D = 2,083 − 517 − 527 − 521 = 518 and Q3'25 SG&A = 1,860 − 472 − 485 − 446 = 457. Then 518 + 521 + 510 + 535 = 2,084 and 457 + 446 + 464 + 490 = 1,857.
4. **Agreement with TI's own statement.** D11 line 17 says "Over the past 12 months we invested $3.9 billion in R&D and SG&A". $3,941 million rounds to $3.9 billion.
5. **Internal consistency.** Every operating-profit line reconciles. For example, Q2'26: 5,463 − 2,111 − 535 − 490 − 17 = 2,310. FY2025: 17,682 − 7,599 − 2,083 − 1,860 − 117 = 6,023. Q1'25 and Q2'25 also reconcile with no other charges. Nothing indicates any figures were restated.
6. **Ratio.** 3,941 / 19,453 = 0.202591 → **20.26%**. Check: 19,453 × 0.2026 = 3,941.18, which is just above 3,941, and 19,453 × 0.20259 = 3,940.98, just below. The unrounded value is 20.259%, which rounds to 20.26%.
7. **Exclusions.** Acquisition charges (17 in each of Q1'26 and Q2'26) and restructuring charges/other (85 in Q3'25, derived, and 32 in Q4'25) are separate income-statement lines. They are not R&D or SG&A, so they are left out.

minimal_documents: D10, D11 and D12 are all needed for the exact figure. Only D10 has the Q1'26 and Q1'25 numbers, D11 has Q2'26, Q2'25 and the twelve-month revenue, and D12 has FY2025. The packet does not include TI's Q3 2025 release, so no other set works. D11 alone is enough only for the rounded version described below.

readings:
- **Rounded headline figure.** Using D11's "$3.9 billion in R&D and SG&A" with revenue of $19,453 million gives 3,900 / 19,453 = **20.05%**. This is less precise, because the $3.9 billion is rounded and a two-decimal answer needs the exact $3,941 million.
- **Including acquisition and restructuring charges.** Adding 34 + 117 to 3,941 gives 4,092 / 19,453 = 21.04%. This does not fit the question's wording ("R&D and SG&A"), so I reject it.
- **Wrong time window.** Using only Q2 2026 gives (535 + 490) / 5,463 = 18.76%. This is not the period asked about.

gaps: No Q3 2025 TI release is in the packet, so the Q3 2025 figures are derived by subtraction from the FY2025 totals. Every reconciliation check above passes. All documents are text-only (manifest "method": "text", no PDFs or layout files), so nothing was lost in extraction. I did not read D01–D09 (Analog Devices, Microchip and onsemi releases) in full. A search of those files for "Texas Instruments|TXN|TI" found no matches. The TI rows in text/ match the docs/ source files.

contaminated: no

Files used:
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\solver-2\text\D10.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\solver-2\text\D11.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\solver-2\text\D12.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r1-v2-f1d2a9bc4ff4747ff8cbeb729f7b30c0ea1007c34a23b1cebe9db04d399f0456\solver-2\text\manifest.json
