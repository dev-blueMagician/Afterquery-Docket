# aq-06835 - lean candidate sketches

Current target: hard (user, 2026-10-18: "there is no slot for Easy or Medium Tier for this bundle, we should
target high"); measured platform success pending. Origin of every sketch: claude. Task page (capture
17:59): Hard 0/5 open, Medium closed, Easy full; 0 of 20 quick tests and 15 of 15 runs used; up to 5 ideas.
Five sketches, five distinct mechanisms (i01 and i05 share hook h1's conversion step). Every sentence passed
`docket_agent.py screen` with no failure; the remaining notes are settled in each sketch.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md): Stryker Instruments, twelve months to Jun 30, 2026, 2025 make-up; gold 3,278 | h1 | lures 3,350 (as printed), 3,251 (OI not added), 3,269 (ET kept); D06 + D05 necessary, D04 optional | local 3/3 (ledger row 70); quick test failed (user, 2026-10-18) |
| i02 | [sketches/i02.md](sketches/i02.md): ZB best adjusted-gross-margin quarter of 2025 (Q3, unprinted) -> reported operating profit margin; gold 17.55% | h2 | lures 6.89 (Q4), 14.44 (Q2), 26.53 (adjusted); D09 + D08; all ZB inputs past the form's number window (false alarms); same mechanism as aq-06801 i02 (local 3/3) | local 3/3 (ledger row 71); quick test survived (user, 2026-10-18: "only i02 survived"); promoted to [q01](../questions/q01.md) rev 0, checked |
| i03 | [sketches/i03.md](sketches/i03.md): Edwards pre-tax impairment losses on investments, Q3 2025-Q2 2026; gold 263.4 | h4 | lures 303.4 (developed-technology $40.0M), 310.5 (window), 206.7 (after tax); D03 + D02; Q2 2026 wording "one of its VIE" | local 3/3 (ledger row 72); quick test failed (user, 2026-10-18) |
| i04 | [sketches/i04.md](sketches/i04.md): ZB second-half 2026 growth implied by the latest reported-revenue guidance midpoint; gold 2.0% | h5 | lures 0.3 (earlier edition), 1.0 (CC), -1.2 (organic); D09 + D08 | local 3/3 (ledger row 73); quick test failed (user, 2026-10-18) |
| i05 | [sketches/i05.md](sketches/i05.md): Stryker Orthopaedics, 2025 make-up, in the weakest 2025 knee quarter (Q3, unprinted); gold 2,255 | h1 | lures 2,355 / 2,810 (Q1), 1,333 (mixed), 2,318 (ET); D06 + D05 (+ D04 optional) | local 3/3 (ledger row 74); quick test failed (user, 2026-10-18) |

Round 2 (2026-10-18, after q01 rev 0 came back Too easy at High 4/6; playbook section 7: replace the stack). The derived-quarter selection is kept only where the answer moves elsewhere (i06 into notes' prose, i07 into reconciliation rows); i08 and i09 are new families.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i06 | [sketches/i06.md](sketches/i06.md): ZB's best 2025 quarter by reported operating margin (Q3, unprinted) -> its contingent-consideration fair-value gain, built from prose in D09 and D08; gold 55.1 | h2 | lures -1.7 (Q1), 62.8 (first half skipped), 82.0 ("respectively" swap); D09 + D08 | local 3/3 (ledger row 87); quick test failed (user, 2026-10-18: "all too easy") |
| i07 | [sketches/i07.md](sketches/i07.md): Stryker's weakest 2025 quarter by reported gross margin (Q3, unprinted; Q1 and Q2 print 63.8% each) -> inventory step-up; gold 61 | new | lures 65 (Q2), 34 (Q1), 160 (year less Q4); D06 + D05 | local 3/3 (ledger row 88); quick test failed (user, 2026-10-18: "all too easy") |
| i08 | [sketches/i08.md](sketches/i08.md): Edwards' Q3 2025 operating margin excluding only certain litigation expenses (90.4, prose only); gold 25.6% | h6 | lures 27.5 (adjusted), 20.5 (2024's 10.8), 22.9 (Q4); D03 + D02 | local 3/3 (ledger row 89); quick test failed (user, 2026-10-18: "all too easy") |
| i09 | [sketches/i09.md](sketches/i09.md): Edwards minus Stryker adjusted operating margin, Q3 2025 (both unprinted); gold 1.9 | new | lures 2.6 (Q2), 1.0 (reported); D03, D02, D06, D05 | local 3/3 (ledger row 90); quick test failed (user, 2026-10-18: "all too easy") |

Round 3 (2026-10-18, after round 2's quick tests: "all too easy"). The last round before reporting options (WORKFLOW section 6). It carries q01's three features (an unprinted quarter that wins an adjusted-margin selection by a fraction of a point, the answer on the other basis, two decimals) to new data.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i10 | [sketches/i10.md](sketches/i10.md): Stryker's lowest 2025 adjusted gross profit margin quarter (Q3, 64.93%, under Q4's printed 65.2%) -> reported operating income margin; gold 18.74% | q01 stack on Stryker | lures 25.16 (Q4), 25.59 (adjusted); D06 + D05 | local 3/3 (ledger row 92); quick test failed (user, 2026-10-19: "all too easy"); promoted to [q02](../questions/q02.md) rev 0 for a run (user, "go on option 1") |
| i11 | [sketches/i11.md](sketches/i11.md): smallest Q3 2025 gap between adjusted and reported operating margin among the three companies (Stryker 6.85; Edwards smallest in every printed quarter but Q4); gold 6.85 | new | lures 1.40 (Q2), 6.25 (year), 5.02 (Q4); six documents | local 3/3 (ledger row 93); quick test failed (user, 2026-10-19: "all too easy") |
| i12 | [sketches/i12.md](sketches/i12.md): Stryker's 2025 quarters ranked by reported gross profit margin, lowest first (Q3 unprinted; Q1 and Q2 print 63.8% each); gold Q3, Q2, Q1, Q4 | new | lures Q2, Q1, Q4; Q3, Q1, Q2, Q4; D06 + D05 | local 3/3 (ledger row 94); quick test failed (user, 2026-10-19: "all too easy") |

Not drafted: Stryker's largest quarterly impairment of 2025 (Q3, 73; a single rebuild, playbook section 2), h6 (Edwards Q3 2025 operating income), h7 (ZB E&O twelve months), h8 (ZB Q2 dividends + buybacks,
a bank topic), Edwards quarterly sales beat over projections (19.6; forecast vs actual plus rounded "$1.74
billion" highlight; kept in reserve).
