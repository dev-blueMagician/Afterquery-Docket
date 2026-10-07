# q04 rev 2 - shortcut audit (raw, verbatim)

- Date: 2026-10-06. Fresh shortcut-auditor agent (claude-opus-5-5, scope hook), given only the
  workspace root, the shortcut packet path and the question. Copied verbatim from the task
  notification.
- tested_sha256: 0642033f48a4f31d6e03ff05ecf695cb3791cecd20aee2372d093ec7988fcba8

## Return

answer: 20.33%

verdict: clear

shortest_path:
1. The 2026 definition is set out in D11 line 85: the Q1 2026 structure took "the skin health business (previously within the North America reportable operating segment)" out of North America and put it into a new Europe, Middle East &amp; Africa segment. D12 lines 83 and 457 say the history was "recast ... to conform to the reporting structure effective for the quarter ended March 31, 2026."
2. D10 (the recast exhibit dated 2026-03-17) gives North America on the new basis for the year ended Dec 31, 2025: "$ 3,679 | $ 1,510 | $ 1,375 | $ 4 | $ 790" (line 25), so net sales were $3,679M and operating profit $790M. Its six months to June 2025 were $1,823M and $384M (line 245).
3. D12 Table 5 (lines 428 and 444) gives North America(1) for the six months ended June 30: 2026 net sales $1,779M against $1,823M for 2025, and operating profit $333M against $384M. The 2025 column repeats D10's recast figures.
4. Trailing twelve months = full year 2025 + first half 2026 − first half 2025:
   - Net sales: 3,679 + 1,779 − 1,823 = 3,635
   - Operating profit: 790 + 333 − 384 = 739
   - Margin: 739 / 3,635 = 20.330%, so **20.33%**
5. A quarterly cross-check gives the same totals:
   - Q3 2025 (D10 line 312): 922 / 199
   - Q4 2025 (full year minus nine months in D10): 3,679 − 2,745 = 934 and 790 − 583 = 207
   - Q1 2026 (D11 lines 369 and 385): 888 / 141
   - Q2 2026 (D12): 891 / 192
   - Sum: 3,635 / 739

sufficient_documents: D10 and D12 together are the smallest set that works. The alternative is D10 + D11 + D12, adding quarters. Neither D10 nor D12 is enough alone:
- D10 has no 2026 figures.
- D12 has no second-half or full-year 2025 figures on the new basis.

No other document gives the second half of 2025 on the new basis. The older releases (D08 and D09) only show North America with skin health still in it.

searches:
- Literal and concept terms: "twelve months", "trailing", "TTM", "LTM", "12 months", "rolling" (as a whole word), "annualized"; "recast", "reporting structure", "realign", "Africa/Eurasia"; and every "North America" row in all of D01–D12.
- Read in full: D10, D12 and the manifest. Read in part: D11 (lines 1–140 plus its segment tables) and D09 (lines 1–200 plus its segment tables).
- I checked the original files in docs/ for D10 and D12, and the North America figures match the text extraction.
- No document reports a trailing-twelve-month or year-to-June-2026 figure for North America. The only reported margins are single quarters: Q2 2026 at 21.6% (D12 line 102) and Q1 2026 at 15.8% (D11 line 104).
- D01–D08 were only searched, not read in full. They are dated before March 2026, so they cannot hold figures on the 2026 basis.

readings/gaps:
- **Wrong-definition trap:** using the old North America figures (with skin health) for Q3 and Q4 2025 from D08 and D09 (999/190 and 1,021/203), plus 2026 on the new basis, gives 726 / 3,799 = 19.11%.
- **Other mixed-basis routes:**
  - Old full year 2025 (4,045 / 784) with new six-month figures gives 733 / 4,001 = 18.32%.
  - Old full year with the old first half of 2025 from D07 (2,025 / 390) gives 727 / 3,799 = 19.14%.
- **Averaging the four quarterly margins** (21.58%, 22.16%, 15.88%, 21.55%) gives 20.29%. That is not the standard method; profit over sales for the whole period gives 20.33%.
- **Wrong period:** the full-year 2025 recast margin is 790 / 3,679 = 21.47%.
- **Difficulty risk, not a shortcut:**
  - The answer needs only two documents and a standard trailing-twelve-month subtraction. D12's 2025 comparative column duplicates D10's first half, so D11 is not needed.
  - D12's footnote ("Recast historical geographic segment information can be found on the Company's website") points straight to the D10 kind of source.
- **Rounding:** the source notes that tables "may not sum due to rounding". Both routes still land on 3,635 / 739.
- **Contamination:** none seen. No answer key, notes or prior outputs were available, and none were read.

Files used (all under `D:\Dev\Docket\tasks\aq-docket-trial-02\runs\q04-r2-v2-0642033f48a4f31d6e03ff05ecf695cb3791cecd20aee2372d093ec7988fcba8\shortcut\`):
- `text\D10.txt`
- `text\D12.txt`
- `text\D11.txt`
- `text\D09.txt`
- `text\D08.txt`
- `docs\cl_ex991_2026-03-17.txt`
- `docs\cl_ex991_2026-07-31.txt`
