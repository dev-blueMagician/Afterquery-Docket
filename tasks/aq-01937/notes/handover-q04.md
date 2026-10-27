# aq-01937 q04 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01937 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 8bf47c841070d7a19836ca6d52ceb745fafcb3deccf0c326c0a639223fb3bd64: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 1, D02 = Doc 2, D03 = Doc 3, D10 = Doc 10.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By what percentage were State Street's total expenses in the first half of 2026 higher than in the first half of 2023? Answer to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
19.4%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 10, expense table, columns 2Q26, 1Q26, 2Q25): total expenses were 2,659 ($ millions) in 2Q26 and 2,811 in 1Q26.

Step 2. Calculation (Doc 10, first half of 2026): 2,811 + 2,659 = 5,470 ($ millions).

Step 3. Source input (Doc 1, FY2024 expense outlook slide, footnote): FY2023 GAAP expenses were $9,583M. The $8,963M that the slide carries for FY2023 is the non-GAAP figure, which excludes $(620)M of notable items, so it is not total expenses.

Step 4. Source input (Doc 2, expense table, columns 3Q24, 2Q24, 3Q23): total expenses were 2,180 in 3Q23.

Step 5. Source input (Doc 3, expense table, columns 4Q24, 3Q24, 4Q23): total expenses were 2,822 in 4Q23.

Step 6. Calculation (Doc 1 and Doc 2): no document reports the first half of 2023, so take the FY2023 GAAP total less the third quarter: 9,583 - 2,180 = 7,403 ($ millions).

Step 7. Calculation (Doc 3): less the fourth quarter as well, which leaves the first half of that year: 7,403 - 2,822 = 4,581 ($ millions).

Step 8. Calculation (later half-year less earlier half-year): 5,470 - 4,581 = 889 ($ millions).

Step 9. Calculation (increase as a share of the earlier half-year): 889 / 4,581 = 19.4% (one decimal place).
```

### Answer components

Component 1

```text
19.4%
```

### Evidence

Evidence 1: document Doc 10 (stt_ex991_2026-07-16.txt), proves component 1. 19.4% (local note: expense table header, L276)

```text
(Dollars in millions) 2Q26 1Q26 2Q25 % QoQ % YoY
```

Evidence 2: document Doc 10 (stt_ex991_2026-07-16.txt), proves component 1. 19.4% (local note: expense table, total row, L283)

```text
Total Expenses $ 2,659 $ 2,811 $ 2,529
```

Evidence 3: document Doc 1 (stt_ex991_2024-02-27.txt), proves component 1. 19.4% (local note: FY2024 expense outlook slide, footnote, L23)

```text
FY2023 non-GAAP expenses of $8,963M is FY2023 GAAP expenses of $9,583M excluding notable items of $(620)M
```

Evidence 4: document Doc 2 (stt_ex991_2024-10-15.txt), proves component 1. 19.4% (local note: expense table header, L311)

```text
(Dollars in millions) 3Q24 2Q24 3Q23 % QoQ % YoY
```

Evidence 5: document Doc 2 (stt_ex991_2024-10-15.txt), proves component 1. 19.4% (local note: expense table, total row, L319)

```text
Total Expenses $ 2,308 $ 2,269 $ 2,180
```

Evidence 6: document Doc 3 (stt_ex991_2025-01-17.txt), proves component 1. 19.4% (local note: expense table header, L312)

```text
(Dollars in millions) 4Q24 3Q24 4Q23 % QoQ % YoY
```

Evidence 7: document Doc 3 (stt_ex991_2025-01-17.txt), proves component 1. 19.4% (local note: expense table, total row, L320)

```text
Total Expenses $ 2,440 $ 2,308 $ 2,822
```

### Necessary documents

- Tick Doc 1 (stt_ex991_2024-02-27.txt), role: Answer component
- Tick Doc 2 (stt_ex991_2024-10-15.txt), role: Answer component
- Tick Doc 3 (stt_ex991_2025-01-17.txt), role: Answer component
- Tick Doc 10 (stt_ex991_2026-07-16.txt), role: Answer component

Leave unticked: Doc 4 (stt_ex991_2025-03-05.txt), Doc 5 (stt_ex991_2025-04-17.txt), Doc 6 (stt_ex991_2025-07-15.txt), Doc 7 (stt_ex991_2025-10-17.txt), Doc 8 (stt_ex991_2026-01-16.txt), Doc 9 (stt_ex991_2026-04-17.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Figure that must be computed

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Doc 1's slide shows FY2023 expenses as $8,963M, but that is non-GAAP; its footnote gives GAAP $9,583M. First-half 2023 is printed nowhere: 9,583 less 3Q23 (Doc 2, 2,180) and 4Q23 (Doc 3, 2,822) is 4,581, giving 19.4%. Using $8,963M gives 38.1%; halving FY2023 gives 14.2%.
```

(45 / 50 words.)
