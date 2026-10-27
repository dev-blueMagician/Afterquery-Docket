# Removal probe return: q03 rev 0 without Doc 2 (D02)

- Date: 2026-10-08 (local; returned after midnight UTC)
- tested_sha256: ffb33cc8c041179c676ea01d4095b23c33491b1bf997f644b8e2b45803711f78
- Packet: tasks/aq-02220/runs/q03-r0-alt-d5/solver-2 (Doc 1 -> D01, Doc 3 -> D02, Doc 4 -> D03; neutral headers)
- Role: blind-solver (fresh context, question only, plus the forced-guess instruction)

Raw return (verbatim):

answer: Not fully answerable from the packet. No document gives England's projected 2050 heat demand. The share heat networks are now expected to supply is clear: a fifth (20%), from D03. Converting it to TWh needs a demand total, and none of the three totals the packet implies fits all of "England", "projected" and "2050". The best-supported reading gives 80.0 TWh, but D01 does not say what year that England total refers to.
confidence: low

path:
1. Expected share now (D03, 2026 government response, line 18): "a target to more than double the amount of heat demand met via heat networks in England to 7% (27TWh) by 2035 with them expected to provide a fifth of all heat by 2050." So the 2050 share is 0.20.
2. Earlier expectation, which "now" replaces: D01 line 138 says "the Committee on Climate Change estimated in 2015 that with government support, they could provide 18% of heat demand by 2050". D02 line 38 repeats the 18% figure for the UK.
3. Possible demand totals for multiplying by 0.20:
   a. England, year not stated (D01 line 927): "The results show waste heat supplying 14 TWh of a total 76 TWh of heat being met by district heat networks in England, which is about 19% of all heat demand in England." 76 / 0.19 = 400.0 TWh, and 0.2 × 400 = **80.0 TWh**. The same paragraph calls the 486 TWh UK figure "current" but gives no year for the England figure.
   b. 2050 projection, but stated for the UK (D01 line 155): "enable an additional 31 TWh of deployment in the period to 2050 (around 7% of total UK heat demand)". Line 808 adds "reaching around 31 TWh in 2050". 31 / 0.07 = 442.857 TWh, and 0.2 × 442.857 = 88.571, which rounds to **88.6 TWh**.
   c. England, but for 2035 (D03 line 18): 27 / 0.07 = 385.714 TWh, and 0.2 × 385.714 = 77.143, which rounds to **77.1 TWh**.
4. Each total conflicts with the question in some way. (b) is explicitly UK. (c) is explicitly 2035. (a) is explicitly England and is only undated, not contradicted. That makes (a) the reading with the least conflict.
5. Arithmetic checked: 0.19 × 400 = 76; 0.07 × 442.857 = 31.0; 0.07 × 385.714 = 27.0. The "about 19%" and "around 7%" inputs are approximate, so one decimal place is more precise than the sources. For example, 18.5–19.5% gives 77.9–82.2 TWh.

minimal_documents: D03 + D01. D03 supplies the 2050 share and D01 supplies the demand total. D02 adds only the earlier CCC 18% UK figure and has no TWh numbers, so it cannot replace D01. Reading (c) needs D03 alone.

readings:
- 80.0 TWh: England total from D01 line 927, assuming it applies to 2050.
- 88.6 TWh: the 2050 total implied by D01's Impact Assessment, accepting that D01 calls it UK demand. The question's "projected 2050" wording fits this one well, and both D01 and D03 use a 7% figure, which could be a deliberate trap.
- 77.1 TWh: D03's 2035 total, assuming demand stays flat to 2050.
- Old-expectation figures, which are not the requested "now" figure: 18% × 400 = 72.0 and 18% × 442.9 = 79.7.

gaps:
- No document states England's 2050 heat-demand total, and D01 gives no year for the 76 TWh / 19% England analysis.
- D01 was read at lines 1–40, 130–324, 760–959, 1028–1077 and 1600–1729. D02 was read at lines 1–80 and 1203–1237. D03 was read in full.
- The rest of D01 and D02 was covered only by searches across all three files for: 2050, TWh/GWh/MWh/terawatt, "heat demand", projected/forecast, fifth/18%/19%/20%/7%, "impact assessment", and heat use/consumption/load synonyms. D02 has no TWh figures (its only energy units are 10 GWh, 100 MWh, 50 MWh and 30 kWh).
- I did not open the original PDFs or the docs folder, as the caller limited me to text\. The text folder has no layout files, and the manifest gives method "text" with pages null.

contaminated: no

Files: D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-02220\runs\q03-r0-alt-d5\solver-2\text\D01.txt, D02.txt, D03.txt, manifest.json

forced_guess: 80.0
forced_probability: 0.35, source: both
