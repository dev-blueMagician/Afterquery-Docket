# aq-02631 - lean candidate sketches

Current target: medium (hard welcome); the user says this bundle has no Easy slot. Measured platform
success pending for every candidate. Hooks: notes/hooks.md. Writer: Claude Code (claude-opus-5-5), origin
claude. No local model solves were run; a clean sketch screen proves structure and quotes only.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | h1: the T. Rowe Price proposal as it stood when the SEC instituted proceedings (January 28, 2026, dated only in D07) against Bitwise 10's June 30, 2025 weights; gold 0.35% (SUI) | Competing 0% (D07's amended list, April 21, 2026) fails the event condition; 10.16% fails "eligible assets in T. Rowe Price's ... proposal". D06 unique for the pending list; D04 or D05 for the weights; D07 not necessary. Screen clean, no number warnings | Promoted to q01 rev 0. Difficulty Run 1 (Version 45cf69): Too easy, Low 5/5; every attempt dated the event and chose the original filing. Dropped 2026-10-10; no repair keeps the hook |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: launch minimum pending at the same event (100,000 Shares, D06) over Hashdex's 40,000 (D02); gold 2.5 times | Competing 0.25 (D07's 10,000) fails the event; 2 (D02's 50,000 continued-listing floor) fails "at launch". D06 and D02 each unique. Screen clean with two depth warnings (100,000 and 40,000 sit past character 20,000) | Quick test 2026-10-10: too easy (user chat). Dropped with q01's mechanism |
| i03 | [sketches/i03.md](sketches/i03.md) | h11: days between the staff approval of Bitwise 10 (July 22, 2025) and the earliest day needing no good-cause finding (30th day after the amendment's July 23, 2025 publication, a date only D05 prints); gold 31 days | Competing 26 (July 18 release date, the only amendment date D04 has), 33 (D04's own FR date), 25 (filing date) each use a date that is not the amendment's publication. D05 unique for July 23, 2025; D04 unique for the stated standard, but the 30-day rule is statutory. Screen clean, no number warnings | Quick test 2026-10-10: too easy (user chat). Dropped: a two-lookup date gap, as measured on earlier bundles |
| i11 | [sketches/i11.md](sketches/i11.md) | h12: Solana's weight under the Hashdex sponsor's Rule 5712 method at December 31, 2024 index weights (4.13, derived) against Bitwise 10's June 30, 2025 Solana weight (3.03); gold 1.10 percentage points | Competing 1.75 (printed 4.78) fails "method for complying"; 0.70 and the CME-based 1.75 fail "constituents whose futures markets Nasdaq's filing cites"; 1.85 drops Cardano and Uniswap from the capped group. D02 unique for weights, method and cited markets; D05 or D04 for 3.03. Screen clean with depth warnings | Promoted to q02 rev 0; quick test 2026-10-10: too easy (user chat). One focused repair, rev 1 (checked, bb40ae5c...): the named method and eligibility test are out of the question, which asks for the weight "under the strategy as Nasdaq filed it". Platform quick test pending |
| i21 | [sketches/i21.md](sketches/i21.md) | h13: date a portfolio held at the Hashdex index's December 31, 2024 weights would first meet Rule 5712's 90% test; gold March 18, 2025 (CME Solana futures, dated only in the T. Rowe Price filing) | Competing May 20, 2025 (XRP) fails "first"; September 18, 2025 carries NYSE Arca's six-month criterion into Nasdaq's rule; an immediate answer fails "held at the index weights". Same date under either reading of the covered set. D02 unique for rule and weights; D06 unique for the launch date. Screen clean | Promoted to q03 rev 0 (0bcf30b3...). Difficulty Run 2 (Version 45cf7c): In band, Easy tier, Low 2/5; below target, no Easy slot per the user. All five attempts had the reasoning; three used a recalled launch date (March 17, 2025) instead of Doc 6's |

Sketch round 1 (2026-10-10): i01 promoted, i02 and i03 held for the platform quick test. The independent author (other families) returned i11, now q02, and a
weak fallback (137 days, hooks.md) that was not sketched.

Sketch round 2 (2026-10-10), after q01's Too easy and three quick-test failures: q02 rev 1 (the one repair of
q02) and i21 -> q03 (new hook). The attempts on q01 show the low model dates events and compares versions
without help, so round 2 leaves the deciding rule or the deciding document out of the question instead.
If both fail, round 3 has no untested fair mechanism left in this bundle (hooks.md): report that.

Outcome of round 2 (2026-10-10): q03 measured Easy (Low 2/5). q02 rev 1: no platform result reported. Across both
difficulty runs every low attempt that read the deciding passage answered correctly (q01 5 of 5; q03 2 of 2), so no
recorded hook contains a step such an attempt gets wrong. No round 3 sketch is proposed; recommendation: release the
bundle, or submit q03 if an Easy slot opens.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes searched
-> what is lost without it. Recheck the dependency after every clarification.
