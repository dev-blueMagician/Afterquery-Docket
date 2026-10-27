# aq-03423 q02 hand-over

Generated 2026-10-12 by `python tools/check_questions.py tasks/aq-03423 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 6258b1cf1b15039b292fc4c562d885ed9d19919727906e4def39ce4673ae002a: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D05 = Doc 1, D08 = Doc 7.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 1 doesn't mention 70. Doc 1 prints it first at character 38,145, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 7 doesn't mention 55. Doc 7 prints it first at character 39,195, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Over a first year, how much more or less per included gigabyte, to the nearest cent, does the 10GB plan 2degrees cites cost than its 25GB plan that the Commerce Commission priced?
```

### Number of asks

1 ask

### Gold answer

```text
$1.60 more per gigabyte
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, pricing section): the Commission prices 2degrees' SIM-only plan with a data allowance of up to 25 GB at 70 dollars per month. The 65 dollars printed beside it is Skinny Direct's price, not 2degrees'.

Step 2. Source input (Doc 7, answer on higher-volume prices): 2degrees replies that its rates are lower than stated and cites a plan at 55 dollars for 10 GB, with double data for the first 3 months.

Step 3. Calculation (Doc 1 and Doc 7): the doubled monthly allowance, in GB: 2 × 10 = 20.

Step 4. Calculation (Doc 1 and Doc 7): months of a first year at the standard allowance: 12 − 3 = 9.

Step 5. Calculation (Doc 1 and Doc 7): data in the double-data months, in GB: 3 × 20 = 60.

Step 6. Calculation (Doc 1 and Doc 7): data in the other months, in GB: 9 × 10 = 90.

Step 7. Calculation (Doc 1 and Doc 7): data the cited plan includes over the year, in GB: 60 + 90 = 150.

Step 8. Calculation (Doc 1 and Doc 7): price of the cited plan over the year, in dollars: 12 × 55 = 660.

Step 9. Calculation (Doc 1 and Doc 7): the cited plan, in dollars per GB over the year: 660 / 150 = 4.4.

Step 10. Calculation (Doc 1 and Doc 7): the plan the Commission priced, in dollars per GB, the same in every month: 70 / 25 = 2.8.

Step 11. Calculation (Doc 1 and Doc 7): difference in dollars per GB: 4.4 − 2.8 = 1.6. The plan 2degrees cites is the dearer one by that amount per included gigabyte.
```

### Answer components

Component 1

```text
$1.60 more per gigabyte
```

### Evidence

Evidence 1: document Doc 1 (nzcc_mobile_r1_issues_study_of_mobile_telecommunications_markets_in_ne.txt), proves component 1. $1.60 more per gigabyte (local note: para 100, L550)

```text
with data allowances of up to 25GB, for $65 per month (Skinny Direct) and $70 per month (2degrees)
```

Evidence 2: document Doc 1 (nzcc_mobile_r1_issues_study_of_mobile_telecommunications_markets_in_ne.txt), proves component 1. $1.60 more per gigabyte (local note: para 101, L551)

```text
the 25GB plans offered by Skinny Direct and 2degrees have no fixed term
```

Evidence 3: document Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), proves component 1. $1.60 more per gigabyte (local note: answer on Q5, L333)

```text
rates are lower than that stated and substantially lower than in the benchmarking table
```

Evidence 4: document Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), proves component 1. $1.60 more per gigabyte (local note: answer on Q5, L335)

```text
2degrees currently offers $55 for 10GB (with double data, i.e. 20GB, for the first 3 months)
```

### Necessary documents

- Tick Doc 1 (nzcc_mobile_r1_issues_study_of_mobile_telecommunications_markets_in_ne.txt), role: Answer component
- Tick Doc 7 (nzcc_mobile_r1_issues_two_degrees_submission_on_the_issues_paper_26_oc.txt), role: Answer component

Leave unticked: Doc 2 (nzcc_mobile_r1_issues_chorus_submission_on_terms_of_reference_30_novem.txt), Doc 3 (nzcc_mobile_r1_issues_new_street_research_submission_on_terms_of_refer.txt), Doc 4 (nzcc_mobile_r1_issues_vocus_submission_on_terms_of_reference_30_novemb.txt), Doc 5 (nzcc_mobile_r1_issues_trustpower_analysys_mason_submission_on_terms_of.txt), Doc 6 (nzcc_mobile_r1_issues_bluereach_submission_on_terms_of_reference_6_dec.txt), Doc 8 (nzcc_mobile_r1_issues_two_degrees_covec_mobile_market_development_in_n.txt), Doc 9 (nzcc_mobile_r1_issues_vocus_submission_on_the_issues_paper_26_october_.txt), Doc 10 (nzcc_mobile_r1_issues_wispa_nz_submission_on_the_issues_paper_26_octob.txt), Doc 11 (nzcc_mobile_r1_issues_speedchecker_ltd_submission_on_the_issues_paper_.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Aggregation

Leave unticked: Temporal alignment, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike company

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Out-of-range period

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Look-alike company: Doc 1 prices Skinny Direct's 25GB plan at $65 beside 2degrees' $70; using it gives $1.80 more. Out-of-range period: Doc 7's 20GB lasts three months; applied all year it gives $0.05 less, ignored $2.70 more. The gold counts three doubled months: $1.60.
```

(44 / 50 words.)
