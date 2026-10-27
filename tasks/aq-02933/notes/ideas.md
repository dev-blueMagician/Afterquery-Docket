# aq-02933 - lean candidate sketches

Current target: medium (user, 2026-10-11: no Easy slot on this bundle; Medium and Hard open).
Measured platform success pending for every candidate. Origin of all sketches: claude.
Doc N = task-page numbers; D05 = Doc 6 (HHA), D06 = Doc 5 (hospice).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| i03 | [sketches/i03.md](sketches/i03.md) | h1: Doc 6's shared-address HHA States against Doc 5's Table 1 States; combined hospice growth for Nevada and Texas, 57.7% | Competing: California (Doc 5's "single building" remark is about hospices) 98.5; Texas alone (Doc 6's later partial mention) 50.6; average of printed 151 and 51 = 101.0; all fail "home health agencies" or "combined count". Doc 6 alone fixes the State set; Doc 5 alone has the counts. Screen: eligible, no warnings. | promoted to q01 (rev 0); untested. Held as the alternate of q04 after q03's run: its filter starts from the table's own States, the direction the low model handled five times in five |
| i02 | [sketches/i02.md](sketches/i02.md) | h2: six-month would-be entrants, Doc 3's printed 300 plus half of Doc 5's 166 per year, 383 | Competing: 466 (two parentheticals), 800 (three-year total), 766 (both yearly); each fails "six months". Each pace is in one document only. Screen: eligible; all inputs past character 22,000 (form number check may flag them). | promoted to q02 (rev 0) |
| i01 | [sketches/i01.md](sketches/i01.md) | h3: Texas's yearly hospice gain against its yearly HHA loss, 144.8% | Competing: 96.5 (raw changes, spans ignored) fails "average yearly". Each count pair is in one document only. Screen: eligible; footnote 23 at character 36,942. | held: alternate to q01 only (shares Texas's hospice counts); quick-test line available |
| i11 | [sketches/i11.md](sketches/i11.md) | h10: States with enrolled totals for both 2019 and 2025; HHAs lost (Michigan, Texas) 500 against hospices gained (Georgia, Nevada) 185, gap 315 | Competing: 398 (Nevada from its printed CY 2023 pair) fails "From 2019"; 448 (Nevada omitted) fails because both its totals are reported; -48 (Texas hospices) fails "both years". Universe: every 2019 and 2025 mention in Docs 3, 5, 6 read. Each side's totals are in one document only. Screen: eligible; seven inputs past character 36,000. | promoted to q03 (rev 0). Difficulty Run 1, 2026-10-11: "In band — Easy tier", Low 1/5 (four attempts 367, Georgia left out; Nevada built correctly by all five). Below target, not going forward at Medium |
| i12 | independent author's return (not saved as a sketch file) | h11: medical supply revocation rate over the top of the general range, 17 / 3 = 5.7 | Competing: 3 ("nearly triple", other DMEPOS types), 6.0 (hospices' 18 percent). Range is "about 1 to 3 percent", so one decimal rests on a rounded input. | held: two lookups and one division; quick-test line only if wanted |
| i21 | [sketches/i21.md](sketches/i21.md) | h13: States with a 2019 hospice total (Table 1's four plus Georgia in prose) minus those Doc 6 names for HHAs sharing an address (Texas, Nevada); 152 + 1,130 + 221 = 1,503 | Competing: 1,282 (Georgia missed), 1,558 (Texas alone excluded), 2,276 (no exclusion), 373 (California excluded on Doc 5's hospice remark). Doc 5 alone has the totals; Doc 6 alone names Texas and Nevada. Screen: eligible; 221 at character 45,920. | promoted to q04 (rev 0), written after q03's Run 1. Rev 0 failed the form's "One defensible answer" check on California's status (2026-10-11); rev 1 leaves California out and asks the named States' share, 773 / 1,146 = 67.45%. Rev 1 difficulty Run 2 (2026-10-11): "Too hard", 0 of 15, every attempt 83.57% (Table 1 only). Rev 2 adds "tabulated or only in text": difficulty Run 3 (2026-10-11) "In band — Easy tier", Low 3/5. Hook retired at Medium |
| i31 | [sketches/i31.md](sketches/i31.md) | h14: across the three notices' lists of cited fraud cases (about 35, prose only), those with a prison sentence dated 2024: 3 + 4 + 1 = 8 | Competing: 10 (a 2024 guilty verdict and a 2024 conviction counted, or defendants counted), 9 (an undated co-defendant), 18 (every sentence), 14 (every 2024 case). Each notice holds its own cases; removing one gives 5, 4 or 7. Screen: eligible. | promoted to q05; rev 0 (2024 only, 8 cases) never run; rev 1 (2026-10-12) widens to 2024 or 2025, 13 cases (3 + 5 + 5; decoys 15, 18, 8, 12); quick test "too easy" (user chat, 2026-10-12, one draw, no trace); dropped |

Hooks not sketched and why: notes/hooks.md (h4 soft round figures; h5 application counts, tangled
and a shape measured too easy; h6 two lookups; h7 Doc 3 replaceable; h8 public State list; h9 Docs
1-2 not connected by the documents).

Round 1 (2026-10-11): five sketches (i01-i03 by the caller, i11-i12 from the independent author),
three promoted (q01, q02, q03). The independent author (question-author, fresh context, told only
that the caller held a Texas projection and a six-month entrant sum) reported that, working from the
sources alone, its first-choice hook was h1 with the same figures as q01 (773 to 1,219, 57.70%;
98.53 with California; 98.98 for all four; 101.0 from the printed percentages) and no further
competing reading. It then opened notes/ to check for duplicates, so its agreement on h4-h8 is not
independent. It predicted no tier.

Round 2 (2026-10-11, after q03's difficulty Run 1): one new sketch, i21, promoted to q04. It reuses
the one step that separated the low attempts on q03 (a member printed only in prose) and adds the
Doc 6 exclusion as a second, independent membership step. No wording repair was made to q03: every
ask on its four pairs turns on the same single step.

Round 3 (2026-10-11, after q04 rev 1's difficulty Run 2): q04 repaired once (rev 2, the counting rule stated) and one new sketch, i31, promoted to q05. Three sketch rounds are now used. What the two runs showed about this bundle: a step that asks which States a second document names is solved at every level; a member printed only in prose is found by nobody when a table fits the description (0 of 15) and by about one low attempt in five when no table does. q05 has no table at all and about 35 prose items.

After q04 rev 2's Run 3 (2026-10-12): the prose-member hook is closed (q03 Easy, q04 rev 1 Too hard, q04 rev 2 Easy). q05 is the one candidate left; it was widened before its first run so that a single thorough low attempt is less likely to clear it. If q05 also misses the open tiers, report that no fair Medium design is left and recommend release.

Outcome (2026-10-12): q05 quick-test too easy, dropped. Three sketch rounds used, seven candidates written or sketched (q01-q05, i01, i12), three difficulty runs and one quick test observed: Easy (q03), Too hard (q04 rev 1), Easy (q04 rev 2), quick-test too easy (q05). No fair Medium design found; release recommended. Unresolved avenue, not written up: a wording of q04 between rev 1 (no hint that text totals count, 0 of 15) and rev 2 ("tabulated or only in text", Low 3/5); it would be a third wording of one hook.

Update (2026-10-12): the user quick-tested the middle wording of q04 ("Wherever CMS gives a State's 2019 hospice total ...") and it survived (chat report, one draw, no trace). Written up at the user's request as q04 rev 3; gold 67.45% unchanged. Difficulty run pending. A miss of the open tiers ends this family and the bundle.

Update (2026-10-12, later): q04 rev 3 difficulty Run 4 "Between levels", Low 0/5, Medium 4/5. The medium attempts that succeeded all re-read Doc 5 because of the word "Wherever". Rev 4 is the half step back ("Across every State with a 2019 hospice total from CMS"); difficulty run pending. Measured so far on this one sentence: no statement 0/0/0, "Wherever" 0/4, "tabulated or only in text" 3.

Update (2026-10-12, evening): q04 rev 4 was blocked by the form's "One defensible answer" check before any run (both solvers 83.57%). Rev 5 names the scope ("whose 2019 hospice total appears in CMS's hospice notice"); form Checks and difficulty run pending. Cue ladder so far: none 0/0/0; "every State ... from CMS" form block; "Wherever" Low 0, Medium 4; "tabulated or only in text" Low 3.

Update (2026-10-12, night): q04 rev 5 measured In band, Medium tier (Low 0/5, Medium 1/5; Run 5) and was submitted by the user. Routes and the retrospective are in notes/feedback-q04.md.

Round 4, Hard target (user: "see if you can still make a hard tier"): no write-up. Re-read for a second separator: the bundle's only item the stronger solvers missed in five runs is Georgia's prose total beside Table 1, and q04 uses it. Other late members carry no number that changes an answer (Ohio in the hospice oversight list and in both co-location passages; Nevada's 188 was assembled by all five low attempts on q03). Ohio's nested minimum (5 x 5 + 3 x 9 + 18 = 70 HHAs at nine addresses) is one-document: no other notice supplies a needed input. Scope-rule scenarios rest on hedged clauses ("generally", "typically") or on plain sentences. Not written: a second question deciding on Georgia's sentence (same answer path as the submitted q04). Untested on other passages: q02 (383, Docs 3 and 5) and sketch i01 (144.8, Texas per year); both are stated sentences plus arithmetic.
