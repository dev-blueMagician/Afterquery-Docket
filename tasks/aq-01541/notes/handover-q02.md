# aq-01541 q02 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01541 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D03 = Doc 7, D07 = Doc 6.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN sibling: six words shared with q01: 'in trans union's preliminarily approved settlement'
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Suppose every member of the class in Trans Union's preliminarily approved settlement filed a valid claim. Taking the court's figure for the money set aside for valid-claim payments, how many dollars of it would go to each claimant who gets no automatic payment? Give one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
$29.1
```

### Step-by-step reasoning

```text
Step 1. Doc 7: members of the No Bankruptcy Group get an automatic payment of $100.00, and members of the Aged Bankruptcy Group do not, so the claimants who get no automatic payment are the Aged Bankruptcy Group. Approximately $2,882,000.00 is reserved for valid-claim payments. A valid claim earns a No Bankruptcy Group member three pro rata points and an Aged Bankruptcy Group member one, and each claimant's payment is its points divided by all claimants' points, so an Aged Bankruptcy Group claimant receives the value of one point.

Step 2. Doc 7: both groups are defined by Jaffe's April 22, 2025 Supplemental Report: no locatable bankruptcy record with the same nine-digit SSN, or only one filed more than ten years before the report.

Step 3. Doc 6: Jaffe's April 22, 2025 report re-ran Step Two through Thomson Reuters, which eliminated 920 individuals and left a class list of 57,233. On that list, 20,891 class members had no bankruptcy record located in PACER or Thomson Reuters, and 36,317 had only a bankruptcy record filed more than ten years before their report.

Step 4. Doc 6 and Doc 7: No Bankruptcy Group points if every member claims: 3 × 20,891 = 62,673.

Step 5. Doc 6 and Doc 7: all points: 62,673 + 36,317 = 98,990.

Step 6. Doc 6 and Doc 7: one point's share of the valid-claims money: 2,882,000 / 98,990 = 29.1 dollars (to one decimal place).

Decoys: Doc 7's "approximately $350" for Aged Bankruptcy Group claimants is the plaintiff's estimate at typical claim rates, not the payment when every member claims. Doc 6 first prints Jaffe's March 2025 split, 22,212 SSNs with no bankruptcy record and 35,941 with only older filings, which the April report superseded.
```

### Answer components

Component 1

```text
$29.1
```

### Evidence

Evidence 1: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. $29.1 (local note: Automatic Payments, p. 5; l.63)

```text
Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim.
```

Evidence 2: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. $29.1 (local note: Automatic Payments, p. 5; l.64)

```text
Members of the Aged Bankruptcy Group will not receive these automatic payments.
```

Evidence 3: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. $29.1 (local note: Valid Claim Payments, p. 5; l.66)

```text
Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims.
```

Evidence 4: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. $29.1 (local note: Valid Claim Payments, p. 5; l.66)

```text
Each class members’s payment will be calculated by dividing the class member’s individual pro rata points by the aggregate total number of pro rata points assigned to all
```

Evidence 5: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. $29.1 (local note: p. 6; l.73)

```text
No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point.
```

Evidence 6: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. $29.1 (local note: footnote 2, p. 5; l.67)

```text
according to the analysis conducted by Plaintiff’s expert Jonathan Jaffe and set forth in his April 22, 2025 Supplemental Report, there is no locatable public record of a bankruptcy with the same nine-digit SSN
```

Evidence 7: document Doc 7 (uscourts_paed_2_22_cv_00048_10.txt), proves component 1. $29.1 (local note: footnote 3, p. 5; l.68)

```text
the only locatable public record of a bankruptcy with the same nine-digit SSN as on the Trans Union consumer report giving rise to class membership was filed more than ten years prior to the date of that report
```

Evidence 8: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. $29.1 (local note: Post-Certification Discovery, p. 3; l.41)

```text
Jaffe Apr. 22, 2025 Report (Doc. No. 139-4, “Jaffe April 2025 Report”)
```

Evidence 9: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. $29.1 (local note: p. 4; l.47)

```text
This search resulted in the elimination of 920 individuals from the initial Step Two search, resulting in a class list of 57,233 individuals.
```

Evidence 10: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. $29.1 (local note: p. 4; l.49)

```text
Dr. Lasater generated a sample of the 20,891 class members for whom Jaffe’s search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters.
```

Evidence 11: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. $29.1 (local note: p. 5; l.61)

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

Trap: Look-alike measure

How a careless solver fails: Misapplies a rule or premise

Where the trap sits:

```text
Doc 7, Payments to Class Members (page 6): "Class members in the Aged Bankruptcy Group who submit valid claims are expected to receive approximately $350." The same estimate is repeated in the court's equitable-treatment discussion (page 17). It is a printed dollar figure for exactly the people the question asks about, the claimants who get no automatic payment. It belongs to the plaintiff's projections in that paragraph: the companion figure for the other group is described as based "on estimates derived from similar litigation as well as from typical claims rates data for similar cases", and the court calls both "these estimates based on historical data", so they assume a settlement in which only some members claim.
```

The wrong answer a careless solver gives:

```text
$350. A solver who finds the group and its printed expected payment answers with that figure, ignoring the question's premise that every member of the class files a valid claim, and so never computes the point value at all.
```

Why the correct answer avoids it:

```text
The question fixes the claim rate: every member of both groups files a valid claim. Under Doc 7's formula each claimant's share is its points over all claimants' points, so with every member claiming the points are 3 × 20,891 + 36,317 = 98,990 (counts from Doc 6's April list), and one point, which is all an Aged Bankruptcy Group claimant holds, is worth 2,882,000 / 98,990 = $29.11, or $29.1. The $350 estimate rests on far fewer claimants sharing the same money, so it cannot apply.
```

(243 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Superseded date or version

How a careless solver fails: Uses the wrong period or date

Where the trap sits:

```text
Doc 6, the Post-Certification Discovery section (pages 3-4): "This search resulted in 22,212 SSNs that had no bankruptcy records returned, and 35,941 SSNs that had one or more bankruptcy filings that predated the applicable consumer report by more than ten years." These are the results of Jaffe's March 12, 2025 report, a PACER search, and they paraphrase the two definitions Doc 7 gives the settlement's groups. They are the first split of the whole class list that Doc 6 prints.
```

The wrong answer a careless solver gives:

```text
$28.1. Taking 22,212 as the No Bankruptcy Group and 35,941 as the Aged Bankruptcy Group gives 3 × 22,212 + 35,941 = 102,577 points, and 2,882,000 / 102,577 = $28.10, or $28.1.
```

Why the correct answer avoids it:

```text
Doc 7's footnotes 2 and 3 define both groups by Jaffe's April 22, 2025 Supplemental Report. Doc 6 says that report re-ran the search through Thomson Reuters, eliminated 920 individuals and left a class list of 57,233, and it later gives the April split, 20,891 and 36,317, where Trans Union's experts drew their samples. Those counts give 98,990 points and $29.1 per point. The March figures also sum to 58,153, not the 57,233 on the list.
```

(188 words across the three boxes; the form needs at least 150.)
