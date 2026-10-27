# aq-02086 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02086 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 6ba84dabf46910a845ac9246aaf3b1593f1d43a34db562c5764e961383ee0878: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 1, D03 = Doc 2.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Under the consultation-stage impact assessment's assumptions, how many staff hours a year would the Ishak family's landlord spend preparing additional written summaries?
```

### Number of asks

1 ask

### Gold answer

```text
2,400 hours
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 1, Annex C glossary entry for Rochdale Boroughwide Housing): the housing association the Ishak family rented their social home from is a housing society with 12,000 homes throughout Rochdale.

Step 2. Source fact (Doc 2, preparation and posting costs for written summaries): the impact assessment assumes 4 repairs per property are carried out per year, the upper bound of the Housemark estimate.

Step 3. Source fact (Doc 2, same section): it takes the English Housing Survey estimate that 40% of faults are urgent as the proportion of responsive repairs requiring a written report to tenants.

Step 4. Source fact (Doc 2, same section): it assumes only 50% of these reports will be an additional burden, because some landlords already give tenants this information.

Step 5. Source fact (Doc 2, same section): it assumes 15 minutes of staff time per report sent.

Step 6. Calculation (from Steps 1 and 2; Doc 1 and Doc 2), repairs a year at the landlord: 12,000 * 4 = 48,000 repairs.

Step 7. Calculation (from Steps 3 and 6; Doc 1 and Doc 2), repairs needing a written summary: 48,000 * 40% = 19,200 summaries.

Step 8. Calculation (from Steps 4 and 7; Doc 1 and Doc 2), additional written summaries a year: 19,200 * 50% = 9,600 summaries.

Step 9. Calculation (from Steps 5 and 8; Doc 1 and Doc 2), staff time a year in minutes: 9,600 * 15 = 144,000 minutes.

Step 10. Calculation (from Step 9; Doc 1 and Doc 2; 60 minutes per hour is a unit convention), staff time a year in hours: 144,000 / 60 = 2,400 hours.
```

### Answer components

Component 1

```text
2,400
```

### Evidence

Evidence 1: document Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), proves component 1. 2,400 (local note: L1047, Annex C glossary)

```text
Resident and employee co-owned housing society, with 12,000 homes throughout Rochdale. This was Housing Association the Ishak family rented their social home from.
```

Evidence 2: document Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), proves component 1. 2,400 (local note: L482, written summaries)

```text
Housemark estimate, that 4 repairs per property are carried out per year
```

Evidence 3: document Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), proves component 1. 2,400 (local note: L483, written summaries)

```text
Using the EHS estimate that 40% of faults are classified as requiring an urgent repair as a proxy for the proportion of responsive repairs requiring a report to be provided to tenants
```

Evidence 4: document Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), proves component 1. 2,400 (local note: L484, written summaries)

```text
we have assumed that only 50% of these reports will be an additional burden to the sector
```

Evidence 5: document Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), proves component 1. 2,400 (local note: L474, preparation costs)

```text
we have assumed that it will take 15 minutes of staff time per report sent
```

### Necessary documents

- Tick Doc 1 (Awaabs-Law-consultation-on-timescales-for-repairs-in-the.txt), role: Answer component
- Tick Doc 2 (Awaabs-Law-consultation-stage-impact-assessment.txt), role: Answer component

Leave unticked: Doc 3 (Awaabs-Law-government-response.txt), Doc 4 (A-Decent-Homes-Standard-in-the-private-rented-sector.txt), Doc 5 (Response-to-the-consultation-on-a-Decent-Homes-Standard-in.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Entity resolution

Leave unticked: Temporal alignment, Conditional filter, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Doc 2 cites survey responses of 4.2 repairs per property but adopts 4; using 4.2 gives 2,520 hours. Doc 2 counts only 50% of required summaries as additional; all 19,200 give 4,800 hours. Gold: 12,000 homes (Doc 1) x 4 x 40% x 50% x 15 minutes.
```

(47 / 50 words.)
