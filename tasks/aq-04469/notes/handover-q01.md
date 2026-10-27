# aq-04469 q01 hand-over

Generated 2026-10-14 by `python tools/check_questions.py tasks/aq-04469 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 4c75e1bbe9697fe97c16b06849977bf21effc3b00c7c2df1fbbfe8886b72330b: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D06 = Doc 5, D09 = Doc 9, D13 = Doc 13.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Which of these submitters, if any, cite figures published by Hort Innovation? List them alphabetically.
```

### Number of asks

1 ask

### Gold answer

```text
Australian Fresh Produce Alliance, AUSVEG, Fruit Producers SA
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 5, key facts): the Australian Fresh Produce Alliance says its key facts are "sourced largely from Hort Innovation's Australian Horticulture Statistics Handbook", and its footnote gives that handbook as "Australian Horticulture Statistics Handbook 2022/23 - Hort Innovation". It cites Hort Innovation figures (first component).
Step 2. Source input (Doc 9, executive summary and its footnote): AUSVEG writes "Harvest to Home citing 78 percent of retail fresh vegetables are sold through Coles, Woolworths, and Aldi", and its footnote gives the source as "'Harvest to Home', Hort Innovation". It cites a Hort Innovation figure (second component).
Step 3. Source input (Doc 13, executive summary): Fruit Producers SA gives its growers' "over $150 million in value of production (Source: Australian Horticultural Statistics 2022/2023)". It names no publisher.
Step 4. Join (Doc 5 and Doc 13): Doc 5 says the Australian Horticulture Statistics Handbook for 2022/23 is Hort Innovation's. Fruit Producers SA's source is that publication for the same year, so its figure is also a Hort Innovation figure (third component).
Step 5. Decoy: Fresh Markets Australia also names Hort Innovation, but only in a proposal that the Government steer Hort Innovation's fruit and vegetable levies towards independent retailers. It cites no figure from Hort Innovation, so it is not in the list. No other submission names Hort Innovation, Harvest to Home or the horticulture statistics handbook as a source.
Step 6. Final answer (Doc 5, Doc 9 and Doc 13): Australian Fresh Produce Alliance, AUSVEG, Fruit Producers SA.
```

### Answer components

Component 1

```text
Australian Fresh Produce Alliance
```

Component 2

```text
AUSVEG
```

Component 3

```text
Fruit Producers SA
```

### Evidence

Evidence 1: document Doc 5 (autreas_grocery_code_review_c2024_489934_australian_fresh_produce_allian.txt), proves component 1. Australian Fresh Produce Alliance (local note: key facts, line 169)

```text
The following key facts and information, sourced largely from Hort Innovation’s Australian Horticulture Statistics Handbook
```

Evidence 2: document Doc 5 (autreas_grocery_code_review_c2024_489934_australian_fresh_produce_allian.txt), proves component 3. Fruit Producers SA (local note: footnote 3, line 183)

```text
Australian Horticulture Statistics Handbook 2022/23 - Hort Innovation
```

Evidence 3: document Doc 9 (autreas_grocery_code_review_c2024_489934_ausveg.txt), proves component 2. AUSVEG (local note: executive summary, line 51)

```text
Harvest to Home citing 78 percent of retail fresh vegetables are sold through Coles, Woolworths, and Aldi
```

Evidence 4: document Doc 9 (autreas_grocery_code_review_c2024_489934_ausveg.txt), proves component 2. AUSVEG (local note: footnote 2, line 58)

```text
‘Harvest to Home’, Hort Innovation.
```

Evidence 5: document Doc 13 (autreas_grocery_code_review_c2024_489934_fruit_producers_sa.txt), proves component 3. Fruit Producers SA (local note: executive summary, line 10)

```text
These horticultural activities represent over $150 million in value of production (Source: Australian Horticultural Statistics 2022/2023)
```

### Necessary documents

- Tick Doc 5 (autreas_grocery_code_review_c2024_489934_australian_fresh_produce_allian.txt), role: Answer component
- Tick Doc 9 (autreas_grocery_code_review_c2024_489934_ausveg.txt), role: Answer component
- Tick Doc 13 (autreas_grocery_code_review_c2024_489934_fruit_producers_sa.txt), role: Answer component

Leave unticked: Doc 1 (autreas_grocery_code_review_c2024_489934_alfred_e_chave.txt), Doc 2 (autreas_grocery_code_review_c2024_489934_australian_chicken_growers_coun.txt), Doc 3 (autreas_grocery_code_review_c2024_489934_accc.txt), Doc 4 (autreas_grocery_code_review_c2024_489934_australian_dairy_farmers.txt), Doc 6 (autreas_grocery_code_review_c2024_489934_australian_grape_and_wine.txt), Doc 7 (autreas_grocery_code_review_c2024_489934_australian_macadamia_society.txt), Doc 8 (autreas_grocery_code_review_c2024_489934_asbfeo.txt), Doc 10 (autreas_grocery_code_review_c2024_489934_eastausmilk.txt), Doc 11 (autreas_grocery_code_review_c2024_489934_fresh_markets_australia.txt), Doc 12 (autreas_grocery_code_review_c2024_489934_freshmark.txt), Doc 14 (autreas_grocery_code_review_c2024_489934_greenlife_industry_australia.txt), Doc 15 (autreas_grocery_code_review_c2024_489934_metcash.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 13 sources its $150 million to "Australian Horticultural Statistics 2022/2023" and names no publisher; only Doc 5 calls that handbook Hort Innovation's. Searching for Hort Innovation finds Docs 5 and 9 and gives two names; the link adds Fruit Producers SA.
```

(45 / 50 words.)
