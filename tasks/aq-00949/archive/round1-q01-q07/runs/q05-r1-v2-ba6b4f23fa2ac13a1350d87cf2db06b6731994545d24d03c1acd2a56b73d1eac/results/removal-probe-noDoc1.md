# q05 rev 1 - local removal probe without D01 (platform Doc 1), 2026-10-08

Design evidence, not a blind solve. Fresh blind-solver (agent a7ab83efbfc2f582c; 24 tool uses; about
722 s) on packet runs/q05-r1-alt-c8/solver-1: a byte copy of the rev 1 solver-1 packet minus D01,
remaining ids renumbered contiguously (probe D01 = D02, D02 = D03, D03 = D04, D04 = D05, D05 = D06,
D06 = D07), neutral run name, bound with docket_agent.bind_scope. Prompt: root, packet, verbatim rev 1
question, plus "forced_answer" and "forced_probability" lines. tested_sha256
ba6b4f23fa2ac13a1350d87cf2db06b6731994545d24d03c1acd2a56b73d1eac.

Result: guess-reaches. The unforced answer is "not answerable" (no December 31, 2019 figures in the
packet), but the probe recalled EOG's 2019 cash (about $2,028M) and total debt (about $5,175M) "from my
own memory" and forced the gold, 22.7, at p 0.4.

Raw return as received (probe ids; harness indent removed):

answer: not answerable from this packet. The June 30, 2026 ratio is 61.9% (4,907 / 7,926). No document gives EOG's cash or debt at December 31, 2019.
confidence: high (that the packet cannot answer it)

path:
1. June 30, 2026 figures. D06 (docs/eog_ex991_2026-08-04.txt, the Q2 2026 supplemental data). The "Net Debt-to-Total Capitalization Ratio" table on printed p.23 (text/D06.txt lines 829–836) has this header: "June 30, 2026 March 31, 2026 December 31, 2025 September 30, 2025 June 30, 2025". Its rows include "Current and Long-Term Debt (GAAP) - (b) | 7,926 | 7,931 | 7,936 | 7,694 | 4,236 |" and "Less: Cash | (4,907) | (3,849) | (3,396) | (3,530) | (5,216) |".
   - The balance sheet on p.12 (lines 186, 212, 216) agrees. The June 2026 column shows "Cash and Cash Equivalents ... 4,907", "Current Portion of Long-Term Debt ... 27" and "Long-Term Debt ... 7,899". 27 + 7,899 = 7,926.
   - 4,907 / 7,926 = 61.910%.
2. December 31, 2019 figures are missing.
   - A regex search for "2019" across all of text/ and docs/ returns zero matches. A search for 2010–2023 finds only FY 2021–2023 columns, and those are income, volume and cash-flow data, not balance sheets.
   - The earliest debt figure is March 31, 2024. D01's net-debt table (header line 822: "March 31, 2025 December 31, 2024 September 30, 2024 June 30, 2024 March 31, 2024") ends with debt of 3,791.
   - The earliest cash figure is December 31, 2023: 5,278, the "Cash and Cash Equivalents at Beginning of Period" for 1Q 2024 (D01 line 290).
   - No year-by-year cash or debt bridge back to 2019 exists. There is no ROCE or "capital employed" table, and no narrative comparison using "since", "pandemic" or "decade".
3. Result: the ending ratio is known (61.9%), but the starting ratio cannot be found, so the rise in percentage points cannot be calculated.

minimal_documents: D06 alone covers the June 30, 2026 side. Only D06 contains that date, so there is no substitute. No document covers December 31, 2019.

readings:
- If the start date means the latest year-end in the packet, December 31, 2025 (D06 table, same rows): 3,396 / 7,936 = 42.792%. Rise = 61.910 − 42.792 = 19.118, so **19.1 pp**. Only D06 is needed. This is the only date in the packet that gives a "rise".
- If it means December 31, 2024 (D03 lines 831/838 or D04 line 861: debt 4,752; net debt (2,340), so cash 7,092; D04 balance sheet agrees: 532 + 4,220): 7,092 / 4,752 = 149.243%. The change is −87.3 pp, a fall, which does not fit "rise".
- From my own memory, not the packet and not verified: EOG at 12/31/2019 had cash of about $2,028M and total debt of about $5,175M (1,015 current + 4,160 long-term). That gives 39.188%, and a rise of 61.910 − 39.188 = 22.722, so about **22.7 pp**. If debt were about $5,160M without finance leases, the result would be 22.6, so the rounding is sensitive to the exact debt figure.

gaps:
- The packet has no December 31, 2019 cash or total debt figure. A FY2019 10-K or Q4 2019 earnings release would supply it.
- I read D02 in full and these parts of D06: lines 1–110, 160–239, 720–880 and 940–1208. I did not read D01, D03, D04 or D05 end to end. Instead I ran regex searches over both text/ and docs/ for: 2019, 201x/2020–2023, "December 31", year-end, total debt, net debt, cash and cash equivalents, long-term debt, capital employed/ROCE, since, balance sheet, pandemic, decade, historical.
- All sources are .txt files (method "text", pages null). There are no PDFs, so I could not check any charts or images from the original filings.
- D06 seems to hold only the supplemental pages (9–29); the narrative press-release pages may be missing. The searches show no 2019 content anywhere in the packet.

contaminated: no. The auto-attached git status listed workspace file and run-directory names, but nothing about this question's answer or reasoning. I read no notes, question files or other packets.

Files used:
- d:\Agents\Docket\tasks\aq-00949\runs\q05-r1-alt-c8\solver-1\text\manifest.json
- d:\Agents\Docket\tasks\aq-00949\runs\q05-r1-alt-c8\solver-1\text\D06.txt
- d:\Agents\Docket\tasks\aq-00949\runs\q05-r1-alt-c8\solver-1\text\D02.txt
- d:\Agents\Docket\tasks\aq-00949\runs\q05-r1-alt-c8\solver-1\text\D01.txt, D03.txt, D04.txt, D05.txt (searched only)
- d:\Agents\Docket\tasks\aq-00949\runs\q05-r1-alt-c8\solver-1\docs\ (searched only)

forced_answer: 22.7
forced_probability: 0.4
