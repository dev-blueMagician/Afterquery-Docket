# q02 rev 1 independent review (fresh question-review agent, 2026-10-08)

tested_sha256: 0a6b22bd46104415d02e061b28a62f2c1bb722c77676be7228ee03267f09a17b
Inputs: question file, snapshot, corpus, all rev 1 raw returns (A, B, audit, closed-book, two removal probes), rev 0 history, floor; caller's four adjudication points; a follow-up message pointing to the rev 0 probe file without D04.

Raw return:

q02 (rev 1; tested_sha256: 0a6b22bd46104415d02e061b28a62f2c1bb722c77676be7228ee03267f09a17b)

**gold_verified: yes.** I worked this out again from my own full reading of D01–D08.
- D04 l.15 and l.121–125: Royal Caribbean (RCCL) moved to dismiss under the Ticket Contract's forum clause. The motion was GRANTED, and the case was dismissed under forum non conveniens in favor of the Courts of England and Wales.
- D08 l.21 and l.42: Deaton's 2022 suit "against JLF Defendants" (defined as "Steven Johnson and his Law firm") was removed to federal court. The District of Rhode Island then transferred "this case" on the JLF motion "based on certain provisions within their engagement agreement with Moreno".
- Date check (script): all eight rulings fall in Sept 11–15, 2026. Some sit on the endpoints (Sept 11: D05, D06, D07; Sept 15: D02, D03), and the count "eight" forces the inclusive reading.
- Every other defendant fails the test:
  - DUAL, Chaucer and Houston: transfer denied (D06 l.14, l.173, l.260).
  - OEC India: forum non conveniens denied, and the request rested on Indian litigation, not a contract (D07 l.210, l.451).
  - OEC USA: dismissed under Rule 12(b)(2) (l.449).
  - OEC India's Section 13 ruling only caps damages (l.453).
  - Ofcom: dismissed under the FSIA; forum non conveniens never reached (D03 l.97).
  - UAE, Alp, Besson, Vidino: dismissed on immunity, jurisdiction or 12(b)(6) (D02 l.564).
  - Lewis Machining: settlement dismissal, and the same court keeps jurisdiction (D05 l.161).
  - Philadelphia: won on the merits; the only remand was the Fifth Circuit's own jurisdictional one (D01 l.99).
  - Norvell: made no motion.
  - D08's 2024 res judicata dismissal and 2026 arbitration denial involve only the JLF Defendants.

**Point 1 (the readings you asked about):**
- "ever" removes the narrow reading. Both rev 1 solvers get Royal Caribbean alone only by "ignoring 'ever'".
- Norvell is not defensible: the transfer motion is credited to "JLF Defendants" only, and the suit was filed against them.
- The engagement agreement with Moreno counts. The question says "a contract's terms", with no requirement that the contract be with the plaintiff, and the court granted the motion.
- Cited precedents are outside "the lawsuits that eight federal rulings decided": Turner, Lebedinsky, Aviation One, Azima, plus Atlantic Marine (D06) and Chick Kam Choo (D08 l.81).
- One weak alternative remains: if "in favor of another court" attached only to "transfer", Lewis Machining would come in. That parse makes the phrase redundant for "transfer", and all six solver and probe returns rejected it.

**outcome: A: match; B: match.** Both named Royal Caribbean plus the JLF Defendants with high confidence, from different packets, citing D04 l.15/121–125 and D08 l.21/42. Both rejected Norvell, DUAL, arbitration and the precedents. B says it cannot confirm how it was invoked, but its path comes from the documents and I saw no leakage.

**closed-book: misses.** It answered "unknown"; forced guess "none", p 0.15.

**necessity:**
- Royal Caribbean appears only in D04, and the Deaton/JLF transfer only in D08. Searching text/ and docs/ gives the same hits.
- I checked both rev 1 probe packets: the removed text is absent and the rev 1 question is verbatim.
  - Without D08: "cannot be determined"; forced guess Royal Caribbean alone, p 0.5.
  - Without D04: "cannot be determined"; forced guess JLF alone, p 0.55.
- No smaller source set works.

**shortcut: clear.** The shortest route is two searches:
- "forum-selection" finds D04 (granted) and D06 (denied).
- "transfer" or "venue" finds D08 l.42.

No passage holds both items. This is a difficulty risk, not a shortcut.

**source_assessment: no gaps.**
- Intake shows all eight documents complete (no gaps, every one matching the capture), and the capture says "8 of 8 read in full".
- D04 and D08 text match the originals byte for byte apart from the header line.
- Small character normalisations exist at D01 l.239, D06 l.120 and D07 l.156, 161, 200 and 268. None of these lines carries anything this question relies on: premises, gold, exclusions, uniqueness, necessity or the shortcut route.

**difficulty: easy.** Locally it is poorly suited to the Medium target.
- "ever" is needed for fairness, but it flags that an earlier event counts; the rev 1 probe without D08 said so explicitly.
- l.42 uses the question's own word "transfer". Doc 3 is short (6,285 tokens) and third of eight, so the item is neither late nor in the longest document.
- Royal Caribbean is the obvious item: the bundle is titled "Forum Non Conveniens Federal Opinions" and the Doc 5 overview names that dismissal.
- Each decoy is ruled out in its own passage, the trial-05 rulings pattern that reviewed Easy or Too easy.
- aq-01433's late, misspelled row was harder to find than this and still reached only Easy (Low 2/5). The independent author's estimate for this design (a02) was the low model right 60–70% of the time, Medium ≤5%.

**Point 3, my judgement for a difficulty run:** Too easy ~35%, Easy ~50%, Between levels ~6%, Medium ~5%, High ~1%, Too hard or Answer not supported ~3%.

**Point 2, form "One defensible answer" block:** about 5–10%.
- The main route is both form solvers leaving out JLF. That is an omission, not the printed look-alike figure behind the four recorded blocks, and aq-01433's omission trap cleared the form.
- Both adding DUAL (denied in D06's first paragraph) or Lewis Machining (weak parse): ≤2% each.

**verdict: revise**

**failure_modes:**
- **FM1** (Linking across documents / Wrong members in a list):
  - Real: D08 l.42 exists, and missing it gives "Royal Caribbean Cruises Ltd." alone (gold minus JLF, recomputed).
  - Every box claim checks out: page 3, no forum-selection or forum non conveniens words for this step, and the 2026 rulings are about injunctions and arbitration.
  - Not ruled out by the wording: "ever" fixes the reading error, not the search miss.
  - The cause fits. The trap label fits weakly, because nothing is linked across documents (l.21 and l.42 are both in Doc 3). "Older figure inside a newer report" (a 2023 event inside a 2026 opinion) fits better. Avoid "Out-of-range period", which "ever" already rules out.
  - No local attempt actually fell for it.
- **FM2** (Wrong jurisdiction or scope / Misapplies a rule or premise): the passage is real (D06 l.60, 65, 81, 173), but:
  - (a) The stated wrong answer, "Royal Caribbean Cruises Ltd. and DUAL North America", also assumes the FM1 miss. FM2 on its own gives Royal Caribbean, the JLF Defendants, DUAL, Chaucer and Houston.
  - (b) All three insurers filed the motion jointly (l.14), so DUAL alone is not the natural wrong answer.
  - (c) "with a court's agreement that the clause was enforceable" overstates it: l.81 records the parties' agreement, not the court's.
  - (d) The label fits weakly: the boxes describe a motion that was tried and denied, not a jurisdiction or scope error.
  - (e) No attempt produced it, and the denial is printed in D06's first paragraph.
- **Necessary documents roles:** the section is empty, so both ticked documents default to Answer component, which matches how each is used.

**findings:**
1. **Targeted failure modes (Q15):** FM2 points (a)–(d) and FM1's label, above. A platform reviewer could reject these claims. The section is outside the fingerprint, so correct FM2 or withdraw it (FM1 alone meets the 1–3 rule); no re-test is needed.
2. **Target (Q13):** difficulty is below Medium, and an Easy result is unusable here (4 submissions left, only Medium open). Quick-test before any difficulty run (0 of 10 quick tests used). I found no fair fix within this design that raises difficulty without bringing back the narrow reading.
3. **Lever record (Q11):** "Bury one list item late" is not active as the Guide defines it (last or longest document). The real mechanism is a low-profile background item. This is a record fix; check whether the front-matter levers field is fingerprinted.
4. **Reasoning step 3, Doc 1:** it says OEC USA sought forum non conveniens and "the court denied it". In fact the denial was as to OEC India (l.451), and OEC USA was dismissed under 12(b)(2) (l.449). OEC USA is still excluded, but the sentence is imprecise and that dismissal is exactly q03's gold. The reasoning is inside the fingerprint, so fix it only alongside another fingerprinted edit, then re-prepare.
5. **Set level:** q01, q02 and the new draft q03 share the same "eight federal rulings … which defendants, if any" frame. Wording similarity is 0.447 against q01 (a 6-token shared run) and 0.454 against q03. q02 and q03 also draw on the same forum-motion cases (D03, D04, D06, D07). Expect Sibling or Question mix warnings; vary them or pick one.
6. **Records:** Lever checks still says "Removal probes: pending" (stale). The evidence note "p. 11; l.121" should be page 12. notes/handover-q02.md has not been generated.
7. **Platform-only checks, unknown:** One defensible answer, Needs two or more documents, Original question (my local maximum against other tasks is 0.354), Not a duplicate, Restricted names, and the token window (the capture shows 114,252 of 115,000 before the question is added). The authorship tick is the user's to make (origin claude).
8. **Your correction:** the rev 0 probe without D04 (D:\Agents\Docket\tasks\aq-01540\runs\q01-r0-alt-n5\results\probe-q02-without-D04.md, saved 12:12) matches the result recorded in the question file. It is rev 0 history only.
9. **Fingerprint:** the report tool recomputes 0a6b22bd…, matching every rev 1 record and raw return. There is no platform record, so this is local readiness only, not observed platform survival.

Files reviewed: D:\Agents\Docket\tasks\aq-01540\questions\q02.md, D:\Agents\Docket\tasks\aq-01540\runs\q02-r1-v2-0a6b22bd46104415d02e061b28a62f2c1bb722c77676be7228ee03267f09a17b\results\, D:\Agents\Docket\tasks\aq-01540\runs\q02-r0-alt-c9\results\
