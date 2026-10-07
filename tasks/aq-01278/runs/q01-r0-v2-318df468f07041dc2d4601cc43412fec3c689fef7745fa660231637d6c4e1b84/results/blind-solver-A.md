# q01 rev 0 blind solver A (fresh blind-solver agent, packet solver-1), 2026-10-06

Raw return as received by the caller (agent result text; tool trace not exported):

answer: -10.4%

confidence: high

path:
1. **The Canadian business is the "International" line.** D09 (Travelers Q2 2026 release, Personal Insurance section, line 340) says: "Net written premiums in the prior year quarter included $178 million related to the Canadian operations divested by the Company in the first quarter of 2026." The same section's table (line 324) shows "International — 178 (100)", so the $178M is the International line. The CEO quote (line 64) calls it "the sale of our Canadian business". D10 (line 1212) shows "Proceeds from the divestiture of the Canadian business … 2,384" in 1Q2026.
2. **Q2 2026 personal auto NWP is $1,858M.** D09 table (line 321) reads "Automobile $|1,858 $|1,968 (6)%" under Domestic. International is "—" in Q2 2026, so there are no Canadian premiums that quarter. As a check, the six-month auto figure is 3,614, and 3,614 − 1Q26's 1,756 (D08 line 274) = 1,858.
3. **Q2 2025 personal auto NWP including Canada is $2,074M.** D10 (Q1 2026 Financial Supplement, page 20, "Selected Statistics - Personal Insurance - Automobile", line 656) reads "Net written premiums $|1,955 $|2,074 $|2,165 $|1,956 $|1,756" for 1Q25 to 1Q26. D10 page 19 (line 639) shows Domestic Automobile of 1,859, 1,968, 2,062, 1,856, 1,756.
   - The page 20 figures include Canada. Auto: 2,074 − 1,968 = 106. Homeowners (page 21 NWP 2,592 vs Domestic 2,520): 72. 106 + 72 = 178, which matches International exactly.
   - The same check works in every quarter: 1Q25 96+50=146, 3Q25 103+64=167, 4Q25 100+59=159, 1Q26 0.
   - Page 20 + page 21 add up to the segment total: 2,074 + 2,592 = 4,666 (page 18/19 total for 2Q25).
4. **Calculation:** (1,858 − 2,074) / 2,074 = −216 / 2,074 = −0.10415, which rounds to **−10.4%**.
5. **Source check:** The decisive rows are the same in the raw docs/ files (trv_ex992_2026-04-16.txt lines 722, 725, 741; trv_ex991_2026-07-17.txt lines 360, 363).

minimal_documents: D09 + D10. D09 alone has no product split of the International $178M. D10 alone has no Q2 2026 data. D08 only covers Q1 and can't replace either one. No alternative document sets were found.

readings:
- **Excluding Canada (domestic only):** (1,858 − 1,968) / 1,968 = **−5.6%**. The press release rounds this to "(6)%". The question explicitly says to include Canada, so this is not the requested reading.
- **Rejected approximations:** Adding the whole $178M to auto gives (1,858 − 2,146) / 2,146 = −13.4%. Splitting it pro rata gives about −9.2%. Neither holds up, because $72M of the $178M is homeowners and D10 prints the actual auto figure.

gaps:
- The packet has no Q2 2026 financial supplement. The Q2 2026 auto figure comes from the D09 release table, which is consistent because International is zero.
- D10 page 20 labels its premiums "Statutory underwriting" net written premiums. They tie exactly to the reported figures (page 18 equals page 19, and 1Q26 equals 1,756 on both pages).
- I did not fully read D01–D07, which cover Allstate, Chubb and Progressive. The only non-Travelers "Canad" hit was an Allstate rate-change footnote in D03 line 27, which is irrelevant.
- I read only the relevant sections of D08–D10, not the entire documents.
- The documents are text-only (no PDFs, "pages": null), so I couldn't check page images. Text and layout extracts agreed.

contaminated: no

Files used:
- D:\Dev\Docket\tasks\aq-01278\runs\q01-r0-v2-318df468f07041dc2d4601cc43412fec3c689fef7745fa660231637d6c4e1b84\solver-1\text\D09.txt
- D:\Dev\Docket\tasks\aq-01278\runs\q01-r0-v2-318df468f07041dc2d4601cc43412fec3c689fef7745fa660231637d6c4e1b84\solver-1\text\D10.txt
- D:\Dev\Docket\tasks\aq-01278\runs\q01-r0-v2-318df468f07041dc2d4601cc43412fec3c689fef7745fa660231637d6c4e1b84\solver-1\text\D08.txt (check only)

Usage reported: 18 tool uses, 131 s.
