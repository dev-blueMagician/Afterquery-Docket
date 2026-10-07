# q01 rev 2, shortcut auditor (fresh shortcut-auditor agent, shortcut packet), 2026-10-06

Input: workspace root, packet path runs/q01-r2-v2-16db8ba5.../shortcut, question verbatim.
Return copied verbatim from the task notification.

answer: **$1.65 trillion.** Climate change/carbon funds held $3.45T and military/weapons funds held $1.8T, so 3.45 − 1.80 = 1.65.

verdict: clear

shortest_path:
1. Searching "SIF" and "trillion" leads to only two documents with US SIF ESG-issue figures, D07 and D12.
2. D12 (Americans for Financial Reform Education Fund letter, Apr 16, 2024), line 24: "According to US SIF Foundation, of the $8.4 trillion AUM in funds that consider ESG factors in their investment decision-making, $3.45 trillion address climate change/carbon and $1.23 trillion apply fossil fuel divestment policies." Footnote 4 (line 34) cites "US SIF Foundation, 2022 Report on US Sustainable Investing Trends Executive Summary, 4". This gives the climate-change-only figure, $3.45T. It does not give the ranking or any other issue's figure.
3. D07 (Sierra Club letter, Oct 19, 2023), line 45: "attention to climate change and fossil fuel divestment is by far the most significant of the ESG claims ... addressed in funds with a combined $4.8 trillion in AUM. The next largest ESG categories, military/weapons and tobacco, are addressed in funds with $1.8 trillion and $1.7 trillion in AUM, respectively." Lines 23–24 tie this to the 2022 report and the same $8.4T base. D07 only gives climate change combined with fossil fuel divestment.
4. Deciding the second-ranked issue: once climate change ($3.45T) is counted on its own, fossil fuel divestment alone is $1.23T (D12). That is below military/weapons ($1.8T) and tobacco ($1.7T). D07 says nothing else sits above military/weapons apart from the combined climate category. So military/weapons ranks second at $1.8T.
5. 3.45 − 1.80 = **1.65**.

sufficient_documents: D07 + D12 together; neither is sufficient alone, and I found no alternative pair. D12 lacks the ranking and the second issue's figure. D07 lacks a climate-only figure, and its $4.8T can't be split without D12. The figures in the original docs files match the text extraction (D07 source line 43, D12 source line 22).

searches:
- Literal: "SIF", "trillion", "climate change", "climate change/carbon", "fossil fuel divest", "weapon", "tobacco", "8.4 trillion", "Trends", "ussif".
- Synonyms and ranking terms: "Sustainable Investment Forum", "Forum for Sustainable", "military", "human rights", "board diversity", "conflict risk", "ranked", "next largest", "most significant", "top ESG", "fund assets", dollar-trillion/billion amounts.
- Read in full: D07, D12, D06.
- Targeted reads of matching lines: D01 (13, 66), D02 (30–57), D03 (1–16), D05 (1–24, 156–161), D08 (1–20), D10 (55–64, 345–356), D11 (1–20). The other "trillion" hits are ICI/MFA member assets and a Credit Suisse IRA estimate in D02, none relevant. D10 uses a USSIF member-fund list for ownership research, not 2022 issue figures. D06's match was "SIFMA".
- Checked docs/ originals for the key figures.

readings/gaps:
- **3.00** (D07 only): reading "climate change" as D07's combined climate change plus fossil fuel divestment, 4.8 − 1.8. This contradicts the question's "funds addressing climate change", which matches D12's "address climate change/carbon". The two-decimal request also fits 3.45. This is the most likely trap.
- **2.22** (D12 only): taking fossil fuel divestment as second, 3.45 − 1.23. D07 shows military/weapons and tobacco are both larger, so this is wrong.
- Minor inconsistency: D12's 3.45 + 1.23 = 4.68, but D07 says "combined $4.8 trillion". It doesn't change which issue ranks second or the answer.
- Precision: D07 gives military/weapons only to one decimal ($1.8T), so 1.65 assumes 1.80.
- Difficulty risk, not a shortcut: the route is a simple two-document lookup and subtraction. Searching "US SIF" turns up both inputs quickly.
- Coverage gaps: D04 and D09 had no hits for any key term and weren't read in full. D05 and D10 are long and were only keyword-searched plus spot-read. No extraction gaps were seen.

Relevant files:
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r2-v2-16db8ba51b534db6f52a1ac469d27996257318064e1b5aabd5dc954cfaa94744\shortcut\text\D07.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r2-v2-16db8ba51b534db6f52a1ac469d27996257318064e1b5aabd5dc954cfaa94744\shortcut\text\D12.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r2-v2-16db8ba51b534db6f52a1ac469d27996257318064e1b5aabd5dc954cfaa94744\shortcut\docs\sec_esg_disclosures_advisers_funds_s71722-276419-672002.txt
- D:\Dev\Docket\tasks\aq-01431\runs\q01-r2-v2-16db8ba51b534db6f52a1ac469d27996257318064e1b5aabd5dc954cfaa94744\shortcut\docs\sec_esg_disclosures_advisers_funds_s71722-458951-1174494.txt
