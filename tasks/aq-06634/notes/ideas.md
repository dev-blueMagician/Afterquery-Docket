# aq-06634 - lean candidate sketches

Current target: hard (user, 2026-10-18: "there is no slot for Easy or Medium Tier for this bundle, we should
target high"; page: "Hard 0/5 · Medium closed · Easy 0/0", quick tests 0 of 20). Origin of every sketch:
claude. Measured platform success pending. Design: playbook section 4 (mine first, stack two or three levers).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: repurchases over the twelve months ended Aug 31, 2026 = 126.5 + 75.0 + 249.4 + 0 = $450.9M; March-May 2026 rebuilt from remaining authorization (D06 $925.0 -> D02 $675.6) | cash vs trade value equal (nil June-Aug 2026 cash repurchases); equity-plan withholdings are a separate line; D02 sole source after Feb 28; D06 or D04 places the Jan-Feb purchases in the new program | screen 3/3 (runs/i01-screen-155659c7335608d0; ledger row 48): ranked last, handed over 2026-10-18 |
| i02 | [sketches/i02.md](sketches/i02.md) | h1: largest fiscal-2026 quarter = March-May 2026, $249.4M (lure: June-Aug 2025 $160.1M, the largest printed) | fiscal quarters by the question's own year-end; no tie; D02 sole source after Feb 28; D06 or D04 for the program split | screen 3/3 (runs/i02-screen-e2dd112e124dd805; row 49): ranked last, handed over; shares h1 with i01, a set uses one |
| i03 | [sketches/i03.md](sketches/i03.md) | h2: total borrowings fell 4,954.1 - 4,556.1 = $398.0M in March-May 2026 (lures 400.0 principal; +2.0 long-term line only) | carrying basis pinned by "net of debt issuance costs"; short-term nil both dates; D05/D06 and D01/D02 interchangeable per date | screen 3/3 (runs/i03-screen-517cca374b8c678e; row 50): ranked last, handed over |

Rejected hooks h3-h10 and their reasons: [hooks.md](hooks.md).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
Allow one focused repair per distinct observed failure; a repeated failure means change the hook.
