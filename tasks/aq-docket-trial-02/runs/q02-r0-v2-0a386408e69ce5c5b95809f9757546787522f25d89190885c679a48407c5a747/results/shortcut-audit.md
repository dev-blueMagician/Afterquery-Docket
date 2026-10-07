# q02 rev 0 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, omitClaudeMd, scope hook), given
  only the workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 0a386408e69ce5c5b95809f9757546787522f25d89190885c679a48407c5a747

## Return

answer: $132 million. The midpoint of the latest estimate is $450M ((350 + 550) / 2). Cumulative pretax program charges recorded through June 30, 2026 are $318M ($13M in 2025 plus $305M in the first half of 2026). 450 − 318 = 132.

verdict: clear

shortest_path:
1. **Latest estimate:** D11 (Q1 2026 release, May 1, 2026), line 39: "cumulative pretax charges related to the SGPP, once all projects are approved and implemented, are now estimated to be $350 million to $550 million, increased from $200 million to $300 million." The midpoint is $450M. D12 (July 31, 2026) does not change this estimate. D07 line 41 has the original $200–$300M estimate, which this one replaced.
2. **2025 charges:** D09 (Q4 2025 release), line 495: full-year 2025 Corporate operating profit "included ... the Strategic Growth and Productivity Program of ... $13". The pretax reconciliation (Table 9 continued, line 865) reads "Restructuring programs(1) 13 2 11 — 11". Footnote at line 903 says the 2025 restructuring charges are this program. Q4 alone was also $13, so Q1–Q3 2025 had none. D08 (Q3 2025) agrees: it shows no charges for this program.
3. **First-half 2026 charges:** D12, Table 9 continued, line 800: "Strategic Growth and Productivity Program 305 61 244 2 242". The 305 is pretax, in the income-before-taxes column, for the six months ended June 30, 2026.
   - Cross-check by quarter: D11 Q1 pretax 176 (line 548) + D12 Q2 129 (line 656) = 305.
   - Cross-check by line item: operating-profit charges of 300 (2 + 13 + 285) plus 5 in non-service postretirement costs (line 760) = 305.
4. **Calculation:** 13 + 305 = 318 recorded, and 450 − 318 = **132**.

sufficient_documents:
- **Minimal set:** D09 + D11 + D12. Alternatively, D11's Q1 figure plus D12's Q2 figure can replace D12's six-month figure; the same three documents are still needed.
- **Why no smaller set works:**
  - D12 has neither the estimate nor the 2025 charges.
  - D11 has neither Q2 2026 nor 2025.
  - D09 has neither the expanded estimate nor any 2026 figures.
  - D10 (Mar 17, 2026) only recasts segments and has no program data.
  - D01–D06 come before the program.
- **Originals check:** the three key strings ($350–$550M, the 305 row, and "Restructuring programs(1) 13 2 11") match the docs/ originals of D11, D12 and D09.

searches:
- **Terms searched:** "Strategic Growth and Productivity", "cumulative pre-?tax charges", "$200/$300/$350/$550", "to date", "cumulative", "three-year", "productivity program", "once all", "restructuring", "program".
- **Read in full:** D12 and D10.
- **Read in part:**
  - D11: narrative and reconciliation tables.
  - D09: narrative and reconciliation tables.
  - D07: the announcement passage.
- **Grep only:** D08 shows only 2022 Global Productivity Initiative amounts in 2024 comparative columns. D01–D06 have no mention of this program.
- **Not found anywhere:** a reported program-to-date total, a stated remaining amount, or an estimate update after May 1, 2026.

readings/gaps:
- **Operating-profit basis gives 137:** 13 + 300 = 313, and 450 − 313 = 137. I rejected this because the question asks for pretax charges, and the pretax reconciliation also counts the $5M of non-service postretirement charges.
- **Leaving out the 2025 charge gives 145:** 450 − 305. This is wrong because "cumulative" means everything charged since the program started (announced Aug 1, 2025, first charges in Q4 2025).
- **Using the original estimate gives −68:** midpoint 250 − 318. That estimate had already been replaced.
- **Difficulty risk:** this is a simple three-document midpoint, sum and difference. The main traps are dropping the $13M and using operating-level rather than pretax amounts. Nothing qualifies as a shortcut.
- **Gaps:** D01–D06 were checked by grep only; none mention this program.
- **Contamination:** none. Listing the packet root showed a question.txt; I did not open it.

Files used (all under D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q02-r0-v2-0a386408e69ce5c5b95809f9757546787522f25d89190885c679a48407c5a747\shortcut\):
- text\D09.txt, text\D11.txt, text\D12.txt
- text\D07.txt, text\D08.txt, text\D10.txt, text\manifest.json
- docs\cl_ex991_2026-01-30.txt, docs\cl_ex991_2026-05-01.txt, docs\cl_ex991_2026-07-31.txt
