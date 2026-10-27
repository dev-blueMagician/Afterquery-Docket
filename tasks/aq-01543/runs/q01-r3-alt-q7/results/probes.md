# q01 rev 3 - removal probes, run q01-r3-alt-q7 (renumbered packets, 19 documents each), 2026-10-07

Tested fingerprint: 50f506ffa773a20f026c1af48472b2d9ecdf23b879bd482205ccf3ed32c33219 (question unchanged since rev 1).
Both: fresh blind-solver subagents; root, packet path and the verbatim question, plus "First give the answer as you
would submit it from this packet (you may say it cannot be determined). Then give a forced best guess at the numeric
answer, with your probability that it is correct and where each part of the guess comes from."
Packet check (caller): every renumbered text equals its original after the rewritten "# Dnn |" header line; docs/
originals byte-identical; manifests list 19 entries without the left-out source; probe-map.json sits outside both packets.
Transcript audits (caller, notes/helpers/audit_transcript.py): solver-1 16 calls, solver-2 14 calls (Glob, Grep,
Read, SubagentHandback); every path inside its own packet; clean.

## solver-1: without Doc 1 / D02 (Bulgaria)

answer: Not answerable from this packet. Poland's 2024 coal share of electricity generation is given as 56.2%, but no document gives Bulgaria's coal share, so the difference can't be computed.

Forced best guess: **27.2 percentage points**, which is 56.2 (from the packet) minus about 29.0 (Bulgaria, from my own unchecked memory, not the packet). I'd put about 5% on it being exactly right to one decimal place, and about 55% on the true answer being within ±3 pp.

confidence: high that the packet can't answer this; low for the numeric guess.

path:
1. Poland, D10 (Poland Country Commercial Guide, Energy Sector, Power Generation), line 13: "In 2024, the share of coal in electricity generation was 56.2% (down from 70.7% in 2022 and 4.3 p.p. less than in 2023)."
   - File: D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r3-alt-q7\solver-1\text\D10.txt
2. Two other Poland figures in D10 don't fit the question, so I excluded them:
   - Line 21: "By 2030, Poland's energy mix is to decrease to at least 56 percent reliance on coal". This is a 2030 target.
   - Line 93: "Fossil fuels made up 70% of Poland's energy sources in 2024". This covers all fossil fuels and total energy, not coal's share of electricity.
3. Bulgaria. The manifest lists 19 country guides: Angola, Chile, China, Finland, Germany, Indonesia, Israel, Mauritius, Mexico, Poland, Portugal, Romania, South Africa, South Korea, Spain, UAE, UK, Uruguay and Vietnam. None is for Bulgaria.
   - File: D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r3-alt-q7\solver-1\text\manifest.json
   - Bulgaria appears only twice, both in D12 (the Romania guide), and neither gives a coal figure:
     - Line 23: "Romania exports and imports electricity to and from neighboring countries, including Hungary, Bulgaria, Serbia, Ukraine, and Moldova".
     - Line 40: "Bulgaria-Romania-Hungary-Austria (BRUA) pipeline".
   - File: D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r3-alt-q7\solver-1\text\D12.txt
4. Calculation: 56.2 minus Bulgaria's share, which is missing, so it can't be done.
5. Where the guess comes from:
   - Poland: 56.2 from D10 line 13.
   - Bulgaria: about 29.0%, from memory outside the packet. I recall 2024 generation of roughly 40–41 TWh, with Kozloduy nuclear near 40% and lignite (Maritsa East) at roughly 27–31%. I can't pin the exact source figure.
   - 56.2 − 29.0 = 27.2. A plausible range is about 25–29 pp.

minimal_documents: No packet document covers Bulgaria, so no set of documents is sufficient. D10 alone covers the Poland half, and no other document repeats its figure. D12 is the only document that mentions Bulgaria, and it doesn't help.

readings:
- "Percentage points" means a straight subtraction of the two shares, so there's no relative-percent reading.
- There is no other defensible reading. Using Romania's figure instead would be wrong on three counts:
  - It isn't Bulgaria.
  - "11.47% Coal" (D12 line 52) is installed capacity, not generation.
  - It is "as of May 2025", not 2024.
  - That substitution would give 56.2 − 11.47 ≈ 44.7, which I reject.

gaps:
- The missing fact is Bulgaria's 2024 coal share of electricity generation. The Bulgaria guide's energy section seems to be missing from the packet; if leaving it out wasn't intended, the caller should fix the packet.
- I read D10 and D12 in full and the manifest. For the other 17 documents I only ran searches across all of text/ (and docs/ for the Bulgaria names), using:
  - Bulgaria and related names: Bulgar, Sofia, Kozloduy, Maritsa, Balkan, Bobov, Varna, Burgas and the Cyrillic spelling.
  - Coal shares: patterns pairing coal with a percentage, plus "lignite".
  - Regional comparisons: coal-dependence wording, EU comparisons, Eastern/Southeast Europe, CEE, Visegrad.
  - Poland: it appears only in D10.
- The "CEE" hits in D14 are just the letters inside words like "exceed", not a regional comparison.
- There are no original PDFs in this packet (the manifest says "method": "text", "pages": null), so there were no page images to check.
- I did not open the packet's question.txt, as the rules require.

contaminated: no. The workspace git status attached to my session lists file names from other tasks (aq-00949) and memory files, but nothing about this question, its answer or its sources.

## solver-2: without Doc 2 / D11 (Poland)

answer: Not answerable from this packet. None of the 19 documents gives a coal share for Poland in 2024. Bulgaria's 2024 coal share can be worked out from D02: about 33.4%.

Forced best guess: about 23.6 percentage points. This comes from Poland at about 57.0%, taken from my memory and not from the packet (Ember / Forum Energii style reporting that coal fell to roughly 57% in 2024), minus Bulgaria's 33.4% derived from D02. Probability that 23.6 is exactly right: about 12–15%. The Poland half is unsupported, and a Poland source could print 56.6, 57.1 and so on.

confidence: high that the packet can't answer it; low for the forced guess.

path:
1. Poland is missing from the packet. The manifest (text/manifest.json) lists D01–D19, which cover Angola, Bulgaria, Chile, China, Finland, Germany, Indonesia, Israel, Mauritius, Mexico, Portugal, Romania, South Africa, South Korea, Spain, UAE, UK, Uruguay and Vietnam. There is no Poland guide.
   - Searching text/ and docs/ for `Poland|Polish|Polska|Warsaw|Silesia|Belchat|Tauron|Orlen|Visegrad` found nothing.
   - A search for every coal/lignite percentage in the packet found only figures for South Africa, Indonesia, Spain, Mexico, Vietnam, South Korea, Mauritius, the UK, Germany, Romania, Israel, Finland and Bulgaria. None of them is for Poland or compares with Poland.
2. Bulgaria's 2024 coal share is not stated directly. D02 (docs/ccg_energy_cleantech_sectors_bulgaria.txt, Energy section) gives three facts that make it possible to calculate it:
   - Total output, line 10: "Bulgaria's electricity production decreased by 4.98% year-on-year, to some 37,963 GWh in 2024."
   - Coal plus nuclear, line 11: "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024". I read the comma as a decimal point, so 28.46 TWh.
   - Nuclear share, line 13: "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria's total electricity generation, according to the International Atomic Energy Agency (IAEA)."
   - Calculation: 28.46 / 37.963 = 74.97%; 74.97 − 41.6 = 33.37%, which rounds to 33.4%.
   - Cross-check: nuclear is 0.416 × 37.963 = 15.79 TWh; coal is 28.46 − 15.79 = 12.67 TWh; 12.67 / 37.963 = 33.37%.
   - The docs/ copy prints the same numbers (37,963; Baseload; 41.6%; 27.6%).
3. Other Bulgaria coal figures in D02 cover different periods:
   - Line 18: "From September 2024 to August 2025 … coal being dominant at 27.6%". This is a rolling 12 months, not calendar 2024.
   - Lines 70 and 135: "dropped from 35 percent in 2020 to 27 percent in 2025" (35% in 2020, 27% in 2025).
4. Final step: Poland's 2024 share minus 33.4. This can't be done because Poland's share isn't in the packet.

minimal_documents: D02, for the Bulgaria half only. No document in the packet supplies the Poland half, and none of the other 18 can stand in for it.

readings:
- (a) Using calendar-2024 Bulgaria = 33.4% (derived): answer = Poland_2024 − 33.4. With Poland ≈ 57.0 (memory), that gives 23.6.
- (b) Using the Sept 2024–Aug 2025 Bulgaria figure of 27.6%: Poland − 27.6, which gives 29.4 if Poland is 57.0.
- (c) Using Bulgaria's 27% for 2025: 30.0 if Poland is 57.0. This uses the wrong year.
- (d) A small risk in (a): the IAEA nuclear share (41.6%) may rest on a different total than 37,963 GWh. That could move the derived Bulgaria figure by a few tenths. Within the packet, though, 33.4% is the only figure tied to calendar 2024.

gaps:
- Poland's 2024 coal share of electricity generation is missing entirely. The question seems to assume a Poland document that this packet doesn't have, so the caller should check that the packet was prepared correctly.
- What I read:
  - D02 and D12 in full; D06 lines 1–40.
  - Every other document only through searches across all of text/ and docs/ (Poland and its aliases; every coal/lignite percentage).
  - All sources are plain .txt (method "text", no PDFs or layout files), so there were no extraction problems.
  - The garbled "3,3264 GWh" renewables figure in D02 line 11 isn't needed.
- I did not open the packet's question.txt, as instructed.

contaminated: no. I received only the workspace root, the packet path and the question. The Poland ~57% in the forced guess is my own recall, flagged as outside the packet, and not leaked from the caller.

Relevant paths:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r3-alt-q7\solver-2\text\D02.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r3-alt-q7\solver-2\docs\ccg_energy_cleantech_sectors_bulgaria.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r3-alt-q7\solver-2\text\manifest.json
