# aq-02447 q01 hand-over

Generated 2026-10-09 by `python tools/check_questions.py tasks/aq-02447 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 3, difficulty_target medium, origin claude.
- tested_sha256 b1fe5542bdd7fa87e85b31bbfc9ff3c3d99621d2df1a895025e76e6c3bfc55af: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D01 = Doc 1, D06 = Doc 6.
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
How many distinct ECCNs in the UAE license requirement of BIS's July 2026 rule were absent from the China-and-Macau license requirement of its January 2023 Macau rule?
```

### Number of asks

1 ask

### Gold answer

```text
10 ECCNs
```

### Step-by-step reasoning

```text
Step 1. Source fact (Doc 6, amendment 7, which revises § 742.6(a)(6)(iii)(B), headed "License Requirement for the United Arab Emirates (UAE) and Country Groups D:1, D:4, or D:5"; the rule is effective July 10, 2026): this UAE license requirement covers items specified in ECCNs 3A001 (z paragraphs), 3A090.b, 3D001, 3E001, 4A003 (z paragraphs), 4A004.z.2, 4A005.z.2, 4A090.b, 4D001, 4D090, 4E001, 5A002 (z paragraphs), 5A004 (z paragraphs), 5A992.z.2, 5D002 (z paragraphs), 5D992.z.2, 5E002 and 5E992.

Step 2. Source fact (Doc 1, amendment 9, which revises § 742.6(a)(6), the "RS requirement that applies to the People's Republic of China (China) and Macau"; the rule is effective January 17, 2023): paragraph (a)(6)(i) requires a license for China or Macau for items specified in ECCNs 3A090, 3B090, 4A090 and 5A992 (meeting the 3A090 or 4A090 parameters) and associated software and technology in 3D001, 3E001, 4D090, 4E001 and 5D992 (meeting the same parameters); paragraph (a)(6)(ii) names no ECCN. The RS control paragraphs of the seven ECCN entries the rule also revises point to this paragraph ("See Sec. 742.6(a)(6)"), and the rule's other China-and-Macau restrictions name only 3B-group ECCNs, 3D001 and 3E001, none of them in Step 1's list beyond those already shared.

Step 3. Matching (Doc 6 and Doc 1): counted by ECCN, Step 1's 5A992.z.2 is a paragraph of ECCN 5A992 and 5D992.z.2 a paragraph of ECCN 5D992, so the ECCNs named in both texts are 3A090, 3D001, 3E001, 4A090, 4D090, 4E001, 5A992 and 5D992; 3B090 is named only in 2023.

Step 4. Exclusion (Doc 6 and Doc 1): Step 1's ECCNs absent from Step 2 are, in Category 3, 3A001; in Category 4, 4A003, 4A004, 4A005 and 4D001; in Category 5, 5A002, 5A004, 5D002, 5E002 and 5E992.

Step 5. Calculation (Doc 6 and Doc 1): new Category 4 and Category 5 ECCNs from Step 4: 4 + 5 = 9.

Step 6. Calculation (Doc 6 and Doc 1): adding Category 3's 3A001: 9 + 1 = 10 distinct ECCNs named in 2026 but not in 2023.

Step 7. Look-alike check (Doc 1): the preamble's list of the seven ECCNs whose RS control paragraphs gained Macau leaves out 5A992 and 5D992, which § 742.6(a)(6)(i) itself names; counting against that list instead would give 12.
```

### Answer components

Component 1

```text
10
```

### Evidence

Evidence 1: document Doc 6 (fr_2026_14132.txt), proves component 1. 10 (local note: DATES, L30)

```text
This rule is effective July 10, 2026.
```

Evidence 2: document Doc 6 (fr_2026_14132.txt), proves component 1. 10 (local note: amendment 7, L256)

```text
7. Sec. 742.6 is amended by revising paragraph (a)(6)(iii)(B) to read as follows:
```

Evidence 3: document Doc 6 (fr_2026_14132.txt), proves component 1. 10 (local note: revised § 742.6(a)(6)(iii)(B) heading, L263)

```text
(B) License Requirement for the United Arab Emirates (UAE) and Country Groups
```

Evidence 4: document Doc 6 (fr_2026_14132.txt), proves component 1. 10 (local note: revised § 742.6(a)(6)(iii)(B), L264)

```text
A license is required to export, reexport, or transfer (in-country) items specified in ECCNs 3A001.z.1.b, z.2.b, z.3.b, z.4.b; 3A090.b; 3D001 (for ``software'' for commodities controlled by 3A001.z.1.b, z.2.b, z.3.b, z.4.b; 3A090.b); 3E001 (for ``technology'' for commodities controlled by 3A001.z.1.b, z.2.b, z.3.b, z.4.b, or 3A090.b); 4A003.z.1.b, z.2.b; 4A004.z.2; 4A005.z.2; 4A090.b; 4D001 (for ``software'' for commodities controlled by 4A003.z.1.b, z.2.b, 4A004.z.2, and 4A005.z.2); 4D090 (for ``software'' for commodities controlled by 4A090.b); 4E001 (for commodities controlled by 4A003.z.1.b, z.2.b, 4A004.z.2, 4A005.z.2, 4A090.b or ``software'' specified by 4D001 (for 4A003.z.1.b, z.2.b, 4A004.z.2, or 4A005.z.2), or 4D090 (for ``software'' for commodities controlled by 4A090.b)); 5A002.z.1.b, z.2.b, z.3.b, z.4.b, z.5.b; 5A004.z.1.b, z.2.b; 5A992.z.2; 5D002.z.1.b, z.2.b, z.3.b, z.4.b, z.5.b, z.6.b, z.7.b, z.8.b, and z.9.b; 5D992.z.2; 5E002 (for ``technology'' for commodities controlled by 5A002.z.1.b, z.2.b, z.3.b, z.4.b, z.5.b or 5A004.z.1.b, z.2.b or ``software'' specified by 5D002 (for 5A002. z.1.b, z.2.b, z.3.b, z.4.b, z.5.b or 5A004.z.1.b, z.2.b commodities)); or 5E992
```

Evidence 5: document Doc 1 (fr_2023_00888.txt), proves component 1. 10 (local note: DATES, L31)

```text
Effective date: This rule is effective on January 17, 2023.
```

Evidence 6: document Doc 1 (fr_2023_00888.txt), proves component 1. 10 (local note: amendment 9, L224)

```text
9. Section 742.6 is amended by revising paragraphs (a)(6) and (b)(10) to read as follows:
```

Evidence 7: document Doc 1 (fr_2023_00888.txt), proves component 1. 10 (local note: revised § 742.6(a)(6) heading, L229)

```text
RS requirement that applies to the People's Republic of China (China) and Macau for advanced computing and semiconductor manufacturing items
```

Evidence 8: document Doc 1 (fr_2023_00888.txt), proves component 1. 10 (local note: revised § 742.6(a)(6)(i), L229)

```text
A license is required for items specified in ECCNs 3A090, 3B090, 4A090, 5A992 (that meet or exceed the performance parameters of ECCNs 3A090 or 4A090) and associated software and technology in 3D001 (for 3A090 or 3B090), 3E001 (for 3A090 or 3B090), 3B090, or 3D001 (for 3A090 or 3B090), 4D090, 4E001 (for 4A090 and 4D090), and 5D992 (that meet or exceed the performance parameters of ECCNs 3A090 or 4A090)
```

### Necessary documents

- Tick Doc 6 (fr_2026_14132.txt), role: Answer component
- Tick Doc 1 (fr_2023_00888.txt), role: Answer component

Leave unticked: Doc 2 (fr_2024_06067.txt), Doc 3 (fr_2024_22587.txt), Doc 4 (fr_2025_17893.txt), Doc 5 (fr_2026_10712.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution, Aggregation

Leave unticked: Temporal alignment, Unit normalization

### Targeted failure modes

#### Failure mode 1

Trap: Look-alike measure

How a careless solver fails: Takes the wrong line item

#### Failure mode 2

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Look-alike measure: Doc 1's preamble lists seven ECCNs whose RS paragraphs gained Macau, lacking 5A992 and 5D992; using it gives 12. Linking: Doc 6's 5A992.z.2 and 5D992.z.2 are paragraphs of Doc 1's ECCNs 5A992 and 5D992; left unmatched they give 12. Gold: 18 named, 8 shared, 10.
```

(47 / 50 words.)
