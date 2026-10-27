# aq-03570 q03 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03570 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 3, difficulty_target medium, origin claude.
- tested_sha256 e04413be595f6eabe746b12591ba2e273aeebe33b982510c65fef0382b2c22be: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D07 = Doc 7, D12 = Doc 12.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q03.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
In US SIF's 2022 figures for ESG fund assets by issue, the assets of funds addressing climate change as a stand-alone issue were what percentage larger than those of funds addressing the second-ranked issue? Give one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
91.7%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 12, the paragraph on investors' need for emissions information and its footnote 4): citing the US SIF Foundation's 2022 Report on US Sustainable Investing Trends, the letter says that of the $8.4 trillion in funds that consider ESG factors, $3.45 trillion address climate change/carbon and $1.23 trillion apply fossil fuel divestment policies.

Step 2. Source input (Doc 7, its account of US SIF's 2022 report and the section on climate-related greenwashing): the same report counts $8.4 trillion in funds that disclose an ESG investing methodology at the beginning of 2022. Doc 7 gives climate change and fossil fuel divestment a combined $4.8 trillion, and says the next largest ESG categories, military/weapons and tobacco, are addressed in funds with $1.8 trillion and $1.7 trillion.

Step 3. Application (Doc 7 and Doc 12): the $4.8 trillion covers two issues together, and Doc 12 gives each of them its own figure, so as a stand-alone issue the figure for funds addressing climate change is Doc 12's $3.45 trillion, which is still the largest. Fossil fuel divestment, at $1.23 trillion, is smaller than both military/weapons and tobacco, so the second-ranked issue is military/weapons at $1.8 trillion.

Step 4. Calculation (Doc 7 and Doc 12): the gap in trillion dollars: 3.45 - 1.8 = 1.65

Step 5. Final answer (Doc 7 and Doc 12): the gap as a percentage of the second-ranked issue's figure: 1.65 / 1.8 = 91.7% (to one decimal place)
```

### Answer components

Component 1

```text
91.7%
```

### Evidence

Evidence 1: document Doc 12 (sec_esg_disclosures_advisers_funds_s71722-458951-1174494.txt), proves component 1. 91.7% (local note: paragraph before "Our Approach", l24; Doc 12)

```text
of the $8.4 trillion AUM in funds that consider ESG factors in their investment decision-making, $3.45 trillion address climate change/carbon and $1.23 trillion apply fossil fuel divestment policies
```

Evidence 2: document Doc 12 (sec_esg_disclosures_advisers_funds_s71722-458951-1174494.txt), proves component 1. 91.7% (local note: footnote 4, l34; Doc 12)

```text
US SIF Foundation, 2022 Report on US Sustainable Investing Trends Executive Summary
```

Evidence 3: document Doc 7 (sec_esg_disclosures_advisers_funds_s71722-276419-672002.txt), proves component 1. 91.7% (local note: first section, l23; Doc 7)

```text
In its 2022 report tallying the assets under management (AUM) of ESG funds, the US SIF Foundation
```

Evidence 4: document Doc 7 (sec_esg_disclosures_advisers_funds_s71722-276419-672002.txt), proves component 1. 91.7% (local note: first section, l24; Doc 7)

```text
at the beginning of 2022, $8.4 trillion of U.S.-domiciled assets under professional management were funds that disclose an ESG investing methodology
```

Evidence 5: document Doc 7 (sec_esg_disclosures_advisers_funds_s71722-276419-672002.txt), proves component 1. 91.7% (local note: climate-related greenwashing section, l45; Doc 7)

```text
attention to climate change and fossil fuel divestment is by far the most significant of the ESG claims made by asset managers, addressed in funds with a combined $4.8 trillion in AUM
```

Evidence 6: document Doc 7 (sec_esg_disclosures_advisers_funds_s71722-276419-672002.txt), proves component 1. 91.7% (local note: climate-related greenwashing section, l45; Doc 7)

```text
The next largest ESG categories, military/weapons and tobacco, are addressed in funds with $1.8 trillion and $1.7 trillion in AUM, respectively.
```

### Necessary documents

- Tick Doc 7 (sec_esg_disclosures_advisers_funds_s71722-276419-672002.txt), role: Answer component
- Tick Doc 12 (sec_esg_disclosures_advisers_funds_s71722-458951-1174494.txt), role: Answer component

Leave unticked: Doc 1 (sec_esg_disclosures_advisers_funds_s71022-20149214-316483.txt), Doc 2 (sec_esg_disclosures_advisers_funds_s71722-20149095-316284.txt), Doc 3 (sec_esg_disclosures_advisers_funds_s71722-190239-374582.txt), Doc 4 (sec_esg_disclosures_advisers_funds_s71722-233101-486783.txt), Doc 5 (sec_esg_disclosures_advisers_funds_s71722-235999-492462.txt), Doc 6 (sec_esg_disclosures_advisers_funds_s70422-246959-547222.txt), Doc 8 (sec_esg_disclosures_advisers_funds_s71722-288759-704802.txt), Doc 9 (sec_esg_disclosures_advisers_funds_s71722-305579-785682.txt), Doc 10 (sec_esg_disclosures_advisers_funds_s71722-450259-1152422.txt), Doc 11 (sec_esg_disclosures_advisers_funds_s71722-457031-1170374.txt)

### Reasoning tags

Tick: Cross-document join, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Part vs total: Doc 7 gives climate change and fossil fuel divestment a combined $4.8 trillion beside military/weapons at $1.8 trillion. Taking that total for climate change gives 166.7%. Doc 12 splits it: climate change/carbon is $3.45 trillion, which is 91.7% larger than military/weapons.
```

(44 / 50 words.)
