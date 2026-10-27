# q01 rev 7 - removal probes, run q01-r7-alt-s4 (renumbered packets, 19 documents each), 2026-10-08

Tested fingerprint: 8f3d3a8eca736a2bb0d563f616066c226ad2baa1e533d1bcb8d417772e272512 (question unchanged since rev 1).
Both: fresh blind-solver subagents; root, packet path and the verbatim question, plus the forced-guess request.
Packet check (caller): built with notes/helpers/build_probe.py; renumbered texts equal their originals after the
"# Dnn |" header and docs/ copies are byte-identical; the left-out source is absent from docs/ and the manifest.
Transcript audits (caller): solver-1 12 calls, solver-2 16 calls (Glob, Grep, Read, SubagentHandback);
every path inside its own packet; clean.

## solver-1: without Doc 1 / D02 (Bulgaria)

answer: Not answerable from this packet. It gives Poland's 2024 coal share of electricity generation (56.2%) but has no figure for Bulgaria's 2024 coal share.

confidence: high (that the packet cannot answer it)

path:
1. Locating documents. `text/manifest.json` lists 19 ITA Country Commercial Guide energy/cleantech text files (D01–D19): Angola, Chile, China, Finland, Germany, Indonesia, Israel, Mauritius, Mexico, Poland (D10), Portugal, Romania (D12), South Africa, South Korea, Spain, UAE, UK, Uruguay and Vietnam. There is no Bulgaria document. All are plain text (`"method": "text"`, `"pages": null`), so there were no PDF pages or layout files to check.
2. Poland. D10, line 13 (`text\D10.txt`; same text in `docs\ccg_energy_cleantech_sectors_poland.txt`, line 11): "In 2024, the share of coal in electricity generation was 56.2% (down from 70.7% in 2022 and 4.3 p.p. less than in 2023)."
   - Consistency check: wind 24.5 TWh is "14.5% share", so total generation is about 169.0 TWh. Gas 20.6 TWh is "(12.2%)", giving about 168.9 TWh. Coal "fell by 5.4 TWh (-5.4% y/y)", so coal was about 94.6 TWh, or about 56.0% of 169 TWh. That matches 56.2% within rounding.
   - Figures I excluded: 70.7% is the 2022 share. "at least 56 percent reliance on coal" (line 21) is a 2030 target. "Fossil fuels made up 70% of Poland's energy sources in 2024" (line 93) covers all fossil fuels and all energy, not coal's share of electricity.
3. Bulgaria. A case-insensitive search for "bulgar" across all of `text/` and `docs/` finds only two lines, both in D12 (Romania):
   - Line 23: "Romania exports and imports electricity to and from neighboring countries, including Hungary, Bulgaria, Serbia, Ukraine, and Moldova".
   - Line 40: "the Bulgaria-Romania-Hungary-Austria (BRUA) pipeline".
   Neither gives a Bulgarian coal or generation figure. I also searched for Bulgarian aliases and place names (Cyrillic "Бълг", Sofia, Maritsa/Marica, Kozloduy, Varna, Burgas, Plovdiv, Stara Zagora, the code "BG"); the only hit was a Romanian "Danube Delta" line. Searches for regional terms (Balkan, Southeast Europe, CEE, "member states", "coal-dependent") and for "share of coal", "coal's share", "coal share" and "lignite" turned up no data for Bulgaria or for other countries side by side.
4. Calculation: 56.2 − [Bulgaria 2024 coal share, missing] cannot be computed.

minimal_documents: D10 is enough for the Poland figure. No document in the packet supplies the Bulgaria figure. D12 is the only document that mentions Bulgaria, and it has nothing relevant.

readings: I found no other defensible reading that makes the question answerable. The Poland figure is stated directly and only once for 2024. Using 70% (fossil fuels, all energy), 70.7% (2022) or 56% (2030 target) would answer a different question.

Forced best guess (memory only, not from the packet): **28.2 percentage points**.
- Poland: 56.2%, from D10 line 13 (packet).
- Bulgaria: about 28.0%. This is my rough recollection of 2024 figures from sources like Ember, Eurostat or the Energy Institute: total generation of roughly 40 TWh, lignite/coal of roughly 11 TWh, and coal sliding from about 43% in 2022 to the mid/high-20s in 2023–2024. I can't cite a specific figure and may be partly reconstructing it. The plausible range is about 26–31%.
- Result: 56.2 − 28.0 = 28.2 pp, with a plausible range of about 25–30 pp.
- I put roughly a 5% chance on 28.2 being exactly right to one decimal, and about 40–50% on the true answer being within ±2 pp of it.

gaps:
- The packet has no figure for Bulgaria's 2024 coal share of electricity generation. Answering needs a Bulgaria source, most likely the matching ITA Bulgaria Country Commercial Guide energy section, which is not in this packet.
- Coverage: I read the manifest, D10 and D12 in full. For the other 17 documents I relied on searches (Bulgaria, its aliases, regional terms, coal and coal-share phrases) rather than reading every line. Some very long lines in those were hidden from the search display, but the search still matches whole lines, so the result that only D12 mentions Bulgaria is reliable.
- Per instructions, I did not read `question.txt`.

contaminated: no. The auto-attached git status listed file names from a different task (aq-00949) but contained no answer, reasoning or hint for this question.

Key files:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r7-alt-s4\solver-1\text\manifest.json
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r7-alt-s4\solver-1\text\D10.txt (line 13)
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r7-alt-s4\solver-1\text\D12.txt (lines 23, 40)

Caller verdict: misses unforced (not answerable); forced 28.2 (p about 0.05, Bulgaria from memory near 28.0%) is not
the gold 22.8.

## solver-2: without Doc 2 / D11 (Poland)

answer: Not answerable from this packet. No document gives Poland's coal share. Bulgaria's 2024 coal share can be worked out from D02 as about 33.4%.
Forced best guess: **23.6 percentage points**, with about a 15% chance of being correct. Poland's figure comes from my memory, not the packet.

confidence: high that the packet can't answer it. Medium on the Bulgaria figure. Low on the forced guess.

path:
1. Poland is missing. I searched all of text/ and docs/ for "Poland|Polish", for polan/polish/polsk/warsaw (ignoring case), and for \bPL\b / \bPOL\b. Nothing matched. The manifest lists 19 country guides (Angola through Vietnam) and none is Poland. I also searched regional terms (Visegrad, V4, CEE, Central/Eastern Europe, coal-dependent, "most coal", EU average). They found nothing about Poland.
2. Bulgaria facts, all from D02 (`D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r7-alt-s4\solver-2\text\D02.txt`). The matching lines in docs/ccg_energy_cleantech_sectors_bulgaria.txt are the same.
   - Line 10: "Bulgaria's electricity production decreased by 4.98% year-on-year, to some 37,963 GWh in 2024."
   - Line 11: "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024". I read the comma as a decimal point, so 28.46 TWh.
   - Line 13: "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria's total electricity generation, according to the International Atomic Energy Agency (IAEA)."
   - Calculation: coal plus nuclear share = 28.46 / 37.963 = 74.968%. Coal share = 74.968 − 41.6 = **33.37%**, or 33.4%. Check: coal = 28.46 − 0.416 × 37.963 = 12.667 TWh, and 12.667 / 37.963 = 33.37%.
   - These coal figures are for other periods, not calendar 2024:
     - Line 18: "From September 2024 to August 2025 … coal being dominant at 27.6%".
     - Lines 70 and 135: "dropped from 35 percent in 2020 to 27 percent in 2025".
3. Forced guess: Poland's 2024 coal share was about 57%. I remember this from Ember, Forum Energii and PSE reporting, not from the packet. 57.0 − 33.37 = 23.63, which rounds to 23.6. If Poland's figure was 57.1%, the result is 23.73, or 23.7. Rounding Bulgaria to 33.4 first gives the same answers.
   - Chance of exactly 23.6: about 15%. That combines roughly 60% that the Bulgaria figure is the 33.4 derivation with roughly 25–30% that Poland's figure rounds to 57.0.

minimal_documents: D02 covers the Bulgaria part only. No document in this packet, alone or combined, supplies Poland. D12 (Romania) mentions Bulgaria only for electricity trade, so it can't replace D02.

readings:
- If the Bulgaria figure is taken as the Sep 2024–Aug 2025 share of 27.6% (the wrong period), the answer is Poland − 27.6. With Poland at 57.0 that is 29.4; at 57.1 it is 29.5.
- If the 2025 figure of 27% is used: 57 − 27 = 30.0.
- Mixing periods by using the Sep 2024–Aug 2025 nuclear share of 40.38% (line 18) gives Bulgaria 74.97 − 40.38 = 34.6%, and an answer of about 22.4. I think this reading is weaker.
- Poland's true 2024 share could plausibly be anywhere from about 56.5% to 57.5%, so the guess ranges from about 23.1 to 24.1.

gaps:
- Poland's 2024 coal share is not in the packet. It seems a Poland document was left out or removed.
- The derived Bulgaria figure assumes the IAEA 41.6% uses the same total as the 37,963 GWh production figure.
- D02 line 44 refers to a monthly production chart that the text doesn't contain. No PDF is available, but the chart shows production, not coal share.
- I read D02 and D12 in full and D06 lines 1–55. I did not read the other 16 documents in full. I only searched them, using the Poland, Bulgaria, coal, lignite and regional terms above.
- I did not read question.txt in the packet.

contaminated: no. The workspace git-status context lists file names from another task (aq-00949) and memory files, but it contains no answer, reasoning or hint for this question.

Caller verdict: misses unforced (not answerable); forced 23.6 (p about 0.15, Poland from memory near 57.0%) is not the
gold 22.8.
