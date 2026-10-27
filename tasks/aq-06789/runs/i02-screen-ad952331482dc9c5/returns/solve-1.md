# i02 blind solve 1 (fresh blind-solver, 2026-10-18) - judged RIGHT

Raw return, verbatim:

answer: 70%

confidence: high

path:
1. April 2005 testimony = D02 (GAO-05-532T). Header (D02.txt line 5): "(14-APR-05, GAO-05-532T)"; line 13: "DATE: 04/14/2005". Testimony before the House Subcommittee on Housing and Community Opportunity (line 37).
2. D02 gives the FEMA staff count three times, consistently:
   - Line 67 (What GAO Found): "under the regulation, management, and oversight of about 40 FEMA employees assisted by about 170 contractor employees."
   - Line 119: "regulated, managed, and overseen by about 40 FEMA employees with the assistance of about 170 contractor employees."
   - Line 170: "according to a FEMA official, about 40 FEMA employees are responsible for regulating, managing, and overseeing the program ... FEMA is assisted in this effort by about 170 contractor employees."
3. December 2007 report = D09 (GAO-08-28). Header (D09.txt line 5): "(28-DEC-07, GAO-08-28)"; line 11: "DATE: 12/28/2007".
4. D09 line 187 (Background): "As of September 2007, FEMA had about 68 employees, assisted by about 170 contractor employees, to manage and oversee the NFIP and the National Flood Insurance Fund". No other NFIP staff count appears in D09.
5. "FEMA's own employees" excludes the 170 contractor employees (unchanged in both documents anyway). Also excluded: D02 footnote 1 (line 84) "FEMA and its approximately 2,500 staff became part of the Department of Homeland Security", a FEMA-wide count as of March 2003, not NFIP.
6. Calculation: (68 − 40) / 40 = 28 / 40 = 0.70 = 70.0% → nearest whole percent: 70%.

minimal_documents: D02 + D09. No substitutes: D02 is the only April 2005 document and D09 the only December 2007 document; the others are D01 (Sep 2003, toy guns), D03 (Sep 2006, alternative mortgages), D04 (Feb 2006, OCC consumer assistance), D05 (Nov 2005, insurer terrorism preparedness), D06 (May 2007, bankruptcy counseling), D07 (Jul 2008, long-term care insurance), D08 (Jul 2008, fair lending). A search for NFIP/FEMA content outside D02 and D09 found none (D05 mentions FEMA only for continuity-of-operations guidance; the D01 and D08 hits were "female").

readings:
- Total workforce including contractors: (68+170) − (40+170) = 28; 28 / 210 = 13.3% → 13%. Rejected by "FEMA's own employees".
- Timing nuance: the D09 figure is dated "As of September 2007" but published in the December 2007 report; the question's framing ("from ... testimony to its ... report") points to the figure as published, giving the same 70%.
- Both figures carry "about"; the result is the ratio of the published round numbers. No exact counts are given.

gaps:
- No original PDFs in the packet (docs/ holds only .txt files; manifest.json shows method "text" and pages null for every document), so no page images could be checked; the GAO ASCII text read cleanly at every key passage.
- D02 and D09 read in part (headers, summary/background passages above, plus full-text keyword searches for employee/staff/personnel/workforce/headcount/contractor), not start to finish.
- D01, D03–D08 checked only by keyword searches (staffing terms, NFIP, FEMA, contractor) and title/date headers, not read in full.
- question.txt not opened, per instructions.

contaminated: no

Packet files used:
D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06789\runs\i02-screen-ad952331482dc9c5\solver-1\text\manifest.json
D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06789\runs\i02-screen-ad952331482dc9c5\solver-1\text\D02.txt
D:\Projects\Projects\AfterQuery-Docket\10.8\tasks\aq-06789\runs\i02-screen-ad952331482dc9c5\solver-1\text\D09.txt
