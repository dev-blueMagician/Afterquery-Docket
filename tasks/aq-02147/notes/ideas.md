# aq-02147 - lean candidate sketches

Current target: medium (hard where the design supports it); user 2026-10-08 "there is no slot for
Easy Tier for this bundle, we should target medium and high. do your best." Measured platform
success pending. Choose hooks from notes/hooks.md and draft from shorthand facts, then reopen sources
to verify premises, exact names, terms, periods and units. Keep at most two active sketches.

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i01 | [i01](sketches/i01.md) | h1 | Readings: April 2025 flat rate (week 9) excluded by "Using the 2024 sick-pay consultation's figures"; employers' median (week 2) excluded by "employee respondents"; continuous crossing 11.58 weeks still falls in week 12 because the question asks for the week. Necessity: Doc 5 is the only source of 90%; Doc 3 or Doc 4 (same £123 five-day profile, flat rate, waiting days) grouped as alternatives | promoted to q01, origin claude, target medium; DROPPED 2026-10-08 after Run 1 (necessity: Doc 4 replaced Doc 3; Low 2/5), see feedback-index F1/F2 |
| i02 | [i02](sketches/i02.md) | h2 | Readings: employees' median gives "never" (flat rate) and is excluded by "employers'"; Doc 4's 80% statement ("always notionally better off") is a different rate; week 3 holds at £116.75 and £118.75. Necessity: Doc 4 is the only source of the £175 five-day case; Doc 5 the only source of 50% | promoted to q02, origin claude, target medium; same family as q01, so offered as the easier sibling |
| i03 | [i03](sketches/i03.md) | h9 | Readings: Doc 3's average £30,614 fails "median"; the annex's component medians (£5,000, £3,100) and Table 4's individual £4,100 fail "saving per retained employee"; the £1.07bn total and Doc 5's £30m gap fail "rise over current SSP costs". Necessity: Doc 2 is the only median saving, Doc 3 the only current-system cost; Doc 5 not needed (80% stated) | promoted to q03, origin claude, target medium; replacement for q01; DROPPED 2026-10-08 after the quick test "Too easy — solver got it" (F3) |

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.

Independent check (2026-10-08, scratchpad breakeven.py, Decimal): the cumulative model reproduces Doc 3
Table 1's 2/3/4 weeks and both of Doc 4's case-study tables to the pound before any candidate is computed.
