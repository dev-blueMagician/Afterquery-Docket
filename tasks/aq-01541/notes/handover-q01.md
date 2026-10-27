# aq-01541 q01 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01541 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 6fa7875382f3e0998151a32334fa280b2f1f698e99c654aecb5fe82f95c7232a: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D03 = Doc 7, D07 = Doc 6.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: six words shared with q02: 'in trans union's preliminarily approved settlement'
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
If every class member in Trans Union's preliminarily approved settlement filed a valid claim, what percentage of the money set aside for valid-claim payments would go to the members who also get the automatic payment? Answer to one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
63.3%
```

### Step-by-step reasoning

```text
Step 1. Doc 7: members of the No Bankruptcy Group get an automatic payment of $100.00, and members of the Aged Bankruptcy Group do not. A valid claim earns a No Bankruptcy Group member three pro rata points and an Aged Bankruptcy Group member one, and each claimant's payment is its points divided by all claimants' points, so each group's share of the valid-claims money equals its share of the points.

Step 2. Doc 7: both groups are defined by Jaffe's April 22, 2025 Supplemental Report: no locatable bankruptcy record with the same nine-digit SSN, or only one filed more than ten years before the report.

Step 3. Doc 6: Jaffe's April 22, 2025 report re-ran Step Two through Thomson Reuters, which eliminated 920 individuals and left a class list of 57,233. On that list, 20,891 class members had no bankruptcy record located in PACER or Thomson Reuters, and 36,317 had only a bankruptcy record filed more than ten years before their report.

Step 4. Doc 6 and Doc 7: No Bankruptcy Group points if every member claims: 3 × 20,891 = 62,673.

Step 5. Doc 6 and Doc 7: all points: 62,673 + 36,317 = 98,990.

Step 6. Doc 6 and Doc 7: share of the valid-claims money: 62,673 / 98,990 = 63.3% (to one decimal place).

Decoy: Doc 6 first prints Jaffe's March 2025 split, 22,212 SSNs with no bankruptcy record and 35,941 with only older filings. The April report superseded it, and the settlement groups rest on the April report.
```

### Answer components

Component 1

```text
63.3%
```

### Evidence

Evidence 1: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. 63.3% (local note: Automatic Payments, p. 5; l.63)

```text
Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim.
```

Evidence 2: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. 63.3% (local note: Automatic Payments, p. 5; l.64)

```text
Members of the Aged Bankruptcy Group will not receive these automatic payments.
```

Evidence 3: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. 63.3% (local note: Valid Claim Payments, p. 5; l.66)

```text
Each class members’s payment will be calculated by dividing the class member’s individual pro rata points by the aggregate total number of pro rata points assigned to all
```

Evidence 4: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. 63.3% (local note: p. 6; l.73)

```text
No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point.
```

Evidence 5: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. 63.3% (local note: footnote 2, p. 5; l.67)

```text
according to the analysis conducted by Plaintiff’s expert Jonathan Jaffe and set forth in his April 22, 2025 Supplemental Report, there is no locatable public record of a bankruptcy with the same nine-digit SSN
```

Evidence 6: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. 63.3% (local note: footnote 3, p. 5; l.68)

```text
the only locatable public record of a bankruptcy with the same nine-digit SSN as on the Trans Union consumer report giving rise to class membership was filed more than ten years prior to the date of that report
```

Evidence 7: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. 63.3% (local note: Post-Certification Discovery, p. 3; l.41)

```text
Jaffe Apr. 22, 2025 Report (Doc. No. 139-4, “Jaffe April 2025 Report”)
```

Evidence 8: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. 63.3% (local note: p. 4; l.47)

```text
This search resulted in the elimination of 920 individuals from the initial Step Two search, resulting in a class list of 57,233 individuals.
```

Evidence 9: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. 63.3% (local note: p. 4; l.49)

```text
Dr. Lasater generated a sample of the 20,891 class members for whom Jaffe’s search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters.
```

Evidence 10: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. 63.3% (local note: p. 5; l.61)

```text
the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years
```

### Necessary documents

- Tick Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), role: Answer component
- Tick Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), role: Answer component

Leave unticked: Doc 1 (uscourts_paed_2_22_cv_00048_0.txt), Doc 2 (uscourts_paed_2_22_cv_00048_1.txt), Doc 3 (uscourts_paed_2_22_cv_00048_2.txt), Doc 4 (uscourts_paed_2_22_cv_00048_4.txt), Doc 5 (uscourts_paed_2_22_cv_00048_6.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Entity resolution, Aggregation

Leave unticked: Unit normalization, Conditional filter

### Targeted failure modes

#### Failure mode 1

Trap: Superseded date or version

How a careless solver fails: Uses the wrong period or date

Where the trap sits:

```text
Doc 6, the Post-Certification Discovery section (pages 3-4): "This search resulted in 22,212 SSNs that had no bankruptcy records returned, and 35,941 SSNs that had one or more bankruptcy filings that predated the applicable consumer report by more than ten years." These are the results of Jaffe's March 12, 2025 report, a PACER search. The sentence describes the same two categories that Doc 7 later uses to define the settlement's groups, and it is the first split of the whole class list that Doc 6 prints, ahead of the April figures.
```

The wrong answer a careless solver gives:

```text
65.0%. Taking 22,212 as the No Bankruptcy Group and 35,941 as the Aged Bankruptcy Group gives 3 × 22,212 = 66,636 points against 66,636 + 35,941 = 102,577 points in all, and 66,636 / 102,577 = 64.96%, which rounds to 65.0%.
```

Why the correct answer avoids it:

```text
Doc 7's footnotes 2 and 3 define both groups by Jaffe's April 22, 2025 Supplemental Report. Doc 6 says that report re-ran the search through Thomson Reuters, eliminated 920 individuals and left a class list of 57,233, so the March split is out of date (its two figures sum to 58,153, not 57,233). The April split appears later in Doc 6, where Trans Union's experts drew their samples: 20,891 class members with no record located and 36,317 with only an older filing. With those figures, 62,673 / 98,990 = 63.3%. Doc 7's own reserve agrees: about $2,100,000 for $100 automatic payments fits 20,891 members, not 22,212.
```

(238 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Linking across documents

How a careless solver fails: Rounding, scale or sign

Where the trap sits:

```text
Doc 7, Payments to Class Members (page 5): "Approximately $2,100,000.00 of the Settlement Fund is reserved to provide No Bankruptcy Group class members with automatic payments." Doc 7 never states how many members either group has, and Doc 6, which does, never uses the groups' names. A solver who takes only the class-list total from Doc 6 ("a class list of 57,233 individuals", in the sentence on the Thomson Reuters re-run) without matching the settlement's group definitions to Doc 6's later descriptions can back the No Bankruptcy Group's size out of this rounded reserve instead, dividing it by the $100.00 automatic payment.
```

The wrong answer a careless solver gives:

```text
63.5%. Dividing $2,100,000 by $100 gives 21,000 members in the No Bankruptcy Group and leaves 57,233 - 21,000 = 36,233 in the Aged Bankruptcy Group, so 3 × 21,000 = 63,000 points against 63,000 + 36,233 = 99,233 in all, and 63,000 / 99,233 = 63.49%, which rounds to 63.5%. In local checks this route appeared only as a reading the solvers rejected, not as an answer.
```

Why the correct answer avoids it:

```text
The reserve is stated only as "Approximately" $2,100,000, so it cannot fix a count to the precision asked. Doc 7's footnote 2 defines the No Bankruptcy Group as the members with no locatable bankruptcy record under the same nine-digit SSN in Jaffe's April 22, 2025 report, and Doc 6 gives that count exactly: "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters," with 36,317 for the other group. The exact counts give 62,673 / 98,990 = 63.3%, and 20,891 × $100 = $2,089,100 is consistent with Doc 7's approximate $2.1 million.
```

(274 words across the three boxes; the form needs at least 150.)
