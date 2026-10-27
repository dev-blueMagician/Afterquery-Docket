# Docket authoring workflow v3.1: early design checks, platform validation

This workflow incorporates useful practices from [D:\Docket_new\workflow.md](D:/Docket_new/workflow.md).
The platform guide/form defines valid questions and the platform validates them. Since
2026-10-14 the user's bundles have Easy and Medium full, so the check starts at the High model
and new questions use `difficulty_target: hard` (the lowest tier the user names as open, if lower).
Design by [hard-playbook.md](.claude/memory/reference/hard-playbook.md), the current rulebook; it
supersedes the dated case law in this file and in the frozen memory notes where they differ.
The local path is author arithmetic verification, the strong-solver screen for a Hard target
(section 4), one mechanical preflight and a complete handover. No other local model solve, audit,
closed-book check, removal probe or reviewer run is mandatory. Run an optional diagnostic only on
explicit request or for a concrete unresolved issue; do not simulate platform tiers.
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

## 2. Reuse source work and map the needed relationships

Resume from the existing map and verified passages when recorded source/extraction hashes match.
Changed inputs invalidate their mapped facts and dependent claims; refresh those sections first.
For an unmapped bundle, locate promising relationships, read their actual passages with context,
and expand into tables, notes or late passages as the candidate requires. Search the entire bundle
for duplicate/substitute inputs and direct answers. Search coverage is not full reading: record
read/unread ranges and missing originals honestly. Lists/counts still need the complete relevant
candidate universe; needed or unresolved gaps block the affected candidate. Do not repeat a full
bundle read for a wording edit. A mapper is optional when existing navigation is sufficient.
Before recording that a text is silent on something, search it with a pattern that can match at the
start of a paragraph, and include recitals, preambles and footnotes: a context pattern such as
`.{150}word` skips a paragraph that opens with the word (aq-03736: recital 18 announced an exclusion
the caller had recorded as dropped without a word, which made one sketch a one-document answer).

Reuse measured results the same way. When the same source hashes, or the same document family,
already have platform captures, read those before the sources: run `tools/verdict_summary.py` on
each, record every wrong attempt's committed answer and the step where it left the gold in
`notes/hooks.md`, and design first from a miss that recurs, so that it decides every counted cell
rather than one (aq-02749 q02: sixteen designs below Medium on the same bytes, then Medium from the
one miss the earlier runs showed). A family those captures show the easier solver handling stays
closed unless the dependency changes; adding cells of the same kind does not change it.

Record authors vs named organizations, dates and fiscal periods, editions, aliases, quantities
with units/scales, forecasts vs actuals, deadlines, definitions, amendments, hedge attachment,
exceptions and contradictions, each with locations. The map is navigation, not question ideas.
Its shared-ground section records relationships across documents and repeated evidence. If it
is sparse, look again at forecast/actual pairs, editions, cited rules and changed classifications.

## 3. Find hooks before drafting

Mine the bundle first (2026-10-17):

```powershell
python tools/docket_agent.py mine tasks/<slug>
```

It writes `notes/mine.md`, the guide's "compare every quote of the same passage across documents, every
spelling of each name, each figure against its earlier versions, and each summary against the rest of
the document" done mechanically over `text/`: shared passages with a word or figure changed, one rule
stated in two documents' own words (an exception in one only), restatement and definition-change
statements, quarters printed only cumulatively, row labels printed with different values, one thing
under two names, rounded prose figures, table notes, stated counts and summary-only figures, each with
`text/Dnn.txt` line numbers. It runs no model and proposes nothing; read each candidate's passages
before it becomes a hook. Rerun it after any re-extraction (its header carries the corpus hash).

The author/caller writes `notes/hooks.md`: source facts that combine into a world fact.
Start with a precise numerical gold derived across at least two indispensable documents, the
user's preferred shape (2026-10-08). Choose the metric, scope, units and supported precision first;
ordinary short calculations qualify. Use another answer shape when the bundle supports it better.
Before settling on a list with one hard-to-find member, check whether its members carry counts or amounts
that sum against a figure one document prints for the visible members; if they do, the total is the first
sketch (aq-03993 q02, 2026-10-13: the list measured "Between levels" at Medium 4/7, the total Medium 2/6).
Explore the Guide's full range, including:

- Forecast in one release and actuals in another.
- Proposal deadline plus final effective date or comment count.
- Repeated tables across editions, changed rows and conflicting same-period figures.
- Contract terms and operative amendments in order.
- Mentions versus actions, hedge words versus the claims they qualify.
- Entity/edition matching, ordered answers, late list members, and match then exclude.
- Ordinary cross-document differences, ratios, rankings, counts and date calculations.
- Definitions or exceptions applied to separately reported instances.
- One organisation's results quoted by two documents for different periods (the first half in one,
  the full year in the other): the remainder that neither prints. In bundles of parties' submissions
  on one paper this was the only cross-document derived figure (aq-03120), so look for it first:
  list every third party that two or more documents quote with figures, and compare the periods.

Record the involved documents, essential input facts/locations, possible ask and one or two
selected levers. Prefer the Guide's most-effective levers where the evidence supports them;
do not force them onto every hook. For a Hard target a hook is a path that carries two or three
levers, each with its own wrong answer, over three dependent steps ([playbook](.claude/memory/reference/hard-playbook.md)
section 4; guide of 2026-10-16: "One lever usually lands Easy; two together land Medium or Hard"). Keep at most two active sketches for the next question by
default; explore another relationship only when needed, without an exhaustive hook quota.

A decoy is required for every "which items" question. Wrong-route calculations are required
when claiming a lever that depends on changing the answer, such as rounded-prose comparisons
or skipping an exclusion. Other legitimate hooks may state "not applicable" with a reason.
A remote defeating fact, hidden trap or misleading alternative is not mandatory for every ask.

## 4. Screen lean sketches before full write-up

Draft at most two distinct candidates from neutral shorthand fact notes with source wording out
of view. Then reopen the passages and verify each premise, exact name, period, unit and term.
This promotes original phrasing; it does not change authorship. Keep the required precise terms.

A sketch needs the exact question, provisional short gold, essential quotes/locations, selected
mechanism, source risks and a decision. Before promotion record two concise author checks:

- Ambiguity: each plausible competing answer/input -> the condition in the question it fails,
  with a source location. Use concrete population, metric, period, comparison direction and units;
  avoid undefined ties such as "same basis". If no alternative was found, record search coverage.
- Necessity: each required document -> its unique input -> substitutes searched -> what remains
  unknowable or changes without it. Check repeated tables, year-to-date reconstruction, rounded
  summaries and inferred dates. A document merely containing a decoy is not necessary when removing
  it also removes that decoy. Nor is a document that only defines or labels the asked population when
  a reader would assume the same set without it (aq-02501: a "less than honorable" list equal to every
  characterization but honorable; reviewer: "Only document 3 is necessary"). Removal test: delete the
  document and name the gold component that becomes unreachable, not merely unconfirmed; each ticked
  document supplies its own gold component or an exclusion that changes the answer. If the platform's
  document check says a marked document may not be needed, repair that dependency before submitting:
  the page's reviewer note unblocks Submit but did not survive review.
  Run the removal test as delete-and-guess, and write its result in the sketch: with the document gone,
  what would a solver answer from the rest, and from what it knows of a well-reported law? If that guess
  is the gold, the document is not needed, however many steps the design has. Two shapes failed it on
  aq-03736: a gold equal to the whole set one document lists (the proposal's two optional guidance items;
  the adopted text only confirmed that both became duties: "Your answer can still be reached without
  document 3", Low 2/5), and an input that is a headline figure of a public law (thresholds and phase-in
  dates were recalled exactly, closed-book). Redo the test whenever the ask is narrowed: that gold was
  safe while the ask covered five discretionary steps and unsafe once it was cut to guidance.
  If fewer than two indispensable documents remain, redesign the hook.

Check both together after a wording repair: clarification must not supply the fact another
document was meant to contribute. Recompute relevant alternate inputs in the same arithmetic
check. Legitimate readings must agree at the requested precision; a substitute route reaching the
gold defeats the claimed dependency. Use only precision justified by the inputs; if clarity and
necessity cannot both hold, choose another quantity. Do not weaken a defining condition to chase
a tier. These are author/source checks, not new solver jobs or mechanically proven semantics.

Full components, submission reasoning and required failure modes follow promotion of one sketch.
Reuse sketch evidence/calculations in the full write-up instead of repeating the investigation.

Optionally save it as `notes/sketches/iNN.md` using the sketch template and run:

```powershell
python tools/docket_agent.py screen tasks/<slug> --idea iNN
```

This read-only screen checks length/answer shape and quoted inputs from two documents. It
requires no full components or reasoning. It does not solve, run a model, prove uniqueness,
verify arithmetic or establish a tier pass. For a Hard target it also reads the sketch's
`## Lever stack` (template `notes/sketches/i00.md`): it FAILs a trap or settling quote not found in
its document and WARNs on fewer than two levers, a lever name outside the guide's table, two levers
whose misses give the same answer (or the gold), fewer than three numbered steps, no decoy, and a rare
word of the question (printed in at most a third of the documents) that also sits in a settling
passage. Its sentence notes include the guide's (2026-10-15/16): hint words ("actually", "originally"),
a gold carrying words or a bracket the question does not ask for, a selector, a literal reading of
"the latest report", and the 20-45 word aim. A passed screen makes a sketch eligible for further
work, not ready. It also warns when an input quote states a number of 10 or more only in words, or
quotes digits the document prints first past character 20,000. The form's reasoning number check
reads digits near the start of a document only, so an operand like that draws "Doc N doesn't mention
X" on the form whatever the wording (aq-02505 q01: "One hundred and seven entities"). Prefer another
input; if the design needs it, keep the passage as evidence and say with the hand-over that the form
will show this false alarm.

The screen also warns when a period word in the question ("half-year", "first-half", "full-year",
"interim", "year-end") is printed in a document as a reporting label ("half-year results"). Check
every noun phrase that names the asked period or population the same way, by searching the bundle
for it: if the documents use it as a label for a narrower or different item, a strong reader can take
that item, and the platform scores it as a second answer (aq-03120: "its last completed financial
half-year" gave Low 0/5 · Medium 2/5 and "Answer not supported"; a dating event called "first-half
results" was blocked twice by "One defensible answer"). Name the period by its structure instead
("the half of its financial year that last ended before ..."), and never date a period by an event
whose name carries the other period's label.

### Strong-solver screen (Hard target)

With only Hard open the platform's first solver is its strongest. The task page (2026-10-16) runs
quick tests "against the high model", and a quick test "never sets a tier": quick-test survivors still
went Too easy at High (ledger rows 4, 17, 21, 25, 34). On 2026-10-14 every one of 14 unscreened runs
failed, 13 of them "High 3/3"; from 2026-10-14 to 16 all eight screened runs failed too, and 138 of 138
local solves were right. Before offering a Hard sketch for a quick test or a run:

```powershell
python tools/docket_agent.py packet tasks/<slug> --idea iNN
```

The packet holds the exact sentence and the documents only, and the read guard is bound. Launch
three `blind-solver` agents, each fresh, each given only the workspace root, the packet path and the
exact question (never the gold, notes, documents chosen or traps). Judge each answer against the gold,
read every miss's own path, and record:

```powershell
python tools/docket_agent.py record-screen tasks/<slug> --idea iNN --results right,wrong,right --note "the step each miss took"
```

- Three right: still hand it over, ranked last and marked "local 3/3: likely Too easy at High". The
  screen ranks; the user decides what to quick-test or run (aq-05049: four 3/3 sketches withheld drew
  "you even didn't give me any questions"). Do not reword it or re-screen it to fish for a miss; for
  the next round, look for a different hook. The floor WARNs on the sentence.
- One or two right: rank it first if each miss came from the intended deciding step. A miss from a
  second reading or an unclear term is a wording defect: fix it, then make a new packet and screen.
- None right: check the gold and the readings first. Since the run page of 2026-10-18 the High check
  passes even when every attempt misses ("Ready when both get it wrong at least once, even if every
  attempt is wrong"), so an all-wrong screen is a fairness question, not a difficulty one.
- A contaminated or cut-off solve does not count; replace it with another fresh solve.

The record binds to the sentence's words and the corpus bytes, so a survivor carried word for word
into a question file keeps it. Any change to the sentence needs a new screen. The screen ranks and
predicts no tier: a miss is not a pass, and a 3/3 is not a platform result. Add a row to `notes/hard-runs.md` for every screen.

The author performs a cheap factual check and targeted attack: direct whole-answer retrieval,
one-source sufficiency, obvious alternate readings, false premises and applicable lever checks.
Source gaps need impact assessment; they do not automatically stop unrelated drafting.
Ordinary arithmetic, dates, shared IDs, endpoint editions or short valid joins are eligible.
A short successful reasoning path is a difficulty risk to measure, not a Guide violation.

If an authorized current platform draft screen is available, test the strongest sketch at the
earliest stage the actual form permits, completing every field that check requires. Do not assume
a question-only draft can run, omit required failure modes, or spend runs on a wording ladder.
Defer optional narrative until the issue is settled. Preserve exact wording, proposed answer,
corpus identity, raw feedback and stage. A draft quick test is preliminary; never transfer it
automatically into a final exact-content tier pass. No platform access leaves that screen pending.

## 5. Promote, solve and check the gold

Promote viable sketches to `questions/qNN.md`, with accurate origin, explicit target and revision.
Write all form fields, components, tagged verbatim evidence and the full source-to-answer path.
Each necessary document must contribute an indispensable input after searching the rest of the
bundle for duplicate/substitute evidence. A document that is not an answer component gets its form
role ("Used to identify", or "Exclusion / condition source" with the reviewer note) in
`## Necessary documents`; documents carrying the same fact may be grouped with "or".

For Step-by-Step Reasoning, make the origin of every numerical value explicit:

- **Source input:** cite Doc N and its table/row, note or passage; name the metric, period, scope,
  value and units. Keep verbatim evidence quotes to what the source actually states.
- **Calculation:** identify the input steps/locations and show the arithmetic with substituted
  values, units and derived result. Link an intermediate result to its earlier calculation;
  never write "Doc N states X" for a value that was calculated. The operands and their relationship
  must be supported; arithmetic alone does not justify combining unrelated figures.
- **Final answer:** show the last equation and requested rounding. Retain intermediate precision
  and round once at the end unless the question requires otherwise. For percentages identify the
  numerator/denominator and label multiplication by 100 as conversion to percent, not a source fact.

Illustrative format only (not evidence for a real candidate):

```text
Step 1. Source input (Doc 1, pack-size table): 5 units per pack.
Step 2. Source input (Doc 2, order table): 10 packs of that size.
Step 3. Calculation from Steps 1 and 2: 5 units/pack × 10 packs = 50 units (derived total).
```

Attach the source quotes for operands and scope to the numerical answer component. A supported
calculated result need not appear verbatim in any document. Reuse the already verified calculation;
this presentation rule adds no local model check and does not establish a platform pass.

The form reads every number in every step and flags, in orange under the reasoning box, any it
cannot place: "Step N: Doc X doesn't mention Y." Such lines used to reveal real reasoning mistakes,
which must never reach the user again (2026-10-09), so the floor emulates the check
(`tools/form_numbers.py`, from the recorded screenshots) and FAILs each miss a rewording could fix,
with its cause. A number passes when a document named in the step's head (before the
first colon) prints it in digits within about the first 20,000 characters; when it is the exact result
straight after "=" of the step's first bare calculation (no unit words inside the expression, no
brackets; a plain result must be exact, while a result written with "%" may be rounded, as in
"109 / 78 = 139.7%"); or, in a step citing two or more documents, when an earlier step wrote the
identical string. So:

- Cite each document as "Doc N" ("Calculation (Doc 2 and Doc 6):"), never a range; a step that uses
  an earlier result cites every contributing document, because a one-document step accepts none.
- Write each source figure in digits exactly as its document prints it, once, and reuse that string.
  Never restate a result ("or 10.1%"), type a reused result as a percentage, or convert units alone.
- A figure the cited document states only in words or deep in a long document cannot pass by any
  wording. Quoted as evidence from that document, it is an expected false alarm (a WARN naming the
  document and character position): say with the hand-over that the form will show it. Prefer digit
  inputs at sketch time (section 4).

The emulation can miss a flag (aq-01321 q02's period-labelled sum), so read the form after pasting.

The form also requires 1-3 Targeted failure modes (2026-10-07). Write them in
`## Targeted failure modes` once the lever checks prove each trap. Each mode gives one trap from the
form's list (each trap at most once) and one "How a careless solver fails" cause. Since 2026-10-08 the
form has one shared "Why these are traps" box for all modes, at most 50 words (its counter matches
whitespace-separated words; Submit is blocked above 50): where each trap sits (Doc N and the passage),
the exact wrong answer, and why the gold avoids it. Declare only traps the question really sets, never a
slip its wording already rules out. Recompute each wrong answer in Lever checks. Failure modes sit
outside the fingerprint, like Lever checks; the author verifies their factual claims.

Calculate once from the passages, then independently recalculate using a script/calculator or
another derivation. Verify input choice, units, signs and rounding as well as arithmetic. For date
gaps record the elapsed/inclusive/business-day convention and use only a convention supported by
the question/bundle. Never label the author's own calculation as a blind solve.

For lists/counts, verify the complete candidate universe and every exclusion. For selected levers,
record the applicable answer-changing checks. Other lever checks may be explicitly not applicable.
Count list items from the answer independently of evidence components. Grouping several items
inside one component does not reduce the list size. The floor's separator parsing is a heuristic;
resolve ambiguous segmentation from the actual answer, preserving commas in names, dates and numbers.
Combine the mechanical check with the handover at the final phase boundary (section 10).

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

Repairs after a verdict follow [hard-playbook.md](.claude/memory/reference/hard-playbook.md)
("After a verdict"). The repair order measured against the Low and Medium solvers on
2026-10-10 to 2026-10-13 is kept verbatim in
[workflow-repair-order-2026-10-14.md](.claude/memory/archive/workflow-repair-order-2026-10-14.md),
for a bundle where the user names Easy or Medium as open.

Historical failed mechanisms affect priority and suggested attacks, not universal eligibility.
Make one focused repair for a distinct observed failure. If that same mechanism fails again,
replace the hook instead of trying synonyms or weaker definitions. A separate new issue may need
its own repair; identify it. After three unproductive sketch rounds, report the supported options
and unresolved avenues instead of inventing difficulty or claiming the bundle is impossible.

## 7. Freeze final fields and assess source gaps

Run `python tools/docket_agent.py prepare tasks/<slug> --q qNN`. It freezes the form fields and
one corpus copy in a platform snapshot. It does not create solver packets, bind the read guard or
launch models. Reuse only intact snapshots. Keep the full form/source fingerprint for exact-content
platform records; a changed hash makes older results historical, not a reason to rerun local models.

Known source gaps are assessed for this candidate. If a gap could affect a premise, gold, excluded
item, uniqueness, necessity or shortcut search, readiness is blocked until resolved. The author or
supplied platform evidence may establish concretely that each known gap is irrelevant to all six.
Record that candidate-specific source assessment with the snapshot/gap hashes; it permits the
candidate to proceed while the corpus remains labelled incomplete. No independent model is mandatory.
Invalid/unknown provenance and unavailable necessary/cited source material cannot be waived.

## 8. Record platform results and optional diagnostics

Save actual platform returns under the run directory. All validation records carry
current `rev: N` and the `tested_sha256` from prepare. Structural fields precede terminal free
text. Use authentic returns and the user's local date.

```text
## Platform validation
- DATE | rev: N | platform difficulty check | tested_sha256: HASH | platform_verdict: pass | passed_tier: easy | tiers: EXACT PLATFORM LINE | feedback: EXACT PLATFORM WORDS

## Source assessment
- DATE | rev: N | assessor: AUTHOR_OR_EVIDENCE_ID | tested_sha256: HASH | source_gaps_sha256: GAP_HASH | verdict: unaffected | findings: JSON_OBJECT
```

Source assessment is optional when the corpus has no known gaps. `GAP_HASH` and exact gap labels
come from prepare/report. For gaps, `JSON_OBJECT` maps every exact label to concrete explanations
under `premises`, `gold`, `exclusions`, `uniqueness`, `necessity` and `shortcut`; avoid generic
"unaffected" assertions. The script checks binding/coverage; the author owns the evidence judgment.
Identify the actual assessor or supplied platform evidence; legacy `reviewer`/`author` identity
fields remain readable without asserting independent model review. Legacy platform records in
`## Blind solve` remain readable.

Use `pass|fail|unknown`; ambiguous or unfinished feedback remains unknown. Low/Easy and High/Hard
are label aliases, not pass thresholds. Counts show execution only. Preserve the full raw response.
An explicit earlier-tier pass may coexist with later-tier failure; report the achieved tier exactly.
Status `checked` means mechanical preflight done, platform pending. Status `ready` requires a clean
floor and a current-fingerprint explicit platform pass at/above the target. Draft screens, optional
local diagnostics and script suites never establish that result. On a tested-content/source change,
increment revision, reset draft and prepare the updated snapshot for the next platform result.

The strong-solver screen for a Hard target is not optional (section 4); it uses its own
`docket_agent.py packet` and `record-screen` commands. Other optional diagnostics require an
explicit request or a concrete unresolved issue. Choose only the
needed role; never launch the old full sequence by default or to refresh stale local records. Use
`python tools/docket_agent.py prepare tasks/<slug> --q qNN --local-checks` to create isolated
solver/auditor packets, a question-only closed-book packet and scope binding without evicting other
active runs. This command prepares packets; it does not run models.

Read the applicable role prompt explicitly. Every diagnostic worker starts fresh without writer
history/shared memory (`fork_turns: none` on Codex; supported `omitClaudeMd` on Claude). A blind
solver/auditor receives only the exact question and one prepared packet, never gold, notes, selected
IDs or intended traps. A closed-book worker gets only the question and no tools/files. An optional
removal probe gets a renumbered packet without the tested document, using neutral folder names.
An independent reviewer gets frozen fields, full corpus and actual raw returns. Preserve returns
outside packets, bind records to their snapshot and report contaminated/cut-off runs accurately.
Resolve concrete findings, but do not assign local tier ratings or turn missing diagnostics into
readiness requirements.

Preserve current adverse diagnostic returns. Resolve concrete findings with source/platform evidence;
if no frozen content changes, an optional `## Local resolution` record can capture that adjudication:

```text
- DATE | rev: N | tested_sha256: HASH | assessor: ID | issue: EXACT_DIAGNOSTIC_LABEL | verdict: resolved | findings: CONCRETE_SOURCE_OR_PLATFORM_EVIDENCE
```

Use the exact diagnostic label from the checker (for example, `blind: ambiguous`). This records
resolution of an actual issue, never a new solve, a platform pass or a required extra report.

## 9. Style and set review

Read question/reasoning aloud for clarity; remove stock wording, unnecessary setup and copied
syntax. Preserve exact technical terms, periods and verbatim evidence. Keep answers bare and
checkable. Current platform form/guide limits govern; the older external workflow's trial details
and added writing kit are not treated as new official requirements.

For multiple questions, compare their actual answer paths, not just phrasing. Check duplicate
facts, shared answer paths, sibling hints, reciprocal giveaways and wording reuse. Vary levers,
document pairs and reasoning tags where evidence allows; diversity is not a quota or a reason to
reject the best single question. Record set decisions before hand-over.

## 10. Hand-over, feedback and state

`python tools/docket_agent.py report tasks/<slug> --q qNN` reports evidence read-only when needed.
Run one mechanical preflight with `python tools/check_questions.py tasks/<slug> --handover --q qNN`
after arithmetic verification and snapshot preparation. Fix FAILs and fix/explain WARNs; repeat
only after a relevant edit or unresolved failure. This phase-boundary command also writes
`notes/handover-qNN.md` with every form field in the form's order: Question, Number of asks, Gold
answer, Step-by-step reasoning, Answer components, Evidence (one row per component, with Doc N),
Necessary documents (role, alternatives, unticked rest), Reasoning tags (tick and leave unticked) and
Targeted failure modes. It maps local ids to the task page's Doc numbers from `notes/intake.json`,
states the origin and floor result, and exits 1 on a FAIL. Give the user the whole set of fields
every time, not only the changed ones, and say which form state they replace. The platform's run
history says "any edit to the question, answer or necessary documents needs a new result" and names no
other field. Ask the user to look at the form's "One defensible answer" check before spending a difficulty
run on a derived gold: it runs first and costs nothing (aq-03120 q01 rev 0 was run without it being seen).
Report measured results, not odds: no "likelier" tier, no pass probability, and no release recommendation
while a one-reading, no-cue wording of a hook whose counts were in band is still untested (on aq-03120 that
wording was called a one-in-four chance and then passed at Medium).
After pasting, check the difficulty panel before submitting: on 2026-10-07 the same page also
called its passing result "for an earlier version". Record a pass only when the page shows no such
conflict. Locally, any change inside the fingerprint is still a new revision and snapshot; old local
records stay historical and do not require replacement solves. Record actual platform results when
supplied or already authorized; preparation alone does not authorize external testing or submission.
`python tools/check_questions.py tasks/<slug> --export` writes ready user-origin sheets with the same
fields. Other origins remain accurate and their export restriction is reported. A sheet is not
a submission. Freeze the entire question file on confirmed submission/acceptance; later findings
and platform status observations go into `notes/feedback-qNN.md`.

For extension input, the handover also writes `questions/qNN.json` when the floor is clean and
all form inputs/document mappings are encodable. For only JSON, run
`python tools/check_questions.py tasks/<slug> --json --q qNN`: it serializes the existing fields
without validation runs or Markdown edits. Include all nine form fields and no local metadata,
notes, status, hashes or validation records. Use actual one-based platform Doc/component numbers
and exact option labels. See the [JSON field contract](tasks/template-task/README.md#json-input-values).
Unknown mappings or missing fields stop JSON generation; preserve the existing sidecar and report
that it was not refreshed. Regenerate successfully after edits before using the JSON. Exported data
is not submission, acceptance or an authorship declaration.

Track the [39 platform Checks](.claude/memory/reference/platform-quality-checks.md) independently
of the difficulty result. When a supplied capture is verified against an existing prepared snapshot:

```powershell
python tools/docket_agent.py record-checks tasks/<slug> --q qNN --capture <capture.txt> --revision N --tested-sha256 HASH
```

The explicit revision/hash asserts a verified match of the platform-tested content to that
snapshot. A matching title, save time or gold does not establish identity; if fields/version are
unavailable, retain the capture as unbound feedback and leave current Checks pending. The command
runs no models and appends raw captures to `notes/platform-checks-qNN.json`. Report/handover shows
all 39 outcomes and currentness separately from `ready`. Recorded submission clearance needs
current platform blocking checks and no explicit footer blocker. Missing/unknown blocking results,
stale/reload warnings and retained difficulty blockers prevent clearance; advisory warnings/retries
remain advisory. Only an admin can clear the own-words checks; report an explicitly nonblocking
reasoning-review state accurately, without changing actual authorship. Clearance is not acceptance.

Learning from verdicts (user-approved 2026-10-14): one run is three tries by one or two solvers, so
its lesson is often noise. After each verdict, record it in the question file, add one row to the
workspace ledger `notes/hard-runs.md` (date, bundle/question, design kind, screen result, platform
tier line and verdict, one-line route from the traces) and decide only that question's next action
by the playbook. Add no rule, memory note or tool check for one run. Every five new platform results
in the ledger (screen-only rows do not count), or when the user asks, review the batch: what the misses had in common, whether the screen's rejections and
permissions matched the platform, and which playbook lines to add, change or retire. Keep the
playbook to two pages and cite the rows each change rests on.

Triage feedback once in `notes/feedback-index.md`: exact platform version, issue, raw artifact,
current local revision/fix and next action. Deduplicate repeated panels only when their identity
and issue match; unknown versions remain unresolved. Compare the current fields before repairing
an old return. Keep verdicts, Coach summaries and raw traces distinct; a wrong answer is evidence
to inspect, not automatic proof of ambiguity. Preserve raw history and frozen questions.

Read a difficulty capture with `python tools/verdict_summary.py <capture.txt> --q tasks/<slug>/questions/qNN.md`
before interpreting it. It lists each run's version and tiers, how often the question file's wording is
quoted and whether "Your answer" equals its gold (the evidence for binding a run to a revision), and the
value each attempt's own Full answer commits to, beside the platform's note. Name every wrong attempt's
route from that list before designing a repair: the declared trap is often not what separated the solvers
(aq-02564). The tool only reads; its committed values are a reading aid, and the platform's grade is the result.
A committed value is not a route. The summary prints each attempt's line span, whether its Reasoning block was
loaded when the page was saved, and a note when a wrong attempt's Full answer is a bare value: read that span before
writing a route into a note, a memory or a report, and write "route unread" for a block that was not loaded
(aq-02749 q02: a 6 that equalled a predicted subtraction and a 9 called a miscount were both one list misread).
With `--q` the summary also prints, per attempt, the share of each Evidence quote that its trace echoes and
whether the quote's end is echoed (aq-03736 q01: four wrong attempts echoed the head of the deciding sentence
and none of its closing exception, while the page called all four a wrong phase). Use it to tell "never reached
the clause" from "read it and set it aside"; a paraphrase scores low, so it points to the span and does not
replace reading it.

For the next five newly promoted candidates, use one owner index (linked from other bundles if
needed) to record actual authoring minutes, revisions and ambiguity/necessity returns, plus observed
acceptance. Resume/revise the same row; record unknown timing as unknown and exclude platform wait
time from authoring time. Use accepted questions per known authoring hour only with complete timing
and acceptance observations, not local test counts. No retroactive timing estimates or extra model
checks. Checkpoints under 4,000 characters link the index and record the next concrete action.

## 11. Measure the next five candidates

Workspace `notes/feedback-index.md` owns this trial across bundles; `notes/efficiency.json` stores
the measurements. Do not create a new ledger per bundle or enroll historical questions. Candidate
IDs persist through resumption and revisions. Track prospective sketch work before promotion;
`promote` assigns one of five slots when that candidate becomes a question. Unpromoted work is
reported separately, not silently included in or omitted from a claimed end-to-end total.

Use these lightweight commands at work boundaries, not after every edit:

```powershell
python tools/docket_agent.py efficiency start --bundle <slug> --candidate i01 --phase sketch
python tools/docket_agent.py efficiency stop --session <returned-session-id>
python tools/docket_agent.py efficiency promote --bundle <slug> --candidate i01 --q q01 --revision 0
python tools/docket_agent.py efficiency record --event <measured-event.json>
python tools/docket_agent.py efficiency report
```

Start/stop measured intervals for `sketch`, `draft` or `revision` work. Stop before platform waits,
idle time, or yielding the turn; resume with a new interval on the same candidate. Only one timer
may run at once, and open intervals are not counted as finished work. If interrupted and the
active time is unknown, use `stop --session ID --discard` and retain incomplete timing coverage.
Never estimate missed time retrospectively. Agent/tool maintenance is not candidate authoring.

Record only actual observations as JSON events, with a stable `event_id`, `bundle`, `candidate`,
`kind` and `source` (trace, raw return or session-note reference). Reusing the same event is
idempotent; conflicting reuse is rejected. The [event fields](tasks/template-task/notes/feedback-index.md#measured-events)
cover reported tokens, platform attempts, revisions, outcomes and coverage. Unknown platform-run
identity remains pending in feedback notes; never manufacture an attempt ID from a repeated screenshot.
Do not count captures/check rows as separate runs or infer revisions merely from preparing again.

Token counts must come from actual model/API usage reports. Document token-window counts,
tool-output token counts and text-length estimates are not model usage. Leave tokens unknown
when that report is unavailable; record an observed zero explicitly. `complete` coverage is an
explicit source-backed assertion, not inferred from one timer or usage record. New work/usage
requires renewed coverage confirmation; partial totals must remain labelled partial.

Acceptance requires an actual platform observation; difficulty passes do not establish it.
Retired-before-submission candidates count as unsuccessful only when no submission is pending.
The report groups measured time by phase, platform attempts by stage, and revision work so the
largest recorded activities can be inspected. It does not infer causes of waste or model quality.
Accepted questions per authoring hour stays unknown until all five have complete timing, settled
outcomes and a positive time denominator. Keep token-coverage limits separate from timing limits.
These commands use local bookkeeping only; they never launch validators, models or external actions.
