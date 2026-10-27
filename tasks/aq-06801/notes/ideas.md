# aq-06801 - lean candidate sketches

Current target: hard (user, 2026-10-18: no Easy or Medium slot for this bundle; check starts at High).
Measured platform success pending. Origin of every sketch: claude. Hooks in notes/hooks.md.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | h1 Comtech GAAP net income, fiscal Q4 2025 (+7.9, printed nowhere) to fiscal Q1 2026 (-15.9): -23.8 | NLA reading (-8.2) fails "net income or loss"; non-GAAP (+2.0) fails "GAAP". Needs D04 (nine-month FY25) + one of D01/D02/D03 (Q1 FY26). Form number check: D04 inputs sit past character 23,000 (expected false alarms; cite D02 for Q1 FY26) | screen 3/3 right; user (2026-10-18): "all too easy" |
| i02 | [i02](sketches/i02.md) | h2 Iridium lowest-net-income 2025 quarter (Q2, printed nowhere): OEBITDA margin 55.9% | Q4 lure 54.2%; H1 56.4%. Needs D05 + D06; D07 replaceable (FY less nine months) | screen 3/3 right; user (2026-10-18): "all too easy" |
| i03 | [i03](sketches/i03.md) | h3 Iridium commercial IoT ARPU, H2 2025 less H1 2025 by the footnote's two-point average: +$0.14 | averaged quarterly ARPUs $0.04; FY - 9M $0.03. Needs D06 + D07 | screen 3/3 right; user (2026-10-18): "all too easy" |
| i04 | [i04](sketches/i04.md) | h12 Comtech Adjusted EBITDA / net sales, twelve months ended Apr 30 2026: 8.9% | nine months 8.3%; Q3 FY25 as proxy 8.8%. Needs D04 + D02 (or D01). Form false alarms as i01 | screen 3/3 right; user (2026-10-18): "all too easy" |
| i05 | [i05](sketches/i05.md) | h14 Comtech preferred stock's bifurcated derivative, fair-value change in the quarter to Jan 31 2026: -1.8 (printed nowhere; D02's carrying-value rule applied to D03's caption) | D03's mislabeled "purchase option liability" line +1.4; liabilities line +3.1. Needs D02 + D03 (D04 long route). Form false alarms on D03's figures | round 3; screen 3/3 right; quick test survived (user, 2026-10-18: "i05 survived"); promoted word for word as q01 (checked rev 0, tested_sha256 59a088bb...) |

Round 1 (i01, i02) both 3/3: every solver derived the missing period, rebuilt the FY figure and named each lure;
all searched the 10-Q rather than reading it. Round 2 changes mechanism (a rule applied to unreported half-years;
a trailing window with a prose-only input) rather than wording. Round 2 also 3/3 (i03, i04): solvers applied the footnote per half and found the 10-Q's Q4 sales by search.
Remaining reserve: h4, h5 (same derived-quarter family as i02, cleared at high confidence). Ledger rows 56-59, 83.
Round 3 (i05) also 3/3: solvers found the 10-Q's rule and rejected the mislabeled line. Reserve h15 (APIC overlap, 111.1) unscreened: post-October allocation only inferred.
