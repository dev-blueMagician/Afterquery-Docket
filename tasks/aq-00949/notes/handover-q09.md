# aq-00949 q09 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-00949 --handover --q q09` from questions/q09.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 3d35521f66376bdd40548b7bcaa04d06405eec5d4f383a17f00eb7131873a18b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D03 = Doc 3, D07 = Doc 7.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By how much did EOG's net debt increase from June 30, 2025 to June 30, 2026 in excess of the debt EOG said it expected to use to fund the Encino acquisition? Answer in millions of dollars.
```

### Number of asks

1 ask

### Gold answer

```text
$499 million
```

### Step-by-step reasoning

```text
Step 1. Doc 3 (May 30, 2025): EOG said it "currently expects to fund the acquisition through $3.5 billion of debt and $2.1 billion of cash on hand", so the debt it expected to use was $3.5 billion = 3,500 million dollars.
Step 2. Doc 7: the net debt table shows net debt (non-GAAP) of (980) at June 30, 2025, a negative amount because cash of 5,216 exceeded debt of 4,236, and net debt of 3,019 at June 30, 2026 (millions of dollars).
Step 3. Doc 7: moving from net cash of 980 to net debt of 3,019, net debt rose by 3,019 + 980 = 3,999 million dollars.
Step 4. Doc 3 and Doc 7: the rise in excess of the expected debt is 3,999 - 3,500 = 499 million dollars.
Decoy. Doc 7: reading (980) as a positive net debt of 980 understates the rise and makes the answer negative; the 3Q 2025 long-term debt borrowings of 3,472 are what EOG borrowed, not the debt it said it expected to use.
```

### Answer components

Component 1

```text
$499 million
```

### Evidence

Evidence 1: document Doc 3 (eog_ex991_2025-05-30.txt), proves component 1. $499 million (local note: line 13, release date)

```text
May 30, 2025
```

Evidence 2: document Doc 3 (eog_ex991_2025-05-30.txt), proves component 1. $499 million (local note: line 19, funding plan)

```text
EOG currently expects to fund the acquisition through $3.5 billion of debt and $2.1 billion of cash on hand
```

Evidence 3: document Doc 7 (eog_ex991_2026-08-04.txt), proves component 1. $499 million (local note: line 829, net debt table header)

```text
June 30, 2026 March 31, 2026 December 31, 2025 September 30, 2025 June 30, 2025
```

Evidence 4: document Doc 7 (eog_ex991_2026-08-04.txt), proves component 1. $499 million (local note: line 834, debt row)

```text
Current and Long-Term Debt (GAAP) - (b) 7,926 7,931 7,936 7,694 4,236
```

Evidence 5: document Doc 7 (eog_ex991_2026-08-04.txt), proves component 1. $499 million (local note: line 835, cash row)

```text
Less: Cash (4,907) (3,849) (3,396) (3,530) (5,216)
```

Evidence 6: document Doc 7 (eog_ex991_2026-08-04.txt), proves component 1. $499 million (local note: line 836, net debt row)

```text
Net Debt (Non-GAAP) - (c) 3,019 4,082 4,540 4,164 (980)
```

### Necessary documents

- Tick Doc 3 (eog_ex991_2025-05-30.txt), role: Answer component
- Tick Doc 7 (eog_ex991_2026-08-04.txt), role: Answer component

Leave unticked: Doc 1 (eog_ex991_2020-03-16.txt), Doc 2 (eog_ex991_2025-05-01.txt), Doc 4 (eog_ex991_2025-08-07.txt), Doc 5 (eog_ex991_2025-11-06.txt), Doc 6 (eog_ex991_2026-05-05.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Rounding, scale or sign

Where the trap sits:

```text
Doc 7's net debt-to-total capitalization table prints net debt for June 30, 2025 as "(980)". At that date EOG's cash of 5,216 exceeded its debt of 4,236, so the company held net cash, and the parentheses mark a negative amount; the ratio row shows the same thing as "-3.5 %". The June 30, 2026 figure in the same row is a positive 3,019. Doc 3, the May 30, 2025 announcement, gives the planned "$3.5 billion of debt" for the Encino acquisition.
```

The wrong answer a careless solver gives:

```text
-$1,461 million. The solver reads (980) as a positive net debt of 980, takes the rise as 3,019 - 980 = 2,039, and subtracts the $3.5 billion of planned debt: 2,039 - 3,500 = -1,461. It then reports that net debt grew $1,461 million less than the planned debt, or that it did not exceed the plan at all.
```

Why the correct answer avoids it:

```text
A careful reader checks the sign against the rows above it. Debt of 4,236 less cash of 5,216 is -980, so EOG moved from net cash of 980 to net debt of 3,019. Net debt therefore rose by 3,019 + 980 = 3,999 million dollars over the year. Subtracting the 3,500 million of debt EOG said it expected to use leaves 3,999 - 3,500 = $499 million. The answer is positive: net debt grew by more than the planned acquisition debt.
```

(221 words across the three boxes; the form needs at least 150.)
