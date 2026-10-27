# q01 rev 0 - removal probe without Doc 1 / D02 (Bulgaria), packet q01-r0-alt-p4/solver-1, 2026-10-07

Packet: 19 documents renumbered D01-D19 (probe-map.json); question verbatim. Fresh blind-solver.
Transcript audit (caller, parsed tool calls): all paths inside the probe packet; clean.

**Answer I would submit:** Cannot be determined from this packet. South Korea's 2024 coal share is 28.1%, but no document gives Bulgaria's coal share of electricity generation for 2024 or any other year.

**Forced best guess:** about +0.2 percentage points. I put roughly a 5% chance on that exact one-decimal value, and only about 50–60% on the sign being right. The guess does not come from the packet. It rests on my uncertain memory that Bulgaria's coal (mostly lignite) share of generation in 2024 was about 27–30%, centred near 28.3%. That gives 28.3 − 28.1 = +0.2. Any value from about −2 to +2 is roughly as plausible.

answer: not answerable (Bulgaria's coal share is missing; South Korea = 28.1%)
confidence: high that the packet can't answer it; low on the forced guess

path:
1. South Korea, 2024 (D14, text\D14.txt line 9): "Korea's total electricity generation in 2024 reached 595.6 TWh … Coal and LNG each generated 167.2TWh, or 28.1%". The table on the same page (D14 lines 71–92, 2024 row) gives "167.2" in the coal column and "28.1%" in the matching coal ratio. Check: 167.2 / 595.6 = 0.28073, which is 28.07% and rounds to 28.1%. The text and the table agree.
2. Bulgaria: the string "Bulg" appears in only two places across all of text\ and docs\, both in D12 (Romania) and neither about coal:
   - D12 line 23: "Romania exports and imports electricity to and from neighboring countries, including Hungary, Bulgaria, Serbia, Ukraine, and Moldova"
   - D12 line 40: "the Bulgaria-Romania-Hungary-Austria (BRUA) pipeline"
   The manifest (text\manifest.json) lists 19 country guides: Angola, Chile, China, Finland, Germany, Indonesia, Israel, Mauritius, Mexico, Poland, Portugal, Romania, South Africa, South Korea, Spain, UAE, UK, Uruguay and Vietnam. There is no Bulgaria document.
3. I also searched for ways Bulgaria could appear without being named:
   - Bulgarian places and plants ("Kozloduy", "Maritsa", "Sofia") and the code "BG": no hits. The only "Balkan" hit is the Transbalkan pipeline in D12 line 40. The "CEE" hits are just letters inside other words such as "MCEE" and "succeed".
   - EU comparison phrases ("coal-dependent", "most coal", "member states", "neighbor", "second highest", "highest share", "EU countries", "European countries"): nothing gives a coal share for Bulgaria. D10 line 9 says only that "Poland remains one of the most coal-dependent countries in the EU". D04's "second highest" is about Finland's renewables share, after Sweden.
   - All 57 "coal" mentions across 16 files: none attributes a coal share to Bulgaria.
4. Calculation: Bulgaria (missing) − 28.1 cannot be computed.

minimal_documents: D14 is enough for the South Korea half. No document in the packet covers Bulgaria's figure, and D12 is not a substitute. A complete answer would need a Bulgaria source, presumably the missing Bulgaria country guide of the same kind (from the docs\ file naming, it would be "ccg_energy_cleantech_sectors_bulgaria").

readings:
- Using unrounded Korea (28.07%) instead of 28.1% would change the result by at most 0.1 point, once a Bulgaria value exists. It doesn't change the conclusion.
- Romania's figures (D12 line 52: "11.47% Coal" of installed capacity as of May 2025) are for another country, measure capacity rather than generation, and cover a different period. Using them as a stand-in would be wrong.
- I found no other defensible reading.

gaps:
- Bulgaria's 2024 coal share of generation is not in the packet.
- Read in full: D14, D12, D10, D05, and D04 lines 27–37 (from docs\).
- Covered only by targeted searches (full text\ and docs\ sweeps for Bulgaria terms, coal and comparison phrases): D01–D03, D06–D09, D11, D13 and D15–D19.
- All sources are plain text (method "text", no pages), so there are no PDF pages to inspect. D14 mentions a chart ("The chart below shows Korea's LNG import trends") that was lost in extraction, but it is about LNG and doesn't matter here.

contaminated: no. I received only the root, packet path and question. I did not read the packet's question.txt. The git status in the session context lists unrelated task files and shows no answer or hints for this question.
