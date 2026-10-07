# Sketch round 2: preliminary screen returns (aq-01430, 2026-10-06)

Sketch-stage evidence only, not final check records. Blind solves are fresh blind-solver agents
given the workspace root, a sketch-r1 packet path (byte copies of docs/ and text/, no question file,
bound to the read guard) and the sketch question verbatim. The c02 removal probe uses the q01
probe packet q01-r0-probe-k3 (byte copy without D06 = Doc 3, ids renumbered). Closed-book agents
received only the question. Returns copied verbatim from task notifications.

## Failed runs (API session limit, not misses)

The first c02 blind solve, the first c02 removal probe and the first d02 blind solve terminated
early: "Agent terminated early due to an API error: You've hit your session limit · resets 10:20pm
(America/Los_Angeles) (error type rate_limit, HTTP 429 ...)". Failed or cut-off execution is
missing evidence; all three were relaunched after the limit reset.

## c02 closed-book solve (closed-book-solver, question only), 110 s, 0 tool uses

Question: What share of the world's growth in electricity demand between 2000 and 2025 came from China? Give the percentage to one decimal place.

answer: 56.2% (about 56%)
confidence: low
basis: This is an estimate from memory. I don't have the source dataset (Ember, IEA or Energy Institute), so the decimal is uncertain. World electricity demand rose from about 15,500 TWh in 2000 to about 31,800–32,000 TWh in 2025, an increase of about 16,400 TWh. China's rose from about 1,350 TWh to about 10,400–10,600 TWh, an increase of about 9,100–9,250 TWh. That puts China's share at roughly 55.5–56.5%. I called no tools.
contaminated: Workspace metadata only, nothing related to the answer. The session automatically attached a git status snapshot (branch name plus memory and task file names, without their contents) and the user's account email.

Caller note: misses the gold (55.9%) at one decimal, but its stated band (55.5-56.5%) contains the
gold and it recalled China's 2000 demand as "about 1,350 TWh" (the D06 figure is 1,347): a
general-knowledge proximity risk, and a sign that D06's necessity may fail on recall.

## d02 closed-book solve (closed-book-solver, question only), 759 s, 0 tool uses

Question: Among the four largest power-sector CO2 emitters, counting the EU as one economy, which got a smaller share of their electricity from solar over the whole of 2025 than in January–June 2025? List them in any order.

answer: The EU and the United States

confidence: low

basis: This is reasoning from memory, not recalled figures. I don't remember the exact solar shares. Solar output peaks in spring and early summer, so January–June includes the best months. The EU had a very sunny spring in 2025. US demand is heavier in the second half because of summer cooling. Both should therefore show a lower full-year share. India's second-half capacity was about 19% higher and its demand was weaker, which should make up for monsoon losses. China is borderline: the huge solar build-out before June 2025 roughly cancels out its strong second-half demand. China could also belong on the list.

contaminated: no. The context contained only an automatically attached email and git status listing file names, with nothing related to this question.

Caller note: misses the gold (China, the United States, the European Union) by one item, and names
China as a possible member: seasonal reasoning alone gets close, so the closed-book reach risk is
real (a sibling run could add China).

## c02 blind solve, rerun (blind-solver, sketch-r1 solver-1 packet), 122 s, 24 tool uses

answer: 55.9%

confidence: high

path:
1. World demand in 2000 and 2025. D01 line 50: "Global electricity demand more than doubled over the last two decades, increasing from 15,279 TWh in 2000 to 31,774 TWh in 2025". World growth = 16,495 TWh.
2. China's demand in 2000. D06 line 960: "Electricity demand in China has increased sevenfold from 2000 (1,347 TWh) to 2024 (10,066 TWh)." No other document gives a 2000 figure for China.
3. China's demand in 2025. D07 line 553 (repeated L904): "reaching 10,573 TWh of electricity demand in 2025". The only 2025 total for China.
4. China's growth = 10,573 − 1,347 = 9,226 TWh.
5. Share = 9,226 / 16,495 = 0.55932, which rounds to **55.9%**.
6. Consistency checks: D07 L553 "a third of global electricity demand (33.3%)" (10,573 / 31,779 = 33.27%); "less than 10% at the beginning of the 21st century" (1,347 / 15,279 = 8.8%).
7. Other printed world figures (D07 L525 31,779; D06 L520-522 4,199 + 11,079 = 15,278) give 55.91-55.93%, all 55.9%.

minimal_documents: D06 and D07 (D06 gives China and world in 2000; D07 gives China and world in 2025); {D01, D06, D07} also works. D06 and D07 both required.

readings:
- Mixing the printed world figures gives 55.91-55.93%, all 55.9%.
- Using 2024 as the end year (D06 alone) gives 8,719 / 15,578 = 55.97%, which rounds to 56.0% (not what the question asks).
- The change in China's share of world demand (8.8% to 33.3%) answers a different question; rejected.

gaps:
- The 2000 and 2025 figures for China come from different editions; the editions report slightly different 2024 figures (D07 implies 2024 China about 10,070 vs D06 10,066; world 2024 30,930 vs 30,856). No document gives a revised 2000 figure for China.
- The rounding is fairly sensitive to that 2000 figure: with D01's world figures the answer stays 55.9% only if China's 2000 demand is between about 1,344 and 1,360 TWh.
- Coverage: D01 in full; relevant sections of D07, D06, D04, D05; searches across all eight files. Plain text, no PDFs.

contaminated: no.

Caller note: match (55.9%, high). The solver's own sensitivity band (1,344-1,360) overlaps the
public 2000 figure, which sharpens the D06 removal risk; the probe without D06 decides it.

## d02 blind solve, rerun (blind-solver, sketch-r1 solver-2 packet), 156 s, 15 tool uses

answer: China, the United States and the European Union

confidence: high. The US difference is only 0.1 percentage points, but it still holds at the precision the reports print.

path (condensed from the verbatim return):
1. Universe: D03 L144 ("The world's four largest polluters ... China 54% (198 TWh), the US 21% (76 TWh), India 3.3% (12 TWh) and the EU 2.4% (9 TWh)"), L51 ("the top four CO2-emitting economies"), L247; D07 confirms (China largest emitter L912; US 1,737 MtCO2e L970; India third-largest at 1,395 MtCO2e L1106; EU 587 MtCO2e L1042); Russia (544 MtCO2 in 2024, D06 L1180; fell 2.9 MtCO2e in 2025, D07 L1156) stays below the EU; Japan fifth (D07 L1210, L1224).
2. January–June 2025 shares (D03): China 11.5% (L269), US 8.7% (L295), India 9.2% (L323), EU 14% (L345).
3. Full-year 2025 shares (D07): China 11.1% (L1218, L1050), US 8.6% (L964, L1050), India 9.4% (L1098), EU 13.1% (L1050); each matches D07's own solar output and demand totals (EU 367/2,774 ≈ 13.2%, generation vs demand basis).
4. Comparison: China −0.4 pp (yes), US −0.1 pp (yes), EU about −0.9 pp (yes), India +0.2 pp (no, excluded). Rounding check: printed 8.6% < 8.65% ≤ printed 8.7%; EU 14% ≥ 13.5% > 13.1%.

minimal_documents: D03 and D07; no replacement (D08 has no country shares; D01 none; D02/D04/D05/D06 earlier years). D06/D07 corroborate the ranking.

readings:
- Rounding to whole percentages would drop the US (9% both periods): not defensible, the documents print one decimal.
- Ranking by 2024 or full-year 2025 emissions gives the same four.
- Countries only (ignoring "counting the EU as one economy") would bring in Russia, which has no first-half share: excluded by the question.

gaps: two halves from reports six months apart (US margin narrow); D03 L337 "The EU generated 8.8% (1,303 TWh) of global electricity" repeats the global solar figures and looks like a source error (recomputed EU first-half share about 14.7%, still above 13.1%); D07 never states Russia's 2025 emissions directly (about 540 estimated); D01, D03, D07, D08 read in full, others searched.

contaminated: no.

Caller note: match (China, US, EU), high confidence; the closed-book run came within one item
(EU and US, China "borderline"), so a closed-book reach is a live risk at the difficulty check.

## c02 removal probe without D06, rerun (blind-solver, q01-r0-probe-k3 packet, ids renumbered), 222 s, 36 tool uses

answer (verbatim opening): The packet doesn't give the exact answer because it has no figure for China's electricity demand in 2000. From the packet alone, China's share must be **above about 54.8% and at most 64.1%**. My best estimate is **55.9%**. I put the chance that this is exactly right at one decimal place at about **0.4**.

confidence: low for the 55.9% figure. High that the packet only supports the range above.

path (condensed): D01 L50 world 15,279 (2000) and 31,774 (2025), growth 16,495; probe-D06 (bundle D07) L553 China 10,573 in 2025 and "less than 10% at the beginning of the 21st century" (L904 also 5,802 in 2015); China's 2000 demand is in no remaining document; bounds 54.8% to 64.1%. The estimate uses memory, not the packet: China's 2000 demand about 1,347-1,356 TWh (NBS generation 1,355.6 minus about 8 TWh net exports; D05 L517 says Ember uses NBS data for China), giving 55.9% (holds for 2000 values of about 1,344.1-1,360.5 TWh).

readings: world 2025 31,779 also gives 55.9%; an 8.8% 2000 share gives 55.9%, 9% gives 55.8%, EIA-style 1,280 gives about 56.3%.

contaminated: no.

Caller note: REACHES the gold without D06 (forced 55.9%, p 0.4) by recalling the public 2000
figure. The platform's document check (high model, each marked document left out) would count D06
as not needed. c02 DROPPED.
