# aq-02940 q01 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02940 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 a171d32d06e179ff23e046d0e9deca285c8b26f0e92d5b9c9a223ff512b1b0a2: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D06 = Doc 8, D13 = Doc 1.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 3: Doc 8 doesn't mention 0.39%. expected false alarm: Doc 8 prints it at character 141,016, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN form-numbers: Step 5: Docs 1 and 8 don't mention 0.39. expected false alarm: Doc 8 prints it at character 141,016, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
  - WARN sibling: q02 has the same answer; do the two ask for the same fact?
  - WARN sibling: six words shared with q02: 'caps save merchants yearly in $'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
If merchant service fees fell by the percentage a Spanish study found per 1% interchange cut, what would the Commerce Commission's proposed commercial credit caps save merchants yearly, in $ million to one decimal?
```

### Number of asks

1 ask

### Gold answer

```text
$26.5 million
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, Executive summary): New Zealand merchants pay approximately $125 million a year in interchange fees to accept commercial credit cards, and the Commission estimates that its draft decision would reduce those fees by $50 million.

Step 2. Source input (Doc 1, Introduction): merchants pay approximately $170 million a year in merchant service fees to accept Mastercard and Visa commercial credit card payments.

Step 3. Source input (Doc 8, section on acquirers and pass-through): a Spanish study estimates that a 1% reduction in interchange fees is associated in the long run with a 0.39% reduction in merchant service fees. Both figures are percentages of the fee they describe, so the study's figure applies to the percentage cut in interchange, not to its dollar amount.

Step 4. Calculation (Doc 1): share of commercial credit interchange that the proposed caps remove: 50 / 125 = 0.4

Step 5. Calculation (Doc 1 and Doc 8): share of merchant service fees removed at the study's rate: 0.4 × 0.39 = 0.156

Step 6. Final answer (Doc 1 and Doc 8): yearly saving in $ million: 0.156 × 170 = 26.52. To one decimal place the second decimal drops, giving the gold answer.
```

### Answer components

Component 1

```text
$26.5 million
```

### Evidence

Evidence 1: document Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), proves component 1. $26.5 million (local note: Executive summary, paragraph X4)

```text
New Zealand merchants currently pay approximately $125 million per year in interchange fees to accept domestic and foreign-issued commercial credit cards.
```

Evidence 2: document Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), proves component 1. $26.5 million (local note: Executive summary, paragraph X14)

```text
we estimate the draft decision would reduce commercial credit interchange fees by $50 million.
```

Evidence 3: document Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), proves component 1. $26.5 million (local note: Chapter 1, paragraph 1.4)

```text
Merchants currently pay approximately $170 million in merchant service fees each year to accept Mastercard and Visa commercial credit card payments.
```

Evidence 4: document Doc 8 (nzcc_interchange_r3_commercial_keystone_report_on_behalf_of_mastercard_submissi.txt), proves component 1. $26.5 million (local note: section 5.2.3, acquirers and pass-through)

```text
one Spanish study estimates that a 1% reduction in interchange fees is associated in the long run with a 0.39% reduction in MSFs, suggesting partial rather than full pass-through.
```

### Necessary documents

- Tick Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), role: Answer component
- Tick Doc 8 (nzcc_interchange_r3_commercial_keystone_report_on_behalf_of_mastercard_submissi.txt), role: Answer component

Leave unticked: Doc 2 (nzcc_interchange_r3_commercial_merchant_survey_summary_produced_by_commerce_com.txt), Doc 3 (nzcc_interchange_r3_commercial_anz_submission_on_commercial_credit_card_interch.txt), Doc 4 (nzcc_interchange_r3_commercial_asb_submission_on_commercial_credit_card_interch.txt), Doc 5 (nzcc_interchange_r3_commercial_bnz_submission_on_commercial_credit_card_interch.txt), Doc 6 (nzcc_interchange_r3_commercial_citibank_na_nz_submission_on_commercial_credit_c.txt), Doc 7 (nzcc_interchange_r3_commercial_fsf_submission_on_commercial_credit_card_interch.txt), Doc 9 (nzcc_interchange_r3_commercial_kiwibank_submission_on_commercial_credit_card_in.txt), Doc 10 (nzcc_interchange_r3_commercial_mastercard_submission_on_commercial_credit_card_.txt), Doc 11 (nzcc_interchange_r3_commercial_retail_nz_submission_on_commercial_credit_card_i.txt), Doc 12 (nzcc_interchange_r3_commercial_revolut_submission_on_commercial_credit_card_int.txt), Doc 13 (nzcc_interchange_r3_commercial_tsb_submission_on_commercial_credit_card_interch.txt), Doc 14 (nzcc_interchange_r3_commercial_westpac_submission_on_commercial_credit_card_int.txt), Doc 15 (nzcc_interchange_r3_commercial_paymark_submission_on_commercial_credit_card_int.txt), Doc 16 (nzcc_interchange_r3_commercial_restaurant_association_of_nz_submission_on_comme.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization

Leave unticked: Temporal alignment, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 8's Spanish study gives a 0.39% fee fall per 1% interchange cut; multiplying Doc 1's $50 million cut by 0.39 gives $19.5 million. Look-alike measure: 15.6% of Doc 1's $125 million interchange, not its $170 million merchant service fees, gives $19.5 million. Gold $26.5 million.
```

(49 / 50 words.)
