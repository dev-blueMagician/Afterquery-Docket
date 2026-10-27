# q03 rev 0 independent review (fresh question-review agent, 2026-10-08)

tested_sha256: 66f37c0d6a1f00265f764dac0175fda28dc35ba2d369a1b43db135c37e26a4f2
Inputs: question file, snapshot, corpus, all raw returns (A, B, audit, closed-book, two removal probes), floor; caller's five adjudication points.

Raw return:

q03 (rev 0; tested_sha256: 66f37c0d6a1f00265f764dac0175fda28dc35ba2d369a1b43db135c37e26a4f2)

gold_verified: yes. I rebuilt the full candidate universe from the passages. Four defendants in the bundle asked for FNC dismissal: Royal Caribbean (D04 l.35, dismissed on FNC itself at l.121, so out), Ofcom (D03 l.97 and fn 3 l.218; complaint dismissed for lack of subject-matter jurisdiction at l.250, so in), OEC India (D07; FNC denied at l.451 and Counts I-VIII survive at l.455, so out) and OEC USA (co-movant per l.25, l.83, l.210, l.278; dismissed under Rule 12(b)(2) at l.204 and l.449, so in). Nobody else qualifies: D06 moved to transfer and nobody was dismissed; D08's JLF moved to transfer in 2023; D01, D05 and D08 only cite FNC precedent or record a waiver; D02 records no FNC request. All six evidence quotes are verbatim and unique in text/ and docs/ (104-157 characters), with correct locations. Floor: 0 FAIL, 1 WARN (origin). The report matches the fingerprint and shows no source gaps.

outcome: A: match; B: match. Both were fresh, distinct packets, uncontaminated. Each named the "OEC India's request" reading and rejected it. Their raw confidence was "high for Ofcom; medium-high for OEC USA", but q03.md records "high" for both, so the records need correcting.

closed-book: misses. Answer "unknown", forced guess "none" at p 0.05. Not equivalent to the gold.

necessity: D03 (Doc 7) is the only source for Ofcom's FNC request and its immunity dismissal; Ofcom has 75 mentions there and none anywhere else. The probe without it gave "OEC USA" (forced p 0.5): a miss. D07 (Doc 1) is the only source for OEC USA's joint motion and its 12(b)(2) dismissal; OEC has 96 mentions there and none elsewhere. The probe without it gave "Ofcom" (forced p 0.45): a miss. No smaller set works and nothing can substitute. Each document stays needed even if the every-document answer were "Ofcom". D04 correctly carries no role.

shortcut: clear. Shortest route: search "forum non conveniens", which hits all eight documents. D03 l.97 plus l.250 gives Ofcom; D07 l.83, l.210 and l.25 plus l.449 gives OEC USA. No passage and no overview summary gives both. Difficulty risk: the term is the bundle's own title ("Forum Non Conveniens Federal Opinions") and the search surfaces every input.

source_assessment: no gaps. intake.json shows 8 of 8 complete with capture hashes matching, and the report's source_gaps list is empty (4f53cd...).

difficulty: easy. Local suitability for the Medium target is low; reasons under finding 3.

verdict: revise

failure_modes:
- FM1 (Look-alike company / Wrong members in a list): the trap is real. Treating OEC India as the only FNC requester recomputes to "Ofcom". The label is acceptable; "Document convention" (the conclusion relabels requests per surviving party) fits the mechanism slightly better. The cause fits. One claim is false: "Its forum non conveniens part speaks only of the Indian parent". Part III opens with "Defendants next argue..." (l.210) and closes with "Defendants' Motion is DENIED as to that issue" (l.278). As written, the box concedes the alternative reading. "Appears in that part only as already gone" is also imprecise: Part III's own text never names OEC USA, only footnote 6's spill-over at l.219 does. No local run took this answer. The box must state what the burden analysis, fn 10 and l.451 say against what l.83, l.210 and l.278 say.
- FM2 (Part vs total): the wrong answer recomputes ("Ofcom, OEC USA and OEC India"), but the question's own words "dismissed from the case" rule it out, so it fails Q15. No run produced it. "Both sentences put the word DISMISSED beside OEC India" is wrong: the second sentence names only claims. "Which movants" misquotes the question, which says "defendants". It also repeats q01 FM1's decoy and label. Withdraw it; FM1 alone has 246 words.

findings:

1. Adjudicating "Ofcom" alone:
   - It is a wrong-lever answer, not a second defensible answer. The words "had asked" are answered by l.25, l.83, l.210 and l.278.
   - The conclusion's "OEC India's request" (l.451) is a relabeling after OEC USA left (l.284). The same conclusion calls the jointly moved 12(b)(6) request "OEC India's request" (l.453). Yet the body says "Defendants' Motion is GRANTED as to this claim (Count IX)" (l.444), and l.83 has both defendants moving under 12(b)(6). The strict reading would therefore also deny OEC USA's 12(b)(6) request, which contradicts l.83.
   - The reading is still colorable to anyone who treats the disposition list as the record of who asked.
   - Risk estimates: platform reviewer return about 10%, rising to about 25% if the difficulty run attaches "may be too vague" with wrong answers clustered on "Ofcom" (the aq-01278 q02 path). Form block about 15-25%. The decoy is the court's own printed wording in its disposition list, the pattern behind the recorded blocks. Local matches do not predict blocks, and the independent author (ideas.md a01) flagged the same risk.
   - A wording change is not needed for fairness. If the free form check blocks it, any fix must make "asked" turn on the motion each defendant filed or joined, not on the ruling's later label. That points straight at the joint motion, makes FM1 a trap the wording rules out, and leaves two keyword finds: Too easy or Easy (the author's similar wording A: Medium 3-6%). With only Medium submittable, treat a block as a reason to drop rather than rewrite.
2. D02 exclusion is sound on the text. The ruling gives each disposition (l.564) and names other arguments (UAE, Alp, Vidino and Besson motions at l.516; Vidino's First Amendment point in fn 16). Its only FNC mention is the Azima citation (l.321). "A variety of grounds" (l.117) and "other legal grounds" (l.167) leave an unrecorded possibility, not a nameable candidate; all six runs excluded D02. Reviewer note risk about 3-5%. Step 3's "no defendant asked" (Doc 8) overstates: the text supports only "no such request is recorded". This is in the fingerprint and optional.
3. Difficulty estimate for the platform: Too easy 25-30%, Easy 50-55%, Medium 5-10%, Between levels about 5%, High at most 2%, Too hard or Answer not supported 3-5%.
   - Ofcom comes from one pair of passages (D03 l.97 and l.250).
   - OEC USA's co-movant status sits in the same search hits (l.83, l.210), so the trap only catches readers who rely on the conclusion.
   - The exclusions are tied: each fails in its own passage.
   - In calibration, one-hidden-member filters landed at Easy (aq-01433 q01, Low 2/5) or Too easy (aq-01432 q03, Low 5/5).
   - Before any difficulty run, use the free form check, then a quick test (0 of 10 used).
4. Evidence passes. Optional and inside the fingerprint (so prepare and all checks would need re-running): adding l.210 and l.278 would strengthen the record for a reviewer.
5. Set review (q01, q02, q03):
   - All three are two-defendant disposition filters with the same opening frame. Word-overlap ratios are 0.449 with q02 and 0.439 with q01; the longest shared run is 5 words. Expect the "Sibling question" and "Question mix" advisories.
   - OEC India's Count IX decoy appears as Part vs total in both q01 FM1 and q03 FM2. "Each trap once per task" may mean per bundle; withdrawing FM2 removes the repeat.
   - q02's reasoning (Step 3) states q03's crux: "Oriental Export Corporation and OEC USA sought forum non conveniens dismissal ... the court denied it" and "Ofcom raised forum non conveniens, but the court did not reach it". It also contradicts q03 Step 2's "never reached forum non conveniens for OEC USA". Make both match the text: FNC denied as to OEC India (l.451), and OEC USA dismissed under 12(b)(2).
   - None of the three question texts gives away another's answer. Each uses a different pair of documents.
6. Records outside the fingerprint: fix A and B's confidence; replace the stale "Removal probes: pending" in Lever checks.
7. Minor risks:
   - Step 2's "September 11, 2026" appears in D07 only as 09/11/26, a small risk for the form's number check.
   - "Eight federal rulings" counts the documents. The floor did not flag it, but it is a low rule-10 risk.
   - The token window fits: the capture shows 114,252 tokens before the question, and the cap is 115,000.
   - Unknown, platform-only: restricted names, "Not a duplicate", and the model checks.
8. Readiness: after the FM1 fix and FM2 withdrawal, q03 is at best checked; platform result pending. Nothing here establishes a tier.

Files: D:\Agents\Docket\tasks\aq-01540\questions\q03.md; D:\Agents\Docket\tasks\aq-01540\text\D07.txt; D:\Agents\Docket\tasks\aq-01540\notes\ideas.md (a01); D:\Agents\Docket\tasks\aq-01540\questions\q02.md (Step 3).

Caller note: q02's Step 3 sentence on Oriental Export Corporation and OEC USA was already corrected in q02 rev 2 before this review returned (the reviewer read the rev 1 text).
