# Current bundle checkpoint

- Goal: user 2026-10-06 "work on AQ-01428 ... difficulty_target to at least medium". Page: Hard 0/2, Medium 0/3, Easy 0/1 slots; 9 submissions; 8 difficulty runs; 10 quick tests.
- Target / measured tier: medium / pending.
- Bundle: complete capture, 4/4 docs, no gaps. D01 = Doc 2 (Eni Q1, Apr 24), D02 = Doc 1 (Eni Q2/H1, Jul 29), D03 = Doc 4 (Oxy Q1), D04 = Doc 3 (Oxy Q2). Form fields cite Doc N.
- Phase: handed over rev 2 (awaiting form check / quick test / difficulty check).
- Platform so far: q01 rev 1 wording (+ stray "two decimal places" sentence from q02) was BLOCKED by the form's model check: "too vague to submit ... Both answered €1.40 billion" (Feedback log in q01.md). No quick test or difficulty run used.
- q01 rev 2 checked (primary): "During the month in which Eni secured ten years of regasification capacity at Ravenna, what full-year 2026 proforma adjusted EBIT did the guidance then in force expect from its Global Gas & LNG Portfolio business? Give it in € billion to one decimal place." -> €1.3 billion. tested_sha256 5956339a...; A/B match, closed-book €1.0 (miss), audit clear, review ready medium (marginal): form block ~10%, Too easy ~17%, Easy ~37%, Medium ~23%, High ~4%; Doc 1 flag ~15%; first-run Medium+ ~23%, Easy+ ~55%.
- q02 rev 0 checked (fallback, Easy-leaning, robust necessity): H2 adjusted CFFO needed vs guidance in place at end-June -> €6.45 bln.
- Next: user pastes rev 2 exactly (no extra sentence, gold "€1.3 billion", re-derive reasoning), runs the full checks (form block must clear), then a quick test; difficulty check only if the low model misses. If the quick test says Too easy, revisit (e.g. a segment-identification step) before spending a run.
- Lessons saved (memory + gpt-project): two-edition removal risk; half-year prior; form "too vague" block on soft anchors.
