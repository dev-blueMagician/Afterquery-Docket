# aq-03635 q02 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03635 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 9be1dc937218883e80864fdcac3584d448aa71d5932eafc30d7bd5f0ffa6f88e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D09 = Doc 1, D11 = Doc 9.
- Floor: 0 FAIL, 10 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 9 doesn't mention 1,006. expected false alarm: Doc 9 prints it at character 101,977, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 1: Doc 9 doesn't mention 1,101. expected false alarm: Doc 9 prints it at character 101,983, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 1: Doc 9 doesn't mention 1,425. expected false alarm: Doc 9 prints it at character 101,989, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 1: Doc 9 doesn't mention 2017. Doc 9 prints it first at character 27,632, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 9 doesn't mention 1,463. expected false alarm: Doc 9 prints it at character 101,995, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 2: Doc 9 doesn't mention 202. expected false alarm: Doc 9 prints it at character 102,473, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 2: Doc 9 doesn't mention 308. expected false alarm: Doc 9 prints it at character 102,477, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 2: Doc 9 doesn't mention 339. expected false alarm: Doc 9 prints it at character 102,481, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN sibling: six words shared with q01: 'the top of the commission's reasonable-return'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
In whichever of its 2016 to 2018 financial years Z Energy's ROACE (return on average capital employed) on the Commission's figures was highest, how many percentage points above the top of the Commission's reasonable-return range was it? Give one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
15.8 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 9, Appendix 2, capital employed reconciliation, the row "The Commission capital employed", in $ million at each year end): 1,006 at the year end before 2016, 1,101 for 2016, 1,425 for 2017 and 1,463 for 2018.

Step 2. Source input (Doc 9, Appendix 2, earnings reconciliation, the row "The Commission net operating after tax", in $ million): 202 for 2016, 308 for the year after and 339 for 2018. The row has three figures, and Doc 9's earnings chart, which averages the same row, is titled 2016 to 2018.

Step 3. Source input (Doc 9, Part A, on replacement cost): ROACE divides earnings by average capital employed. A year's average capital is therefore the mean of the balance at the end of the year before and the balance at the end of that year, which is why the capital rows start one year earlier than the earnings rows. Doc 9 states the Commission's ROACE for Z only as approximately 22% for the three years together, so each year's figure has to be worked out.

Step 4. Source input (Doc 1, paragraph X45.2): the Commission's estimate of a reasonable return is the range 6.9 - 8.6%, so the top of the range is 8.6%.

Step 5. Calculation (Doc 9 and Doc 1): opening plus closing capital for 2016: 1,006 + 1,101 = 2,107

Step 6. Calculation (Doc 9 and Doc 1): average capital employed for 2016: 2,107 / 2 = 1,053.5

Step 7. Calculation (Doc 9 and Doc 1): ROACE for 2016: 202 / 1,053.5 = 19.2%

Step 8. Calculation (Doc 9 and Doc 1): opening plus closing capital for 2017: 1,101 + 1,425 = 2,526

Step 9. Calculation (Doc 9 and Doc 1): average capital employed for 2017: 2,526 / 2 = 1,263

Step 10. Calculation (Doc 9 and Doc 1): ROACE for 2017: 308 / 1,263 = 24.4%

Step 11. Calculation (Doc 9 and Doc 1): opening plus closing capital for 2018: 1,425 + 1,463 = 2,888

Step 12. Calculation (Doc 9 and Doc 1): average capital employed for 2018: 2,888 / 2 = 1,444

Step 13. Calculation (Doc 9 and Doc 1): ROACE for 2018: 339 / 1,444 = 23.5%

Step 14. Comparison (Doc 9 and Doc 1): the ratio for 2017 is the highest of the three, so 2017 is the year the question asks about.

Step 15. Calculation (Doc 9 and Doc 1): the earnings, in $ million, that a return at the top of the range gives on the average capital employed for 2017: 1,263 × 8.6% = 108.618

Step 16. Calculation (Doc 9 and Doc 1): the earnings for 2017 above that return, in $ million: 308 − 108.618 = 199.382

Step 17. Final answer (Doc 9 and Doc 1): that excess as a rate on the average capital employed for 2017, which is the number of percentage points by which the ROACE exceeds the top of the range, to one decimal place: 199.382 / 1,263 = 15.8%
```

### Answer components

Component 1

```text
15.8 percentage points
```

### Evidence

Evidence 1: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 15.8 percentage points (local note: Appendix 2, l935; Doc 9)

```text
The Commission capital employed	1,006	1,101	1,425	1,463
```

Evidence 2: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 15.8 percentage points (local note: Appendix 2, l936; Doc 9)

```text
$m	2015	2016	2017	2018
```

Evidence 3: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 15.8 percentage points (local note: Appendix 2, l949; Doc 9)

```text
The Commission net operating after tax	202	308	339
```

Evidence 4: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 15.8 percentage points (local note: earnings chart title, l172; Doc 9)

```text
2016 to 2018 average earnings: Z's assessment and The Commission's assessment
```

Evidence 5: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 15.8 percentage points (local note: para 42.2, l179; Doc 9)

```text
the average capital employed used in the denominator (where earnings are the numerator) to calculate ROACE
```

Evidence 6: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 15.8 percentage points (local note: para 24.2, l102; Doc 9)

```text
the approach used in the draft report shows an average ROACE for Z of approximately 22% for the period 2016 – 2018
```

Evidence 7: document Doc 1 (nzcc_fuel_r2_draft_retail_fuel_market_study_executive_summary_for_d.txt), proves component 1. 15.8 percentage points (local note: X45.2, l159; Doc 1)

```text
well above our estimate of a reasonable return (6.9 - 8.6%)
```

### Necessary documents

- Tick Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), role: Answer component
- Tick Doc 1 (nzcc_fuel_r2_draft_retail_fuel_market_study_executive_summary_for_d.txt), role: Answer component

Leave unticked: Doc 2 (nzcc_fuel_r2_draft_aa_submission_on_retail_fuel_draft_report_13_sep.txt), Doc 3 (nzcc_fuel_r2_draft_business_new_zealand_submission_on_retail_fuel_d.txt), Doc 4 (nzcc_fuel_r2_draft_gull_new_zealand_limited_submission_on_retail_fu.txt), Doc 5 (nzcc_fuel_r2_draft_mobil_submission_on_retail_fuel_draft_report_13_.txt), Doc 6 (nzcc_fuel_r2_draft_mta_submission_on_retail_fuel_draft_report_13_se.txt), Doc 7 (nzcc_fuel_r2_draft_refining_nz_submission_on_retail_fuel_draft_repo.txt), Doc 8 (nzcc_fuel_r2_draft_waitomo_submission_on_retail_fuel_draft_report_1.txt), Doc 10 (nzcc_fuel_r2_draft_bp_submission_on_retail_fuel_draft_report_13_sep.txt), Doc 11 (nzcc_fuel_r2_draft_meug_cross_submission_on_retail_fuel_draft_repor.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Wrong year or edition

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 9's Appendix 2 lists year-end capital employed; dividing by it instead of average capital makes 2018 the peak and gives 14.6. Wrong year: Doc 9's paragraph 24.2 prints 22% for 2016 to 2018 together, giving 13.4. Averaging the balances makes 2017 the peak, 15.8.
```

(47 / 50 words.)
