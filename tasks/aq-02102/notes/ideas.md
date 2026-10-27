# aq-02102 - lean candidate sketches

Current target: medium (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target medium and
high. do your best."; page: Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10 quick tests); hard where a design
supports it. Measured platform success pending. Origin of all sketches: claude (Opus 5.5).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: individuals' share of all responses received, 2021-22 (Doc 2) vs 2023 (Doc 4); same-label Table 2 rows with different inclusion rules | Decoys 4.21 (both table totals), 4.28 (both "in total" sentences), 3.88/3.89 (one side wrong), all distinct at two decimals from 3.81. Doc 2 and Doc 4 each hold the only counts for their consultation. Vague-block risk: Doc 4's own column "Total Received" totals 107 | q01 rev 1-2 quick test "too easy" (user, 2026-10-08); dropped, family closed (untied wording reopens the 107 reading) |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: unions that accepted the 2016 compensation offer (Doc 5) and were engaged in 2023 without a written reply (Doc 4) | Universe of ten engaged unions enumerated; decoys Prospect/DPF (wrote), POA UK (refused; look-alike of PGA), ISU (not party), UNISON (not engaged). Doc 5 only source of 2016 stances; Doc 4 only source of 2023 engagement and respondents. Risks: PGA only an acronym; recall of 2016 stances | q02 quick test "Too easy — solver got it" (2026-10-08); dropped |
| h3-h5, h8 | [hooks.md](hooks.md) | promised vs actual response date; women's share gap; WPS/partnership arithmetic; consultation lengths | each is two plain lookups and one operation, the shape measured Easy or Too easy elsewhere | parked |
| h6, h7 | [hooks.md](hooks.md) | draft vs final rules; edition contradictions | h6 is a one-document answer (Doc 4 states the final rule whole); h7 has no single defensible answer | rejected |

q01 rev 0 ("share of all responses received") was replaced before hand-over: its full-corpus blind solve called Doc 4's
Table 2 "Total Received" 107 "the main alternative", the likely "too vague" pattern. Rev 1 states "including those
addressing no question"; its solve matched at high confidence. Remaining traps: 3.82 (Doc 2's 32 added twice), 4.21
(Doc 4's ten taken as already counted), 2.40 (Doc 4's 68 row), 3.89 (Audit Wales). Expect the stated condition to cost
some difficulty. Fallback for q02 if the PGA link is challenged: NTUC unions only (FDA, GMB, Unite).
