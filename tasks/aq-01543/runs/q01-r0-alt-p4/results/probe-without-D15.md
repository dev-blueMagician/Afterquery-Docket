# q01 rev 0 - removal probe without Doc 4 / D15 (South Korea), packet q01-r0-alt-p4/solver-2, 2026-10-07

Packet: 19 documents renumbered D01-D19 (probe-map.json); question verbatim. Fresh blind-solver.
Transcript audit (caller, parsed tool calls): all paths inside the probe packet; clean.
Caller verdict: unforced answer "cannot be determined" (miss), but the FORCED GUESS EQUALS THE GOLD (5.3, p 0.20),
reached by recalling South Korea's 2024 coal share as 28.1%. Recorded as guess-reaches: a stated recall risk for
the platform's Document check on Doc 4.

**Answer I would submit from this packet:** cannot be determined. None of the packet's documents gives South Korea's coal share. Bulgaria's 2024 share can only be worked out, at about 33.4%.

**Forced best guess:** 5.3 percentage points, with about a 20% chance of being correct. It rests on two things:
- **Bulgaria (from D02):** coal and nuclear together made 28.46 TWh out of 37.963 TWh, which is 74.97%. Taking away nuclear's 41.6% leaves coal at 33.37%.
- **South Korea (not in the packet):** I recall coal was about 28.1% of South Korea's 2024 generation, but this is unverified memory. 33.37 − 28.1 = 5.27, which rounds to 5.3. If the real figure is between 28% and 30%, the answer would be between about 3.4 and 5.3.

answer: not answerable (cannot be determined from this packet)
confidence: high (that the packet cannot answer it)

path:
1. text\manifest.json lists D01–D19. All are U.S. International Trade Administration country commercial guides for Angola, Bulgaria, Chile, China, Finland, Germany, Indonesia, Israel, Mauritius, Mexico, Poland, Portugal, Romania, South Africa, Spain, UAE, UK, Uruguay and Vietnam. There is no South Korea guide.
2. I searched all of text\ and docs\ for "Korea" (any case). The only hit is D11 (Poland) line 188: "Warsaw has chosen the South Korean company POSCO E&C for renovation and expansion of the existing waste-to-energy plant in Warsaw". This is not a coal share. Searches for other names (ROK, Seoul, KEPCO, KPX, KHNP, Doosan, Hanwha, Hyundai, Samsung, Busan) found nothing.
3. Bulgaria, calendar 2024, from D02. The same text appears in docs\ccg_energy_cleantech_sectors_bulgaria.txt.
   - Line 10: "Bulgaria's electricity production decreased by 4.98% year-on-year, to some 37,963 GWh in 2024."
   - Line 11: "Baseload power plants (coal, nuclear) generated a total of 28,46TWh of electricity in 2024". The comma is a decimal point, so this is 28.46 TWh.
   - Line 13: "In 2024, nuclear power accounted for approximately 41.6% of Bulgaria's total electricity generation, according to the International Atomic Energy Agency (IAEA)."
   - Calculation: 28.46 / 37.963 = 74.97%, and 74.97 − 41.6 = 33.37%, about 33.4%. Checked another way: coal = 28.46 − 0.416 × 37.963 = 12.67 TWh, and 12.67 / 37.963 = 33.4%.
   - D02 also gives coal shares for other periods, which I did not use:
     - Line 18: "From September 2024 to August 2025 … Fossil fuels account for about 32.73% … with coal being dominant at 27.6%".
     - Lines 70 and 135: coal "has dropped from 35 percent in 2020 to 27 percent in 2025".
   - D02 has no directly stated coal share for calendar 2024.
4. Result: Bulgaria's figure (about 33.4%, worked out) minus South Korea's (missing) cannot be computed.

minimal_documents: D02 is enough for the Bulgaria part. No document supplies South Korea. The conclusion that it is missing comes from searching all of D01–D19 in both text\ and docs\.

readings:
- Using Bulgaria's stated 27.6% (September 2024 to August 2025) or 27% (2025) as a stand-in still gives no answer, because South Korea is missing.
- Mixing periods, for example the 40.38% nuclear share from D02 line 18 (September 2024 to August 2025) with the calendar-2024 coal-plus-nuclear total, gives Bulgaria 34.6%. This is not defensible for calendar 2024.
- Reading "South Korea" as South Africa is not defensible. D14 line 10 says coal provides "approximately 80 percent of the nation's electricity", with no date. That would give about −46.6.

gaps:
- South Korea's 2024 coal share is not in the packet at all.
- Bulgaria's 2024 coal share is worked out, not stated. It combines national production figures with an IAEA nuclear share. If the two use different bases (for example gross versus net generation), the first decimal could change.
- D02 line 44 refers to a monthly production chart that is not in the text. It covers production, not coal share. The documents are plain text, so there was no PDF to check.
- D02 line 11's "3,3264 GWh" for renewables is garbled. I did not use it.
- Coverage: read in full D02; read in part D11 lines 180–194, D13 lines 1–45, D14 lines 1–14; searched only the other documents.

contaminated: no. The automatically attached git status listed file paths from an unrelated task (aq-00949) and contained nothing about this question's answer, reasoning or sources. No project instructions appeared in my context.
