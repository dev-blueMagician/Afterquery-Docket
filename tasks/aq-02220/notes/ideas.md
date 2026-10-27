# aq-02220 - lean candidate sketches

Current target: medium (user 2026-10-08, no Easy slot); hard where a design supports it. Measured platform
success pending. The page offers 10 free quick tests (0 used) and 8 difficulty runs; quick-test first.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md), q01 | h1 benchmark gas share of input, 40.0% (rev 2, one decimal) | heat share 15.0% fails "electricity and gas input"; boiler 84/86% fail "heat-network"; probe without Doc 4 gave 32.7% (misses); whole-percent rev 1 replaced because typical COP guesses round to 40% without Doc 2 | q01 rev 2 quick test "too easy" (user, 2026-10-08): dropped, hook h1 closed |
| i05 | [sketches/i05.md](sketches/i05.md), q02 | h2 CG-led stages in model C, £9,500,000 | probe without Doc 1 reached the gold unforced (inferred from Doc 3 L956-958 and the plural "stages") | q02 dropped 2026-10-08; hook h2 retired |
| i02 | below | h3 2035 share of target, 46.3% | Doc 4 only 2035 target; Table 12 only 2035 value (Doc 1 has 2050 only: 12.4 interpolated gives 45.9%) | quick test "too easy" (user, 2026-10-08): dropped, hook h3 closed |
| i03 | below, q03 | h4 2050 TWh at the now-expected share, 87.8 TWh | CCC 18% (Docs 1-3) is "could provide", UK-wide; only 2050 England demand is Doc 2's 439 | quick test survived (user, 2026-10-08); q03 rev 0 then reported "too easy" (2026-10-09, stage not stated); q03 rev 1 also quick-test "too easy" (2026-10-09): dropped, hook h4 retired |
| i06 | below | h5 waste-heat use vs economic potential, 42% | integer precision makes 31 and 31.2 agree; Doc 1 only source of 14 TWh; Doc 2 only source of the 19% mix | quick test "too easy" (2026-10-09): dropped, hook h5 closed |
| i07 | [sketches/i07.md](sketches/i07.md) | h8 rebuilt: respondents' top per-zone staffing x IA zones, 4,080 | 170 towns (1,360) fails "zones"; IA's own staffing not used; Doc 3 only 1-8 range, Doc 2 only zone count | quick test "too easy" (2026-10-09): dropped, hook h8 closed |

## i02 (quick-test sketch)

Question: What percentage of England's 2035 heat-network target would the impact assessment's preferred zoning
option's 2035 deployment equal, to one decimal place? (22 words; rev of an earlier "add that year", which could be
read as one year's increment)
Answer: 46.3%
Inputs: Doc 4 L18 "to 7% (27TWh) by 2035"; Doc 2 Table 12 High (preferred) 2035 = 12.5 TWh (pairs per year:
0.1/0.1, 4.2/6.3, 8.3/12.5, ...). 12.5 / 27 = 46.296%.
Ambiguity: medium option 8.3 (30.7%) fails "preferred"; 2050 31.2 fails "that year"; reading the Medium/High run
sequentially gives 16.6 (61.5%), a parse slip, not a second reading (Low row and Annex 2050 values fix the pairs).
Necessity: Doc 4 only 2035 target (27 TWh appears nowhere else). Doc 2 only 2035 deployment; without it, Doc 1's
"around 31 TWh in 2050" interpolated linearly gives 12.4 (45.9%).
Risk: plain two-lookup ratio; difficulty rests on reading the paired table.

## i03 (quick-test sketch)

Question: How many TWh of England's projected 2050 heat demand are heat networks now expected to supply, to one
decimal place? (18 words)
Answer: 87.8 TWh
Inputs: Doc 4 L18 "expected to provide a fifth of all heat by 2050"; Doc 2 L1495 "439 TWh in 2050". 0.2 x 439 = 87.8.
Ambiguity: CCC 18% (Doc 2 L412, Docs 1 and 3) is an older estimate of what networks "could provide" for UK heat:
79.0. Doc 4's 27 TWh = 7% implies 385.7 TWh in 2035 (77.1), not a 2050 projection. Doc 1's 486 TWh is current UK
building demand (97.2).
Necessity: Doc 4 only "fifth"; Doc 2 only 2050 England demand.
Risk: Doc 4's first paragraph matches "expected"; DESNZ's "20% by 2050" may be recalled.

## i06 (quick-test sketch)

Question: With the impact assessment's central generation mix, what share of the consultation's economic waste-heat
supply would its preferred option use in 2050, to the nearest percent? (25 words)
Answer: 42%
Inputs: Doc 2 L979 "19% of heat network heat demand could be met with waste heat sources" (Table 4: 9 + 4 + 6);
Table 12 High 2050 31.2 TWh (para 107 "31 TWh/yr"); Doc 1 L927 "waste heat supplying 14 TWh of a total 76 TWh".
31.2 x 19% = 5.928 TWh; / 14 = 42.3% (31 gives 42.1%; both 42%).
Ambiguity: alternative mix 36% (80%) fails "central"; medium option (28%) fails "preferred".
Necessity: Doc 1 only 14 TWh; Doc 2 only the mix share (without it, 14/76 as the share gives 41%).
Risk: Doc 1's "about 19% of all heat demand in England" could be misread as the waste share (gives 42%).

## Parked / rejected

See notes/hooks.md h6-h12. h6 (11 homes) and h7 (175%) are fair but plain lookups plus one step.

## Outcome (2026-10-09)

All seven designs closed: q01, i02, q03 (revs 0 and 1), i06, i07 quick-test or user-reported "too easy"; q02 dropped
when a removal probe reached its gold without Doc 1. No fair Medium design remains; see notes/hooks.md h1-h12.
