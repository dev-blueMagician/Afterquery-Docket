# aq-06903 - lean candidate sketches

Current target: hard (user, 2026-10-18); measured platform success pending. Every sketch is
author-written (origin: claude) and screened by three fresh blind solvers before hand-over; the
screen ranks and never withholds.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | h1 OCF estimate, before working capital, July repriced to April's deck: +0.19 | WC sign and sensitivity edition each have their own wrong answer; D03 (April estimate, deck) and D04 (July estimate, sensitivities) both indispensable | local 3/3 (2026-10-19), ranked with round 1; handed over paste-ready; user quick tests pending |
| i02 | [i02](sketches/i02.md) | h2 silver Jan-Jun 2026, BHP minus Freeport's mines: 5.2 | "report selling" keeps Antamina (BHP's totals); D02 June quarter and D04 six-month notes indispensable | local 3/3 (2026-10-19), ranked with round 1; handed over paste-ready; user quick tests pending |
| i03 | [i03](sketches/i03.md) | h3 Q2 2026 payout share of OCF after capex and NCI distributions: 40% | paid, not declared; own buybacks, not Cerro Verde; whole percent robust to dividend estimates | local 3/3 (2026-10-19), ranked with round 1; handed over paste-ready; user quick tests pending |
| i04 | [i04](sketches/i04.md) | h4 BHP realised copper over LME, Jan-Jun 2026: 27 cents | LME half = mean of two quarterly averages; three documents indispensable | local 3/3 (2026-10-19), ranked with round 1; handed over paste-ready; user quick tests pending |
| i05 | [i05](sketches/i05.md) | h5 implied Jul-Dec 2026 molybdenum sales, April -> July: 0 | "own figures" pins April's Q2 estimate; D03's FY estimate indispensable | local 3/3 (2026-10-19), ranked with round 1; handed over paste-ready; user quick tests pending |
| i06 | [i06](sketches/i06.md) | h10 Q2 2026 revenue from repricing Q1 2026 copper sales: 74 | two routes agree (prior and current columns); consolidated tables govern over the division schedules (73) | local 3/3 (2026-10-19), ledger rows 104-105; quick test failed (user: "both failed") |
| i07 | [i07](sketches/i07.md) | h11 own share of reported copper sales, Jan-Jun 2026, Freeport minus BHP: 1.9 pp | Escondida at 57.5%, Antamina as reported (proportionate), Morenci already net in Freeport's figures | local 3/3 (2026-10-19), ledger rows 104-105; quick test failed (user: "both failed") |

Round 1 (i01-i05): all quick-tested 2026-10-19, all failed (user: "all failed"). Round 2 replaces the hooks.
Recomputations of every gold and lure: scratchpad golds.py (round 1) and golds2.py (round 2), session 2026-10-19.

Closed 2026-10-19 at the user's choice ("Stop on this bundle"): seven designs, all local 3/3, all failed quick tests.
