# aq-02562 q01 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02562 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status ready, revision 1, difficulty_target medium, origin claude.
- tested_sha256 6b96b593fa543b29b3a5e1143be3a485513f1d9269da4fda28188a9108af7f6d: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D07 = Doc 7.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 2: Doc 2 doesn't mention 75. Doc 2 prints it first at character 43,079, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
What is the most MASC and ASCF combined could pay a four-partner general partnership if one partner's average AGI exceeded $900,000, 70 percent from crops and the rest from selling seed to farmers?
```

### Number of asks

1 ask

### Gold answer

```text
$1,250,000
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, payment limitation and payment eligibility section): for ASCF, a person or legal entity other than a joint venture or general partnership "is ineligible for ASCF Program payments, directly or indirectly," if average adjusted gross income for the 2021, 2022, and 2023 tax years exceeds $900,000. Doc 7 states no farm-income exception to this bar.

Step 2. Source input (Doc 2, Average AGI Limitation and Payment Limitation): MASC applies the same average AGI bar to the same tax years, "unless the person or legal entity's average adjusted gross farm income is at least 75 percent of their average AGI."

Step 3. Source input (Doc 2, Definitions): income derived from farming includes "(1) Production of crops"; if the average adjusted gross farm income "derived from items 1 through 12" is at least 66.66 percent of average AGI, the average adjusted gross farm income "may also take into consideration" income from "The provision of production inputs and production services to farmers", and "Production inputs mean material to conduct farming operations, such as seeds".

Step 4. Application (Doc 2): the partner's crop income is item (1) income and makes up 70 percent of average AGI, at least the 66.66 percent of Step 3, so the seed sold to farmers (production inputs) also counts as farm income. All of the partner's average AGI is then farm income, the partner meets the Step 2 exception and stays eligible for MASC.

Step 5. Application (Doc 7): the same partner's average AGI exceeds $900,000 and Step 1 allows no exception, so no ASCF payment can reach that partner directly or indirectly. At most, the other three partners remain eligible: ASCF accepts a partnership "consisting solely of citizens of the United States or resident aliens", and the question states nothing else against them.

Step 6. Source input (Doc 2, payment limitation and attribution): the $125,000 MASC cap binds "a person or legal entity, other than a joint venture or general partnership", and "A payment made to a legal entity will be attributed to those members who have a direct or indirect ownership interest in the legal entity"; the legal-entity definition lists general partnerships. Each of the four partners is therefore capped separately.

Step 7. Calculation (Doc 2): MASC maximum in dollars with all four partners eligible (Steps 4 and 6): 125,000 + 125,000 + 125,000 + 125,000 = 500,000.

Step 8. Source input (Doc 7, payment limitation rule): "A person, legal entity, or member of a joint venture or general partnership" cannot receive, directly or indirectly, more than $250,000 under the ASCF Program, so each eligible partner is capped separately.

Step 9. Calculation (Doc 7): ASCF maximum in dollars for the three eligible partners (Steps 5 and 8): 250,000 + 250,000 + 250,000 = 750,000.

Step 10. Final answer (Doc 2 and Doc 7): most the partnership could receive from MASC and ASCF combined, in dollars (Steps 7 and 9): 500,000 + 750,000 = 1,250,000.
```

### Answer components

Component 1

```text
$1,250,000
```

### Evidence

Evidence 1: document Doc 7 (fr_2026_10930.txt), proves component 1. $1,250,000 (local note: section VI, payment limitation and payment eligibility, L148)

```text
is ineligible for ASCF Program payments, directly or indirectly, if the person's or legal entity's average adjusted gross income (AGI), using the average of the adjusted gross incomes for the 2021, 2022, and 2023 tax years, exceeds $900,000.
```

Evidence 2: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Average AGI Limitation and Payment Limitation, L274)

```text
a MASC payment if the average adjusted gross income of the person or legal entity exceeds $900,000 for 2021, 2022, and 2023, unless the person or legal entity's average adjusted gross farm income is at least
```

Evidence 3: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Average AGI Limitation and Payment Limitation, L275)

```text
75 percent of their average AGI.
```

Evidence 4: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Definitions, L103)

```text
If the resulting average adjusted gross farm income derived from items 1 through 12 of the definition of income derived from farming, ranching, and forestry operations is at least 66.66 percent of the average AGI of the person or legal entity, then the average adjusted gross farm income may also take into consideration income or benefits derived from the following:
```

Evidence 5: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Definitions, L105)

```text
(2) The provision of production inputs and production services to farmers, ranchers, foresters, and farm operations.
```

Evidence 6: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Definitions, L119)

```text
(1) Production of crops and unfinished raw forestry products;
```

Evidence 7: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Definitions, L144)

```text
Production inputs mean material to conduct farming operations, such as seeds, chemicals, and fencing supplies.
```

Evidence 8: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Average AGI Limitation and Payment Limitation, L276)

```text
A person or legal entity, other than a joint venture or general partnership, cannot receive, directly or indirectly, more than $125,000 in MASC payments.
```

Evidence 9: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Average AGI Limitation and Payment Limitation, L277)

```text
A payment made to a legal entity will be attributed to those members who have a direct or indirect ownership interest in the legal entity
```

Evidence 10: document Doc 2 (fr_2024_29017.txt), proves component 1. $1,250,000 (local note: Definitions, L133)

```text
Legal entity means a corporation, joint stock company, association, limited partnership, limited liability company, irrevocable trust, estate, charitable organization, general partnership, joint venture
```

Evidence 11: document Doc 7 (fr_2026_10930.txt), proves component 1. $1,250,000 (local note: Sec. 1414.109(a), L363)

```text
A person, legal entity, or member of a joint venture or general partnership, as determined in 7 CFR part 1400 in effect for program year 2025 on June 1, 2026, cannot receive, directly or indirectly, more than $250,000 under this subpart.
```

Evidence 12: document Doc 7 (fr_2026_10930.txt), proves component 1. $1,250,000 (local note: Sec. 1414.104(b)(3), L309)

```text
Partnership organized under State law consisting solely of citizens of the United States or resident aliens
```

### Necessary documents

- Tick Doc 2 (fr_2024_29017.txt), role: Answer component
- Tick Doc 7 (fr_2026_10930.txt), role: Answer component

Leave unticked: Doc 1 (fr_2023_12820.txt), Doc 3 (fr_2024_30710.txt), Doc 4 (fr_2025_18328.txt), Doc 5 (fr_2025_18624.txt), Doc 6 (fr_2026_09212.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Scope: Doc 2's 75 percent farm-income exception belongs to MASC only; Doc 7 bars ASCF payments to anyone averaging over $900,000 AGI, with no exception. Carrying Doc 2's exception into ASCF keeps all four partners eligible there: $500,000 + $1,000,000 = $1,500,000. Excluding that partner from ASCF gives $1,250,000.
```

(49 / 50 words.)
