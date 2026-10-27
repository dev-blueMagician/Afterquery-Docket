# aq-02028 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-02028 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 4, difficulty_target medium, origin claude.
- tested_sha256 5007fa6a3162365494c5611119662bdcd2cee729c02972be932aa79cba25f6d3: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D06 = Doc 6.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
On the WA coastal-trading exemption's last day, what was the mean stevedore infrastructure surcharge per full import container across the 13 container terminals at Adelaide, Brisbane, Fremantle, Melbourne and Sydney, to the nearest cent?
```

### Number of asks

1 ask

### Gold answer

```text
$117.39
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 6, section on a permanent coastal trading exemption): the Federal government's section 11 exemption of the Coastal Trading (Revitalising Australian Shipping) Act 2012 for voyages by container and roll-on, roll-off vessels to Western Australia applied until 31 March 2022, so its last day was 31 March 2022.

Step 2. Source fact (Doc 2, Attachment A title, header and narrative): the national stevedore infrastructure surcharges are listed per full container, excluding GST, as at 25 January 2022, in columns for stevedore, port, export, import and effective date. Doc 2's text says the latest increases by Patrick Terminals are shown on the right-hand side and will be implemented on 1 March 2022.

Step 3. Source fact (Doc 2, Attachment A rows with no later rate): the import surcharge per full container was $100.00 at AAT Brisbane (effective 1-Jul-21), $128.90 at DP World Australia Brisbane (1-Jan-22), $133.08 at Hutchison Ports Brisbane (1-Mar-21), $45.00 at DP World Australia Fremantle (1-Jan-21), $144.70 at DP World Australia Melbourne (1-Jan-22), $141.80 at VICT Melbourne (1-Jan-22), $131.60 at DP World Australia Sydney (1-Jan-22) and $135.65 at Hutchison Ports Sydney (1-Mar-21). None of these rows lists a later rate.

Step 4. Source fact (Doc 2, Attachment A Patrick rows): Patrick's import surcharge from 1-Mar-21 was $113.20 at Brisbane, $53.85 at Fremantle, $129.50 at Melbourne and $117.85 at Sydney. Each Patrick row adds a right-hand import rate dated 7/03/2022: 135.85 at Brisbane, 57.69 at Fremantle, 155.40 at Melbourne and 141.45 at Sydney.

Step 5. Source fact (Doc 2, Attachment A Flinders Adelaide Container Terminal row): the import surcharge was $75.00 from 1-Jul-21, with a right-hand import rate of 112.50 dated 1/04/2022.

Step 6. Date check (from Steps 1, 2, 4 and 5; Doc 6 and Doc 2): Doc 2 writes these dates day first, since its text puts Patrick's increases in March (1 March 2022) while the table dates them 7/03/2022. Patrick's increases had taken effect by 31 March 2022, so that day its import rates were 135.85, 57.69, 155.40 and 141.45. The Flinders Adelaide increase starts on 1/04/2022, the day after 31 March 2022, so that terminal still charged $75.00.

Step 7. Count (from Steps 3 to 5; Doc 2): the table lists 1 terminal at Adelaide, 4 at Brisbane, 2 at Fremantle, 3 at Melbourne and 3 at Sydney: 1 + 4 + 2 + 3 + 3 = 13 terminals.

Step 8. Calculation (from Steps 3, 5 and 6; Doc 2): sum of the import rates in force that day, in the table's order (Adelaide; Brisbane AAT, DP World, Hutchison, Patrick; Fremantle DP World, Patrick; Melbourne DP World, Patrick, VICT; Sydney DP World, Hutchison, Patrick): 75.00 + 100.00 + 128.90 + 133.08 + 135.85 + 45.00 + 57.69 + 144.70 + 155.40 + 141.80 + 131.60 + 135.65 + 141.45 = $1,526.12.

Step 9. Calculation (from Steps 7 and 8; Doc 2 and Doc 6): mean import surcharge = 1,526.12 / 13 = $117.39 (to the nearest cent).
```

### Answer components

Component 1

```text
$117.39
```

### Evidence

Evidence 1: document Doc 6 (pcau_maritime_r1_sub021_maritime_logistics.txt), proves component 1. $117.39 (local note: L152, permanent coastal trading exemption)

```text
for voyages by container and roll-on, roll-off vessels to Western Australia until 31 March 2022
```

Evidence 2: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L174, Attachment A title)

```text
INFRASTRUCTURE SURCHARGES - AS AT 25 January 2022 per full container / excluding GST
```

Evidence 3: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L175, Attachment A header)

```text
STEVEDORE PORT EXPORT IMPORT EFFECTIVE
```

Evidence 4: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L137, narrative on Attachment A)

```text
the latest increases in charges by Patrick Terminals are highlighted on the right-hand side which will be implemented on 1 March 2022
```

Evidence 5: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L176, Adelaide and first two Brisbane rows)

```text
Flinders Adelaide Container Terminal Adelaide $75.00 $75.00 1-Jul-21 79.50 112.50 1/04/2022 Australian Amalgamated Terminals (AAT) Brisbane $78.00 $100.00 1-Jul-21 DP World Australia Brisbane $105.90 $128.90 1-Jan-22
```

Evidence 6: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L177, Hutchison Brisbane row)

```text
Hutchison Ports Brisbane $133.08 $133.08 1-Mar-21
```

Evidence 7: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L178, Patrick Brisbane and DP World Fremantle rows)

```text
Patrick Brisbane $84.90 $113.20 1-Mar-21 101.90 135.85 7/03/2022 DP World Australia Fremantle $45.00 $45.00 1-Jan-21
```

Evidence 8: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L179, Patrick Fremantle and DP World Melbourne rows)

```text
Patrick Fremantle $26.92 $53.85 1-Mar-21 28.84 57.69 7/03/2022 DP World Australia Melbourne $105.90 $144.70 1-Jan-22
```

Evidence 9: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L180, Patrick Melbourne, VICT and DP World Sydney rows)

```text
Patrick Melbourne $84.90 $129.50 1-Mar-21 101.90 155.40 7/03/2022 Victoria International Container Terminal (VICT) Melbourne $141.80 $141.80 1-Jan-22 DP World Australia Sydney $105.90 $131.60 1-Jan-22
```

Evidence 10: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L181, Hutchison Sydney row)

```text
Hutchison Ports Sydney $135.65 $135.65 1-Mar-21
```

Evidence 11: document Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), proves component 1. $117.39 (local note: L182, Patrick Sydney row)

```text
Patrick Sydney $84.90 $117.85 1-Mar-21 101.90 141.45 7/03/2022
```

### Necessary documents

- Tick Doc 2 (pcau_maritime_r1_sub008_maritime_logistics.txt), role: Answer component
- Tick Doc 6 (pcau_maritime_r1_sub021_maritime_logistics.txt), role: Used to identify

Leave unticked: Doc 1 (pcau_maritime_r1_sub007_maritime_logistics.txt), Doc 3 (pcau_maritime_r1_sub014_maritime_logistics.txt), Doc 4 (pcau_maritime_r1_sub016_maritime_logistics.txt), Doc 5 (pcau_maritime_r1_sub017_maritime_logistics.txt), Doc 7 (pcau_maritime_r1_sub023_maritime_logistics.txt), Doc 8 (pcau_maritime_r1_sub024_maritime_logistics.txt), Doc 9 (pcau_maritime_r1_sub025_maritime_logistics.txt), Doc 10 (pcau_maritime_r1_sub026_maritime_logistics.txt), Doc 11 (pcau_maritime_r1_sub032_maritime_logistics.txt), Doc 12 (pcau_maritime_r1_sub033_maritime_logistics.txt), Doc 13 (pcau_maritime_r1_sub034_maritime_logistics.txt), Doc 14 (pcau_maritime_r1_sub037_maritime_logistics.txt), Doc 15 (pcau_maritime_r1_sub040_maritime_logistics.txt), Doc 16 (pcau_maritime_r1_sub041_maritime_logistics.txt), Doc 17 (pcau_maritime_r1_sub042_maritime_logistics.txt), Doc 18 (pcau_maritime_r1_sub043_maritime_logistics.txt), Doc 19 (pcau_maritime_r1_sub046_maritime_logistics.txt), Doc 20 (pcau_maritime_r1_sub048_maritime_logistics.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Aggregation

Leave unticked: Unit normalization, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Superseded date or version

How a careless solver fails: Uses the wrong period or date

#### Failure mode 2

Trap: Out-of-range period

How a careless solver fails: Uses the wrong period or date

#### Failure mode 3

Trap: Document convention

How a careless solver fails: Uses the wrong period or date

#### Why these are traps (at most 50 words)

```text
Doc 2's surcharge table shows 25 January 2022 rates, averaging $111.55. Doc 6 dates the exemption's last day to 31 March 2022: Patrick's 7/03/2022 rises apply, Adelaide's 1/04/2022 rise does not ($120.28 if applied). Reading those dates month-first gives $114.43. Correct mean: $117.39.
```

(43 / 50 words.)
