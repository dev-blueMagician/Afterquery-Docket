# aq-01650 q01 hand-over

> WITHDRAWN 2026-10-08: q01 is dropped for the Medium target. A platform difficulty check on a
> closely related wording (version 1923ac) ended "Answer not supported" (Low 3/5; the high model took
> 13.7 in 3 of 3 every-document attempts). Do not paste or run this sheet. Details: questions/q01.md
> Feedback log. The text below is the stale rev 1 sheet, kept only as a record.

Generated 2026-10-08 by `python tools/check_questions.py tasks/aq-01650 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 1, difficulty_target medium, origin claude.
- tested_sha256 4f003703a5866803c8eb8c390fb0a3d6018bb6af42f0fda2e748f53199319b40: question, number of asks, answer, answer type, components, reasoning, evidence, documents, tags, target and corpus. Targeted failure modes are outside it, and so are the default Answer component roles shown below.
- Local ids and the task page's numbers: D01 = Doc 5, D03 = Doc 2.
- Floor: 0 FAIL, 1 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
On each survey's own literacy test, how many percentage points higher was the average share of questions answered correctly by all non-student respondents to Japan's 2016 Financial Literacy Survey than by households in the 2015 China Household Finance Survey? Give one decimal place.
```

### Number of asks

1 ask

### Gold answer

```text
9.2 percentage points
```

### Step-by-step reasoning

```text
Step 1. Doc 5: Japan's survey measured financial literacy as the number of correct answers out of 25 questions. The study excluded 1,212 students, leaving 23,788 non-student respondents.
Step 2. Doc 5 (gender decomposition table, N 23,788 with 11,658 men and 12,130 women): men averaged 14.719 correct answers and women 13.480. 11,658 × 14.719 = 171,594.102
Step 3. Doc 5: 12,130 × 13.480 = 163,512.4
Step 4. Doc 5: 171,594.102 + 163,512.4 = 335,106.502
Step 5. Doc 5: 335,106.502 / 23,788 = 14.0872 correct answers per non-student respondent
Step 6. Doc 5: 14.0872 / 25 = 56.349% of the questions answered correctly
Step 7. Doc 2: for the 2015 China Household Finance Survey, the mean number of the three questions answered correctly was 1.414. 1.414 / 3 = 47.133%
Step 8. Doc 5 and Doc 2: 56.349% - 47.133% = 9.2 percentage points (to one decimal place)
Step 9. Doc 5: the descriptive table's financial literacy mean of 15.2 covers only the 15,228 complete cases (non-students with no missing education, self-rating, income or asset data), so it is not the mean for all 23,788 non-student respondents.
```

### Answer components

Component 1

```text
9.2 percentage points
```

### Evidence

Evidence 1: document Doc 5 (Age-gender-and-financial-literacy-in-Japan.txt), proves component 1. 9.2 percentage points (local note: Doc 5, Definitions of variables)

```text
we measured knowledge-based financial literacy by the number of correct answers out of 25 questions on the survey
```

Evidence 2: document Doc 5 (Age-gender-and-financial-literacy-in-Japan.txt), proves component 1. 9.2 percentage points (local note: Doc 5, Methods, sample)

```text
We exclude students (n = 1,212) from our analyses, since they may not be financially independent. Among the remaining 23,788 respondents
```

Evidence 3: document Doc 5 (Age-gender-and-financial-literacy-in-Japan.txt), proves component 1. 9.2 percentage points (local note: Doc 5, Table 5)

```text
Men: 14.719 (0.067)Women: 13.480 (0.060)
```

Evidence 4: document Doc 5 (Age-gender-and-financial-literacy-in-Japan.txt), proves component 1. 9.2 percentage points (local note: Doc 5, Table 5, N row)

```text
23,788 (Men: 11,658, Women: 12,130)
```

Evidence 5: document Doc 2 (Does-Financial-Literacy-Affect-Household-Financial-Behavior.txt), proves component 1. 9.2 percentage points (local note: Doc 2, Financial Literacy)

```text
The mean value of the number of questions they answered correctly was just 1.414
```

Evidence 6: document Doc 2 (Does-Financial-Literacy-Affect-Household-Financial-Behavior.txt), proves component 1. 9.2 percentage points (local note: Doc 2, Table 1 note)

```text
Calculated by the data of Chinese Household Financial Survey in 2015.
```

Evidence 7: document Doc 2 (Does-Financial-Literacy-Affect-Household-Financial-Behavior.txt), proves component 1. 9.2 percentage points (local note: Doc 2, Financial Literacy)

```text
only 10.77% of the households answered all three questions (interest rate calculation, inflation, and venture market) correctly
```

### Necessary documents

- Tick Doc 5 (Age-gender-and-financial-literacy-in-Japan.txt), role: Answer component
- Tick Doc 2 (Does-Financial-Literacy-Affect-Household-Financial-Behavior.txt), role: Answer component

Leave unticked: Doc 1 (Household-financial-literacy-and-relative-poverty-An.txt), Doc 3 (Does-financial-literacy-influence-preventive-health-check-up.txt), Doc 4 (Financial-Literacy-Financial-Education-and-Cancer-Screening.txt), Doc 6 (Digital-inclusive-finance-and-asset-allocation-of-Chinese.txt), Doc 7 (The-roles-of-financial-literacy-and-overconfidence-in.txt)

### Reasoning tags

Tick: Cross-document join, Unit normalization, Aggregation

Leave unticked: Temporal alignment, Conditional filter, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Part vs total

How a careless solver fails: Picks the wrong entity or section

Where the trap sits:

```text
Doc 5, the study of age, gender and financial literacy in Japan. Its sample paragraph begins by excluding 1,212 students, says "Among the remaining 23,788 respondents" some lacked education, self-rating, income or asset information, and then states "Thus, the final usable number of complete cases equalled 15,228 individuals. Table 2 shows the descriptive statistics by gender." Table 2, which follows that paragraph under the title "Descriptive statistics for complete cases", prints the only overall financial literacy mean in the paper: a "Financial literacy" row with N 15,228, mean 15.2 and standard deviation 6.6. It carries the asked measure's own label and comes straight after the paragraph that excludes the students, so it looks like the non-student figure.
```

The wrong answer a careless solver gives:

```text
13.7 percentage points. The solver takes 15.2 correct answers as the non-student mean, converts it to 15.2 / 25 = 60.8% of the 25 questions, takes Doc 2's 2015 mean of 1.414 of three questions (47.133%), and subtracts: 60.8 - 47.133 = 13.667, or 13.7 at one decimal place.
```

Why the correct answer avoids it:

```text
A careful reader checks the N beside the 15.2: it is 15,228, the complete cases, not all 23,788 non-students, as the question asks. The other 8,560 non-students, who lacked education, self-rating, income or asset information, are left out of Table 2 but kept in the paper's regressions and decomposition, which use all 23,788 non-students (11,658 men and 12,130 women) and impute the missing items. The literacy score is not among the items the paper lists as missing, so the decomposition's means are averages over all 23,788 non-students. That table gives 14.719 for men and 13.480 for women, with N 23,788 (11,658 men, 12,130 women). Weighting them gives 14.0872 correct answers, 56.349% of the questions, and 56.349 - 47.133 = 9.216, which is 9.2 percentage points at one decimal place.
```

(295 words across the three boxes; the form needs at least 150.)

#### Failure mode 2

Trap: Figure that must be computed

How a careless solver fails: Calculation slip

Where the trap sits:

```text
Doc 5's gender decomposition table (Table 5) is the only place that reports financial literacy means for all non-student respondents. It prints two of them in its header, "Men: 14.719 (0.067)Women: 13.480 (0.060)", and gives the group sizes only in a separate N row at the foot of the table, "23,788 (Men: 11,658, Women: 12,130)". No overall non-student mean is printed anywhere in the paper, so the solver has to build one from these two rows.
```

The wrong answer a careless solver gives:

```text
9.3 percentage points. The solver averages the two printed means without weights, as if the two groups were the same size: (14.719 + 13.480) / 2 = 14.0995 correct answers, which is 56.398% of the 25 questions. Against Doc 2's 47.133%, that gives 56.398 - 47.133 = 9.265, or 9.3 at one decimal place.
```

Why the correct answer avoids it:

```text
Women outnumber men among the non-students (12,130 against 11,658), so the overall mean must weight each sex by its own count in the 23,788: (11,658 x 14.719 + 12,130 x 13.480) / 23,788 = 14.0872. Without rounding it first, that is 56.349% of the questions, and 56.349 - 47.133 = 9.216, which is 9.2 at the one decimal place the question asks for. Using Doc 2's distribution instead of its printed mean (1.4142 correct answers) gives 9.209, still 9.2.
```

(209 words across the three boxes; the form needs at least 150.)
