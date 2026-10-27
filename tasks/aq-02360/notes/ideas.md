# aq-02360 - lean candidate sketches

Current target: medium (user, 2026-10-09: "there is no slot for Easy Tier for this bundle, we should target medium and
high. do your best."; page: Hard 0/2 · Medium 0/3 · Easy 0/1, 0 of 10 quick tests, 8 of 8 runs); hard where a design
supports it. Measured platform success pending. Origin of all sketches: claude (Opus 5.5).

Sources are byte-identical to tasks/aq-02102, aq-02165 and aq-02198; their closed families are listed in notes/hooks.md.
Quick test = one low-model attempt ("Too easy — solver got it" or survived), with "Harder variations" offered after a
result (screenshot tasks/aq-02102/notes/platform-feedback/q02-rev1-quick-test-2026-10-08.png).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [sketches/i01.md](sketches/i01.md) | m1: Pension Schemes Act 1993 subsection the transfer-payment rule cited from 1 April 2022: section 95(2) | 95(2A) fails "did ... cite" (Doc 2 L619 drops the draft). Doc 1 alone prints the subsection numbers; Doc 2 alone records the drop; Docs 3-5 silent (grep "95(", "142", "cross.refer") | quick test survived (user, 2026-10-09); promoted to q01 rev 0; rev 0 form check "Needs the documents" failed (95(2) guessable); rev 1-2 add regulation 142(4) to the gold (rev 2 order wording, ac260ba1...); rev 2 reported too easy (F6): redesign or retire |
| i02 | [sketches/i02.md](sketches/i02.md) | m2: days from the 2023 consultation's opening (Doc 4 only) to the last day for receiving opted-out elections (Doc 3 only, "before 30 September 2024"): 573 | 574 fails "last day" with "before"; 504/505 fail "opened"; 208 is Doc 4's retirement date. Each date single-source | quick test survived (user, 2026-10-09); promoted to q02 rev 0; user paraphrase measured Between levels (Low 0/5, Medium 4/5, F5); rev 1 anchors on the last union meeting (4 May 2023): 514 days, checked, tested_sha256 a1fc3019...; platform pending |
| m3-m6 | [hooks.md](hooks.md) | contribution cliff, response-to-consultation gap, PCS membership, final 2023 rules | recall, closed family, plain bridge or one-document final | rejected / parked |

i01 differs from aq-02198 i01 (never tested): that wording named "regulation 142(4)", tying the trap to the sentence
that defeats it; this one describes the rule by function and dates it to the draft's own commencement.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
