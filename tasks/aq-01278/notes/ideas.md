# aq-01278 - lean candidate sketches

Current target: medium (user, 2026-10-06: "difficulty_target to at least medium"); measured platform success pending.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, mechanism, source risk and preliminary decision. Full components,
submission reasoning, membership proof and independent checks follow promotion.

Round 1 (2026-10-06): two independent question-author runs (origin claude): A on Travelers/Allstate
(i01-i04), B on Progressive/Chubb (i05-i09, B's own ids i01-i05 renumbered). Caller verified the
inputs of i01, i03, i05, i06 in text/Dnn.txt and recomputed their golds.

| ID | Hook/mechanism | Question and provisional gold | Essential inputs/locations | Selected levers/applicable tests | Source risk | Sketch screen/decision |
| --- | --- | --- | --- | --- | --- | --- |
| i01 | h2 reversed: Canadian auto premiums only in D10's statutory product page | Travelers personal auto NWP incl. the Canadian business sold in Q1 2026, Q2 2025 to Q2 2026 change, sign, one decimal: -10.4% | D09 PI NWP table auto 1,858 / 1,968, International - / 178, prose $178M; D10 p.20 auto statutory NWP 2Q25 2,074 (p.19 domestic 1,968 + International 178 split 106/72 via p.21 homeowners 2,592) | scatter the pieces; calculate across docs. Wrong: domestic -5.6% (printed "(6)%"), all 178 to auto -13.4%, segment -7.7%, pro-rata -9.2% | statutory label (totals equal GAAP in all quarters); inputs in pipe rows only | screen passed; closed-book "about -6.0%" (miss); filed as q01 rev 0: two matches, audit clear, closed-book miss; quick-test batch |
| i02 | TTM build of a non-GAAP measure | Travelers pre-tax underlying underwriting income, twelve months ended June 30, 2026: $6,901M | D10 p.3 3Q25/4Q25 premiums, fee income, claims, DAC, G&A, non-insurance G&A, cats, PYD (1,758; 1,944); D08 $1.521B; D09 $1.678B (H1 3,199) | calculate across docs; aggregation. Wrong: statutory row 6,974; calendar 2025 6,919; no non-insurance exclusion 6,660 | long build: Too-hard risk; method reproduces printed 1Q25, 2Q25, 1Q26; Q3/Q4 2025 headline values pre-cutoff | closed-book "About $6,800 million" (miss, near); reserve |
| i03 | match then exclude with an unprinted Q2 exclusion | Travelers H1 2026 repurchase cost under board authorizations: $3,100M | D08 $1.800B under authorizations (+$185M employee), capacity $5.215B Mar 31; D09 $1.311B total, capacity $3.915B Jun 30 | match then exclude. Wrong: 3,111 (1,800+1,311), 3,296 (headlines) | relies on no new Q2 authorization (bounded: any new one <= $11M) | closed-book: "about $3,000 million", low, 15% (miss, near); one-answer risk; quick-test batch |
| i04 | stated method, unreported period | Allstate homeowners recorded combined ratio, twelve months ended June 30, 2026, one decimal: 76.5 | D03 p.7/10 Q3/Q4 2025 PE and UW income; D02 H1 2026 | none (ordinary); wrong: simple average 76.2 | aq-00998 q05 shape (measured Easy); two-decimal split | hold (Easy-leaning) |
| i05 | count derived as equity / BVPS at two dates | Chubb common shares outstanding fall Mar 31 to Jun 30, 2026, one decimal: 2.9 million | D04 equity 73,788, BVPS $189.93; D05 equity 75,372, BVPS $195.45 (388.50 -> 385.63) | calculate across docs. Wrong: Q2 buybacks 979/327.18 = 3.0; diluted averages 3.3 | count inferred (BVPS denominator not defined; tangible BVPS "divided by the shares outstanding"); 2.9 vs 3.0 closeness | closed-book "about 3.8 million" (miss); quick-test batch |
| i06 | scope trap: P&C vs consolidated six-month line | H1 2026 vs H1 2025: Progressive NPW increase minus Chubb P&C NPW increase: $1,272M | D07 44,718 / 42,282; D04 P&C 11,716 / 10,926; D05 P&C 12,768 / 12,394; D05 six-month consolidated 28,710 / 26,842 (decoy) | calculate across docs. Wrong: consolidated 568; Global P&C 1,350 | Chubb six-month P&C not printed (needs D04); pipe cells | closed-book "About $1,000 million" (miss); quick-test batch |
| i07 | invested-assets definition only in D05 | Chubb total invested assets growth in Q2 2026: $2,573M | D05 172,649 + 2,753 = 175,402; D04 170,195 + 2,634 | wrong: investments only 2,454; six months 4,212 | layout shows the sum | drop (Easy; sibling of i05) |
| i08 | carve-out printed in table label | Chubb Agricultural underwriting income, H1 2026: $184M | P&C minus Global P&C, Q1 (D04) and Q2 (D05) | wrong: 274, 122 | rule printed beside the numbers | drop (Easy) |
| i09 | h1 footnote with base conversion | Progressive Personal Lines property combined ratio, Q2 2026, excluding the one-time June methodology benefit, whole point: 82 | D07 June 258 / 65.6 / footnote 11.7; D07 YTD 1,547 / 78.1; D06 YTD 770 / 78.3 | wrong: 78, 80, 90 | names the exclusion (measured too-easy signpost); whole-point only | hold (Easy predicted) |
| i10 | i01 without the Canadian cue (caller rewording) | Travelers worldwide personal auto NWP, Q2 2025 to Q2 2026, sign, one decimal: -10.4% | as i01 (D09 domestic Automobile under a "Domestic" heading; D10 p.20 2,074) | scatter the pieces; printed domestic "(6)%" in the path | "worldwide" = domestic + international (ordinary meaning) | screen passed; closed-book "About -5.0%", 3% (miss); quick-test batch |

| i11 | same series, right edition: a Q1 growth basis applied to Q2 rows (round 2, origin claude) | Chubb NA commercial NPW grew 2.8% in Q1 2026; on that same basis, Q2 2026 YoY change, sign, one decimal: -1.3% | D04 L45 bullet; D04 NA total 6,887/6,615, personal 1,681/1,552 (ex-personal +2.82%; commercial segment alone 2.3%); D05 NA 8,424/8,394, personal 2,054/1,938 | decoy D05 "North America Commercial was down 2.3%" (also CEO quote, table); NA total +0.4% | tie phrase "On that same basis" needed for fairness; pipe-cell inputs | filed as q02 rev 0; checks running; quick-test batch slot 5 |
| i12 | segment premiums built from statement minus segment rows (round 2) | Allstate Protection Services premiums earned, Q2 2025 to Q2 2026, sign, one decimal: +8.2% | D02 statement P&C premiums 15,670/15,041 minus P-L premiums earned 14,918/14,346; D03 glossary scope sentence and PS premiums-earned series 671-751 | decoy PS revenue +7.8% (D02 L160) | D02 alone gives both quarters if the identity is guessed (author: ~35% removal risk) | reserve; needs a removal probe before any test |
| i13 | same family as i11 on Chubb's P&C consumer/commercial split | Chubb commercial P&C NPW grew 4.6% in Q1; same basis in Q2: +0.8% | D04 L41; D05 P&C, NA personal, OG consumer rows | decoys +8.8% (Overseas General commercial), -2.3%, 3.0% | removal risk without D04 25-30% | reserve (use only if q02 measures Easy) |
| i14 | segment combined ratio with inferred earned premium (round 2) | Chubb NA Agricultural combined ratio, H1 2026, whole percent: 78% | D04/D05 P&C minus Global P&C UW income; segment CRs 37.5%, 89.7% | decoys 63.6, 74.8, 83.9 | denominator inferred; fails "printed decoy in path"; Too-hard risk | drop |

Discarded leads (round 1): Allstate "2.4 points" (imprecise; Q1 89.5 printed in D01 and D03);
Allstate diluted-share BVPS (no answer change); PIF excluding sold businesses (count not printed);
Progressive "about 3 percentage points" and TNC renewal (approximate / no amount); Chubb
"excluding large account and E&S property" carve-outs (do not reconcile; D04 7.7% vs 7.8%);
Travelers repurchase capacity alone (two lookups); Progressive rebuilt component ratios (66.76 vs
printed 66.7: definitional mismatch, avoid).

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
