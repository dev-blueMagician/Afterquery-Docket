# aq-06994 - lean candidate sketches

Current target: hard (user, 2026-10-19: no Easy or Medium slot for this bundle; check starts at High).
Repeat of aq-06801 (identical documents); the user chose "Proceed, new stacks" (2026-10-19). aq-06801's i01-i05
(all local 3/3; i01-i04 "all too easy"; i05 = q01 High 3/3 Too easy) are history in
[aq-06801/notes/ideas.md](../../aq-06801/notes/ideas.md); their families are closed here (hooks.md).
Measured platform success pending. Origin of every sketch: claude. Hooks in notes/hooks.md.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | h16 Comtech's last quarter of positive GAAP operating income (fiscal Q4 2025, printed nowhere as a quarter): operating income before restructuring / net sales = (1,861,000 + 1,363,000) / 130.4M = 2.47% | lures 2.50 (D01's rounded $1.9M), 1.96 / 1.99 (S&S-only $0.7M), 4.83 (Q3 FY26 non-GAAP line), 7.60 (Q4 non-GAAP); broad "restructuring" (CEO transition added, 3.27%) rejected by every operating-income itemization. Needs D04 (FY less nine months) + D02 (Q4 net sales; D01's 14.8% alone reaches 2.48%). Form false alarms: D04 cells past character 20,000, D02's 130.4 deep | screen 3/3 right (row 116); handed over, ranked second |
| i02 | [i02](sketches/i02.md) | h17 Comtech total outstanding borrowings, Jul 31 2025 (234.045M, only as 10-Q note rows) to Apr 30 2026 (223.8M): -10 | lures +10 (D04's own Jul 31 net column), +1 (net both dates), -17 (cash repayments), -13 (D01's Oct 31 base), -3 (make-whole). Needs D02 + D04. Form false alarms: D02 note rows deep | screen 3/3 right (row 117); handed over, ranked third |
| i03 | [i03](sketches/i03.md) | h24 the 3M move: Comtech Adjusted EBITDA change, quarter ended Jul 31 2025 (13,310,000, only FY less D04's nine months) to Oct 31 2025 (9,606,000), in thousands: -3,704 | lures -3,700 (D01/D02's own sentence: $9.6M vs $13.3M), -3,694 (mixed), -2,970 (Q3 FY25 base), -4,094 (Allerium's $13.7M). Needs D04 + D01 (or D03, or D02 for the October figure). Form false alarms: D04 and D01 reconciliation cells past character 20,000 | screen 3/3 right (row 118); handed over, ranked first |

Round 1 (i01-i03) moves away from aq-06801's families: the bank's 3M move (a rounded prose figure beside the
exact one only a fiscal-year-less-nine-months subtraction gives; i03 in its pure form, i01 stacked with a
selector, a segment-only look-alike and a non-GAAP look-alike), and a look-alike basis (net carrying amounts
against borrowings) with a base date printed only in the 10-Q's notes (i02). All three local 3/3 at high
confidence: likely Too easy at High; ranking within the round follows the platform evidence for the 3M move
(the bank's 3M pass; ledger row 114, Solver A 0/3 on a rounded headline). Reserve: h19 (S&S sale price / trailing
net sales, 0.70x; same family as aq-06801 i04).
