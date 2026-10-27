# aq-02198 - lean candidate sketches

Current target: medium (user, 2026-10-08: "there is no slot for Easy Tier for this bundle, we should target medium and
high. do your best."; page: Hard 0/2 · Medium 0/3 · Easy 0/1, 9 submissions, 0 of 10 quick tests, 8 of 8 runs); hard
where a design supports it. Measured platform success pending. Origin of all sketches: claude (Opus 5.5).

Sources are byte-identical to tasks/aq-02102 and tasks/aq-02165. Families closed there by quick test ("too easy"):
response shares, union lists, SPA-relative ages, missed-election count on Table 1, WPS share. Doc 1 and Doc 2 print the
same EQIA, so no Table 1 or diversity figure can make either document necessary (notes/hooks.md).

| ID | Sketch/source notes link | Hook | Ambiguity / necessity findings | Decision / next action |
| --- | --- | --- | --- | --- |
| k1 | [hooks.md](hooks.md) | 2016 members unprotected under Doc 4's glossary (274,563) | Table 1 printed in Doc 1 and Doc 2: only Doc 4 is necessary; form-block risk on the printed 222,424 | reject (necessity) |
| k2 | [hooks.md](hooks.md) | lowest salary the £250 rise moves up a band (£22,851) | both inputs public (alpha bands, 2020 Spending Review rise); Document check likely reaches the gold without either document | reject (recall) |
| i01 (k3) | [sketches/i01.md](sketches/i01.md) | subsection of the Pension Schemes Act 1993 that regulation 142(4) cites after the 2022 amendments: section 95(2) | Doc 1 only source of "95(2)" (D02 L1220); Doc 2 only source of the drop (D01 L619); decoy 95(2A); trap tied (D01 L619 names regulation 142); non-numeric; time pinned to the 2022 amendments (Doc 2 "will consider further") | screen passed (no failures/warnings, sha 3fc68a12...); caller and both authors expect "too easy"; optional free quick test at the user's choice |
| i02 (k4) | [sketches/i02.md](sketches/i02.md) | days from the 2023 launch (Doc 4 only) to the statutory statement deadline (Doc 3 only): 757 | wrong routes 756 (31 March 2025), 688 (from the 14 May close), 758 (inclusive); plain dated lookups and one gap; PSPJOA 18-month deadline may be recalled | screen passed (no failures/warnings, sha 49a6333a...); expected "too easy"; optional free quick test at the user's choice |
| a-i01 | author A (dropped) | date tribunal-rate interest stops for a member paid before a statement issued on its statutory deadline: 29 April 2025 | Doc 4 §4.14 (D03 L283, interest "until the amount owed is paid in full") conflicts with §4.16 (L287, 28 days after the statement "or if later, the date of payment"); constructed boundary case; 24 words | dropped (unfair) |
| a-i02 | author A (dropped) | MDP officers' MOD-funded EPA if legacy benefits are chosen: neither converted nor refunded (Doc 2 L359 + Doc 4 L369) | remedy-period purchases not confirmed; non-numeric; one hop from "MOD has agreed to fund" to "Employer-funded EPA" | dropped |
| x01 | author B (dropped) | grades that could already buy unreduced retirement at 60 within alpha (EEPA list, Doc 3) | keyword chain, recallable, non-numeric, answer-unit block risk | dropped |
| x02 | author B (dropped) | share of 2016 members the 2023 remedy rolls back (70.98%) | twin documents on both sides; i03 shape; 70.97 vs 70.98 rounding conflict | dropped |

Author B (question-author, 2026-10-08) read all five texts and found no fair Medium-capable design in Doc 1-Doc 2 or Doc 5:
EQIA twins, final rules printed whole in Doc 2, and Doc 5 linked to Docs 1-4 only through closed routes. Extra conflicts it
logged: IHR underpin start "received on or before 31 March 2022" (Doc 2 D01 L404/L448) vs "applications started before 31
March 2022" (Doc 4 D03 L421); first union meeting 15 days after launch in both 2021 and 2023.

Author A (question-author, 2026-10-08) read all five texts and found no fair Medium-capable design in the 2023 pair or its
joins: final rules printed whole in Doc 4, measured too-easy families, cross-edition conflicts, invented cases, or two
lookups plus one operation. It also flagged the regulation 142 trap as likely too easy and advised against quick-testing
its own two sketches.

Round 1 result (caller plus two independent authors, all five texts read in full by each): no fair Medium-capable design
on these bytes, matching aq-02102 and aq-02165. Remaining fair sketches i01 and i02 are offered only as optional free
quick tests; no difficulty run is recommended unless one survives.

Keep facts/checks in the linked sketch or these notes, not in duplicate write-ups. Ambiguity:
competing answer -> wording condition it fails. Necessity: source -> unique input -> substitutes
searched -> what is lost without it. Recheck the dependency after every clarification.
