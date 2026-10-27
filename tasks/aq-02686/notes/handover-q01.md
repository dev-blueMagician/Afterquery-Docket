# aq-02686 q01 hand-over

Generated 2026-10-10 by `python tools/check_questions.py tasks/aq-02686 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 3, difficulty_target medium, origin claude.
- tested_sha256 3c37e0b3ad5af40fb30df2d7b65c54acca07e1d1fb5eb524319c6242a5abc736: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D07 = Doc 7.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN form-numbers: Step 1: Doc 7 doesn't mention 99%. Doc 7 prints it first at character 26,471, past the deepest observed pass (19,581); the form flagged printed numbers near character 80,000, so it may flag this one: prefer an input printed earlier
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Once EPA's 2026 significant-new-use proposal is final, a large recycler reclaims a covered oxide with 90%-efficient dust controls, exporting to non-FEOCs among: a Chinese province's 15%-owned Thai firm; a Chinese city's 10%-owned Polish firm, with city-held notes convertible into another 20%; a Japanese firm whose one Chinese-province-picked director, of seven, alone has two votes. What would notifying EPA cost altogether?
```

### Number of asks

1 ask

### Gold answer

```text
$45,602
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, proposed significant new uses): it is a significant new use to process the substance, where processing includes recycling or reclaiming it from batteries, except with dust controls of a minimum capture and control efficiency of 99%, and a SNUN is required prior to any significant new use. The recycler's 90% controls are below that minimum, so it must notify EPA with a SNUN.

Step 2. Source input (Doc 7, estimated costs for SNUN submissions): a SNUN submission costs an estimated $45,496 for large business submitters. The estimate already includes preparing and submitting the SNUN and the user fee.

Step 3. Source input (Doc 7, estimated costs for export notifications): a person exporting a substance that is the subject of a SNUR gives EPA a one-time notice for the first export to a particular country, at approximately $106 per notification.

Step 4. Source input (Doc 4, final interpretation, government and control tests): a government of a foreign country includes a subnational government, and an entity is controlled when 25% or more of its board seats, voting rights or equity interest, each metric evaluated independently, is held by that government. The province's stake in the Thai firm is below that threshold and nothing else ties the firm to a covered nation, so the Thai firm is not an FEOC.

Step 5. Source input (Doc 4, response to comments and explanation on equity interests): equity interests include contingent equity interests, and the amount that can be reasonably determined is included in the 25% control calculation, without consideration of whether conversion is imminent or within the holder's control. The city's stake in the Polish firm together with the stake its convertible notes carry is three tenths, above 25%, so the Polish firm is an FEOC and receives no export.

Step 6. Source input (Doc 4, response to comments on board seats): DOE values a board seat at its voting power on the board, and a seat holding 25% of the board voting power makes the entity a controlled FEOC. The province's director casts two of the eight board votes, a quarter, so the Japanese firm is an FEOC and receives no export, although the province fills only one of seven seats.

Step 7. Final answer (Doc 7 and Doc 4): the SNUN plus one export notice, for Thailand, in dollars: 45,496 + 106 = 45,602.
```

### Answer components

Component 1

```text
$45,602
```

### Evidence

Evidence 1: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,602 (local note: I.D.1, estimated costs for SNUN submissions, L70)

```text
If a SNUN is submitted, costs are an estimated $45,496 per SNUN submission for large business submitters
```

Evidence 2: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,602 (local note: I.D.1, L70)

```text
These estimates include the cost to prepare and submit the SNUN (including registration for EPA's Central Data Exchange (CDX)), and the payment of a user fee.
```

Evidence 3: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,602 (local note: I.D.2, estimated costs for export notifications, L71)

```text
a one-time notice to EPA must be provided for the first export or intended export to a particular country
```

Evidence 4: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,602 (local note: I.D.2, L71)

```text
the estimated cost of the export notification requirement on a per unit basis is approximately $106
```

Evidence 5: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,602 (local note: proposed 721.12219(a)(2)(iii), L320)

```text
It is a significant new use to manufacture, process (all processing includes recycling or reclaiming substances from batteries or other items containing the PMN substance), or use the substance, except with the use of dust controls with an overall minimum capture and control efficiency of 99%.
```

Evidence 6: document Doc 7 (fr_2026_08012.txt), proves component 1. $45,602 (local note: II.A, L101)

```text
A SNUN is required prior to any significant new use.
```

Evidence 7: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,602 (local note: V.C, L308)

```text
(i) A national or subnational government of a foreign country;
```

Evidence 8: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,602 (local note: V.E, L323)

```text
(i) 25% or more of the entity's board seats, voting rights, or equity interest, with each metric evaluated independently, are cumulatively held by that other entity
```

Evidence 9: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,602 (local note: II.E, response on equity interests, L138)

```text
DOE intends to refer to percent value of the ownership interest, to include capital or profit interests and contingent equity interests, in the company held by an individual or entity, with the amount of contingent interest that can be reasonably determined included for the purpose of determining FEOC compliance.
```

Evidence 10: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,602 (local note: III.E.i, contingent equity interests, L255)

```text
should be included in the 25% control calculation, without consideration of whether conversion is imminent or within the control of the equity-owning entity
```

Evidence 11: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,602 (local note: II.E, response on board seats, L138)

```text
DOE intends for the value of a board seat to equal the value of its voting power on the board
```

Evidence 12: document Doc 4 (fr_2024_08913.txt), proves component 1. $45,602 (local note: II.E, response on board seats, L138)

```text
that seat holds 25% of the board voting power, then that entity would be considered a controlled FEOC
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

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Why these are traps (at most 50 words)

```text
Look-alike measure: one of seven seats looks like 14%, but Doc 4's comment response values a seat by board voting power, two of eight votes, 25%. Part vs total: the city's 10% stake omits the notes' 20%, which Doc 4 counts as contingent equity. Either adds $106: $45,708 or $45,814.
```

(50 / 50 words.)
