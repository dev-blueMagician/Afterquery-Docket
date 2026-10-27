---
name: docket-redesign-v2
description: "2026-10-05 replacement policy: Easy minimum, evidence dependencies, independent shortest-route audit, exact-content records and explicit measured platform success."
metadata:
  node_type: memory
  originSessionId: ae999fcd-0d3a-4c3d-ae53-d4952c82e292
  modified: 2026-10-07T08:32:41.659Z
---

> **Frozen history (2026-10-14).** Measured mostly against the Low and Medium solvers. The current
> design rules are in [hard-playbook.md](reference/hard-playbook.md); where this note differs, the
> playbook wins. Open this note only for a specific case it records.

## Current rule

V2.1 adopts useful practices from D:\Docket_new\workflow.md: readable-document coverage and
extraction spot-checks; a hook inventory; lean sketches and cheap screening before full write-up;
drafting from factual notes with source recheck; independent numerical/date calculations; and
semantic set review. Decoys/counterfactuals are conditional on the selected lever. Ordinary valid
cross-document calculations/date/identifier joins are eligible. Gaps get candidate-specific,
exact-content impact review; missing needed material/unknown provenance remain blocking.

The latest user instruction is an Easy minimum, with Medium/Hard optional higher targets.
[CLAUDE.md](../../CLAUDE.md), [WORKFLOW.md](../../WORKFLOW.md), and the
[gate](reference/question-gate.md) define the current policy. Previous maximum-only rules and
D1-D7 ratings are historical, uncalibrated risk prompts. Do not reintroduce them as mandatory
High-only acceptance criteria.

Generate different evidence dependencies, not paraphrases of directly printed per-item statuses.
Use two supported matching fresh solves for fairness; a separate question-only shortcut auditor
tries the whole bundle's semantic, identifier, overview and duplicate-evidence paths. Reviewer
recomputes the key and tries to replace each necessary document using the remaining corpus.

Prepare binds all new check records to the current form fields and corpus bytes. Tier counts
show execution only. Only a genuine explicit fingerprint-bound platform pass at the target
establishes observed success. A local review, solver miss or Python suite cannot establish it.
Known missing/clipped ranges block readiness when their effect is relevant or unresolved.
Substantive independently reviewed irrelevant-gap assessments can permit a candidate while
preserving the incomplete-corpus warning; they cannot waive missing necessary/cited sources.

The form's slots line ("Hard 0/2 · Medium 0/3 · Easy 0/1") counts accepted questions only; "a question in
review holds its slot until then", so "Easy 0/1" does not show an open Easy slot. When the user says a tier
has no slot, treat that as settled: do not read the slots line against it, do not ask again, and do not offer
a submission below the stated tier (aq-02750, 2026-10-11: after an Easy pass the author twice offered an Easy
submission and asked about the slot; user: "no easy slot left, so must be medium or high"). Record the lower
pass and move to another hook or say plainly that none exists.
Tier slots are per bundle: a bundle can lack a slot for a tier (user, 2026-10-06: aq-00745 "have
no easy slot. we need to target at Medium"). Confirm the bundle's open tier before designing; a pass
below the open tier is not usable there, so new work targets the open tier (difficulty_target:
medium for aq-00745). Same for aq-00949 after q04's Easy pass (user, 2026-10-05: "at least Medium",
one attempt): new work there targets medium. Same for aq-docket-trial-01 (user, 2026-10-06: "set
target difficulty as at least Medium ... start work from the scratch again on Trial 1 ... we have
only one attempt, once after reach result, you need to check carefully again"): rebuilt from the
2026-10-06 capture, difficulty_target: medium, and a second careful check before hand-over. Later the
same day, after both write-ups failed the quick test, the user relaxed it: "actually in trial, it's
okay if accept in even Low tier" (trial-01 accepts an Easy pass; still one submission attempt). Same request for aq-docket-trial-05 (user, 2026-10-06: "set target difficulty as at least Medium ... start work from the scratch again on Trial 5 ... only one attempt"): rebuilt from the 2026-10-06 capture, difficulty_target: medium; reviews and a fresh author found no fair Medium design in that bundle (see [[docket-local-solver-calibration]]), so the hand-over asked whether the trial-01 relaxation also applies.
Same Medium target for aq-docket-trial-02 (user, 2026-10-06: "set target difficulty as at least Medium
... start work from the scratch again on Trial 2 ... only one attempt"): rebuilt from the 2026-10-06
capture; the trial-01 relaxation was not restated for trial-02. Same request for aq-docket-trial-07
(user, 2026-10-06, with "once after reach result, you need to check carefully again"): rebuilt from the
2026-10-06 capture, difficulty_target: medium; two authors and two reviews found no fair Medium design
(see [[docket-local-solver-calibration]]), so the hand-over asked the user to quick-test first and
decide whether Easy is acceptable. Same Medium target for aq-01321 (user, 2026-10-06: "work on
AQ-01321 ... you should do difficulty_target to at least medium"; slots Hard 0/2, Medium 0/3, Easy 0/1,
9 submissions): new bundle, difficulty_target: medium; two checked write-ups were reviewed Easy-leaning
(Medium about 9-12%), so the hand-over asked for quick tests before any difficulty run. Same Medium
target for aq-01433 (user, 2026-10-06: "work on AQ-01433 ... you should do difficulty_target to at least
medium"; slots Hard 0/2, Medium 0/3, Easy 0/1, "In review: Medium 1", 8 submissions): new bundle; q01
rev 1 checked (review Easy-leaning, Medium ~17%) and q02 checked with a deferred reasoning-quote fix
(Medium ~10%); hand-over asked for quick tests first. The user ran q01's difficulty check directly:
"In band — Easy tier", Low 2/5 (Run 1, version 55d10a), below the bundle's Medium target; the Easy slot
(0/1) was open; the user submitted it there (confirmed 2026-10-07: "q01 is passed and now submitted,
set status. and answer_tier as Easy Tier", then "I mean accepted_tier"; front matter now
accepted_tier: Easy Tier) and a second sketch round found no fair Medium design. Same Medium target for aq-01428 (user,
2026-10-06: "work on AQ-01428_2026-10-06_1949 / you should do difficulty_target to at least medium"; slots
Hard 0/2, Medium 0/3, Easy 0/1, 9 submissions): new bundle, difficulty_target: medium; q01 (untied event
edition trap, review Medium+ ~45%) handed over as primary and q02 (Easy-leaning, robust necessity) as fallback.
Same Medium target for aq-01431 (user, 2026-10-06: "work on AQ-01431_2026-10-06_1949 / you should do
difficulty_target to at least medium"; slots Hard 0/2, Medium 0/3, Easy 0/1, 9 submissions): new bundle of
SEC comment letters, difficulty_target: medium; the caller and two authors found no fair Medium design, and
the one fully checked write-up (q01) was reviewed Easy (Medium 6-8%), so the hand-over asked for a quick test
and the user's decision on Easy before any difficulty run. The user ran the difficulty check anyway: rev 0
"Between levels" (Low 0/5 · Medium 4/5), so rev 1 removed the cue the medium model followed (same target).
On 2026-10-08 the user restarted aq-01431: "remove questions you prepared before and start from fresh. there is
no slot for Easy Tier for this bundle, we should target medium and high. do you best." The old q01 work was
removed (recoverable from git 30c3f7e) and new work targets medium, with hard where a design supports it.

Same Medium target for aq-01541 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should
target medium and high. do you best."; page "Hard 1/2 · Medium 0/3 · Easy 1/1", "Easy questions are full on this
set"): seven rulings from one FCRA class action; three checked write-ups (q01/q02 alternatives on one path, q03 a
second document pair), all reviewed Easy-leaning (usable Medium-or-High ~15-20%); hand-over asked for quick tests
before any difficulty run, since an Easy result cannot be submitted there.
Same Medium target for aq-01432 (user, 2026-10-06: "work on AQ-01432_2026-10-06_1949 ... you should do
difficulty_target to at least medium"; slots Hard 0/2, Medium 0/3, Easy 0/1, 9 submissions): new bundle of eleven FTC
and CMA consumer-protection guidance documents; no fair numeric design; two checked write-ups reviewed Easy-leaning
(Medium about 8-10%), so the hand-over asked for quick tests and whether Easy is acceptable.
Same Medium target for aq-01278 (user, 2026-10-06: "work on AQ-01278_2026-10-06_1140. you should do
difficulty_target to at least medium"; slots Hard 0/2, Medium 0/3, Easy 0/1, 9 submissions): four-insurer peer bundle
of Q1/Q2 2026 releases; quick-test batch of five handed over. The user ran q02's difficulty check: "In band — Medium
tier", Low 0/5 · Medium 1/5 (Run 1, version 4093c3), with the "may be too vague" advisory; local review had said
easy, marginal toward medium. Binding to a local fingerprint waited for the tested form fields.

Same Medium target for aq-01650 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should
target medium and high. do you best."; slots Hard 0/2 · Medium 0/3 · Easy 0/1, "In review: Easy 1", 8 submissions,
0 of 10 quick tests used): seven unrelated academic papers on financial literacy (three CHFS, two on Osaka's PPS
2010/2011 waves, one BoJ 2016 survey, one Saudi survey). Two independent authors found one Medium-plausible design
(q01, a hidden complete-case scope in the BoJ paper joined to a CHFS 2015 mean; review Medium about 22%, Easy 45%)
and no Hard design; the hand-over asked for the free form check and a quick test before any difficulty run.
Platform: q01's four difficulty runs ended "Answer not supported" (twice), "Did not finish" and "Too hard"; 4 of 8 runs
left. Restarted 2026-10-08 under gate v3 (user: "first clear work history on AQ-01650 and start again by new updated
gate"): round 1 moved unchanged to tasks/aq-01650/archive/round1-q01/ (README there); target kept Medium; new q02 =
women's share of the Osaka panel's 40-64 non-mandatory check-up takers minus their share of 40+ people with a counted
cancer examination (both Table 4s, 14.5 points; look-alike within-sex percentages give -9.3), checked, platform pending.

Same Medium target for aq-01539 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do you best."; page "Hard 0/2 · Medium 1/3 · Easy 1/1", "Easy questions are full on this set", 7
submissions left, 0 of 10 quick tests used): fourteen orders from the Snowflake data-breach MDL. Two independent authors
and the caller found one Medium-capable design (q01, a per-district tag-along count derived from the transfer order's
counting footnote; review ready, medium, usable Medium-or-High about 35%); every other design leaned Easy. Hand-over:
form free check, then a quick test, then a difficulty run only on a survivor.

Same Medium target for aq-01960 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do you best.", plus a fix prompt to check arrived verdicts with the feedback skill; the intake capture
showed "Hard 0/2 · Medium 0/3 · Easy 0/1", 0 runs and no drafts, so no verdict existed): fourteen KLA quarterly earnings
releases (Q3 FY23 to Q4 FY26, ten-for-one split in the last). Two checked write-ups on one family, guidance-implied gross
profit: q01 the June 2026 quarter's non-GAAP gross profit against D13's revenue x non-GAAP margin midpoints (3.3%, trap:
bundled acquisition charges vs the cost-of-revenues part), q02 fiscal 2026 GAAP gross profit against the four quarterly
guidance products ($250 million, trap: pairing each release with its own next-quarter guidance). No local review or tier
estimate (gate v3); platform pending; submit both only by the user's decision. Quick tests (user reports, same day): q01, q02 and a split-anchored guidance-in-force sketch (i03) were all "too easy"; round 3 offered i04 (fiscal-2026 non-GAAP gross margin whose printed grouped acquisition charges are the decoy).

Same Medium target for aq-02028 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do your best", plus a fix prompt to check arrived verdicts; none had arrived; page "Hard 0/2 · Medium
0/3 · Easy 0/1", 9 submissions, 0 of 10 quick tests): twenty Productivity Commission maritime-logistics submissions.
Rule 10 rules out submitter lists, and most cross-document figures were approximate or conflicting. The one
Medium-plausible mechanism was an untied anchor: Doc 6 alone dates the WA coastal-trading exemption's end (31 March
2022), which falls after Patrick's scheduled surcharge rises (7/03/2022) and one day before Flinders Adelaide's
(1/04/2022) in Doc 2's dated table. q01 asks for the mean of all 13 import surcharges that day ($117.39), so both the
stale reading ($111.55) and "apply every new rate" ($120.28) fail. Rev 4 (34 words, at the user's
request) failed the quick test ("Too easy"), as rev 2 had, so q01 was dropped. q02 replaces the hook: yearly truck
trips saved at 4 TEU loads instead of VTA's current 2.5 (Doc 8), on the port throughput stated by the newest
terminal (Doc 1, 2.88 million TEU), beside VTA's printed "approximately 450,000" on its own 3 million base. Rev 0
(3.5 TEU, 34 words, 329,000) drew the length warning and three reasoning-number flags. Rev 1 (20 words, 432,000,
every step an exact bare expression) was Too hard, Low 0/5 · Medium 0/5 · High 0/5, "may be too vague": "the port
throughput [the terminal] states" also read as VICT's own 800,000 TEU (9 of 15 attempts, 120,000), and 5 took Doc 8's
printed 450,000. Rev 2 ("whole-port throughput", 20 words, same gold) is the one focused repair; checked, platform
pending; a repeat of the same failure retires the hook. A two-terminal variant was kept as a sketch, because its gold equalled the "apply every new rate" answer.

Same Medium target for aq-02086 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do your best."; page "Hard 0/2 · Medium 0/3 · Easy 0/1", 9 submissions, 0 of 10 quick tests): five UK
housing-policy documents (Awaab's Law consultation, its consultation-stage IA and the government response; Decent Homes
Standard private-rented consultation and response). Two checked write-ups, platform pending: q01 = staff hours a year the
Ishak family's landlord (RBH, 12,000 homes, Doc 1 glossary only) would spend on additional written summaries under Doc 2's
chain (4 repairs x 40% x 50% additional x 15 minutes = 2,400 hours; decoys 4.2 survey repairs, all 19,200 summaries); q02 =
annexed consultation examples outside Awaab's Law's first phase (rodents, faulty window), where Phase 1's "all emergency
hazards" excludes the door-lock and water-loss examples of Phase 3 types. Parked: a BRE per-home damp cost (269 / 75,000
repeats, so the form's exact-result check would flag it) and a projection year with discrete/continuous readings. Results (same day): q01 quick test "too easy" (dropped); q02 rev 0 blocked as "too vague" (form solvers answered in hazard types, one took the water-supply decoy), rev 1 (asks for the examples; gold adds type labels) quick-test "too easy" (dropped). Round 3: q03 (registered-provider responses, Doc 3, as a percentage of registered providers, Doc 2: 253 / 1,645 = 15.4%) and q04 (hazard types with an annexed emergency/significant example the first phase missed; decoy water supply) both quick-test "too easy": all four designs dropped; stopped after three rounds and reported to the user. The user then chose to try a remaining idea: q05 (relative shrink of the private-minus-social non-decency gap, 2010 to 2020; 2010 social share only in Doc 1, the rest in Doc 4: 53.5%) checked, platform pending.

Same Medium target for aq-02102 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10 quick tests): five Cabinet
Office papers (Civil Service McCloud remedy consultations 2021-22 and 2023 with their responses; a 2017 compensation-
scheme consultation), few cross-document numbers. q01 = fall in individuals' share of all responses received (3.81 pp;
the two responses' Table 2s count non-answering responses under different rules). Rev 0's full-corpus solve called
Doc 4's "Total Received" 107 a defensible second reading, so rev 1 states "including those addressing no question";
rev 2 fixed a form reasoning flag (see [[docket-form-automated-checks]]); quick test "too easy" (user, same day), dropped. q02 (unions that
accepted the 2016 offer and were engaged in 2023 without a written reply; PGA alias, POA look-alike) quick test "Too
easy — solver got it", dropped.

Same Medium target for aq-02147 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10 quick tests): five
DWP/DHSC papers (2019 "Health is everyone's business" consultation and its 2021 response; the 2024 SSP percentage-rate
consultation, its equality analysis and the 2025 response). Design constraint: every statutory figure (LEL, flat SSP
rates, the 80% decision) is duplicated across documents and likely recallable, so each necessary document had to add a
bundle-specific input (local inference, no platform evidence yet). Two checked write-ups, platform pending: q01 = week in
which the consultation's break-even point falls at the employee respondents' median rate (90%, response only) -> Week 12
(Table 1 prints 2/3/4 weeks for 60/70/80%; "Doc 3 or Doc 4" alternatives for the £123 five-day profile); q02 = week the
equality analysis's £175 case study is first worse off overall at the employers' median (50%) -> Week 3 (easier sibling).
q01 Run 1 (same day, version 8b4bdc): "A marked document may not be needed ... without document 3" (the equality analysis's
identical case study replaced the consultation) with Low 2/5; q01 dropped, hook retired. q02 shares its mechanics, so a quick
test comes before any difficulty run. Replacement q03 (checked, platform pending): retentions a year at the 2021 response's
median saving per retained employee (£8,000, Doc 2 annex) that offset an 80% rate's rise over current SSP costs (£0.65bn to
£1.07bn, Doc 3 only) -> 52,500; look-alikes Doc 3's average £30,614 (13,719) and the £1.07bn total (133,750). q03 quick test (same day): "Too easy — solver got it", dropped;
no fair Medium design left among the bundle's hooks; next: vet the platform's "Harder variations".

Same Medium target for aq-02165 (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target
medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10 quick tests): the same five
Cabinet Office papers as aq-02102, byte-identical, so that bundle's two quick-test "too easy" families (response shares,
union lists) were treated as closed and its map reused by hash. A second task on identical documents also means the
platform's cross-task Original question check can see aq-02102's drafts: reuse no sentence frame. One checked write-up,
platform pending: q01 = years between the earliest employer-funded pension top-up under the 2017 compensation proposals
(State Pension age minus 10, Doc 5) and the MOD-funded effective pension age of MDP officers (State Pension age minus 3,
Doc 2's DPF extract) = 7, the officer's SPA cancelling; decoys Home Office police NPA 60 in the same extract (5) and age 55
held fixed against SPA 67 (9). Held sketch i02: classic's 1.5% WPS (Doc 4) as a share of the 2021/22 7.35% band rate
(Doc 1) = 20.4%, weak because alpha rates are widely recallable. Quick test, same day (user): q01 "it's too easy to pass
quick test"; dropped, family closed. Round 2 (i03: 2023 missed-election rule on the 2016 Table 1 count, 54,807; i02)
both quick-test too easy (user, same day); a definition-scope variant (Doc 4's "unprotected" glossary, 274,563) was
rejected as a likely form "too vague" block. Stopped and reported: no fair Medium design found on these bytes.

Same Medium target for aq-02157 (user, 2026-10-08: "let's work on AQ-02157_2026-10-08_1559. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions,
0 of 10 quick tests, 8 of 8 runs): five UK tobacco/vaping papers (smokefree generation consultation Doc 1 and response Doc 2;
pack-insert consultation Doc 3, its May 2023 impact assessment Doc 4 and response Doc 5). Removal probes, run for a concrete
recall concern, decided the set. q02 (share choosing the Netherlands' flavour method but not Finland's, 6.1%) was dropped: a
probe without Doc 1 recalled the country-to-method mapping (p 0.65). q03 (highest individual support for the generational
ban among nations whose rate fell, 65.5%) was dropped: probes recalled the directions (p 0.8 and 0.45). q01 rev 0 (first
nation to 5%: 2032) was guess-reached via Scotland's remembered rates; rev 1 asks the 2030 gap between the highest and lowest
nation repeating each 2021-22 point change (Doc 3 2021 list + Doc 1 2022 list, reordered) = 8.9 points, which needs NI's exact
small rise (probe without Doc 3 forced 7.4; without Doc 1 forced the gold at p 0.1, stated). q04 = rise in the minimum excise
duty on a 20-pack from the IA's October 2021 MET (Doc 4) to the response's "at least £8.46" (Doc 2) = 21.6% (look-alike: the
IA's £7.98 average-pack duty; Doc 1's £7.87 edition decoy; both probes missed). Form paste (user screenshots, same day):
q01 rev 1 drew "Say the rounding" and q04 rev 0 drew reasoning flags "£8.46" and "122," (see
[[docket-form-automated-checks]]); q01 rev 2 (one decimal stated) and q04 rev 1 (plain amounts) checked; a second paste
was read as a list-and-deep-text blind spot (v8), so q01 rev 3 reused identical number strings; its paste cleared Steps 1-12
(lists are read after all) and flagged only Step 13's 15.6, a result written "= 15.6 per cent"; rev 4 put rate units
before the expression, but the user's wording ("in %:") drew the same flag (2026-10-09), so q01 rev 5 ends with the 2022
gap plus the widening (0.1 + 8.8 = 8.9 points) instead of subtracting the two 2030 rates (v10 emulator); q04 keeps two
deep-text flags (Steps 1-2) that wording cannot fix. q04's first difficulty run (Too hard, 0/15) measured the user's
paraphrase without "response" (literal answer 13.1%, Doc 1's £7.87; every Medium/High attempt found the MET floor), so
q04 rev 2 named "the government's response to the smokefree consultation". Run 2 (Too hard, 0/15) measured the user's
next paraphrase, "What is the increase in ...", still graded against 21.6%: High 5/5 gave the literal £1.5 (the MET
route), Medium fell for the £7.98 look-alike (3) and the £7.87 edition (1), Low took Doc 1's £7.87 as the start (5);
q04 rev 3 adopts that wording with gold £1.5, and Run 3 passed "In band — Medium tier" (Low 0/5, Medium 2/5); q04
ready, submission the user's; q01 platform pending.

Same Medium target for aq-02198 (user, 2026-10-08: "let's work on AQ-02198_2026-10-08_1809. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; capture page Hard 0/2 · Medium 0/3 · Easy 0/1, 9
submissions, 0 of 10 quick tests, 8 of 8 runs): the third task on aq-02102's byte-identical Cabinet Office papers, so the
closed families of aq-02102 and aq-02165 carried over. The caller and two independent question-author agents each read all
five texts and found no fair Medium-capable design: Doc 1 and Doc 2 reprint the same equality assessment, so no Table 1 or
diversity figure can make either necessary (see [[docket-series-editions-necessity]]); final rules are printed whole in
the responses; public figures are recallable; Doc 5 links only through closed families. Two fair sketches passed the
mechanical screen and were offered only as optional free quick tests: i01 (regulation 142(4) still cites section 95(2)
after the dropped 2022 correction; decoy 95(2A)) and i02 (757 days from the 2023 launch to the statutory statement
deadline). All three authors expected both to be too easy. No question promoted; next step is the user's decision.

Same Medium target for aq-02208 (user, 2026-10-08: "let's work on AQ-02208_2026-10-08_1841. there is no slot for Easy
Tier for this bundle, we should target medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9
submissions, 0 of 10 quick tests): six Federal Register space-launch documents (FAA CSLCA final rule; FCC WTB proposed
licensing/coordination procedures, Dec 2024; FCC Third R&O; WTB final procedures, 2025; FCC 2026 emergent-space NPRM; FAA
2026 waiver NPRM). Two independent authors found numeric cross-document hooks thin (single-source cost model, inferable or
weekend-shifted effective dates, recallable thresholds and CFR frequencies). q01 (proposed coordination items the final
procedures require of no licensee, two silently dropped items) quick-test "too easy"; dropped. i11 (how many more
transmitter-characteristic items the final list holds than the proposal, 17 - 12 = 5, Doc 4's discussion explaining only
three additions) survived the quick test (user, same day) and became q02; difficulty run pending.

Same Medium target for aq-02220 (user, 2026-10-08: "let's work on AQ-02220_2026-10-08_1905. there is no slot for Easy Tier
for this bundle, we should target medium and high. do you best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of
10 quick tests): four UK heat network zoning papers (2021 consultation, its impact assessment, the June 2022 response, a 2026
summary of the 2023-consultation response). Facts printed twice (10-year grace period, CCC 18%, IA SNPVs) carry no necessity,
so every design paired the IA with a one-document fact. Quick tests (user): q01 (benchmark gas share of input, 40.0%) and i02
(2035 share, 46.3%) too easy; i03 survived but q03 (same wording; 87.8 TWh) was then reported "too easy"; q02 dropped after a
removal probe reached its gold without Doc 1; i06 and i07 vanished from the page untested. q03 rev 1 (paraphrased "most
recently stated 2050 share", one focused repair) was also quick-test "too easy" (2026-10-09), as were re-entered i06
and i07: all seven designs closed, no fair Medium design left; reported to the user to stop or release the bundle.

Same Medium target for aq-02367 (user, 2026-10-09: "let's work on AQ-02367_2026-10-09_0158. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of
10 quick tests, 10 of 10 runs): byte-identical to aq-02220 (all four sources and extractions sha256-equal), so its seven
too-easy designs were closed families and its sentence frames off-limits (cross-task Original question check). The caller
(hooks n1-n7) and two independent question-author agents (a1-a11) each read all four texts and found no fair Medium design.
The one fair two-document sketch left, i01 (2050 IA deployment depending on the group Doc 4 would connect at zero cost,
31.2 - 20.7 = 10.5 TWh; Doc 1's rounded 31 - 21 = 10 as decoy), is a keyword bridge plus two lookups, so it was offered only
as an optional free quick test, with the recommendation to release the bundle if it fails.

Same Medium target for aq-02408 (user, 2026-10-09: "let's work on AQ-02408_2026-10-09_0407. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of
10 quick tests, 10 of 10 runs): six unrelated Federal Register texts (FERC reactive-power NOPR 2024, DOE North Plains
Connector NOI, WAPA-218, EPA coal-ash deadline proposal Nov 2025, DOJ Constellation/Calpine judgment and CIS Dec 2025, FERC
IBR modeling order Feb 2026); no editions, no proposal/final pair, no cross-citations. The caller and two independent
question-author agents read all six texts; only one fair cross-document numeric join exists: EPA's covered coal plants by
market (Doc 4) against DOJ's relevant geographic markets, ERCOT and PJM's Coastal Mid-Atlantic area only (Doc 5). q01 rev 0
(checked, platform pending; tested_sha256 2e56252f...): Calpine-owned capacity divested in the DOJ markets holding a covered
coal plant, nearest 10 MW = 660 (ERCOT only: 557 + 28.5% x 365); decoys 5,040 (PJM divestitures added), 920 (whole Gregory).
Removal probe without Doc 4 forced the gold at p 0.4 from the "Calpine-owned" wording and regional coal geography, so Doc 4
is ticked "Exclusion / condition source" with a reviewer note. Hand-over recommends the free form check and a quick test first.
Quick test, same day (user: "q01 too easy for quick test", no panel): dropped. Both traps were tied (the Coastal Mid-Atlantic
scope sits in the sentence naming DOJ's PJM market; Calpine's 28.5% share follows Gregory's 365 MW), so no fair focused
repair; join closed, and no other fair Medium design was found on the bundle.

Same Medium target for aq-02447 (user, 2026-10-09: "let's work on AQ-02447_2026-10-09_0556. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of
10 quick tests, 10 of 10 runs): five BIS export-control rules (Jan 2023 Macau IFR, Mar 2024 SDN 744.8, Oct 2024 Data Center VEU,
Sep 2025 Entity List, Jul 2026 UAE-to-A:5 rule, post-cutoff) plus an unrelated May 2026 EPA SNUR rule. No organization is shared
across documents; the only numeric series is OMB 0694-0088 (29.4/29.6/29.4/29.7 minutes; +20, ten, about -50 applications).
The caller and two independent question-author agents found one Medium-capable fair design: q01 = distinct five-character
ECCNs named in Doc 6's 2026 § 742.6(a)(6)(iii)(B) (18) but absent from Doc 1's January 2023 § 742.6(a)(6) (9) = 10; look-alike:
Doc 1's preamble list of seven ECCNs (no 5A992/5D992) gives 12. Rev 1 named "January 2023" (a probe without Doc 1 read "the
2023 Macau rule" as the October 2023 rules) and "five-character" (Doc 6 itself writes "ECCNs 3A001.z.1.b"); removal probes
without each document and closed-book probes on revs 0-1 all missed; checked, platform pending. Held for a free quick test only:
net 0694-0088 burden of the SDN and UAE rules, -893 minutes. Quick tests (user, same day): rev 1 "too easy"; the unpinned sketch wording
("How many distinct ECCNs does BIS's July 2026 UAE rule name in § 742.6(a)(6)(iii)(B) that its January 2023 Macau rule's
§ 742.6(a)(6) did not?") "survived", so rev 2 adopts it verbatim (checked, difficulty pending). Rev 2 removal probes without
Doc 1 forced the gold twice in three runs from the recalled public October 2022 list: a stated Document-check risk. Difficulty Run 1 on rev 2
(Version 0cf427): "Too easy", Low 5/5 (Coach: the paragraph citations point to both lists); rev 3 names the two provisions in words
("the UAE license requirement of BIS's July 2026 rule", "the China-and-Macau license requirement of its January 2023 Macau rule", gold
still 10 under every reading but the preamble's seven ECCNs) was quick-test "too easy" (user, same day), so the family was retired and q01
dropped; the last fair idea, i02 (net license-application burden of the SDN-list and UAE rules, -15 hours at the nearest hour),
was quick-test "too easy" too (user, same day): no fair Medium design left; release recommended.

Same Medium target for aq-02483 (user, 2026-10-09: "let's work on AQ-02483_2026-10-09_0840. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of
10 quick tests, 10 of 10 runs): five EPA proposed approvals of state CCR permit programs on one template (Wyoming 2025;
Virginia, Louisiana, Alabama, Wisconsin 2026) plus an unrelated OSMRE Pennsylvania rule. Templated twins kill necessity
(Virginia/Louisiana lists identical; EPA's dated amendment list printed in all five), so every design pairs two
state-specific facts. The caller and two independent question-author agents found one untied numeric trap: q01 = days
between the newest federal amendments reflected in Wyoming's rules ("promulgated through December 14, 2020", a cutoff, so
the November 12, 2020 amendment) and Wisconsin's (August 28, 2020) = 76 (decoy 108); checked, platform pending. Four more
sketches (Legacy Rule definitions Wyoming minus Virginia 3; deadlines 28 weeks; Alabama-not-Wisconsin approvals 8;
"infiltration" landfills 16) were handed over for the free quick test; list-only diffs ranked low after aq-02447's Run 1.
Quick tests (user, same day: "q01, i03 too easy. i04 survived"): the cutoff-to-amendment mapping (q01) and the Wyoming-minus-
Virginia definition count (i03) were too easy, q01 dropped; i04 survived and became q02 rev 0 word for word: "To the nearest
week, how far apart were Wisconsin's deadline for CCR landfills' initial-permitting submittals and Wyoming's for existing CCR
impoundments' permit applications?" = 28 weeks (Wyoming's 12-month rule in Doc 2's permitting section applied to chapter 18's
August 19, 2022 effective date in another section, against Doc 6's printed February 1, 2023; decoy 24 weeks). Its
difficulty Run 1 (Version 7ed75f): "Too easy", Low 5/5, every attempt chaining the rule's own "effective date of the State
rule" pointer; Coach not captured; no fair focused repair, q02 dropped. Remaining sketches (i01 8, i05 16, i06 59 weeks) are
weaker designs; three authors found no other fair Medium mechanism; release recommended unless the user wants free quick tests.

Same Medium target for aq-02486 (user, 2026-10-09: "let's work on AQ-02486_2026-10-09_0906. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of
10 quick tests, 10 of 10 runs): seven unrelated Federal Register fee rules (FOIA rules of FLRA 2023, Peace Corps 2024, NRC 2026
final, ONCD and Access Board 2026 proposed; Copyright Office 2026 fee schedule; DHS Form I-246 fee). No proposal/final pair,
edition or cross-citation; no FOIA rule prints a dollar search rate. The caller and two independent question-author agents
found only parallel-rule applications to one stated request, no measured Medium recipe. q01 = ONCD's proposed FOIA charge
minus the Access Board's for photocopied pages to a news reporter: only the Access Board forgoes totals of "$25.00 or
less", ONCD's $25 is a notice. Rev 0 (225 pages, $12.50) drew the form's "Step 1: Which document says 225?" (the question's
own number, printed only in an unticked document); rev 1 (216 pages, printed in Doc 5; $11.60; 35dd0246...) drew difficulty Run 1 "In band — Easy tier", Low 2/5 (user: "no easy slot
open, must be placed in medium or hard"): the grader accepted the missed-rule route's -$11.60; rev 2 (f377c49c...) asks the
reporter's total paid to both agencies (gold $11.60, missed rule $34.80): difficulty Run 2 "In band — Medium tier", Low 0/5 ·
Medium 2/5 (Version c47c1a; user: "evaluated as medium tier. well done."); status ready, submission the user's. Removal probes without either document
said "not answerable" (forced gold p 0.25 / 0.15 by assuming the DOJ-template rule or a generic rate). Quick-test sketches: i03
(FLRA minus NRC, 1,400 pages, NRC's PDR $0.30 beside its FOIA $0.20 flips the sign, $65) and i04 (NRC rounds search up to the hour vs the
Peace Corps' more-than-half quarter hours, 45 minutes; FLRA prints the same Peace Corps sentence, a Document-check risk).
Platform pending.

Same Medium target for aq-02505 (user, 2026-10-09: "let's work on AQ-02505_2026-10-09_1045. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; page Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of
10 quick tests, 10 of 10 runs): seven Federal Register texts filed as "Forced Labor Import Enforcement Filings": three editions
of DHS's UFLPA Entity List (Nov 25, 2024; Jan 15, 2025; Aug 3, 2026, each superseding the last; printed totals 107, 144, 187,
which count each entity once across sub-lists) plus four unrelated rules (DOL H-2B survey NPRM, NOAA seafood COA NPRM, USTR
Section 301 forced-labor determinations, CBP supply-chain ANPRM) that share no figures with the series. The caller read all
seven texts; no independent authors were run. q01 rev 0 (checked, platform pending; tested_sha256 2917dbde...) = percentage
growth of UFLPA-listed entities from November 1, 2024 to August 3, 2026, 139.7%: the November 1 version is not printed, so
its size is Doc 2's 107 less the update's new entities, 29 rather than the 5 + 25 named, because Xinjiang Daqo was already
listed (stated only in its own description paragraph); end 187 (Doc 6). Traps 142.9% (Daqo counted) and 74.8% (Doc 2's
November 25 total as the base). Removal probe without Doc 2: "not answerable", forced gold p 0.3 from recalled 2024 totals
(stated risk). Docs 2 and 6 print the totals in words, so the form's number check may flag three source steps. Sibling
sketch i02 (entities listed when DOL published its H-2B proposal on Nov 18, 2024: 78) was closed after the closed-book
check below recalled 78. Difficulty Run 1 on rev 0 (Version 95fd92): "In band — Easy tier", Low 1/5 (4 low attempts at
142.9%; closed-book 84.6% from a recalled ~78; Document check: Docs 2 and 6 both needed), unusable without an Easy slot.
Rev 1 (f58099e1...) asked from November 15, 2024, a date no document prints: Run 2 (Version 4200aa) "Too hard", 0/15,
all high attempts reading the date as a typo for November 25 (74.8%), the rest missing Daqo. Rev 2 (36ff520a..., checked,
platform pending) asked from "the list in force on November 15, 2024": Run 3 (Version 0b7d6e) Easy again, Low 1/5, so the
family was retired and q01 dropped (2026-10-10); the user asked to "check arrived verdicts and improve your performance", and
two independent question-author agents searched the bundle for a mechanism medium clears and low does not. Result: q02 rev 0
(checked, platform pending; tested_sha256 ae90f7cd...) = which entities first placed on the UFLPA Entity List from November 25,
2024 through August 3, 2026 mine, process or source copper (four names, one member set per notice; decoy Xinjiang Habahe
Ashele Copper, a Doc 4 copper addition already on Doc 2's November 2024 list outside its five additions). Removal probes:
without Doc 2 forced gold p 0.4 from memory, without Doc 4 gold only as a p 0.3 runner-up (stated recall risks). Held: a
Jiangsu-based count (8) whose parent company's base is unstated. Run 4 on q02 (Version b94f39): Easy again, Low 1/5 (2 Ashele, 2 incomplete,
1 right by cross-checking the appendices; all three documents needed). Four runs, three at exactly Low 1/5 across two
mechanisms: the decision (another question, use Easy, or release) was returned to the user. The user chose another question
("option 3"): q03 rev 0 (checked, platform pending; tested_sha256 e2278b31...) widens q02 to entities that mine or source
copper or lithium (five names, adding SDIC Xinjiang Lithium Industry) with two mentions-vs-does decoys in Doc 6 (SDIC Lop Nur
Potash via "respectively"; Xinjiang Tianhongji, lithium-battery electrode materials from carbon); q02 dropped. Run 5 on q03 (Version 704f4c):
"Between levels", Low 0/5 · Medium 0/5 · High 5/5 ("Make it a little harder, so the high model reaches your answer only some of
the time"); the medium model put Ashele in every answer that reached Doc 4's (v) descriptions, the high model excluded it five
times; the Coach's near-miss example (Xinjiang Zijin Nonferrous) smelts zinc. q03 dropped; the one focused repair is q04 rev 0
(checked, platform pending; tested_sha256 e5563dcd...): "To one decimal place, what percentage of the entities first placed on
the UFLPA Entity List from November 25, 2024 through August 3, 2026 mine or source copper or lithium?" = 5 / 109 = 4.6%, so the
Daqo check (base 187 - 78) and the Ashele check (set) must both be cleared; traps 5.5% and 4.5%; two expected number-check false
alarms (107, 187 in words). The user quick-tested it before any run ("q04 too easy for quick test", no panel): the low model
reached 4.6% with both checks stacked. q04 dropped and the decision returned to the user (release, or the Easy result if that
slot is usable): with a hidden already-listed check this bundle lands Easy or Between levels, and without one the low and medium
models read the notices alike.

Same Medium target for aq-02501 (user, 2026-10-09: "let's work on AQ-02501_2026-10-09_1008. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; the capture itself showed "Hard 0/2 · Medium 0/3 · Easy
0/1" and "Still open ... Easy", flagged once to the user, user statement followed): seven Federal Register texts on GI Bill,
discharge and DMDC topics (DEERS SORN 2022, VA 85/15 final 2024, VA character-of-discharge final 2024, ED CEVSS FY2024 notice,
DoD DARB interim final rule 2024, VA STEM Scholarship NPRM 2026, DMDC 01/USHRIS SORN 2026); no editions, no proposal/final pair,
no cross-citations. The caller and two independent question-author agents (A numeric, B rule/scope) found no measured-Medium
mechanism. Free quick tests (user, same day: "i01 survived, others failed"): i02 (proposal-to-final-publication gaps,
1,386 - 461 = 925 days) and i03 (lettered routine uses, DEERS 37 with no JJ minus DMDC 01 26 = 11) too easy; i01 survived and
became q01 rev 0 word for word: "Which separations does DoD's Discharge Appeal Review Board count as less than honorable but VA
automatically accept as other than dishonorable?" = general (under honorable conditions) discharges and entry-level
separations (Doc 5's DARB definition includes general and uncharacterized; Doc 3 binds general discharges and splits
uncharacterized into three types, only entry level accepted); checked (tested_sha256 e23be069...). Its full checks failed the blocking "Needs the documents"
(user screenshot, same day: "Answerable without the documents"): both VA facts are public 38 CFR 3.12 text. Rev 1, the one
focused repair, keeps Doc 5's set but takes the VA side from the 2024 rule's own statements of effect: "For which separations
that DoD's Discharge Appeal Review Board counts as less than honorable does VA's 2024 character-of-discharge rule expand benefit
eligibility?" = OTH discharges, bad-conduct discharges and dropped-from-the-rolls separations (Doc 3 section IV: rule "does not
apply" to entry level, void enlistments "not impacted", dropped from the rolls "favorably impacted"); a local closed-book probe
missed (OTH + special-court-martial BCD); checked (tested_sha256 3c537469...). Difficulty Run 1 (Version f1d195): Low 0/5 ·
Medium 2/5 · High —, closed-book "Needed the documents ✓", but the gate failed "A marked document may not be needed": the high model
without Doc 5 assumed uncharacterized separations are less than honorable; Medium 3/5 answered OTH and BCD only. Fix handed over: the
page's one-line reviewer note for Doc 5 (no content change, keeps the Medium-band count). After the note the page read "That allows
submit, but an admin must sign it off (waive the check for this content) before the task can be approved" and "+$20 Medium+ bonus if
accepted"; the user submitted it the same day (status submitted, accepted_tier: Medium Tier; admin waiver and acceptance pending; later
observations in tasks/aq-02501/notes/feedback-q01.md). The reviewer sent it back on 2026-10-10 ("Only document 3 is necessary. Ensure at least two docs are
necessary for the solver to get the "gold answer"."): the note was not accepted. Rev 2 keeps the first ask word for word and adds a
second ask only Doc 5 answers (the board's discharge-date eligibility test, December 20, 2019; 34 words, asks 2; checked,
tested_sha256 e0593b76...). Run 2 (Version 432875): "In band — Medium tier", Low 0/5 · Medium 1/5, both documents "Needed ✓";
resubmitted 2026-10-10 (status submitted, accepted_tier: Medium Tier; reviewer outcome pending in notes/feedback-q01.md).

Same Medium target for aq-02564 (user, 2026-10-09: "let's work on AQ-02564_2026-10-09_1808. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; the capture itself showed "Hard 0/2 · Medium 0/3 · Easy
0/1", user statement followed): seven "broker" Federal Register texts (FTC Mobilewalla and Gravy consent-order notices, FMCSA
broker financial-responsibility extension, CFPB payment-data RFI, SEC notices of Cboe EDGX's and BYX's Small Retail Broker
Hosted Solutions Programs, EOIR IMBRA interim final rule). Only the EDGX/BYX pair carries a fair cross-document numeric: the
notices are word-for-word parallel and differ only in Top-feed figures (EDGX $750 Distribution Fee, $750 set fee, 0.10 per
user; BYX $250, $100, 0.025; Cboe One figures identical). FTC pair fails necessity (Ferguson's joint statement, reprinted in
both, cites both complaints' count paragraphs); D03, D04, D07 are single-document. q01 rev 0 = how much lower a hosted
subscriber's total monthly EDGX Top + BYX Top fees are under the hosted programs than the existing programs at 10,000
non-professional users, $1,400; decoy each notice's footnote 12 "maximum, savings" ($250 + $150 = $400, user fees only, the
waived Distribution Fee left out); checked (tested_sha256 d584a570...). i02 (host's bill with the per-firm user count,
$1,475) was the sibling alternative. Quick tests (user, same day: "q01, i02 too easy for quick test"): both too easy; q01
dropped, hooks h1/h2 closed (tasks/aq-02564/notes/feedback-index.md P1-P2). Round 2 i03 (a host with 2,000 users
whose only subscriber grows to 10,500 users loses its credit: the notices keep a host in only "so long as it has at
least one External Hosted Subscriber", and their example keeps it through "the other" subscriber) survived the quick
test (user 2026-10-10: "i03 survived"; P3). q02 rev 0 = the same wording with the host at 5,000 users, $1,625 (EDGX 750
+ 5,000 x 0.10, BYX 250 + 5,000 x 0.025), because 2,000 is printed in neither notice and the form's number check would
flag it; checked (tested_sha256 b9ad2a2a...). Difficulty Run 1 (Version be6014, 2026-10-10): "In band — Easy tier", Low
2/5, below the open tiers (user: "still easy tier ... need to level up to medium or high"). All five low attempts made the
eligibility inference; three left the host's user fees unpriced, two priced them from footnote 12; both documents needed,
closed-book missed. Rev 1 (one focused repair, tested_sha256 27f12de0...): the two notices applied as two programs: a host
with 5,000 users on each feed and two hosted subscribers, one on EDGX Top only (4,000 users), the other with 4,000 EDGX Top
and 10,500 BYX Top users; EDGX 5,000 x 0.10 + 750 + 750 = 2,000 (credit kept), BYX 250 + 5,000 x 0.025 = 375 (no BYX
hosted subscriber left), $2,375; wrong routes 2,125 (BYX credit kept) and 1,625 (second subscriber dropped from both);
checked. Difficulty Run 2 (Version 8ce393, 2026-10-10): "In band — Medium tier", Low 0/5 · Medium 3/5, "+$20 Medium+ bonus if
accepted"; the user submitted it at Medium the same day (status submitted, accepted_tier: Medium Tier; acceptance pending;
later observations in tasks/aq-02564/notes/feedback-q02.md). Low misses: $875 x3 (hosted subscribers' set fees left off the
host's bill), $1,750 (user fees unpriced), $2,125 (BYX credit kept); the declared scope trap ($1,625) caught no one.

Same Medium target for aq-02562 (user, 2026-10-09: "let's work on AQ-02562_2026-10-09_1751. there is no slot for Easy Tier
for this bundle, we should target medium and high. do your best."; the capture itself showed "Hard 0/2 · Medium 0/3 · Easy
0/1" and "Still open on this set: Hard, Medium, Easy", flagged once to the user; 9 submissions, 0 of 10 quick tests, 10 of 10
runs): seven unrelated Federal Register texts (FDA FOP research PRA 2023, USDA MASC NOFA Dec 2024, FNS grain-dessert/high-
protein-yogurt RFI Dec 2024, HHS Fall 2025 agenda, SNAP stocking NPRM Sep 2025, FNS fluid milk final rule May 2026, CCC ASCF
final rule Jun 2026). The caller (hooks n1-n12) and two independent question-author agents (A numeric, B rule/scope) each read
all seven texts and converged on one fair mechanism: MASC's (Doc 2) 75 percent farm-income exception to the $900,000 average-AGI
bar is absent from ASCF's (Doc 7) identical bar. q01 rev 0 (checked, platform pending; tested_sha256 9d38952d...): "What is the
most MASC and ASCF combined could pay a four-partner general partnership if one partner's average AGI exceeded $900,000, all
from farming?" = 4 x $125,000 + 3 x $250,000 = $1,250,000 (both caps exclude general partnerships and bind each partner);
traps $375,000 (partnership capped once) and $1,500,000 (exception carried into ASCF); with three partners a two-error route
would tie the gold. Quick-test sketches: i02 (single farmer, 70% crops + farmland rent, $125,000) and i03 (q01 with "all from
renting out farmland", the focused repair if q01 is too easy). CNP quantities (D03/D06) were rejected as public CFR text.
Rev 0 quick test (user, same day): "q01 too easy for quick test": the easier solver handled per-partner caps plus the asymmetry
when every decisive rule was keyword-reachable from the question ("general partnership", "$900,000", and "all from farming"
settling the exception in its own sentence). Rev 1 (6b96b593..., checked, platform pending), the one focused repair: "...70 percent
from crops and the rest from selling seed to farmers?" (33 words), so D02's definitions decide the exception (crops clear the
66.66% gate for production inputs, which include seeds; farm income 100%); gold unchanged, new trap $1,125,000 (crops only).
A second too-easy result retires the family. Rev 1 difficulty Run 1 (2026-10-10, Version 9f31eb): "In band — Hard tier", Low 0/5 ·
Medium 0/5 · High 1/5, "Your question measures Hard, and a Hard slot is open for it"; 13 of 15 attempts answered $1,500,000
(exception carried into ASCF; the high model argued D07's "as determined in accordance with 7 CFR part 1400, subpart F" imports
it), shown as the non-blocking "may be too vague" advisory; gold kept (D07 prints no exception, D02 does); only one attempt
took the crops-only $1,125,000. Submit then refused failure mode "Look-alike measure" for that crops-only route ("not a
similar-metric confusion where a solver takes a sibling line item"); the modes were cut to the measured "Wrong jurisdiction or
scope / Misapplies a rule or premise" (outside the fingerprint, no new run). Submitted 2026-10-10 after the paste (user:
"accepted after pasting"): status submitted, accepted_tier: Hard Tier; file frozen.

## Evidence and history

- 2026-10-05: user requests review of D:\Docket_new and adoption of good points. Imported
staged hook/sketch/promote workflow, applicable lever tests, independent calculations and set
review. Source workflow's older trial quota, word minimum, fixed test budget and added writing
kit are context-specific; current platform form/guide still governs.

- 2026-10-05, latest user: the current agent fails even the easiest level, requests an entire
  redesign, and requires at least one level, at minimum Easy. This supersedes the 2026-10-04
  maximum-only target without relaxing the platform's quality rules.
- Prior aq-00745 q01: Low 5/5 solved a direct semantic status filter despite longer derivations.
  Trial-03 q04 and trial-07 q05 were locally rated maximum but solved on the platform. No stored
  positive result calibrates the old gate or the redesign.
- New checks cover exact form/corpus hashes, distinct matching solver IDs, shortcut audit,
  source provenance and explicit verdicts. Historical replay rejects the two structured saved
  platform failures. This validates bookkeeping behavior, not future model performance.
- 2026-10-05: first positive platform result under the redesign. aq-00964 q01 rev 0 was "In band
  — Medium tier" (Low 0/5 · Medium 1/5 · High —; "The difficulty check passes on the current
  content"), meeting the Easy minimum. Mechanism: a dated event reported in the latest release
  selects the previous outlook edition, with the same release's later outlook as the decoy. Local
  review had rated it easy (marginal). See [[docket-local-solver-calibration]].
- 2026-10-06: aq-00998 q03 rev 1 platform difficulty check "Too easy" (Low 5/5; page text: "Ready
  when 1–3 attempts at a level are right, out of up to 5"), and q01/q02/q04 failed the quick test
  (user report). All four had two Opus matches, closed-book misses, clear audits and local "easy
  (marginal)" reviews. A plainly dated event bridge into labelled figures is not an Easy question
  for this platform. See [[docket-local-solver-calibration]].
- 2026-10-06: aq-00745 q01 passed at Easy ("In band — Easy tier", Low 1/5), but the user said the
  bundle has no Easy slot; target Medium for further aq-00745 work.
- 2026-10-06: aq-00745 q09 rev 1 passed at the High tier (user report: "great! you passed as a
  High tier."), above the bundle's Medium requirement. Untied single edition trap; see
  [[docket-local-solver-calibration]].
- 2026-10-06: aq-01320 (user: "difficulty_target to at least medium"; page slots Hard 0/2 · Medium 0/3 ·
  Easy 0/1). q01 rev 2 (Darden outlook edition in force at the Q4 start) measured Easy (user report "Easy
  Tier"), below the target; the user then had it accepted (2026-10-07, "accepted"), filling the Easy slot.
  See [[docket-local-solver-calibration]].
- 2026-10-06: aq-01430 (user: "work on AQ-01430_2026-10-06_1949 ... difficulty_target to at least
  medium"; slots Hard 0/2 · Medium 0/3 · Easy 0/1): new bundle, difficulty_target medium. Two checked
  write-ups were reviewed Easy (Medium about 7-12%) and handed over for quick tests; the bundle's Easy
  slot is open, so an Easy pass is usable there if the user accepts it. See
  [[docket-local-solver-calibration]].
- 2026-10-07: aq-01430 q01 submitted at the Easy tier (user: "set q01 status as submitted and
  accepted_tier as Easy Tier"), filling the bundle's Easy slot; the Medium slots remain open (q02
  checked and reviewed Easy-leaning; d02 a screened sketch).
- 2026-10-07: aq-01333 (target medium, user 2026-10-06 "at least medium") q01 rev 4 passed at the Easy tier
  and the user submitted it ("set q01 status as submitted and accepted_tier as Easy Tier"), below the
  stated target by the user's own decision. Earlier runs on the bundle: q02 Too easy, q01 rev 1 Answer
  not supported, q01 rev 2 Too easy. Medium 0/3 and Hard 0/2 slots remain open per the capture.
  The platform reviewer then returned q01 ("Revision requested", 2026-10-07): Doc 5 (the decoy release,
  ticked as "Exclusion / condition source") was not necessary. Rev 5 unticks it and leaves the question
  unchanged. Resubmission is pending.
- 2026-10-08: aq-docket-trial-06 (user: "there is no slot for Easy Tier for this bundle, we should target medium
  and high. do you best."): target medium. Rebuilt from the 2026-10-06 capture. Two independent authors again found
  no other cross-document Medium mechanism. Two candidates were handed over, both checked (v3 preflight) with the
  platform pending. q01 rev 1 is a set bridge (Doc 5's interviewed states) into Doc 2's site-visit de-duplication,
  40.5%; its rev 0 independent review said "easy". q02 is the 2026-10-06 credit-union remainder design (2,361),
  restored with its bound records. Only one practice submission is allowed.
