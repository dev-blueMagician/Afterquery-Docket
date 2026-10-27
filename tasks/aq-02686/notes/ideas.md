# aq-02686 - lean candidate sketches

Current target: medium, Hard welcome (user 2026-10-10: "there is no slot for Easy Tier for this bundle, we
should target medium and high"); measured platform success pending. Hooks are in notes/hooks.md. Origin of
every sketch here: claude (Claude Code, claude-opus-5-5). Round 2 of at most three; round 1 ended with q01 dropped (Easy at the difficulty check, then too easy at the quick test after its one repair).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | sketches/i01.md | h1: D04's FEOC tests decide which of three export prospects a recycler may ship to; D07 prices its SNUN ($45,496, large business) and its export notices (about $106 per country). Gold $45,708 | Competing answers and the wording each fails are in the sketch: $45,602 (seat count 40% for board voting power 20%, or the Shanghai parent's status carried to its Korean subsidiary), $45,814 (Polish firm kept), $212 (no SNUN), $82,708 (fee added twice). D07: costs and the 99% trigger, D07 only. D04: board-seat valuation (L138), D04 only; D02's text gives $45,602 | promoted to q01; screen passed 2026-10-10 with one depth warning (99% at character 26,471). Rev 0 said "Korean subsidiary"; a removal probe listed "Korean" read as North Korean (a covered nation, $45,496), so rev 1 names Indonesia. Optional diagnostics on rev 0: blind solve matched $45,708 (minimal documents D07, D04); removal probe without Doc 4 answered $45,602. q01 rev 1: platform Run 1 (Version bac61b) "In band — Easy tier", Low 3/5, below target (feedback-index F1). Rev 2 (2026-10-10): prospects replaced (Thai firm 15% province-owned, eligible; Polish firm 10% city-owned plus notes convertible into 20% more, a FEOC at 30%; Japanese firm with one province-picked director of seven who alone has two votes, a FEOC at 25% of board votes); gold $45,602. Blind solve on rev 2 matched $45,602 (minimal documents D07, D04) and named a strained reading of "20% more" as 12% in all, so rev 3 says "another 20%". q01 rev 3: form quick test "too easy" (user chat 2026-10-10, no panel). q01 dropped; hook closed in this form after Easy (rev 1) and too easy (rev 3) |
| i03 | this row | h1 documents, different dependency: a bill whose cells must be counted, not a filter. "Once EPA's 2026 significant-new-use proposal is final, a large recycler reclaims both covered oxides, one with 90%-efficient dust controls and one with 99%-efficient. Barring FEOCs, it exports both to two Japanese buyers and a Chilean one, and one to a Thai buyer 10% owned by a Chinese city holding notes convertible into another 20%. What would notifying EPA cost altogether?" (60 words). Gold $45,920 = one SNUN $45,496 (only the oxide reclaimed under 99% is a significant new use, D07 L320) + four export notices at about $106 (each oxide to Japan and to Chile: D07 L71, "vary by chemical, depending on ... the number of countries to which the chemical is exported"); the Thai buyer is a FEOC (contingent equity, D04 L138, L255) | Competing: $45,708 (two notices, countries only), $46,132 (six, per buyer), $46,026 (Thai buyer kept), $91,416 (two SNUNs), $424 (no SNUN). Risk: the per-chemical count rests on one sentence of D07; a solver may count one notice per country for both oxides. Necessity: D07 costs and counting rule; D04 contingent equity (D02: $46,026) | form quick test "survived" (user chat 2026-10-10, no panel); promoted to q02 rev 0 (1f910fbd56b1...): difficulty Run 2 (Version a9ec06) "Answer not supported", Low 2/5, the high model $46,026 three times (feedback-index F5). Every attempt completed each document step; the split was the phrase "Barring FEOCs". q02 rev 1 (1e00d4644a27...) states the policy as its own sentence; checked, quick test first |
| i02 | this row | h1, two prospects, FEOC spelled out. "Once EPA's 2026 significant-new-use proposal is final, a large recycler reclaims a covered oxide with 90%-efficient dust controls, exporting only to prospects that are not foreign entities of concern: a Chinese city's 50%-owned Polish firm, and a Japanese firm where a Chinese province picks two of five directors, casting 20% of board votes. What would notifying EPA cost it altogether?" Gold $45,602 (45,496 + 106) | Same evidence as i01 without the jurisdiction-subsidiary step. Competing: $45,496 (seat count 40%, no export; a printed figure, so a form "too vague" block is possible if both form solvers drop the Japanese firm), $45,708 (Polish firm kept). Necessity as i01 | retired 2026-10-10: it rests on the same printed "20% of board votes" that let three of five low attempts through in Run 1 |

Not sketched, with the reason (details in hooks.md):

- h2, the natural partner design (D04's FEOC tests deciding a section 30D credit total from D05's $7,500 /
  $3,750). D05's only unique inputs are the statutory credit amounts. The platform's document check answers
  once without each ticked document, and a model supplies those amounts from memory, so D05 would probably be
  judged not needed (workspace evidence: aq-00949 q07, aq-02147 q01). The same FEOC steps are used in q01 with
  D07's 2026 cost figures instead.
- h3 (60 days between the DOE and Treasury effective dates), h4 (15-day comment-window gap), h6 (funding
  ratio 240): one or two lookups and one operation on public dates or appropriations.
- h5 (proposal against final on CPPCC members): the proposal side has two defensible readings.
- h7, h8: small counts or two-way choices.

Design notes for q01 (author checks, not model validations):

- The FEOC condition is tied to a real statement in D04: BIL section 40207 has DOE "prioritize recycling
  applicants who will not export recovered critical materials to a FEOC" (L68).
- Scenario numbers were chosen from figures the ticked documents print (D07 "90 days"; D04 "50%", "20%") so
  the reasoning can state them; the form's number check accepts no scenario number a ticked document lacks.
- Count-based totals can hide offsetting errors, so the three prospects sit in three countries, one clear
  exclusion and two look-alike inclusions; only "Korea and Japan" gives two notices.
- Kept out on purpose: tiered minority chains (D04 L150 against scenario 3), the small-business SNUN cost
  (two printed values), the per-chemical multiplier (two substances share one generic name).

Ambiguity: competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

Run 1 reading (2026-10-10, rev 1, traces in verdicts/AQ-02686_difficulty_2026-10-10_1539.txt): every low attempt got
the SNUN trigger and cost, the per-country export notice, the plain 50% holding and the jurisdiction-only
subsidiary right. Two attempts counted seats (40%) and three took the question's printed 20% of board votes as
the control share; none cited Doc 4's comment response. Design consequence for rev 2: no printed share on the
deciding metric; two derived classifications that both need that comment response; the only eligible
prospect is a plain sub-threshold government holding so neither "all pass" nor "all fail" gives the gold.
If rev 2 is Easy again, candidates for a different hook are few (hooks.md h2-h8 are all weaker): say so.

Quick test of rev 3 (2026-10-10, user chat, no panel): too easy. Reading: derived shares that follow from
adding the question's own pieces do not stop the easier solver; with Run 1 this closes the filter-style
design on these documents. Round 2 keeps only i03, which moves the work from classifying buyers to counting
notices per chemical and country. Considered and not offered: the 30D credit bill (h2: closed-book and
document-check risks, both from how well known the credit rules are) and a signature-to-effective-date gap
(h3 variant, 78 days: a 60-day assumption from the publication date reaches it without the Treasury agenda).
If i03 is too easy as well: report that no fair Medium design was found and recommend release.

Quick test of i03 (2026-10-10, user chat "quick test survived", no panel): survived. One draw; it sets no tier. q02 is the write-up.

Run 2 reading (2026-10-10, q02 rev 0): the quick-test survival and Low 2/5 came from an ambiguous phrase of mine, not from the documents. With the phrase fixed (rev 1) nothing observed separates the solvers. If the quick test of rev 1 is too easy: report that no fair Medium design was found and recommend release (round 3 has no distinct hook).
