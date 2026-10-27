# aq-01960 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01960 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 838418ade3cf65ac55d44635e5d9df1524a3ddff5cafa60c89ef4902dc308221: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D13 = Doc 13, D14 = Doc 14.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
For its fiscal quarter ended June 30, 2026, by what percentage did KLA's non-GAAP gross profit exceed the gross profit implied by multiplying the midpoints of the revenue and non-GAAP gross margin guidance it gave for that quarter? Round to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
3.3%
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 13, fourth-quarter fiscal 2026 guidance): the guidance covers the fourth quarter of fiscal 2026 ending in June. Total revenues are expected at $3.575 billion +/- $200 million and non-GAAP gross margin at 61.75% +/- 1.00%, so the two midpoints are $3.575 billion and 61.75%.

Step 2. Calculation (from Step 1; Doc 13): converting to the thousands used in the financial statements, $3.575 billion = 3,575,000 thousand dollars.

Step 3. Calculation (from Steps 1 and 2; Doc 13): implied non-GAAP gross profit = 3,575,000 × 61.75% = 2,207,562.5 thousand dollars.

Step 4. Source fact (Doc 14, statement of operations, three months ended June 30, 2026, in thousands): total revenues 3,657,556 and costs of revenues 1,413,108.

Step 5. Source fact (Doc 14, pre-tax impact of GAAP to non-GAAP adjustments, three months ended June 30, 2026): costs of revenues include $36,200 thousand of acquisition-related charges and no restructuring charges. The quarter's other acquisition-related amounts, 8,470 in selling, general and administrative and (11,601) in other expense (income), net, sit below gross profit; with them the reconciliation's bundled total is 33,069.

Step 6. Calculation (from Step 4; Doc 14): GAAP gross profit = 3,657,556 - 1,413,108 = 2,244,448 thousand dollars.

Step 7. Calculation (from Steps 5 and 6; Doc 14): non-GAAP gross profit = 2,244,448 + 36,200 = 2,280,648 thousand dollars.

Step 8. Calculation (from Steps 3 and 7; Doc 13 and Doc 14): excess over the implied amount = 2,280,648 - 2,207,562.5 = 73,085.5 thousand dollars.

Step 9. Calculation (from Steps 3 and 8; Doc 13 and Doc 14): 73,085.5 / 2,207,562.5 = 3.3% (ratio expressed as a percentage, to one decimal place).
```

### Answer components

Component 1

```text
3.3%
```

### Evidence

Evidence 1: document Doc 13 (klac_ex991_2026-04-29.txt), proves component 1. 3.3% (local note: L38, Fourth Quarter Fiscal 2026 Guidance heading)

```text
The following details our guidance for the fourth quarter of fiscal 2026 ending in June
```

Evidence 2: document Doc 13 (klac_ex991_2026-04-29.txt), proves component 1. 3.3% (local note: L39, revenue guidance)

```text
Total revenues are expected to be in a range of $3.575 billion +/- $200 million
```

Evidence 3: document Doc 13 (klac_ex991_2026-04-29.txt), proves component 1. 3.3% (local note: L39, non-GAAP gross margin guidance)

```text
Non-GAAP gross margin is expected to be in a range of 61.75% +/- 1.00%
```

Evidence 4: document Doc 14 (klac_ex991_2026-07-28.txt), proves component 1. 3.3% (local note: L94, statement of operations columns)

```text
Three Months Ended June 30, Twelve Months Ended June 30,
```

Evidence 5: document Doc 14 (klac_ex991_2026-07-28.txt), proves component 1. 3.3% (local note: L101, statement of operations, first column = three months ended June 30, 2026)

```text
Total revenues 3,657,556 3,174,741 13,579,476 12,156,162
```

Evidence 6: document Doc 14 (klac_ex991_2026-07-28.txt), proves component 1. 3.3% (local note: L104, statement of operations)

```text
Costs of revenues 1,413,108 1,207,286 5,255,060 4,751,867
```

Evidence 7: document Doc 14 (klac_ex991_2026-07-28.txt), proves component 1. 3.3% (local note: L223-224, pre-tax impact table, three months ended June 30, 2026)

```text
Costs of revenues $ 36,200
```

### Necessary documents

- Tick Doc 13 (klac_ex991_2026-04-29.txt), role: Answer component
- Tick Doc 14 (klac_ex991_2026-07-28.txt), role: Answer component

Leave unticked: Doc 1 (klac_ex991_2023-04-26.txt), Doc 2 (klac_ex991_2023-07-27.txt), Doc 3 (klac_ex991_2023-10-25.txt), Doc 4 (klac_ex991_2024-01-25.txt), Doc 5 (klac_ex991_2024-04-25.txt), Doc 6 (klac_ex991_2024-07-24.txt), Doc 7 (klac_ex991_2024-10-30.txt), Doc 8 (klac_ex991_2025-01-30.txt), Doc 9 (klac_ex991_2025-04-30.txt), Doc 10 (klac_ex991_2025-07-31.txt), Doc 11 (klac_ex991_2025-10-29.txt), Doc 12 (klac_ex991_2026-01-29.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Unit normalization

Leave unticked: Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

Where the trap sits:

```text
Doc 14's reconciliation of GAAP to non-GAAP net income prints one bundled row for the June 2026 quarter, "Acquisition-related charges a 33,069". That total mixes three pieces that only the pre-tax impact table below it separates: $36,200 thousand in costs of revenues, $8,470 thousand in selling, general and administrative, and a $(11,601) thousand credit in other expense (income), net, which footnote a describes as "a discrete release of $11.6 million of interest on unrecognized tax positions".
```

The wrong answer a careless solver gives:

```text
3.2%. A solver who adds the bundled 33,069 to GAAP gross profit gets 2,244,448 + 33,069 = 2,277,517 thousand dollars of non-GAAP gross profit. Against the implied 2,207,562.5 thousand that is a ratio of 1.0317, so the excess rounds to 3.2% instead of 3.3%.
```

Why the correct answer avoids it:

```text
Gross profit is revenue minus costs of revenues, so only adjustments recorded in costs of revenues change it. The pre-tax impact table puts $36,200 thousand there and nothing from restructuring, while the SG&A amortization and the interest release sit below gross profit. Doc 13's guidance reconciliation treats the margin the same way, adding acquisition-related charges of 1.03% of revenue to GAAP gross margin. Adding 36,200 gives 2,280,648 thousand dollars and 3.3%.
```

(191 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

Where the trap sits:

```text
The release that reports the June 2026 quarter (Doc 14, dated July 28, 2026) prints its own guidance block, but for the next quarter: "The following details our guidance for the first quarter of fiscal 2027 ending in September", with total revenues of "$4.0 billion +/- $200 million" and non-GAAP gross margin of "62.5% +/- 1.0%". Doc 14's highlights say only that revenue was "above the midpoint of the guidance range" and never restate the June-quarter range.
```

The wrong answer a careless solver gives:

```text
-8.8%. A solver who takes the guidance printed beside the June-quarter results multiplies $4.0 billion by 62.5% to get an implied 2,500,000 thousand dollars, and 2,280,648 against 2,500,000 is a shortfall of 8.8%, so the answer comes out as -8.8% instead of a 3.3% excess.
```

Why the correct answer avoids it:

```text
The question asks for the guidance given for the June 2026 quarter itself, which was issued one release earlier. Doc 13 (April 29, 2026) states "our guidance for the fourth quarter of fiscal 2026 ending in June": $3.575 billion +/- $200 million of revenue and 61.75% +/- 1.00% non-GAAP gross margin. Their product is 2,207,562.5 thousand dollars, and the actual 2,280,648 thousand exceeds it by 3.3%.
```

(188 words across the three boxes; the form needs at least 150.)

#### Failure mode 3

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

Where the trap sits:

```text
Doc 14's statement of operations prints only GAAP lines for the June 2026 quarter, "Total revenues 3,657,556" and "Costs of revenues 1,413,108" in thousands, and no release in the bundle prints a non-GAAP gross profit or any actual gross margin percentage for any quarter. The GAAP gross profit is therefore the figure that sits ready on the page once revenue and costs are subtracted, while the guidance it is set against in Doc 13 is the non-GAAP gross margin of 61.75%, a measure that excludes some of those costs.
```

The wrong answer a careless solver gives:

```text
1.7%. Using GAAP gross profit, 3,657,556 - 1,413,108 = 2,244,448 thousand dollars, against the non-GAAP implied 2,207,562.5 thousand gives a ratio of 1.0167, an excess of 1.7%, about half the true figure.
```

Why the correct answer avoids it:

```text
The question compares like with like: non-GAAP gross profit against the non-GAAP gross margin guidance. KLA's non-GAAP measures exclude acquisition-related charges, and the pre-tax impact table in Doc 14 shows $36,200 thousand of them inside costs of revenues for the quarter. Adding that back to GAAP gross profit gives non-GAAP gross profit of 2,280,648 thousand dollars, which exceeds the guidance-implied 2,207,562.5 thousand by 3.3%.
```

(185 words across the three boxes; the form needs at least 150.)
