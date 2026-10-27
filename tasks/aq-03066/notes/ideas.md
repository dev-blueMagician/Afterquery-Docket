# aq-03066 - lean candidate sketches

Current target: medium (user, 2026-10-11: "there is no slot for Easy Tier for this bundle, we should target medium
and high"). Measured platform success pending; no quick test or difficulty run has been reported.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | sketches/i01.md -> questions/q01.md | h1: Commission's illustrative loss calculation rerun at Crown Fibre Holdings' 9% mid-point (D03 + D02) | One rate input used twice (return on qualifying RAB, discounting); wrong routes 2%, 4%, 10%, 24%; both documents single-source for their input | Quick test 2026-10-11: too easy (user chat, "both are too easy for quick test"; no panel pasted). q01 dropped |
| i02 | sketches/i02.md | h2: first-period write-off of the loss asset over the longest four-period span (D03 + D04) | Exact gold 257; wrong routes 385.5, 231.3; D04's rule can be rebuilt from D01 line 1103 plus D03 line 461 or recalled from the Act | Quick test 2026-10-11: too easy (same message). Dropped |

| i03 | sketches/i03.md | h8: quality dimensions backed by exactly two of Chorus, Spark, Vodafone (D08 + D07 + D01) | Gold ordering, provisioning, switching, faults; Spark's grouped clause decides every member; wrong routes availability + performance, provisioning + faults, all six | Quick test 2026-10-11: too easy (user chat, "both of them too easy to pass quick test"; no panel pasted). Dropped |
| i05 | sketches/i05.md | h8 as one total of backings (D01 + D08 + D07) | Gold 14; wrong totals 18, 8, 13, 15; "six" in the question makes it the more explicit sibling | Quick test 2026-10-11: too easy (same message). Dropped |
| i04 | this row | h9: Frontier's allocations where the emerging views propose no prescriptive rules at first (D08 + D04). Q: "Which of the four cost allocations Frontier rated for Vodafone fall where the Commission's May 2019 emerging views proposed no prescriptive allocation rules at first?" A: "Layer 1 vs Layer 2, and anchor vs other products" | Fair, two single-source inputs, but no careless route gives a definite wrong answer | Hold: optional quick test only |
| i06 | this row | h12: 16 submissions and expert reports less Vodafone's and Spark's (gold 11) | The pack never says attached reports were itemised in the 16 | Dropped, not offered |

Round 2 (2026-10-11): i03 and i05 both quick-test too easy. The easier solver resolves a grouped clause across
documents and a three-way membership; family h8 closed. 4 of 10 quick tests used; one sketch round remains.

Round 1 (2026-10-11): two sketches, both quick-test too easy. Family closed: a what-if or rerun on D03's
illustrative table with the rule or parameter named in the question, including the "rate used twice" and
"first period is three years" steps the easier solver was expected to miss. Round 2: two independent
question-author runs (rules/definitions; figures/conflicts), sketches i03-i06 reserved for their returns.

Closed without a sketch (notes/hooks.md): h3 deferral effect (deciding input in three documents), h4 Vodafone rate
(one scaling step), h5 quality-dimension diff, h6 date gaps, h7 section renumbering.

Ambiguity: competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
