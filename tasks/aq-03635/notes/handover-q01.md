# aq-03635 q01 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03635 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 ff49c0d61bf1f96cfd4494c33cfc66cb75a57367c9b0331db7bf0ec115347d69: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D09 = Doc 1, D11 = Doc 9.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
On the Commission's assessment of Z Energy's average earnings and capital employed for 2016 to 2018, what percentage of those earnings exceeded a return on that capital at the top of the Commission's reasonable-return range? Give one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
61.9%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 9, the chart of 2016 to 2018 average earnings): the Commission's assessment of Z Energy's earnings is 283, in $ million a year. Z's own assessment in the same chart is 231, which is not the figure asked for.

Step 2. Source input (Doc 9, the chart of 2016 to 2018 average capital employed): the Commission's assessment of Z's capital employed is 1,254, in $ million. Z's own assessment in the same chart is 2,085, which is not the figure asked for.

Step 3. Check (Doc 9): the two Commission figures belong together, because their ratio is the return Doc 9 reports for the Commission's approach, approximately 22%: 283 / 1,254 = 22.6%

Step 4. Source input (Doc 1, paragraph X45.2): the Commission's estimate of a reasonable return is the range 6.9 - 8.6%, so the top of the range is 8.6%.

Step 5. Calculation (Doc 1 and Doc 9): the yearly earnings, in $ million, that a return at the top of the range gives on the Commission's figure for capital employed: 1,254 × 8.6% = 107.844

Step 6. Calculation (Doc 1 and Doc 9): the part of the Commission's earnings figure above that return, in $ million a year: 283 − 107.844 = 175.156

Step 7. Final answer (Doc 1 and Doc 9): that part as a share of the Commission's earnings figure, to one decimal place: 175.156 / 283 = 61.9%
```

### Answer components

Component 1

```text
61.9%
```

### Evidence

Evidence 1: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 61.9% (local note: earnings chart, l164; Doc 9)

```text
23 231 14 45 16 283 0 50 100 150 200 250 300 350
```

Evidence 2: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 61.9% (local note: earnings chart labels, l170-172; Doc 9)

```text
2016 to 2018 average earnings: Z's assessment and The Commission's assessment
```

Evidence 3: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 61.9% (local note: capital employed chart, l118; Doc 9)

```text
141 134 41 254 79 200 2,085 17 1,254 0 500 1,000 1,500 2,000 2,500 Z's assessment of capital employed
```

Evidence 4: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 61.9% (local note: capital employed chart labels, l124; Doc 9)

```text
The Commission's assessment of capital employed $m 2016 to 2018 average capital employed
```

Evidence 5: document Doc 9 (nzcc_fuel_r2_draft_z_energy_submission_on_retail_fuel_report_13_sep.txt), proves component 1. 61.9% (local note: para 24.2, l102; Doc 9)

```text
the approach used in the draft report shows an average ROACE for Z of approximately 22% for the period 2016 – 2018
```

Evidence 6: document Doc 1 (nzcc_fuel_r2_draft_retail_fuel_market_study_executive_summary_for_d.txt), proves component 1. 61.9% (local note: X45.2, l159; Doc 1)

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

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 9's two charts print Z's own assessment (earnings 231, capital employed 2,085) beside the Commission's (283 and 1,254). Taking Z's bars gives 22.4%. The question asks for the Commission's assessment, so the answer uses 283 and 1,254 and reaches 61.9%.
```

(43 / 50 words.)
