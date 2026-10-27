# aq-03635 q03 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03635 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 e45f64306b5747ab4680202cc799bd9b9ad4363dec8e842738d4b3daff24bb9e: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D09 = Doc 1, D11 = Doc 9.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: six words shared with q01: 'commission's reasonable-return range give one decimal'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Z Energy says the Commission should have used Z's own capital employed in working out Z's ROACE. Doing that and changing nothing else in the Commission's calculation, by how many percentage points would Z's ROACE exceed the top of the Commission's reasonable-return range? Give one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
5.0 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 9, the chart of 2016 to 2018 average earnings): the Commission's calculation of Z Energy's ROACE covers 2016 to 2018, and its assessment of Z's earnings is 283, in $ million a year. Z's own assessment in the same chart is 231, which stays out because nothing but capital employed changes.

Step 2. Source input (Doc 9, the chart of 2016 to 2018 average capital employed): Z's own assessment of its capital employed is 2,085, in $ million. The Commission's assessment in the same chart is 1,254, which is the figure being replaced.

Step 3. Check (Doc 9): the two Commission figures are a pair, because their ratio is the ROACE that Doc 9 reports for the Commission's approach, approximately 22%: 283 / 1,254 = 22.6%

Step 4. Check (Doc 9, Appendix 2): the appendix lists capital employed at four year ends. The chart's figure is Doc 9's own average for 2016 to 2018, built from each year's opening and closing balance, so it is not the plain mean of the last three year-end balances in the appendix. The figure to use for Z's capital employed is therefore the printed 2,085.

Step 5. Source input (Doc 9, paragraph 26): Z says that including the components the Commission left out of capital employed would reduce its ROACE on the Commission's numbers by approximately 9%. Doc 9 gives the size of the fall only as an approximation, so the ratio is worked out from the two chart figures.

Step 6. Calculation (Doc 9): Z's ROACE with the Commission's earnings over Z's capital employed: 283 / 2,085 = 13.6%

Step 7. Source input (Doc 1, paragraph X45.2): the Commission's estimate of a reasonable return is the range 6.9 - 8.6%, so the top of the range is 8.6%.

Step 8. Calculation (Doc 9 and Doc 1): the yearly earnings, in $ million, that a return at the top of the range gives on Z's figure for capital employed: 2,085 × 8.6% = 179.31

Step 9. Calculation (Doc 9 and Doc 1): the part of the Commission's earnings figure above that return, in $ million a year: 283 − 179.31 = 103.69

Step 10. Final answer (Doc 9 and Doc 1): that part as a rate on Z's capital employed, which is the number of percentage points by which the ROACE exceeds the top of the range, to one decimal place: 103.69 / 2,085 = 5.0%
```

### Answer components

Component 1

```text
5.0 percentage points
```

### Evidence

Evidence 1: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 5.0 percentage points (local note: earnings chart, l164; Doc 9)

```text
23 231 14 45 16 283 0 50 100 150 200 250 300 350
```

Evidence 2: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 5.0 percentage points (local note: earnings chart title, l172; Doc 9)

```text
2016 to 2018 average earnings: Z's assessment and The Commission's assessment
```

Evidence 3: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 5.0 percentage points (local note: capital employed chart, l118; Doc 9)

```text
141 134 41 254 79 200 2,085 17 1,254 0 500 1,000 1,500 2,000 2,500 Z's assessment of capital employed
```

Evidence 4: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 5.0 percentage points (local note: capital employed chart labels, l124; Doc 9)

```text
The Commission's assessment of capital employed $m 2016 to 2018 average capital employed
```

Evidence 5: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 5.0 percentage points (local note: para 26, l105; Doc 9)

```text
would reduce Z’s ROACE – on the Commission’s numbers – by approximately 9%
```

Evidence 6: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 5.0 percentage points (local note: para 24.2, l102; Doc 9)

```text
the approach used in the draft report shows an average ROACE for Z of approximately 22% for the period 2016 – 2018
```

Evidence 7: document Doc 1 (nzcc_fuel_r2_draft_retail_fuel_market_study_executive_summary_for_d.txt), proves component 1. 5.0 percentage points (local note: X45.2, l159; Doc 1)

```text
well above our estimate of a reasonable return (6.9 - 8.6%)
```

### Necessary documents

- Tick Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), role: Answer component
- Tick Doc 1 (nzcc_fuel_r2_draft_retail_fuel_market_study_executive_summary_for_d.txt), role: Answer component

Leave unticked: Doc 2 (nzcc_fuel_r2_draft_aa_submission_on_retail_fuel_draft_report_13_sep.txt), Doc 3 (nzcc_fuel_r2_draft_business_new_zealand_submission_on_retail_fuel_d.txt), Doc 4 (nzcc_fuel_r2_draft_gull_new_zealand_limited_submission_on_retail_fu.txt), Doc 5 (nzcc_fuel_r2_draft_mobil_submission_on_retail_fuel_draft_report_13_.txt), Doc 6 (nzcc_fuel_r2_draft_mta_submission_on_retail_fuel_draft_report_13_se.txt), Doc 7 (nzcc_fuel_r2_draft_refining_nz_submission_on_retail_fuel_draft_repo.txt), Doc 8 (nzcc_fuel_r2_draft_waitomo_submission_on_retail_fuel_draft_report_1.txt), Doc 10 (nzcc_fuel_r2_draft_bp_submission_on_retail_fuel_draft_report_13_sep.txt), Doc 11 (nzcc_fuel_r2_draft_meug_cross_submission_on_retail_fuel_draft_repor.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization

Leave unticked: Temporal alignment, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Document convention: Doc 9's Appendix 2 lists Z's capital employed at each year end. Averaging the last three balances gives 2,293 and an answer of 3.7. Doc 9's chart states the 2016 to 2018 average, built from opening and closing balances, as 2,085, which gives 5.0.
```

(46 / 50 words.)
