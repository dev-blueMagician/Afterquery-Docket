# q01 rev 1 blind solver B (fresh blind-solver agent, packet solver-2), 2026-10-06

Raw return as received by the caller (agent result text; tool trace not exported):

answer: -10.41%

confidence: high

path:
1. **Q2 2025 worldwide automobile NWP is $2,074M.** Source is D10 (Q1 2026 Financial Supplement), printed page 20, "Selected Statistics - Personal Insurance - Automobile". Line 656 reads: "Net written premiums $|1,955 $|2,074 $|2,165 $|1,956 $|1,756" (columns 1Q2025–1Q2026). The same row appears in docs/trv_ex992_2026-04-16.txt line 741.
2. **That $2,074M line includes international business, not just domestic.**
   - D10 page 19 (lines 639, 642) has the domestic and international figures: "Automobile $|1,859 $|1,968 ..." and "International 146 178 167 159 —".
   - D10 page 21 (line 700) has Homeowners and Other NWP for 2Q2025: 2,592. The domestic figure is 2,520.
   - Subtracting domestic from the page-20/21 figures: 2,074 − 1,968 = 106 for auto, and 2,592 − 2,520 = 72 for homeowners. 106 + 72 = 178, which equals the International row.
   - 2,074 + 2,592 = 4,666, which equals the Personal Insurance total NWP on pages 18 and 19.
   - The same check works for 1Q2025, 3Q2025 and 4Q2025 (96+50=146, 103+64=167, 100+59=159).
   - In 1Q2026, after the Canada sale, page 20 shows 1,756, which equals domestic auto (1,756), and International is "—".
3. **Q2 2026 worldwide automobile NWP is $1,858M.** Source is D09 (Q2 2026 press release), lines 321–325:
   - Line 321: "Automobile $|1,858 $|1,968 (6)|%"
   - Line 324: "International — 178 (100)"
   - Line 325: "Total $|4,308 $|4,666 (8)|%"
   - Line 340 explains the drop: "Net written premiums in the prior year quarter included $178 million related to the Canadian operations divested by the Company in the first quarter of 2026."
   - With international at zero, worldwide auto = 1,858 + 0 = 1,858.
   - D09's Q2 2025 domestic auto (1,968) matches D10, so there was no restatement.
4. **Calculation:** (1,858 − 2,074) / 2,074 = −216 / 2,074 = −0.104147, which rounds to **−10.41%**.

The decisive rows match the original source files: docs/trv_ex992_2026-04-16.txt (lines 722–741) and docs/trv_ex991_2026-07-17.txt (lines 360–364).

minimal_documents: D09 + D10. Both are needed:
- D10 is the only document with a Q2 2025 automobile figure that includes international business.
- D09 is the only source for Q2 2026.
- D08 (Q1 2026 release) only has domestic auto for Q1, so it can't replace either one.
- D01–D07 are Allstate, Chubb and Progressive filings. A search found no mention of "Travelers" in any of them.

readings:
- **Domestic auto only, or "excluding the impact of the sale":** (1,858 − 1,968) / 1,968 = −110 / 1,968 = **−5.59%**. The press release prints this as "(6)%". I rejected this reading because "worldwide" asks for international business to be included.
- **Six months year-to-date (not asked):** domestic is 3,614 vs 3,827. A worldwide year-to-date figure would need 1Q2025's 1,955 + 2,074 = 4,029, giving −10.30%. That is outside the question's quarter-to-quarter scope.

gaps:
- The packet has no Q2 2026 financial supplement, so Q2 2026 worldwide auto is not printed directly. It is derived as domestic auto plus an International line that D09 prints as "—". This inference is strongly supported by the 1Q2026 pattern described in step 2.
- The international split for Q2 2025 (106 auto / 72 homeowners) is derived by subtraction, not printed.
- The manifest says these are text-only extractions (pages: null; no layout files or PDF page markers), so page numbers are the printed footer numbers.
- I did not fully read D01–D07, only searched them for "Travelers". I did not read the parts of D08–D10 unrelated to Personal Insurance premiums.

contaminated: no

Usage reported: 18 tool uses, 121 s.
