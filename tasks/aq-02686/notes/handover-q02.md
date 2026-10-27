# aq-02686 q02 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02686 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 1e00d4644a279c1a1ed08ab6d196524780c89182e933bf49e5c85956ab8f47a1: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D07 = Doc 7.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 7 doesn't mention 99%. Doc 7 prints it first at character 26,471, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Once EPA's 2026 significant-new-use proposal is final, a large recycler reclaims both covered oxides, one at 90% dust-control efficiency, one at 99%. It refuses FEOC buyers. Orders: both oxides from two Japanese buyers and one Chilean; one oxide from a Thai buyer 10% owned by a Chinese city holding notes convertible into another 20%. What would notifying EPA cost altogether?
```

### Number of asks

1 ask

### Gold answer

```text
$45,920
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, proposed significant new uses): for each of the two covered oxides it is a significant new use to process the substance, where processing includes recycling or reclaiming it from batteries, except with dust controls of a minimum capture and control efficiency of 99%, and a SNUN is required prior to any significant new use. The oxide reclaimed at 90% efficiency is below that minimum and needs a SNUN. The oxide reclaimed at 99% meets the minimum and needs none.

Step 2. Source input (Doc 7, estimated costs for SNUN submissions): a SNUN submission costs an estimated $45,496 for large business submitters. The estimate already includes preparing and submitting the SNUN and the user fee.

Step 3. Source input (Doc 7, estimated costs for export notifications): a person exporting a substance that is the subject of a SNUR gives EPA a one-time notice for the first export to a particular country. The number of notices is counted by chemical, as the number of countries to which that chemical is exported, and each costs approximately $106.

Step 4. Source input (Doc 4, final interpretation, control test and equity interests): an entity is controlled when 25% or more of its equity interest is held by a government of a covered nation, which includes a subnational government. Equity interests include contingent equity interests, and the amount that can be reasonably determined is counted. The Chinese city's stake in the Thai buyer together with the stake its convertible notes carry is three tenths, above 25%, so the Thai buyer is an FEOC, the recycler refuses its order and no export goes to Thailand. Nothing ties the Japanese or Chilean buyers to a covered nation.

Step 5. Calculation (Doc 7): each oxide is exported to Japan and to Chile, however many buyers it has there, so each oxide needs two notices, in dollars: 106 + 106 = 212.

Step 6. Calculation (Doc 7 and Doc 4): notices for both oxides, in dollars: 212 + 212 = 424.

Step 7. Final answer (Doc 7 and Doc 4): the one SNUN plus the four export notices, in dollars: 45,496 + 424 = 45,920.
```

### Answer components

Component 1

```text
$45,920
```

### Evidence

Evidence 1: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,920 (local note: I.D.1, estimated costs for SNUN submissions, L70)

```text
If a SNUN is submitted, costs are an estimated $45,496 per SNUN submission for large business submitters
```

Evidence 2: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,920 (local note: I.D.1, L70)

```text
These estimates include the cost to prepare and submit the SNUN (including registration for EPA's Central Data Exchange (CDX)), and the payment of a user fee.
```

Evidence 3: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,920 (local note: I.D.2, estimated costs for export notifications, L71)

```text
For persons exporting a substance that is the subject of a SNUR, a one-time notice to EPA must be provided for the first export or intended export to a particular country.
```

Evidence 4: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,920 (local note: I.D.2, L71)

```text
The total costs of export notification will vary by chemical, depending on the number of required notifications (i.e., the number of countries to which the chemical is exported).
```

Evidence 5: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,920 (local note: I.D.2, L71)

```text
the estimated cost of the export notification requirement on a per unit basis is approximately $106
```

Evidence 6: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,920 (local note: III.C, L172)

```text
The substances subject to the proposed SNURs in this document are identified below with the proposed CFR citation.
```

Evidence 7: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,920 (local note: proposed 721.12219(a)(2)(iii), L320)

```text
It is a significant new use to manufacture, process (all processing includes recycling or reclaiming substances from batteries or other items containing the PMN substance), or use the substance, except with the use of dust controls with an overall minimum capture and control efficiency of 99%.
```

Evidence 8: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,920 (local note: II.A, L101)

```text
A SNUN is required prior to any significant new use.
```

Evidence 9: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,920 (local note: V.C, L308)

```text
(i) A national or subnational government of a foreign country;
```

Evidence 10: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,920 (local note: V.E, L323)

```text
(i) 25% or more of the entity's board seats, voting rights, or equity interest, with each metric evaluated independently, are cumulatively held by that other entity
```

Evidence 11: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,920 (local note: II.E, response on equity interests, L138)

```text
DOE intends to refer to percent value of the ownership interest, to include capital or profit interests and contingent equity interests, in the company held by an individual or entity, with the amount of contingent interest that can be reasonably determined included for the purpose of determining FEOC compliance.
```

### Necessary documents

- Tick Doc 4 (fr_2024_08913.txt), role: Answer component
- Tick Doc 7 (fr_2026_08012.txt), role: Answer component

Leave unticked: Doc 1 (fr_2022_12459.txt), Doc 2 (fr_2023_26479.txt), Doc 3 (fr_2024_07411.txt), Doc 5 (fr_2024_16461.txt), Doc 6 (fr_2024_30401.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Misapplies a rule or premise

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Unit or basis: Doc 7 counts export notices by chemical and by country, so two oxides to Japan and Chile need four; counting countries gives $45,708, counting buyers $46,132. Part vs total: the city's 10% stake omits the notes' 20%, which Doc 4 counts; keeping the Thai buyer gives $46,026.
```

(50 / 50 words.)
