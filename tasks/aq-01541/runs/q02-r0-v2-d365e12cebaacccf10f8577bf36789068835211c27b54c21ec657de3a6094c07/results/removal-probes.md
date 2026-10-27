# Removal probes, q02 rev 0 (2026-10-08)

Packets: runs/q02-r0-alt-m6/solver-1 (q02's prepared packet minus docs/uscourts_paed_2_22_cv_00048_10.txt = Doc 7,
ids renumbered D01-D06) and runs/q02-r0-alt-m6/solver-2 (minus docs/uscourts_paed_2_22_cv_00048_8.txt = Doc 6).
tested_sha256 (question fields): d365e12cebaacccf10f8577bf36789068835211c27b54c21ec657de3a6094c07

## Without Doc 7 (D03), raw return (verbatim; probe ids are renumbered)

answer: not answerable. The packet has no preliminarily approved Trans Union settlement, no fund figures and no automatic or claim-based payment terms.

confidence: high (that the packet cannot answer it)

path:
1. The manifest (D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-alt-m6\solver-1\text\manifest.json) lists six documents. All are from Brooks v. Trans Union, E.D. Pa. No. 2:22-cv-00048, and come from docs/ files _0, _1, _2, _4, _6 and _8. I read all six text files in full:
   - D01 (Doc 105, 7/30/24): memorandum on sealing.
   - D02 (Doc 106): sealing order and Appendix A.
   - D03 (Doc 114, 8/1/24): ruling under Rule 702 (expert evidence) striking Wodzinski as an expert.
   - D04 (Doc 116, 8/1/24): class certification granted.
   - D05 (Doc 154, 10/29/25): memorandum on sealing.
   - D06 (Doc 157, 12/2/25): decertification and the motion to strike both denied. It ends at "Page 29 of 29".
2. Search results across text/ and docs/:
   - A search for "$" found no matches anywhere.
   - "settlement" appears only in D04, and only about the 2003 Clark case: "In December 2003, Trans Union and Clark reached a class action settlement agreement" (D04 p.3). It gives no amounts and no claims process.
   - Searches for claimant, valid claim, claim form, automatic, preliminary approval, settlement fund, pro rata, payment, award and distribution found nothing relevant. The only hits were "payment of the reasonable expenses" in a Rule 37 sanctions passage (D06), "statutory damages" (D04), "preserve", the Pansy "fairness" factor, "242 million consumers" and "tens of thousands".
3. The packet does contain class-size facts, but no fund figure to divide by them:
   - D06 p.4: "resulting in a class list of 57,233 individuals".
   - D06 p.4: "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing".
   - D06 p.5: "the 36,317 class members for whom Jaffe located a bankruptcy filing ... more than ten years" earlier.
   - 20,891 + 36,317 = 57,208, which is 25 short of 57,233.

minimal_documents: none suffice. The "not answerable" conclusion rests on reading all of D01–D06. D06 is the latest document (12/2/25) and mentions only private mediation (footnote 3), not any settlement.

readings:
- (a) "Trans Union's settlement" could mean the 2003 Clark settlement (D04). It is not described as preliminarily approved here and has no figures, so this reading is also not answerable.
- (b) It could mean Ramirez v. Trans Union. D04 p.29 cites it only as a citation ("2022 WL 17722395 ... (N.D. Cal. Dec. 15, 2022)") with no settlement terms, so this is also not answerable.

gaps: The packet lacks the preliminary-approval memorandum or order, which is probably a later docket item beyond _8. That document would supply four missing facts:
- the court's figure for money set aside for valid-claim payments;
- the settlement class size;
- how many members get automatic payments;
- the allocation rule, including whether automatic-payment recipients also share the claims fund.

Docs _3, _5, _7 and anything after _8 are not in the packet. There are no PDFs or layout files. Extraction caused no problems.

contaminated: no. Only the packet path and question were provided. The environment's git-status snapshot listed file paths for an unrelated task (aq-00949) but contained no answer for this question. I did not read solver-1\question.txt or any notes.

forced best guess: $137.6, with about 0.5% probability of being right. This is almost entirely speculative. I assumed the 20,891 no-bankruptcy members get automatic payments. That leaves 57,233 − 20,891 = 36,342 members with no automatic payment. I then assumed a $5,000,000 valid-claims pool, which is not in the packet: $5,000,000 / 36,342 = 137.58, rounded to 137.6.

Caller note: unforced "not answerable"; forced $137.6 (p 0.005). Off the gold $29.1. Doc 7 is needed.

## Without Doc 6 (D07), raw return (verbatim)

answer: Not answerable from this packet. Each Aged Bankruptcy Group claimant (the only claimants with no automatic payment) would get $2,882,000 ÷ (3 × N_NoBankruptcy + N_AgedBankruptcy). The packet implies N_NoBankruptcy ≈ 21,000, but it never gives the size of the Aged Bankruptcy Group. The only firm limit is an upper bound: under $45.75, so at most $45.7.

Forced best guess: $33.1, about 2% chance of being right. My chance that the gold answer is actually "not answerable": about 55–60%.

confidence: high that the packet can't settle the number; low for any numeric guess.

path:
1. Court's figure for valid-claim money. D03 (Doc. 176, 7/6/26), page 5, line 66: "Approximately $2,882,000.00 of the Settlement Fund is reserved for payments to settlement class members (including both No Bankruptcy Group members and Aged Bankruptcy Group members) who submit valid claims."
2. How the money is split. D03 page 5, line 66: "Each class members's payment will be calculated by dividing the class member's individual pro rata points by the aggregate total number of pro rata points assigned to all claiming class members." Page 6, line 73: "No Bankruptcy Group members who submit a valid claim will receive three pro rata points, and Aged Bankruptcy Group members who submit a valid claim will receive one individual pro rata point."
3. Who gets an automatic payment. D03 page 5, lines 63–64: "Members of the No Bankruptcy Group will receive an automatic payment of $100.00 without the need to submit a claim." "Approximately $2,100,000.00 … reserved to provide No Bankruptcy Group class members with automatic payments." "Members of the Aged Bankruptcy Group will not receive these automatic payments." So the claimants with no automatic payment are the Aged Bankruptcy Group, at 1 point each.
4. The settlement was preliminarily approved. D03 page 20, line 243: "Plaintiff's motion for preliminary approval of the settlement agreement is granted."
5. Calculation. $2,100,000 ÷ $100 ≈ 21,000 No Bankruptcy Group members, so 63,000 points if all of them claim. The Aged group's size (N_AB) is never stated. Footnotes 2–3 on D03 page 5 only define the groups by "Jaffe … April 22, 2025 Supplemental Report"; that report isn't in the packet, and D06 only lists it as a sealed exhibit. Share per Aged claimant = 2,882,000 ÷ (63,000 + N_AB), which is below 45.746. It would round to 45.7 only if N_AB ≤ about 132.
6. Basis for the forced guess (a proxy I chose, not a packet fact). The 2024 certification opinion, D05 (Doc. 116) page 27, line 316, reports June 2022 sample results: "270 … returned no bankruptcy on PACER, and 311 … returned only a stale bankruptcy." Applying that ratio: N_AB ≈ 21,000 × 311/270 ≈ 24,189. Then 2,882,000 ÷ 87,189 = 33.05, so $33.1. As a sanity check, Plaintiff's expected payouts (about $1,000 for 3 points, about $350 for 1 point, D03 line 75) would then imply a claim rate of roughly 10%.

minimal_documents: D03 alone holds every settlement fact, and it shows the group size is missing. No other document has settlement terms, so there's no substitute. D05 is used only for the guess.

readings:
- Fund-residual reading. $8,310,000 − $2,770,000 − $308,000 − $50,000 − $210,000 − $2,100,000 = $2,872,000, which is $10,000 less than the court's figure. The question says to use the court's figure. Either way it's still not answerable; the upper bound would be $45.6 instead of $45.7.
- Other ways to fill in the missing group size give different results:
  - Equal-sized groups (N_AB = 21,000): $34.3.
  - Combined three-month ratio from D05 (10,405 : 9,747): $33.7. The March 2021 figures in D05 line 317 look internally inconsistent (4,741 is 32.0% of 14,816, which matches the stale-bankruptcy share, not the no-bankruptcy share).
  - Treating the Aged group as negligible: $45.7.
- Naive misreading: counting all 21,000 as the whole class gives $137.2, which is wrong because those are No Bankruptcy members only.

gaps:
- Missing facts: the size of the Aged Bankruptcy Group, and an exact No Bankruptcy Group count (both figures are only "approximately").
- Coverage: I read D03 and D06 in full; D05 lines 1–167 and 290–329; the first 30 lines of D01 and D02; D04 only through search hits. All six text files were searched for: automatic, preliminary, the group names, comma-formatted and spelled-out numbers, approximately/roughly/thousand, and supplemental report/stale/ten-year.
- docs/ check: the D03 source matched text/ on the key-term count (18 = 18).
- There are no PDFs or layout files in the packet (the manifest says method "text", pages null), so I couldn't check any original pages.
- I didn't read question.txt.

contaminated: no. Only the packet path, the question and the general instructions were provided. I saw no answers, notes or project instructions. The only workspace context in my session was a git-status file list (no contents). I can't check the Claude Code version myself, so I can't confirm the omitClaudeMd requirement is met.

Paths: D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-alt-m6\solver-2\text\D03.txt (decisive); D:\Agents\Docket\tasks\aq-01541\runs\q02-r0-alt-m6\solver-2\text\D05.txt (proxy for the guess only).

Caller note: unforced "not answerable"; forced $33.1 (p 0.02). Off the gold $29.1. Doc 6 is needed.
