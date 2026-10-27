# q02 rev 2 independent review (same question-review agent as rev 1, continued by message, 2026-10-08)

tested_sha256: de27f6a2d7ad3d2fc2be3f0838a925089e7e2078585be2a4cba6db69f37ca500
Inputs: the caller's delta summary (rev 1 -> rev 2), question file, rev 2 snapshot, rev 2 raw returns (A, B, audit, closed-book, two removal probes), floor.

Raw return:

q02 (rev 2; tested_sha256: de27f6a2d7ad3d2fc2be3f0838a925089e7e2078585be2a4cba6db69f37ca500)

Rev 2 is locally ready, but it remains Easy-leaning, so it does not suit the Medium target; quick-test it before any difficulty run.

**gold_verified: yes.**
- The rev 1 and rev 2 snapshots differ only where you said: Step 3's Doc 1 sentence, the D04 l.121 page label (11 → 12) and the levers field. Question, answer, components, other evidence, corpus hashes and gap hash are all identical, so my rev 1 recomputation still holds: Royal Caribbean (D04 l.15, l.121–125) and Steven Johnson with his law firm (D08 l.21, l.42), with every other defendant failing.
- The new Step 3 sentence is accurate against D07:
  - Forum non conveniens was denied "as to OEC India's request" (l.451), and OEC India is Oriental Export Corporation (l.25).
  - The request rested on "the parallel Indian court proceedings" (l.210). The analysis (l.210–278) cites no forum clause; the only terms quoted are Sections 11, 13 and 15, and 15 is a Delaware choice-of-law clause (l.52–60).
  - OEC USA was dismissed under Rule 12(b)(2) (l.449).
- l.121 is on page 12, so the corrected label is right.
- Every date in the reasoning is printed in the document it cites (D08 prints 09/14/26, May 22, 2022 and May 3, 2023).

**outcome: A: match; B: match.**
- Both answered Royal Caribbean plus the JLF Defendants with high confidence, from separate full packets, citing D04 l.15/121–125 and D08 l.21/42.
- Readings both rejected: Norvell, attempts that were denied (DUAL), "in favor of another court" applying to transfer only (Lewis Machining, OEC India), and a contract that must bind the plaintiff.
- Neither shows contamination.

**closed-book: misses.** It answered "unknown"; forced guess "none", p 0.10. Its "minor" self-report is the harness git-status and email context, which has nothing about aq-01540, so I accept the miss.

**necessity:**
- Royal Caribbean appears only in D04 and the JLF transfer only in D08.
- The rev 2 probes reuse the rev 1 packets legitimately: question and corpus are unchanged, each question.txt is byte-identical to rev 2, and the removed document's text is absent.
  - Without D08: "cannot be determined"; forced Royal Caribbean alone, p 0.45.
  - Without D04: answered the JLF Defendants alone (with a caveat about the missing ruling); forced the same, p 0.55.
- Both are off the gold, and no smaller source set exists.

**shortcut: clear.** The audit's route checks out: D04 l.15/121, then D08 l.21/42. No single passage gives the answer. The quick "forum-selection" and "transfer venue" searches are a difficulty risk, not a shortcut.

**source_assessment: no gaps.** Intake shows all eight documents complete. D04 and D08 match their originals byte for byte, and the small character normalisations elsewhere (D01 l.239, D06 l.120, D07 l.156, 161, 200, 268) touch nothing this question relies on.

**difficulty: easy.** This is local suitability, not a measured tier. The question text is unchanged, so my rev 1 assessment stands:
- "ever" points solvers at case history, and l.42 uses the question's own word "transfer".
- Royal Caribbean is the obvious item (bundle title, Doc 5 overview).
- Each decoy is ruled out in its own passage.
- Estimate: Too easy ~35%, Easy ~50%, Between levels ~6%, Medium ~5%, High ~1%, Too hard or Answer not supported ~3%.

**verdict: ready (local only).**
- All local conditions are met: gold verified, two matches, closed-book miss, clear audit, both probes off the gold, floor 0 FAIL with one WARN (origin, explained), and Q14/Q15 satisfied.
- The difficulty above is not target-suitable for Medium, so the gate's final-readiness condition is not met. Keep status checked.
- An Easy result is unusable on this set, so quick-test it (0 of 10 used) before spending a difficulty run.

**failure_modes:**
- FM1 is now "Older figure inside a newer report" / "Wrong members in a list":
  - The trap is real. D08 l.42's quote is verbatim in both text/ and docs/. Recomputed wrong answer: "Royal Caribbean Cruises Ltd." alone, which is the gold minus JLF.
  - I checked every claim and each is true:
    - The September 14, 2026 opinion denies the motion to reopen.
    - The transfer sits in one background paragraph on page 3, followed by assignment to "the undersigned" on May 3, 2023.
    - D08 never says "forum-selection", and "forum non conveniens" appears only at l.81 (Chick Kam Choo).
    - The 2026 rulings are all denied (l.17–18, l.152, l.168, l.172, l.175).
    - The decoy summary is accurate: Doc 5 granted, Doc 4 denied, Doc 1 denied, Doc 7 not reached.
    - The 2022 Rhode Island suit is "this case".
  - Word count: 117 + 57 + 67 = 241.
  - The trap is the best of the form's 15 options: "Linking across documents" does not apply, and "Out-of-range period" is ruled out by "ever". The cause fits.
  - It is not ruled out by the wording: "ever" says history counts but does not locate the transfer, and the boxes describe a skim of Doc 3.
- Withdrawing FM2 was right. One mode meets the 1–3 rule.
- Roles: the section is empty, so both ticked documents default to Answer component, which matches how each is used.

**findings:**
1. **Target suitability (main):** unchanged, as described under verdict.
2. **Form "One defensible answer" block:** still ~5–10%. Two routes both lead to "Royal Caribbean alone": both form solvers omitting JLF, or both requiring the contract to bind the parties. That second reading was raised by rev 0's solver B and the rev 2 probe without D04, and every full-packet return rejected it.
3. **Stale records** (outside the fingerprint; no re-test needed):
   - Lever checks' "Selected-lever checks" line still says "Late item".
   - The "Necessity" line cites rev 0/1 probes only.
   - "Style/set review" names q01 but not q03. q03 shares the forum-motion cases and the opening frame (similarity 0.454); q01 scores 0.447 with the shared run "15 2026 which defendants if any". Expect possible Sibling or Question mix warnings.
   - The Review record mixes your later fixes into my rev 1 findings; the raw review.md is faithful.
4. **FM1 nit (optional):** "an injunction under the Anti-Injunction Act" is shorthand. The request rested on that Act's relitigation exception (l.104) and on the All Writs Act (l.154). It is not misleading.
5. **Hand-over:** notes/handover-q02.md has not been generated yet; generate it after this review.
6. **Platform-only checks, unknown:** One defensible answer, Needs two or more documents, Original question, Not a duplicate, Restricted names, token window (114,252 of 115,000 before the question). The authorship tick is the user's to make.
7. **Fingerprint:** the report tool recomputes de27f6a2…, and every rev 2 record and raw return carries it. There is no platform record, so this is local readiness, not observed platform survival.

Files: D:\Agents\Docket\tasks\aq-01540\questions\q02.md, D:\Agents\Docket\tasks\aq-01540\runs\q02-r2-v2-de27f6a2d7ad3d2fc2be3f0838a925089e7e2078585be2a4cba6db69f37ca500\results\, D:\Agents\Docket\tasks\aq-01540\runs\q02-r0-alt-c9\results\probe-q02r2-without-D08.md, D:\Agents\Docket\tasks\aq-01540\runs\q02-r0-alt-c9\results\probe-q02r2-without-D04.md
