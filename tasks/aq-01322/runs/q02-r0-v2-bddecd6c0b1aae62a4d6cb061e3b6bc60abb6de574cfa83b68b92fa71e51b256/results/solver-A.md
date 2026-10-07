# q02 rev 0 - blind solver A (fresh blind-solver, packet solver-1), 2026-10-06

Raw return as received:

I didn't read question.txt, and no answer or hint leaked.

    answer: $1.16 billion. This is the adjusted free cash flow for fiscal Q2 2026 (the three months ended March 31, 2026), which is $1,156.5M. The releases don't print this number directly; it is derived from their year-to-date figures.
    confidence: high
    path:
     1. Fiscal quarters. D01 line 17: "fiscal year 2026 first quarter ended December 31, 2025". D03 line 15: "fiscal year 2026 second quarter ended March 31, 2026".
     2. Completion date. D03 line 639 (cash flow footnote 1): "to finance a portion of the February 2, 2026 acquisition of OneOncology". D05 line 648 says the same. D03 line 52: "In the second quarter of fiscal 2026, in connection with the acquisition of OneOncology, the Company recorded a gain of $1.1 billion on the remeasurement of its equity method investment". February 2, 2026 falls in fiscal Q2 2026 (January 1 to March 31, 2026). D01 is dated February 4, 2026 and is headlined "Company Completes Acquisition of OneOncology" (line 15), but it reports Q1, which ended before the deal closed.
     3. Definition (D01 line 461, D03 line 678): "net cash provided by operating activities, excluding significant unpredictable or non-recurring cash payments or receipts relating to legal settlements, minus capital expenditures."
     4. Q1, three months (D01 lines 461–469, "for the three months ended December 31, 2025"): operating cash flows $(2,305.2)M; capital expenditures $(119.4)M; free cash flows $(2,424.5)M; "(Less) gains from antitrust litigation settlements $(12.2)M"; "Adjusted free cash flows $(2,436.7)M".
     5. Six months year to date (D03 lines 678–686, "for the six months ended March 31, 2026"): operating cash flows $(966.5)M; capital expenditures $(285.0)M; free cash flows $(1,251.5)M; "Less gains from antitrust litigation settlements $(28.7)M"; "Adjusted free cash flows $(1,280.2)M".
     6. Calculation for Q2 alone:
        - Totals: −1,280.2 − (−2,436.7) = **+1,156.5M**.
        - Component check from the cash flow statements, in thousands (D01 lines 404/406; D03 lines 616/618):
          - Operating cash flow: −966,530 + 2,305,169 = 1,338,639.
          - Capital expenditures: −284,994 + 119,376 = −165,618.
          - Free cash flow: 1,173,021, matching −1,251.5 + 2,424.5 = 1,173.0M.
          - Antitrust gains: 28.7 − 12.2 = 16.5M.
          - Adjusted free cash flow: 1,173.0 − 16.5 = 1,156.5M.
        - Independent check: D03 line 212 gives "a $16.5 million gain from antitrust litigation settlements … in the three months ended March 31, 2026", which matches the derived 16.5.
        - Result: $1,156.5M = $1.1565B, which rounds to **$1.16B**.
     7. Further consistency check (not needed for the answer): the nine-month adjusted free cash flow in D05 line 695 is $1,142.3M, and its antitrust figures add up (28.7 + 5.5 = 34.2; D05 lines 211, 261). "Cost of acquired companies" is $(219.7)M for Q1 (D01 line 407) against $(4,932.0)M for six months (D03 line 619), consistent with the deal closing in Q2.
    minimal_documents: D01 and D03, and both are needed. D03 gives the completion date, the quarter boundaries and the six-month figure; D01 is the only source of the Q1 three-month figure. D05 can confirm the date instead of D03 line 639, but it only gives nine-month cash flows, so it can't replace either document.
    readings:
     - Taking the D01 headline "Company Completes Acquisition of OneOncology" to mean Q1 gives Q1 adjusted free cash flow of $(2,436.7)M, or −$2.44B. I reject this because the deal closed February 2, 2026, after Q1 ended.
     - Treating the year-to-date figure in the Q2 release as the quarter's figure gives $(1,280.2)M, or −$1.28B. That covers six months, not one fiscal quarter.
    gaps:
     - No document states Q2 fiscal 2026 adjusted free cash flow on its own, so the figure is derived from the reported year-to-date numbers.
     - The derivation assumes Q1 was not restated in the six-month totals. The packet contains no restated Q1 figure, but the $16.5M three-month antitrust footnote agrees with the derived amount.
     - Coverage:
       - D01: read lines 1–130 and 380–495.
       - D03: read lines 1–140 and 590–716.
       - D05: read lines 600–699.
       - D02, D04 and D06: searched only. They are fiscal 2025 releases with no "oncology" or "OneOncology" matches.
       - The rest of the income statements and segment tables was not read.
     - Sources are text files (manifest "method": "text", "pages": null), so there were no PDF pages to inspect and no extraction problems.
    contaminated: no

Files used, all under D:\Dev\Docket\tasks\aq-01322\runs\q02-r0-v2-bddecd6c0b1aae62a4d6cb061e3b6bc60abb6de574cfa83b68b92fa71e51b256\solver-1\text\:
- manifest.json
- D01.txt
- D03.txt
- D05.txt
