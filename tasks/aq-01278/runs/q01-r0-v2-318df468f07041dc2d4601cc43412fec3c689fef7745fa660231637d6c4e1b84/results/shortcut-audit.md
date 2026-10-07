# q01 rev 0 shortcut audit (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

Raw return as received by the caller (agent result text; tool trace not exported):

answer: **−10.4%**. Including the Canadian business, Travelers' personal automobile net written premiums fell from $2,074 million in Q2 2025 to $1,858 million in Q2 2026.

verdict: clear

shortest_path:
1. **Q2 2026 figure (D09, Q2 2026 press release, Personal Insurance net written premiums table).** Under "Domestic": "Automobile $|1,858 $|1,968 (6)|%". The International line is "— 178 (100)", so Q2 2026 has no Canadian premiums and $1,858M is the full automobile total. Line 340 says: "Net written premiums in the prior year quarter included $178 million related to the Canadian operations divested by the Company in the first quarter of 2026." D09 does not split that $178M between auto and home.
2. **Q2 2025 figure including Canada (D10, Q1 2026 financial supplement, p.20, "Selected Statistics - Personal Insurance - Automobile").** "Net written premiums $|1,955 $|2,074 $|2,165 $|1,956 $|1,756" for 1Q25 to 1Q26, so 2Q2025 is $2,074M.
3. **Check that p.20 includes Canada.** The p.19 Domestic Automobile line is 1,859 / 1,968 / 2,062 / 1,856 / 1,756. The p.21 Homeowners figures are 1,863 / 2,592 / 2,553 / 2,288 / 1,730, against domestic 1,813 / 2,520 / 2,489 / 2,229 / 1,730.
   - For Q2 2025, Canadian auto is 2,074 − 1,968 = 106 and Canadian home is 2,592 − 2,520 = 72. Together that is 178, which matches International exactly.
   - The same check works for every 2025 quarter: 96+50=146, 103+64=167, 100+59=159.
   - Auto plus home (p.20 + p.21) equals the p.18 segment total each quarter, e.g. 2,074 + 2,592 = 4,666.
   - In 1Q26 p.20 equals domestic (1,756), so the two bases match once there is no international business.
4. **Calculation:** (1,858 − 2,074) / 2,074 = −216 / 2,074 = −10.41%, which rounds to −10.4%.

The raw docs/ files show the same values (trv_ex992_2026-04-16.txt line 741; trv_ex991_2026-07-17.txt line 360).

No single document is enough. D09 has Q2 2026 but only domestic auto plus an unsplit $178M. D10 has the Q2 2025 total including Canada but stops at 1Q2026. The two have to be joined by a simple percent-change calculation. This is a difficulty risk, not a shortcut: once D10 p.20 is found the arithmetic is trivial, but you still have to see that the press-release auto line is domestic-only.

sufficient_documents: D09 + D10. No alternatives: D08 has only Q1 2026 vs Q1 2025 figures, and D01–D07 are Allstate, Chubb and Progressive documents with no Travelers mentions.

searches:
- Terms: "Canad", "automobile", "personal auto", "auto… net written premium", "divest", "international", "held for sale", "disposed", "Travelers" (count by file).
- Inspected:
  - D09: read in full.
  - D08: lines 90–319, covering segment results including Personal Insurance.
  - D10: table of contents, pp.16–21 (lines 560–720), glossary and segment descriptions (lines 1255–1312), plus every Canada/international hit.
  - D03: lines 20–48, an Allstate supplement where "Canadian provinces" refers to rate changes.
  - manifest.json, and docs/ cross-checked by grep.
- Coverage: only D08, D09 and D10 mention Travelers.

readings/gaps:
- **−5.6%** (domestic only): (1,858 − 1,968) / 1,968. The press release rounds this to "(6)%". It leaves Canada out, which contradicts the question's "Including" condition. This is the main trap.
- **−13.4%** (all $178M treated as auto): (1,858 − 2,146) / 2,146. This is wrong because $72M of the $178M is Homeowners and Other.
- No restatement risk: D09's comparative figures for Q2 2025 (1,968 domestic auto, 178 international) match D10.
- Unread: D10 lines 120–560 and 720–1255 (Business Insurance, Bond & Specialty, balance sheet, investments, reserves, cash flow); grep found only non-premium Canada items there (held-for-sale balances, divestiture proceeds of $2,384M, reserves disposed). D08 lines 1–90 and 319 onward (highlights, forward-looking statements, glossary); automobile grep hits there were limited to lines 274, 293 and 314. D01, D02 and D04–D07 were checked by grep only.
- Contamination: I saw no notes, question files, snapshots, CLAUDE.md, memory, keys or prior outputs. From inside the session I could not confirm the invocation flags (non-fork, omitClaudeMd).

Files:
- ...\shortcut\text\D09.txt
- ...\shortcut\text\D10.txt
- ...\shortcut\docs\trv_ex991_2026-07-17.txt
- ...\shortcut\docs\trv_ex992_2026-04-16.txt

Usage reported: 20 tool uses, 221 s.
