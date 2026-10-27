# aq-docket-trial-06 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-docket-trial-06 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 ef9968f1ef348fa65cca898ddda45762caf08bfef0bd39275b2dbc971b332c1d: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D05 = Doc 5.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
In 2003 GAO made unannounced visits to privately insured credit unions. Across the states whose bank regulators GAO later interviewed about OCC's 2004 preemption rules, what percentage of the privately insured credit unions they had at the end of 2002 got at least one visit? Answer to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
40.5%
```

### Step-by-step reasoning

```text
Step 1. Doc 5: for its review of OCC's preemption rules, GAO interviewed state banking departments and other officials "in six states (California, Georgia, New York, North Carolina, Idaho, and Iowa)", and its Table 4 covers the "six state bank regulators that we interviewed".

Step 2. Doc 2: as of December 2002, privately insured credit unions were located in only eight states: Alabama, California, Idaho, Illinois, Indiana, Maryland, Nevada and Ohio. California and Idaho are the only states on both lists.

Step 3. Doc 2, Table 3: California had 22 privately insured credit unions and Idaho had 20: 22 + 20 = 42.

Step 4. Doc 2: the unannounced site visits covered credit union locations in Alabama, California, Illinois, Indiana and Ohio only, so no Idaho credit union got a visit.

Step 5. Doc 2, Table 1, note b: one California credit union had its main location and three branch locations visited, and another its main location and one branch location: 3 + 1 = 4 repeat sites.

Step 6. Doc 2, Table 1: GAO visited 21 sites in California: 21 - 4 = 17 different credit unions.

Step 7. Doc 2: 17 / 42 = 40.5%.

Step 8. Doc 2: counting California's sites as if they were credit unions gives 21 / 42 = 50.0%, which counts visits, not credit unions.

Step 9. Doc 2: leaving out Idaho, whose credit unions got no visit, gives 17 / 22 = 77.3%, which drops one of the interviewed states.
```

### Answer components

Component 1

```text
40.5%
```

### Evidence

Evidence 1: document Doc 5 (gaoreports_gao_06_387.txt), proves component 1. 40.5% (local note: Letter, scope and methodology, L183)

```text
state banking departments, consumer groups, state bankers associations, and national and state banks in six states (California, Georgia, New York, North Carolina, Idaho, and Iowa)
```

Evidence 2: document Doc 5 (gaoreports_gao_06_387.txt), proves component 1. 40.5% (local note: Appendix VI, L797)

```text
Table 4 provides more detailed information on the funding arrangements for six state bank regulators that we interviewed.
```

Evidence 3: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Background, L233)

```text
As of December 2002, 212 credit unions
```

Evidence 4: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Appendix I, footnote 3, L1207)

```text
We limited our analysis to those states with privately insured credit unions* Alabama, California, Idaho, Illinois, Indiana, Maryland, Nevada, and Ohio.
```

Evidence 5: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Table 3, column heads, L461)

```text
disclosures Total number of privately insured
```

Evidence 6: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Table 3, L467)

```text
California 22 18 3 17 Idaho 20 7 5 71
```

Evidence 7: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Table 3, total row, L469)

```text
Total 212 78 39 50
```

Evidence 8: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Compliance section, L407)

```text
We conducted unannounced site visits to 57 locations of privately insured credit unions (49 main and 8 branch locations) in five
```

Evidence 9: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Compliance section, L409)

```text
states* Alabama, California, Illinois, Indiana, and Ohio.
```

Evidence 10: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Table 1, column heads, L421)

```text
credit unions Total sites visited Total number Total percent
```

Evidence 11: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Table 1, L423)

```text
Alabama 3 5 a 3 60 California 22 21 b 6 29
```

Evidence 12: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Table 1, note b, L429)

```text
For one credit union, in addition to conducting a site visit at the main location, we conducted site
```

Evidence 13: document Doc 2 (gaoreports_gao_03_971.txt), proves component 1. 40.5% (local note: Table 1, note b, L431)

```text
visits at three branch locations. For another credit union, in addition to conducting a site visit at the main location, we conducted a site visit at a branch location.
```

### Necessary documents

- Tick Doc 2 (gaoreports_gao_03_971.txt), role: Answer component
- Tick Doc 5 (gaoreports_gao_06_387.txt), role: Used to identify

Leave unticked: Doc 1 (gaoreports_gao_01_819t.txt), Doc 3 (gaoreports_gao_04_412t.txt), Doc 4 (gaoreports_gao_04_684.txt), Doc 6 (gaoreports_gao_08_148r.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution, Aggregation

Leave unticked: Temporal alignment, Unit normalization

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Takes the wrong line item

Where the trap sits:

```text
Doc 2, Table 1, "Number and Percent of Credit Unions Visited without Required Signage in Lobby", prints California's fieldwork as 21 under "Total sites visited", right beside the state's 22 privately insured credit unions. The Highlights page describes the fieldwork as "unannounced site visits to 57 privately insured credit unions", and Appendix I repeats "unannounced site visits to 57 privately insured credit unions (49 main and 8 branch locations)", so a quick reader treats each visited site as a separate credit union. The body text does speak of locations and of "the 21 sites visited in California", but only note b, printed under the table, shows which California sites belonged to the same credit union.
```

The wrong answer a careless solver gives:

```text
50.0%. The solver correctly takes California and Idaho as the interviewed states with privately insured credit unions (22 + 20 = 42), then reads California's 21 sites as 21 credit unions visited and divides: 21 / 42 = 50.0%. A solver who also keeps only California writes 21 / 22 = 95.5%.
```

Why the correct answer avoids it:

```text
The question counts credit unions that got at least one visit, not visits. Note b under Table 1 says one California credit union was visited at its main location and at three branch locations, and another at its main location and one branch location. Four of the 21 California sites were therefore repeat visits to two credit unions already counted, so only 21 - 3 - 1 = 17 different California credit unions were visited, and 17 / 42 = 40.5%.
```

(248 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Wrong jurisdiction or scope

How a careless solver fails: Wrong members in a list

Where the trap sits:

```text
Doc 5 names the six states whose bank regulators GAO interviewed (California, Georgia, New York, North Carolina, Idaho and Iowa), while Doc 2's unannounced visits covered only Alabama, California, Illinois, Indiana and Ohio. California is the only state on both lists, so it looks like the whole population. Idaho, an interviewed state with 20 privately insured credit unions in Doc 2's Table 3, appears in neither Table 1 nor the list of visited states.
```

The wrong answer a careless solver gives:

```text
77.3%. The solver keeps only the interviewed state where visits took place, California, applies the note b correction and computes 17 / 22 = 77.3%. Without the note b correction the same slip gives 21 / 22 = 95.5%.
```

Why the correct answer avoids it:

```text
The question asks across all the interviewed states, and Doc 2 shows that two of them had privately insured credit unions at the end of 2002: California with 22 and Idaho with 20 (Table 3; the eight-state list in Appendix I). Georgia, New York, North Carolina and Iowa had none. Idaho's 20 credit unions got no visit, but they still belong in the base, so the share is 17 / (22 + 20) = 40.5%.
```

(188 words across the three boxes; the form needs at least 150.)
