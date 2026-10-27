# aq-04830 q01 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04830 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 4beddf7a21fb1415986d99eebb49dcf082b9c216612e922e97783625e28f3772: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 1, D03 = Doc 3.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
For the 2024-25 financial year, the Australian Government's tax receipts and its non-tax receipts both exceeded the amounts the 2024-25 Budget had forecast. What is the larger of the two percentages by which they exceeded those forecasts, to one decimal place?
```

### Number of asks

1 ask

### Gold answer

```text
5.7%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, Fiscal forecasting performance, Tax receipts): tax receipts grew 3.9 per cent in 2024-25 against 0.6 per cent forecast at the 2024-25 Budget, and were $15.3 billion higher than forecast.
Step 2. Source input (Doc 3, Non-tax receipts): non-tax receipts grew 7.1 per cent against 4.4 per cent forecast at the same Budget, and were $3.2 billion higher than forecast.
Step 3. Source input (Doc 1 and Doc 3, Table 3.1 budget aggregates, 2024-25 Actual column): tax receipts were $657.8 billion and non-tax receipts $59.1 billion. Table 3.1 prints each year's column as a separate block; this is the 2024-25 Actual block because its underlying cash balance is -10.0 ($ billion), -0.4 per cent of GDP, the 2024-25 deficit Doc 3 reports, and its gross debt of 928.6 ($ billion) is the figure the balance sheet table prints under "Actual 2024-25".
Step 4. Calculation (Doc 1 and Doc 3): forecast tax receipts = 657.8 - 15.3 = 642.5 ($ billion).
Step 5. Calculation (Doc 1 and Doc 3): forecast non-tax receipts = 59.1 - 3.2 = 55.9 ($ billion).
Step 6. Calculation (Doc 1 and Doc 3): tax receipts' excess over their forecast = 15.3 / 642.5 = 2.4%.
Step 7. Calculation (Doc 1 and Doc 3): non-tax receipts' excess over their forecast = 3.2 / 55.9 = 5.7%.
Step 8. Final answer (Doc 1 and Doc 3): the larger of 2.4% and 5.7% is 5.7%, for non-tax receipts.
Step 9. Look-alike measure (Doc 1 and Doc 3): read as gaps, the growth rates in Steps 1 and 2 rank tax receipts first: 3.9 - 0.6 = 3.3 percentage points, more than non-tax receipts' 7.1 less 4.4. They do not measure how far the amounts exceeded their forecasts: Step 6 shows the $15.3 billion was 2.4% of the forecast tax amount, not 3.3. So the decoy answer, 3.3 for tax receipts, is wrong; the dollar gaps over the forecast amounts give 5.7%.
```

### Answer components

Component 1

```text
5.7%
```

### Evidence

Evidence 1: document Doc 3 (Budget-Paper-No.-1-Statement-8-Forecasting-Performance-and.txt), proves component 1. 5.7% (local note: Doc 3, Tax receipts, line 91)

```text
Tax receipts grew 3.9 per cent in 2024–25 rather than 0.6 per cent forecast at the 2024–25 Budget
```

Evidence 2: document Doc 3 (Budget-Paper-No.-1-Statement-8-Forecasting-Performance-and.txt), proves component 1. 5.7% (local note: Doc 3, Tax receipts, line 91)

```text
Tax receipts were $15.3 billion higher than forecast.
```

Evidence 3: document Doc 3 (Budget-Paper-No.-1-Statement-8-Forecasting-Performance-and.txt), proves component 1. 5.7% (local note: Doc 3, Non-tax receipts, line 110)

```text
Non-tax receipts grew 7.1 per cent in 2024–25 rather than 4.4 per cent forecast at the 2024–25 Budget
```

Evidence 4: document Doc 3 (Budget-Paper-No.-1-Statement-8-Forecasting-Performance-and.txt), proves component 1. 5.7% (local note: Doc 3, Non-tax receipts, line 110)

```text
Non-tax receipts were $3.2 billion higher than forecast.
```

Evidence 5: document Doc 3 (Budget-Paper-No.-1-Statement-8-Forecasting-Performance-and.txt), proves component 1. 5.7% (local note: Doc 3, Underlying cash balance, line 130)

```text
The underlying cash balance was a deficit of 0.4 per cent of GDP in 2024–25
```

Evidence 6: document Doc 1 (Budget-Paper-No.-1-Statement-3-Fiscal-Strategy-and-Outlook.txt), proves component 1. 5.7% (local note: Doc 1, Table 3.1 column headings, lines 72-74)

```text
Actual Estimates 2024-25 2025-26 2026-27 2027-28 2028-29 2029-30 Total(a)
```

Evidence 7: document Doc 1 (Budget-Paper-No.-1-Statement-3-Fiscal-Strategy-and-Outlook.txt), proves component 1. 5.7% (local note: Doc 1, Table 3.1 row labels, lines 89-95)

```text
Tax receipts 757.0 699.5 Per cent of GDP 23.8 23.6 Non-tax receipts
```

Evidence 8: document Doc 1 (Budget-Paper-No.-1-Statement-3-Fiscal-Strategy-and-Outlook.txt), proves component 1. 5.7% (local note: Doc 1, Table 3.1, 2024-25 Actual block, lines 144-152)

```text
-10.0 -0.4 717.0 25.8 657.8 23.7 59.1 2.1
```

Evidence 9: document Doc 1 (Budget-Paper-No.-1-Statement-3-Fiscal-Strategy-and-Outlook.txt), proves component 1. 5.7% (local note: Doc 1, Table 3.6 balance sheet, Actual 2024-25 column, lines 1635-1651)

```text
Actual 2024-25 $b 665.4 24.0 227.4 8.2 892.8 32.1 1,507.4 54.3 -614.5 -22.1 -841.9 -30.3 928.6 33.4
```

### Necessary documents

- Tick Doc 1 (Budget-Paper-No.-1-Statement-3-Fiscal-Strategy-and-Outlook.txt), role: Answer component
- Tick Doc 3 (Budget-Paper-No.-1-Statement-8-Forecasting-Performance-and.txt), role: Answer component

Leave unticked: Doc 2 (Budget-Paper-No.-1-Statement-7-Debt-Statement.txt), Doc 4 (The-Global-Fiscal-Response-to-COVID-19.txt), Doc 5 (Government-Bond-Markets-in-Advanced-Economies-During-the.txt), Doc 6 (Economic-Reform-Roundtable-Budget-sustainability-and-tax.txt), Doc 7 (Inflation-linked-Financial-Markets-RBA-Bulletin-Oct-2024.txt), Doc 8 (The-fiscal-and-distributional-impact-of-the-reform-of.txt), Doc 9 (Government-Finance-Statistics-Australia-June-2026.txt), Doc 10 (The-Yield-and-Market-Function-Effects-of-the-Reserve-Bank-of.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 3 gives 2024-25 forecast misses as growth rates and dollar gaps. Comparing growth gaps (tax 3.9 against 0.6 per cent) picks tax receipts, 3.3%. Dollar gaps over forecast amounts (Doc 1 outcomes less the gaps) give tax 2.4%, non-tax 5.7%.
```

(43 / 50 words.)
