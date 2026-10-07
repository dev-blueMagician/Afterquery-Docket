# q01 rev 1 - removal probes (2026-10-06)

Each probe is a fresh blind-solver agent given a prepared packet of this run (same corpus bytes), the
verbatim question and an instruction to treat one marked document as absent and, if not answerable,
commit to a forced guess with its probability. It approximates the platform's document check (the
high model re-solving without each marked document). Not an official blind solve. tested_sha256:
3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7. Gold: +$69 million.

## Without D10 (recast segment exhibit), solver-1 packet

Return (verbatim):

**answer:** This can't be answered exactly from the eleven documents left without D10. My forced guess is **+41** million dollars (an increase). I put the chance that +41 is exactly right at about 4%, and the chance the true value is within ±8 of it at about 50%.

**confidence:** low

**path:**
1. D11 (Q1 2026 release), note (1) at line 85 defines what moved: "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business ... have been combined in a new Europe, Middle East &amp; Africa reportable operating segment ... Russia and Belarus ... are now reported within the Asia Pacific reportable operating segment." So the moved operations are Africa/Eurasia minus Russia and Belarus.
2. D09 Table 5, line 464 (checked against the docs/ original, line 462): "| Africa/Eurasia | 309 | 269 | 1,172 | 1,095 |". These are full-year 2025 and 2024. D05 line 461 confirms 2024 = 1,095. The whole segment changed by 1,172 − 1,095 = **+77**.
3. So the change asked for = 77 − (Russia/Belarus 2025 − Russia/Belarus 2024). A search for "Russia" and "Belarus" across the eleven documents finds only D11's note. No full-year Russia/Belarus figures, and no recast full-year 2024 or 2025 segment figures, are in them.
4. A partial figure can be worked out. Russia/Belarus sales = recast Asia Pacific − old Asia Pacific:
   - **Q1 2025:** D11 recast "Asia Pacific(1) | 804 | 738" minus D06 old "Asia Pacific | 690 | 727" gives 738 − 690 = 48.
   - **Q2 2025:** D12 recast "Asia Pacific(1) | 782 | 746 | 1,586 | 1,484" minus D07 old "Asia Pacific | 687 | 682 | 1,378 | 1,408" gives 746 − 687 = 59.
   - **First half 2025:** 1,484 − 1,378 = 106.
   - **Check:** Skin health = old North America − recast North America. For Q1 2025 that is 998 − 904 = 94, and Europe 690 + (271 − 48) + 94 = 1,007, which matches D11's recast Europe, Middle East &amp; Africa figure. For the first half it is 2,025 − 1,823 = 202, and 1,427 + (566 − 106) + 202 = 2,089, which matches D12.
   - So the moved operations had sales of 460 in the first half of 2025. The documents give no recast figures for any part of 2024 or for Q3–Q4 2025.
5. The forced guess:
   - Russia/Belarus full-year 2025 ≈ 106 + about 60 (Q3) + about 61 (Q4) ≈ 227. This assumes Q3 and Q4 stay near the Q2 level.
   - Russia/Belarus full-year 2024 ≈ 190–193. This relies on an assumption from outside the packet, based on memory: the ruble was on average about 11% stronger against the dollar in 2025 than in 2024 (by quarter roughly −1%, +12%, +10%, +24%). It also assumes local-currency growth near Africa/Eurasia's organic growth (D09: 6.5% for the year; quarterly 1.8%, 7.7%, 6.2%, 10.3% from D06–D09).
   - That gives a Russia/Belarus change of about +36, so 77 − 36 ≈ **+41**.
   - The documents themselves point the same way. Russia/Belarus rose from 48 to 59 between Q1 and Q2 2025 (+23%), while the rest of Africa/Eurasia rose only from 223 to 236 (+6%). Africa/Eurasia's currency effect also moved from −3.4% in Q1 2025 (D06) to +4.7% in Q4 2025 (D09).
   - Sensitivity: local growth of 0–15% moves the result to roughly +55 to +28.

**minimal_documents:**
- For the definition and the whole-segment change: D11 + D09 (D05 can replace D09 for the 2024 figure only).
- For the first-half 2025 Russia/Belarus figure: D07 + D12 (or D06 + D11 for Q1 alone).
- An exact answer almost certainly needs D10's recast full-year data, together with D09 and D11.

**readings:**
- (a) Treating the whole Africa/Eurasia segment as moved gives +77 from D09 alone. That ignores D11's Russia/Belarus carve-out, so it is less defensible.
- (b) A forced guess using only the documents assumes Russia/Belarus kept a constant share of Africa/Eurasia (106 / 566 = 18.7%). That gives 77 × 460 / 566 ≈ +63, with about a 2% chance of being exact. It conflicts with the faster Russia/Belarus growth visible in 2025.

**gaps:**
- Missing facts: Russia/Belarus net sales for full-year 2024 and full-year 2025, or equivalently recast full-year Asia Pacific, Europe/Middle East/Africa or North America figures. Recast Q3 and Q4 2025 figures are also missing.
- The exchange-rate inputs in the guess come from outside the packet.
- D10 was not read or searched, as instructed.
- Coverage: I read D01 (an unrelated 2019 stock-award agreement), D09, D11 and D12 in full. For D06 and D07 I read the segment tables. D02–D05 and D08 were only searched, for Russia, Belarus, Ukraine, Eurasia and Middle East, plus segment rows; their narrative text was not read in full.
- There are no layout files in this packet. I checked the D09 and D12 rows that the answer rests on against the originals in docs/.

**contaminated:** no

Result: gold +69 not reached (+41 forced, +63 alternative). D10 needed in practice.

## Without D09 (Q4/FY2025 release), shortcut packet

Return (verbatim):

I couldn't get an exact answer without D09. My forced best guess is **+$50 million** (2025 about $929M against $879M in 2024). The 2024 figure and January–September 2025 are exact; only October–December 2025 is estimated.

    answer: not answerable exactly without D09. Forced best guess: +50 ($ millions; FY2025 ≈ 929 vs FY2024 = 879). Probability exactly right ≈ 7%; ≈ 60% within ±5; ≈ 85% within ±10; sign positive > 97%.
    confidence: low (high for the 2024 base of 879 and for the positive sign)
    path:
    1. Which operations moved – D11 line 85: "The results of the Europe and Africa/Eurasia (excluding Russia and Belarus) reportable operating segments and the skin health business (previously within the North America reportable operating segment) have been combined in a new Europe, Middle East & Africa reportable operating segment… Russia and Belarus… are now reported within the Asia Pacific reportable operating segment." So the moved operations = Africa/Eurasia minus Russia & Belarus (RB).
    2. RB = recast Asia Pacific minus old Asia Pacific. Skin health = old North America minus recast North America.
    3. FY2024 (D05 lines 457–461, old segments: NA 4,113; Europe 2,770; APAC 2,858; Africa/Eurasia 1,095. D10 lines 56–59, recast: NA 3,716; EMEA 4,046; APAC 3,074):
       - RB = 3,074 − 2,858 = 216. Moved = 1,095 − 216 = **879**.
       - Cross-check: 4,046 − 2,770 − (4,113 − 3,716 = 397) = 879.
    4. Jan–Sep 2025 (D08 lines 419–423, old: NA 3,024; Europe 2,228; APAC 2,092; Africa/Eurasia 863. D10 lines 333–336, recast: NA 2,745; EMEA 3,204; APAC 2,259):
       - Moved = 863 − (2,259 − 2,092 = 167) = **696**. The EMEA route gives 3,204 − 2,228 − 279 = 697 (rounding).
       - By quarter, from D06 lines 359–363, D07 lines 434–438 and D10: Q1 223, Q2 236, Q3 236.
    5. Full-year 2025 recast totals (D10 lines 25–28): NA 3,679; EMEA 4,276; APAC 3,038. Subtracting Jan–Sep gives Q4 2025 recast: EMEA 1,072; APAC 779; NA 934. The Q4 2025 split on the old segments (Europe, Africa/Eurasia, old APAC, old NA) appears only in D09, so Q4 has to be estimated.
    6. Q4 2025 estimate, using document trends only:
       - Africa/Eurasia Q4 2025 ≈ 269 (Q4 2024, D05) × 1.068 (Q3 2025 year-on-year, D08) ≈ 287. Alternatively 297 × 0.976 (average Q4/Q3 ratio for 2023–24, D04 and D05) ≈ 290.
       - RB ≈ 61 (Q3 2025 level). Equivalently 779 minus an estimated old APAC of 713–722 gives 57–66.
       - Moved ≈ 229.
       - These trend estimates of the old segments add up to 18–35 less than the known recast Q4 total of 2,785. Assigning part of that gap to the moved operations puts Q4 at about 230–236, central about 233.
       - FY2025 ≈ 696 + 233 ≈ 929. Change ≈ 929 − 879 = **+50**.
    7. Sign: for the total to fall, Q4 2025 moved sales would have to be below 183. That is far under every observed quarter (223–236) and Q4 2024's implied level of about 217.

    minimal_documents: D11 (definition), D10 (recast FY2024, FY2025 and Jan–Sep 2025), D05 (old FY2024), D08 (old Jan–Sep 2025). D06+D07+D08 quarters can replace D08's nine-month column. D12 repeats only D10's Q2 and first-half 2025 recast figures, so it cannot replace D10. D12's recast note leaves out the Russia/Belarus detail, so it cannot replace D11. An exact answer needs D09 (old-segment FY2025 or Q4 2025), which is absent.

    readings:
    - Correct reading: Africa/Eurasia excluding Russia and Belarus, as above: about +50.
    - Treating the whole Africa/Eurasia segment as moved: 1,095 → about 863 + 290 ≈ 1,153, roughly +58 (also forced). This ignores the stated carve-out.
    - Change in the whole new EMEA segment: 4,276 − 4,046 = +230 (exact, D10). This also includes Europe and skin health, so it isn't the quantity asked.
    - Rounding: the exact gold could differ by ±1 depending on whether it is computed through Africa/Eurasia − RB or EMEA − Europe − skin health.

    gaps:
    - Q4 2025 old-segment net sales (only in D09). The Q4 estimate depends on trend and seasonality assumptions, and RB and skin health are small differences of large numbers.
    - No 2024 quarterly recast exists in the remaining documents, so a quarter-by-quarter year-on-year comparison isn't possible.
    - Not read in full: D01, D02, D03 (2019 and early-2024 releases on the older structure), and the remainder of D04, D06, D07, D12. All of them were covered by searches for Africa/Eurasia, Eurasia, Middle East/EMEA, Russia, Belarus and skin health.
    - D09 was never read or searched.

    contaminated: no

Result: gold +69 not reached (+50 forced; +69 outside its stated ±10 band). D09 needed in practice.
Caller note on the probe's rounding remark: for the full-year figures both routes give exactly 948
and 879 (Oral, Personal and Home Care totals equal in both structures); the ±1 difference it saw
belongs to the nine-month figures (696/697), which the gold does not use.

## Without D11 (Q1 2026 release, the only composition note), solver-2 packet

Return (verbatim):

**answer:** **+69** (an increase of about $69 million, from about $879M in 2024 to about $948M in 2025). This is a forced guess, because without D11 the exact answer can't be established. I put the chance it is right at about 50%. The basis is that it is the only clean split of the segment changes that also makes economic sense (path, step 5).

**confidence:** low

**path:**
1. D09 Table 5 (old basis), full-year 2025 / 2024 net sales:
   - "| North America | $ 1,021 | $ 1,036 | $ 4,045 | $ 4,113 |"
   - "| Europe | 734 | 668 | 2,962 | 2,770 |"
   - "| Asia Pacific | 722 | 724 | 2,814 | 2,858 |"
   - "| Africa/Eurasia | 309 | 269 | 1,172 | 1,095 |"
   - Latin America is 4,776 / 4,782. Oral, Personal and Home Care total is 15,769 / 15,618.
2. D10 "Segment Information (Recast)":
   - 2025: North America $3,679, Latin America 4,776, "Europe, Middle East & Africa | 4,276", Asia Pacific 3,038.
   - 2024: North America $3,716, Latin America 4,782, EMEA 4,046, Asia Pacific 3,074.
   - The totals are unchanged. D12 line 83 confirms the recast is "effective for the quarter ended March 31, 2026."
3. Net shifts from old to recast, 2025 / 2024:
   - North America lost 366 / 397.
   - Asia Pacific gained 224 / 216.
   - EMEA minus (Europe + Africa/Eurasia): 4,276 − 4,134 = +142 and 4,046 − 3,865 = +181.
   - Check: −366 + 224 + 142 = 0.
4. Context:
   - D04, D05 and D06 say that from July 2024, "The results of the skin health business previously reported within the Europe reportable operating segment are reported with the other skin health businesses in the North America reportable operating segment."
   - That Europe piece was small. Q1 2024 Europe was 711 before the recast (D02) and 673 after it (D06), a gap of 38. Q2 2024 was 720 (D03) against 685 (D07), a gap of 35. That is roughly $150M a year.
   - D10 gives U.S. sales for this business of "$3,596 in 2025" and "$3,640 in 2024". Recast North America is only $83M and $76M above those figures. That suggests some U.S.-sold business also left North America, most likely the whole skin health unit (about $397M in 2024).
5. Asia Pacific's gain (+216 / +224) is unlikely to have come from North America:
   - It is larger than the roughly $150M of non-U.S. skin health.
   - Operating profit points the same way. Asia Pacific's operating profit rose by 60 in 2025 (760 to 820) and 80 in 2024 (812 to 892). The operations leaving North America ran at about breakeven (−6 and −17: 784 to 790 and 839 to 856).
   - So the most consistent reading is that part of Africa/Eurasia went to Asia Pacific, and North America's moved operations went to EMEA.
6. Calculation:
   - Africa/Eurasia moved into EMEA, 2025: 1,172 − 224 = 948.
   - Same for 2024: 1,095 − 216 = 879.
   - Change: 948 − 879 = **+69**.
   - Cross-check via EMEA: 4,276 − 2,962 − 366 = 948, and 4,046 − 2,770 − 397 = 879.

**minimal_documents:** D09 and D10. D05 can stand in for D09's 2024 figures only. D02–D07 support the skin-health inference but are not needed for the arithmetic.

**readings:**
- If all of Africa/Eurasia moved into EMEA, the answer is 1,172 − 1,095 = **+77**. I'd put this at about 20%. It would mean North America sent $216–259M a year to Asia Pacific at high margins, which doesn't fit.
- A naive calculation of EMEA minus old Europe gives 1,314 − 1,276 = **+38**. That can't be right, because 1,314 is more than all of Africa/Eurasia (1,172).
- If part of skin health (for example Filorga's Asian sales) went to Asia Pacific, the answer would be 69 plus the change in that piece, probably a little below 69.

**gaps:** D11 was excluded, so no remaining document says which operations moved where. My split rests on inference from the numbers. D01 is an unrelated stock award agreement. I read D10 in full and the relevant parts of D02–D09 and D12, and searched D01–D10 and D12 for the key terms. I did not read the docs/ copies.

**contaminated:** no

Result: gold +69 REACHED as a forced guess at about 50% (alternative +77 at about 20%). D11 is
logically necessary (only statement of the composition and the only document naming Russia and
Belarus, the excluded item) but its removal does not reliably change a strong reader's answer.
Platform document-check risk for D11 if it is marked necessary: the platform counts a document as
needed "when it is the only document naming an item you marked it as excluding", and its flag text
invites a one-line reviewer note for exactly this case.
