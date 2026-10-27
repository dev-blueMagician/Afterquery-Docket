# aq-04112 q01 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-04112 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 e21fa8ca748e30dd744dff7a5d147206fd58ff0778b207792a37ce790c1f6eb6: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 2, D03 = Doc 1.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 1 doesn't mention 610. expected false alarm: Doc 1 prints it at character 60,122, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 2: Doc 1 doesn't mention 199. expected false alarm: Doc 1 prints it at character 60,162, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 2: Doc 1 doesn't mention 800. Doc 1 prints it first at character 34,579, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 1 doesn't mention 624. expected false alarm: Doc 1 prints it at character 60,412, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
At the Association of Labour Providers' unit costs, what would it cost to recruit, for three years, the staff Nick Allen's example plant lacked?
```

### Number of asks

1 ask

### Gold answer

```text
£1,273,150
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, Table 3 in the section on the cost of using the immigration system): the Association of Labour Providers costs a business recruiting workers for three years through the Skilled Worker Visa route, line by line, with a unit cost and a total for each line. For the sponsor application the total is the same as the unit cost, so a company pays it once. Every other line is charged for each worker, and two of them for each year as well.
Step 2. Source input and calculation (Doc 1, Table 3): the charges paid once for each worker are the visa at £610, the Certificate of Sponsorship at £199, recruitment at £2,000 and travel at £800: 610 + 199 + 2,000 + 800 = 3,609 pounds.
Step 3. Source input and calculation (Doc 1, Table 3): the charges paid every year for each worker are the Immigration Skills Charge at £1,000 and the Immigration Health Surcharge at £624: 1,000 + 624 = 1,624 pounds a year. The sponsor application, the one line a company pays once, is a further £1,000.
Step 4. Source input (Doc 2, Nick Allen of the British Meat Processors Association, in his first answer to the Chair): he takes a meat plant as his example and says that on any morning it is "150 people short".
Step 5. Calculation (Doc 1 and Doc 2): worker-years for those staff over the table's three years: 150 × 3 = 450.
Step 6. Calculation (Doc 1 and Doc 2): once-only charges for all of them: 150 × 3,609 = 541,350 pounds.
Step 7. Calculation (Doc 1 and Doc 2): yearly charges over the three years: 450 × 1,624 = 730,800 pounds.
Step 8. Calculation (Doc 1 and Doc 2): with the one sponsor application added: 541,350 + 730,800 + 1,000 = 1,273,150 pounds.
Step 9. Check (Doc 1 and Doc 2): the sponsor application is counted once, as in the table, where its total equals its unit cost. Scaling the table's whole cost up to the larger head count would count that application more than once.
Step 10. Final answer (Doc 1 and Doc 2): recruiting them would cost £1,273,150.
```

### Answer components

Component 1

```text
£1,273,150
```

### Evidence

Evidence 1: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £1,273,150 (local note: para 50, sentence introducing Table 3)

```text
The Association of Labour Providers (ALP) provided the data set out in Table 3 to illustrate the full costs over three years for a business recruiting 50 workers through the Skilled Worker Visa route.
```

Evidence 2: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £1,273,150 (local note: Table 3, sponsor application)

```text
Sponsor application - large company £1,000 £1,000
```

Evidence 3: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £1,273,150 (local note: Table 3, visa)

```text
Skilled worker visa £610 £30,500
```

Evidence 4: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £1,273,150 (local note: Table 3, certificate)

```text
Certificate of Sponsorship £199 £9,950
```

Evidence 5: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £1,273,150 (local note: Table 3, recruitment, label)

```text
Recruitment - advertising, short-listing, interviewing, translation and interpretation
```

Evidence 6: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £1,273,150 (local note: Table 3, recruitment, figures)

```text
£2,000 £100,000
```

Evidence 7: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £1,273,150 (local note: Table 3, travel and skills charge)

```text
Travel from home country to place of work Est £800 £40,000 Immigration Skills Charge £1,000/year £150,000
```

Evidence 8: document Doc 1 (ukc_1497_report_9580.txt), proves component 1. £1,273,150 (local note: Table 3, health surcharge)

```text
Immigration Health Surcharge £624/year £93,600
```

Evidence 9: document Doc 2 (ukc_1497_oral_2900.txt), proves component 1. £1,273,150 (local note: Q70, Nick Allen)

```text
If you are running a meat plant at the moment and you have 1,000 people, you wake up in the morning and you know you are 150 people short already.
```

### Necessary documents

- Tick Doc 1 (ukc_1497_report_9580.txt), role: Answer component
- Tick Doc 2 (ukc_1497_oral_2900.txt), role: Answer component

Leave unticked: Doc 3 (ukc_1497_oral_2977.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Aggregation

Leave unticked: Temporal alignment, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Rounding, scale or sign

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 1's Table 3 charges the sponsor application once per company and every other line per worker. Scaling its £425,050 total for 50 workers up to Doc 2's 150 charges the application three times: £1,275,150. Priced line by line with one application, the cost is £1,273,150.
```

(49 / 50 words.)
