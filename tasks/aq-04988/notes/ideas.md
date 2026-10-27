# aq-04988 - lean candidate sketches

Current target: medium (user 2026-10-14: no Easy slot, "target medium and high"); measured platform success pending.
Runs on "Medium 0/1" sets started at the High level all day on 2026-10-14, so every sketch is audited against the high
solver (two solvers x 3 tries; ready only if both miss at least once and not every attempt is wrong).
Sources: caller (all ten texts read) plus two independent question-author agents (A, B), origin claude throughout.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | A-h1: Argentina's 2011-2015 salt fall (Doc 7) / review's mandatory-reformulation cut 0.58 g/day, a SODIUM figure (Doc 2) = 1.4 | 3.4 if 0.58 read as salt; one unpointed step, its sodium cue one sentence before and after; Doc 9 says no LMIC reduced intake by 2018 (premise contested); recall risk without Doc 2 (source review's 1.45 g salt) | quick test survived (user 2026-10-14, "both survived"); q01 checked rev 0, not run; strong-solver screen 3/3 right (ranked last, ledger row 16) |
| i02 | [i02](sketches/i02.md) | B-i01: largest % fall between two whole-country 24-h urine surveys = Turkey 16.7% (Doc 7); Argentina's 17.9% excluded by Doc 9 (regional surveys) | strong-solver default 17.9%; one half-pointed step (exclusion in another paper, no question word names Argentina); "One defensible answer" block risk if both form solvers stop at 17.9% | quick test survived; q02 checked rev 0: platform Run 1 "Too easy", High 3/6 (refunded); hook retired (ledger row 13) |
| i03 | [i03](sketches/i03.md) (was h2) | order Argentina, Mongolia, South Africa, Vietnam by latest measured intake (Doc 9 + Doc 7) | decisive Argentina 2015 value reached by a lookup of a named country | strong-solver screen 3/3 right (ranked last, ledger row 20) |
| A-i02 | author A | optimistic-scenario deaths (514 + 1,065) / 22,000 diet deaths 2019 = 7.2% | ratio of figures no document connects (2017-based model vs 2019 GBD); "additional" cue in the same sentence | not offered |
| i05 | [i05](sketches/i05.md) (was A-i03) | Durban crisps 100% (40/40) vs 2016 evaluation 67% = 33 pp | decoy is the discussion's swapped years; results give explicit counts first | strong-solver screen 3/3 right (ranked last, ledger row 19) |
| B-i02 | author B | national policies keeping salt shakers off tables = 4 | national status of Costa Rica/France/Uruguay policies inferred; small guessable integer | not offered |
| i04 | [i04](sketches/i04.md) (was B-i03) | HeartSAFE 17 vs HFP 12 major categories = 5 | fully pointed ("top-level" -> "major product categories") | strong-solver screen 3/3 right (ranked last, ledger row 18) |

Set check: i01 and i02 both read Doc 7's Table 1 (Argentina row), with different levers (units vs match-then-exclude)
and different answers; neither question gives the other's answer away. i02 treats Argentina's surveys as regional;
i01 asks only about the fall as reported, so they do not contradict each other.

Keep facts/checks in the linked sketches. A passed script screen verifies structure/input quotes only; it does not
prove gold/uniqueness or difficulty. One focused repair per distinct observed failure; a repeated failure means
change the hook.
