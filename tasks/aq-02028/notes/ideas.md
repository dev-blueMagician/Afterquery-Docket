# aq-02028 - lean candidate sketches

Current target: medium (user 2026-10-08: no Easy slot, "target medium and high"); measured platform
success pending.
Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources to verify
premises, exact names, terms, periods and units. A sketch needs question, provisional short gold,
essential inputs/locations, ambiguity and necessity checks, mechanism, risk and decision. Keep at
most two active sketches. Full components, submission reasoning and mechanical preflight follow
promotion; complete relevant membership/exclusion proof before promoting a list/count. The platform
validates the completed question; do not predict its tier or run local models by default.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) (origin claude, target medium) | h1: D06 exemption end date (31 March 2022) selects each D02 Attachment A rate; mean of 13 import rates | Competing: $111.55 stale as-at, $120.28 every scheduled rate, $114.43 month-first dates, $96.98 export, Table 1 averages; each fails the stated day, "import" or the period/scope. Necessity: D06 sole end date (D19/D17 undated); D02 sole per-terminal rates. Risk: end date recallable | screen passed 2026-10-08; promoted to [q01](../questions/q01.md); quick test "Too easy" on rev 4 (F3, after F2 on rev 2): dropped |
| i03 | [sketches/i03.md](sketches/i03.md) (origin claude, target medium) | h8: VTA's TEU-to-trips method and printed 342,857 (D08) on its own 3m base vs the port throughput stated by the newest terminal (D01, 2.88m); fewer trips at 3.5 vs 2.5 TEU = 329,000 | Competing: 343,000 (VTA base, printed), 91,000 (VICT's own 800k capacity), 617,000 (containers per truck), 432,000/192,000 (4/3 TEU); each fails the stated base, "port", TEU loads or "estimated capacity". Necessity: D01 only other Melbourne throughput; D08 only load factors | screen passed 2026-10-08 (3.5 TEU design); promoted to [q02](../questions/q02.md). Rev 1 takes the sketch's 4 TEU route as the gold (432,000), because 2.88 / 3.5 never terminates and the form accepts only exact "=" results (F4); traps 450,000 (Doc 8's printed figure on its own base) and 120,000 (VICT's own capacity). Rev 1 difficulty check: Too hard 0/15 (F5), "port throughput [the terminal] states" read as VICT's own 800,000; rev 2 says "whole-port throughput", checked, platform pending; a repeat retires the hook |
| i04 | [sketches/i04.md](sketches/i04.md) (origin claude, target medium) | h6: Port Botany 2019 actual 2.6m (D09) to 2045 expectation 8.4m (D13); CAGR 4.6% | Competing: 4.5%/5.1% (D13's 2.7m "today" base), 4.4%/4.8% (27/25 years), 8.6% linear. Risk: plan figures recallable; short route | screen passed; fallback, not promoted |
| i02 | [sketches/i02.md](sketches/i02.md) (origin claude, target medium) | h1 two-row variant: Patrick minus DP World import surcharge at Fremantle on the same day ($12.69) | Stale reading $8.85 fails the day; but "apply every right-hand rate" also reaches $12.69, so the trap is one-sided | screen passed (sketch_sha256 5e95eed1...); kept as fallback, not promoted |

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

For optional script screening save notes/sketches/iNN.md and run docket_agent.py screen --idea iNN.
A passed script screen verifies structure/input quotes only; it does not prove gold/uniqueness or
difficulty. Optional authorized platform draft screens remain preliminary and stage-bound.
Require decoys for which-items; use wrong-route calculations for selected rounding/exclusion
levers. Other hooks may be not applicable. Ordinary valid cross-document reasoning remains eligible.
Preserve failed screens and whether revisions change the actual evidence/mechanism.
Allow one focused repair per distinct observed failure; a repeated failure means change the hook.

## Rejected or parked families (2026-10-08, round 1)

- h2 SA wine share of 2021 export revenue (D05 Figure 2 + D09 "$351 billion or 68 per cent"): part-vs-total
  trap is explicit in D09's sentence; national wine value is widely reported (recall could replace D05); likely
  below Medium. Parked.
- h3 Newcastle Navigation Service Charge, nominal prose vs 2020-dollar Figure 1 (D12): single document; no second
  indispensable source found. Parked.
- h6 Port Botany growth, 2019 actual 2.6m TEU (D09 L107) to 8.4m by 2045 (D13 L167): two lookups and a growth
  formula; same NSW Ports master plan may be recalled; likely below Medium. Parked.
- Rule 10 bars answers naming submitters or counting documents, so list/count questions about which
  organisations recommended something were not pursued.
- Same-label conflicts (D17 vs D19 census shortfall; D08 vs D19 Melbourne access fee history; D10 vs D05/D09 ACCC
  report release date; D02 Table 1 rise cells) give two defensible answers. Rejected.
