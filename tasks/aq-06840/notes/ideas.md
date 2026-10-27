# aq-06840 - lean candidate sketches

Current target: hard (user, 2026-10-18: no Easy or Medium slot for this bundle; page "Hard 0/5 · Medium closed").
Measured platform success pending. All sketches origin claude. Design: playbook section 4, from notes/mine.md and
the caller's same-period comparison (doc-map "Shared ground"); hooks in notes/hooks.md.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: FCF improvement Q4 2024 -> Q1 2025 on the Q3 2025 release's basis; FY2024 (D08) and Q1 2025 (D02) revised in later, unannotated releases; gold 711.8 | readings (a)-(e) rejected by the question's own FCF definition and D06's revised 2024 column; necessary D06, D08, D02; lures 717.8, 709.9, 702.8, 701.0 | screen 3/3 right (medium-high, medium, medium; ledger row 75): local 3/3, likely Too easy at High; ranked 1st of round 1; quick test survived (user, 2026-10-18) -> written up as [q01](../questions/q01.md); rev 1 Run 1 (2026-10-18): Answer not supported, High 0/6, every-document attempts 717.8 ("basis" read as the FCF definition): repaired as i06 |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: Q2 FCF 2026 vs 2025 on the Q2 2026 release's basis; Q1 2025 revised only in D02; gold 766.9 | necessary D04 (H1 2025 also D03), D02; lures 765.1, 766.7, 402.3 | screen 3/3 right (row 76); one solver: one-decimal rounding of the quarters gives 767.0 -> superseded by i05, not offered |
| i03 | [sketches/i03.md](sketches/i03.md) | h6: Q4 2024 FCF on the FY2025 release's basis; 9M 2024 revised only in D06; gold -347.2 | necessary D08, D06; lures -364.0, -355.1, -338.3 | screen 3/3 right, high (row 77): ranked 3rd; not quick-tested |
| i04 | [sketches/i04.md](sketches/i04.md) | h5: pre-tax write-downs plus sale loss, Ketjen refining catalysts; gold 521.7 | necessary D08, D02 or D04; lures 479.4 (net $52.7M), 426.7; different-family contrast, low expected difficulty | screen 3/3 right, high (row 78): ranked last; not quick-tested |
| i05 | [sketches/i05.md](sketches/i05.md) | h2 as i02, answer to the nearest million (rounding repair): gold 767 | necessary D04 (or D03 for H1 2025), D02; lures 765, 402; every rounding route gives 767 | screen 3/3 right (high, medium-high, high; row 79): ranked 2nd; quick test survived (user, 2026-10-18) -> written up as [q02](../questions/q02.md) rev 1, not run; same "basis" phrase: repaired as i07 before any run |
| i06 | [sketches/i06.md](sketches/i06.md) | h1 repaired (feedback index F1): "Using the most recently published figures" in place of the named release; gold 711.8 | single reading: latest printing of each input (D08, D06, D02); lures 717.8, 702.8, 709.9, 728.6 | screen 3/3 right, high (ledger row 102): local 3/3, likely Too easy at High; handed over for the user's quick test; result not reported (user, 2026-10-19, named only i07): q01 stays at rev 1 |
| i07 | [sketches/i07.md](sketches/i07.md) | h2 repaired (F2): same wording change; gold 767 | single reading; lure 765 (D01 Q1) | screen 3/3 right, high (row 103): local 3/3, likely Too easy at High; quick test survived (user, 2026-10-19: "i07 survived") -> written up word for word as [q02](../questions/q02.md) rev 2, difficulty run pending |

Round 1 result (2026-10-18): 15 of 15 solves right. Each hidden restatement was found whenever its figure was a needed
input: solvers compare cash-flow line items across editions (the FX-forward investing line marks the revised layout)
and check each release's own prose ("$128 million", "$594 million", "$201 million"). Reserve: h3 (TTM FCF to Sep 30,
2025, 112.2) and h4 (first negative-OCF quarter) rest on the same, already-caught revision. Dropped: h7 (necessity),
h8, h9 (lookups).

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
