# q02 rev 0 - removal probes (2026-10-06)

Each probe is a fresh blind-solver agent given a prepared packet of this run, the verbatim question
and an instruction to treat one marked document as absent and answer "as you normally would" (best
answer plus probability). Approximates the platform's document check. Not an official blind solve.
tested_sha256: 0a386408e69ce5c5b95809f9757546787522f25d89190885c679a48407c5a747. Gold: $132 million.

## Without D12 (Q2 2026 release), solver-2 packet

Return (verbatim):

I can't give the exact answer from the eleven remaining documents. The June 30, 2026 figure needs the second-quarter 2026 charges (or a cumulative-to-date figure), and those would be in the July 31, 2026 release (D12), which I didn't read or search. What the other documents do support is **$261 million still unrecorded as of March 31, 2026**. The June 30 answer is $261 million minus the Q2 2026 charges.

    answer: Not answerable exactly without D12. Best figure: $261 million (as of March 31, 2026). June 30, 2026 = $261 million minus Q2 2026 pretax charges for the program. Probability that $261 million is the correct June 30 answer: about 3%.
    confidence: high for $261 million as of March 31, 2026; low for any June 30, 2026 figure
    path:
     1. Latest estimate available: D11 (May 1, 2026), line 39: "on April 30, 2026, the Company's Board of Directors approved an expansion of the SGPP … cumulative pretax charges related to the SGPP … are now estimated to be $350 million to $550 million, increased from $200 million to $300 million." Midpoint = (350 + 550) / 2 = $450 million.
     2. Q1 2026 pretax charges: D11, Table 6 continued, line 548: "Strategic Growth and Productivity Program 176 37 139 1 138 (0.4) % 0.17", so $176 million before income taxes. Cross-check: operating-profit charges of 171 (line 494) are SG&A 6 (line 471) plus other expense 165 (line 487); adding non-service postretirement costs of 5 (line 508) gives 171 + 5 = 176.
     3. 2025 pretax charges: D09, Table 9 continued, line 865 (full-year 2025): "Restructuring programs(1) 13 2 11 — 11 — % 0.01". Footnote, line 903: "The restructuring program charges relate to the Strategic Growth and Productivity Program in 2025". The Q4 2025 figure is also $13 million (line 703), so nothing was recorded in Q1–Q3 2025. That fits D07 line 41 (the program was announced August 1, 2025 with "$200 and $300 million" in charges) and D08, which has no program row in its 2025 reconciliations.
     4. Recorded through March 31, 2026: 13 + 176 = $189 million. Unrecorded: 450 − 189 = $261 million.
     5. Q2 2026: none of the remaining documents gives the charges. D10 is only a segment recast covering 2023 to Q3 2025. A search of D10 and D11 for "June 30, 2026", "second quarter", "cumulative" and "incurred" found nothing beyond D11 line 39.
     6. Why ~3%: $261 million is right only if Q2 2026 charges were exactly zero and D12 didn't change the $350–$550 million estimate. That is unlikely, since Q1 2026 alone had $176 million in charges and the board expanded the program on April 30, 2026. If the estimate didn't change and charges weren't reversed, $261 million is an upper limit for the June 30 figure.
    minimal_documents: D11 + D09 are enough for the March 31, 2026 figure. D07 is optional (announcement date and original estimate). The June 30 answer needs D12; no other document in the packet can replace it.
    readings:
     - Counting only operating-profit charges (leaving out the $5 million postretirement amount): 450 − (13 + 171) = $266 million as of March 31. I rejected this because the estimate is stated as "pretax".
     - Using the original $200–$300 million estimate (midpoint $250 million): 250 − 189 = $61 million as of March 31. I rejected this because D11 replaced that estimate.
     - If D12 revised the estimate again, the midpoint changes too, and that can't be checked without D12.
    gaps: Q2 2026 (or first-half 2026) pretax program charges, any revised estimate, and any cumulative-to-date disclosure are all in the excluded D12. I read D11, D10 and the relevant parts of D09 in full. D07 and D08 I read in part (narrative plus a search of every restructuring or program row). D01–D06 I only searched by keyword: they never mention the program, and their dates (2019 through April 2025) are before its August 1, 2025 announcement. The text extraction scrambled some table rows, but the row totals check out arithmetically.
    contaminated: no

Result: gold $132 million not reached (best figure $261 million, about 3%). D12 needed.

## Without D11 (Q1 2026 release, the expanded estimate), solver-1 packet

Return (verbatim):

I couldn't get an exact answer from the eleven remaining documents. They fully establish the charges recorded ($318 million), but the only estimate they contain is the original one, and the recorded total already exceeds it. The latest estimate was most likely in the excluded D11.

answer: Not answerable exactly without D11. The general result is (midpoint of the latest revised estimate) − $318 million. Using the only estimate in the remaining documents ($200–$300 million, midpoint $250 million), the result is 250 − 318 = **−$68 million**: nothing is left unrecorded, and charges are $68 million past the midpoint. I put about a 5% chance on this being the expected answer. The question assumes some amount was still unrecorded, and $318 million is above even the $300 million top of the range. So the "latest estimate" was almost certainly raised later. The only packet document dated between the earlier releases and June 30, 2026 is D11 (May 1, 2026). D12 does not restate any estimate.

confidence: low

path:
1. **Estimate.** D07 line 41 (Aug 1, 2025) says the "new three-year productivity program … is projected to result in cumulative pre-tax charges, once all initiatives are approved and implemented, totaling between $200 and $300 million over the course of the three-year program." The midpoint is (200+300)/2 = $250M.
2. **Same program under its later name:**
   - D07 line 146: "cost reduction plans (including the productivity program announced on August 1, 2025)".
   - D08 line 129 uses the same wording with the new name: "(including the Strategic Growth and Productivity Program)".
   - D08 line 37: "deploy our previously announced Strategic Growth and Productivity Program".
3. **No charges through Q3 2025.** D08 line 450: the nine months to September 30, 2025 included only "ERISA litigation matter of $15 and acquisition-related costs of $9."
4. **2025 charges: $13M.**
   - D09 line 495 (twelve months 2025): "ERISA litigation matter and the Strategic Growth and Productivity Program of $99 and $13, respectively."
   - Pretax row, D09 line 865: "Restructuring programs(1) 13 2 11 — 11".
   - Footnote, line 903: "relate to the Strategic Growth and Productivity Program in 2025".
5. **First-half 2026 charges: $305M.**
   - D12 line 800 (six months to June 30, 2026, pretax column first): "Strategic Growth and Productivity Program 305 61 244 2 242". The same row is at line 798 of the original source file.
   - This equals $300 of operating profit (line 742; line 461 "$129 and $300") plus $5 of non-service postretirement costs (line 760).
   - Q2 alone was $129 (line 656), so Q1 2026 was 305 − 129 = $176.
6. **Total recorded by June 30, 2026:** 13 + 305 = **$318M**. The total at March 31, 2026 was 13 + 176 = $189M.
7. **Result:** 250 − 318 = −68. Charges also exceed the $300M top of the range by $18M.
8. **No other estimate exists outside D11:**
   - Searches for "pre-tax/pretax/cumulative", "between $", "productivity program" and dollar-range patterns found only D07 line 41.
   - D08, D09, D10 and D12 contain no estimate. I read D09, D10 and D12 in full and checked D12's original source.

minimal_documents: D07, D09 and D12 establish everything that is available; D08 adds the name link. A complete answer also needs D11, which was excluded. I found no replacement for it in the other documents.

readings:
- Counting only operating-profit charges: 13 + 300 = 313, so 250 − 313 = −63.
- Counting only 2026 charges: 250 − 305 = −55.
- With a revised midpoint M from D11: M − 318 (or M − 313 on the operating-profit basis).
- Every reading that uses the D07 estimate gives a negative number, so none of them fits the question's assumption.

gaps:
- The revised estimate, presumably in D11, is unavailable.
- D01–D06 were only searched, not read. They predate the program's announcement and never mention it.
- D07 was read at lines 1–80 and 140–151 only, D08 at lines 30–44 and 125–134 only, plus search hits in both.
- D11 was not read or searched. No layout or PDF files exist, so there were no extraction problems.

contaminated: no. The instruction to treat D11 as absent is part of the task design; it revealed no figures or reasoning.

Result: gold $132 million not reached (best -68, about 5%). D11 needed. The probe also derived the
recorded total of 318 from D09 and D12 alone, confirming the pretax reading (305) without D11.

## Without D09 (Q4/FY2025 release), shortcut packet

Summary of the verbatim return (task notification 2026-10-06; key lines quoted):
"I can't give an exact figure without D09. The exact answer is $145 million minus the program's
pretax charges recorded in Q4 2025, and that Q4 2025 amount appears only in D09. My best estimate is
about **$50 million**, with roughly a 3% chance of being exactly right (about 60% chance of being
within ±$30M). If no charges were recorded in Q4 2025, the answer would be $145 million, which I put
at about 10% likely."
path: D11 l.39 (450); D07 l.41 / D08 l.37 alias; 2026 charges Q1 176 (D11 l.548), Q2 129 (D12
l.656), H1 305 (D12 l.800; l.461 "$129 and $300"; l.760 $5); no charges Jan-Sep 2025 (D08 l.450);
Q4 2025 inferred from D10 Corporate (1,717) - (523) = 1,194, balance-sheet goodwill and intangibles
drop (~915 impairment) and normal Corporate cost (~185) -> program charges ~94 -> 145 - 94 = ~51.
readings: 2026-only $145M; operating-profit basis ~$56M; original estimate rejected.
contaminated: no.

Result: gold $132 million not reached (best ~$50M; alternative $145M at about 10%). D09 needed.
