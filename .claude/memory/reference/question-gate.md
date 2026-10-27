# Docket question gate v3: platform validation

The current platform form/guide and [instruction.md](../../../instruction.md) govern quality,
with [the newer-guide note](../docket-platform-guide-newer-than-instruction.md), the guide's sections
4-7 of 2026-10-15/16 ([platform-guide-2026-10-16.md](platform-guide-2026-10-16.md), including its
send-back reasons) and [platform quality checks](platform-quality-checks.md). [WORKFLOW.md](../../../WORKFLOW.md)
defines the adopted staged workflow. New work targets Hard (2026-10-14), or the lowest tier the user
names as open; Hard design follows [hard-playbook.md](hard-playbook.md).

The sketch stage checks only essential facts and obvious faults. Full evidence/components,
author arithmetic verification and one mechanical preflight/handover follow promotion. The platform
handles validation; local model diagnostics are optional only on explicit request or for a concrete
unresolved issue. A Guide-compliant ordinary calculation, date gap,
ranking, edition choice or identifier join is eligible; simplicity alone is not a rejection rule.
The script checks mechanical records, not independence, uniqueness or platform authenticity.
The [39-item checklist](platform-quality-checks.md) distinguishes structural/heuristic coverage,
author/source checks and platform/admin outcomes. Parse answer items independently of components;
ambiguous separators need review, never an assumed pass or an extra model job.

| Check | Pass needs | Evidence |
| --- | --- | --- |
| Q1 Bundle only | Premises/inputs supported by bundle, ordinary arithmetic/word meanings only | Source quotes and platform validation |
| Q2 Necessary documents | At least two indispensable sources after all-bundle substitution search; no complete one-source answer; each ticked document supplies its own gold component or an answer-changing exclusion, not only a definition or label a reader would assume without it (aq-02501: document check "A marked document may not be needed", then reviewer "Only document 3 is necessary"; a reviewer note does not cure it) | Author dependency analysis (removal test: which gold component becomes unreachable) and platform Document check; local removal probes are optional diagnostics |
| Q3 Reasoning beyond direct lookup | Search finds inputs rather than the whole answer; no copied question passage | Actual retrieval route |
| Q4 One answer | Gold recomputation and alternatives refuted; every printed figure the question's words fit on a loose reading fails a condition the question states, not only one the documents reveal (the form blocks it as "too vague" when both its solvers take it: [form block](../docket-form-vague-block.md)) | Author calculation/source evidence and platform validation |
| Q5 Short/checkable | Required answer shape/units, length, list order/count/empty case as applicable | Current form and floor |
| Q6 Required reasoning | At least two actual reasoning tags; arithmetic/comparison/counting/ranking/application qualifies; every number in a step is printed in digits in a document the step cites (near its start), or is the step's exact "=" result, or repeats an earlier step's string in a step citing two or more documents, so the form shows no "Doc N doesn't mention" line except an expected false alarm (a quoted figure the document states only in words or deep), named with the hand-over (user, 2026-10-09) | Cited source inputs -> explicit calculation -> derived result (WORKFLOW section 5); computed outputs need not be printed; floor form-numbers check, then the form after pasting |
| Q7 Self-contained | World entities described; no filenames/pages/local IDs in question | Question and floor |
| Q8 No giveaway | No answer part or semantic hint | Floor, author wording check and platform validation |
| Q9 Exact scope | True premises, exact period/fiscal convention, line item, units, direction and precision | Input variants and recalculation |
| Q10 Readable shape | Current form 8-80 words, aim concise; at most two parallel asks; no rulebook/judgment scale | Current quality checks |
| Q11 Applicable lever works | Which-items decoy fails; all membership exclusions checked; rounding/exclusion counterfactuals only when those levers are claimed | Targeted attacks; not-applicable acceptable otherwise |
| Q12 No manufactured failure | No undefined term, unsupported inference or format trap; missing-item comparison labels handled | Source evidence and alternatives |
| Q13 Measured target | Genuine final exact-content pass at/above Easy/Medium/Hard target | Platform verdict and raw tier line |
| Q14 Components/evidence | 1-10 answer pieces; asks/numbers covered; necessary sources quoted; tagged contiguous evidence supports the component/input; non-component documents carry the form's role | Floor and recomputation |
| Q15 Targeted failure modes | 1-3 traps the question really sets, each from the form's list and used once, whose platform definition fits the actual wrong route (Submit checks this since 2026-10-09), with a cause from its list; one shared "Why these are traps" reason of at most 50 words (form of 2026-10-08) naming Doc N and the passage, the exact wrong answer and why the gold avoids it; each wrong answer recomputed in Lever checks; none the wording already rules out | Floor (structure, lists, words) and author source verification (truth of each claim) |

## Final readiness

Before full write-up, record the sketch's competing answer -> wording condition and each
necessary source -> unique input -> substitute search. Recheck the dependency after clarifying;
these author checks screen design defects early and do not establish a platform pass.

For new targeted questions:

- No floor FAIL; remaining WARNs fixed or explained.
- Arithmetic/date verification and complete form fields, including Targeted failure modes.
- Gaps that could affect this candidate are resolved. Known irrelevant gaps require a substantive
  candidate-specific Source assessment by the author or supplied platform evidence, naming all exact
  gap labels and matching submission/gap hashes. Independent model review is not required.
  Missing necessary/cited material and unknown/invalid provenance remain blocking. A permitted
  candidate does not turn the corpus into a complete one.
- Explicit final platform pass at/above selected target, matching tested content and observed tier
  line, with verbatim feedback and no target/lower-tier contradiction.
- Hand-over from `check_questions.py --handover`: every form field in the form's order, Doc N numbers.
- Authorship and remaining platform-only quality checks reported separately.

`checked` means mechanical preflight done, platform pending. `ready` requires the clean floor plus
an exact-content recorded platform pass at/above target. Use `## Platform validation`; legacy platform
records under `## Blind solve` remain readable. Early draft quick tests never transfer
automatically to final readiness. Changed source/form fields invalidate records even if a revision
bump was missed. Historical targetless questions keep Hard/maximum compatibility until migrated.

Report platform Checks separately from difficulty readiness. `record-checks` accepts a supplied
capture only with an explicitly verified prepared revision/fingerprint; never infer this binding
from the task name or saved time. All 39 outcomes/currentness appear in report/handover. Recorded
submission clearance needs current blocking results and no explicit footer blocker; missing or
unknown blocking results and stale/reload warnings prevent clearance. Advisory warning/retry
states remain advisory. Own-words outcomes belong to the admin, including an explicitly nonblocking
reasoning-review state; preserve actual origin. Neither Checks clearance nor `ready` means accepted.

## Optional diagnostics

Do not automatically run local solves, audits, closed-book checks, removal probes or independent
review. Use only a diagnostic that an explicit request or concrete unresolved issue warrants.
`prepare` freezes fields and one corpus copy; `prepare --local-checks` opts into isolated packets
and scope binding. Follow the fresh-context/no-answer-leakage rules in WORKFLOW.md and role prompts.
Never simulate platform difficulty, predict tier suitability or treat local misses as tier evidence.

Missing or stale local records remain historical; they do not require replacement solves. Preserve
current adverse returns and resolve their actual source/interpretation finding. If a current adverse
diagnostic is adjudicated without changing the frozen content, an optional `## Local resolution` record
can cite the concrete source/platform evidence:

```text
- DATE | rev: N | tested_sha256: HASH | assessor: ID | issue: EXACT_DIAGNOSTIC_LABEL | verdict: resolved | findings: SOURCE_OR_PLATFORM_ADJUDICATION
```

Use the exact label reported by the checker (for example, `blind: ambiguous` or
`shortcut audit: shortcut`). A resolution preserves the adverse return; it is not a new solve or platform pass.

A decoy/wrong route is not compulsory for an ordinary date or arithmetic
ask. Finding needed inputs quickly or following a shared ID can be valid reasoning. Reject a
demonstrated Guide violation; prioritize candidates from measured failure/success evidence.

## Set and external checks

Before handing over a set, check duplicate answer paths, sibling hints, reciprocal giveaways,
wording reuse and opportunities to vary levers/doc pairs. Diversity is a preference where possible,
not a requirement for an individual question.

Unseen restricted names, cross-task originality/duplicates, platform token window and uncaptured
current AI-use terms remain external. Preserve accurate authorship and current user-only export.
A tier pass does not establish submission acceptance.
