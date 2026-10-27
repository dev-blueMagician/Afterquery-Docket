# aq-03169 q02 hand-over

Generated 2026-10-13 by `python tools/check_questions.py tasks/aq-03169 --handover --q q02` from questions/q02.md. Regenerate it after any edit. It is not a submission.

- Status checked, revision 4, difficulty_target medium, origin claude.
- tested_sha256 d020902e0730964355141dead5c422d48c0e1dd9d4d701792905a190834511c1: question, number of asks, answer, answer type, components, reasoning, evidence, documents, their roles, tags, target and corpus. Targeted failure modes are outside it.
- Local ids and the task page's numbers: D02 = Doc 2, D04 = Doc 4.
- Floor: 0 FAIL, 3 WARN.
  - WARN origin: the form asks you to tick; export takes origin: user only
  - WARN list-contract: the answer lists 5 items; say how many to expect, or ask for one value (form: list contract)
  - WARN revision: more than two revision rounds; replace an ineffective question family or record why new evidence justifies another revision
- Recorded platform Checks: unknown; 0/39 passed in the latest capture. Submission clearance recorded: no. Difficulty readiness and Checks clearance are separate; neither is acceptance.
  - Checks: No platform Checks capture recorded.
- Authorship: origin claude. The form's authorship and AI-use statements are the user's to make; the export sheet takes origin user only.
- Form input JSON: questions/q02.json (input values only).

Paste each block into the form field of the same name, replacing what the field holds. Copy only the text inside each box. On the platform, an edit to the question, answer or necessary documents needs a new difficulty result.

### Question

```text
Of the CMA's potential measures that Deloitte rates High for costs and Low for benefits, which, if any, does Grant Thornton's response say could leave the audit market less concentrated, and which does it warn could reduce or destabilise audit quality? List each group alphabetically.
```

### Number of asks

2 asks

### Gold answer

```text
Big Four break-up (lower concentration), joint audits (lower concentration), non-audit services ban for all large companies (lower concentration), audit-only split (quality risk), NAO-style national auditor (quality risk)
```

### Step-by-step reasoning

```text
Step 1. Source input (Doc 2, summary table of measures in the appendix): Deloitte gives each measure a rating for costs, then benefits, then implementation challenges. The measures rated High for costs and Low for benefits are: reform of mandatory tendering and auditor rotation, prohibiting non-audit services to all large clients and PIEs, splitting UK firms into audit-only and non-audit practices, joint audits, break-up of the largest firms into smaller audit firms, an insurance-based system, and an NAO-style national auditor.
Step 2. Source input (Doc 4, annex of costs and benefits, one numbered row per measure): the row for prohibiting non-audit services to any other large company or PIE lists as a benefit that other firms can grow, "potentially leading to less audit market concentration and more competition". The row for breaking up the largest firms lists "Immediate impact on market concentration".
Step 3. Source input (Doc 4, reply on the market share cap and joint audits): joint audit is common in France, and "This does appear to have created a more dynamic and less concentrated market". The annex row for joint and shared audits says nothing about concentration, so this member comes from the reply and not from the annex.
Step 4. Check (Doc 2 and Doc 4): no other measure in Step 1 is said to cut concentration. The audit-only split leaves "no impact to market concentration"; the rows for the insurance-based system and the NAO-style auditor do not mention concentration. Decoy: of more regular tendering Doc 4 says "Alone, it may not reduce market concentration", so tendering reform is out. Decoy: Doc 4 does say a market share cap would reduce concentration, but Doc 2 rates that measure High for benefits, so it is not in Step 1.
Step 5. Source input (Doc 4, same annex): the costs of the audit-only split continue after a page break and include "Loss of access of some technical specialisms and restricting talent pool, potentially reducing audit quality." The costs of the NAO-style auditor also continue after a page break and include the loss of partners and staff and "likely destabilisation of audit quality, particularly in very large companies".
Step 6. Check (Doc 4): no other measure in Step 1 carries such a warning. Joint audits are credited with better quality, the all-clients prohibition with more investment in audit quality, and the rows for the break-up, tendering reform and the insurance-based system do not mention audit quality. Decoy: Doc 4 notes a fall in audit quality "In spite of an increase in tendering and auditor rotation", which does not blame tendering.
Final answer (Doc 2 and Doc 4): Big Four break-up (lower concentration), joint audits (lower concentration), non-audit services ban for all large companies (lower concentration), audit-only split (quality risk), NAO-style national auditor (quality risk).
```

### Answer components

Component 1

```text
non-audit services ban for all large companies
```

Component 2

```text
Big Four break-up
```

Component 3

```text
joint audits
```

Component 4

```text
audit-only split
```

Component 5

```text
NAO-style national auditor
```

### Evidence

Evidence 1: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 1. non-audit services ban for all large companies (local note: appendix 14.4 table, L423)

```text
Prohibit audit firms from providing non-audit services to all large clients and PIEs
```

Evidence 2: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 1. non-audit services ban for all large companies (local note: appendix 14.4 table, L424)

```text
4.8(b) High Low High 14.5.11 Exec sum and
```

Evidence 3: document Doc 4 (cma_audit_itc_responses_grant_thornton.txt), proves component 1. non-audit services ban for all large companies (local note: Annex 2, row 2, L840)

```text
potentially leading to less audit market concentration and more competition
```

Evidence 4: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 2. Big Four break-up (local note: appendix 14.4 table, L431)

```text
4.27 High Low High !4.5.13 None
```

Evidence 5: document Doc 4 (cma_audit_itc_responses_grant_thornton.txt), proves component 2. Big Four break-up (local note: Annex 2, row 9, L877)

```text
Immediate impact on market concentration
```

Evidence 6: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 3. joint audits (local note: appendix 14.4 table, L429)

```text
Joint audits 4.18(a) High Low Medium 14.5.12 Q23
```

Evidence 7: document Doc 4 (cma_audit_itc_responses_grant_thornton.txt), proves component 3. joint audits (local note: reply to Q19-Q23, para 23.5, L349)

```text
This does appear to have created a more dynamic and less concentrated market
```

Evidence 8: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 4. audit-only split (local note: appendix 14.4 table, L426)

```text
Split UK firms into audit only and non-audit services practices
```

Evidence 9: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 4. audit-only split (local note: appendix 14.4 table, L427)

```text
4.8(c) High Low High 14.5.11 Exec sum and
```

Evidence 10: document Doc 4 (cma_audit_itc_responses_grant_thornton.txt), proves component 4. audit-only split (local note: Annex 2, row 3 continued, L849)

```text
Loss of access of some technical specialisms and restricting talent pool, potentially reducing audit quality.
```

Evidence 11: document Doc 2 (cma_audit_itc_responses_deloitte.txt), proves component 5. NAO-style national auditor (local note: appendix 14.4 table, L435)

```text
style national auditor 4.50 High Low High 14.5.16 None
```

Evidence 12: document Doc 4 (cma_audit_itc_responses_grant_thornton.txt), proves component 5. NAO-style national auditor (local note: Annex 2, row 15 continued, L909)

```text
likely destabilisation of audit quality, particularly in very large companies
```

### Necessary documents

- Tick Doc 2 (cma_audit_itc_responses_deloitte.txt), role: Answer component
- Tick Doc 4 (cma_audit_itc_responses_grant_thornton.txt), role: Answer component

Leave unticked: Doc 1 (cma_audit_itc_responses_bdo.txt), Doc 3 (cma_audit_itc_responses_ey.txt), Doc 5 (cma_audit_itc_responses_hermes.txt), Doc 6 (cma_audit_itc_responses_icaew.txt), Doc 7 (cma_audit_itc_responses_moore_stephens.txt), Doc 8 (cma_audit_itc_responses_nexia_smith_williamson.txt), Doc 9 (cma_audit_itc_responses_standard_life.txt), Doc 10 (cma_audit_itc_responses_uss.txt)

### Reasoning tags

Tick: Cross-document join, Conditional filter, Entity resolution

Leave unticked: Temporal alignment, Unit normalization, Aggregation

### Targeted failure modes

#### Failure mode 1

Trap: Linking across documents

How a careless solver fails: Picks the wrong entity or section

#### Failure mode 2

Trap: Document convention

How a careless solver fails: Wrong members in a list

#### Why these are traps (at most 50 words)

```text
Linking across documents: Doc 4's annex credits the all-clients ban and break-up with less concentration, its reply credits joint audits; either alone gives a partial list. Document convention: the NAO-style auditor's quality cost continues after a page break in the annex; reading only the row's first lines drops that member.
```

(50 / 50 words.)
