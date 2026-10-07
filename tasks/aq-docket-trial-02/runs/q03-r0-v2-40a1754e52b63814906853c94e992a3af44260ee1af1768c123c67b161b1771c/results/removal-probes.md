# q03 rev 0 - removal probes (2026-10-06)

Each probe is a fresh blind-solver agent given a prepared packet of this run, the verbatim question
and an instruction to treat one marked document as absent and answer "as you normally would" (best
answer plus probability). Approximates the platform's document check. Not an official blind solve.
tested_sha256: 40a1754e52b63814906853c94e992a3af44260ee1af1768c123c67b161b1771c. Gold: 37.04%.

## Without D10 (recast segment exhibit), shortcut packet

Return (verbatim):

**answer:** Not answerable exactly from the eleven remaining documents. My best estimate is about **21.5%**, within a range of roughly 20.75% to 22.3%. The chance that this figure, or any two-decimal guess, matches the exact answer is under 1%. The chance that the true value is within ±2 percentage points of it is about 40%.

**confidence:** high that it can't be answered exactly; low for the estimate.

**path:**
1. **Definition (D11, line 85):** "Russia and Belarus, which were previously reported within the Africa/Eurasia reportable operating segment, are now reported within the Asia Pacific reportable operating segment… Recast historical geographic segment information can be found on the Company's website." This structure took effect for the quarter ended March 31, 2026.
2. **No 2024 figures for Russia and Belarus anywhere.** Searching "Russia|Belarus" across all remaining text/ and docs/ files finds only that D11 footnote. The 2024 segment data in D05 (lines 457–478) and D09 (lines 460–481) uses the old structure only:
   - Asia Pacific: net sales $2,858, operating profit $812.
   - Africa/Eurasia: net sales $1,095, operating profit $253.
   
   D11 and D12 give recast figures only for 2026 and 2025.
3. **An exact answer needs 2024 recast Asia Pacific figures** (recast minus original Asia Pacific = Russia and Belarus). No remaining document contains them.
4. **Russia and Belarus can be derived for 2025** as recast Asia Pacific minus originally reported Asia Pacific ($ millions):

   | Period | Net sales | Operating profit | Margin |
   |---|---|---|---|
   | Q1 2025 (D11 vs D06) | 738 − 690 = 48 | 204 − 198 = 6 | 12.50% |
   | Q2 2025 (D12 vs D07) | 746 − 687 = 59 | 202 − 187 = 15 | 25.42% |
   | H1 2025 (D12 vs D07) | 1,484 − 1,378 = 106 | 407 − 385 = 22 | **20.75%** |

   - A cross-check through the new Europe, Middle East & Africa segment gives H1 net sales of 106 and operating profit of 21 (19.81%). The differences come from rounding.
   - Latin America, Hill's, Corporate and the Oral, Personal and Home Care totals are identical in the original and recast 2025 figures. So the recast changed only what the footnote describes.
5. **Adjusting to 2024:**
   - The Africa/Eurasia margin fell from 23.11% in FY2024 (253/1,095) to 21.76% in FY2025 (255/1,172), and from 23.68% to 21.55% between H1 2024 and H1 2025.
   - In H1 2025, the rest of Africa/Eurasia earned 100/460 = 21.74%, about 0.99 points above Russia and Belarus.
   - Keeping that gap in 2024 gives 23.11 − 0.813 × 0.99 ≈ **22.31%**. With no adjustment, the estimate is 20.75%. I took the midpoint, about 21.5%.
   - The probability is low because quarterly margins swung from 12.5% to 25.4%, and the rounding noise alone is about ±1 point.

**minimal_documents:**
- For an exact answer: recast 2024 segment data, which the remaining documents lack, plus D05 or D09 (they give the same original FY2024 figures).
- For the estimate: D11 (definition), D07 and D12 (H1 2025 derivation), and D05 or D09 (the 2024 adjustment). D06 is needed only for the Q1 breakdown.

**readings:**
- If "operations in Russia and Belarus" meant the segment that contained them in 2024 (Africa/Eurasia), the answer would be 253/1,095 = **23.11%**. I reject this because it covers much more than Russia and Belarus.
- If it meant the recast 2024 Asia Pacific segment, that also can't be computed without the recast 2024 data.
- Using a single 2025 quarter instead gives 12.50% (Q1) or 25.42% (Q2); both are weaker proxies.

**gaps:**
- D10 (text/D10.txt, docs/cl_ex991_2026-03-17.txt) was not read or searched, as the probe required. I make no claim about what it contains.
- D01 is an unrelated 2019 stock award agreement.
- D02–D04 and D08 were searched with grep only (Russia, Belarus, Eurasia, recast, realign, Middle East), not read in full. D09 was searched and its segment table checked.
- All figures are rounded to $ millions, so derived margins carry about ±1 point of noise.
- No extraction problems found; these are text sources, not PDFs.

**contaminated:** no

Result: gold 37.04% not reached (best about 21.5%). D10 needed.

## Without D11 (Q1 2026 release, the only document naming Russia and Belarus), solver-1 packet

Summary of the verbatim return (task notification 2026-10-06; key lines quoted):
"**Not answerable exactly without D11.** None of the 11 remaining documents mentions Russia or Belarus,
and none says which countries moved in the 2026 segment change. My best guess is **37.04%**, with
about a 35–40% chance that it is right."
path: zero hits for Russia/Belarus outside D11 (only "Ukraine" boilerplate); D12 l.83 says only that the
structure changed; FY2024 old (D05/D09) vs recast (D10): North America -397/+17, EMEA vs Europe +
Africa/Eurasia +181/-97, Asia Pacific +216/+80; the North America outflow most plausibly went whole to
EMEA (the July 2024 note puts skin health in North America), leaving the Asia Pacific gain as a block
from Europe/Africa-Eurasia; "Assumption, not verified (it presumably comes from D11): if that block is
exactly Russia and Belarus, the margin is 80 / 216 = 37.037% → 37.04%." Probability basis: 50-60% that
D11 names Russia and Belarus as the only move into Asia Pacific, about 85% that the gold uses these
figures. Readings: Africa/Eurasia 23.11% (about 2%), recast EMEA 20.12% (about 1%), 2025 26.79%, 2023
42.86%. contaminated: "no. The probe instruction names D11 as the document to exclude, which hints it
is the key source, but no answer or reasoning leaked."

Result: gold REACHED as the best guess at about 35-40% by inference from the question's naming of
Russia and Belarus plus the recast pattern. D11 is logically necessary (the only document naming
them) but the platform's document check may judge it replaceable; the probe itself notes the
instruction hinted D11 was the key source, so an unhinted platform attempt may infer this less often.
Mitigation: the reviewer note offered with the flag.
