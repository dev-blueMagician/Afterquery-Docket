# q06 rev 0 independent review (question-review, fresh context), completed 2026-10-06 (agent a9c6b26742377838b)

Dispatched with the frozen fields, corpus, fingerprint, target, raw returns and the platform context only.
Pasted unabridged.

q06 is locally ready for the Easy target. The gold answer holds up when recomputed from the sources, every check record is bound to this exact fingerprint, and nothing found is a correctness problem. The only open items are a minor wording slip in Step 1 of the reasoning and two form checks that only the platform can confirm.

**q06 (rev 0; tested_sha256: 956127708f59b4caf6b7364e4d895f05a928070f2b436fc33c5580530be0ff63)**

**gold_verified:** yes. A read-only script parsed all eleven Attachment 2 balance tables (D01–D06, D08–D12).
- Every printed net-debt or adjusted-debt figure equals total debt minus cash, time deposits and marketable securities.
- The December 31 balances (2023, 2024, 2025) are identical in every release that prints them.
- Quarter-on-quarter changes, total debt / net debt ($M):

| Quarter | Change | Result |
|---|---|---|
| 1Q24 | +999 / +2,944 | out (debt rose) |
| 2Q24 | +1,349 / +3,619 | out |
| 3Q24 | +2,657 / +1,962 | out |
| 4Q24 | −1,300 / −3,382 | out (both fell) |
| 1Q25 | +5,140 / +7,282 | out |
| **2Q25** | **−214 / +363** | **qualifies** |
| 3Q25 | +12,077 / +8,416 | out |
| **4Q25** | **−786 / +644** | **qualifies** |
| 1Q26 | +4,670 / +5,640 | out |
| 2Q26 | −8,353 / −11,556 | out (both fell) |

So the gold "2Q 2025, 4Q 2025" holds, and all eight exclusions are proved.

Other readings checked:
- **Early labels:** in D02 and D03, "Adjusted debt" leaves out time deposits, and neither prints any for March or June 2024. Those quarters already fail because total debt rose, so this cannot change the answer.
- **Figure choice:** each input is stated once, or identically across releases, so there is no rounded-versus-exact split. Rounding to $0.1B keeps the same set.
- **Wrong comparison column:** comparing each release with its own prior-December column gives none. The question's "previous quarter-end" rules this out.
- **Ratio rows:** using the debt-ratio and net-debt-ratio rows gives 4Q 2025 only (D08 shows the debt ratio rising 16.6% to 16.8% while debt fell). The question defines net debt as an amount, which rules this out.
- **Cash-flow lines:** each quarter's three-month "Net change in debt" and change in cash give the same set.

**outcome:** A: match; B: match. Both ran in separate packets with the read guard bound to this run. The question text is identical across packets and the source-file hashes match the snapshot and the live bundle. Both rebuilt net debt from its parts and rejected the prior-December reading; B also rejected the ratio reading. Neither reported contamination.

**closed-book:** misses. It answered "1Q 2024 and 2Q 2025" at low confidence: one wrong item, and 4Q 2025 missing. It got 2Q 2025's direction from rough remembered balances but said it could not recall 4Q 2025 through 2Q 2026, which the full answer needs.

**necessity:** Each listed release is the only source of one non-December quarter-end balance, confirmed by searching both the text files and the originals:
- D02: March 31, 2024 (21,835), needed for the 1Q24 and 2Q24 exclusions.
- D03: June 30, 2024 (23,184), for 2Q24 and 3Q24.
- D04: September 30, 2024 (25,841 / 21,138), for 3Q24 and the 4Q24 decoy.
- D06: March 31, 2025 (29,681 / 25,038), for 1Q25 and the 2Q25 match.
- D08: June 30, 2025 (29,467 / 25,401), for the 2Q25 match and 3Q25.
- D09: September 30, 2025 (41,544 / 33,817), for 3Q25 and the 4Q25 match.
- D11: March 31, 2026 (45,428 / 40,101), for 1Q26 and the 2Q26 decoy.
- D12: June 30, 2026 (37,075 / 28,545), for the 2Q26 decoy.

If any one is removed, the remaining documents offer only two substitutes, and neither settles the balance directions:
- **Cash-flow lines** measure flows, not balances. In 3Q25 the flow was +2.1B against a +12,077 balance change.
- **Ratio rows** are rounded, the equity needed to back out the balances is missing for the removed date, and they point the wrong way for 2Q25.

No smaller set works. D01, D05 and D10 only repeat the December balances, and D07 has no balance data. The approximate cash-flow route would reach the gold without D02–D04, so their necessity rests on the exclusions and on the question's balance definition. That is legitimate for a "which quarters" question.

**shortcut:** clear. The shortest complete route is to read the total-debt and net-debt rows from the eight Attachment 2 tables (December values from the first-quarter releases' comparison columns), take the ten consecutive differences, and apply both conditions. That matches the auditor's route and my gold.
- No passage states a quarter-to-quarter net-debt change.
- The bundle overview and D12 line 93 mention only the 2Q 2026 "$8.4 billion" debt reduction, which is a decoy.
- The cash-flow route still needs six releases and ten sign checks, so it is a difficulty risk, not a Guide violation.

**source_assessment:** no gaps. The capture is complete: its hash matches the intake record, and all 12 documents are flagged complete with zero missing characters. The recorded empty gap list hashes to sha256("[]") as expected. Source-file hashes match across the snapshot, the bundle and all three document packets. No gap-impact mapping is needed.

**difficulty:** easy (local suitability only; not measured). This is a different family from the single dated-bridge lookups the platform scored as too easy on this bundle.
- **Ways a weaker solver can go wrong:** the comparison column is the previous December, not the previous quarter, for seven of the ten quarters. The highlights ratio rows conveniently show previous-quarter columns, but they mislead on 2Q25. The label switches from "Adjusted debt" to "Net debt", and the 2Q25 margins are small.
- **Too-easy risk is moderate:** every input is a labelled table cell, the cash-flow route also reaches the gold, and both blind solvers matched with high confidence.

**verdict:** ready

**findings:**
1. **Reasoning Step 1 (minor).** It says Doc 2 and Doc 3 "print the same quantity as 'Adjusted debt'". In fact D02 line 346 and D03 line 358 define it as "Total debt less cash and cash equivalents and marketable securities", with no time deposits. No number depends on this, since Steps 2–4 use only total debt. Fixing it changes the fingerprint, so fold the fix into any future revision rather than re-testing for it alone.
2. **Form number check (platform only).** Steps 3, 4, 5, 7, 8, 9 and 11 each cite two documents, and each holds numbers found in only one of them. For example, Step 3's 21,835 and "March 31, 2024" are only in D02, while 23,184, "June 30, 2024" and "2Q 2024" are only in D03. Every number appears in one of the cited documents, and the single-document Steps 2, 6 and 10 fully pass. How the form treats two-document steps has not been observed; check its reasoning panel after pasting.
3. **Verbatim quotes (platform only).** The quotes use spaces where the documents and the capture have tabs (e.g., D02 line 334 is "Total debt $\t21,835 $\t20,836"). The local floor passes them; whether the platform normalises whitespace is unknown.
4. **Lever works.** Without the net-debt condition the answer would be 4Q24, 2Q25, 4Q25 and 2Q26. The decoys 4Q24 and 2Q26 fail the second condition, and the ratio and prior-December readings give 4Q 2025 only and none respectively.
5. **Format (platform advisory).** "If any" signals that nothing might qualify but does not say what to answer in that case; the form's advisory may still ask.
6. **Tags.** "Entity resolution" rests only on the label change from "Adjusted debt" to "Net debt". That is weak, but the other three tags cover the two-tag requirement.
7. **Records.** Rev 0 and the fingerprint match the snapshot, the report's recomputed fingerprint and all four check records. The report omits the shortcut audit only because it reads just the Blind solve section. There is no platform record yet, so the status should stay checked, with the platform result pending.
8. **Set review.** No overlap with q05 (ROCE). The dropped q01's 2Q26 net-debt change is now only a decoy here.

Files reviewed:
- D:\Dev\Docket\tasks\aq-00998\questions\q06.md
- D:\Dev\Docket\tasks\aq-00998\runs\q06-r0-v2-956127708f59b4caf6b7364e4d895f05a928070f2b436fc33c5580530be0ff63\snapshot.json
- D:\Dev\Docket\tasks\aq-00998\runs\q06-r0-v2-956127708f59b4caf6b7364e4d895f05a928070f2b436fc33c5580530be0ff63\results\returns.md
- D:\Dev\Docket\tasks\aq-00998\text\D01.txt–D12.txt
- D:\Dev\Docket\AQ-00998_2026-10-06_0256.md
