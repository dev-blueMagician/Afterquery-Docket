# q02 rev 0 shortcut audit (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

tested_sha256: 0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b
Prompt: workspace root, packet path shortcut, question verbatim. Return copied verbatim from the task notification.

---

answer: **20.26%.** For the twelve months ended June 30, 2026, TI's R&D was $2,084M and SG&A was $1,857M, for a combined $3,941M. Revenue was $19,453M. 3,941 / 19,453 = 20.259%, which rounds to 20.26%.

verdict: clear

shortest_path:
1. **D11** (TI Q2 2026 release, `text/D11.txt`):
   - Q2 2026: R&D 535, SG&A 490, revenue 5,463.
   - Q2 2025 comparatives: R&D 527, SG&A 485, revenue 4,448.
   - The non-GAAP table headed "For 12 Months Ended June 30" gives revenue of "$19,453" for 2026.
2. **D10** (TI Q1 2026 release):
   - Q1 2026: R&D 510, SG&A 464, revenue 4,825.
   - Q1 2025 comparatives: R&D 517, SG&A 472, revenue 4,069.
3. **D12** (TI Q4 2025 release), "For Years Ended December 31" 2025: R&D 2,083, SG&A 1,860, revenue 17,682.
4. Roll the twelve months forward (full-year 2025, minus Q1–Q2 2025, plus Q1–Q2 2026):
   - R&D: 2,083 − 517 − 527 + 510 + 535 = 2,084
   - SG&A: 1,860 − 472 − 485 + 464 + 490 = 1,857
   - Combined: 3,941
   - Revenue: 17,682 − 4,069 − 4,448 + 4,825 + 5,463 = 19,453. This matches D11's reported twelve-month revenue exactly.
5. 3,941 / 19,453 = 0.202591, or 20.26%.
6. Cross-check by quarter. Q3 2025 is derived as full year minus Q4, Q1 and Q2 2025: R&D 518, SG&A 457, revenue 4,742. Adding Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026 gives R&D 2,084, SG&A 1,857 and revenue 19,453, the same totals.

sufficient_documents:
- D10, D11 and D12 are all needed. No subset of them works:
  - Only D10 has the Q1 2026 and Q1 2025 figures.
  - Only D11 has the Q2 2026 and Q2 2025 figures.
  - Only D12 has full-year 2025.
- D11's reported twelve-month revenue ($19,453M) gives the denominator directly. That saves arithmetic but not a document, because the numerator still needs all three.
- No alternative documents exist. D01–D09 cover Analog Devices, Microchip and onsemi and never mention TI.

searches:
- I read D10, D11, D12 and the manifest in full.
- Terms searched across text/ and docs/:
  - "Texas Instruments", "TXN" and "TI": hits only in the three TI docs.
  - "R&D and SG&A", "3,941", "20.26", "20.05", "3.94", "20.3%": the only relevant hits are the three narrative "$3.9 billion" lines. The "20.3%" hits in D01, D05 and D07 are other companies' metrics.
  - "% of revenue", "percentage of revenue", "Q3 2025", "September 30", "operating expenses", "Trailing 12", "12 Months Ended June": only cash-flow and free-cash-flow ratios turn up, and there is no standalone Q3 2025 data.
- The text/ extractions of D10–D12 match the docs/ files line for line on every value used.
- A question.txt sits at the packet root. I did not open it. No notes or answer material leaked, so the run is not contaminated.

readings/gaps:
- **Narrative trap (a difficulty risk, not a shortcut).** D11 line 15 says: "Over the past 12 months we invested $3.9 billion in R&D and SG&A." Dividing by $19,453M gives 20.05%. That is wrong at two decimal places because $3.9B is rounded from $3,941M. D10 and D12 contain the same rounded $3.9B sentence for their own periods.
- **Wrong-period readings, for the reviewer:**

| Period | Combined R&D + SG&A | Revenue | Ratio |
|---|---|---|---|
| Calendar 2025 | 3,943 | 17,682 | 22.30% |
| Q2 2026 quarter only | 1,025 | 5,463 | 18.76% |
| Twelve months ended March 31, 2026 | 3,928 | 18,438 | 21.30% |

- **Scope.** Acquisition charges (17 in each of Q1 and Q2 2026) and restructuring charges are separate line items. They fall outside "R&D and SG&A" and are correctly excluded.
- **Difficulty risk.** The cross-document route is short: one twelve-month roll-forward plus a directly reported denominator. That is ordinary search-and-calculate work, not a shortcut.
- **Gaps.** I did not read D01–D09 in full. Searches show no TI content in them. There are no extraction gaps for the TI docs.

Files:
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\shortcut\docs\texas-instruments-incorporated-2q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-07-22.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\shortcut\docs\texas-instruments-incorporated-1q-2026-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-04-22.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\shortcut\docs\texas-instruments-incorporated-4q-2025-earnings-release-form-8-k-item-2-02-ex-99-1-filed-2026-01-27.txt
- D:\Dev\Docket\tasks\aq-01321\runs\q02-r0-v2-0e828aede328eedce5c851af6e3037167596f7a3dc3455f4db6129180297ce1b\shortcut\text\manifest.json
