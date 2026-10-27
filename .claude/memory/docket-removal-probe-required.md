---
name: docket-removal-probe-required
description: "User, 2026-10-08: check the platform's Document check before hand-over: one removal probe per marked document (unforced answer must not be the gold); a closed-book reach fails every document"
metadata:
  type: feedback
---

User instruction (2026-10-08), with a screenshot of aq-00949 q07's difficulty check Run 5 ("A marked
document may not be needed ... without documents 3 and 7"): "check this, recently I occured several
times with your task. when build task, you need to check that gate. can you understand what I mean?"

The gate is the difficulty check's Document check: "The high model answers with every document, then
once with each document you marked necessary left out. A document is needed when the answer without it
is wrong, or changes from the every-document answer ... Reaching the same answer without it means that
document is not needed." When it fires, the gate does not pass whatever the tier counts, and the run is
spent (a result is final for its version).

**Why:**
- It fired on aq-00998 q05 rev 3 (2026-10-06: Doc 11's rounded 5.4% at face value replaced Doc 10) and on
  aq-00949 q07 (2026-10-08: both documents, through recall, inference from the other document and an
  assumed unchanged dividend). The user reports more cases.
- In both, the local Necessity bullet named the risk, but no probe measured it. "No other document prints
  this fact" is not the platform's test. The platform asks whether a strong model still lands on the
  gold without the document, by recall, inference, assumption, a rounded figure or a lazy heuristic.

**How to apply:**
- Before any hand-over, and before suggesting a platform run, run one removal probe per ticked document
  at the current fingerprint. Do it at sketch time too for any document whose only input looks
  recallable, guessable or rebuildable. A question is not `checked` until every probe is recorded.
- Probe: a fresh blind-solver on a copy of a prepared packet without that one document. Renumber the
  ids and manifest contiguously and use neutral folder names; up to three probes fit in one bound run as
  solver-1, solver-2 and shortcut (see [[docket-concurrent-sessions]]). Rename the docs/ originals too:
  court-docket names like uscourts_..._0/_1/_2/_4/_6/_8 let a probe without _10 infer "a later filing
  is missing" (aq-01541, 2026-10-08; it still answered "not answerable", so no harm that time). Give it the verbatim question
  only. Ask for the answer it would give (it may say it cannot be determined), then a forced best guess
  with its probability.
- The probe fails (gate Q2) when the unforced answer equals the gold at the stated precision, counting
  equivalent forms. Fix the question (precision, anchor, a document-specific fact) or the ticked
  documents, then probe again. A forced guess on the gold reached only by recall is a recorded risk: fix
  it when a fair change exists, otherwise state it at hand-over. A forced guess reached by inference from
  the remaining documents is a FAIL, not a risk (see Calibration; aq-01432 q04 was mislogged as a risk
  and dropped on review).
- A closed-book reach fails the probe for every marked document. Do not spend probes; fix or drop.
- Calibration: the blind-solver role is told to state missing facts rather than fill gaps from memory,
  so its unforced answer is more cautious than the platform's high model, which reached q07's gold
  without either document. Weigh a forced guess by its source. A gold reached by inference from the
  remaining documents is a FAIL even when forced; q06 without Doc 3 reached it unforced with high
  confidence. A gold reached only by recalling exact pre-cutoff figures is a stated risk: q05 without
  Doc 1 forced 22.7 at p 0.4, while the platform passed q04 rev 2 with the same Doc 1 dependence and
  no Doc 1 flag, a provisional report.
- Record each probe in `## Blind solve` without an `outcome:` field (the floor's parser skips such
  lines): `- DATE | rev: N | removal probe | tested_sha256: HASH | left_out: Doc N (Dnn) | result:
  misses|reaches|guess-reaches | forced_guess: <answer, p> | packet: <run/folder> | answer: <unforced>`
  (typed fields before the free-text answer). Keep the raw return under the run's results/.
- Tool gap (2026-10-08): the floor does not require these records and docket_agent.py has no
  removal-packet builder, so packets are still built by hand.
- Design against recall, not only check for it: when an input is a public statistic or another country's rule,
  make the answer need the exact document values of the least-remembered item. Probes remember directions
  (which nations' smoking rates fell) far better than values, so a direction-only filter is guess-reached while an
  exact-value result on the same inputs misses (aq-02157: q03 dropped at p 0.8; q01 rev 1's gap missed). A
  bridge that maps a country to a method (the Dutch ingredient list, Finland's characterising-flavour ban) is
  world knowledge, so the document carrying it is not necessary (aq-02157 q02, p 0.65).
- Related: [[docket-series-editions-necessity]] (mechanisms that defeat necessity),
  [[docket-general-knowledge-check]] (recall), reference/question-gate.md Q2.

## Evidence and history

- 2026-10-08, aq-01333 q01 rev 5 (an edition trap; Doc 4 and Doc 6 ticked), probed before the whole-form
  re-hand-over in one bound run (q01-r5-alt-h3). Without Doc 4: 61.7%, forced p 0.55 (the December range, after
  inferring that a March release was missing). Without Doc 6: not answerable, forced 41.7% at p 0.2. Both miss.
  The Doc 4 probe listed the gold's 2.40 midpoint as "illustrative only, not facts". A sensitivity line that
  happens to hit the gold is not a reach, but it shows the residual risk: a model that assumes a small raise
  lands on the gold. Local evidence only.
- 2026-10-08, aq-00949, first probes under this rule, run when the user asked which question to try.
  q06 without Doc 3: $0.94 unforced (agreement quarter inferred from the supplements' first Encino
  costs), so q06 was dropped before any run. q06 without Doc 7: not answerable. q05 without Doc 1:
  "not answerable", forced 22.7 at p 0.4 from recall. q05 without Doc 7: not answerable. Four probes
  in two bound runs (q05-r1-alt-c8, q06-r0-alt-j2), no peer run evicted. Local evidence only.
- 2026-10-08, aq-00949 round 6 sketch screens (i12-i14, leverage-ratio reasoning). Without Doc 1 or Doc
  3, all three probes said "not answerable" unforced, then forced the gold from memory: EOG's end-2019
  net debt 3,147, equity 21,641 and debt 5,175 at p 0.6, and the Encino "$3.5 billion of debt" at
  p 0.75. The local model recalls these exactly, so any design that leans on D01 or D03 numbers keeps
  a stated recall risk. Caveat: subagents see the harness git status. After the round-1 archive move it
  listed deleted run paths, including the removed document's file name, so a probe can tell that the
  document exists. That makes local probes more conservative, not less. Local evidence only.
- 2026-10-08, aq-01431 q01 (Justice Department letter's file numbers vs a narrative trio; gold 84.3). Two
  fresh probes on byte-identical packets without Doc 4 both said "cannot be determined" unforced, but one
  forced the gold from memory (S7-29-22 = Rule 605, Jan. 20, 2023) at p 0.6 and the other forced the decoy
  91.7 at p 0.6 with the gold as a recalled runner-up (0.25). Forced guesses on the same packet vary by
  run, so one probe bounds a recall risk only loosely; record each run and state the higher reading.
  Local evidence only.
- 2026-10-08, aq-01432 q04: UK fake-review services judged by the FTC staff reading of the US reviews rule, with
  Doc 2 the staff Q&A. Two probe runs on the byte-identical packet without Doc 2 disagreed:
  - rev 0 forced the two-item list at p 0.5, with the gold at 0.3;
  - rev 1 forced the gold at p 0.5, inferring from the rule's own "sell" that a fake-review broker sells reviews.
  Staff's broker answer (Doc 2 L63) only restates what the rule text implies. The caller first logged the rev 1
  reach as a stated risk; the delta review applied the inference rule above, and q04 was dropped before any
  platform run. Design lesson: a staff or guidance document is reliably necessary only when it decides an item
  against or beyond the literal rule text, as in q02 (staff say paying to change a negative review is not
  prohibited by the rule, although the rule's wording seems to catch it). Local evidence only.
- 2026-10-08, aq-01539 q01 (a count derived from the transfer order, Doc 1; Doc 3 only identifies which defendant's
  consolidation district is meant). The bridge wording decided the Doc 3 probe. With Kroll, the settlement administrator
  named only in Doc 3, two probes without Doc 3 said "not answerable" but forced the gold at p 0.55 and 0.45 by
  elimination: Doc 1 names only two consolidations (Advance Auto, Snowflake) and Snowflake never settles in the bundle.
  Closed-book runs also tied Kroll to AT&T's real-world settlement, a description-uniqueness risk outside the bundle.
  With Doc 3's California Settlement Subclass as the bridge (rev 1), the probe forced the decoy (Montana's 12) at p 0.72
  and never tried the derivation: without Doc 3, "California" pointed to Snowflake's California class members. Lesson:
  when a "Used to identify" document picks one of two candidates another document names together, choose an identifying
  fact that, without the document, points toward the decoy candidate rather than one elimination settles. Local only.
- 2026-10-08, aq-docket-trial-06 (six unrelated GAO reports): a bridge that names one entity leaks by design intent when
  that entity is the only candidate where the trap changes the answer. Doc 5 picked California (by its bank regulator's
  $2.20-per-$1,000 cap) for a Doc 2 count where only California's table note turns 21 sites into 17 credit unions. Four
  probes without Doc 5 said "cannot be determined" but forced the gold at p 0.4, 0.3, about 0.25 and 0.2. The cue "at
  least one visit" pointed at the states with repeat-visit notes. Naming the regulator a "Department of Financial
  Institutions" let a probe recall that California had one. With neither, the probe still reasoned that "California is
  the one state where counting credit unions instead of sites changes the result". Fix that held: let the bridge define
  a set that includes a member the trap never touches. Doc 5's six interviewed states contain California and Idaho, and
  Idaho's 20 unvisited credit unions sit in the base (17/42). Probes without Doc 5 then forced 77.3% (p 0.15) and 27.7%
  (p 0.08-0.10); California plus Idaho was not among their listed alternatives. Local only; platform result pending.

- 2026-10-08, aq-02157 (UK smokefree generation and pack-insert papers), probes for a concrete recall concern, 9 probes in 5 bound runs.
  q02 (Netherlands' flavour method but not Finland's, 6.1%): without Doc 1 the probe supplied the mapping from memory and
  forced the gold at p 0.65; dropped. q01 rev 0 (first nation to reach 5% repeating each 2021-22 change, 2032, Scotland):
  forced from remembered ONS rates at p 0.5 (no Doc 3) and 0.2 (no Doc 1). Rev 1 (2030 highest-lowest gap, 8.9) turns on
  NI's small rise: no Doc 3 forced 7.4 (NI 2021 remembered as 14.1, earlier 14.3); no Doc 1 forced the gold at p 0.1 while
  another run remembered NI 2022 as 14.5, so recall of the decisive values varies by run. q03 (highest support among nations
  whose rate fell, 65.5%): forced at p 0.8 and 0.45 from remembered directions; dropped. q04 (minimum duty per 20-pack, IA
  October 2021 MET to the response's £8.46, 21.6%): no Doc 4 forced 7.5% (assumed 2023 rates, named the gold as the pre-March
  2023 alternative); no Doc 2 answered 13.1% from the consultation's £7.87. Local evidence only.
- 2026-10-09, aq-02208 q01: the probe without Doc 2 answered "None" at p 0.8 from Doc 4's own account of its changes, and the
  caller declared that as a third trap; with both documents present the easier solver diffed the lists and the quick test
  came back "too easy". A probe's answer without a document measures necessity only; it is no evidence that a decoy catches
  solvers holding that document. q01's two probe rounds were also spent before its free quick test removed it.
- 2026-10-08, aq-02220 (heat network zoning papers), five probes. q02 (cost of the methodology stages central government
  leads in the consultation's private-sector-led model, £9.5 million from the IA's Table 6) failed: without Doc 1, the only
  source of the model's stage roles, the probe still answered the gold unforced, inferring central leadership of local
  refinement from the 2022 response's summary ("did not consider the central authority should play a role in ... the local
  refinement (1b)") and the question's plural "stages"; dropped. A response that summarises respondents' views on each
  model can stand in for the consultation's role table. q01 (Doc 4 benchmark x Doc 2 efficiencies) and q03 (Doc 4 share x
  Doc 2 demand) missed on every document (32.7%, not answerable; 31.2, 80.0). Whole-percent precision on q01 would have let
  textbook efficiencies (COP 3, 80% boiler) round to the gold without Doc 2, so it moved to one decimal. Local evidence only.
- 2026-10-09, aq-02408 q01 (Calpine-owned capacity divested in DOJ's relevant markets that hold a coal plant EPA's coal-ash
  proposal covers; Doc 4 only decides which of two named markets qualifies). Without Doc 4 the probe said "not answerable"
  but forced the gold (660) at p 0.4: the question's "Calpine-owned" matters only where ownership is partial (Gregory, in
  ERCOT), the nearest-10 precision is robust only for ERCOT, and it remembered that coastal mid-Atlantic PJM has few coal
  plants. A document whose sole role is a filter between named options is guessable whenever the qualifying option is the a
  priori likely one, and wording that exists for fairness can point at it. Without Doc 5: forced 5,390 at p 0.01 (it
  recalled the divested plant names but not their sizes). Mitigation chosen: "Exclusion / condition source" plus reviewer
  note; the alternative is a design where the filter document also supplies a number. Local evidence only.
- 2026-10-09, aq-02486 q01 (ONCD's proposed FOIA charge minus the Access Board's for 225 photocopies, $12.50; the gold
  turns on the Access Board's "$25.00 or less, no fee" rule, which is DOJ-template wording also printed by the Peace Corps
  in the bundle). Without Doc 7 the probe said "not answerable" and forced the gold at p 0.25 by assuming the template
  rule at an unknown rate, listing -12.50 as an equal alternative; it did not borrow the Peace Corps text. Without Doc 5,
  "not answerable", forced gold p 0.15 from a generic rate guess. Template-standard rule text shared across agencies is a
  forced-guess risk here, not an unforced reach; contrast a rule printed word for word for another agency in the bundle
  (FLRA's quarter-hour sentence for the Peace Corps' sketch i04), which risks the inference FAIL pattern (not yet probed).
  Local evidence only.
- 2026-10-09, aq-02505 q01 (growth of the UFLPA Entity List from the November 1, 2024 version, backed out of Doc 2 as
  107 - 29 = 78 because one of the update's 30 named additions was already listed, to Doc 6's August 2026 count of 187,
  139.7%). Without Doc 2 the probe said "not answerable" (it rebuilt November 25's 107 from Doc 4 but found no November 1
  count) and forced the gold at p 0.3 from memory: it recalled the late-2024 revision "taking the list from 78 to 107",
  with the firms' sector misremembered. DHS entity-list totals of 2024-early 2025 are recalled; a base built from them
  keeps a stated Document-check risk, while the post-cutoff end count needs no probe. Local evidence only.
  Platform follow-up (three difficulty runs, 2026-10-09/10): the Document check found Doc 2 needed every time (78.1% or an
  unfinished answer without it), so the local forced-guess reach did not predict a platform reach.
- 2026-10-10, aq-02505 q02 (copper entities first placed Nov 25, 2024 - Aug 3, 2026; one member per notice). Without Doc 2:
  "not answerable in full" (Ashele's first-listing date and the November 25 additions unknown), forced gold p 0.4 from
  recalled November 2024 additions. Without Doc 4: "not answerable as a complete list", forced three names without Zijin
  at p 0.55, gold a p 0.3 runner-up from memory that Zijin mines copper. A member whose qualifying attribute is famous
  (Zijin and copper) is a recall risk even when its listing date needs the documents. Local evidence only.
- 2026-10-10, aq-02770 q01 (lowest TE2 for a gas-fired commercial furnace at the federal minimum; base from Doc 2's
  standards by manufacture date, estimates and NEEA's share from Doc 4). Rev 0 dated the furnace "built in 2022":
  without Doc 2 the probe said "not answerable" (the 81 percent level's compliance date is in no other document) and
  forced the gold at p 0.65 from memory ("81 percent applies to units manufactured from January 1, 2023"). A codified
  compliance date is recalled even when the documents around it are obscure. Rev 1 dated the furnace by an event only
  Doc 2 reports, "the day DOE published its final determination not to amend" the standards, with no year in the
  question: the probe again said "not answerable" and its forced guess became 77.0, the wrong-year trap answer, at p
  0.75 "by inference from the documents". Fair change for a recallable date rule: have the question date the item
  through an event that only the ticked document reports, so the document must supply both the date and the rule.
  Check that every reading of the event's date other than the gold's (here the effective date a month later) falls
  on the trap side. Local evidence only; platform result pending.
