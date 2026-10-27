# aq-01960 - lean candidate sketches

Current target: medium (user 2026-10-08: "there is no slot for Easy Tier for this bundle, we should
target medium and high. do you best."); hard where a design allows. Measured platform success pending.
Hooks: [hooks.md](hooks.md). Map: [doc-map.md](doc-map.md).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: Q4 FY26 non-GAAP gross profit vs gross profit implied by D13 guidance midpoints | Bundled acquisition charges 33,069 -> 3.2; GAAP GP -> 1.7; D14 own guidance -> -8.8; range-midpoint reading -> 3.2 (excluded by "multiplying the midpoints"); stated revenue variants all 3.3 at 1 dp. D13 and D14 each hold unique inputs; D12-proxy -> 10.2 | screen pass 2026-10-08; promoted q01; form quick test 2026-10-08 "too easy" (user report) -> q01 dropped |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: FY26 GAAP gross profit vs sum of quarterly guidance-implied gross profits | Off-by-one editions -> -$302M; non-GAAP midpoints -> $96M; range-midpoint reading -> $244M; revenue variants 250/251 (prose visibly rounded). D10-D13 GAAP GM guidance unique, D14 FY totals unique; neighbour-midpoint proxies all differ in dollars | screen pass 2026-10-08; promoted q02; rev 1 2026-10-08 fixes the form's reasoning number warnings (Steps 2, 4, 6, 8); form quick test "too easy" (user report 2026-10-08) -> q02 dropped; family retired |
| i03 | [sketches/i03.md](sketches/i03.md) | h7: split-anchored guidance in force, per post-split share | D14 $1.14 decoy fails "in force when"; $9.66 fails "per post-split share"; D12 $0.885 superseded. D13 and D14 each unique | screen pass 2026-10-08; form quick test "too easy" (user report) -> dropped |
| i04 | [sketches/i04.md](sketches/i04.md) | h8: FY26 non-GAAP gross margin from full-year totals, grouped 178,075 as the printed decoy | 178,075 -> 62.61; D14 quarters only -> 61.84; quarterly-mean -> 62.41 (excluded by "full-year totals"); Q4x4 -> 62.37 (two decimals). D14 unique; first-half splits need D12 or D11+D13 (form "or" group) | round 3: screen pass 2026-10-08; offered for the form's quick test before write-up |

Rejected before sketching (see hooks.md): h1a margin form (gold 0.6 shared by GAAP route and a
D12-proxy route), h2a non-GAAP fiscal-year form (midpoint coincidences), h3 split EPS beat (whole
cents only, weak trap), h4 dividend levels, h5 balance-sheet changes, h6 impairments/Display exit.

Rounds: 1 (i01, i02), 2 (i03), 3 (i04). Set note: q01 and q02 shared the "guidance-implied gross profit" construct (q01 non-GAAP, one
quarter, D13-D14; q02 GAAP, four quarters, D10-D14). They are a ladder on one family, not two
independent families; no other robust Medium-capable family was found in this bundle.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
