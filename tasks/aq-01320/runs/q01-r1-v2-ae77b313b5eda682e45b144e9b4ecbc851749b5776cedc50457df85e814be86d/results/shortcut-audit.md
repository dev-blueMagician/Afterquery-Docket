# q01 rev 1 shortcut auditor (fresh shortcut-auditor agent, packet shortcut), 2026-10-06

Prompt: workspace root, packet path shortcut, exact question text only.

**answer:** −$0.28. Darden's actual fiscal 2026 reported diluted EPS from continuing operations was $10.44. The midpoint of the outlook range in force when Q4 began ($10.62 to $10.82) was $10.72. So $10.44 − $10.72 = −$0.28.

**verdict:** clear

**shortest_path:**
1. **When Q4 began:** D05 (line 11), dated "March 19, 2026", reports results "for the third quarter ended February 22, 2026". So Q4 began February 23, 2026, and D05's updated outlook came out about 3.5 weeks after that. D06 agrees: the year "ended May 31, 2026" with a 53rd week, and Feb 23 to May 31 is exactly 14 weeks. D04 also agrees: its Q2 "ended November 23, 2025", and 13 weeks later is Feb 22, 2026.
2. **Outlook in force on Feb 23, 2026:** D04 (December 18, 2025). Its headline bullet gives only the adjusted range ("$10.50 to $10.70", line 90). The reported range is in the reconciliation table, line 139: "Reported diluted net earnings per share from continuing operations | $10.62 | to | $10.82". The table reconciles: 10.62 + 0.06 + 0.08 − 0.26 = 10.50, and 10.82 → 10.70. Midpoint = (10.62 + 10.82) / 2 = **10.72**.
3. **Actual result:** D06, line 49: "Reported diluted net earnings per share from continuing operations were $10.44". The same figure appears in the year-to-date reconciliation (line 173) and the earnings statement (line 271).
4. **Result:** 10.44 − 10.72 = **−0.28**.

**sufficient_documents:**
- D04 (range) plus D06 (actual) are the core.
- Timing comes from D05's quarter-end date and release date. D05 also rules itself out as the source.
- Alternatively, timing can be inferred from D04's Q2 end date plus 13 weeks, or from D06's 53-week year ending May 31.
- No single document answers the question:
  - D06 gives only the fiscal 2027 outlook and never restates the fiscal 2026 range.
  - D05 says it "updated" the outlook but doesn't repeat the D04 range, and it has no full-year actual.
  - D04 has no actual result.

**searches:**
- I read the manifest and D04, D05 and D06 in full.
- Searches on "Darden|DRI|Olive Garden" matched only D04–D06. The Chipotle, Wendy's and Yum filings (D01–D03, D07–D12) have no Darden content, so they can't hold a Darden outlook or recap.
- Answer-shaped searches ("10.72", "0.28", "midpoint", "guidance", "previously", "prior outlook") found no Darden hits. The only "0.28" hits are Chipotle EPS and a Wendy's dividend.
- Searching each candidate value (10.62, 10.82, 10.40, 10.50, 10.44, 10.45) found them only where expected.
- I checked the key figures and dates against the original docs/ files, and they match the text extraction.

**readings/gaps:**
- **Wrong timing:** D05's March 19 outlook, reported $10.40 to $10.50 (midpoint $10.45), gives −$0.01. It was issued after Q4 began, so it wasn't the outlook "as it stood" then. This is the main trap, not a defensible alternative.
- **Wrong metric, adjusted range:** D04's adjusted range (midpoint $10.60) against the reported actual gives −$0.16. Adjusted against adjusted (actual $10.64) gives +$0.04. D05 adjusted against adjusted gives +$0.02.
- **Wrong line, net EPS:** using net EPS including discontinued operations ($10.38) gives −$0.34.
- **Difficulty risk:** once the timing is right, this is a two-document subtraction. The work is in the timing and in finding the reported range, which sits only in D04's reconciliation table.
- **Unresolved gap:** any Darden reaffirmation or update between Dec 18, 2025 and Feb 23, 2026 that isn't in the packet. Within the packet there is none.
- **Contamination:** none seen; I accessed no notes, question files, key or outside material.
