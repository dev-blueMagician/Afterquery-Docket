# q01 rev 1 - removal probes, run q01-r1-alt-w8 (renumbered packets, 19 documents each), 2026-10-07

Both: fresh blind-solver subagents; root, packet path and the verbatim question, plus a request for the
unforced answer and a forced best guess with probability. Transcript audits (caller): all paths inside each packet; clean.

## solver-1: without Doc 1 / D02 (Bulgaria)

**Answer I would submit:** cannot be determined from this packet. Poland's figure is in the packet: 56.2%. No document gives Bulgaria's 2024 coal share of electricity generation.

**Forced best guess:** 28.2 percentage points. I put about a 3% chance on it being correct to one decimal place. The Poland half comes from D10 (56.2%). The Bulgaria half is about 28% and comes from my memory only, not from any packet document. My recollection of Ember/Eurostat-style figures puts Bulgaria's 2024 coal share somewhere around 26–30%, so the difference could plausibly be anywhere from about 26 to 30 points.

answer: not answerable (cannot be determined from this packet)
confidence: high (that the packet cannot answer it); low (on the forced guess)

path (summary of the return): Poland D10 line 13 "In 2024, the share of coal in electricity generation was 56.2% (down from 70.7% in 2022 and 4.3 p.p. less than in 2023)"; rejected the 2030 "at least 56 percent" target and the 70% fossil share of energy sources. Bulgaria: searches for "bulgari", "Bulg", "BG", "BGR", "Sofia", "Kozloduy", "Maritsa" and "Balkan" across text\ and docs\ found Bulgaria only in D12 (Romania) lines 23 and 40 (trading partner; BRUA). 57 "coal" hits in 16 files: none gives Bulgaria's share. Calculation not computable.

minimal_documents: D10 is enough for Poland's 56.2%; no packet document supplies Bulgaria's value.
readings: none that make it answerable; Romania's "11.47% Coal" is installed capacity (May 2025), not a stand-in.
gaps: Bulgaria's 2024 coal share missing. Fully read D10 and D12; D05 lines 9–53; others searched only.
contaminated: no.

## solver-2: without Doc 2 / D11 (Poland)

**Answer I would submit:** This packet can't answer it. No document gives Poland's coal share of electricity generation, for 2024 or any other year. Only the Bulgaria half can be derived (about 33.4%, D02).

**Forced best guess:** 23.6 percentage points. I'd put about 15% on it being exactly right. The Poland part comes from my memory, not the packet: I recall reports (Ember / Forum Energii style) that coal made up about 57% of Poland's electricity generation in 2024. The Bulgaria part is the 33.37% derived from D02 below. 57.0 − 33.37 = 23.63, which rounds to 23.6. If Poland was 57.1%, the result is 23.7; if 56.7%, it is 23.3. If the gold used Bulgaria's 27.6% instead (a Sept 2024–Aug 2025 window), it would be 29.4.

answer: not answerable from this packet (Poland's 2024 coal share is missing; Bulgaria's 2024 coal share can be derived as about 33.4%)
confidence: high that it is not answerable from the packet

path (summary of the return): no Poland document; searched Poland, Polish, Polska, Polen, Pologne, Polonia, PL, Warsaw, Silesia, Belchatow, Turow, Katowice, Gdansk, Swinoujscie, Krakow, Wroclaw, Poznan, Lodz, Orlen, Tauron, Enea, Baltic Pipe, PLN, zloty: nothing. Bulgaria derived from D02 lines 10, 11, 13: 28.46 / 37.963 = 74.968%, minus 41.6% = 33.37%; rejected line 18 (27.6%, Sep 2024–Aug 2025) and lines 70/135 (2025).
minimal_documents: D02 for the Bulgaria half; nothing supplies Poland.
gaps: Poland missing; the baseload category could in principle include gas CHP; IAEA base may differ; D02 line 44 chart absent.
contaminated: no.

Caller verdicts: both probes miss unforced; neither forced guess equals the gold 22.8 (28.2 at p 0.03; 23.6 at p 0.15).
