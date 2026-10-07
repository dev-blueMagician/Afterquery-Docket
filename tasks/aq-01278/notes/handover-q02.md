# aq-01278 q02 hand-over

Generated 2026-10-07 by `python tools/check_questions.py tasks/aq-01278 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 4, difficulty_target medium, origin claude.
- tested_sha256 f8d502af3abf9790a43a7a1b8c0be58613a857813b7af5921d0b1a8ad2ccaa40: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D04 = Doc 4, D05 = Doc 9.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Chubb said its North American commercial insurance net premiums written grew 2.8% from a year earlier in the quarter ended March 31, 2026. For the same business lines behind that 2.8%, what was the percentage change in net premiums written in the quarter ended June 30, 2026 from a year earlier? Give the sign, to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
-1.3%
```

### Step-by-step reasoning

```text
Step 1. Doc 4 (highlights): "North America was up 4.1%, including growth of 8.3% in personal insurance and 2.8% in commercial insurance", and "All comparisons are with the same period last year unless otherwise specifically stated." The North America table comprises NA Commercial P&C Insurance, NA Personal P&C Insurance and NA Agricultural Insurance.
Step 2. Doc 4 (North America table, net premiums written, 2026 vs 2025): Total North America P&C 6,887 and 6,615; North America Personal 1,681 and 1,552. 6,887 - 1,681 = 5,206
Step 3. Doc 4: 6,615 - 1,552 = 5,063
Step 4. Doc 4: 5,206 - 5,063 = 143
Step 5. Doc 4: 143 / 5,063 = 2.8%, the stated growth, so the 2.8% covers the North American business lines other than personal insurance.
Step 6. Doc 4: the North America Commercial P&C Insurance segment alone (4,895 against 4,787) grew only 2.3%; adding North America Agricultural Insurance gives 4,895 + 311 = 5,206, so the business lines behind the 2.8% are North America Commercial P&C Insurance and North America Agricultural Insurance.
Step 7. Doc 9 (North America table, quarter ended June 30, 2026 vs 2025): North America Commercial P&C Insurance 5,594 and 5,723; North America Agricultural Insurance 776 and 733. 5,594 + 776 = 6,370
Step 8. Doc 9: 5,723 + 733 = 6,456
Step 9. Doc 9: 6,370 - 6,456 = -86
Step 10. Doc 9: -86 / 6,456 = -1.3% (to one decimal place)
Step 11. Doc 9 and Doc 4: the second-quarter release's "North America Commercial was down 2.3%" covers the commercial segment without agriculture, the business line that grew 2.3% rather than 2.8% in the first quarter, so it leaves out one of the business lines behind the 2.8%.
```

### Answer components

Component 1

```text
-1.3%
```

### Evidence

Evidence 1: document Doc 4 (cb_ex991_2026-04-21.txt), proves component 1. -1.3% (local note: Doc 4, p. 1 highlights)

```text
North America was up 4.1%, including growth of 8.3% in personal insurance and 2.8% in commercial insurance
```

Evidence 2: document Doc 4 (cb_ex991_2026-04-21.txt), proves component 1. -1.3% (local note: Doc 4, North America table)

```text
(Comprising NA Commercial P&C Insurance, NA Personal P&C Insurance and NA Agricultural Insurance)
```

Evidence 3: document Doc 4 (cb_ex991_2026-04-21.txt), proves component 1. -1.3% (local note: Doc 4, p. 6)

```text
All comparisons are with the same period last year unless otherwise specifically stated.
```

Evidence 4: document Doc 4 (cb_ex991_2026-04-21.txt), proves component 1. -1.3% (local note: Doc 4, Total North America P&C Insurance)

```text
Net premiums written ||$| |---|---| ||6,887| ||$| |---|---| ||6,615|
```

Evidence 5: document Doc 4 (cb_ex991_2026-04-21.txt), proves component 1. -1.3% (local note: Doc 4, North America Personal P&C Insurance)

```text
North America Personal P&C Insurance Net premiums written ||$| |---|---| ||1,681| ||$| |---|---| ||1,552|
```

Evidence 6: document Doc 4 (cb_ex991_2026-04-21.txt), proves component 1. -1.3% (local note: Doc 4, North America Commercial P&C Insurance)

```text
North America Commercial P&C Insurance Net premiums written ||$| |---|---| ||4,895| ||$| |---|---| ||4,787| 2.3%
```

Evidence 7: document Doc 4 (cb_ex991_2026-04-21.txt), proves component 1. -1.3% (local note: Doc 4, North America Agricultural Insurance)

```text
North America Agricultural Insurance Net premiums written ||$| |---|---| ||311| ||$| |---|---| ||276| 12.7%
```

Evidence 8: document Doc 9 (cb_ex991_2026-07-21.txt), proves component 1. -1.3% (local note: Doc 9, North America Commercial P&C Insurance)

```text
North America Commercial P&C Insurance Net premiums written (increase of 4.1% excluding large account and E&S property) ||$| |---|---| ||5,594| ||$| |---|---| ||5,723| (2.3)%
```

Evidence 9: document Doc 9 (cb_ex991_2026-07-21.txt), proves component 1. -1.3% (local note: Doc 9, North America Agricultural Insurance)

```text
North America Agricultural Insurance Net premiums written ||$| |---|---| ||776| ||$| |---|---| ||733| 6.0%
```

Evidence 10: document Doc 9 (cb_ex991_2026-07-21.txt), proves component 1. -1.3% (local note: Doc 9, highlights)

```text
North America Commercial was down 2.3%.
```

### Necessary documents

- Tick Doc 4 (cb_ex991_2026-04-21.txt), role: Answer component
- Tick Doc 9 (cb_ex991_2026-07-21.txt), role: Answer component

Leave unticked: Doc 1 (pgr_ex991_2026-04-15.txt), Doc 2 (trv_ex991_2026-04-16.txt), Doc 3 (trv_ex992_2026-04-16.txt), Doc 5 (all_ex991_2026-04-29.txt), Doc 6 (all_ex992_2026-04-29.txt), Doc 7 (pgr_ex991_2026-07-15.txt), Doc 8 (trv_ex991_2026-07-17.txt), Doc 10 (all_ex991_2026-08-05.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Entity resolution, Aggregation

Leave unticked: Unit normalization, Conditional filter

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Misapplies a rule or premise

Where the trap sits:

```text
Doc 9, Chubb's release for the quarter ended June 30, 2026, prints the answer-shaped -2.3% three times under look-alike commercial labels: the highlights bullet "North America Commercial was down 2.3%.", Evan Greenberg's comment "North America was up about 0.5%, with commercial down 2.3%, while personal lines and agriculture each grew 6%", and the North America Commercial P&C Insurance row of its North America table (5,594 against 5,723, (2.3)%). That segment is only one of the two business lines behind the first-quarter figure. In Doc 4, the 2.8% growth "in commercial insurance" in the highlights is not this segment alone: Doc 4's segment commentary gives North America Commercial P&C Insurance growth of 2.3%.
```

The wrong answer a careless solver gives:

```text
-2.3%. The solver reads "North American commercial insurance" in the question, looks in the second-quarter release for commercial premiums, and takes Chubb's printed "North America Commercial was down 2.3%" as the same measure as the first quarter's 2.8%, without checking which business lines the 2.8% covered. In the platform's difficulty check (Run 2), nine of the ten solver attempts answered -2.3 in some form.
```

Why the correct answer avoids it:

```text
A careful reader first rebuilds the 2.8% from Doc 4's North America table. North America Commercial P&C Insurance alone grew from 4,787 to 4,895, only 2.3%. Adding North America Agricultural Insurance (276 to 311) gives 5,063 to 5,206, which is 2.8%, the same as total North America minus personal lines. So the business lines behind the 2.8% are commercial P&C plus agriculture. In Doc 9 those two rows sum to 5,594 + 776 = 6,370 against 5,723 + 733 = 6,456 a year earlier, a change of -86 / 6,456 = -1.3%. Chubb's -2.3% leaves out agriculture, which grew 6.0%.
```

(276 words across the three boxes; the form needs at least 150.)
