# q01 rev 0 blind solver B (fresh blind-solver agent, packet solver-2), 2026-10-06

Prompt: workspace root, packet path solver-2, exact question text only.

answer: **$0.28.** The actual figure was $10.44, against a midpoint of $10.72 for the $10.62–$10.82 range that was in effect when fiscal Q4 began on February 23, 2026.

confidence: high

path:
1. **When Q4 began.** D05, line 11 (filed March 19, 2026): "third quarter ended February 22, 2026". So fiscal Q4 began on February 23, 2026. D06, line 13: "fourth quarter and fiscal year ended May 31, 2026, which included a 53rd week of operations". That gives a 14-week Q4 from February 23 to May 31, which is consistent.
2. **Which outlook applied on February 23, 2026.** The latest update before that date was in the December 18, 2025 release. D04, lines 11 and 76 say "The Company updated its full year financial outlook for fiscal 2026". The range is in D04, line 139 (Reconciliation of Fiscal 2026 Reported to Adjusted Earnings Outlook): "Reported diluted net earnings per share from continuing operations|$10.62|to|$10.82|".
   - Check against the adjusted range: 10.62 + 0.06 + 0.08 − 0.26 = 10.50, and 10.82 gives 10.70. Both match the "$10.50 to $10.70" adjusted range on line 143.
3. **Why the March update doesn't count.** The next update came on March 19, 2026 (D05, lines 11 and 76), about 3.5 weeks after Q4 began. D05, line 139 gives "$10.40|to|$10.50".
4. **Actual full-year figure.** D06, line 49: "Reported diluted net earnings per share from continuing operations were $10.44". The same figure appears in the year-to-date reconciliation (line 173) and the income statement for the twelve months ended 5/31/2026 (line 271).
   - Cross-check: $1,213.7M ÷ 116.3M diluted shares = 10.436, which rounds to $10.44.
5. **Calculation.** Midpoint = (10.62 + 10.82) ÷ 2 = 10.72. Shortfall = 10.72 − 10.44 = **0.28**.
   - The actual figure was also below the low end of the range by $0.18.

The original source files under docs/ show the same rows ($10.62 to $10.82, $10.40 to $10.50, $10.44, and the February 22, 2026 quarter end).

minimal_documents:
- D04 for the range.
- D05 for the Q4 start date, and to show the March update came after it.
- D06 for the actual figure.

No replacements exist. A search for "Darden|DRI" matched only D04, D05 and D06. Without D05, the Q4 start date could only be inferred by assuming Q3 was 13 weeks long, counting from D04's November 23, 2025 Q2 end.

readings:
- **Using the March 19, 2026 outlook** (issued during Q4, not when it began): range $10.40–$10.50, midpoint $10.45, so the shortfall would be **$0.01**. This doesn't fit "as it stood when that fiscal year's fourth quarter began".
- **Using adjusted EPS** (not what the question asks): the actual adjusted figure of $10.64 beat both adjusted midpoints, $10.60 (December) and $10.62 (March), so there would be no shortfall.
- **Using diluted net EPS including discontinued operations** ($10.38) would give $0.34. This doesn't fit either, because the question specifies continuing operations.

gaps:
- No packet document directly confirms that Darden made no outlook update between December 18, 2025 and February 22, 2026. I inferred that because D05 describes the March 19 change as an update and no other Darden document is in the packet. I did not use any outside knowledge.
- The sources are plain text (manifest method "text", no PDFs or layout files), so no page images needed checking.
- I did not read D01–D03 or D07–D12 (Chipotle, Wendy's and Yum); I only searched them for Darden references and found none.

contaminated: no

Files used: solver-2\text\D04.txt, D05.txt, D06.txt
