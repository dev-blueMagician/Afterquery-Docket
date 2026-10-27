# aq-07019 - lean candidate sketches

Current target: hard (user, 2026-10-19); measured platform success pending. Repeat of aq-06903 and
aq-01189 (same four documents); the user chose "Proceed, Hard, new hooks". Every sketch is
author-written (origin: claude) and screened by three fresh blind solvers before hand-over; the screen
ranks and never withholds.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | h12 BHP realised energy coal price, quarter ended 30 June 2025: 85.7 | weights fixed by the price note (export only, BMA energy coal in), verified on FY26; D01 (9M FY25 price) and D02 (FY25 price) both indispensable | local 3/3 (2026-10-19, high confidence; ledger row 119), ranked first; handed over paste-ready; user quick tests pending |
| i02 | [i02](sketches/i02.md) | h13 BHP's 85% share of WAIO production, Jan-Jun 2026 v Jan-Jun 2025: -622 | "ownership share" = 85% of WAIO (header + Jimblebar note); March 2025 quarter only in D01, June 2026 quarter only in D02; second reading -1,389 (reported Total) named by two solvers and rejected on "ownership share" + the Jimblebar note | local 3/3 (2026-10-19, high/medium/medium; row 120), ranked second; handed over paste-ready; user quick tests pending |
| i03 | [i03](sketches/i03.md) | h14 BHP realised steelmaking coal price, quarter ended 30 June 2025: 177.3 | sibling of i01 (offer one of the two); hard-coking-coal weights implied by the energy coal note, verified on FY26 | local 3/3 (2026-10-19, high confidence; row 121), ranked third (sibling of i01); handed over paste-ready; user quick tests pending |
| i04 | [i04](sketches/i04.md) | h12b BHP realised energy coal price change, quarter ended June 2025 to June 2026, one decimal: 37.4 | round 2; same derived price as i01 with no method given and D02's rounded "37%" beside the answer; weights fixed by the price note, verified on FY26 and H2 FY26; alternative to i01 (offer one) | local 3/3 (2026-10-19, medium-high/high/high; row 122); handed over paste-ready |
| i05 | [i05](sketches/i05.md) | h18 assets beating the top of the half-year FY26 range, ranked by % overshoot: Samarco, NSWEC, Antamina | all three solvers raised "BHP assets" read through the boilerplate as operated assets only (NSWEC alone) | local 3/3 (row 123); wording defect, superseded by i08; not offered |
| i06 | [i06](sketches/i06.md) | h19 like-for-like copper production change, Jan-Jun 2025 to Jan-Jun 2026, assets producing in Apr-Jun 2026: -5.7 | March 2025 quarter only in D01, June 2026 only in D02; Carajas out of both halves by a structural test | local 3/3 (high; row 124); handed over paste-ready |
| i07 | [i07](sketches/i07.md) | h20 Apr-Jun 2026 ore throughput per day, Cerro Verde minus Escondida, nearest thousand: 22,000 | Cerro Verde = Freeport's South America mill line (El Abra has no mill); Escondida at 100% over 91 days | local 3/3 (high; row 125); handed over paste-ready |
| i08 | [i08](sketches/i08.md) | h18 repaired: the assets BHP gave production guidance for: Samarco, NSWEC, Antamina | one focused repair of i05's scope; nothing else changed; the operated-only reading no longer fits (two solvers did not raise it, one rejected it on the question's words) | local 3/3 (high; row 126); handed over paste-ready |

Rejected this session: h15 (precision), h16 (period lever does nothing), h17 (necessity), the page's
debt-limit idea (Doc 1 not needed). See notes/hooks.md.

Round 2 (2026-10-19, after the 08:13 capture showed 0 of 20 quick tests used): re-checked for restated
figures (BHP: 142 overlapping quarter rows and every year-to-date column agree; only a 1 kt Samarco
rounding), so the restated-figure lever stays unavailable. New stacks i04, i06, i07 and i08 (i05
repaired); all screened 3/3. Considered and not drafted: Samarco/NSWEC operated-asset growth (keyword
leads to the boilerplate), exploration expensed share Q4 v Q4 (two rebuilds of one kind), iron ore Q4
YoY (4.6, weaker sibling of i04), steelmaking coal YoY (31.35% sits on a rounding boundary), FCX payout
and provisional-pricing designs (tried on aq-06903 or approximate sensitivities).
