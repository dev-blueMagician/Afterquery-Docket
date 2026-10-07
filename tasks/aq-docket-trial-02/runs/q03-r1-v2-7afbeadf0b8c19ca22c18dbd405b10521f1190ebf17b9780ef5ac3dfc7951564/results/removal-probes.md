# q03 rev 1 - removal probes (2026-10-06)

Each probe is a fresh blind-solver agent given a prepared packet of this run, the verbatim question
and an instruction to treat one marked document as absent and answer "as you normally would" (best
answer plus probability). Approximates the platform's document check. Not an official blind solve.
tested_sha256: 7afbeadf0b8c19ca22c18dbd405b10521f1190ebf17b9780ef5ac3dfc7951564. Gold: 19.68%.

## Without D10 (recast segment exhibit), solver-1 packet

Summary of the verbatim return (task notification 2026-10-06; key lines quoted):
"Not answerable exactly without D10. My best answer is **23.11%** (full-year 2024 operating profit of
$253M ÷ net sales of $1,095M for the whole old Africa/Eurasia segment). I put about a 15% chance on it
being the requested figure ... If it means only the part that moved (excluding Russia and Belarus), my
estimate is about 23.3%, with a plausible range of about 22.2–25.1%. A two-decimal match there is under
2% likely."
path: D11 l.85 composition; D09 l.464/481 (and D05 l.461/478) whole-segment 2024 1,095 / 253;
"Russia" and "Belarus" only in D11; no 2024 recast in D11/D12; 2025 Russia and Belarus derived from Q1
(D11 vs D06) and Q2/H1 (D12 vs D07); H1 2025 shares applied to 2024 give 23.30%; Q1 or Q2 shares give
25.12% or 22.22%.
contaminated: no.

Result: gold 19.68% not reached (best 23.11%; estimate about 23.3%). D10 needed.

## Without D11 (Q1 2026 release, the composition note), shortcut packet

Summary of the verbatim return (task notification 2026-10-06; key lines quoted):
"answer: 23.11% (253 / 1,095). This holds if the whole former Africa/Eurasia segment went into EMEA.
Without D11 nothing in the packet confirms that, so it can't be answered exactly. Best answer 23.11%,
about 80% likely to be right."
path: D09 l.464/481 and D05 l.461/478 (2024: 1,095 / 253); D04 nine months plus Q4 cross-check; D10
l.58 EMEA 4,046 / 814; segment changes net to zero (North America -397/+17, Asia Pacific +216/+80, EMEA
vs Europe + Africa/Eurasia +181/-97); D12 l.83/117 generic recast notes.
readings: whole former segment 23.11% (main); quarterly-sum denominator 23.08%; EMEA minus old Europe
12.23%; whole recast EMEA 20.12%; "Only part of Africa/Eurasia moved to EMEA ... would not be
answerable"; the 20% risk is that D11 says only part moved.
contaminated: no.

Result: gold 19.68% not reached (best 23.11% at about 80%). D11 needed in practice; the no-D11 reading
is the whole segment, as designed.
