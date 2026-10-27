# aq-02940 q05 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02940 --handover --q q05` from questions/q05.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 a928e83fa0400bda74ed5ac632d193a178f3ea88c78a8d8ffbf7c59ba436c692: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 4, D13 = Doc 1, D16 = Doc 14.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: six words shared with q04: 'both asb's and westpac's timing requests'
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q05.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Had the Commerce Commission's final decision come the day submissions closed, what is the earliest date the caps could start while satisfying both ASB's and Westpac's timing requests?
```

### Number of asks

1 ask

### Gold answer

```text
1 April 2027
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 1, Executive summary): the Commission asked for submissions on its draft decision by 12pm on Monday 13 July 2026, so submissions closed that day. In the question's case the final decision is announced that day.

Step 2. Source input (Doc 4, Recommendation 3): ASB asks for an implementation date no earlier than 8 months from the announcement date. The 2 months it gives the schemes and the 6 months it gives acquirers are parts of those 8 months, not further requests.

Step 3. Source input (Doc 14, end-of-year implementation section): Westpac asks for a minimum six-month implementation period, with changes taking effect from 1 March 2027 at the earliest, and for a first-of-month effective date.

Step 4. Final answer (Doc 1, Doc 4 and Doc 14): 8 months after 13 July 2026 is 13 March 2027. That is more than six months after the decision and later than 1 March 2027, so ASB's request sets the earliest day. It is not the first of a month, so Westpac's last request moves the start to the next one, 1 April 2027.
```

### Answer components

Component 1

```text
1 April 2027
```

### Evidence

Evidence 1: document Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), proves component 1. 1 April 2027 (local note: Executive summary, paragraph X17)

```text
Please submit your views by 12pm on Monday 13 July 2026.
```

Evidence 2: document Doc 4 (nzcc_interchange_r3_commercial_asb_submission_on_commercial_credit_card_interch.txt), proves component 1. 1 April 2027 (local note: ASB Recommendation 3)

```text
ASB Recommendation 3: Set an implementation date of no earlier than 8 months from the announcement date and Commission to direct the schemes to confirm applicable rates and criteria no later than 2 months from announcement date to allow acquirers 6 months for implementation.
```

Evidence 3: document Doc 14 (nzcc_interchange_r3_commercial_westpac_submission_on_commercial_credit_card_int.txt), proves component 1. 1 April 2027 (local note: paragraph 3.21)

```text
Westpac considers that a minimum six-month implementation period, with changes taking effect from 1 March 2027 at the earliest, would better support orderly delivery, reduce customer disruption and maintain the stability of critical payments infrastructure.
```

Evidence 4: document Doc 14 (nzcc_interchange_r3_commercial_westpac_submission_on_commercial_credit_card_int.txt), proves component 1. 1 April 2027 (local note: paragraph 3.23)

```text
Additionally, any interchange changes should align with a first-of-month effective date.
```

### Necessary documents

- Tick Doc 1 (nzcc_interchange_r3_commercial_retail_payment_system_commercial_credit_card_int.txt), role: Used to identify
- Tick Doc 4 (nzcc_interchange_r3_commercial_asb_submission_on_commercial_credit_card_interch.txt), role: Answer component
- Tick Doc 14 (nzcc_interchange_r3_commercial_westpac_submission_on_commercial_credit_card_int.txt), role: Answer component

Leave unticked: Doc 2 (nzcc_interchange_r3_commercial_merchant_survey_summary_produced_by_commerce_com.txt), Doc 3 (nzcc_interchange_r3_commercial_anz_submission_on_commercial_credit_card_interch.txt), Doc 5 (nzcc_interchange_r3_commercial_bnz_submission_on_commercial_credit_card_interch.txt), Doc 6 (nzcc_interchange_r3_commercial_citibank_na_nz_submission_on_commercial_credit_c.txt), Doc 7 (nzcc_interchange_r3_commercial_fsf_submission_on_commercial_credit_card_interch.txt), Doc 8 (nzcc_interchange_r3_commercial_keystone_report_on_behalf_of_mastercard_submissi.txt), Doc 9 (nzcc_interchange_r3_commercial_kiwibank_submission_on_commercial_credit_card_in.txt), Doc 10 (nzcc_interchange_r3_commercial_mastercard_submission_on_commercial_credit_card_.txt), Doc 11 (nzcc_interchange_r3_commercial_retail_nz_submission_on_commercial_credit_card_i.txt), Doc 12 (nzcc_interchange_r3_commercial_revolut_submission_on_commercial_credit_card_int.txt), Doc 13 (nzcc_interchange_r3_commercial_tsb_submission_on_commercial_credit_card_interch.txt), Doc 15 (nzcc_interchange_r3_commercial_paymark_submission_on_commercial_credit_card_int.txt), Doc 16 (nzcc_interchange_r3_commercial_restaurant_association_of_nz_submission_on_comme.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment

Leave unticked: Unit normalization, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 14 prints 1 March 2027 as Westpac's earliest date. Linking Doc 4's 8 months from Doc 1's 13 July 2026 deadline gives 13 March 2027, and Westpac's separate first-of-month request then makes the gold 1 April 2027.
```

(41 / 50 words.)
