# aq-02408 - lean candidate sketches

Current target: medium (hard where supported); user 2026-10-09: "there is no slot for Easy Tier for
this bundle, we should target medium and high. do your best." Page: Hard 0/2 · Medium 0/3 · Easy 0/1,
9 submissions, 0 of 10 quick tests, 10 of 10 difficulty runs. Measured platform success pending.
Origin of all sketches: claude.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | notes/sketches/i01.md | h1: coal capacity of EPA's covered plants inside DOJ's relevant geographic markets (D04 + D05) = 650 MW | decoys 2,858 (all PJM plants), 1,706 (Welsh as Texas), 3,914; 0 fails "capacity at plants covered"; D04 and D05 each unique; recall risk Coleto Creek 650 MW public | screen pass (mechanical), overlap max 0.154; Easy-leaning (gold is one printed plant figure); candidate for a free quick test |
| i02 | notes/hooks.md h2 | FERC hourly labor cost 2026 minus 2024 = -$36.48 (D06 fn64 $63.52, D01 fn124 $100) | "$508.16/hr" cell label gives +408.16; but $63.52/hour is printed in five footnotes; FERC's $100/hour FY2024 rate may be recalled | parked: two plainly labelled lookups, measured too-easy shape |
| i03 | author B (independent question-author agent, no notes access), 2026-10-09 | h1 reversed: D04's covered coal plants decide which DOJ relevant market counts (ERCOT only); D05 gives Calpine-owned divested capacity there: 557 + 0.285 x 365 = 661.025 -> 660 MW (nearest 10) | decoys 5,040 (PJM divestitures added), 920 (whole Gregory), 560 (Fusco only); 28% complaint share also -> 660; gold printed nowhere | promoted to q01 rev 0; quick test "too easy" (user, 2026-10-09); dropped, h1 closed (i01 closed with it) |

| i04 | notes/sketches/i04.md | h2 reframed for sign: FERC's assumed hourly cost, 2024 NOPR $100 (D01 fn124) -> 2026 IBR order $63.52 (D06 fn64) = -$36.48 per hour | Doc 6 tables print per-response costs labelled "/hr" ($508.16 in 21 cells) -> +$408.16 sign flip; $63.52 only in five footnotes; $100/hour may be recalled | screen pass 2026-10-09; optional free quick test only, expected too easy |

Author B found no other fair Medium-capable design (rejected list in its return, summarised in hooks.md).

Removal probes on q01 rev 0 (runs/q01-r0-alt-k4, raw returns in results/): without Doc 5 "not answerable",
forced 5,390 at p 0.01 (misses); without Doc 4 "not answerable", forced the gold 660 at p 0.4 from the question's
"Calpine-owned" wording (partial ownership exists only at Gregory, ERCOT) plus remembered regional coal geography.
Any filter of DOJ's markets by "holds a covered coal plant" is open to that geography prior, so Doc 4 keeps the
"Exclusion / condition source" role with its reviewer note; i01's shape (Doc 4 supplies the 650 MW gold) carries
less Doc 4 risk but is a filter plus one printed figure.
i01 and i03/q01 share the h1 join: submit only one of them.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
Allow one focused repair per distinct observed failure; a repeated failure means change the hook.
