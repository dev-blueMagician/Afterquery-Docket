# aq-03736 q01 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03736 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 1355d693a4d11dc3555809a8f60170bbddc51869718dd6f59546c1a2c59bb6f0: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 1, D02 = Doc 3.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 8: Doc 3 doesn't mention 2029. expected false alarm: Doc 3 prints it at character 185,866, past the 60,000 characters the form is taken to read, in a passage quoted as evidence; no wording clears it, so say so with the hand-over
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
An EU company that must publish its due diligence statement always has 6,000 employees, EUR 1.2 billion worldwide turnover and accounts closed each 30 June. Had the Commission's proposal entered into force when the adopted directive did, how many months after its first statement deadline under the proposal does the first accounting year its directive statement must cover end?
```

### Number of asks

1 ask

### Gold answer

```text
38 months
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 3, Official Journal header and the article headed "Entry into force"): the directive was published on 5.7.2024 and enters into force on the twentieth day following its publication. Counting on from the fifth of July: 5 + 20 = 25. It therefore entered into force on that day of July 2024, the date its review article also prints. On the question's supposition the proposal enters into force on the same day.
Step 2. Source input (Doc 1, scope article, point (a)): a company formed under the law of a Member State with more than 500 employees on average and a net worldwide turnover above the amount set in the same point is a point (a) company. The posed company is above both.
Step 3. Source input (Doc 1, transposition article): the rules apply to point (a) companies from 2 years from the entry into force.
Step 4. Source input (Doc 1, article headed "Communicating"): the annual statement "shall be published by 30 April each year, covering the previous calendar year".
Step 5. Calculation (Doc 1 and Doc 3): 2024 + 2 = 2026, so the proposal's rules reach the company in late July of that year.
Step 6. Calculation (Doc 1 and Doc 3): the first 30 April after that falls in the next year: 2026 + 1 = 2027. That 30 April is the first statement deadline under the proposal.
Step 7. Source input (Doc 3, transposition article, first group): the first group must exceed both a head-count and a turnover amount. The posed company exceeds the head-count but not the turnover, so it is not in the first group.
Step 8. Source input (Doc 3, transposition article, second group): the posed company exceeds both amounts set for the second group, and for that group the statement duty applies "for financial years starting on or after 1 January 2029". Calculation: 2029 - 1 = 2028. With accounts closed at the end of June, the company's accounting year (its financial year) runs from July to June. The year that began in July of that earlier year started before the date, so it does not count. The first year starting on or after the date begins in July 2029 and ends at the close of June 2030.
Step 9. Final answer (Doc 1 and Doc 3): from 30 April 2027 to 30 April 2030 is three years of 12 months, and the close of June 2030 is 2 months later: 12 + 12 + 12 + 2 = 38 months.
```

### Answer components

Component 1

```text
38 months
```

### Evidence

Evidence 1: document Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), proves component 1. 38 months (local note: Article 38, L1055)

```text
This Directive shall enter into force on the twentieth day following that of its publication in the Official Journal of the European Union.
```

Evidence 2: document Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), proves component 1. 38 months (local note: Article 36(1), L1011)

```text
It shall be published at the earliest possible opportunity after 25 July 2024, but no later than 26 July 2026.
```

Evidence 3: document Doc 1 (com-2022-71-proposal-for-a-directive-on-corporate-sustainability-due-diligence.txt), proves component 1. 38 months (local note: Article 2(1)(a), L551)

```text
the company had more than 500 employees on average and had a net worldwide turnover of more than EUR 150 million in the last financial year for which annual financial statements have been prepared;
```

Evidence 4: document Doc 1 (com-2022-71-proposal-for-a-directive-on-corporate-sustainability-due-diligence.txt), proves component 1. 38 months (local note: Article 30(1)(a), L1063)

```text
2 years from the entry into force of this Directive] as regards companies referred to in Article 2(1), point (a), and Article 2(2), point (a);
```

Evidence 5: document Doc 1 (com-2022-71-proposal-for-a-directive-on-corporate-sustainability-due-diligence.txt), proves component 1. 38 months (local note: Article 11, L821)

```text
The statement shall be published by 30 April each year, covering the previous calendar year.
```

Evidence 6: document Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), proves component 1. 38 months (local note: Article 37(1)(a), L1037)

```text
that had more than 5 000 employees on average and generated a net worldwide turnover of more than EUR 1 500 000 000 in the last financial year preceding 26 July 2027
```

Evidence 7: document Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), proves component 1. 38 months (local note: Article 37(1)(b), L1039)

```text
from 26 July 2028 as regards companies referred to in Article 2(1), points (a) and (b), which are formed in accordance with the legislation of the Member State and that had more than 3 000 employees on average and generated a net worldwide turnover of more than EUR 900 000 000 in the last financial year preceding 26 July 2028 for which annual financial statements have been or should have been adopted, with the exception of the measures necessary to comply with Article 16, which Member States shall apply to those companies for financial years starting on or after 1 January 2029
```

### Necessary documents

- Tick Doc 1 (com-2022-71-proposal-for-a-directive-on-corporate-sustainability-due-diligence.txt), role: Answer component
- Tick Doc 3 (directive-eu-2024-1760-on-corporate-sustainability-due-diligence.txt), role: Answer component

Leave unticked: Doc 2 (swd-2022-43-executive-summary-of-the-impact-assessment-report-accompanying-the-csdd-proposal.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Out-of-range period

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Out-of-range period: Doc 3's phase-in sentence ends by applying the statement duty only to financial years starting on or after 1 January 2029. The July-June year in which the rules start, ending 30 June 2029, is outside it, giving 26 months. The first year inside ends 30 June 2030: 38.
```

(50 / 50 words.)
