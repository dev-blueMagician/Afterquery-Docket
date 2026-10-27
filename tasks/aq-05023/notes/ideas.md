# aq-05023 - lean candidate sketches

Round 1 result (2026-10-14): both filed sketches rejected by the strong-solver screen (3/3 right each); no
fair sketch left without a screen result. Current target: hard (user, 2026-10-14: "there is no slot for Easy or Medium Tier for this bundle, we should
target high"; page: "Easy or Hard only", "Hard 0/5 · Medium closed · Easy 0/0"). Measured platform success
pending. The difficulty check will run at the High level only; a quick-test survival (easier solver) says
nothing about it. Origin of every sketch: claude unless marked otherwise.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h3: FY2025 buyback spending / FY2025 net income, both built by roll-forward (remaining authorization; accumulated deficit); gold 4.3 | Every buyback basis gives 4.3; wrong routes 3.8 (program-to-date), 5.1 (nine months), 4.5 (target top), 3.2, 6.8. Groups: D08 or D04; D02 or D06 (D01/D05 approximate); D02 or D06 alone also gives FY net income (both print the Dec 31, 2024 and 2025 deficits). Watch: share-count estimate without D04/D08 can land on 4.3; full-year 2025 figures may be recallable if the 2026 documents are real filings | mechanical screen eligible; not a playbook design ("a number rebuilt from printed figures", hard-playbook section 3); strong-solver screen run for completeness 2026-10-14 (packet i01-screen-bbdb90e8...): right 3/3, REJECTED: all three rebuilt both figures and rejected the program-only 3.8 by name |
| i02 | [sketches/i02.md](sketches/i02.md) | h5 reframed by an independent author (origin claude): Q1 2025's share of the nine-month 2025 G&A total; the only standalone Q1 2025 print (20,885, 2026 filings) is re-presented; gold 36.0% | Lure 29.1% (re-presented Q1), mixed 37.6% / 27.5%. Groups: D08 or D07; D04 or D03. One unpointed inference (basis), lure printed and labelled "As Reported (1)". Risk: "One defensible answer" if both form solvers take 29.1% | mechanical screen eligible; strong-solver screen 2026-10-14 (packet i02-screen-61b3e914...): right 3/3, REJECTED: all three found the re-presentation (footnote, Note 1, H1 41,416 vs 47,566) and rejected 29.1% by name. Siblings over other expense lines keep the same deciding step: not screened |
| r1 | (both author reports, not filed) | Buybacks Jan 1, 2025 - Jun 30, 2026 by aggregate purchase price, $143M (143,235); program shortcut 133, Q4 omitted 121, cash-flow or equity basis 144 (so "aggregate purchase price" must be named) | Same roll-forward as i01's buyback half, one inference; the window's start date may send the high model to the program start | not screened separately: its deciding steps (Q4 2025 from the authorization drop; rejecting the program-only total) were cleared by all three i01 solves |
| r2 | (author B report, not filed) | Q4 2025 net income from the accumulated deficit, $7.4M (7,398) | One inference, no printed decoy (wrong: equity change -5.0, comprehensive 7.8, FY 20.1); recall risk if the 2026 filings are real | not screened separately: all three i01 solves derived Q4 2025 net income 7,398 from the deficit |

Wording choice for i02: author A's "the general and administrative expense Cars.com reported for the nine
months ended September 30, 2025" (pins the denominator to the printed 71,890); author B's version without
"reported" leaves the denominator's presentation open. Both authors independently ranked this hook first.
Quick tests (user, 2026-10-14, after the sketches were shown on request; exact sentences as shown): "i01, r1 survived, others failed". So the easier solver missed i01 and r1 and solved i02 and r2. i01 stays blocked by its strong-solver screen (3/3 right). r1 is filed as i03 word for word and goes to its own strong-solver screen before any write-up.

Write-ups (2026-10-14, after the user's quick test; the user chose to have survivors written up, as on aq-05049): i01 -> questions/q01.md rev 0, tested_sha256 dfdc826c...09db, checked, 0 FAIL / 7 WARN; i03 (r1) -> questions/q02.md rev 0, tested_sha256 919597bd...a846, checked, 0 FAIL / 5 WARN. Both local 3/3 (likely Too easy at High); hand-overs notes/handover-q01.md, handover-q02.md. Efficiency: promote refused (all five slots enrolled).

Platform results: q01 (i01) Run 1, Version c9917a: "Too easy", Low — · Medium — · High 3/3, refunded; q02 (i03 = r1) Run 2, Version 0aa132: "Too easy", Low — · Medium — · High 3/3, refunded; routes unread in both. Hooks h3 and h14 closed (no rewording). Every sketch now has a result: i01 and i03 Too easy at High, i02 and r2 failed the quick test. No other hook with a judgment step was found (caller, two independent authors, definition diff).

Superseded plan: i01 and i02 were to go to the quick test; under the playbook adopted mid-session both went to
the strong-solver screen instead and were rejected, so nothing reached the user's quick test (15 of 15 left).
Remaining judgment families: none found. A definition diff of the 2025 vs 2026 editions (2026-10-14) shows the
only change with numeric weight is the expense re-presentation (i02's step); non-GAAP and key-metric
definitions are identical. Untested playbook kinds looked at and not sketched: MD&A attributions ("primarily
due to ... partially offset by") and "we believe" hedges, both plainly worded and keyword-findable.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
