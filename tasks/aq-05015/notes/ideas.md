# aq-05015 - lean candidate sketches

Current target: hard (only Hard open on the page; user named no Easy slot). Measured platform
success pending. From 2026-10-14 (CLAUDE.md, playbook) every Hard sketch passes the strong-solver
screen before it is offered; every fair sketch goes to the user with its result.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | h1: share of 2025 cost of materials in H2 2025 on the year's presentation, $50,370 million (D06 FY 101,096 - D08 restated H1 50,726) | Open: 47,216 (D04's first half), not rejected by the words, only by the documents; 52,196 (D05 Q3 + Q4) not a portion of 101,096. D06 and D08 each indispensable; delete-and-guess passes. Screen clean (after "full-year" dropped) | quick test 2026-10-14: "too easy"; dropped, family closed |
| i02 | [i02](sketches/i02.md) | h1 sibling: twelve months ended June 30, 2026, $111,685 million | Open: 113,511 (D05 Q3 as first printed), 108,531 (D04 first half), 118,620 (all old presentation). D06, D08 indispensable. The usual TTM route reaches the gold without noticing the change, so weaker against the high model; fallback if i01 fails "One defensible answer" | quick test 2026-10-14: "too easy"; dropped, family closed |
| i03 | [i03](sketches/i03.md) | h9: West Coast operating expenses excl. depreciation per barrel, Q3 -> Q4 2025, -$1.3 (lure +$0.8 from the printed "Adjusted" rows, which leave out Q3's $50M Benicia retention costs) | Open: Valero's adjusted per-barrel statistic as the measure (+0.8), rejected by "operating expenses" and D05's definition. D05 and D06 indispensable (without D05 the rebuilt Q3 gives -1.4). Screen clean but D05/D06 regional rows sit past character 20,000 (expected form number-check false alarms) | screen 3/3; quick test survived (user, 2026-10-14); written up as q01 rev 0 (checked, run pending) |
| i04 | [i04](sketches/i04.md) | h4: DGD's 2025 capital investments vs Valero's January 2025 outlook, $50 million less (outlook prints only the other member's half, 110, so DGD expected 220; actual 71 + 99 = 170) | Open: the halves (110 - 85 = 25), rejected by "Diamond Green Diesel spend" and the row label. D02 and D06 indispensable | screen 3/3; quick test failed (user, 2026-10-14); dropped |
| i05 | [i05](sketches/i05.md) | h7: 2025 capital investments not for sustaining the business, $203 million (four quarterly prose splits; no annual split printed) | Open: Q4 only (44), attributable base (112), table categories (799), each rejected (see sketch). D03-D06 each indispensable | screen 3/3; quick test survived (user, 2026-10-14); written up as q02 rev 0 (checked, run pending) |

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
