# aq-00949 q08 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-00949 --handover --q q08` from questions/q08.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 71912869ab61d6e220623cf1853bae7898a608dbdcac564ea9a0ac010148eb4a: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 1, D07 = Doc 7.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN points-or-percent: comparing a rate: say 'percentage points' or 'percent (relative)'
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Holding EOG's stockholders' equity at its June 30, 2026 level, how much additional net debt would have lifted its net debt-to-total capitalization ratio to the December 31, 2019 ratio computed from that date's reported net debt and stockholders' equity? Answer in millions of dollars, rounding only the final result to the nearest million.
```

### Number of asks

1 ask

### Gold answer

```text
$1,615 million
```

### Step-by-step reasoning

```text
Step 1. Doc 1: at December 31, 2019, EOG reported net debt of 3,147 and total stockholders' equity of 21,641 (millions of dollars), so its net debt-to-total capitalization ratio was 3,147 / 24,788 = 12.6957%, where 24,788 is total capitalization (non-GAAP), equity plus net debt. The release rounds this ratio to 13 percent; the question asks for the ratio computed from the reported amounts.
Step 2. Doc 1: that ratio stays the same whenever net debt keeps the same proportion to stockholders' equity, and at December 31, 2019 that proportion was 3,147 / 21,641 = 0.1454184.
Step 3. Doc 7: at June 30, 2026, EOG reported total stockholders' equity of 31,864 and net debt of 3,019 (millions of dollars), a net debt-to-total capitalization ratio of 8.7%.
Step 4. Doc 1 and Doc 7: with equity held at 31,864, the net debt that restores that proportion is 31,864 × 0.1454184 = 4,633.61.
Step 5. Doc 1 and Doc 7: the additional net debt is 4,633.61 - 3,019 = 1,615 million dollars, rounded to the nearest million only at this step.
Decoy. Doc 1 and Doc 7: Doc 7's total capitalization (non-GAAP) of 34,883 already includes the June 30, 2026 net debt; applying the end-2019 ratio to that figure holds total capitalization fixed, which would need equity to fall as net debt rises, so it understates the additional net debt.
```

### Answer components

Component 1

```text
$1,615 million
```

### Evidence

Evidence 1: document Doc 1 (eog_ex991_2020-03-16.txt), proves component 1. $1,615 million (local note: lines 155-157, net debt table date)

```text
At December 31, 2019
```

Evidence 2: document Doc 1 (eog_ex991_2020-03-16.txt), proves component 1. $1,615 million (local note: lines 159-163, December 31, 2019 equity)

```text
Total Stockholders' Equity - (a) $ 21,641
```

Evidence 3: document Doc 1 (eog_ex991_2020-03-16.txt), proves component 1. $1,615 million (local note: lines 175-177, December 31, 2019 net debt)

```text
Net Debt (Non-GAAP) - (c) 3,147
```

Evidence 4: document Doc 1 (eog_ex991_2020-03-16.txt), proves component 1. $1,615 million (local note: lines 185-189, December 31, 2019 total capitalization)

```text
Total Capitalization (Non-GAAP) - (a) + (c) $ 24,788
```

Evidence 5: document Doc 7 (eog_ex991_2026-08-04.txt), proves component 1. $1,615 million (local note: line 829, net debt table header)

```text
June 30, 2026 March 31, 2026 December 31, 2025 September 30, 2025 June 30, 2025
```

Evidence 6: document Doc 7 (eog_ex991_2026-08-04.txt), proves component 1. $1,615 million (local note: line 833, June 30, 2026 equity)

```text
Total Stockholders' Equity - (a) 31,864
```

Evidence 7: document Doc 7 (eog_ex991_2026-08-04.txt), proves component 1. $1,615 million (local note: line 836, June 30, 2026 net debt)

```text
Net Debt (Non-GAAP) - (c) 3,019
```

### Necessary documents

- Tick Doc 1 (eog_ex991_2020-03-16.txt), role: Answer component
- Tick Doc 7 (eog_ex991_2026-08-04.txt), role: Answer component

Leave unticked: Doc 2 (eog_ex991_2025-05-01.txt), Doc 3 (eog_ex991_2025-05-30.txt), Doc 4 (eog_ex991_2025-08-07.txt), Doc 5 (eog_ex991_2025-11-06.txt), Doc 6 (eog_ex991_2026-05-05.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Figure that must be computed

How a careless solver fails: Misapplies a rule or premise

Where the trap sits:

```text
Doc 7's net debt-to-total capitalization table for June 30, 2026 prints net debt of 3,019 and, two rows below it, "Total Capitalization (Non-GAAP) - (a) + (c)" of 34,883, with the ratio 8.7%. Doc 1's table for December 31, 2019 prints the matching components (equity 21,641, net debt 3,147, total capitalization 24,788) and a ratio rounded to 13%. No document prints the net debt the question asks for. The ready-made 34,883 is printed two rows above the ratio rows, so it looks like the base to apply the 2019 ratio to.
```

The wrong answer a careless solver gives:

```text
$1,410 million. The solver computes the 2019 ratio, 3,147 / 24,788 = 12.6957%, multiplies it by the printed total capitalization, 34,883 × 12.6957% = 4,428.6, and subtracts the current net debt of 3,019 to get 1,409.6, or $1,410 million. That treats total capitalization as fixed, so it assumes the added net debt comes with an equal fall in equity.
```

Why the correct answer avoids it:

```text
The question holds stockholders' equity at 31,864, so every dollar of added net debt also raises total capitalization. A careful reader solves N / (31,864 + N) = 3,147 / 24,788, which holds exactly when N / 31,864 = 3,147 / 21,641, the net debt-to-equity proportion at December 31, 2019. That gives N = 31,864 × 0.1454184 = 4,633.61, so the additional net debt is 4,633.61 - 3,019 = 1,614.61, or $1,615 million. As a check, 4,633.61 / 36,497.61 = 12.6957%, the 2019 ratio. The shortcut's 4,428.6 would leave the ratio at 4,428.6 / 36,292.6 = 12.20%, short of the target.
```

(251 words across the three boxes; the form needs at least 150.)
