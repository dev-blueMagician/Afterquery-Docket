# aq-02780 q01 hand-over

Generated 2026-10-11 by `python tools/check_questions.py tasks/aq-02780 --handover --q q01` from questions/q01.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 5, difficulty_target medium, origin user+claude.
- tested_sha256 9a1c7f695d366cdad73ac51798f5c08f9cd9d6f3062e7455da391726f398b4bc: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D04 = Doc 4, D07 = Doc 7.
- Floor: 0 FAIL, 2 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin user+claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q01.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
A State nonmember bank opens 6 branches and moves 5 next door. A covered community savings association opens 8 branches. It forms 1 qualifying operating subsidiary; a covered community bank forms 4. Each institution moves its head office next door; nobody comments. Applying OCC’s 2026 community-bank rule and FDIC’s 2025 branch proposal, how many changes need each agency's approval?
```

### Number of asks

2 asks

### Gold answer

```text
3 by the OCC and 7 by the FDIC
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 7, expedited or reduced filing procedures): a national bank generally needs an application to establish an operating subsidiary, but a well capitalized and well managed bank may give after-the-fact notice instead when the subsidiary meets the structural and activity requirements, and the rule lets a covered community bank qualify for that. The bank's 4 qualifying subsidiaries need no OCC approval.

Step 2. Source input (Doc 7, expedited or reduced filing procedures): for a Federal savings association the provision is expedited review of an application to establish an operating subsidiary, and the rule adds covered community savings associations to it. An application is still filed, so the association's 1 subsidiary needs OCC approval.

Step 3. Source input (Doc 7, expedited or reduced filing procedures): a covered community savings association need not file an application to establish or relocate a branch if it has published public notice and no person has filed a comment opposing the branch. Nobody comments, so its 8 new branches need no approval.

Step 4. Source input (Doc 7, expedited or reduced filing procedures): relocating a main office or a home office is done by application, for banks and savings associations alike. The bank's head-office move needs OCC approval, and so does the association's: 1 each.

Step 5. Calculation (Doc 7): OCC approvals, the association's subsidiary and the two head offices: 1 + 1 + 1 = 3

Step 6. Source input (Doc 4, statutory requirements and filing procedures): a State nonmember bank needs the FDIC's consent to establish a branch or to move its main office or a branch, and under the proposal it submits a filing to establish a branch or to relocate a branch or its main office. Its 6 new branches each need FDIC approval.

Step 7. Source input (Doc 4, proposed definition of branch relocation): a de minimis change in address, when a branch exchanges one facility for another on contiguous properties or the same block, is neither a branch establishment nor a branch relocation, so the 5 branches moved next door need no filing. The definition speaks of a branch only. The main office moved next door is still a main office relocation and needs FDIC approval: 1 more.

Step 8. Calculation (Doc 4): FDIC approvals, the new branches and the main office: 6 + 1 = 7
```

### Answer components

Component 1

```text
3 by the OCC
```

Component 2

```text
7 by the FDIC
```

### Evidence

Evidence 1: document Doc 7 (fr_2026_04275.txt), proves component 1. 3 by the OCC (local note: operating subsidiaries of banks, L141)

```text
Twelve CFR 5.34(f)(2) permits a national bank that is well capitalized and well managed to provide after-the-fact notice instead of an application if the operating subsidiary meets certain structural and activity requirements.
```

Evidence 2: document Doc 7 (fr_2026_04275.txt), proves component 1. 3 by the OCC (local note: covered community banks added, L142)

```text
The OCC proposed that a national bank qualify for these expedited or reduced filing requirements if it is a covered community bank or is both well capitalized and well managed.
```

Evidence 3: document Doc 7 (fr_2026_04275.txt), proves component 1. 3 by the OCC (local note: operating subsidiaries of savings associations, L145)

```text
Twelve CFR 5.38 provides for expedited review of an application to establish or acquire an operating subsidiary or to perform a new activity in an existing operating subsidiary by a Federal savings association
```

Evidence 4: document Doc 7 (fr_2026_04275.txt), proves component 1. 3 by the OCC (local note: covered community savings associations added, L145)

```text
The OCC proposed to add covered community savings associations to these provisions.
```

Evidence 5: document Doc 7 (fr_2026_04275.txt), proves component 1. 3 by the OCC (local note: branches of savings associations, L112)

```text
provides that an eligible savings association need not file an application to establish or relocate a branch if it has published public notice and no person has filed a comment opposing the branch
```

Evidence 6: document Doc 7 (fr_2026_04275.txt), proves component 1. 3 by the OCC (local note: main and home offices, L113)

```text
Twelve CFR 5.40(c)(4) provides for expedited review of applications to relocate a main office or home office of an eligible bank or eligible savings association, respectively.
```

Evidence 7: document Doc 7 (fr_2026_04275.txt), proves component 1. 3 by the OCC (local note: extension to the new classes, L113)

```text
The OCC proposed adding covered community bank or covered community savings association to each of these provisions referencing an eligible bank or eligible savings association.
```

Evidence 8: document Doc 4 (fr_2025_13568.txt), proves component 2. 7 by the FDIC (local note: statutory requirements, L67)

```text
requires the FDIC's prior written consent for an insured State nonmember bank to establish and operate a new domestic branch or to move its main office or any domestic branch from one location to another.
```

Evidence 9: document Doc 4 (fr_2025_13568.txt), proves component 2. 7 by the FDIC (local note: proposed filing procedures, L186)

```text
Under the proposed rule, a bank would be required to submit a letter filing to the appropriate FDIC office to establish a domestic branch or complete a branch relocation or main office relocation.
```

Evidence 10: document Doc 4 (fr_2025_13568.txt), proves component 2. 7 by the FDIC (local note: proposed Sec. 303.41(b)(1), L546)

```text
For the purposes of this subpart, a de minimis change in address is neither a branch establishment nor a branch relocation.
```

Evidence 11: document Doc 4 (fr_2025_13568.txt), proves component 2. 7 by the FDIC (local note: proposed Sec. 303.41(b)(1)(i), L547)

```text
A de minimis change in address occurs when a branch exchanges one physical facility for another within the same approximate location, such as where:
```

Evidence 12: document Doc 4 (fr_2025_13568.txt), proves component 2. 7 by the FDIC (local note: proposed Sec. 303.41(b)(1)(i)(C), L550)

```text
The facilities are located on contiguous properties or on the same block.
```

### Necessary documents

- Tick Doc 4 (fr_2025_13568.txt), role: Answer component
- Tick Doc 7 (fr_2026_04275.txt), role: Answer component

Leave unticked: Doc 1 (fr_2024_02663.txt), Doc 2 (fr_2024_21560.txt), Doc 3 (fr_2024_22189.txt), Doc 5 (fr_2025_13589.txt), Doc 6 (fr_2026_03818.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Aggregation

Leave unticked: Temporal alignment, Unit normalization, Entity resolution

### Targeted failure modes

#### Failure mode 1

Trap: Wrong jurisdiction or scope

How a careless solver fails: Misapplies a rule or premise

#### Why these are traps (at most 50 words)

```text
Wrong jurisdiction or scope: Doc 7 groups expedited and reduced filings; only a savings association's branches and a bank's qualifying operating subsidiaries need no application. Taking every filing as an application gives OCC 15; swapping the rules gives 6. Doc 4's de minimis rule excludes the main office: FDIC 7.
```

(50 / 50 words.)
