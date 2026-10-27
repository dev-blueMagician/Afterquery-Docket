# aq-02673 - lean candidate sketches

Current target: medium (hard welcome); measured platform success pending. User, 2026-10-10: "there is no
slot for Easy Tier for this bundle, we should target medium and high. do your best." (The capture's page
line reads "Hard 0/2 · Medium 0/3 · Easy 0/1"; the user's instruction governs.)

Hooks are in notes/hooks.md. The fair cross-document surface is the quota proposal and its final rule
(D03, D06); D06 reprints most of D03, so a D03 input counts only when no other text prints it.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | sketches/i01.md | h1: share of the 2025 swordfish TAC that was U.S. underharvest not carried into 2026, 18.7% | Competing 14.0 (no dw-to-ww conversion), 19.1 (Table 1's 2025 column holds the 2024 shortfall), 22.6 (carried part not removed), 4.0 (the carried part): each fails a stated condition or the weight basis D03 prints. D03 -> TAC 14,769 (only there); D06 -> 2,514.9 and 440.6 (only there). Screen passed 2026-10-10. | promoted to q01 rev 0 (22 words); floor 0 FAIL / 1 WARN (origin); hand-over generated; platform pending. Closed-book diagnostic recalled the public TAC 14,769 (hedged, beside 13,200): the form's "Needs two or more documents" check may say Doc 3 is not needed (stated risk). |
| i02 | sketches/i02.md | h3: U.S. quota at 26 percent of the lowest possible swordfish TAC as a percentage of 2025 U.S. landings, 146% | Competing 194 (whole weight over dressed weight), 149 (exact 3,907/14,769 share; the question fixes 26 percent, D03's own multiplier), 540 (printed maximum quota). D03 -> lowest TAC 4,764 mt ww (only there; D06 keeps only the maximum); D06 -> landings 637.7 mt dw. Screen passed 2026-10-10. | promoted to q02 rev 0 (31 words, "total allowable catch" spelled out); floor 0 FAIL / 1 WARN (origin); hand-over generated; platform pending. Same family as q01 (shares D06's landings sentence and the 1.33 factor, not the TAC figure). Closed-book diagnostic: neither input recalled. Risk: D03's worked highest-TAC case (x 0.26, both weights) is a template for the solver. |
| i03 | this row | h2: adjusted 2026 swordfish quota as a share of the TAC, 30.4% (3,378.2 x 1.33 / 14,769) | Competing 26 (D03's printed "approximately 26 percent", the baseline share), 22.9 (no conversion). Same inputs as q01 with one step fewer. | dropped 2026-10-10: D03 alone prints 3,378.2 (its Alternative A1 "maximum adjusted quota"), so D06 is not needed |
| i04 | this row | h4: days from the proposal's June 8, 2026 comment deadline to the final rule's August 19, 2026 effective date, 72 | D06 itself says the comment period "closed on June 6, 2026" (74 days); the question must say the deadline the proposal set. D03 -> June 8; D06 -> August 19. | quick-test only (a date gap of this shape was too easy on aq-02501) |
| i05 | this row | h5: change in Atlantic Tunas General plus Swordfish General Commercial permits, December 2023 to 2025: 2,420 + 616 - 3,471 = -435 | D02 prints the two permit types as one count; D03 and D06 print them apart. Competing -1,051 (2,420 alone). D02 -> 3,471; D03 or D06 -> 2,420 and 616. | quick-test only |
| i06 | this row | h3 with one more step: the maximum adjusted quota (26 percent of the lowest TAC plus the 15 percent carryover) over 2025 U.S. landings, 168% (1,238.64 x 1.15 / 848.141) | "Maximum adjusted U.S. quota" is D03's own term, worked for the highest TAC only (3,963.0 mt dw, the same-label printed figure: 621%). Missed carryover gives q02's 146; no conversion 223. Same documents and inputs as q02 plus the 15 percent rule (both documents). | promoted to q03 rev 0 (33 words); floor 0 FAIL / 2 WARN (origin; sibling wording shared with q02, intended); hand-over generated; q02's harder variant, never both submitted |
| i07 | hooks.md h10 (independent author's sketch, re-verified by the caller) | h10: rise in the U.S. allocation out of the western Atlantic bluefin TAC, 2025 to 2026, 168.84 mt | Competing 193.84 (baseline pair, drops 2025's 25 mt, which D03 says came out of the western TAC), 231.34 (total pair, keeps 2026's 62.5 mt, which D03 and D06 say is eastern-derived), 447.34 (adjusted rows; the lead clause excludes them). D06 -> 1,316.14 and the 25 mt (only there); D03 -> the earlier allocation's western origin (only there). Closed-book diagnostic: 174.24 (miss), but both deciding facts were recalled. | q04 rev 0 (33 words): difficulty Run 1 "Too hard", Low 0/5 · Medium 0/5 · High 0/5, all 15 attempts 193.84, "may be too vague" (the counting rule was only in D03). Rev 1 (37 words) adds "counting any longline bycatch allocation drawn from that TAC"; floor 0 FAIL / 3 WARN (origin; two operands past character 20,000); hand-over regenerated. Rev 1 quick test: too easy (user report, 15:43, no capture). Rev 2 (31 words) replaces the clause with "in total"; q05 (36 words) is the same question with "whatever fishery the tonnage was reserved for". Both checked, floor 0 FAIL; quick test pending. Order of hints: rev 0 none (too hard) < q04 rev 2 "in total" < q05 "reserved for" < rev 1 explicit clause (too easy). Take the more explicit survivor to the difficulty check; if neither survives, or it is too hard again, retire the hook. Measured 2026-10-10: q04 rev 2 ("in total") Run 2 "Between levels", Low 0/5 · Medium 0/5 · High 4/5, dropped; q05 ("reserved for") Run 3 "In band — Medium tier", Low 0/5 · Medium 1/5, Document check both documents needed: q05 ready, submit. |

Alternate added 2026-10-10 after q04's runs: q06 = q01 plus the scope phrase "both on the same weight basis" (28
words, gold 18.7%, same fields), because q01's deciding condition (catch limit in whole weight, underharvest in
dressed weight) sits only in the documents, as q04 rev 0's did. Quick-test q01 and q06 together; take q06 to the
difficulty check if it survives, else q01; one of the two at most.

Rejected before sketching (hooks.md h6-h9): the bluefin revenue-per-permit differences between proposal and
final rule (two lookups and a subtraction; D03's own totals are internally inconsistent); bluefin quota over
TAC (the set-aside comes from another TAC; operands past character 20,000); bluefin carryover cap (the two
documents give different bases); the logbook proposal and shark permits (yes/no, or numbers the documents
never connect). Unrelated documents (D01, D04, D05, D07): mapper found no cross-document relationship beyond
a shared citation of the 2026 halibut annual measures (D04 Area 2A troll allocation, D07 Alaska vessel caps),
which joins no rule to any instance.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
