# Blind solver B (packet solver-2), q03 rev 0 (2026-10-08)

Role: blind-solver, fresh context, input = root, packet path, question text.
tested_sha256: 5096099312ef09a6e6330c159a9eac06f76bebba5e88106ba107169b9ff5deaf

Raw return (verbatim):

answer: -10.0 percentage points. About 36.5% of the class list in place at decertification had no bankruptcy record found at all, against about 46.5% of the 581 June 2022 class members located at certification.
confidence: high

path:
1. When the decertification motion was filed (D07, Doc. 157, filed 12/02/25, p.5 at line 67 of text/D07.txt): "Trans Union moved for decertification on July 31, 2025. (See Doc. No. 139.)" D03 (line 37) repeats this.
2. Which class list was in place then (D07 p.3–4, line 47): Jaffe's March 2025 search "resulted in 22,212 SSNs that had no bankruptcy records returned, and 35,941 SSNs that had one or more bankruptcy filings that predated the applicable consumer report by more than ten years." His April 2025 Thomson Reuters re-run "resulted in the elimination of 920 individuals from the initial Step Two search, resulting in a class list of 57,233 individuals." Check: 22,212 + 35,941 = 58,153, and 58,153 − 920 = 57,233. D07 footnote 5 (line 127) calls the April 22, 2025 report "Jaffe's final report", and D06 (line 33) lists it as Exhibit B to the decertification motion. So the list in place on July 31, 2025 is the April 2025 list.
3. No-record group on that list (D07 p.4, line 49): "the 20,891 class members for whom Jaffe's search failed to locate any public record of a bankruptcy filing in PACER or Thomson Reuters." The stale group (line 61) is "the 36,317 class members for whom Jaffe located a bankruptcy filing public record that preceded the applicable consumer report by more than ten years."
   Share A = 20,891 / 57,233 = 36.50%.
4. June 2022 at certification (D05, Doc. 116, filed 08/01/24, p.26, line 312): "In the month of June 2022 alone, Plaintiff's proposed method for determining class membership located 581 class members." Line 148 says "at least 270 lacked a public record of a bankruptcy action on PACER. Additionally, 311 individuals had a public record of a bankruptcy that was more than 10 years old." Check: 270 + 311 = 581.
   Share B = 270 / 581 = 46.47%.
5. A − B = 36.50 − 46.47 = −9.97, which rounds to −10.0 percentage points.
6. The D05 text file prints "270 of 97330 such files". The raw docs/uscourts_paed_2_22_cv_00048_4.txt reads "270 of 973", so the "30" is a footnote marker. Footnote 30 says "only 973 of the 1,100 input/output logs from June 2022 contained a nine-digit social security number." 270/973 = 27.7% and 311/973 = 32.0%, matching the printed percentages. I also confirmed 20,891, 57,233, 36,317, 22,212, 35,941 and "elimination of 920" in the raw docs/uscourts_paed_2_22_cv_00048_8.txt.
7. The decertification counts don't quite add up: 20,891 + 36,317 = 57,208, which is 25 short of the stated 57,233. Using 57,208 as the denominator gives 36.52%, so A − B = −9.95, which still rounds to −10.0. The answer is unaffected.

minimal_documents: D05 + D07. No replacements found. D03 defines the No Bankruptcy Group from the April 22, 2025 report but gives no counts; its "approximately $2,100,000" for $100 automatic payments implies only about 21,000 members. D06 is a sealing order with no counts. D04 gives only 22,141 June 2022 primary files, which are not class members. D01 and D02 are sealing documents.

readings:
- If the March 2025 list is taken as the operative one: 22,212 / 58,153 = 38.20%, and 38.20 − 46.47 = −8.3 pp. I reject this because the April 2025 report replaced it before the July 31, 2025 motion.
- If the June 2022 share uses the 973 files with nine-digit SSNs (27.7%) instead of the 581 located class members: 36.5 − 27.7 = +8.8 pp. I reject this because the question says "among the class members located."
- If it uses the 1,100 step-one potential members: 270/1,100 = 24.5%, giving +12.0 pp. This is less defensible for the same reason.
- If the subtraction order were reversed, the answer would be +10.0. As written, the question asks for list share minus June share, so −10.0.

gaps: D05 says "at least 270", which is a slight hedge, but the numerosity passage uses 270 as the count. The 25-person gap in item 7 is unexplained in the documents. No PDFs exist in the packet (manifest method is "text"), so I checked against the raw docs/ text instead.
Coverage: I read D03, D06 and D07 in full. For D05 I read lines 140–169 and 300–329 plus search hits. For D01, D02 and D04 I read only the headers (plus D04 lines 88–91) and relied on searches. Searches across all text files covered decertif, no bankruptcy/no record, June 2022, class list, stale/ten-year terms, and the key numbers. I did not read question.txt.

contaminated: no

Caller note: the solver says the raw docs/ file reads "270 of 973"; the extracted text and the original both read "97330" per the mapper (footnote marker fused). Not material to the answer.
