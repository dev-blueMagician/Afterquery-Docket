# q01 rev 1, shortcut auditor (fresh shortcut-auditor agent, shortcut packet), 2026-10-06

Input: workspace root, packet path runs/q01-r1-v2-25b3d92f.../shortcut, question verbatim.
Return copied verbatim from the task notification.

**answer:** $1.65 trillion. Climate change/carbon was $3.45T and military/weapons was $1.8T, so 3.45 − 1.80 = 1.65.

**verdict:** clear. No single document gives the answer and none was contaminated. One difficulty risk: a single search for "US SIF" brings up both passages, and the arithmetic is one subtraction.

**shortest_path:**
1. I searched for "US SIF" and "trillion". That led to D07 line 45 (Sierra Club letter, Oct 19, 2023): "attention to climate change and fossil fuel divestment is by far the most significant of the ESG claims made by asset managers, addressed in funds with a **combined $4.8 trillion** in AUM. The next largest ESG categories, **military/weapons and tobacco**, are addressed in funds with **$1.8 trillion and $1.7 trillion** in AUM, respectively."
2. D12 line 24 (Americans for Financial Reform Education Fund letter, Apr 16, 2024): "According to US SIF Foundation, of the $8.4 trillion AUM … **$3.45 trillion address climate change/carbon** and **$1.23 trillion apply fossil fuel divestment policies**." Its footnote 4 cites the "US SIF Foundation, 2022 Report on US Sustainable Investing Trends Executive Summary, 4."
3. The two letters use the same dataset. Both give the $8.4T total, and D07 lines 23–24 say "In its 2022 report…", "at the beginning of 2022, $8.4 trillion."
4. Ranking the single issues: climate change/carbon 3.45 > military/weapons 1.8 > tobacco 1.7 > fossil fuel divestment 1.23. D07's "next largest" wording rules out any other category between 1.8 and the climate figure.
5. 3.45 − 1.80 = **1.65**.

**sufficient_documents:** D07 and D12, and both are needed. D07 has the second-largest issue and the ranking, but only a "combined" figure for the top one. D12 has the single-issue climate figure but no other issue categories. There are no alternative documents: no other file has US SIF issue-level figures.

**searches:**
- **Terms searched:** "US SIF|USSIF|SIF Foundation|Forum for Sustainable"; "trillion"; "billion"; "military|weapon|tobacco|firearm"; the specific values "3.45", "1.23", "4.8 trillion", "1.8 trillion", "1.7 trillion", "8.4 trillion", "climate change/carbon" and "fossil fuel divest"; and ranking or summary wording such as "most significant", "next largest", "second largest", "by far", "Sustainable Investing Trends", "ESG criteria", "ESG issues" and "ESG categor".
- **D07 and D12:** read in full.
- **D10:** its US SIF hits are about ESG fund ownership measured in basis points, which is irrelevant. Its "1.23" and "3.45" hits are fragments of regression statistics ("-11.230", "33.451").
- **Other "trillion" hits:**
  - D01, D03, D06 and D11 give the asset totals that ICI's members manage.
  - D05 and D08 give MFA members' assets.
  - D02's "$1.7 trillion" is Inflation Reduction Act financing.
- **Coverage:** all 12 text files were searched. I re-searched the docs/ originals and they show the same figures for D07 and D12.

**readings/gaps:**
- **3.00 (D07 only, 4.8 − 1.8):** this treats the "combined" climate-plus-fossil-fuel figure as one issue. I rejected it because the question asks for a "single" issue and D07 itself calls the figure "combined."
- **2.22 (D12 only, 3.45 − 1.23):** this assumes fossil fuel divestment is second. I rejected it because D07 shows military/weapons ($1.8T) and tobacco ($1.7T) are both larger.
- **Internal inconsistency:** 3.45 + 1.23 = 4.68, not D07's "$4.8 trillion." That could come from overlap between categories or from rounding, but it doesn't change the ranking.
- **Precision risk:** military/weapons is only given to one decimal place ($1.8T). The two decimal places in 1.65 are formatting, not true precision. Within this packet, 1.65 is the only supported value. If the underlying US SIF figure is anywhere from 1.75 to 1.85, the true gap would fall between 1.60 and 1.70. I did not use any outside material.
- **Extraction gaps:** none. Every manifest entry is a plain .txt file (extraction method "text"), and the docs/ originals match.

Files:
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r1-v2-25b3d92f987b21435753a4f65759635194d2786b2541c213f57d0f886a706b6d\shortcut\text\D07.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r1-v2-25b3d92f987b21435753a4f65759635194d2786b2541c213f57d0f886a706b6d\shortcut\text\D12.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r1-v2-25b3d92f987b21435753a4f65759635194d2786b2541c213f57d0f886a706b6d\shortcut\docs\sec_esg_disclosures_advisers_funds_s71722-276419-672002.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r1-v2-25b3d92f987b21435753a4f65759635194d2786b2541c213f57d0f886a706b6d\shortcut\docs\sec_esg_disclosures_advisers_funds_s71722-458951-1174494.txt
