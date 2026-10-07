# q01 rev 1 - independent review (raw, verbatim)

- Date: 2026-10-06. Fresh question-review agent (claude-opus-5-5), given the frozen fields, corpus,
  raw returns and target, without the writer's conversation. Copied verbatim from the task
  notification.
- tested_sha256: 3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7

## Return

q01 (rev 1; tested_sha256: 3fabaea5b09e8aa48f7f43ab3c660f33c4ddb165ecd48bccd092cf0423edb7f7)

**gold_verified: yes.** I recomputed the gold by script from the original rows.
- **Old structure (D09 Table 5, l.460-465):** Africa/Eurasia 1,172 (2025) and 1,095 (2024). Asia Pacific 2,814 and 2,858.
- **Recast (D10, l.28 and l.59):** Asia Pacific 3,038 and 3,074.
- **Russia and Belarus:** 224 and 216. **Moved operations:** 948 and 879. **Change:** +69.
- **Second route:** recast EMEA − old Europe − (old North America − recast North America) gives the same 948 and 879. Both structures total 15,769 and 15,618, and Latin America is unchanged, so the two routes agree exactly.
- **Units and sign:** $ millions as printed; 2025 minus 2024; positive.

**outcome: A: match; B: match.** Both answered +69 with high confidence, from separate fresh packets that held only the documents and the question. Each used the Africa/Eurasia route with an EMEA cross-check. They rejected +77, +38 and +230. D11 l.85 disproves all three: Russia and Belarus went to Asia Pacific, and skin health came from North America. Both are valid supported matches.

**closed-book: misses.** It answered "+$35 million" at low confidence, a growth guess applied to a remembered segment size. That is not equivalent to +69.

**necessity:**
- **D09** is the only source of 2025 full-year old-structure figures. D08 has nine months only, and the Q4 2025 old rows (309, 722) exist only in D09. D05 repeats the 2024 column only. The probe without D09 forced +50 and said +69 was outside its ±10 band.
- **D10** is the only source of any 2024 recast, and of the Q3/Q4 and full-year 2025 recasts. D11 and D12 recast only Q1, Q2 and H1 2025. The probe without D10 forced +41, or +63 on a constant-share assumption.
- **D11** is the only statement of what moved and the only document naming Russia and Belarus. D12's recast notes and D10 give no breakdown. D04-D06 describe only the July 2024 skin-health move. Without D11, D09 and D10 fit both +69 and +77.
- **No smaller valid set** exists. D05 can replace D09 for 2024 only.

**shortcut: clear.** The shortest route matches the auditor's and the gold: D11 l.85 → D09 l.463-464 → D10 l.28/l.59 → two subtractions per year → change.
- "Russia" and "Belarus" occur only at D11 l.85.
- 224 appears nowhere. The other hits for 216, 948, 879 and 69 are unrelated (tax provision, 2023 net income, dividends paid, other income).
- The overview summaries for Docs 9-11 omit the realignment, and no single passage gives the answer.

**source_assessment:** No gaps. The intake shows all 12 documents complete and matching the capture. The gap hash 4f53cda1… is the hash of an empty list.

**difficulty: easy.** This is a local judgment only; on these features the design looks weak for the Medium target.
- **Pushing toward Easy:**
  - The question's two segment names retrieve D11 l.85.
  - That passage states the exclusion and, in the next sentence, Russia and Belarus' destination. The destination points straight at the "recast Asia Pacific minus original" subtraction.
  - All inputs are single labelled cells in two short tables, and the same step repeats for both years.
  - The closest measured designs both placed Easy: a tied exclusion (aq-00745 q01, Low 1/5) and a method applied to an unreported quantity (aq-00998 q05, Low 2-3/5).
- **Pushing up:**
  - No document prints Russia and Belarus' sales or the moved operations' sales.
  - There is a same-label decoy: +77 from D09's Africa/Eurasia row, also shown as +7.0% in Table 7. The +38 and +230 routes are also open.
  - D10 has no notes, and D12's note gives no breakdown.
- **Estimate:** Easy is the most likely placement. Medium is roughly one chance in five. Too easy is low-to-moderate and Too hard is low.

**verdict: revise**

**findings:**
1. **Q4, one defensible answer.** The full-year rows give +69, and so does the nine-months-plus-Q4 route. Only rebuilding from quarters, which mixes in the documents' own rounding, gives anything else:
   - Old Asia Pacific quarters (D06-D09) sum to 2,813, not 2,814, so the Africa/Eurasia quarter route gives 947 and +68.
   - The 2024 old Africa/Eurasia quarters sum to 1,096, not 1,095.
   - The EMEA quarter route still gives 948.

   "Full-year" plus the printed full-year rows make these quarter sums solver errors, not defensible readings. No action needed.
2. **Platform document check on D11.** The probe without D11 reached +69 at about 50% by inference from operating-profit margins. That is a guess between allocations, not a document fact, so D11 is logically necessary; the platform's high model may still make the same inference.
   - The risk of a "marked document may not be needed" flag is moderate. Keep D11 marked; unmarking it would misstate necessity.
   - The rule's clause "only document naming an item you marked it as excluding" fits D11, as does the flag's own example ("holds the item your question excludes").
   - Unknown, platform-only: whether the form offers that marking, and whether the 200-character reviewer note unblocks the gate.
   - The note should say that D11 alone defines what moved and names the excluded Russia and Belarus, and that D09 and D10 alone fit +69 or +77. Add it last, because any edit clears it.
3. **Q14, verbatim evidence.** The quotes at D09 l.463 and l.464 and D10 l.28 and l.59 match locally and in docs/, but they exist only as pipe rows. The platform shows these rows without pipes, so the blocking verbatim check may fail.
   - There is no prose substitute for these figures.
   - Get the exact platform text via Save passage before any platform check.
   - Evidence is part of the fingerprint, so any change means re-preparing and running fresh checks.
4. **Form number check (emulated): clean.** The one date is printed in D11. Steps 4-5 use operands that each appear in only one of their two cited documents; Steps 2-3 already state them. How the form handles this is unconfirmed; low risk. The "Decoy:" line restates no result.
5. **Wording (Q9).** The phrase identifies "Africa/Eurasia excluding Russia and Belarus" uniquely, given D11.
   - Russia and Belarus fall outside it ("into … EMEA"; they went to Asia Pacific).
   - Skin health came from North America, and no other carve-out exists.
   - The full year is the calendar year ("Twelve Months Ended December 31"). Units and sign are pinned.
   - Including Russia and Belarus is the intended lever, not an ambiguity.
6. **Q1-Q12 and rule 10:** all pass. Q2 passes locally, with finding 2 as the platform risk. Q10: 36 words, one ask. Q11: skipping the exclusion gives +77, so the lever is active; a which-items decoy does not apply. Q12: D10 is tied to D11's structure because its Q1 2025 recast (904, 1,143, 1,007, 738) equals D11 Table 4's.
7. **Records.** The live fields equal the snapshot, and I recomputed the hash as 3fabaea5…. A, B, closed-book, audit and probes are all bound to that hash. The rev 0 records belong to a superseded question. The report tool omits the audit only because it parses just the blind-solve section.
8. **Platform-only checks: unknown.** Restricted names, originality, token window, Coach reaction and Q13. No platform measurement exists; status stays draft/checked.
