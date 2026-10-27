# aq-01543 q04 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01543 --handover --q q04` from questions/q04.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 addb7a41e30a3b93fdb5f019e31590520c91c44a5de49e352a5dc1f6918593e0: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D14 = Doc 12, D15 = Doc 4.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q04.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Divide South Africa's existing nuclear generating capacity by the combined capacity of the nuclear reactors South Korea had in operation in late September 2025. What is the result in percent, rounded to two decimal places?
```

### Number of asks

1 ask

### Gold answer

```text
7.79%
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 4, Energy, Nuclear): "Korea has 26 nuclear reactors, 23 of which are currently in operation, with total installed nuclear generating capacity of approximately 26 gigawatts electric (GW(e))".

Step 2. Source input (Doc 4, Table 2 "List of nuclear power plants in Korea", data as of September 25, 2025): the 23 rows whose status reads "in operation", with their capacities in MWe: Shin-Kori-1 and Shin-Kori-2, 1,000 each; Saeul-1 and Saeul-2, 1,400 each; Wolsong-2, Wolsong-3 and Wolsong-4, 700 each; Shin-Wolsong-1 and Shin-Wolsong-2, 1,000 each; Hanbit-1 and Hanbit-2, 950 each; Hanbit-3, Hanbit-4, Hanbit-5 and Hanbit-6, 1,000 each; Hanul-1 and Hanul-2, 950 each; Hanul-3, Hanul-4, Hanul-5 and Hanul-6, 1,000 each; Shin-Hanul-1 and Shin-Hanul-2, 1,400 each.

Step 3. Source input (Doc 4, Table 2): the other rows were not in operation on that date. Kori-2 (650) has the status "Taken offline on 3/8/23, 9/28/24, and 8/6/25 and waits for a decision on its operation license renewal", and Kori-3 and Kori-4 (950 each) have no status of their own; with these three set aside, the rows marked "in operation" number 23, the prose's count. Saeul-3 and Saeul-4 (1,400 each) are "Expected to be in operation" in the first half of 2026 and in 2027, Shin-Hanul-3 and Shin-Hanul-4 (1,400 each) by Oct. 2033, and Kori-1 (587) and Wolsong-1 (679) are "Permanently shut down".

Step 4. Calculation (Doc 4, the twelve 1,000 MWe rows in operation: Shin-Kori-1, Shin-Kori-2, Shin-Wolsong-1, Shin-Wolsong-2, Hanbit-3 to Hanbit-6 and Hanul-3 to Hanul-6): 12 * 1,000 = 12,000 MWe.

Step 5. Calculation (Doc 4, the four 1,400 MWe rows in operation: Saeul-1, Saeul-2, Shin-Hanul-1 and Shin-Hanul-2): 4 * 1,400 = 5,600 MWe.

Step 6. Calculation (Doc 4, the four 950 MWe rows in operation: Hanbit-1, Hanbit-2, Hanul-1 and Hanul-2): 4 * 950 = 3,800 MWe.

Step 7. Calculation (Doc 4, the three 700 MWe rows in operation: Wolsong-2, Wolsong-3 and Wolsong-4): 3 * 700 = 2,100 MWe.

Step 8. Calculation (Doc 4, running total): 12,000 + 5,600 = 17,600 MWe.

Step 9. Calculation (Doc 4, running total): 17,600 + 3,800 = 21,400 MWe.

Step 10. Calculation (Doc 4, combined capacity of the 23 reactors in operation): 21,400 + 2,100 = 23,500 MWe.

Step 11. Source input (Doc 12, Energy): at Koeberg, the country's only nuclear plant, "two reactors completed in the 1980s have a combined generating capacity of 1,830 MW".

Step 12. Calculation (Doc 12 and Doc 4, South Africa's capacity divided by Korea's capacity in operation, as a percentage): 1,830 / 23,500 = 7.7872%.

Step 13. Final answer (Doc 12 and Doc 4, the same division rounded once to the two decimal places the question asks): 1,830 / 23,500 = 7.79%.
```

### Answer components

Component 1

```text
7.79%
```

### Evidence

Evidence 1: document Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), proves component 1. 7.79% (local note: Energy, Nuclear, L165)

```text
Korea has 26 nuclear reactors, 23 of which are currently in operation
```

Evidence 2: document Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), proves component 1. 7.79% (local note: Table 2 title, L167)

```text
Table 2: List of nuclear power plants in Korea
```

Evidence 3: document Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), proves component 1. 7.79% (local note: Table 2 note, L318)

```text
(Data as of September 25, 2025)
```

Evidence 4: document Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), proves component 1. 7.79% (local note: Table 2, Kori-2 status, L177)

```text
Taken offline on 3/8/23, 9/28/24, and 8/6/25 and waits for a decision on its operation license renewal
```

Evidence 5: document Doc 12 (ccg_energy_cleantech_sectors_south_africa.txt), proves component 1. 7.79% (local note: Energy, nuclear paragraph, L20)

```text
two reactors completed in the 1980s have a combined generating capacity of 1,830 MW
```

### Necessary documents

- Tick Doc 4 (ccg_energy_cleantech_sectors_south_korea.txt), role: Answer component
- Tick Doc 12 (ccg_energy_cleantech_sectors_south_africa.txt), role: Answer component

Leave unticked: Doc 1 (ccg_energy_cleantech_sectors_bulgaria.txt), Doc 2 (ccg_energy_cleantech_sectors_poland.txt), Doc 3 (ccg_energy_cleantech_sectors_vietnam.txt), Doc 5 (ccg_energy_cleantech_sectors_israel.txt), Doc 6 (ccg_energy_cleantech_sectors_chile.txt), Doc 7 (ccg_energy_cleantech_sectors_angola.txt), Doc 8 (ccg_energy_cleantech_sectors_mauritius.txt), Doc 9 (ccg_energy_cleantech_sectors_germany.txt), Doc 10 (ccg_energy_cleantech_sectors_china.txt), Doc 11 (ccg_energy_cleantech_sectors_united_arab_emirates.txt), Doc 13 (ccg_energy_cleantech_sectors_mexico.txt), Doc 14 (ccg_energy_cleantech_sectors_united_kingdom.txt), Doc 15 (ccg_energy_cleantech_sectors_uruguay.txt), Doc 16 (ccg_energy_cleantech_sectors_portugal.txt), Doc 17 (ccg_energy_cleantech_sectors_spain.txt), Doc 18 (ccg_energy_cleantech_sectors_finland.txt), Doc 19 (ccg_energy_cleantech_sectors_indonesia.txt), Doc 20 (ccg_energy_cleantech_sectors_romania.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter, Aggregation

Leave unticked: Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Out-of-range period

How a careless solver fails: Wrong members in a list

#### Failure mode 3

Trap: Document convention

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Doc 4: the prose's 26 GW(e) covers all 26 installed reactors (7.04%); Table 2's four "Expected to be in operation" units (6.29%) and blank-status Kori-3/4, offline with Kori-2 (7.20%), were not running. Only the 23 "in operation" rows count: Doc 12's 1,830 / 23,500 = 7.79%.
```

(46 / 50 words.)
