# aq-04988 q02 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04988 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 690ceb30daf99d042d7791cfe2238ba84829d9b0e467f66d83eb3df7ea8c3aae: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 7, D05 = Doc 9.
- Floor: 0 FAIL, 8 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: D05: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
  - WARN form-numbers: Step 1: Doc 7 doesn't mention 24. Doc 7 prints it first at character 24,641, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 7 doesn't mention 11.2. Doc 7 prints it first at character 29,823, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 3: Doc 7 doesn't mention 9.2. Doc 7 prints it first at character 29,832, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 5: Doc 7 doesn't mention 18.0. Doc 7 prints it first at character 22,254, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 6: Doc 7 doesn't mention 18.0. Doc 7 prints it first at character 22,254, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN form-numbers: Step 7: Doc 7 doesn't mention 18.0. Doc 7 prints it first at character 22,254, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What is the largest percentage fall in a country's mean salt intake between two whole-country 24-hour urine surveys? Answer to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
16.7%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, table of countries with reported data on change in mean salt intake): the rows whose assessment method is 24-hour urine are Argentina, Australia, Fiji, Finland, Italy, the Netherlands, Samoa, Slovenia, Switzerland, Turkey and the United Kingdom.
Step 2. Source input (Doc 7, same table and its footnote): the Australian row (Victoria) and the Finnish rows (Kuopio area, North Karelia, Southwestern Finland) carry the mark for "Change in salt intake measured at the subnational level", so they are not pairs of whole-country surveys. The other urine rows carry no mark.
Step 3. Source input (Doc 7, Argentina row): mean salt intake fell from 11.2 g a day to 9.2 g a day, the largest fall among the unmarked urine rows.
Step 4. Source input (Doc 9, surveillance table and discussion): Argentina's salt intake measurement by this method is listed as a "Regional survey", the discussion says "Argentina and South Africa conducted regional surveys to measure salt intake using 24-h urines", and only Mongolia had a national measure by this method at baseline. So Argentina's urine pair in Doc 7 is not a pair of whole-country surveys, and it is left out.
Step 5. Source input (Doc 7, Turkey row): mean salt intake fell from 18.0 g a day to 15.0 g a day; the row carries no subnational mark.
Step 6. Calculation (Doc 7): 18.0 - 15.0 = 3.0 (Turkey's fall in grams of salt a day, derived).
Step 7. Calculation (Doc 7): 3.0 / 18.0 = 16.7% (Turkey's fall as a share of its first survey's intake, derived and expressed as a percentage).
Step 8. Source input (Doc 7, remaining unmarked urine rows): Fiji, Italy, the Netherlands, Samoa, Slovenia, Switzerland and the United Kingdom all show smaller falls than Turkey's, or rises.
Step 9. Final answer (Doc 7 and Doc 9): the largest fall between two whole-country 24-hour urine surveys is Turkey's, 16.7% to one decimal place.
```

### Answer components

Component 1

```text
16.7%
```

### Evidence

Evidence 1: document Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), proves component 1. 16.7% (local note: Doc 7, results, title of the table of salt intake changes)

```text
Countries with reported data on change in mean salt intake over time
```

Evidence 2: document Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), proves component 1. 16.7% (local note: Doc 7, same table, Turkey row)

```text
|Turkey (35)|2008–2012|24-hour urine|18.0g to 15.0g; −17%|
```

Evidence 3: document Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), proves component 1. 16.7% (local note: Doc 7, same table, Argentina row, left out)

```text
|Argentina (18)|2011–2015|24-hour urine|11.2g to 9.2g; −18%|
```

Evidence 4: document Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), proves component 1. 16.7% (local note: Doc 7, same table, Australia row, left out)

```text
|Australia1 (19)|2011–2014|24-hour urine|Victoria|
```

Evidence 5: document Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), proves component 1. 16.7% (local note: Doc 7, same table, Finland rows, left out)

```text
|Finland1 (20, 24)|1979–1987|24-hour urine|Kuopio area|
```

Evidence 6: document Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), proves component 1. 16.7% (local note: Doc 7, same table, footnote)

```text
Change in salt intake measured at the subnational level.
```

Evidence 7: document Doc 9 (Implementing-effective-salt-reduction-programs-and-policies.txt), proves component 1. 16.7% (local note: Doc 9, surveillance table, Argentina row)

```text
|Argentina|Regional survey (24 h urine)11 g (2011)(38)|
```

Evidence 8: document Doc 9 (Implementing-effective-salt-reduction-programs-and-policies.txt), proves component 1. 16.7% (local note: Doc 9, discussion)

```text
Of the four countries, only Mongolia had a national measure of salt intake based on this method at baseline.
```

Evidence 9: document Doc 9 (Implementing-effective-salt-reduction-programs-and-policies.txt), proves component 1. 16.7% (local note: Doc 9, discussion, next sentence)

```text
Argentina and South Africa conducted regional surveys to measure salt intake using 24-h urines, while Vietnam had a national survey but used spot urines.
```

### Necessary documents

- Tick Doc 7 (A-Systematic-Review-of-Salt-Reduction-Initiatives-Around-the.txt), role: Answer component
- Tick Doc 9 (Implementing-effective-salt-reduction-programs-and-policies.txt), role: Exclusion / condition source

  Reviewer note:

```text
Doc 9 shows Argentina's 24-hour urine surveys were regional, ruling out Argentina's 11.2 to 9.2 g pair (17.9%), which Doc 7's table lists without a subnational mark.
```

Leave unticked: Doc 1 (The-estimated-health-impact-of-sodium-reduction-through-food.txt), Doc 2 (Estimating-the-health-and-economic-effects-of-the-voluntary.txt), Doc 3 (Sodium-in-the-New-Zealand-diet-proposed-voluntary-food.txt), Doc 4 (Cross-sectional-comparisons-of-sodium-content-in-processed.txt), Doc 5 (Reduction-of-Cardiovascular-Events-and-Related-Healthcare.txt), Doc 6 (Systematic-Review-on-International-Salt-Reduction-Policy-in.txt), Doc 8 (Salty-and-Savoury-Snacks-Compliance-with-2016-and-2019.txt), Doc 10 (An-evaluation-of-the-Victorian-Salt-Reduction-Partnerships.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Wrong jurisdiction or scope: Doc 7's salt-intake table lists Argentina's 24-hour urine pair, 11.2 to 9.2 g, without a subnational mark, so a careless solver answers 17.9%. Doc 9 says Argentina's urine surveys were regional; the largest whole-country pair left, Turkey's 18.0 to 15.0 g, gives 16.7%.
```

(47 / 50 words.)
