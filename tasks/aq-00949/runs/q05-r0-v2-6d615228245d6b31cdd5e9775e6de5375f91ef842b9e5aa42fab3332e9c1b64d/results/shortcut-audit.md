role: shortcut-auditor (fresh Agent subagent, shortcut-auditor role, packet shortcut)
received: 2026-10-05
input: workspace root, packet path shortcut, q05 rev 0 question text verbatim (nothing else)
tested_sha256: 6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d
tool_uses: 19 | duration_ms: 132980

--- raw return (verbatim as received) ---

answer: The ratio rose by about **22.7 percentage points**, from 39.2% at December 31, 2019 to 61.9% at June 30, 2026.

verdict: clear

shortest_path:
1. **December 31, 2019 (D01, the March 16, 2020 press release, net-debt table, text lines 155–177):** "Current and Long-Term Debt (GAAP) - (b)" is 5,175 and "Less: Cash" is (2,028). The table checks out: 5,175 − 2,028 = 3,147, the reported net debt. The narrative on line 41 matches in rounded form: "total debt outstanding was $5.2 billion … $2.0 billion of cash on the balance sheet." Ratio: 2,028 / 5,175 = 39.188%.
2. **June 30, 2026 (D07, the August 4, 2026 Q2 supplement, net-debt table, text lines 829–836):** debt is 7,926 and cash is (4,907). The table checks out: 7,926 − 4,907 = 3,019. The balance sheet agrees (line 186: cash 4,907; lines 212 and 216: current portion of long-term debt 27 plus long-term debt 7,899 = 7,926). Ratio: 4,907 / 7,926 = 61.910%.
3. **Change:** 61.910 − 39.188 = 22.722, which rounds to **22.7 percentage points**. Subtracting the already-rounded ratios (61.9 − 39.2) also gives 22.7.

sufficient_documents: D01 plus D07, and both are required. D01 is the only document with any 2019 data. D07 is the only document with June 30, 2026 figures; D06 ends at March 31, 2026. No single document covers both dates, and no document reports a cash-to-debt ratio, so this is an ordinary two-document lookup plus a ratio difference. That makes it a difficulty risk, not a shortcut.

searches:
- **Terms:** cash as a percent or ratio of debt; "net debt"; "total debt"; "Current and Long-Term Debt"; "Cash and Cash Equivalents"; "Current Portion of Long-Term Debt"; "Long-Term Debt"; "cash on hand"; "cash on the balance sheet"; "liquidity".
- **Dates:** "2019", plus two-digit forms (Q19, YE19, FY19, '19, 12/31/19); "June 30, 2026", "2Q 2026", "Second Quarter 2026".
- **Values:** 5,175, 2,028, 7,926 and 4,907, checked against the original docs/ files, where they match.
- **Read:** the manifest; D01 lines 1–202 (the substantive content); D07 lines 1–60, 174–233, 308–321, 815–859 and 985–1207.
- **Grep only:** D02–D06, through their net-debt tables and the date searches. Their tables cover March 2024 to March 2026, so they hold neither endpoint.

readings/gaps:
- **Rounded narrative figures:** using D01's prose values ($2.0B / $5.2B = 38.46%) with D07's exact ratio gives 23.4 points. This is weaker, because D01's own table has the exact figures.
- **Long-term debt only:** this can't be done for 2019, since D01 gives only the combined current and long-term figure. D01's "total debt" wording points to that combined measure for both dates.
- **Relative change instead of points:** ruled out, because the question asks for percentage points.
- **Number collision:** 5,175 also appears in D04–D07 as total current liabilities at June 30, 2025. It is unrelated.
- **Unread portions:** D02–D06 in full and parts of D07. Date searches exclude them as sources for either endpoint, so no answer-changing gap remains.

Files:
- D:/Dev/Docket/tasks/aq-00949/runs/q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d/shortcut/text/D01.txt
- D:/Dev/Docket/tasks/aq-00949/runs/q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d/shortcut/text/D07.txt
- D:/Dev/Docket/tasks/aq-00949/runs/q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d/shortcut/docs/eog_ex991_2020-03-16.txt
- D:/Dev/Docket/tasks/aq-00949/runs/q05-r0-v2-6d615228245d6b31cdd5e9775e6de5375f91ef842b9e5aa42fab3332e9c1b64d/shortcut/docs/eog_ex991_2026-08-04.txt
