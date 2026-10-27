# aq-04819 - lean candidate sketches

Current target: medium (user 2026-10-14: no Easy slot, "target medium and high"; lower open tier).
Page at capture: Hard 0/5 · Medium 0/1 · Easy 0/0; quick tests 0 of 15; difficulty runs 15 of 15.
Medium has one slot and 2026-10-14 runs started at Medium (aq-04045) or High (four sets): audit every
sketch against the medium and the high solver. Sketch only until the user reports a quick-test survivor.
Origin of every sketch: claude (i03, i04 and the held-back N1-N3 came from independent author agents,
also claude; the caller verified quotes and arithmetic).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i03 | [sketches/i03.md](sketches/i03.md) | people in the two studies Doc 2 cites for one-to-one targeting: Doc 5 row (44) "Russel" 98 + 104, Doc 10 (unsigned) 12 = 214 | still possible: Doc 10 not accepted as Syvertsen et al. 2020 -> 202 or "not stated" (only Doc 2's content matches reject it); delete Doc 5 -> 12, delete Doc 10 -> 202, delete Doc 2 -> guess could still pair Russell with Doc 10 (stated risk) | quick test failed (user 2026-10-14, "only i02 survived"; no panel, so the route is unknown); closed |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: children/teens surveyed at sports venues in Doc 5's included studies, 152 + 111 = 263 | still possible: "sporting sites" read as websites -> 111 (rejected by the row's context, not the question's words); delete Doc 8 -> 152, delete Doc 5 -> 111 or 210 | quick test failed (user 2026-10-14; no panel, route unknown); closed |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: children/teens in Doc 5's parent-and-child studies, 152 + 61 = 213 | still possible: 59 adolescents assumed -> 211; Thomas (45) added because parents consented -> 324 (rejected by "their parents were also participants"); delete Doc 9 -> 211, delete Doc 5 -> 160 | quick test survived (user 2026-10-14); promoted word for word to questions/q01.md rev 0; Run 1 "Too easy", Low — · Medium — · High 3/3 (high traces not recorded); hook retired, no fair repair |
| i04 | [sketches/i04.md](sketches/i04.md) | live-odds adverts by bookmakers reported promoting through Australian sport, 27 + 3 = 30 | Betfair decoy (court ruling) -> 34; delete Doc 9 -> 3, Doc 8 -> 27 | held back: zero unpointed steps (every link is a name sweep from Doc 6's table); not worth a run even if it survives a quick test |
| N1 | numeric author (not filed) | PGSI 8+ share ratio, GB 2019 emerging adults 131/1,496 vs Norway 126/5,830 = 4.1 | "Use category counts" is a cue; edition choice pointed by "same year" | held back: zero unpointed steps |
| N2 | numeric author (not filed) | PGSI 8+ gap, GB 87.0% vs Sweden 3/11 = 59.7 pp (also the hidden-member author's S3) | 56 words; every input pointed | held back: zero unpointed steps |
| N3 | numeric author (not filed) | live-odds adverts by brands on Doc 4's magnet board, Bet365 31 + Ladbrokes 3 = 34 | same Doc 6 x brand-name join as i04 | held back: zero unpointed steps, redundant |

Measured 2026-10-14: the review-to-study link (q01) is cleared by the high model 3/3; citation links (i03) and a review row's setting (i01) did not hold even the easier solver. Bundle finding (caller and both authors, all ten texts read in full): the eight primary studies are
independent, so cross-document numeric joins are two pointed lookups plus one operation. The only
unpointed adjusters are review-to-primary links (Doc 5 rows (43), (45); Doc 2's citations) and
single-document table traps (Doc 6 table note, Doc 6 odds averaging, Doc 7's 6% base, Doc 7's 55 vs 56),
which fail the two-document rule.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
