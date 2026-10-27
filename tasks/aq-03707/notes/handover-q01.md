# aq-03707 q01 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03707 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 31dbf1779467e901a394ace890455ee38278e0800658b96ec1276dd0f56581e7: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D03 = Doc 11, D08 = Doc 1.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 1 doesn't mention 13.1%. Doc 1 prints it first at character 22,308, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 6: Docs 1 and 11 don't mention 13.1. Doc 1 prints it first at character 22,308, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
How far, in percentage points, is Foodstuffs North Island's 2015 to 2019 ROACE in the Commission's final report from the top of the range of overseas grocers' returns that Foodstuffs' profitability consultant treats as comparable with a return measured that way? Give one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
2.1 percentage points above
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, the final report's profitability finding): the Commission's estimate of the return on average capital employed (ROACE) of Foodstuffs North Island, averaged over five years, is 13.1%.

Step 2. Source input (Doc 1, the same finding, on what changed after the draft report): the estimates for the Foodstuffs co-operatives are now on a whole of business basis, which covers the entire co-operative, including its ownership of the property used for retail stores. In the draft report the focus was on the individually owned stores.

Step 3. Source input (Doc 11, the sections on calculating profitability and on benchmarks): when the consultant wrote, the Commission had said it intended to measure Foodstuffs at the level of its stores, on the assumption that the stores are renters of their land and buildings. The consultant calls a return measured that way highly levered. A return with the value of all assets in capital employed is unlevered, and the consultant describes the co-operatives' whole of business return as unlevered. A benchmark fits only returns that are also unlevered unless it is raised to the same leverage.

Step 4. Source input (Doc 11, the section on calculating profitability): the average unlevered return on capital employed of the international sample of grocery retailers was between approximately 9 per cent and 11 per cent. Restated at the leverage of Foodstuffs' stores assumed to be renters, that range becomes approximately 22 per cent to 25 per cent.

Step 5. Matching (Doc 1 and Doc 11): the final report's 13.1% is the whole of business figure, with the stores' property counted, so on the consultant's reasoning it is an unlevered return. The comparable range is the unlevered one, whose top is 11 per cent. The range restated for renters fits only the store-level measure, which the final report did not use for this figure.

Step 6. Calculation (Doc 1 and Doc 11): 13.1 − 11 = 2.1

Step 7. Final answer (Doc 1 and Doc 11): the ROACE of Foodstuffs North Island is 2.1 percentage points above the top of the comparable range.
```

### Answer components

Component 1

```text
2.1 percentage points above
```

### Evidence

Evidence 1: document Doc 1 (nzcc_grocery_r3_postconf_market_study_into_the_retail_grocery_sector_exec.txt), proves component 1. 2.1 percentage points above (local note: profitability finding, l172; Doc 1)

```text
are 12.7% for Woolworths NZ, 12.8% for Foodstuffs SI and 13.1% for Foodstuffs NI
```

Evidence 2: document Doc 1 (nzcc_grocery_r3_postconf_market_study_into_the_retail_grocery_sector_exec.txt), proves component 1. 2.1 percentage points above (local note: changes since the draft, l178; Doc 1)

```text
including the centralised functions provided by the co-operatives and ownership of property used for retail stores
```

Evidence 3: document Doc 1 (nzcc_grocery_r3_postconf_market_study_into_the_retail_grocery_sector_exec.txt), proves component 1. 2.1 percentage points above (local note: changes since the draft, l178; Doc 1)

```text
In the draft report, our focus was on the individually owned and operated stores that directly engage in grocery retailing.
```

Evidence 4: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 2.1 percentage points above (local note: para 3, l72; Doc 11)

```text
to calculate those returns on the assumption that the stores are renters of the land and buildings assets that are employed
```

Evidence 5: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 2.1 percentage points above (local note: para 17a, l221; Doc 11)

```text
for the measured ROACE to be an unlevered return, the value of all assets needs to be included in capital employed
```

Evidence 6: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 2.1 percentage points above (local note: para 29b, l298; Doc 11)

```text
close to (and in many cases higher than) the Foodstuffs cooperatives when the latter is
```

Evidence 7: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 2.1 percentage points above (local note: para 29b continued, l308; Doc 11)

```text
calculated on an unlevered, whole of business basis
```

Evidence 8: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 2.1 percentage points above (local note: para 25, l277; Doc 11)

```text
can only be applied to benchmark returns for the grocery retailers that are also truly unlevered
```

Evidence 9: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 2.1 percentage points above (local note: para 8b i, l159; Doc 11)

```text
the average unlevered return on capital employed for the international sample of grocery retailers was between approximately 9 per cent and 11 per cent
```

Evidence 10: document Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), proves component 1. 2.1 percentage points above (local note: para 8b ii, l162; Doc 11)

```text
this range would adjust to approximately 22 per cent to 25 per cent to be consistent with the leverage
```

### Necessary documents

- Tick Doc 1 (nzcc_grocery_r3_postconf_market_study_into_the_retail_grocery_sector_exec.txt), role: Answer component
- Tick Doc 11 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi.txt), role: Answer component

Leave unticked: Doc 2 (nzcc_grocery_r3_postconf_consumer_nz_post_conference_submission_on_market.txt), Doc 3 (nzcc_grocery_r3_postconf_coriolis_ltd_post_conference_submission_on_marke.txt), Doc 4 (nzcc_grocery_r3_postconf_kore_hiakai_zero_hunger_collective_post_conferen.txt), Doc 5 (nzcc_grocery_r3_postconf_monopoly_watch_post_conference_submission_on_mar.txt), Doc 6 (nzcc_grocery_r3_postconf_ngati_porou_holding_company_ltd_post_conference_.txt), Doc 7 (nzcc_grocery_r3_postconf_northelia_post_conference_submission_on_market_s.txt), Doc 8 (nzcc_grocery_r3_postconf_nz_food_and_grocery_council_post_conference_subm.txt), Doc 9 (nzcc_grocery_r3_postconf_nz_initiative_post_conference_submission_on_mark.txt), Doc 10 (nzcc_grocery_r3_postconf_frugl_post_conference_submission_on_market_study.txt), Doc 12 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi_e77297.txt), Doc 13 (nzcc_grocery_r3_postconf_foodstuffs_north_island_post_conference_submissi_446b21.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 11 says the Commission meant to measure Foodstuffs' stores as renters, so a careless solver takes its renter-leverage range of 22 to 25 per cent and answers 11.9 below. Doc 1's final figure counts the co-operative's store property, so the unlevered range applies: 2.1 above.
```

(49 / 50 words.)
