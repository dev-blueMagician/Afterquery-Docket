# Docket Writer portable playbook v2.1

This mirrors the local adopted workflow. In a chat-only environment carry packets/actual raw
returns between separate fresh contexts. Run the provided Python tools when file access is
available or use authentic local output. A author self-check is not an independent solve.

This workflow incorporates useful practices from [D:\Docket_new\workflow.md](D:/Docket_new/workflow.md).
The platform guide/form defines valid questions. Our process verifies correctness and measures
difficulty; extra local heuristics must not exclude Guide-compliant mechanisms.
New questions default to `difficulty_target: easy`; Medium/Hard are explicit higher targets.
Historical targetless questions retain their saved Hard target until an editable draft is migrated.

## 1. Intake and check extraction

Copy the template to a named bundle and preserve received originals. Split supplied captures
with `python tools/split_capture.py <capture.md> tasks/<slug>`, then extract with
`python tools/extract_text.py tasks/<slug>`. The splitter persists current warnings/source hashes
in `notes/intake.json` and retains previous capture provenance in its history.

Spot-check every extraction against the original: page/section count, one representative table,
and a footnote or other detail where present. Preserve row/column labels, units, comparatives and
qualifiers. Record what was checked and any disagreement. For plain-text captures, compare
the captured body/metadata and note truncation; matching a capture does not make it complete.
Inspect thin PDF pages visually. Fix extraction defects before relying on the affected inputs.

A supplied complete capture may replace a clipped intake through the splitter's `--force`
option; re-extract afterward. Preserve prior provenance and invalidate all old fingerprints.
Never reconstruct omitted source text from memory.

## 2. Map readable documents and their relationships

The mapper reads all available document text in manageable chunks, including appendices,
tables, footnotes and late passages. If a pass ends early, record exact unread ranges and resume;
do not label headings/search snippets as a full read. Missing originals remain explicit gaps.

Record authors vs named organizations, dates and fiscal periods, editions, aliases, quantities
with units/scales, forecasts vs actuals, deadlines, definitions, amendments, hedge attachment,
exceptions and contradictions, each with locations. The map is navigation, not question ideas.
Its shared-ground section records relationships across documents and repeated evidence. If it
is sparse, look again at forecast/actual pairs, editions, cited rules and changed classifications.

## 3. Find hooks before drafting

The author/caller writes `notes/hooks.md`: source facts that combine into a world fact.
Explore the Guide's full range, including:

- Forecast in one release and actuals in another.
- Proposal deadline plus final effective date or comment count.
- Repeated tables across editions, changed rows and conflicting same-period figures.
- Contract terms and operative amendments in order.
- Mentions versus actions, hedge words versus the claims they qualify.
- Entity/edition matching, ordered answers, late list members, and match then exclude.
- Ordinary cross-document differences, ratios, rankings, counts and date calculations.
- Definitions or exceptions applied to separately reported instances.

Record the involved documents, essential input facts/locations, possible ask and one or two
selected levers. Prefer the Guide's most-effective levers where the evidence supports them;
do not force them onto every hook. Find more viable hooks than finished questions requested,
without imposing an unknown task quota.

A decoy is required for every "which items" question. Wrong-route calculations are required
when claiming a lever that depends on changing the answer, such as rounded-prose comparisons
or skipping an exclusion. Other legitimate hooks may state "not applicable" with a reason.
A remote defeating fact, hidden trap or misleading alternative is not mandatory for every ask.

## 4. Screen lean sketches before full write-up

Draft up to five distinct candidates from neutral shorthand fact notes with source wording out
of view. Then reopen the passages and verify each premise, exact name, period, unit and term.
This promotes original phrasing; it does not change authorship. Keep the required precise terms.

A sketch needs only the exact question, provisional short gold, essential source inputs and
locations, chosen mechanism/levers, source risks, and a screen decision. Full components,
submission reasoning and exhaustive lever records come after promotion.

Optionally save it as `notes/sketches/iNN.md` using the sketch template and run:

```powershell
python tools/docket_agent.py screen tasks/<slug> --idea iNN
```

This read-only screen checks length/answer shape and quoted inputs from two documents. It
requires no full components or reasoning. It does not solve, run a model, prove uniqueness,
verify arithmetic or establish a tier pass. A passed screen makes a sketch eligible for further
work, not ready.

The author performs a cheap factual check and targeted attack: direct whole-answer retrieval,
one-source sufficiency, obvious alternate readings, false premises and applicable lever checks.
Source gaps need impact assessment; they do not automatically stop unrelated drafting.
Ordinary arithmetic, dates, shared IDs, endpoint editions or short valid joins are eligible.
A short successful reasoning path is a difficulty risk to measure, not a Guide violation.

If an authorized current platform draft screen is available, test the strongest sketches before
full write-up, following the actual form/budget. Preserve exact wording, proposed answer,
corpus identity, raw feedback and stage. A draft quick test is preliminary; never transfer it
automatically into a final exact-content tier pass. No platform access leaves that screen pending.

## 5. Promote, solve and check the gold

Promote viable sketches to `questions/qNN.md`, with accurate origin, explicit target and revision.
Write all form fields, components, tagged verbatim evidence and the full source-to-answer path.
Each necessary document must contribute an indispensable input after searching the rest of the
bundle for duplicate/substitute evidence.

Calculate once from the passages, then independently recalculate using a script/calculator or
another derivation. Verify input choice, units, signs and rounding as well as arithmetic. For date
gaps record the elapsed/inclusive/business-day convention and use only a convention supported by
the question/bundle. Never label the author's own calculation as a blind solve.

For lists/counts, verify the complete candidate universe and every exclusion. For selected levers,
record the applicable answer-changing checks. Other lever checks may be explicitly not applicable.
Run `python tools/check_questions.py tasks/<slug> --q qNN`; fix FAILs and explain/fix WARNs.

## 6. Attack the selected mechanism

Reject a demonstrated direct whole-answer lookup, a complete answer from one sufficient source,
a bundle-independent answer, an unsupported premise or a second defensible reading. Finding
inputs by search or an ID is expected and does not by itself disqualify a cross-document question.
Remove vague judgments such as "another trivial route": state the actual violated rule.

Use the applicable attacks, not every attack on every question:

| Mechanism | Check |
| --- | --- |
| All questions | Two-source necessity, direct whole-answer exposure, alternate readings, bundle-only premises, period/units and giveaways |
| Which-items answer | Plausible decoy actually fails; every omitted item fails |
| Exact table vs rounded prose | Recompute with rounded/prose inputs; verify the claimed difference |
| Match then exclude | Omit the exclusion and recompute; confirm it changes the answer |
| Hedge scope | Check which claim/clause the qualifier actually modifies |
| Edition/entity/late member | Verify identity and operative period; search earlier/repeated sources and the final passages |
| Numerical/date answer | Independently recompute and check precision/counting convention |

Historical failed mechanisms affect priority and suggested attacks, not universal eligibility.
After two ineffective revisions of one mechanism, prefer a different hook. After three unproductive
rounds, report tested mechanisms and unresolved avenues rather than an unsupported impossibility claim.

## 7. Freeze final fields and verify independently

Run `python tools/docket_agent.py prepare tasks/<slug> --q qNN`. It freezes form/corpus bytes,
creates solver-1, solver-2 and shortcut document packets plus a question-only closed-book packet,
and adds this run to the shared read guard without evicting other active runs (entries expire
after 12 hours or when their run directory is gone). Reuse only intact snapshots; do not edit packets.

Every final role runs in a fresh context with no writer history/shared memory. Claude blind roles
use supported `omitClaudeMd`; Codex uses `fork_turns: none`. Solvers/auditor receive only the
exact question and their full document packet, never gold, selected IDs, tags or intended traps.
A closed-book worker receives only the question with no usable tools/files.
The independent reviewer receives frozen fields, full corpus, actual returns and floor output.

Require two supported matching answers from distinct solver contexts, a closed-book miss and a
clear audit. Agreement alone is not uniqueness proof. Wrong-lever misses are design evidence,
not replacements for the matches. Preserve all failures and settle defensible alternate answers.
The reviewer recomputes the gold, tests all-bundle document necessity and adjudicates actual
shortcut routes. These final QA procedures remain after the lighter sketch stage.

Known source gaps are assessed for this candidate. If a gap could affect a premise, gold, excluded
item, uniqueness, necessity or shortcut search, readiness is blocked until resolved. If independent
review provides concrete evidence that every named gap is irrelevant to all six, an exact-content
source assessment can permit the candidate to proceed while the corpus remains labelled incomplete.
Invalid/unknown provenance and unavailable necessary/cited source material cannot be waived.

## 8. Record exact-content checks and platform measurement

Save raw returns under the run directory outside document packets. All final records carry
current `rev: N` and the `tested_sha256` from prepare. Structural fields precede terminal free
text. Use authentic returns and the user's local date.

```text
## Blind solve
- DATE | rev: N | solver: A | tested_sha256: HASH | outcome: match | docs: ... | answer: ...
- DATE | rev: N | solver: B | tested_sha256: HASH | outcome: match | docs: ... | answer: ...
- DATE | rev: N | closed-book solve | tested_sha256: HASH | result: misses | answer: ...

## Shortcut audit
- DATE | rev: N | tested_sha256: HASH | verdict: clear | findings: actual searches and shortest route

## Review
- DATE | rev: N | tested_sha256: HASH | verdict: ready | difficulty: easy | findings: evidence and unresolved risks

## Source assessment
- DATE | rev: N | reviewer: ID | tested_sha256: HASH | source_gaps_sha256: GAP_HASH | verdict: unaffected | findings: JSON_OBJECT
```

Source assessment is optional when the corpus has no known gaps. `GAP_HASH` and exact gap labels
come from prepare/report. For gaps, `JSON_OBJECT` maps every exact label to concrete explanations
under `premises`, `gold`, `exclusions`, `uniqueness`, `necessity` and `shortcut`; avoid generic
"unaffected" assertions. The script checks binding/coverage; the reviewer owns the evidence judgment.

Local review `difficulty: easy|medium|hard` is suitability only. A clear attack reports its bounded
search, not proof that every route fails. Status `checked` means locally checked, platform pending.
On any tested-content/source change, increment revision, reset draft and rerun fresh checks.

Record a genuine final platform result in Blind solve:

```text
- DATE | rev: N | platform difficulty check | tested_sha256: HASH | platform_verdict: pass | passed_tier: easy | tiers: EXACT PLATFORM LINE | feedback: EXACT PLATFORM WORDS
```

Use `pass|fail|unknown`; ambiguous or unfinished feedback remains unknown. Low/Easy and High/Hard
are label aliases, not pass thresholds. Counts show execution only. Preserve the full raw response.
An explicit earlier-tier pass may coexist with later-tier failure; report the achieved tier exactly.
Status ready additionally requires a current-fingerprint explicit pass at/above the target and
all final quality checks. Draft screens, local solves and script suites never establish that result.

## 9. Style and set review

Read question/reasoning aloud for clarity; remove stock wording, unnecessary setup and copied
syntax. Preserve exact technical terms, periods and verbatim evidence. Keep answers bare and
checkable. Current platform form/guide limits govern; the older external workflow's trial details
and added writing kit are not treated as new official requirements.

For multiple questions, compare their actual answer paths, not just phrasing. Check duplicate
facts, shared answer paths, sibling hints, reciprocal giveaways and wording reuse. Vary levers,
document pairs and reasoning tags where evidence allows; diversity is not a quota or a reason to
reject the best single question. Record set decisions before hand-over.

Reuse a measured question's mechanism, not its sentence frame: the form's blocking "Original
question" check compares a saved question with other tasks' questions, and a draft copying a
measured pass's frame almost word for word was flagged in local review as a near-copy risk.
It happened twice (aq-01322 q01, aq-01333 q01). Before freezing, compare the question's word tokens
with the earlier questions you have; restructure when the overlap is above about 0.4, a shared run
reaches 6 or more words, or the closing sentence repeats one already used on the bundle.

## 10. Hand-over, feedback and state

`python tools/docket_agent.py report tasks/<slug> --q qNN` reports evidence read-only.
`python tools/check_questions.py tasks/<slug> --export` writes ready user-origin sheets from checked
fields. Other origins remain accurate and their export restriction is reported. A sheet is not
a submission. Freeze the entire question file on confirmed submission/acceptance; later findings
and platform status observations go into `notes/feedback-qNN.md`.

Keep verdicts, Coach explanation and raw traces separate when they disagree. Feedback changes
the actual failed dependency or lever rather than automatically requiring a more complicated
question. Update scoped lessons from measured results. Checkpoints under 4,000 characters record
target, phase, read coverage/gaps, hook families, sketch decisions, states and next action.

# Portable acceptance gate

The current platform form/guide and `instruction.md` govern quality,
with the newer-guide summary and
the captured platform quality checks. this playbook
defines the adopted staged workflow. New default target is Easy.

The sketch stage checks only essential facts and obvious faults. Full evidence/components and
independent verification follow promotion. A Guide-compliant ordinary calculation, date gap,
ranking, edition choice or identifier join is eligible; simplicity alone is not a rejection rule.
The script checks mechanical records, not independence, uniqueness or platform authenticity.

| Check | Pass needs | Evidence |
| --- | --- | --- |
| Q1 Bundle only | Premises/inputs supported by bundle, ordinary arithmetic/word meanings only; closed-book misses | Quotes and independent closed-book return |
| Q2 Necessary documents | At least two indispensable sources after all-bundle substitution search; no complete one-source answer | Removal/substitution tests, including rounded figures taken at face value (the platform's removal test counts an approximation that lands on the gold) |
| Q3 Reasoning beyond direct lookup | Search finds inputs rather than the whole answer; no copied question passage | Actual retrieval route |
| Q4 One answer | Independent gold recomputation, supported matching solves, alternatives refuted | Fresh returns and reviewer evidence |
| Q5 Short/checkable | Required answer shape/units, length, list order/count/empty case as applicable | Current form and floor |
| Q6 Required reasoning | At least two actual reasoning tags; arithmetic/comparison/counting/ranking/application qualifies | Source-to-answer derivation |
| Q7 Self-contained | World entities described; no filenames/pages/local IDs in question | Question and floor |
| Q8 No giveaway | No answer part or semantic hint | Floor and reviewer |
| Q9 Exact scope | True premises, exact period/fiscal convention, line item, units, direction and precision | Input variants and recalculation |
| Q10 Readable shape | Current form 8-80 words, aim concise; at most two parallel asks; no rulebook/judgment scale | Current quality checks |
| Q11 Applicable lever works | Which-items decoy fails; all membership exclusions checked; rounding/exclusion counterfactuals only when those levers are claimed | Targeted attacks; not-applicable acceptable otherwise |
| Q12 No manufactured failure | No undefined term, unsupported inference or format trap; missing-item comparison labels handled | Reviewer and alternatives |
| Q13 Measured target | Genuine final exact-content pass at/above Easy/Medium/Hard target | Platform verdict and raw tier line |
| Q14 Components/evidence | 1-10 answer pieces; asks/numbers covered; necessary sources quoted; tagged contiguous evidence supports the component/input | Floor and recomputation |

## Final readiness

For new targeted questions:
- No floor FAIL; remaining WARNs fixed or explained.
- Two supported match records from distinct fresh solver IDs, a closed-book miss, clear audit,
  and independent ready review with target-suitable difficulty; all current revision/fingerprint.
- Gaps that could affect this candidate are resolved. Known irrelevant gaps require a substantive
  independent Source assessment naming all exact gap labels and matching submission/gap hashes.
  Missing necessary/cited material and unknown/invalid provenance remain blocking. A permitted
  candidate does not turn the corpus into a complete one.
- Explicit final platform pass at/above selected target, matching tested content and observed tier
  line, with verbatim feedback and no target/lower-tier contradiction.
- Authorship and remaining platform-only quality checks reported separately.

`checked` means locally checked, platform pending. Early draft quick tests never transfer
automatically to final readiness. Changed source/form fields invalidate records even if a revision
bump was missed. Historical targetless questions keep Hard/maximum compatibility until migrated.

## Difficulty diagnostics

Historical D1-D7 are optional risk prompts, not a required seven-part difficulty score:
bundle-specific deciding facts; direct answer exposure; plausible wrong readings; location/search
of deciding evidence; explicit verifiability; plain wording; actual contribution of a chosen lever.

Use them where relevant. A decoy/wrong route is not compulsory for an ordinary date or arithmetic
ask. Finding needed inputs quickly or following a shared ID can be valid reasoning. Reject a
demonstrated Guide violation; prioritize candidates from measured failure/success evidence.

## Set and external checks

Before handing over a set, check duplicate answer paths, sibling hints, reciprocal giveaways,
wording reuse and opportunities to vary levers/doc pairs. Diversity is a preference where possible,
not a requirement for an individual question.

Unseen restricted names, cross-task originality/duplicates, platform token window and uncaptured
current AI-use terms remain external. Preserve accurate authorship and current user-only export.
A tier pass does not establish submission acceptance.
