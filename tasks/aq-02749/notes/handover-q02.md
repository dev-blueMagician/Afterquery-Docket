# aq-02749 q02 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-02749 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 2, difficulty_target medium, origin claude.
- tested_sha256 f8ddf50d5b33dbee9db14f4c8ada6e8cf9041f00c5e09542c9d14cfb5fd4fabe: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D03 = Doc 3, D04 = Doc 4, D05 = Doc 5, D06 = Doc 6.
- Floor: 0 FAIL, 4 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN documents: D03: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
  - WARN documents: D04: exclusion role; a platform reviewer accepted it only for a document ruling out an item that exists without it, not for its own decoy (aq-01333 q01)
  - WARN documents: 5 documents listed; the form's reasoning usually covers 2-4, only those the answer relies on
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Under EPA's five proposed State coal-ash program approvals, how many of the 2024 Legacy Rule's all-unit amendments would lack an approved State version in exactly two States, and how many in all five? Give the two counts in that order.
```

### Number of asks

2 asks

### Gold answer

```text
10, 12
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, Wyoming Partial Program): Wyoming "is not seeking approval for" the "Amendments made in the Legacy CCR Surface Impoundments and CCR Management Units Final Rule", so no amendment made by that rule would have an approved Wyoming version. Wyoming is one of the States without one for every such amendment.
Step 2. Source input (Doc 5, Alabama Partial Program): for the terms and provisions that rule changed for all CCR units, "EPA is approving the State's version of these requirements", a numbered list that ends at entry 17. The next list, of amendments that "are not being approved", has 5 entries, and 3 of the 5 entries are 2024 Legacy Rule all-unit definitions: "Contains both CCR and liquids", "Infiltration" and "Liquids". The other two entries concern alternate liner demonstrations and suspension of groundwater monitoring.
Step 3. Source input (Doc 6, Wisconsin Partial Program): "EPA is approving the State's version of these requirements", a numbered list that ends at entry 11. It includes "Infiltration" and "Liquids", which Alabama's approved list does not; every other Wisconsin entry is also on Alabama's approved list.
Step 4. Source input (Doc 3, Doc 4, Doc 5 and Doc 6): Virginia's list ("EPA is approving the State's version of the following requirements") and Louisiana's ("EPA is approving the State's version of these requirements") carry every entry on Alabama's or Wisconsin's approved list, among them "Infiltration", "Liquids" and the scope provision on inactive impoundments that Wisconsin's list lacks, and "Contains both CCR and liquids" as well. Virginia and Louisiana therefore have an approved version of every one of them, which is why an amendment missing in Wyoming and one other State is missing in exactly two States. The rule's other all-unit amendments are the more prescriptive ones: each of these four proposals says the State "did not adopt these amendments and did not seek approval of these provisions", and Wyoming seeks approval of none, so they lack an approved version in all five States.
Step 5. Calculation (Doc 5 and Doc 6): entries on both Alabama's and Wisconsin's approved lists, which are Wisconsin's entries less "Infiltration" and "Liquids": 11 - 2 = 9.
Step 6. Calculation (Doc 5 and Doc 6): entries approved for Alabama but not for Wisconsin: 17 - 9 = 8. They are the scope provision on inactive impoundments, the reserved effective-date section, the definitions of "CCR surface impoundment", "CCR unit", "Inactive CCR surface impoundment", "Technically feasible" and "Technically infeasible", and the compliance-deadline provision for inactive impoundments. Virginia, Louisiana and Alabama approve them, so each lacks an approved version only in Wyoming and Wisconsin.
Step 7. First count (Doc 2, Doc 3, Doc 4, Doc 5 and Doc 6): "Infiltration" and "Liquids" are approved for Virginia, Louisiana and Wisconsin, so each lacks an approved version only in Wyoming and Alabama. Adding them: 8 + 2 = 10. Amendments missing in only one State are excluded: the entries on both Alabama's and Wisconsin's lists lack an approved version in Wyoming alone. The amendment missing in three States is excluded too: "Contains both CCR and liquids" lacks an approved version in Wyoming, Alabama and Wisconsin.
Step 8. Source input (Doc 3, Doc 4, Doc 5 and Doc 6): the more prescriptive amendments are the rule's other all-unit amendments, the ones that "apply to all CCR units and are more prescriptive than the requirements in the 2015 CCR Rule". They form a list that ends at entry 12 in Virginia's, Louisiana's and Alabama's proposals and runs from a to l in Wisconsin's, with the same entries in each, and each of these four States "did not adopt these amendments and did not seek approval of these provisions".
Step 9. Second count (Doc 2, Doc 3, Doc 4, Doc 5 and Doc 6): Wyoming seeks approval of no amendment made by the rule, so those 12 lack an approved State version in all five States. No entry of the first list does, because Virginia and Louisiana approve every one of them. The two counts, in the order asked, are 10 and 12.
```

### Answer components

Component 1

```text
10
```

Component 2

```text
12
```

### Evidence

Evidence 1: document Doc 2 (fr_2025_16801.txt), proves component 1. 10 (local note: Wyoming Partial Program, L280)

```text
Wyoming is not seeking approval for the following four requirements of the Federal CCR regulations
```

Evidence 2: document Doc 2 (fr_2025_16801.txt), proves component 1. 10 (local note: Wyoming Partial Program, L282)

```text
Amendments made in the Legacy CCR Surface Impoundments and CCR Management Units Final Rule.
```

Evidence 3: document Doc 2 (fr_2025_16801.txt), proves component 2. 12 (local note: Wyoming Partial Program, L282)

```text
Amendments made in the Legacy CCR Surface Impoundments and CCR Management Units Final Rule.
```

Evidence 4: document Doc 3 (fr_2026_08662.txt), proves component 1. 10 (local note: Virginia Partial Program, L246)

```text
Therefore, EPA is approving the State's version of the following requirements:
```

Evidence 5: document Doc 3 (fr_2026_08662.txt), proves component 1. 10 (local note: Virginia Partial Program, L248)

```text
2. 40 CFR 257.50(c); this amendment revises the scope of applicability to specify that it includes inactive CCR surface impoundments
```

Evidence 6: document Doc 3 (fr_2026_08662.txt), proves component 1. 10 (local note: Virginia Partial Program, L258)

```text
11. ``Infiltration''; this additional definition in 40 CFR 257.53 is consistent with the term's plain meaning and dictionary definitions
```

Evidence 7: document Doc 3 (fr_2026_08662.txt), proves component 1. 10 (local note: Virginia Partial Program, L259)

```text
12. ``Liquids''; this additional definition in 40 CFR 257.53 is consistent with the term's plain meaning and dictionary definitions
```

Evidence 8: document Doc 3 (fr_2026_08662.txt), proves component 1. 10 (local note: Virginia Partial Program, L278)

```text
VADEQ did not adopt these amendments and did not seek approval of these provisions.
```

Evidence 9: document Doc 3 (fr_2026_08662.txt), proves component 2. 12 (local note: Virginia Partial Program, L278)

```text
apply to all CCR units and are more prescriptive than the requirements in the 2015 CCR Rule. VADEQ did not adopt these amendments and did not seek approval of these provisions.
```

Evidence 10: document Doc 3 (fr_2026_08662.txt), proves component 2. 12 (local note: Virginia Partial Program, L290)

```text
12. 40 CFR 257.107(e); (f)(1) through (4); (f)(6) through (13); (f)(18);
```

Evidence 11: document Doc 4 (fr_2026_11312.txt), proves component 1. 10 (local note: Louisiana Partial Program, L316)

```text
Therefore, EPA is approving the State's version of these requirements:
```

Evidence 12: document Doc 4 (fr_2026_11312.txt), proves component 1. 10 (local note: Louisiana Partial Program, L318)

```text
2. 40 CFR 257.50(c); this amendment revises the scope of applicability to specify that it includes inactive CCR surface impoundments
```

Evidence 13: document Doc 4 (fr_2026_11312.txt), proves component 1. 10 (local note: Louisiana Partial Program, L328)

```text
11. ``Infiltration''; this additional definition in 40 CFR 257.53 is consistent with the term's plain meaning and dictionary definitions
```

Evidence 14: document Doc 4 (fr_2026_11312.txt), proves component 1. 10 (local note: Louisiana Partial Program, L329)

```text
12. ``Liquids''; this additional definition in 40 CFR 257.53 is consistent with the term's plain meaning and dictionary definitions
```

Evidence 15: document Doc 4 (fr_2026_11312.txt), proves component 1. 10 (local note: Louisiana Partial Program, L348)

```text
LDEQ did not adopt these amendments and did not seek approval of these provisions.
```

Evidence 16: document Doc 4 (fr_2026_11312.txt), proves component 2. 12 (local note: Louisiana Partial Program, L348)

```text
apply to all CCR units and are more prescriptive than the requirements in the 2015 CCR Rule. LDEQ did not adopt these amendments and did not seek approval of these provisions.
```

Evidence 17: document Doc 4 (fr_2026_11312.txt), proves component 2. 12 (local note: Louisiana Partial Program, L360)

```text
12. 40 CFR 257.107(e); (f)(1) through (4); (f)(6) through (13); (f)(18);
```

Evidence 18: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L308)

```text
In the 2024 Legacy Rule, EPA amended certain terms and provisions that apply to all CCR units.
```

Evidence 19: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L308)

```text
Therefore, EPA is approving the State's version of these requirements:
```

Evidence 20: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L329)

```text
17. 40 CFR 257.104(a); this amendment clarifies that all owners or operators of CCR units that are subject to Sec. 257.102 are subject to the post-closure care requirements
```

Evidence 21: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L337)

```text
as enumerated below, are not being approved:
```

Evidence 22: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L338)

```text
1. ``Contains both CCR and liquids''; this additional definition in
```

Evidence 23: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L340)

```text
2. ``Infiltration''; this additional definition in 40 CFR 257.53 is consistent with the term's plain meaning and dictionary definitions
```

Evidence 24: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L341)

```text
3. ``Liquids''; this additional definition in 40 CFR 257.53 is consistent with the term's plain meaning and dictionary definitions
```

Evidence 25: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L342)

```text
4. 40 CFR 257.71(d) for alternate liner demonstrations; and
```

Evidence 26: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L343)

```text
5. 40 CFR 257.90(g) for suspension of groundwater monitoring requirements based on a no migration demonstration.
```

Evidence 27: document Doc 5 (fr_2026_14118.txt), proves component 1. 10 (local note: Alabama Partial Program, L344)

```text
ADEM did not adopt these amendments and did not seek approval of these provisions.
```

Evidence 28: document Doc 5 (fr_2026_14118.txt), proves component 2. 12 (local note: Alabama Partial Program, L344)

```text
apply to all CCR units and are more prescriptive than the requirements in the 2015 CCR Rule. ADEM did not adopt these amendments and did not seek approval of these provisions.
```

Evidence 29: document Doc 5 (fr_2026_14118.txt), proves component 2. 12 (local note: Alabama Partial Program, L359)

```text
12. 40 CFR 257.107(e); (f)(1) through (4); (f)(6) through (13); (f)(18);
```

Evidence 30: document Doc 6 (fr_2026_18552.txt), proves component 1. 10 (local note: Wisconsin Partial Program, L309)

```text
Therefore, EPA is approving the State's version of these requirements:
```

Evidence 31: document Doc 6 (fr_2026_18552.txt), proves component 1. 10 (local note: Wisconsin Partial Program, L314)

```text
5. ``Infiltration''; this additional definition in 40 CFR 257.53 is consistent with the term's plain meaning and dictionary definitions
```

Evidence 32: document Doc 6 (fr_2026_18552.txt), proves component 1. 10 (local note: Wisconsin Partial Program, L315)

```text
6. ``Liquids''; this additional definition in 40 CFR 257.53 is consistent with the term's plain meaning and dictionary definitions
```

Evidence 33: document Doc 6 (fr_2026_18552.txt), proves component 1. 10 (local note: Wisconsin Partial Program, L320)

```text
11. 40 CFR 257.104(a); this amendment clarifies that all owners or operators of CCR units that are subject to Sec. 257.102 are subject to the post-closure care requirements
```

Evidence 34: document Doc 6 (fr_2026_18552.txt), proves component 1. 10 (local note: Wisconsin Partial Program, L404)

```text
WDNR did not adopt these amendments and did not seek approval of these provisions.
```

Evidence 35: document Doc 6 (fr_2026_18552.txt), proves component 2. 12 (local note: Wisconsin Partial Program, L404)

```text
apply to all CCR units and are more prescriptive than the requirements in the 2015 CCR Rule. WDNR did not adopt these amendments and did not seek approval of these provisions.
```

Evidence 36: document Doc 6 (fr_2026_18552.txt), proves component 2. 12 (local note: Wisconsin Partial Program, L417)

```text
l. 40 CFR 257.107(e); (f)(1) through (4); (f)(6) through (13); (f)(18);
```

### Necessary documents

- Tick Doc 2 (fr_2025_16801.txt), role: Answer component
- Tick Doc 3 (fr_2026_08662.txt), role: Exclusion / condition source

  Reviewer note:

```text
Requested by the reviewer. Doc 3's approved list shows Virginia approves every counted amendment, for example 40 CFR 257.50(c), Infiltration and Liquids. That rules out Virginia as a third State lacking a version, so each of the 10 is missing in exactly two States. Its second list shows Virginia did not adopt the 12 more prescriptive amendments, which the all-five count needs.
```
- Tick Doc 4 (fr_2026_11312.txt), role: Exclusion / condition source

  Reviewer note:

```text
Requested by the reviewer. Doc 4's approved list shows Louisiana approves every counted amendment, for example 40 CFR 257.50(c), Infiltration and Liquids. That rules out Louisiana as a third State lacking a version, so each of the 10 is missing in exactly two States. Its second list shows Louisiana did not adopt the 12 more prescriptive amendments, which the all-five count needs.
```
- Tick Doc 5 (fr_2026_14118.txt), role: Answer component
- Tick Doc 6 (fr_2026_18552.txt), role: Answer component

Leave unticked: Doc 1 (fr_2025_11907.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Wrong members in a list

#### Failure mode 2

Trap: Wrong jurisdiction or scope

How a careless solver fails: Picks the wrong entity or section

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 2 groups Wyoming's unapproved 2024 amendments; leaving Wyoming out gives 1 and 0. Wrong jurisdiction or scope: Doc 6 approves "Infiltration" and "Liquids", which Doc 5 lists as not approved for Alabama; treating Alabama like Wisconsin gives 8 and 12. Gold: 10 and 12.
```

(48 / 50 words.)
