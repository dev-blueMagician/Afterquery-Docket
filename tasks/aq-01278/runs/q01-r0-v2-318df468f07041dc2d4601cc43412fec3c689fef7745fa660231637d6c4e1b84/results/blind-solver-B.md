# q01 rev 0 blind solver B (fresh blind-solver agent, packet solver-2), 2026-10-06

Raw return as received by the caller (agent result text; tool trace not exported):

answer: −10.4% (personal automobile net written premiums fell from $2,074 million in Q2 2025 to $1,858 million in Q2 2026)

confidence: high

path:
1. **Q2 2025 base, including Canada (D10, Q1 2026 Financial Supplement, page 20, "Selected Statistics - Personal Insurance - Automobile").** The columns are "1Q2025 2Q2025 3Q2025 4Q2025 1Q2026". The row reads "Net written premiums $|1,955 $|2,074 $|2,165 $|1,956 $|1,756|" (text/D10.txt line 656; source docs/trv_ex992_2026-04-16.txt line 741). So Q2 2025 = $2,074M.
2. **Check that the $2,074M includes the Canadian premiums.**
   - D10 page 19 (lines 639–643) shows "Domestic Automobile $|1,859 $|1,968 …" and "International 146 178 167 159 —", with Total $4,666 for Q2 2025.
   - D10 page 21 shows Homeowners and Other at $2,592M for Q2 2025 (line 700), against domestic homeowners of $2,520M.
   - Auto difference: 2,074 − 1,968 = 106. Homeowners difference: 2,592 − 2,520 = 72. 106 + 72 = 178, which equals the International line. Also 2,074 + 2,592 = 4,666, the Personal Insurance total.
   - The same check works for Q1 2025: (1,955 − 1,859) + (1,863 − 1,813) = 96 + 50 = 146.
   - In Q1 2026, after the sale, the page 20 figure (1,756) equals domestic auto (1,756).
   - So page 20 is total automobile, including the Canadian operations. D09 line 340 says Q2 2025 "included $178 million related to the Canadian operations divested by the Company in the first quarter of 2026."
3. **Q2 2026 (D09, Q2 2026 press release, Personal Insurance table, lines 321–325).**
   - "Automobile $|1,858 $|1,968 (6)|%"
   - "International — 178 (100)"
   - "Total $|4,308 $|4,666 (8)|%"
   - With no international premiums after the sale, total automobile = $1,858M. The year-to-date figures agree: 1,756 + 1,858 = 3,614, and 1,859 + 1,968 = 3,827.
4. **Calculation:** (1,858 − 2,074) / 2,074 = −216 / 2,074 = −0.10415, which rounds to **−10.4%**.

minimal_documents: D09 + D10. Neither can be swapped out. Only D09 has Q2 2026 figures. Only D10 splits the Canadian premiums by product line (D08 and D09 show "International" only as a segment total). D08 is consistent but not needed.

readings:
- **Domestic only, excluding Canada:** (1,858 − 1,968) / 1,968 = −5.6% (printed as "(6)%"). This conflicts with the question's "Including premiums from the Canadian business".
- **Whole Personal Insurance segment, as reported:** (4,308 − 4,666) / 4,666 = −7.7%. This is not limited to automobile.
- The primary answer remains −10.4%.

gaps:
- The packet has no Q2 2026 financial supplement, so the Q2 2026 total-auto figure is taken from D09: domestic $1,858M plus International "—".
- The D10 row is labelled "Statutory underwriting"; its totals match the reported net written premiums (for example $4,666M).
- I read only the relevant sections of D08–D10. D01–D07 (other insurers) were checked only through searches for "Canad" and "automobile".
- There are no layout files in text/, and the sources are .txt files, so there were no PDF pages to inspect.

contaminated: no

Files used:
- D:\Dev\Docket\tasks\aq-01278\runs\q01-r0-v2-318df468f07041dc2d4601cc43412fec3c689fef7745fa660231637d6c4e1b84\solver-2\text\D09.txt
- D:\Dev\Docket\tasks\aq-01278\runs\q01-r0-v2-318df468f07041dc2d4601cc43412fec3c689fef7745fa660231637d6c4e1b84\solver-2\text\D10.txt
- D:\Dev\Docket\tasks\aq-01278\runs\q01-r0-v2-318df468f07041dc2d4601cc43412fec3c689fef7745fa660231637d6c4e1b84\solver-2\docs\trv_ex992_2026-04-16.txt

Usage reported: 14 tool uses, 113 s.
