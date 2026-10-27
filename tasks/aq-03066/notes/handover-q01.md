# aq-03066 q01 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-03066 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 e75da35cf12664c47ebfe20907ed55f04ca4f2bc61d3e1229fcc53e7ccf1a8d4: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 6, D03 = Doc 2.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
At Crown Fibre Holdings' mid-point WACC for Enable, by what percentage does the opening loss asset in the Commerce Commission's illustrative calculation fall, to the nearest whole percent?
```

### Number of asks

1 ask

### Gold answer

```text
6%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, method slides and appendix table): the Commerce Commission's worked example of past losses has one rate input, WACC 10%, and uses it twice. Each year's return on capital is the WACC times that year's qualifying RAB, and each year's loss is carried to the end of 2021 at a discount rate equal to the WACC. On those inputs the opening loss asset is 1,542.
Step 2. Source input (Doc 6, cost of capital paragraph): CCHL reports that Crown Fibre Holdings used a mid-point WACC of 9% when it set Enable's wholesale pricing.
Step 3. Calculation (Doc 2 and Doc 6): gap between the two rates in percentage points, 10 - 9 = 1
Step 4. Calculation (Doc 2 and Doc 6): the same gap as a fraction of the qualifying RAB, 1 / 100 = 0.01
Step 5. Calculation (Doc 2 and Doc 6): one year of growth on a base of 100 at the lower rate, 100 + 9 = 109
Step 6. Calculation (Doc 2 and Doc 6): that growth as a multiplier, 109 / 100 = 1.09
Step 7. Calculation (Doc 2 and Doc 6): cut in the 2013 return on capital, 20 × 0.01 = 0.2
Step 8. Calculation (Doc 2 and Doc 6): loss for 2013 at the lower rate, 55 - 0.2 = 54.8
Step 9. Calculation (Doc 2 and Doc 6): the first loss carried one year, 50 × 1.09 = 54.5
Step 10. Calculation (Doc 2 and Doc 6): balance at the end of 2013, 54.5 + 54.8 = 109.3
Step 11. Calculation (Doc 2 and Doc 6): cut in the 2014 return on capital, 68 × 0.01 = 0.68
Step 12. Calculation (Doc 2 and Doc 6): loss for 2014 at the lower rate, 64 - 0.68 = 63.32
Step 13. Calculation (Doc 2 and Doc 6): balance carried from 2013 to 2014, 109.3 × 1.09 = 119.137
Step 14. Calculation (Doc 2 and Doc 6): balance at the end of 2014, 119.137 + 63.32 = 182.457
Step 15. Calculation (Doc 2 and Doc 6): cut in the 2015 return on capital, 140 × 0.01 = 1.4
Step 16. Calculation (Doc 2 and Doc 6): loss for 2015 at the lower rate, 79 - 1.4 = 77.6
Step 17. Calculation (Doc 2 and Doc 6): balance carried from 2014 to 2015, 182.457 × 1.09 = 198.87813
Step 18. Calculation (Doc 2 and Doc 6): balance at the end of 2015, 198.87813 + 77.6 = 276.47813
Step 19. Calculation (Doc 2 and Doc 6): cut in the 2016 return on capital, 226 × 0.01 = 2.26
Step 20. Calculation (Doc 2 and Doc 6): loss for 2016 at the lower rate, 96 - 2.26 = 93.74
Step 21. Calculation (Doc 2 and Doc 6): balance carried from 2015 to 2016, 276.47813 × 1.09 = 301.3611617
Step 22. Calculation (Doc 2 and Doc 6): balance at the end of 2016, 301.3611617 + 93.74 = 395.1011617
Step 23. Calculation (Doc 2 and Doc 6): cut in the 2017 return on capital, 302 × 0.01 = 3.02
Step 24. Calculation (Doc 2 and Doc 6): loss for 2017 at the lower rate, 138 - 3.02 = 134.98
Step 25. Calculation (Doc 2 and Doc 6): balance carried from 2016 to 2017, 395.1011617 × 1.09 = 430.660266253
Step 26. Calculation (Doc 2 and Doc 6): balance at the end of 2017, 430.660266253 + 134.98 = 565.640266253
Step 27. Calculation (Doc 2 and Doc 6): cut in the 2018 return on capital, 369 × 0.01 = 3.69
Step 28. Calculation (Doc 2 and Doc 6): loss for 2018 at the lower rate, 148 - 3.69 = 144.31
Step 29. Calculation (Doc 2 and Doc 6): balance carried from 2017 to 2018, 565.640266253 × 1.09 = 616.54789021577
Step 30. Calculation (Doc 2 and Doc 6): balance at the end of 2018, 616.54789021577 + 144.31 = 760.85789021577
Step 31. Calculation (Doc 2 and Doc 6): cut in the 2019 return on capital, 428 × 0.01 = 4.28
Step 32. Calculation (Doc 2 and Doc 6): loss for 2019 at the lower rate, 152 - 4.28 = 147.72
Step 33. Calculation (Doc 2 and Doc 6): balance carried from 2018 to 2019, 760.85789021577 × 1.09 = 829.3351003351893
Step 34. Calculation (Doc 2 and Doc 6): balance at the end of 2019, 829.3351003351893 + 147.72 = 977.0551003351893
Step 35. Calculation (Doc 2 and Doc 6): cut in the 2020 return on capital, 579 × 0.01 = 5.79
Step 36. Calculation (Doc 2 and Doc 6): loss for 2020 at the lower rate, 154 - 5.79 = 148.21
Step 37. Calculation (Doc 2 and Doc 6): balance carried from 2019 to 2020, 977.0551003351893 × 1.09 = 1064.990059365356337
Step 38. Calculation (Doc 2 and Doc 6): balance at the end of 2020, 1064.990059365356337 + 148.21 = 1213.200059365356337
Step 39. Calculation (Doc 2 and Doc 6): cut in the 2021 return on capital, 723 × 0.01 = 7.23
Step 40. Calculation (Doc 2 and Doc 6): loss for 2021 at the lower rate, 136 - 7.23 = 128.77
Step 41. Calculation (Doc 2 and Doc 6): balance carried from 2020 to 2021, 1213.200059365356337 × 1.09 = 1322.38806470823840733
Step 42. Calculation (Doc 2 and Doc 6): balance at the end of 2021, 1322.38806470823840733 + 128.77 = 1451.15806470823840733
Step 43. Calculation (Doc 2 and Doc 6): fall in the opening loss asset, 1,542 - 1451.15806470823840733 = 90.84193529176159267
Step 44. Calculation (Doc 2 and Doc 6): the fall as a share of the printed opening loss asset, 90.84193529176159267 / 1,542 = 6%
```

### Answer components

Component 1

```text
6%
```

### Evidence

Evidence 1: document Doc 2 (nzcc_fibre_im_r1_framework_fibre_emerging_views_presentation_25_june_2019.txt), proves component 1. 6% (local note: appendix table, inputs)

```text
Inputs WACC 10%
```

Evidence 2: document Doc 2 (nzcc_fibre_im_r1_framework_fibre_emerging_views_presentation_25_june_2019.txt), proves component 1. 6% (local note: appendix table, qualifying RAB row)

```text
20 68 140 226 302 369 428 579 723 Return on capital (WACC x Qualifying RAB)
```

Evidence 3: document Doc 2 (nzcc_fibre_im_r1_framework_fibre_emerging_views_presentation_25_june_2019.txt), proves component 1. 6% (local note: appendix table, losses row)

```text
Losses (ie, shortfall) (50) (55) (64) (79) (96) (138) (148) (152) (154) (136) (1,071)
```

Evidence 4: document Doc 2 (nzcc_fibre_im_r1_framework_fibre_emerging_views_presentation_25_june_2019.txt), proves component 1. 6% (local note: appendix table, present values row)

```text
PV losses forward to 2021 (118) (117) (125) (139) (155) (202) (197) (184) (170) (136) (1,542)
```

Evidence 5: document Doc 2 (nzcc_fibre_im_r1_framework_fibre_emerging_views_presentation_25_june_2019.txt), proves component 1. 6% (local note: slide "Adjusting the loss values to present value")

```text
Any annual losses are adjusted to present value at the end of 2021 and summed to calculate the opening value of the loss asset at implementation date.
```

Evidence 6: document Doc 2 (nzcc_fibre_im_r1_framework_fibre_emerging_views_presentation_25_june_2019.txt), proves component 1. 6% (local note: slide "Adjusting the loss values to present value")

```text
The discount rate we propose to apply is the same as the WACC value
```

Evidence 7: document Doc 6 (nzcc_fibre_im_r1_framework_christchurch_city_holding_ltd_submission_on_new_.txt), proves component 1. 6% (local note: paragraph 23)

```text
mid-point WACC of 9%, utilised by Crown Fibre Holdings Limited in establishing Enable
```

### Necessary documents

- Tick Doc 2 (nzcc_fibre_im_r1_framework_fibre_emerging_views_presentation_25_june_2019.txt), role: Answer component
- Tick Doc 6 (nzcc_fibre_im_r1_framework_christchurch_city_holding_ltd_submission_on_new_.txt), role: Answer component

Leave unticked: Doc 1 (nzcc_fibre_im_r1_framework_fibre_regulation_emerging_views_summary_paper_21.txt), Doc 3 (nzcc_fibre_im_r1_framework_vodafone_submission_on_new_regulatory_framework_.txt), Doc 4 (nzcc_fibre_im_r1_framework_chorus_submission_on_new_regulatory_framework_fo.txt), Doc 5 (nzcc_fibre_im_r1_framework_spark_submission_on_new_regulatory_framework_for.txt), Doc 7 (nzcc_fibre_im_r1_framework_spark_axiom_economics_expert_report_21_december_.txt), Doc 8 (nzcc_fibre_im_r1_framework_internet_nz_submission_on_new_regulatory_framewo.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Document convention

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Document convention: Doc 2's method slide sets the discount rate equal to the WACC, so 9% changes both the return on qualifying RAB and the compounding; changing one alone gives 2% or 4%, not 6%. Look-alike measure: Doc 6's same sentence prints the Commission's 5.56% copper mid-point, giving 24%.
```

(49 / 50 words.)
