# aq-01541 q03 hand-over

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01541 --handover --q q03` from questions/q03.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 0, difficulty_target medium, origin claude.
- tested_sha256 5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D05 = Doc 4, D07 = Doc 6.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
In Brooks v. Trans Union, what was the share of class members with no bankruptcy record found at all on the class list in place when Trans Union moved to decertify, minus the same share among the class members located for June 2022 at certification? Answer in percentage points to one decimal.
```

### Number of asks

1 ask

### Gold answer

```text
-10.0 percentage points
```

### Step-by-step reasoning

```text
Step 1. Doc 4: in June 2022 the plaintiff's method located 581 class members: 270 files whose nine-digit Social Security number returned no bankruptcy on PACER and 311 that returned only a bankruptcy more than ten years old. Doc 4's printed 27.7% is 270 of the 973 searched files that had a nine-digit Social Security number, a base that also holds files whose search found a recent bankruptcy, so it is not a share of class members.

Step 2. Doc 4: no-record share among the June 2022 class members: 270 / 581 = 46.47% (to two decimal places).

Step 3. Doc 6: Trans Union moved to decertify on July 31, 2025. By then Jaffe's April 22, 2025 report had re-run Step Two through Thomson Reuters, eliminating 920 individuals and leaving a class list of 57,233, of whom 20,891 had no bankruptcy record located in PACER or Thomson Reuters.

Step 4. Doc 6: no-record share on that list: 20,891 / 57,233 = 36.50% (to two decimal places).

Step 5. Doc 4 and Doc 6: 36.50 - 46.47 = -10.0 percentage points (to one decimal place).

Decoys: Doc 4 and Doc 6: taking Doc 4's printed 27.7% as the June share gives 36.50 - 27.7 = 8.8. Doc 6's first no-record count, 22,212 SSNs, comes from Jaffe's March 2025 report, which the April report replaced before the motion.
```

### Answer components

Component 1

```text
-10.0 percentage points
```

### Evidence

Evidence 1: document Doc 4 (uscourts_paed_2_22_cv_00048_4.txt), proves component 1. -10.0 percentage points (local note: Numerosity, p. 26; l.312)

```text
In the month of June 2022 alone, Plaintiff’s proposed method for determining class membership located 581 class members.
```

Evidence 2: document Doc 4 (uscourts_paed_2_22_cv_00048_4.txt), proves component 1. -10.0 percentage points (local note: Numerosity, p. 27; l.316)

```text
determined that 270 of 97330 such files for which 9-digit social security numbers were available, or 27.7%, returned no bankruptcy on PACER, and 311 of those files, or 32.0%, returned only a stale bankruptcy that was more than ten years old
```

Evidence 3: document Doc 4 (uscourts_paed_2_22_cv_00048_4.txt), proves component 1. -10.0 percentage points (local note: footnote 30, p. 27; l.322)

```text
only 973 of the 1,100 input/output logs from June 2022 contained a nine-digit social security number
```

Evidence 4: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. -10.0 percentage points (local note: Procedural History, p. 6; l.67)

```text
Trans Union moved for decertification on July 31, 2025.
```

Evidence 5: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. -10.0 percentage points (local note: Post-Certification Discovery, p. 3; l.41)

```text
Jaffe Apr. 22, 2025 Report (Doc. No. 139-4, “Jaffe April 2025 Report”)
```

Evidence 6: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. -10.0 percentage points (local note: p. 4; l.47)

```text
This search resulted in the elimination of 920 individuals from the initial Step Two search, resulting in a class list of 57,233 individuals.
```

Evidence 7: document Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), proves component 1. -10.0 percentage points (local note: p. 4; l.49)

```text
Dr. Lasater generated a sample of the 20,891 class members for whom Jaffe’s search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters.
```

### Necessary documents

- Tick Doc 4 (uscourts_paed_2_22_cv_00048_4.txt), role: Answer component
- Tick Doc 6 (uscourts_paed_2_22_cv_00048_8.txt), role: Answer component

Leave unticked: Doc 1 (uscourts_paed_2_22_cv_00048_0.txt), Doc 2 (uscourts_paed_2_22_cv_00048_1.txt), Doc 3 (uscourts_paed_2_22_cv_00048_2.txt), Doc 5 (uscourts_paed_2_22_cv_00048_6.txt), Doc 7 (uscourts_paed_2_22_cv_00048_10.txt)

### Reasoning tags

Tick: Cross-document join, Temporal alignment, Conditional filter

Leave unticked: Unit normalization, Entity resolution, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Unit or basis

How a careless solver fails: Takes the wrong line item

Where the trap sits:

```text
Doc 4, the class certification memorandum, Numerosity section (filed page 27): "Plaintiff’s analysis of the June 2022 input/output logs determined that 270 of 97330 such files for which 9-digit social security numbers were available, or 27.7%, returned no bankruptcy on PACER". The "97330" is 973 followed by the marker of footnote 30, which says only 973 of the 1,100 June 2022 logs held a nine-digit Social Security number. The 27.7% is therefore a share of 973 searched files, a base that still includes files whose search found a bankruptcy within ten years, people outside the class. It is the only printed "no bankruptcy" percentage in the documents.
```

The wrong answer a careless solver gives:

```text
+8.8 percentage points. The solver reads 27.7% as the June 2022 share of class members with no record, takes the list's share as 20,891 / 57,233 = 36.50%, and subtracts: 36.50 - 27.7 = +8.80. With the unrounded 270 / 973 = 27.75% the result is +8.75, which also rounds to +8.8. Both the sign and the size are wrong.
```

Why the correct answer avoids it:

```text
The question measures each share among class members. Earlier in the same paragraph Doc 4 says the plaintiff's method "located 581 class members" in June 2022, which is the 270 with no bankruptcy found plus the 311 with only a stale one, so 270 / 581 = 46.47%. Against the list's 36.50%, the change is -9.97 points, or -10.0 to one decimal.
```

(229 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Superseded date or version

How a careless solver fails: Uses the wrong period or date

Where the trap sits:

```text
Doc 6, the decertification memorandum, Post-Certification Discovery (filed pages 3 to 4): "This search resulted in 22,212 SSNs that had no bankruptcy records returned, and 35,941 SSNs that had one or more bankruptcy filings that predated the applicable consumer report by more than ten years." These are the results of Jaffe's March 12, 2025 PACER search, the first version of the class list, and it is the first no-record count a reader meets in Doc 6.
```

The wrong answer a careless solver gives:

```text
-7.7 percentage points. Pairing the March count with the class list gives 22,212 / 57,233 = 38.81%, and 38.81 - 46.47 = -7.66, which rounds to -7.7. Keeping the March pair together, 22,212 out of 58,153 (38.20%), gives -8.3 instead.
```

Why the correct answer avoids it:

```text
The question takes the list in place when Trans Union moved to decertify, on July 31, 2025. The same paragraph of Doc 6 says Jaffe re-ran Step Two through Thomson Reuters in his April 22, 2025 report, which eliminated 920 people and left "a class list of 57,233 individuals", and the no-record population on that list, which Trans Union's experts later sampled, is "the 20,891 class members for whom Jaffe’s search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters." 20,891 / 57,233 = 36.50%, so the change is -10.0.
```

(212 words across the three boxes; the form needs at least 150.)
