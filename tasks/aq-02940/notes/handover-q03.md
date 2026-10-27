# aq-02940 q03 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02940 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 f1d02a0a83cdc3fd12ab485992cd936ca6c4025da3c86a94325f216762247183: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D11 = Doc 16, D13 = Doc 1.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN precision: the answer is a rate or decimal; state the precision in the question
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
By how many percentage points does commercial credit merchant service fees' share of everything New Zealand businesses pay to accept Visa and Mastercard exceed commercial credit's share of total transaction value?
```

### Number of asks

1 ask

### Gold answer

```text
9 percentage points
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 16, the Association's position): the Commission estimates that businesses pay approximately $1 billion per year overall to accept Visa and Mastercard payments, and $170 million a year in merchant service fees on Mastercard and Visa commercial credit card payments.

Step 2. Source input (Doc 1, Executive summary): commercial credit transactions account for 8% of the total value of transactions. The 19% printed beside it is commercial credit's share of interchange fees, which are one component of merchant service fees, so it is not the share asked for.

Step 3. Calculation (Doc 16 and Doc 1): both documents print the $170 million. Since 1% of $1 billion is $10 million, its share of the overall amount in percent is: 170 / 10 = 17

Step 4. Final answer (Doc 16 and Doc 1): fee share less value share, in percentage points: 17 - 8 = 9
```

### Answer components

Component 1

```text
9 percentage points
```

### Evidence

Evidence 1: document Doc 16 (nzcc_interchange_r3_commercial_restaurant_association_of_nz_submission_on_comme.txt), proves component 1. 9 percentage points (local note: Our position, cost of card acceptance)

```text
The Commission estimates that businesses pay approximately $1 billion per year overall to accept Visa and Mastercard payments and pay $170 million annually in merchant service fees for Mastercard and Visa commercial credit card payments
```

Evidence 2: document Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), proves component 1. 9 percentage points (local note: Executive summary, paragraph X4)

```text
This represents around 19% of total interchange fees paid, despite commercial credit transactions accounting for only 8% of the total value of transactions.
```

### Necessary documents

- Tick Doc 16 (nzcc_interchange_r3_commercial_restaurant_association_of_nz_submission_on_comme.txt), role: Answer component
- Tick Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), role: Answer component

Leave unticked: Doc 2 (nzcc_interchange_r3_commercial_merchant_survey_summary_produced_by_commerce_com.txt), Doc 3 (nzcc_interchange_r3_commercial_anz_submission_on_commercial_credit_card_interch.txt), Doc 4 (nzcc_interchange_r3_commercial_asb_submission_on_commercial_credit_card_interch.txt), Doc 5 (nzcc_interchange_r3_commercial_bnz_submission_on_commercial_credit_card_interch.txt), Doc 6 (nzcc_interchange_r3_commercial_citibank_na_nz_submission_on_commercial_credit_c.txt), Doc 7 (nzcc_interchange_r3_commercial_fsf_submission_on_commercial_credit_card_interch.txt), Doc 8 (nzcc_interchange_r3_commercial_keystone_report_on_behalf_of_mastercard_submissi.txt), Doc 9 (nzcc_interchange_r3_commercial_kiwibank_submission_on_commercial_credit_card_in.txt), Doc 10 (nzcc_interchange_r3_commercial_mastercard_submission_on_commercial_credit_card_.txt), Doc 11 (nzcc_interchange_r3_commercial_retail_nz_submission_on_commercial_credit_card_i.txt), Doc 12 (nzcc_interchange_r3_commercial_revolut_submission_on_commercial_credit_card_int.txt), Doc 13 (nzcc_interchange_r3_commercial_tsb_submission_on_commercial_credit_card_interch.txt), Doc 14 (nzcc_interchange_r3_commercial_westpac_submission_on_commercial_credit_card_int.txt), Doc 15 (nzcc_interchange_r3_commercial_paymark_submission_on_commercial_credit_card_int.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization

Leave unticked: Temporal alignment, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 1's summary prints commercial credit's 19% share of interchange fees beside its 8% share of transaction value, giving 11 points. The question asks about merchant service fees: $170 million of Doc 16's $1 billion is 17%, so the gold is 9 points.
```

(45 / 50 words.)
