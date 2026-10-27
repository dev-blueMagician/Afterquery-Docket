# aq-02198 - cross-document hooks

Target: medium, hard where a design supports it (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we
should target medium and high. do your best."). Page at capture (18:09): Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions
left, 0 of 10 quick tests used, 8 of 8 difficulty runs left; page hints "Applying the right rule" and "Rounding and
sign" (short of these), plus an LGPS overlap frame (Doc 3 / Doc 4). Doc N numbers below; local ids in notes/doc-map.md.

Sources are byte-identical to tasks/aq-02102 and tasks/aq-02165, whose measured results carry over. Closed on these
bytes (quick test "too easy", user reports 2026-10-08): response-statistics shares (aq-02102 q01), union
match-then-exclude (aq-02102 q02), SPA-relative pension ages (aq-02165 q01), missed-election rule on Table 1 (aq-02165
i03), classic WPS share of a band rate (aq-02165 i02). New questions must not reuse those sentence frames (the
platform's Original question check compares across tasks).

## Necessity constraint found this session

Doc 1 and Doc 2 print the same equality assessment (Table 1 protection status, 419,000, 30,000-40,000, Tables 2-6,
diversity statistics). A fact printed in both makes neither individually necessary, and the platform's Document check
has left out one twin alone and reached the gold from the other (aq-02147 q01; memory docket-series-editions-necessity).
So Table 1 can only be an unlisted input; a Table 1 design needs two other documents with unique inputs. Doc 3 and Doc 4
also overlap heavily (14 May 2023, 1 October 2023, most rules restated); only their unique facts (doc-map) can carry
necessity. Public figures (alpha 2021/22-2022/23 bands, the £250 pay-pause rise for under £24,000, McCloud dates, the
Treasury's July-October 2020 consultation) are likely recalled, so they cannot carry necessity either.

| Hook | Source inputs and locations | World fact/possible ask | Selected lever(s) | Applicable decoy/counterfactual | Source risks | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| k1 | Doc 4 glossary L635 "Unprotected members – Members who were moved to alpha on 1 April 2015"; Doc 1/2 Table 1 (Doc 2 L709-754); Doc 1 glossary L1150 (broad) | 2016 members unprotected under the 2023 response's definition: 222,424 + 52,139 (2012-15 joiners moved on 1 April 2015) = 274,563 | Applying the right rule; Document convention | 222,424 (printed label), 303,319 (Doc 1's definition), 277,231 (+tapered) | Table 1 in Doc 1 and Doc 2 (twin), so only Doc 4 is necessary; same design as aq-02165 n8 (form-block risk) | reject (necessity) |
| k2 | Doc 2 L570 £250 rise for workers under £24,000; Doc 1 band 1 "Up to but not including £23,101" (L1200), 2021/22 = 2022/23 (L321-323) | Lowest whole-pound salary the flat rise moves into the 5.45% band: 23,101 - 250 = £22,851 | Rounding and sign (band edge) | £22,850 (using "To £23,100") | both inputs public and recallable (Document check); two lookups and one subtraction | reject |
| k3 | Doc 1 draft reg 5 L1219-1220 (reg 142(4) "95(2)" -> "95(2A)"); Doc 2 L619 amendment dropped | Subsection of the Pension Schemes Act 1993 that reg 142(4) still cites after the 2022 amendments: 95(2) | Same series, right edition (superseded draft) | 95(2A) (draft value) | non-numeric; Doc 2 L619 names regulation 142 in the same sentence that drops it (tied trap) | sketch i01 (screen passed); optional quick test |
| k4 | Doc 4 L28 (launch 6 March 2023, only source); Doc 3 L522/L452 (statements due the day after the 18-month period from 1 October 2023, only source) | Days from the 2023 consultation's launch to the statutory statement deadline: 6 Mar 2023 -> 1 Apr 2025 = 757 | Calculate across documents | 756 (31 March 2025), 688 (from 14 May 2023) | plain dated lookups plus one date gap (too-easy profile) | sketch i02 (screen passed); optional quick test |
| k5 | Doc 1 L56 (response due 10 Feb 2022); Doc 2 L6 (published 4 Mar 2022) | Days late: 22 | Calculate across documents | not applicable | plain dated bridge (aq-02102 h3) | park |
| k6 | Doc 5 L6-8 (2017: 42 days); Doc 4 L28 (2023: 69 days); Doc 1 L32 or Doc 2 L59 (2021-22: 56 days, twin) | Order of the three Cabinet Office consultations by length | Ordered answers | Doc 1 cover typo "17 January 2021"; "16 January 2022" | plain dates; same as aq-02165 n3 | park |

The map is navigation; quotes come from the extracted sources. A short valid calculation or ID join is eligible.
Prior failures suggest tests/priority, not a universal veto.
