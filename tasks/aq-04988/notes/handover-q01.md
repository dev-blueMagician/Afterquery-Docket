# aq-04988 q01 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04988 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 4d36678e54a5fb6d8d7d40c6b421a3ac5748ee032f1abc3d3791669e3fd7dfec: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 7, D04 = Doc 2.
- Floor: 0 FAIL, 5 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN units: the answer is a bare number; give its units (form: 'short and checkable, with units')
  - WARN form-numbers: Step 1: Doc 7 doesn't mention 11.2. Doc 7 prints it first at character 29,823, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 1: Doc 7 doesn't mention 9.2. Doc 7 prints it first at character 29,832, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 2: Doc 2 doesn't mention 0.58. Doc 2 prints it first at character 22,476, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Argentina's 2011-2015 fall in mean salt intake was how many times the average cut a review credits to mandatory reformulation alone? Answer to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
1.4
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, table of countries with reported data on change in mean salt intake, Argentina row, the timescale the question names): Argentina's mean salt intake, measured by urine collection, fell from 11.2 g a day to 9.2 g a day.
Step 2. Source input (Doc 2, discussion of a systematic review of salt reduction policies): "Mandatory reformulation alone could achieve a reduction averaging around 0.58g/day". That sentence names no nutrient. The sentence before it gives the same review's reductions as "reductions in sodium consumption", and the sentence after it as reductions in "sodium intake", so the 0.58 g is a cut in sodium, not in salt.
Step 3. Source input (Doc 2, results): Brazil's modelled decline is given as "0.1 g/day of sodium" and, in brackets, as "0.25 g/day salt", which is the conversion Doc 2 uses between sodium and salt.
Step 4. Calculation (Doc 2): 0.25 / 0.1 = 2.5 (grams of salt per gram of sodium, derived).
Step 5. Calculation (Doc 7 and Doc 2): 11.2 / 2.5 = 4.48 (Argentina's starting intake in grams of sodium a day, derived).
Step 6. Calculation (Doc 7 and Doc 2): 9.2 / 2.5 = 3.68 (Argentina's end intake in grams of sodium a day, derived).
Step 7. Calculation (Doc 7 and Doc 2): 4.48 - 3.68 = 0.8 (Argentina's fall in grams of sodium a day, derived).
Step 8. Calculation (Doc 7 and Doc 2): 0.8 / 0.58 = 137.9% (Argentina's fall as a percentage of the review's average cut for mandatory reformulation alone, derived; multiplying by 100 converts the ratio to percent).
Step 9. Final answer (Doc 7 and Doc 2): Argentina's fall was 137.9% of that cut, which is 1.4 times to one decimal place.
```

### Answer components

Component 1

```text
1.4
```

### Evidence

Evidence 1: document Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), proves component 1. 1.4 (local note: Doc 7, results, title of the table of salt intake changes)

```text
Countries with reported data on change in mean salt intake over time
```

Evidence 2: document Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), proves component 1. 1.4 (local note: Doc 7, same table, Argentina row)

```text
|Argentina (18)|2011–2015|24-hour urine|11.2g to 9.2g; −18%|
```

Evidence 3: document Doc 2 (Estimating-the-health-and-economic-effects-of-the-voluntary.txt), proves component 1. 1.4 (local note: Doc 2, discussion)

```text
A systematic review of 70 papers concluded that multi-component strategies
```

Evidence 4: document Doc 2 (Estimating-the-health-and-economic-effects-of-the-voluntary.txt), proves component 1. 1.4 (local note: Doc 2, discussion, same sentence)

```text
generally achieved the most considerable reductions in sodium consumption across an entire population, most notably 1.6g/day in Finland and Japan, 1.2g/day in Turkey, and 0.52g/day recently in the UK
```

Evidence 5: document Doc 2 (Estimating-the-health-and-economic-effects-of-the-voluntary.txt), proves component 1. 1.4 (local note: Doc 2, discussion, next sentence)

```text
Mandatory reformulation alone could achieve a reduction averaging around 0.58g/day (three separate studies)
```

Evidence 6: document Doc 2 (Estimating-the-health-and-economic-effects-of-the-voluntary.txt), proves component 1. 1.4 (local note: Doc 2, discussion, sentence after)

```text
Tax and community-based counselling could each typically reduce sodium intake by 0.12g/day
```

Evidence 7: document Doc 2 (Estimating-the-health-and-economic-effects-of-the-voluntary.txt), proves component 1. 1.4 (local note: Doc 2, results)

```text
have led to a 0.1 g/day of sodium decline in sodium consumption (0.25 g/day salt) from 2011 to 2017
```

### Necessary documents

- Tick Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), role: Answer component
- Tick Doc 2 (Estimating-the-health-and-economic-effects-of-the-voluntary.txt), role: Answer component

Leave unticked: Doc 1 (The-estimated-health-impact-of-sodium-reduction-through-food.txt), Doc 3 (Sodium-in-the-New-Zealand-diet-proposed-voluntary-food.txt), Doc 4 (Cross-sectional-comparisons-of-sodium-content-in-processed.txt), Doc 5 (Reduction-of-Cardiovascular-Events-and-Related-Healthcare.txt), Doc 6 (Systematic-Review-on-International-Salt-Reduction-Policy-in.txt), Doc 8 (Salty-and-Savoury-Snacks-Compliance-with-2016-and-2019.txt), Doc 9 (Implementing-effective-salt-reduction-programs-and-policies.txt), Doc 10 (An-evaluation-of-the-Victorian-Salt-Reduction-Partnerships.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization

Leave unticked: Temporal alignment, Conditional filter, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Rounding, scale or sign

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 2's review gives mandatory reformulation's average cut, 0.58 g/day, in sodium, while Doc 7's Argentina row is salt, 11.2 to 9.2 g. A careless solver divides 2.0 by 0.58 and answers 3.4; converting with Doc 2's own sodium-to-salt figures gives 1.4.
```

(45 / 50 words.)
