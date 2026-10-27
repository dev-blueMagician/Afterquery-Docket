# Removal probe return: q03 rev 0 without Doc 4 (D01)

- Date: 2026-10-08 (local; returned after midnight UTC)
- tested_sha256: ffb33cc8c041179c676ea01d4095b23c33491b1bf997f644b8e2b45803711f78
- Packet: tasks/aq-02220/runs/q03-r0-alt-d5/solver-1 (Doc 1 -> D01, Doc 2 -> D02, Doc 3 -> D03; neutral headers)
- Role: blind-solver (fresh context, question only, plus the forced-guess instruction)

Raw return (verbatim):

answer: 31.2 TWh. This is the additional heat-network supply in 2050 under the preferred option (Option 3). The June 2022 Government Response says the government is now "minded to pursue" that option.
confidence: medium-low. The wording "heat networks … supply" could mean total supply, but 31.2 counts only the extra supply from zoning. Also, no document in the packet gives a post-2021 ("now") share for England.

path:
1. D02 (Consultation Stage IA, 27/09/21), ¶89, text/D02.txt line 1495: "The total heat demand for England … is estimated to be 439 TWh in 2050. Table 12 presents the proportion of total heat demand in England that could be delivered by the policy options."
2. D02 Table 12, lines 1497–1553: "Deployment under different policy options (in addition to existing heat networks and deployment through other heat network policies)". The rows are split across a page break. Rebuilt for 2025/2030/2035/2040/2045/2050:
   - Low: 0.1/1.1/2.1/3.1/4.1/5.1
   - Medium: 0.1/4.2/8.3/12.5/16.6/20.7
   - High (preferred): 0.1/6.3/12.5/18.8/25.0/31.2
   The steps are even, which matches the IA's linear-growth assumption (lines 953–955).
3. Other places that confirm 31.2:
   - D02 Table 25 (Annex 2), lines 2349–2360, High (preferred) option: "Deployment in 2050 (TWh/yr) 4.7 / 31.2 / 46.4" (lower/central/higher).
   - D02 ¶107, lines 1893–1894: "based on achieving 31 TWh/yr of additional deployment by 2050."
4. D01 (Oct 2021 consultation):
   - line 799: "Option 3 is our preferred option"
   - line 808: "reaching around 31 TWh in 2050 compared to around 21 TWh under option 2 and around 5 TWh under option 1"
   - line 155: "an additional 31 TWh … (around 7% of total UK heat demand)"
   These figures are rounded, so D01 cannot give one decimal place.
5. D03 (Government Response, June 2022), line 1570, which supplies the "now": "we confirm that we are minded to pursue the preferred option for the categories of buildings required to connect as set out in the consultation, subject to future consultation on how these buildings are defined." Line 1205 confirms that Option 3 is the one described in the consultation. The response does not change the scope (for example, communally heated blocks are not dropped), so the Medium figure of 20.7 does not apply. D03 contains no TWh or deployment figures.
6. Check: 31.2 / 439 = 7.1% of England's 2050 demand, which matches D01's "around 7%" (D01 calls it UK demand).

minimal_documents: D02 + D03. D02 gives 439 TWh and 31.2 to one decimal place; D03 gives the post-consultation decision.
- D01 cannot replace D02, because it only gives "around 31".
- D01 cannot replace D03, because it shows the option only as a proposal, before consultation. Without D03, D02 alone still gives 31.2 as the IA's "preferred (or more likely) option".

readings:
- Reading A: total heat-network share using the Climate Change Committee (CCC) estimate.
  - D02 line 412: "The CCC estimate that heat networks could provide 18% of UK heat demand by 2050."
  - D03 line 38: "could rise to 18% by 2050." D01 lines 23, 138 and 169 say the same.
  - 0.18 × 439 = 79.02, so **79.0 TWh**. This applies a UK-wide "could" figure to England's demand. The figure is the same in all three documents, so "now" adds nothing in this reading.
- Reading B: total supply, meaning existing networks plus networks funded by the Heat Networks Investment Project and Green Heat Network Fund plus zoning. This cannot be calculated. D02 ¶49–50 describes this baseline but never gives it in TWh. D02 ¶56 (line 1010) says 3% of heat in its no-policy comparison comes from heat networks, but that covers the modelled buildings, not all of England.
- Reading C: economic potential. D01 line 927: "76 TWh of heat being met by district heat networks in England, which is about 19% of all heat demand in England." This is a potential, not a 2050 expectation. 19% × 439 = 83.4.

gaps:
- No document in the packet gives an updated England-wide share or a revised deployment figure after 2021. If "now expected" points to such a later figure, this packet cannot answer the question.
- Table 12's rows are split by the text extraction, and any percentage column it had is not visible. I rebuilt the values and cross-checked them against Table 25 and D01.
- No PDFs or layout files were in text\, and the caller limited me to that folder, so I did not inspect the original pages.
- I searched all three files by keyword (TWh, 2050, heat demand, %, expect/anticipate/projected, deploy, Option 3, Government response, communal/residential, fifth/20%/18%/3%) and read the passages that came up. I did not read D01 or D03 end to end.

contaminated: no. The environment's git-status listing showed workspace filenames, but nothing about this question's answer, reasoning or sources.

forced_guess: 31.2 TWh
forced_probability: 0.45, source: documents
