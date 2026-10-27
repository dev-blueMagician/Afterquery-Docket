# q01 rev 8 - removal probes, run q01-r8-alt-j2 (renumbered packets, 19 documents each), 2026-10-08

Tested fingerprint: 29706b9980bc393ee5c2d1feddab7a5a62003bc3fafddf6145084ca043abc76a (question unchanged since rev 1).
Both: fresh blind-solver subagents; root, packet path and the verbatim question, plus the forced-guess request.
Packet check (caller): built with notes/helpers/build_probe.py; renumbered texts equal their originals after the
"# Dnn |" header and docs/ copies are byte-identical; the left-out source is absent from docs/ and the manifest.
Transcript audits (caller): solver-1 16 calls, solver-2 17 calls (Glob, Grep, Read, SubagentHandback);
every path inside its own packet; clean.

## solver-1: without Doc 1 / D02 (Bulgaria)

answer: This can't be determined from the packet. The packet gives Poland's 2024 coal share of electricity generation (56.2%), but no document gives Bulgaria's.
confidence: high (that the packet cannot answer it)

path:
1. Poland, from D10 (Poland Country Commercial Guide, Energy Sector). It is line 13 of text/D10.txt and line 11 of docs/ccg_energy_cleantech_sectors_poland.txt. Quote: "In 2024, the share of coal in electricity generation was 56.2% (down from 70.7% in 2022 and 4.3 p.p. less than in 2023)."
   - Consistency check: wind is "24.5 TWh (14.5% share)", which puts total generation at about 169 TWh. Coal "fell by 5.4 TWh (-5.4% y/y)", which puts 2024 coal at about 94.6 TWh. That gives about 56.0%, close to the printed 56.2%. I use the printed figure.
   - Two other D10 figures do not answer the question:
     - Line 21, "By 2030, Poland's energy mix is to decrease to at least 56 percent reliance on coal", is a target.
     - Line 93, "Fossil fuels made up 70% of Poland's energy sources in 2024", covers all fossil fuels and all energy, not coal in electricity.
2. Bulgaria. A case-insensitive search for "Bulgar" across all 19 documents (text/ and docs/) found only D12 (the Romania guide):
   - Line 23: "Romania exports and imports electricity to and from neighboring countries, including Hungary, Bulgaria, Serbia, Ukraine, and Moldova".
   - Line 40: "the Bulgaria-Romania-Hungary-Austria (BRUA) pipeline".
   Neither line gives a coal share. Searches for other Bulgarian terms (Kozloduy, Maritsa, Sofia, Varna, Burgas, Belene, BEH, NEK, BG, BGR) found nothing about Bulgaria; the only hits were parts of words like "behind". The packet has no Bulgaria guide. It covers Angola, Chile, China, Finland, Germany, Indonesia, Israel, Mauritius, Mexico, Poland, Portugal, Romania, South Africa, South Korea, Spain, UAE, UK, Uruguay and Vietnam.
3. So the calculation 56.2 − (Bulgaria's share) cannot be completed from the packet.

Forced best guess: about 28.2 percentage points.
- Poland, 56.2%: from D10, as above.
- Bulgaria, about 28%: from my own memory, not the packet, and not checked. My recollection is roughly 10.5–12 TWh of coal (mostly lignite) out of about 39–41 TWh total generation in 2024, which is about 26–30%.
- 56.2 − 28.0 = 28.2.
- Chance the guess is exactly right to one decimal place: about 5%. Chance the true answer is between 26 and 31 points: about 45–50%.
- If the intended Bulgaria source uses an older, rounded figure (around 35–40% coal), the answer would be about 16–21 points.

minimal_documents: D10 is enough for Poland. Nothing in the packet covers Bulgaria; an outside Bulgaria energy source would be needed. No other document gives Poland's coal share, so D10 has no substitute.

readings:
- Using Romania's "11.47% Coal" (D12 line 52) would give 56.2 − 11.47 ≈ 44.7. I reject this: it is the wrong country, it measures installed capacity rather than generation, and it is dated May 2025.
- Using Poland's share calculated from the TWh figures (about 55.8–56.0%) instead of the printed 56.2% would move any result by no more than 0.4 points. The printed figure is the direct statement, so I prefer it.

gaps:
- Bulgaria's 2024 coal share of electricity generation is missing from the packet.
- Read in full: D05, D10 and D12. The other 16 documents were covered only by searches: "Bulgar", Bulgarian place and company names, BG/BGR, every line mentioning "coal", and EU-comparison phrases ("coal-dependent", "member states", "in the EU", "EU average" and similar).
- The packet has no PDFs and no Dnn.layout.txt files. All documents are .txt with method "text", so there were no pages to check visually.
- I did not open the packet's question.txt.

contaminated: no. The auto-attached git status listed only file names from an unrelated task (aq-00949); no answer, reasoning or hint for this question leaked.

Relevant files:
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r8-alt-j2\solver-1\text\D10.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r8-alt-j2\solver-1\docs\ccg_energy_cleantech_sectors_poland.txt
- D:\Projects\Projects\AfterQuery-Docket\10.7\tasks\aq-01543\runs\q01-r8-alt-j2\solver-1\text\D12.txt

Caller verdict: misses unforced (not answerable); forced 28.2 (p about 0.05, Bulgaria from memory near 28.0%) is not
the gold 22.8.

## solver-2: without Doc 2 / D11 (Poland)

answer: Cannot be determined from this packet. No document gives Poland's coal share of electricity generation, or any Poland data at all. Bulgaria's 2024 coal share can only be worked out from other figures, and comes to about 33.4%.

Forced best guess: **about 23.7 percentage points**, with roughly 15% probability of being correct.
- Bulgaria part: 33.4% (33.37%), calculated from D02 (path below). This is the in-packet part.
- Poland part: about 57.1%. This is from my own memory (Ember / Forum Energii reported Poland's 2024 coal share at about 57%), **not from the packet**. If Poland is 57.0, the result is 23.6.
- If Bulgaria's Sept 2024–Aug 2025 figure of 27.6% were used instead, the result would be 29.5 (or 29.4 with Poland at 57.0).

confidence: high that the packet cannot answer it; low for the numeric guess.

path:
1. Poland is missing. text/manifest.json lists 19 country guides (D01–D19: Angola, Bulgaria, Chile, China, Finland, Germany, Indonesia, Israel, Mauritius, Mexico, Portugal, Romania, South Africa, South Korea, Spain, UAE, UK, Uruguay, Vietnam). None is for Poland.
   - Case-insensitive searches of text/ and docs/ found 0 matches for: Poland, Polish, Polska, "P o l a n d" spacing variants, Polen, Pologne, Warsaw, Silesia, Bełchatów, Turów, Opole, Kozienice, Katowice, Gdańsk, Orlen, Tauron, PGE, Enea, Visegrad, V4, Baltic Pipe.
   - None of the coal mentions in D03–D19 compares coal shares against an unnamed EU country.
2. Bulgaria (D02, text/D02.txt; checked against docs/ccg_energy_cleantech_sectors_bulgaria.txt):
   - L10: "Bulgaria's electricity production decreased by 4.98% year-on-year, to some 37,963 GWh in 2024."
   - L11: "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024" (decimal comma, so 28.46 TWh).
   - L13: "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria's total electricity generation, according to the International Atomic Energy Agency (IAEA)."
   - Calculation: 28,460 / 37,963 = 74.97% (coal plus nuclear). Coal = 74.97 − 41.6 = 33.37%, which rounds to **33.4%**. Cross-check: 0.416 × 37,963 = 15,792.6 GWh of nuclear; 28,460 − 15,792.6 = 12,667.4 GWh of coal; 12,667.4 / 37,963 = 33.37%.
3. Bulgaria figures that do not fit the 2024 window:
   - L18: "From September 2024 to August 2025 … coal being dominant at 27.6%". This is a trailing 12-month period, not calendar 2024.
   - L70 and L135: coal "dropped from 35 percent in 2020 to 27 percent in 2025". These are 2020 and 2025 values.
   - L94: nuclear generates "more than one-third". This is not precise enough to use.

minimal_documents: D02 covers Bulgaria only. No document in the packet covers Poland; a Poland source with 2024 generation-mix data would be needed. No alternative to D02 exists; no other document mentions Bulgaria's coal share.

readings:
- (a) Calendar-2024 Bulgaria share worked out as above (33.4%). This is my preferred reading. The final answer is still not determinable because Poland is missing.
- (b) Using the Sept 2024–Aug 2025 figure as a stand-in for 2024: Bulgaria 27.6%. Still not determinable.
- (c) Using "27 percent in 2025": Bulgaria 27%. Still not determinable.
- Rounding sensitivity in (a): "approximately 41.6%" could be anything from 41.55% to 41.65%. That gives a Bulgaria coal share of 33.32% to 33.42%, so the one-decimal value could be 33.3 rather than 33.4. The 28.46 TWh figure adds about ±0.013 pp.
- Caveat for (a): the calculation mixes the IAEA's nuclear share with a national production total, which may be measured on a different basis. It also assumes the "baseload" figure is only coal and nuclear, which is what the text says.

gaps:
- Poland's 2024 coal share is not in the packet. This is the deciding gap; the packet's preparation would need fixing if Poland was meant to be included.
- All sources are plain text ("method": "text", "pages": null). There are no PDFs or layout files, so there were no chart, row or footnote extraction issues to check.
- What I read: D02 in full, D06 lines 1–40, and the manifest. Targeted searches covered all of text/ and docs/ for Poland, its aliases, cities and companies, coal/lignite, and EU comparison phrases. I did not read the other 17 documents in full, but the Poland searches covered them. I did not open question.txt, as instructed.

contaminated: no

Caller verdict: misses unforced (not answerable); forced 23.7 (p about 0.15, Poland from memory near 57.1%) is not the
gold 22.8.
