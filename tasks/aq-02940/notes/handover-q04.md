# aq-02940 q04 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02940 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 3, difficulty_target medium, origin claude.
- tested_sha256 0a5f5f6925378d3db3d3d6fa9fb375ef0a55d92e74d53706b223d41f6386dabe: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D08 = Doc 10, D13 = Doc 1, D16 = Doc 14.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: six words shared with q06: 'both mastercard's minimum lead times and'
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Had the Commerce Commission's final decision come on its deadline for submissions, how many days later could the highest of its proposed caps first start while satisfying both Mastercard's minimum lead times and Westpac's timing requests?
```

### Number of asks

1 ask

### Gold answer

```text
384 days
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, Executive summary): the Commission asked for submissions on its draft decision by 12pm on Monday 13 July 2026. In the question's case the final decision is announced that day.

Step 2. Source input (Doc 1, Executive summary table and Chapter 3): the proposed caps are 0.50% and 0.90% for domestic commercial credit used in person and online, and 0.70% and 1.50% for foreign-issued commercial credit used in person and online. The highest, 1.50%, is the cap on foreign-issued cards used online.

Step 3. Source input (Doc 10, Implementation Timing and response to question 8): Mastercard asks for a minimum of nine months for domestic rate changes and twelve months for cross-border changes, from the date of final announcement. It calls the earlier caps on foreign-issued cards the cross-border changes, so the longer minimum is the one for this cap.

Step 4. Source input (Doc 14, end-of-year implementation section): Westpac asks for a minimum six-month implementation period, with changes taking effect from 1 March 2027 at the earliest, and for a first-of-month effective date.

Step 5. Application (Doc 1, Doc 10 and Doc 14): 12 months after 13 July 2026 is 13 July 2027. That is more than six months after the decision and later than 1 March 2027, but it is not the first of a month, so Westpac's last request moves the start to the next one, 1 August 2027.

Step 6. Calculation (Doc 1 and Doc 14): July has 13 days up to the 13th and 18 after it, so its length in days is: 13 + 18 = 31

Step 7. Calculation (Doc 1 and Doc 14): the year from 13 July 2026 to 13 July 2027 spans 12 months, and if each were as long as July it would hold: 12 × 31 = 372

Step 8. Calculation (Doc 1 and Doc 14): September, November, April and June are each 1 day shorter than July and February 2027 is 3 days shorter: 1 + 1 + 3 + 1 + 1 = 7

Step 9. Calculation (Doc 1 and Doc 14): days from 13 July 2026 to 13 July 2027: 372 - 7 = 365

Step 10. Final answer (Doc 1, Doc 10 and Doc 14): that year, the 18 days left in July 2027 and the first day of August: 365 + 18 + 1 = 384
```

### Answer components

Component 1

```text
384 days
```

### Evidence

Evidence 1: document Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), proves component 1. 384 days (local note: Executive summary, paragraph X17)

```text
Please submit your views by 12pm on Monday 13 July 2026.
```

Evidence 2: document Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), proves component 1. 384 days (local note: Chapter 3, foreign-issued commercial credit)

```text
Our draft decision is to apply a 0.70% cap to foreign-issued in-person commercial credit card interchange fees and 1.50% to foreign-issued online commercial credit card interchange fees.
```

Evidence 3: document Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), proves component 1. 384 days (local note: Chapter 3, domestic issued commercial credit)

```text
Our draft decision is to apply a 0.50% cap to domestic in-person commercial credit and 0.90% to domestic online commercial credit.
```

Evidence 4: document Doc 10 (nzcc_interchange_r3_commercial_mastercard_submission_on_commercial_credit_card_.txt), proves component 1. 384 days (local note: Implementation Timing)

```text
A minimum of nine months is required for domestic rate changes and twelve months for cross-border changes, from the date of final announcement.
```

Evidence 5: document Doc 10 (nzcc_interchange_r3_commercial_mastercard_submission_on_commercial_credit_card_.txt), proves component 1. 384 days (local note: response to question 8)

```text
The compressed timelines for the July 2025 domestic changes (effective 1 December 2025) and the May 2026 cross-border changes
```

Evidence 6: document Doc 10 (nzcc_interchange_r3_commercial_mastercard_submission_on_commercial_credit_card_.txt), proves component 1. 384 days (local note: Evidentiary basis)

```text
It pre-dates both the December 2025 domestic interchange reductions on personal cards and the May 2026 caps on foreign-issued cards
```

Evidence 7: document Doc 14 (nzcc_interchange_r3_commercial_westpac_submission_on_commercial_credit_card_int.txt), proves component 1. 384 days (local note: paragraph 3.21)

```text
Westpac considers that a minimum six-month implementation period, with changes taking effect from 1 March 2027 at the earliest, would better support orderly delivery, reduce customer disruption and maintain the stability of critical payments infrastructure.
```

Evidence 8: document Doc 14 (nzcc_interchange_r3_commercial_westpac_submission_on_commercial_credit_card_int.txt), proves component 1. 384 days (local note: paragraph 3.23)

```text
Additionally, any interchange changes should align with a first-of-month effective date.
```

### Necessary documents

- Tick Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), role: Answer component
- Tick Doc 10 (nzcc_interchange_r3_commercial_mastercard_submission_on_commercial_credit_card_.txt), role: Answer component
- Tick Doc 14 (nzcc_interchange_r3_commercial_westpac_submission_on_commercial_credit_card_int.txt), role: Answer component

Leave unticked: Doc 2 (nzcc_interchange_r3_commercial_merchant_survey_summary_produced_by_commerce_com.txt), Doc 3 (nzcc_interchange_r3_commercial_anz_submission_on_commercial_credit_card_interch.txt), Doc 4 (nzcc_interchange_r3_commercial_asb_submission_on_commercial_credit_card_interch.txt), Doc 5 (nzcc_interchange_r3_commercial_bnz_submission_on_commercial_credit_card_interch.txt), Doc 6 (nzcc_interchange_r3_commercial_citibank_na_nz_submission_on_commercial_credit_c.txt), Doc 7 (nzcc_interchange_r3_commercial_fsf_submission_on_commercial_credit_card_interch.txt), Doc 8 (nzcc_interchange_r3_commercial_keystone_report_on_behalf_of_mastercard_submissi.txt), Doc 9 (nzcc_interchange_r3_commercial_kiwibank_submission_on_commercial_credit_card_in.txt), Doc 11 (nzcc_interchange_r3_commercial_retail_nz_submission_on_commercial_credit_card_i.txt), Doc 12 (nzcc_interchange_r3_commercial_revolut_submission_on_commercial_credit_card_int.txt), Doc 13 (nzcc_interchange_r3_commercial_tsb_submission_on_commercial_credit_card_interch.txt), Doc 15 (nzcc_interchange_r3_commercial_paymark_submission_on_commercial_credit_card_int.txt), Doc 16 (nzcc_interchange_r3_commercial_restaurant_association_of_nz_submission_on_comme.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Wrong jurisdiction or scope

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Linking across documents: stopping at Mastercard's twelve months in Doc 10, 13 July 2027, gives 365 days; Westpac's first-of-month request in Doc 14 makes it 384. Wrong jurisdiction or scope: Mastercard's nine-month domestic minimum, taken for the highest cap, which Doc 1 sets for foreign-issued cards, gives 292.
```

(48 / 50 words.)
