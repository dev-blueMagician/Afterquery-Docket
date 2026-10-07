# q02 rev 0 independent review (question-review, fresh context), completed 2026-10-05

Dispatched with the frozen fields, corpus, fingerprint, target and raw returns only. Pasted unabridged.

q02 (rev 0; tested_sha256: 7f49b59c78b7e93452a75791c103f707dcae13565dce790e3ec47274e63f5493)

**gold_verified:** yes. I recomputed it by script from the original text.
- **Quarter:** D04 l.81 says "the third quarter 2023 acquisition of a majority stake in ACES Delta, LLC", so the quarter is 3Q 2023.
- **3Q 2023 value:** the D04 table (l.159/161) puts 3Q 2023 in the third column, "Refinery Crude Unit Inputs", at 980 MBD.
- **2Q 2026 value:** the D12 table (l.161/163) gives 1,070 MBD. The prose at l.87 says "1.07 million", which is the same figure, so there is no choice between stated figures.
- **Result:** 1,070 − 980 = 90 thousand barrels per day. It is an integer with no rounding.
- **Cross-checks:** D04's "+2 percent" fits 995/980 (+1.53%), not 995/965 (+3.1%). D12's "+2 percent" fits 1,070/1,051 (+1.81%).
- **Premises and period:** both premises are true. Chevron's year ends December 31 (D01 l.255), so no fiscal/calendar label is needed.
- **Alternatives, each ruled out by the question's own wording:**
  - 109: D01's "Crude Oil Inputs" 961 is a different line item.
  - 105: D04's year-to-date 965.
  - 120 or 147: reading the deal as 4Q 2023, which D04's "third quarter 2023" contradicts.
  - 108: full-year 2023, which is not a quarter.
  - 83: D12's year-to-date 1,063.

**outcome:** A: match; B: match. Both answered 90 using D04 and D12, and both rejected 109 and 120 with evidence. The two packets are separate and hold only the frozen question and the corpus, with bytes matching the snapshot. That gives two uncontaminated matches.

**closed-book:** misses. It answered "unknown (rough estimate: about 80)" with low confidence, which is not 90. It did recall the September 2023 ACES Delta date, so the bridge is something models already know. The sketch-stage guess was about 100 and this one about 80, so a round-number guess near 90 remains possible.

**necessity:**
- **D04 is needed** for the acquisition quarter (D01 l.43/79/97 say only "2023") and for the only 3Q 2023 crude unit figure. Backing the quarter out of other releases (D02 931/950, D03 985, D05 962) gives 978–985 weighted by days, or 982 by simple average. That means an answer of 85–92 or 88, never exactly 90.
- **D12 is needed** because it is the only 2Q 2026 release. D11 stops at 1Q 2026 (1,054).
- No smaller set works, and D01 is not needed.

**shortcut:** clear. The auditor's route holds: D04 l.81 → D04 l.161 (980) → D12 l.163 (1,070) → 90.
- "ACES" and "majority stake" appear only in D01 (three times) and D04 (once).
- No passage, document or overview entry states 90.
- The audit searched all 12 files with adequate terms.

**source_assessment:** no gaps apply to this fingerprint.
- source_gaps is empty, and 4f53cda1… is the hash of an empty list.
- The intake capture hash 9f6eab4d… matches AQ-00998_2026-10-06_0256.md.
- All 12 documents are marked complete with no gaps.
- Corpus and packet bytes match the snapshot. The earlier clipped capture is history only.

**difficulty:** easy (marginal; high risk of a "too easy" verdict). This is local suitability only.
- **Path:** one search for "ACES Delta" lands on D04 l.81, and the needed 3Q 2023 cell is in that same document's table. Then one labelled cell in D12 and one subtraction.
- **Past platform failures this resembles:**
  - trial-07 q05: a bridge picks single cells in two documents' tables; the low model solved it.
  - aq-00949 q02: a one-sentence bridge; returned "too easy".
  - trial-02 q01: labelled figures plus one standard calculation.
  - trial-07 q01: a bridge models already know.
- **Why the one pass doesn't transfer:** aq-00964 q01 passed because the bridge document's own figure was the trap and the wording did not exclude it. Here that is reversed. The bridge document's own figure is the answer, and the trap in the other edition is excluded by the exact line-item label the question needs to have one answer.
- **Likeliest quick-reader wrong routes:**
  1. **109.** The overview lists ACES Delta only under Doc 1, three of the four ACES hits are in D01, and D01 has a 3Q 2023 column. Its only U.S. refinery row is "Crude Oil Inputs" 961. A reader who knows the deal was in Q3 and treats "oil" as "unit" lands here.
  2. **105.** D04's header prints "3Q 2023" twice, with "YTD" on its own line above the table, and the last cell is 965.
  3. **120 or 147.** Treating D01, the Q4 2023 release, as dating the deal.
- Searching for the exact label avoids all three. On the D1-D7 risk prompts, D4 and D7 are weak and D3 moderate; three past "too easy" verdicts came after that profile. This is not a Guide violation, and only a platform result can measure it.

**verdict:** ready (local only; the status stays checked and the platform result is pending)

**findings:**
1. **Q11, "Same series, right edition" lever.** It is active (109 ≠ 90, and plausible via Doc 1) but weak, because the label "crude unit inputs" matches only the D02–D12 rows. The record should describe the trap as told apart by its label. No retest needed.
2. **Q9, author's note on the period WARN.** It attributes "Year Ended December 31" to D04, but D04 prints only "Nine Months Ended September 30" (l.255, l.308). The phrase is in D01 l.255. The conclusion still holds. Correct the note; that section is not part of the fingerprint, so no re-prepare.
3. **Q14, platform-only, unknown.** Both D12 quotes and D04's 980 quote are table rows whose cells are tab-separated in the source but quoted with single spaces. The local floor collapses whitespace; how the form's blocking verbatim and cited-document checks treat tabs has never been seen. Check D12's row with Save passage before filling in the form. If the platform text differs, changing the evidence means a new revision, a fresh prepare and fresh checks. D12 l.87 is a tab-free sentence.
4. **Q1.** The bridge is known to models, but this is not disqualifying: 980 and 1,070 still require D04 and D12.
5. **Set review.** q01 and q02 share one pattern: a quarter defined by an event, labelled cells, one subtraction, D12 as the endpoint, and the same tags. Both follow the task page's suggested "period identified by a fact" frame. Neither gives the other away. Vary the source relationship in later candidates. Duplicate and originality checks are external.
6. **Records.** A, B, the closed-book solve and the audit all carry rev 0 and the tested fingerprint. The report recomputes 7f49b59c… for the current file and corpus; its record list leaves out the audit, which is correctly bound in q02.md. On the origin WARN, "claude" is accurate; report the export restriction separately and do not bypass it.
7. **Q2–Q8, Q10, Q12 and rule 10** pass: the question is 33 words with one ask. **Q13:** there is no platform evidence, and no tier pass is claimed.

Relevant files:
- D:\Dev\Docket\tasks\aq-00998\questions\q02.md
- D:\Dev\Docket\tasks\aq-00998\runs\q02-r0-v2-7f49b59c78b7e93452a75791c103f707dcae13565dce790e3ec47274e63f5493\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q02-r0-v2-7f49b59c78b7e93452a75791c103f707dcae13565dce790e3ec47274e63f5493\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\text\D04.txt
- D:\Dev\Docket\tasks\aq-00998\text\D12.txt
- D:\Dev\Docket\tasks\aq-00998\text\D01.txt
- D:\Dev\Docket\AQ-00998_2026-10-06_0256.md
