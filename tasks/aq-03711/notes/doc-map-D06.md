# aq-03711 - D06 document map (platform "Doc 3")

Navigation only. Line numbers are lines of `tasks/aq-03711/text/D06.txt` (written `L123`).
Quotes are verbatim from that file (curly quotes and apostrophes are the file's own).
Questions quote the documents, never this map. No questions, answers or traps are proposed here.

## 0. Binding, coverage ledger, extraction checks

- Source: `docs/nzcc_contact_code_111_commission_111_contact_code_2024_decisions_and_r.txt`
- sha256 (manifest and intake agree): `d35acf38ffe2f1e5c2689280d316e3057610438b34af087ccc2ea37145c54d04`
- Method `text`, 134,130 chars, 1,259 lines in `text/D06.txt` (2-line header + body, ends with `-----`).
- Read ledger (sequential, all inspected): L1-150, L150-299, L299-428, L429-558, L559-688, L689-818,
  L819-948, L949-1078, L1079-1238, L1238-1259. Remaining unread: none.
- Coverage: FULL for readable text.
- Other files touched only for cross-checks (NOT mapped): D01 (Grep + L156-163, L361-372, L874-889),
  D05 (Grep + L100-204, L228-241, L344-433), D02 (Grep), D03 L1-12, D04 L88-95, D07 L1-8,
  D08 L1-20 + Grep, D13 L1-12, D14 L1-8, D09-D12 (date Grep only).
- Extraction spot-checks against the original (`docs/...decisions_and_r.txt`, itself a plain-text capture):
  - Page count: running header "Commission 111 Contact Code 2024 – Decisions and Reasons paper N" occurs 57 times,
    N = 2 to 58, so 58 pages (cover page has no header).
  - Table: "ID Subject of change" header at original lines 253, 277, 322 = text L255, L279, L324 (constant 2-line offset).
  - Footnote: "136 https" at original line 1165 = text L1167; "51,000 voice-only" original 436 = text L438.
  - Glossary label "Code" on its own line at original 42 = text L44 (so the duplicated label is in the source, not an extraction fault).
- Layout problems (all present in the original text capture; no PDF to inspect, so visually unresolved):
  - Figure 1 (L160) is caption only: "Figure 1: Subset of consumers entitled to be considered vulnerable". Diagram content is MISSING.
  - Glossary (L30-54): the row for the 2020 code is labelled "Code" (L44), same label as the 2024 Code row (L36). The body calls the 2020 code "Previous Code" (L81).
  - Glossary rows run together: L43 "H&D Act The Health and Disability Services (Safety) Act 2001 NZ Police New Zealand Police"; L47-48 "Provider ... Retirement / Villages Act Retirement Villages Act 2003".
  - Contents (L57-77) is flattened; page numbers run into the next heading.
  - Table 1 (L255-349): cells flattened; each row's "Paras x-y" reference is followed on the same line by the NEXT row's ID and sometimes its subject (e.g. L293 "Paras 123- 136 5 Consumers preferred method of contact"). Row 8 is split across the page 15/16 break (reference at L320-321, last two bullets at L327-329).
  - Footnote markers sit on their own lines away from the sentence (e.g. L84 "3", L140 "9", L181 "16", L391 "33").
  - Footnotes 25-27 (L252-254) print before the table they belong to.
  - Run-in headings: e.g. L524 "...may be withdrawn.56 Final decision and reasons", L752, L795, L952.

## 1. Identity, dates, commencement and grace period

| Item | Value | Line | Verbatim |
|---|---|---|---|
| Title | Commission 111 Contact Code 2024, Decisions and Reasons Paper | L6-7 | "Commission 111 Contact Code 2024" / "Decisions and Reasons Paper" |
| Issuer | Commerce Commission (NZ) | L81 | "X1 The Commerce Commission (the Commission) 111 Contact Code (2024) (the Code)" |
| Commission members named | 4: Tristan Gilbertson, Pierre van Heerden, Nathan Strong, Loretta Lovell | L8-11 | "The Commission: Tristan Gilbertson" |
| Legal basis | s 239 Telecommunications Act 2001 | L8 | "Amendments made under section 239 of the Telecommunications Act 2001" |
| ISBN / project | 978-1-991287-45-8 / PRJ0046469; "Public Version" | L3-5 | "ISBN: 978-1-991287-45-8" |
| Publication date | 26 June 2024 | L12 | "Date of publication: 26 June 2024" |
| Edition relationship | Final paper; follows Request for Views (18 May 2023) and Draft Decisions and Reasons (18 Dec 2023) | L16-27 | see table 3.1 |
| Commencement (exec summary) | 1 July 2024 | L106 | "The Code comes into effect on 1 July 2024." |
| Commencement (body) | amendments in force 1 July 2024 | L1171 | "250. The Code amendments will come into force on 1 July 2024." |
| Grace period (exec summary) | six months, 1 July 2024 to 1 January 2025 | L106 | "we have prescribed a six-month grace period starting on 1 July 2024 and ending on 1 January 2025" |
| Grace period (body) | "enforcement grace period", six (6) months, ends 1 January 2025 | L1171 | "there will be an enforcement grace period of six (6) months to allow for providers to come into full compliance with the Code, as amended. The grace period will end on 1 January 2025." |
| What the grace period applies to | "the amendments to the Code" / "the Code, as amended"; no obligation-by-obligation list | L106, L108, L1172 | "During the grace period, providers will be considered to have complied with the requirements of the Code if they complied with the Code as it was prior to these amendments." |
| Immediate changes allowed | providers may apply changes at once, incl. removed obligations | L1174 | "This approach will also allow providers to make changes immediately, including where obligations have been removed such as the exclusion of business landline services." |
| Reason for dates | feedback on Previous Code commencement + Facilities feedback (fn 137 Bupa p 5) | L1174-1175 | "These dates reflect consideration of feedback we received regarding the commencement date of the Previous Code, as well as feedback through this engagement process regarding the application of the Code to Facilities.137" |
| Tracked version | separate "Amendment Version 2024" published | L106, L123 | "6 Commission 111 Contact Code (Amendment Version 2024)." |

No other transition period is stated in D06. D06 does not state a period between publication and commencement in words (26 June 2024 and 1 July 2024 are printed separately, L12 and L106).

### Every other date in D06 and what it marks

| Date | Marks | Line | Verbatim |
|---|---|---|---|
| November 2018 | Act amended by Telecommunications (New Regulatory Framework) Amendment Act 2018 | L139 | "8. In November 2018, the Act was amended by the Telecommunications (New Regulatory Framework) Amendment Act 2018." |
| 17 July 2020 | Spark "Submission on draft 111 Contact Code" (the 2020 draft) | L833 | "Spark “Submission on draft 111 Contact Code” (17 July 2020) paras 94-96 and Appendix A." |
| 17 November 2020 | Previous Code and 2020 Decisions and Reasons paper published | L99, L142, L17-18, L252 | "10. On 17 November 2020 we published the Previous Code accompanied by its decisions and reasons paper" |
| November 2020 / February 2021 / August 2021 (months only) | glossary: published / came into effect / section G (now H) into effect | L45 | "The 111 Contact Code published in November 2020 which came into effect in February 2021 (section G (now section H) of the Code came into effect in August 2021)" |
| 31 December 2020 | date of the 159,000 copper figure | L438 | "as opposed to 159,000 at 31 December 2020" |
| 1 February 2021 | Previous Code came into force | L142 | "The Previous Code came into force on 1 February 2021, and section G (now section H) came into effect on 1 August 2021.11" |
| 10 February 2021 | initial deadline for providers to contact customers (Previous Code cl 7.3); reference now removed | L744, L760, L295-296 | "“10 February 2021”, which was the initial deadline for providers to contact their customers following the Previous Code’s commencement" |
| 1 August 2021 | section G (now section H) came into effect | L142 | as above |
| 2021/22 | "code disclosure year" whose conclusion preceded the compliance evaluation | L166, L1096 | "13 Following the conclusion of the 2021/22 code disclosure year." |
| Throughout 2022 | compliance engagement work | L161 | "14. Throughout 2022 we undertook compliance engagement work to promote compliance with the Previous Code." |
| 30 November 2022 | (a) evaluation of compliance commenced; (b) annual disclosures due date; (c) date of Spark "Feedback on 111 Contact Code" | L161, L1089, L610 | "On 30 November 2022 we commenced an evaluation of compliance with the Previous Code.13" ; "Following annual disclosures being provided to us by 30 November 2022 we conducted an industry-wide review of compliance with the Code." |
| May 2023 / 18 May 2023 | review commenced; Request for Views paper published | L83, L162, L164, L19 | "15. On 18 May 2023 we commenced a review of the Previous Code as it had been in force for two years" ; "16. On 18 May 2023 we published our Request for Views paper." |
| 15 June 2023 | Consumer NZ RfV submission | L706, L971 | "Consumer NZ “Submission on the 111 contact Code Review Request for Views” (15 June 2023) pages 1 & 2" |
| 16 June 2023 | RfV submissions of 2degrees, WISPANZ, NZ Police, One NZ, Whaikaha, DPA, Grey Power, Spark | L378-379, L610, L705, L788, L863 | "2degrees “Submission on 111 Contact Code Review Request for Views” (16 June 2023) page 1" |
| 19 June 2023 | TCF RfV submission (as cited by D06) | L610, L790, L887 | "TCF “Submission on 111 Contact Code Review Request for Views” (19 June 2023) paras 11-14" |
| December 2023 / 18 December 2023 | Draft Amended Code and Draft Decisions and Reasons paper published | L86, L176, L20-23 | "20. On 18 December 2023, we published the Draft Amended Code alongside the Draft Decision and Reasons paper" |
| late 2023/early 2024 | when the accepted-applications data point came to the Commission's attention | L1040 | "It came to our attention that it would be valuable information in late 2023/early 2024, as we were processing and analysing the latest 111 disclosure data." |
| 23 February 2024 | ACA submission on draft | L207, L490 | "ACA “Submission on draft amended 111 Code and draft decisions and reasons paper” (23 February 2024) pages 2-4" |
| 25 February 2024 | RWNZ submission on draft | L197, L402 | "RWNZ “Submission on draft amended 111 Code and draft decisions and reasons paper” (25 February 2024) pages 1-3" |
| 29 February 2024 | Ryman submission on draft | L199, L488 | "Ryman “Submission on draft amended 111 Code and draft decisions and reasons paper” (29 February 2024) pages 3-5" |
| 1 March 2024 | submissions on draft of Bupa, Chorus, TCF (two documents), RVA, Summerset, Age Concern ("ACNZ"), NZ Police | L197-207, L1165 | "Chorus “Submission on draft amended 111 Code and draft decisions and reasons paper” (1 March 2024) page 2" |
| 31 March 2024 | date of the 51,000 copper figure | L438 | "There are 51,000 voice-only copper connections at 31 March 2024" |
| 26 June 2024 | this paper, the Code 2024 and the Amendment Version 2024 published | L12, L24-25 | "26 June 2024 ISBN 978-1-991287-44-1 Commission 111 Contact Code 2024" |
| 1 July 2024 | Code amendments in force; grace period starts | L106, L1171 | above |
| 1 January 2025 | grace period ends | L106, L1171 | above |
| 30 November of each disclosure year | annual provider disclosure deadline (Previous Code section J, now section K) | L983 | "201. The Previous Code required that no later than 30 November of each disclosure year, a provider must disclose to the Commission specified information in respect of the preceding disclosure year.116" |
| 2023-24 / 2023/24 | ARRC Agreement edition named in text | L502, L515 | "Age-Related Residential Care Services Agreement 2023-24" ; "51 Clause 19.6 of the 2023/24 ARRC Agreement. See pages 63 & 64" |
| 2022-23, 1 Sept 2022 | appear only inside the URL of the same footnote 51 | L515 | "ARRC-Agreement-2022-23-effective-1-Sept2022-FINAL-for-website.pdf" |

Statute years named: Telecommunications Act 2001; Health and Disability Services (Safety) Act 2001; Retirement Villages Act 2003; Companies Act 1993; Partnership Law Act 2019; Privacy Act 2020; Legislation Act 2019 (L1213).

## 2. Every number in D06 (complete list)

Whole-file search for `%`, `$`, "per cent", "percent", "million", "thousand" and comma-grouped numbers returns ONLY the two copper figures at L438. D06 prints NO count of vulnerable consumers, NO registration or application counts, NO complaint counts, NO call volumes, NO percentages, NO dollar costs, NO survey results, NO battery-price or battery-size figures. (Complaints are mentioned without numbers: L1023 "nor have we received any evidence or complaints".)

| Line | Figure | Unit / period | What it measures | Source attributed | Rounded vs exact; part of a total? |
|---|---|---|---|---|---|
| L438 | 51,000 | voice-only copper connections, at 31 March 2024 | copper landline connections | none cited (Commission statement, no footnote) | prose only; no table; round thousands |
| L438 | 159,000 | voice-only copper connections, at 31 December 2020 | same series, earlier date | none cited | prose only; decline/difference NOT printed ("declined substantially") |
| L438 | "more than three years" | years the Code has operated | duration | Commission | hedged ("more than") |
| L162 | "two years" | time Previous Code had been in force at 18 May 2023 | duration | Commission | words only |
| L169 | 18 submissions from 17 different parties | submissions on Request for Views | count | Commission; fn 14 names 17 submitters ("The submitters included:") | printed total 18; the footnote lists 17 names; D06 does not say which party made two |
| L179 | 10 parties | submissions on Draft Decisions and Reasons paper | count of parties | Commission; para 22 names ten | number of submissions (documents) not stated; TCF is cited for two differently titled documents (L197, L203) |
| L795 | "only received one submission" | submissions on the application-form topic (draft round) | count | Commission (Age Concern) | words |
| L8-11 | 4 | Commission members named on cover | count (not printed as a number) | - | - |
| L255-349 | 11 | Table 1 IDs (rows 1-11) | amendments summarised | Commission | fn 26 adds "a small number of editorial refinements" outside the table |
| L357-360 | 3 | exclusions (a)-(c) from Previous Code 'retail landline services' | list | Previous Code | - |
| L459-463 | 3 | Scenarios A, B, C | billing-relationship scenarios | Draft paper paras 92-95 | - |
| L479 | "four levels" | levels of age-related residential care | rest home, age-related hospital care, dementia care, psychogeriatric care | Bupa (fn 44, page 3) | words |
| L479, L500, L620, L651, L663 | 24/7 | availability of care / monitoring | - | Bupa; RVA; ACA/Bupa/RVA/Ryman; Commission definition | - |
| L515 | Clause 19.6; pages 63 & 64 | ARRC Agreement reference | - | fn 51 | - |
| L539 | "24 hours or longer" | continuous period in "hospital care" limb of health care services | threshold | H&D Act s 4(1) (fn 57, L545) | "or longer" |
| L539-550 | 4 | kinds of "health care services" (85.1-85.4) | list | H&D Act | - |
| L569-574 | 4 | worked Examples 1-4 of Facilities | list ("four examples") | Commission | words at L569 |
| L608 | 3 | circumstances in Previous Code cl 21 (21.1-21.3) | list | Previous Code (fn 62) | - |
| L683, L724, L744, L755, L762, L1080, L1088, L1108 | 12 months | frequency of Code information to customers | "at least every 12 months" / "at least once every 12 months" | Previous Code cl 7.3; Code cl 9.3 | qualifier "at least" |
| L840, L1135, L1144 | eight-hour | "a continuous eight-hour period" = minimum period | battery/means run time | Previous Code cl 4 (now Code cl 6) (fn 98) | words; unchanged by review |
| L310, L840, L842, L845, L853, L859, L869, L873, L874 | 36 months | replace (old rule) / test (new rule) interval | "at least once every 36 months" | Previous Code cl 29.3; Code | qualifier "at least" |
| L848, L874 | annual / once a year | monitoring that means remains appropriate and functional | "on at least an annual basis"; "at least once a year" | Previous Code cl 33 / section G3 (now H3) | qualifier "at least" |
| L342, L999, L1006, L1021 | 10 working days | (a) decision time on a complete application (Previous Code cl 18); (b) provisioning-time threshold above which a reason must be disclosed | time limit / reporting threshold | Previous Code; Code | L999 prints "within working 10 days"; threshold is "longer than 10 working days" |
| L1231 | 30 working days | submissions window after public notice of a draft code | statutory time limit | Act s 239(3) (Appendix A) | "not later than" |
| L106, L1171 | six / six (6) months | grace period | duration | Commission | words at L106; "six (6)" at L1171 |
| L1052-1072 | 13 | topics (218.1-218.13) on which no further discussion is included | list | Commission | - |
| L1203 | "1 or more" | things the code may do (s 238(4)) | statute text | Act | - |
| L1246 | Sections 241 to 245; Part 4B; section 156S | statute cross-refs | - | Act | - |
| L186, L189 | root=320897; root=347360 | URL parameters for the two submission pages | not data | - | - |
| L101-103 | 316170; 343748; 338199 | URL file ids (RfV paper; tracked Draft Amended Code; Draft Decisions paper) | not data | - | - |

Rounded-prose versus exact-table check: D06 has no numeric table, so no figure is printed both rounded in prose and exactly in a table or footnote. The only repeated quantities are the rule parameters above (12 months, 36 months, eight-hour, 10 working days, six months), which are the same value at every occurrence.

## 3. Tables

### 3.1 Associated documents (L15-27) - columns: Publication date | Reference | Title

| Publication date | Reference | Title |
|---|---|---|
| 17 November 2020 | ISBN 978-1-869458-52-2 | Commission 111 Contact Code |
| 17 November 2020 | ISBN 978-1-869458-53-9 | Final Decisions and Reasons paper |
| 18 May 2023 | ISBN 978-1-991085-00-9 | Request for views paper |
| 18 December 2023 | ISBN 978-1-991085-62-7 | Draft Commission 111 Contact Amendment Code 2023 |
| 18 December 2023 | ISBN 978-1-991085-63-4 | Draft Decisions and Reasons paper |
| 26 June 2024 | ISBN 978-1-991287-44-1 | Commission 111 Contact Code 2024 |
| 26 June 2024 | ISBN 978-1-991287-43-4 | Commission 111 Contact Code (Amendment Version 2024) |

Seven rows. D06's own ISBN (978-1-991287-45-8, L3) is not a row.

### 3.2 Glossary "Table of terms and abbreviations" (L30-54)

ACA = Aged Care Association New Zealand; Age Concern = Age Concern New Zealand; Act = Telecommunications Act 2001; Bupa = Bupa Villages and Aged Care New Zealand; Code = "The Commission 111 Contact Code (2024)"; Commission = Commerce Commission; DPA = Disabled Persons Assembly; Facilities = "Residential care or assisted living facilities, including but not limited to retirement villages, rest and nursing homes, long-stay hospitals, dementia units and psychogeriatric units" (L41); FWA = Fixed Wireless Access; H&D Act = The Health and Disability Services (Safety) Act 2001; NZ Police = New Zealand Police; [second row labelled "Code", L44-45] = the November 2020 code; Provider = "A supplier or suppliers of a retail residential landline services to a consumer" (L47); Retirement Villages Act = Retirement Villages Act 2003; RVA = Retirement Villages Association; RWNZ = Rural Women New Zealand; Ryman = Ryman Healthcare Limited; Summerset = Summerset Group Holdings Limited; TCF = New Zealand Telecommunications Forum; WISPANZ = Wireless Internet Service Providers Association of New Zealand Inc.

Not in the glossary but used: "ACNZ" (L199, L201), Chorus, 2degrees, One NZ, Spark, Whaikaha, Consumer NZ, Grey Power, "Previous Code", "Draft Amended Code", Te Whatu Ora (Health New Zealand), Hato Hone St John.

### 3.3 Table 1: Summary of amendments to the Previous Code (L251-349) - columns: ID | Subject of change | Final decision | Reference in this paper

No units; no totals; text table. Footnotes: fn 26 (L253) qualifies the whole table: "26 We have also made a small number of editorial refinements and drafting improvements to the Code." fn 27 (L254) qualifies row 1.

| ID | Subject of change | Final decision (bullets, verbatim start) | Reference | Lines |
|---|---|---|---|---|
| 1 | Application of the Code to landline services | (a) "State that the Code does not apply to business landline services as defined in the Code. The Code refers to residential landline services instead of retail landline services and has minor changes to defined terms." (b) "Specifically exclude copper landline services (as defined in the Code)27 from the definition of residential landline services." | Paras 42-66 | L256-265 |
| 2 | Application of the Code to health care service providers and operators of retirement villages | (a) "State that the Code does not apply to “health care services”, under the Health and Disability Services (Safety) Act 2001." (b) "Clarify that the Code does apply to Retirement Villages where they provide telecommunications services." | Paras 67-94 | L266-276 |
| 3 | Application of the Code to medical alarms | (a) "State that ‘medical and other safety alarms’, as defined in the Code are a valid means of contacting the 111 emergency service." (b) "State that contact to the 111 emergency service through a defined ‘qualified third party’ is acceptable under the Code." | Paras 95-121 | L280-288 |
| 4 | Communication of code-related information | "Add clarification that consumers are not able to purchase or switch between residential landline services or technology without being aware of the information regarding the Code." | Paras 123-136 | L288-293 |
| 5 | Consumers preferred method of contact | "Remove an outdated reference (’10 February 2021’) in the requirement regarding provision of information by providers to their customers." | Paras 137-143 | L293-298 |
| 6 | Application form template and requirements | (a) template "provided by the Commission for guidance purposes only and that providers can modify it"; (b) "Updated the template to better align it with the requirements under clause 18 of the Code and to simplify it for usability."; (c) "The template is not part of the Code and will be made available on the Commission’s website to avoid any inference it is compulsory." | Paras 146-160 | L298-308 |
| 7 | Replacement of appropriate means supplied to vulnerable consumers | "Remove the requirement to replace appropriate means at least every 36 months and substitute it with the requirement for the provider to test appropriate means at least every 36 months." | Paras 164-173 | L308-312 |
| 8 | When a means can be considered appropriate | (a) means "will be deemed to be appropriate, whether the vulnerable consumer accepts it or not"; (b) "State that a consumer’s application can be considered withdrawn if they reject the appropriate means which complies with the Code requirements."; (c) "Require providers to make vulnerable consumers aware of the implications of rejecting the appropriate means in the application form."; (d) "Require providers to disclose the number of accepted and withdrawn applications during the disclosure year and to maintain accurate records of this information." | Paras 174-191 | L312-329 |
| 9 | Vulnerable status when moving premises | (a) "Remove the automatic loss of vulnerable status when moving premises."; (b) provider "may check the consumer’s status and potentially require them to re-apply if something material has changed" | Paras 194-200 | L331-338 |
| 10 | Disclosure of time taken to provide appropriate means to consumers | "Replace the requirement to disclose an overall average provisioning time with a requirement to report on how long each individual install took for each vulnerable consumer (from the date each application was accepted). If an install took longer than 10 working days, providers must briefly describe why." | Paras 203-211 | L338-344 |
| 11 | Disclosure of accepted applications | "Add a new requirement to disclose the number of accepted applications during the disclosure year and to maintain accurate records of this information." | Paras 212-216 | L344-349 |

Row notes: row 8(d) and row 11 both state the accepted-applications disclosure. Row 3 uses the term ‘medical and other safety alarms’; the body uses ‘managed medical or safety alarms’ (L627). fn 27 (L254): "27 Copper landline service means a landline service provided over a copper line using traditional analogue copper voice technology, but excludes any voice service that is provided using technologies (hardware or software) that rely on mains powered electricity at the premises."

### 3.4 Figure 1 (L160)

Caption only. No content extracted (gap).

## 4. Submitters, and each decision

### 4.1 Complete list of submitters named

D06 names two consultation rounds only. The word "cross-submission" does not occur in D06.

**Request for Views (RfV) round** - L169 "17. We received 18 submissions from 17 different parties in response.14"; fn 14 (L186) lists, in this order: 2degrees, Anonymous, Business Technology Group, Consumer NZ, Disabled Persons Assembly, Fire and Emergency, Grey Power, Mercury, MyRepublic, NZ Police, New Zealand Telecommunications Forum, One NZ, Sky, Spark, Tech Users Association of New Zealand, Whaikaha and Wireless Internet Service Providers Association of New Zealand (17 names; introduced by "The submitters included:").

| RfV submitter | Cited individually in D06? | Citation as printed (date; page/para) | Lines |
|---|---|---|---|
| 2degrees | yes | 16 June 2023; page 1 | L378, L610 |
| WISPANZ | yes | 16 June 2023; page 5 (L378), page 3 (L889) | L378, L889 |
| NZ Police | yes | 16 June 2023; page 2 | L379 |
| Spark | yes - TWO differently titled documents | “Feedback on 111 Contact Code” (30 November 2022) paras 13-21, 41-45, 12, 35-39; “Submission on 111 Contact Code Review Request for Views” (16 June 2023) para 26 | L610, L789, L887, L1010, L863 |
| TCF | yes | 19 June 2023; paras 11-14, 21-22, 7 | L610, L790, L887 |
| One NZ | yes | 16 June 2023; paras 7-10 | L610 |
| Whaikaha | yes | 16 June 2023; pages 1 & 2, page 1 | L705, L790, L1138 |
| DPA | yes | 16 June 2023; page 5 | L705, L706, L1138 |
| Consumer NZ | yes | 15 June 2023; pages 1 & 2, page 3 | L706, L971 |
| Grey Power | yes | 16 June 2023; page 3 | L788 |
| Anonymous, Business Technology Group, Fire and Emergency, Mercury, MyRepublic, Sky, Tech Users Association of New Zealand | no - named only in fn 14 | - | L186 |

D06 introduces Spark's 30 November 2022 "Feedback" under "Submissions on our Request for Views paper" (L602 with fn 63) and "In response to our Request for Views paper" (L780 with fn 90; L991 with fn 121). D06 does not say which party accounts for the 18th submission.

**Draft Decisions and Reasons / Draft Amended Code round** - L179-180 "22. We received submissions from 10 parties on our Draft Decisions and Reasons paper:" Age Concern, ACA, Bupa, Chorus, TCF, NZ Police, RVA, RWNZ, Ryman, Summerset. L182: "Some of the TCF’s members did not provide their own individual submissions as the TCF’s submission represents views of its members on the amendments to the Previous Code."

| Draft-round submitter | Date as cited | Pages/paras cited | Lines (examples) |
|---|---|---|---|
| Age Concern (also printed "ACNZ" at L199, L201) | 1 March 2024 (L973 prints "March 1 2024") | pages 2, 3, 4 | L203, L400, L707, L813, L864, L907, L973, L1034, L1098 |
| ACA | 23 February 2024 | pages 2, 3, 4 | L207, L490, L504, L512, L516, L634 |
| Bupa | 1 March 2024 | pages 2-5; "para 7a" (L492); "para 17" (L543) | L197, L205, L486, L492, L496, L506, L512, L543, L636, L1175 |
| Chorus | 1 March 2024 | page 2 | L197, L406 |
| TCF - “Submission on draft amended 111 Code tracked changes” | 1 March 2024 | pages 12, 13, 14, 16, 21, 22, 23 | L197, L199, L201, L408, L614, L633, L727-728, L769, L866, L909, L972 |
| TCF - “Submission on draft amended 111 Code and draft decisions and reasons paper” | 1 March 2024 | page 2 | L203, L482, L1100 |
| NZ Police | 1 March 2024 | page 1 | L1165 |
| RVA | 1 March 2024 | pages 1, 2 | L199, L207, L494, L510, L513, L518, L575, L638 |
| RWNZ | 25 February 2024 | pages 1-3 | L197, L201, L402, L404, L1139 |
| Ryman | 29 February 2024 | pages 1-5 | L199, L205, L488, L494, L508, L541, L638, L644 |
| Summerset | 1 March 2024 | pages 1-3; "para 6" (L512); "para 10" (L642) | L199, L205, L484, L508, L512, L520, L642 |

Group labels used: "Aged residential care facilities and retirement village providers (Bupa, Ryman and Summerset)21 and associated advocacy groups (the ACA and the RVA)" (L195).

### 4.2 Decisions and amendments (Chapter 4), in paper order

Column "Final vs draft" records D06's own words where it uses them.

**(1) Application to landline services - paras 42-66 (L364-449)**
- RfV input: 2degrees and WISPANZ suggested residential-only (L364); NZ Police on resiliency "in all areas" (L367).
- Draft decision (L370-374): business landline services defined; 'retail landline services' becomes 'residential landline services', 'premises' amended; Code applies only to residential landline services.
- Draft-round submissions: Age Concern supported (L383 "46. Age Concern supported our proposed amendments.31"); RWNZ objected re small rural businesses with residents and made three suggestions 48.1-48.3 (L384-389); Chorus recommended keeping the word ‘retail’ (L392); TCF suggested explicit copper exclusion and, "Alongside this suggestion", informing consumers of the code when first contracting for a copper landline service (L393).
- Final decision (L396-418): "51. We have amended our draft decision in relation to the application of the Code." Items 51.1 business landline services defined; 51.2 new defined term residential landline services; 51.3 definition includes the term ‘retail’; 51.4 definition of premises amended "(used or intended for residence, as opposed to occupation)"; 51.5 "the Code does not apply to business landline services or copper landline services (as currently defined in the Code)"; 51.6 "clause 8.1 of the Previous Code is removed."
- Final vs draft: DIFFERENT (stated). Added since draft: ‘retail’ (Chorus, agreed L433), copper landline exclusion (TCF, agreed L434), removal of clause 8.1 (naked broadband information; L445).
- Declined: all three RWNZ suggestions (L420-431; "We disagree with RWNZ" L423); TCF's additional copper-contracting information proposal (L442 "we disagree with the TCF’s additional proposal", repeated L449).
- Clauses: Previous Code cl 8.1 removed; information in "clause 6" (Previous Code numbering) referred to at L442, L449.

**(2) Health care service providers and retirement villages ("Facilities") - paras 67-94 (L454-577)**
- Origin: "67. Outside of submissions on our Request for Views paper, we were made aware of concerns" (L454).
- Draft paper position: a "preliminary view", no amendment proposed, submissions invited (L464 "70. It was our preliminary view that the party who holds the direct billing relationship with the consumer (ie, the Facility in scenarios A and B) is subject to the Previous Code"; L469 "we did not consider that our views on this point required an amendment be made"). Scenarios A, B, C at L459-463; cross-ref fn 36 = Draft paper paras 92-95.
- Draft-round submissions: TCF agreed with the preliminary views (L474); Summerset: billing relationship "irrelevant" (L475); Bupa: care relationship (L475); Ryman: "broader concept of risk and existing risk-mitigations" (L475); ACA, Bupa, RVA, Ryman: difference between aged residential care and independent living (L476-477); ACA, Bupa, Ryman, Summerset recommended excluding aged residential care facilities (L499); RVA recommended exempting retirement villages with emergency call systems monitored 24/7 (L500); Te Whatu Ora obligations (L501, fn 49 lists ACA, Ryman, Summerset, Bupa, RVA); RVA on the ARRC Agreement and Major Incidents and Health Emergency Plan (L502); ACA, RVA, Ryman gave examples of backup systems (L502); Summerset on resident confusion (L503); Ryman on industry-wide collaboration (L523); Bupa: landline offerings "may be withdrawn" (L524).
- Final decision (L525-531): 82.1 a supplier offering residential landline services meets the definition of ‘provider’ "and may have obligations under the Code"; 82.2 "amend the definition of ‘provider’ to set out that the Code does not apply to providers that also supply ‘health care services’ as defined in the Health and Disability Services (Safety) Act 2001"; 82.3 "maintain that, subject to the matters discussed in paragraph 88 below, the Code does apply to ‘retirement villages’ under the Retirement Villages Act 2003"; 82.4 billing relationship "is a relevant consideration" for providers that do not provide ‘health care services’.
- Final vs draft: the draft held a view with no amendment; the final amends the ‘provider’ definition. D06 does not use "changed/retained" here. Agreement recorded: "83. We agree with Summerset, Bupa and Ryman that the care relationship should be considered" (L533).
- Declined: excluding all retirement villages (L560 "By excluding all retirement villages, there would be an increased risk"); Ryman's collaboration idea "is out of scope of the Code and its review" (L566).
- Response to Bupa: section J quote (L567).
- "health care services" limbs 85.1-85.4 (L539-550): hospital care; residential disability care; rest home care; specified health or disability services.
- Retirement village operator with direct billing relationship must comply incl. 88.1-88.3 (L556-558). Unit-title developments: operator not captured (L562-564, fn 58 RVA p 2).
- Examples 1-4 (L570-577): Ex 1 rest home + hospital + dementia + psychogeriatric care: no obligations "even if they provide landline services"; Ex 2 independent village, no landline offered: not in scope; Ex 3 independent village selling landline: has obligations to residents it sells to; Ex 4 mixed: obligations only "for residents purchasing a residential landline service who are also living in the retirement village".

**(3) Medical alarms - paras 95-121 (L581-667)**
- RfV input: 2degrees, Spark (Feedback 30 Nov 2022), TCF, One NZ suggested medical alarms be explicitly mentioned as appropriate means (L602, fn 63 L610).
- Draft paper position (L603-605, fn 64 = Draft paper paras 103-105): no Code amendment; 103.3 "it would be inappropriate to include a blanket statement in the Code including all medical alarms as appropriate means."
- Draft-round submissions: TCF: add the para 103.1 clarification to the Code (L607); TCF: 'contact 111 emergency service' can mean access via a medical alarm provider (L617); ACA, Bupa, RVA, Ryman described call systems (L619-620); "The RVA and Ryman recommended these systems should be recognised in the Code" (L620); Summerset: none of its residents would meet the definition (L623); Ryman: redefine "vulnerable consumer" (L624).
- Final decision (L625-647): 109.1 define ‘managed medical or safety alarms’; 109.2 amend clause 21 of the Previous Code (now clause 25) so a consumer with such an alarm has a means and "will not qualify as a vulnerable consumer"; 109.3 amend the same clause so a provider may conclude a consumer has a means "if the consumer already has a device or technology which meets the requirements under the Code"; 109.4 define ‘qualified third party’; 109.5 amend ‘111 emergency service’ "to note that this service can be contacted directly by a consumer or via a qualified third party."
- Final vs draft: draft made no amendment; final makes five. No "changed/retained" phrase; L648 says "we still believe".
- Agreement recorded: TCF (L649 "111. We agree with the TCF"); TCF and RVA (L658 "116. We also agree with the TCF and the RVA"); "This approach aligns with Ryman’s feedback" (L667).
- Exclusion inside the definition: L651 "Alarms which send an alert to preprogrammed contacts, such as family or friends would not meet the requirements."

**(4) Communication of code-related information - paras 123-136 (L690-740)**
- RfV input: Whaikaha and DPA (accessibility); Consumer NZ and DPA (not adequately informed) (L692).
- Draft decision (L694-695): explicit requirement that clause 6 information be given so a customer cannot purchase or switch without being aware of it (proposed as an addition to clause 7.4, per L711).
- Draft-round submissions: Age Concern supported and suggested complaints/dispute information be equally visible (L698); TCF suggested a clause that a link plus description satisfies clauses 5 and 6 (L710); TCF suggested removing the proposed addition to clause 7.4, calling it “an overly specific additional requirement in the Code” (L711).
- Final decision (L713-716): 129.1 amend clause 7.4.2 of the Previous Code (now clause 9.4.2) to state “the customer switches to a different residential landline service or technology with the same provider that may not work in a power failure”; 129.2 add a new clause (clause 10, L739).
- Final vs draft: adapted - L739 "we have also adapted our approach on the inclusion of our proposed amendment ... It is now included as clause 10 in the Code."
- Declined: Age Concern's point needs "no amendments" (L719); TCF's link proposal and removal of clause 7.4.2 (L726-731 "We do not agree with the TCF"). fn 84 (L747) records that the Commission clarified TCF's marked-up comment related to clause 7.4.2.

**(5) Consumers' preferred method of contact - paras 137-143 (L744-762)**
- Draft-round submission: TCF proposed removing “if the provider does not know the customer’s preferred method of contact” for “operational simplicity” (L752).
- Final decision (L753-755): amend the first sentence of clause 7.3 of the Previous Code (now clause 9.3) to read “provided to all customers of a residential landline service at least once every 12 months” (removes "10 February 2021").
- Declined: TCF's removal ("140. We disagree with the TCF’s suggestion", L757).
- No draft decision on this topic is described in D06 under the "Context and draft decision" heading (L743-745 give context only).
- L758: "(as suggested by RWNZ above)" - the RWNZ language point is printed later, at L1125 (para 237).

**(6) Application form template - paras 144-160 (L766-823)**
- RfV input: Grey Power, Spark, Whaikaha, TCF: template not accessible, too long (L780).
- Draft decision (L784-787): 149.1 no longer provide the template as Attachment A, upload to website for optional use; 149.2 amend guidance note in Section F2 (now Section G2).
- Draft-round submissions: "150. We only received one submission on this topic. Age Concern supported our proposed amendment" (L795).
- Final decision (L796-800): "we have maintained our draft decision" - 151.1 remove ‘Attachment A – Application form to be considered a vulnerable consumer’; 151.2 amend guidance note; 151.3 publish an amended application form as an editable template.
- Final vs draft: MAINTAINED (stated). Additional non-Code action: template realigned to clause 14 (now 18) and simplified (L802, L821).

**(7) Replacement of appropriate means - paras 161-173 (L829-876)**
- RfV input: Spark (16 June 2023, para 26): 36-month replacement "in some cases too often" (L842).
- Draft decision (L843-846): 165.1 remove the clause 29.3 requirement to replace at least once every 36 months; 165.2 "instead require providers to replace the appropriate means when the device no longer meets the minimum requirements under the Code."
- Draft-round submissions: Age Concern supported (L850); TCF: helpful but providers "would now need to know how long batteries are lasting"; suggested replacement every 36 months "if the device’s performance was unknown" (L853).
- Final decision (L857-869): 169.1 remove the replace-every-36-months requirement (D06: "clause 29.3 of the Previous Code (now clause 33.3 of the Code)"); 169.2 "require providers to test the appropriate means at least once every 36 months"; 169.3 clarify that providers must ensure the means remains appropriate and functional.
- Final vs draft: draft 165.2 = replace when no longer compliant; final 169.2 = test at least once every 36 months. No "changed/retained" phrase is used.
- Declined: TCF's unknown-performance replacement wording (L873 "we disagree with the TCF’s proposed changes").
- Scope notes: tests "must be at no cost to the customer"; amendment "doesn’t replace" the annual monitoring requirement (L874).

**(8) When a means can be considered appropriate - paras 174-191 (L880-939)**
- RfV input: Spark and TCF on compliance uncertainty (L883); WISPANZ's battery-backup example (L883).
- Draft decision (L894-897): 177.1 means deemed appropriate if requirements met, accepted or not; 177.2 require providers to make vulnerable consumers aware of the implications of rejecting (drafted as clause 6.6 of the Draft Amended Code, L906).
- Draft-round submissions: Age Concern supports, with concern about appropriateness (L901); TCF welcomed 177.1 (L902); TCF suggested the application "should be considered withdrawn or declined" (L904); TCF disagreed with clause 6.6 upfront disclosure (L906).
- Final decision (L914-919): 183.1 deemed appropriate; 183.2 "a consumer’s application can be considered withdrawn if they reject the appropriate means which complies with the Code requirements"; 183.3 implications to be given "in the vulnerable consumer application form"; 183.4 record-keeping of withdrawn applications; 183.5 disclosure of the number of withdrawn applications.
- Final vs draft: DIFFERENT - L936 "we have removed our previous proposed amendment to clause 6 of the Previous Code (now clause 8 of the Code), and instead require the information to be communicated ... in the vulnerable consumer application form." 183.2, 183.4, 183.5 are new since the draft.
- Agreement recorded: TCF (L922, L936). Notes: consumer may reapply (L924); withdrawn applications are not in the provisioning-timing disclosure (L934).

**(9) Vulnerable status when moving premises - paras 192-200 (L943-978)**
- RfV input: Consumer NZ (L957).
- Draft decision (L954-956): remove clause 35.2 of the Previous Code; add a clause that the provider "may check" and "may require them to re-apply if something material has changed".
- Draft-round submissions: TCF: adjust clause 37 of the Draft Amended Code so obligations arise only on consumer notification (L959); "197. Age Concern do not agree with the proposed amendments when a consumer moves premises." (L962).
- Final decision (L966-967): "198. We have retained our draft decisions."
- Final vs draft: RETAINED (stated). Both TCF's and Age Concern's points declined (L976, L978).

**(10) Disclosure of time taken to provide appropriate means - paras 201-211 (L983-1025)**
- RfV input: Spark (Feedback 30 Nov 2022, paras 35-39) (L991, L998).
- Draft decision (L1004-1006): amend clause 38.7 of the Previous Code: stop disclosing the average; disclose provisioning timing for each new vulnerable consumer from acceptance date "with a reason for any provisioning that took longer than 10 working days".
- Draft-round submissions: Age Concern supported and suggested also disclosing application processing time (L1009-1015).
- Final decision (L1018-1021): "209. We have retained our draft decisions" - 209.2 "with a brief reason for any provisioning that took longer than 10 working days".
- Final vs draft: RETAINED (stated). Declined: Age Concern's processing-time disclosure (L1025).

**(11) Disclosure of accepted applications - paras 212-216 (L1029-1044)**
- No submitter named. Final decision (L1032-1038): 213.1 keep accurate records of accepted applications; 213.2 disclose the number accepted during the disclosure year.
- Final vs draft: NEW - L1040 "214. We note that this change wasn’t in our Draft Decisions and Reasons paper."
- L1044: "This data will allow us to see the number of temporary vulnerable consumers for the first time."

### 4.3 Chapter 5 - things discussed and NOT changed (L1047-1167)

- Thirteen RfV topics with no further discussion (L1051-1072): 218.1 Clearer vulnerable consumer eligibility; 218.2 Evidence of vulnerability; 218.3 Impact of satellite technology; 218.4 Network resiliency; 218.5 Providers withdrawing landline services; 218.6 Contribution of Local Fibre Companies to code-related costs; 218.7 High compliance costs; 218.8 Minimum period and limited market of appropriate means; 218.9 Clarification of what is out of scope; 218.10 Interested persons; 218.11 Providers identification of vulnerable consumers; 218.12 Use of term ‘vulnerable’ being potentially offensive; 218.13 Providers informing consumers about their right to independent information. Three stated reasons at L1049 (217.1-217.3).
- Lack of consumer awareness (L1078-1112): Age Concern and TCF said more could be done (L1092); Age Concern suggested "a national awareness campaign" (L1092); TCF suggested working with consumer advocacy organisations "eg, Grey Power" (L1104). Outcome: "228. We have retained our draft decision that the Previous Code requires no amendments" (L1107). Campaign noted, not adopted (L1112).
- Accessibility of code-related information (L1116-1131): DPA and Whaikaha suggested alternative formats "such as New Zealand Sign Language or Easy Read" (L1120); RWNZ on consumers without internet / English not first language (L1125). Outcome: "238. We have retained our draft decision" (L1127).
- Definition of minimum period (L1134-1151): TCF suggested “means a continuous eight-hour period when used as recommended” (L1144). Outcome: "244. We disagree with the TCF regarding the amendment of the definition of minimum period and as such haven’t amended the Previous Code." (L1147).
- Other communication channels (L1155-1162): NZ Police "sought correction of wording regarding the text option for contacting 111" (L1158). Outcome: acknowledgement only, no Code change (L1161-1162).

## 5. Defined terms, thresholds, exceptions, qualifiers

| Term / rule | Text | Line |
|---|---|---|
| vulnerable consumer (Act s 238(5)) | "12.1 is at particular risk of requiring the 111 emergency service (for example due to a known medical condition); and" / "12.2 does not have a means for contacting the 111 emergency service that can be operated for the minimum period in the event of a power failure." | L145-147; statute text L1210-1212; fn 60 L592-593 |
| Previous Code approach (three limbs) | 98.1 consumer of a specified telecommunications service; 98.2 at particular risk; 98.3 no means operable for the minimum period | L586-588 |
| Previous Code cl 21 (deemed to have a means) | “21.1 the consumer’s premises receives a copper landline service; 21.2 the consumer has unrestricted access to a mobile phone and that consumer’s premises has adequate mobile phone network coverage; or 21.3 the consumer has an uninterruptable power supply to maintain a means for contacting the 111 emergency service in a power failure”. | L608 |
| retail landline services (Previous Code) | "a landline service provided to a consumer at a premises, and excluded:" (a) mobile services; (b) naked broadband services; (c) applications that provide voice services over broadband services (such as Skype) | L355-360 |
| business landline services (Draft Amended Code wording) | “a telecommunications service that is primarily marketed and/or provided for businesses purposes, and includes a telecommunications service provided to: (a) a company, as defined in the Companies Act 1993; (b) a body corporate; (c) a corporation sole; (d) a sole trader; (e) a partnership, as defined in the Partnership Law Act 2019”. | L187 (fn 15) |
| copper landline service | fn 27 text above; restated L436 | L254, L436 |
| scope after amendment | "The Code will only apply to residential landline services that will not work in a power outage and that can be used to contact the 111 emergency services." | L447 |
| Facilities | glossary L41; para 67 list "retirement villages, rest and nursing homes, long-stay hospitals, dementia units and psychogeriatric units" | L41, L454 |
| health care services (H&D Act s 4(1)) | 85.1-85.4; "hospital care: this includes geriatric services provided for continuous periods of 24 hours or longer" | L537-550 |
| managed medical or safety alarm | "112. A ‘managed medical or safety alarm’ means a device, including a call bell, which provides a consumer the ability to contact a 24/7 monitored contracted service, and which meets the requirements in section H of the Code." | L651 |
| qualified third party | ‘company, as defined in the Companies Act 1993, as amended from time to time, or a person contracted to be available and is capable to contact 111 emergency services 24/7, such as via qualified retirement village staff and relevant medical alarm call centres’ | L663 |
| appropriate means | "a means that is appropriate for the vulnerable consumer’s specific circumstances, considering their physical, mental, and technical capabilities" (cl 26, now cl 30) | L830, L836 |
| minimum period | "a continuous eight-hour period" (cl 4, now cl 6) | L840, L860, L1134-1135 |
| disclosure deadline | "no later than 30 November of each disclosure year" | L983 |
| disclosure year | used, NOT defined in D06 | L166, L329, L983 |

Qualifiers attached to figures or rules (what the hedge attaches to):
- "at least" - 36 months (L310, L859, L869, L874); 12 months (L683, L755, L762); once a year (L874); "on at least an annual basis" (L848).
- "longer than" 10 working days - reporting trigger, strict (L342, L1006, L1021). "within working 10 days" - decision on a complete application (L999).
- "more than three years" - how long the Code has operated (L438). "we expect connection numbers will continue to decline" - forecast, attaches to future copper connections (L438).
- "may have obligations under the Code" - attaches to a supplier's obligations (L527). "may check" / "may require" - provider discretion on moving premises (L956, L967, L976 "This remains at the discretion of the provider.").
- "can be considered withdrawn" - permissive, attaches to the application (L916). "does not necessarily automatically lose" (L956).
- "that may not work in a power failure" - attaches to the service switched to, inside clause 9.4.2 (L715, L734).
- "some providers may only sell business landline services and thus will not be captured" (L426).
- "not all retirement villages have call systems or power backups" (L560). "not all Facilities will be considered providers" (L567).
- "Most medical and safety alarms" (L662). "most providers" - expectation that accepted-application data is already held (L1042 "We anticipate").
- "is likely to further limit awareness" - attaches to allowing written-only information (L758).
- "largely" - RfV providers' view (L169), Commission view (L173), draft submissions (L89). "Generally" (L89, L184).
- "little to no benefit" (L425, L431, L1025).
- "would not necessarily be considered non-compliant if they take more time" (L1002).
- "currently limited to people with hearing or speech difficulties" - attaches to the text option (L1162).
- "for the first time" - temporary vulnerable consumer numbers (L1044).
- fn 108 (L910): "We assume the TCF meant on the ‘provider’s website’." - Commission's assumption about TCF's wording “on the customer’s website” (L906).

Exceptions and exclusions stated: copper landline services and business landline services out of scope (L417); suppliers of health care services out (L529); retirement villages in, where the operator holds the direct billing relationship (L531, L556); unit-title developments where residents arrange their own telecommunications: operator not captured (L562-564); alarms alerting preprogrammed family/friends do not qualify (L651); naked broadband first-contract information no longer required (L445); withdrawn applications excluded from provisioning-timing disclosure (L934).

## 6. Outside organisations quoted with figures

D06 attributes NO numeric data to NZ Police, Fire and Emergency, the TCF, TDRS, Ryman, Summerset or any individual telecom provider. "TDRS" does not occur in D06. The only quantitative statement attributed to an outside organisation:

| Organisation | Statement | Period | Source cited by D06 | Line |
|---|---|---|---|---|
| Bupa | "age-related residential care occurs at four levels: rest home, age-related hospital care, dementia care and psychogeriatric care"; residents "need daily care 24/7" | none stated | fn 44: Bupa submission (1 March 2024) page 3 | L479, L496 |
| RVA | Age-Related Residential Care Services Agreement "2023-24" requires a Major Incidents and Health Emergency Plan | 2023-24 (URL in fn 51 says 2022-23, effective 1 Sept 2022) | fn 50 RVA (1 March 2024) page 1; fn 51 clause 19.6, pages 63 & 64 | L502, L513, L515 |
| RVA | retirement villages with emergency call systems "monitored 24/7" | none | fn 48 RVA page 2 | L500, L510 |
| TCF | proposed 36-month replacement if performance unknown; proposed “a continuous eight-hour period when used as recommended” | none | fn 102 TCF tracked changes page 21; para 243 (no footnote) | L853, L866, L1144 |
| Spark | 36-month replacement "in some cases too often" | none | fn 100 Spark (16 June 2023) para 26 | L842, L863 |
| (Commission, unsourced) | 51,000 voice-only copper connections at 31 March 2024; 159,000 at 31 December 2020 | two dates | no source or footnote given | L438 |

Organisations mentioned without figures: NZ Police (L367, L1158-1162), Fire and Emergency New Zealand (L186, L1162, L1226), Te Whatu Ora (L501), Hato Hone St John (L662), Grey Power (L780, L1104, L1110), Consumer NZ, DPA, Whaikaha, WISPANZ, 2degrees, One NZ, Chorus, RWNZ, ACA, Age Concern, Summerset, Ryman.

## 7. Statements about years/events; things stated two ways inside D06

1. Commencement wording: L106 "The Code comes into effect on 1 July 2024" versus L1171 "The Code amendments will come into force on 1 July 2024". Same date.
2. Grace period: L106 "six-month grace period starting on 1 July 2024 and ending on 1 January 2025" versus L1171 "an enforcement grace period of six (6) months ... will end on 1 January 2025". Same dates; "enforcement" appears only at L1171.
3. Duration in force: L162 "it had been in force for two years" (as at 18 May 2023) versus L438 "The Code has been operating for more than three years" (this paper).
4. 30 November 2022: L161 "On 30 November 2022 we commenced an evaluation of compliance with the Previous Code" versus L1089 "Following annual disclosures being provided to us by 30 November 2022 we conducted an industry-wide review of compliance with the Code." Footnotes 13 (L166) and 126 (L1096) both say "Following the conclusion of the 2021/22 code disclosure year."
5. Alarm term: Table 1 row 3 ‘medical and other safety alarms’ (L284) versus ‘managed medical or safety alarms’ (L627, L649, L651, L667).
6. Glossary: two rows labelled "Code" (L36, L44); body text uses "Previous Code" for the second.
7. Glossary dates by month ("November 2020", "February 2021", "August 2021", L45) versus exact dates in para 10 (17 November 2020, 1 February 2021, 1 August 2021, L142).
8. Provider definition: glossary "A supplier or suppliers of a retail residential landline services to a consumer" (L47) versus decision 82.2 excluding suppliers of health care services (L529).
9. ARRC Agreement edition: "2023-24" (L502) and "2023/24" (L515) versus the footnote URL "ARRC-Agreement-2022-23-effective-1-Sept2022" (L515).
10. TCF copper-contracting proposal rejected twice in near-identical words: L442 (para 63) and L449 (para 66).
11. Moving-premises clause numbers: L967 "remove clause 35.2 of the Previous Code (otherwise now clause 42.2 of the Code)" and, same line, "add a new clause 42 which states ...".
12. "clause 26": L948 (para 192.4) "resubmitted in accordance with clause 26" versus L836/L929 where clause 26 of the Previous Code is the appropriate-means clause ("Clause 26 of the Previous Code (now clause 30 of the Code)").
13. Annual monitoring source: L848 "clause 33 of the Previous Code requires providers to monitor ... on at least an annual basis" versus L874 "section G3 of the Previous Code (now Section H3 of the Code) (Requirement to monitor) ... at least once a year".
14. Section-G renumbering: "section G (now section H)" (L45, L142, L655, L922); "Section F2 ... (now Section G2 ...)" (L783, L787, L800); "section J of the Code (Section I of the Previous Code)" (L567); "Section J of the Previous Code (now section K of the Code)" (L992); "Section L of the Previous Code (now section M of the Code)" (L939). Section letters shift by one.
15. Reason wording for late provisioning: Table 1 "providers must briefly describe why" (L342); draft as restated "with a reason" (L1006); final "with a brief reason" (L1021).
16. Accepted-applications disclosure appears in Table 1 row 8 (L329, "accepted and withdrawn") and row 11 (L346); body places accepted applications under paras 212-216 only and withdrawn under 183.4-183.5.
17. "ACNZ" (L199, L201; 1 March 2024; page 4) is not a glossary alias; the glossary alias is "Age Concern" (L33). Age Concern's citations elsewhere carry the same date (1 March 2024) and pages 2-4; ACA's carry 23 February 2024.
18. Date format outlier: L973 "(March 1 2024)".
19. WISPANZ title variants: L378 "Submission on 111 Contact Code Review Request for Views" versus L889 "Submission on 111 Contact Code Request for Views". Name variants: L364 "Wireless Internet Service Providers Association New Zealand (WISPANZ)" versus glossary L54 and fn 14.
20. Draft paper named two ways: "Draft Decisions and Reasons paper" (L88, L177) and "Draft Decision and Reasons paper" (L176, L454, L1073, L1155).
21. L758 "(as suggested by RWNZ above)" - the RWNZ language point is at L1125, later in the paper.
22. Text option: L1155 quotes the draft paper, “the text option for contacting 111 is currently limited to people that are deaf, hearing or speech impaired.”; L1162 restates "the text option for contacting emergency services is currently limited to people with hearing or speech difficulties."
23. Heading "AMENDMENTS TO DEFINED TERMS" (L451) covers the Facilities and medical-alarm topics; the landline topic sits under "AMENDMENTS TO THE APPLICATION OF THE CODE" (L352).
24. Each-versus-all: L557 "the means provided must be appropriate for the needs of each vulnerable consumer at that premises" (see Shared ground for the Code's wording).

## 8. Cross-references out of D06

To the Draft Decisions and Reasons paper (D01) by paragraph:
- fn 36 (L467): "(18 December 2023) paras 92-95" - Facilities scenarios and preliminary view.
- fn 64 (L612): "paras 103-105" - medical alarms.
- fn 92 (L791): "para 61" - providers may keep using the template.
- fn 122 (L1011): "para 85" - clause 27.1 'reasonably practicable' and clause 18 ten working days.
- L1155: "In paragraph 187 of the Draft Decision and Reasons paper" - text option sentence.
- fn 134 (L1164): "See paras 155-162 of the Draft Decision and Reasons paper for our reasons." - minimum period.
- L1040: accepted-applications change "wasn’t in our Draft Decisions and Reasons paper".
- Draft Amended Code clause numbers: clause 6.6 (L906), clause 37 (L959), clause 7.4 addition (L711).

To the Request for Views paper (D02): fn 8 (L128) "paras 13 to 15"; fn 103 (L885) "para 41".

To the 2020 documents: fn 25 (L252) 2020 Decisions and Reasons paper (17 November 2020); fn 60 (L592) its paragraph 147; fn 94 (L832-833) Spark's 17 July 2020 submission on the 2020 draft Code, paras 94-96 and Appendix A.

Previous Code clause -> Code 2024 clause, as D06 states them:

| Previous Code | Code 2024 | Subject | Line |
|---|---|---|---|
| clause 4 | clause 6 | definitions ("minimum period") | L860 |
| clause 6 | clause 8 | information to be specified | L739, L762, L936, L1093 |
| clauses 6.2, 6.3, 7.3 | clauses 8.2, 8.3, 9.3 | home phone may not work in a power failure; 12-monthly reminder | L1095 |
| clause 7 | clause 9 | how information is provided | L729, L739-740, L1093 |
| clause 7.1 / 7.2 | clause 9.1 / 9.2 | website; point of sale | L1117, L1136 |
| clause 7.3 | clause 9.3 | 12-monthly direct information | L755, L760 |
| clause 7.4.2 | clause 9.4.2 | switching service/technology | L715, L734 |
| (new) | clause 10 | cannot purchase/switch without being aware | L739 |
| clause 8.1 | removed | naked broadband first-contract information | L418, L434, L445 |
| clause 9 | clause 12 | vulnerable consumer definition | L595 |
| clause 13 | clause 16 | accessible application process | L1137 |
| clauses 13-24 | (not mapped by D06) | application process | L775, L987 |
| clause 14 / 14.2 | clause 18 / 18.2 | complete application information | L802, L804, L812 |
| clause 18 | (not mapped by D06) | accept/decline within 10 working days | L999 |
| clause 21 | clause 25 | provider may conclude consumer has a means | L557, L629, L631, L649, L655 |
| clauses 25-30 | (not mapped) | appropriate means provisions | L590 |
| clause 26 | clause 30 | appropriate means definition | L836, L926-927, L929 |
| clause 27.1 | (not mapped) | supply as soon as reasonably practicable after acceptance | L999 |
| clause 27.3 | clause 31.3 | operable for minimum period | L838 |
| clause 27.5 | clause 31.6 | clear instructions and guidance | L930 |
| clause 29 / 29.3 | clause 33 / "33.3" | battery reliance; 36-month replacement | L861, L859, L873 |
| clause 33 / section G3 | Section H3 | requirement to monitor (annual) | L848, L874 |
| clause 35 / 35.2 | "otherwise now clause 42.2"; new clause 42 | no longer vulnerable; moving premises | L949, L956, L967 |
| clause 36 | (not mapped) | consumer's duty to inform | L969 |
| clause 38.1 / 38.2 | clause 45.1 / 45.2 | process descriptions | L993-994 |
| clauses 38.3-38.6 | clauses 45.3, 45.4, 45.6, 45.8 | customer/vulnerable/declined/means metrics | L995 |
| clause 38.7 | (not mapped by D06) | average working days / provisioning timing | L996, L1004 |
| Section F2 | Section G2 | application process section; guidance note | L783, L787, L800 |
| section G | section H | appropriate means | L655, L922 |
| Section I | section J | not withdraw service | L567 |
| Section J | section K | disclosure | L992 |
| Section L | section M; clause 52.3 | disputes | L939 |
| Attachment A | removed | application form template | L798 |

Act provisions cited: s 9A(1)(c)-(d) (L151); s 238(1) (L98, L149, L228, L675); s 238(3) (L220); s 238(3)(a) (L376); s 238(3)(b) (L677, L1078); s 238(3)(c) (L772); s 238(3)(d) (L581, L834); s 238(4)(b) (L583); s 238(4)(c) (L166, L225, L230); s 238(5) (L155, L592); s 239 (L217); s 239(5) (L126, L223). Appendix A (L1178-1257) reproduces ss 9A, 238, 239, 240, 241; s 241 ends at L1257 with paragraph (c) (end of file).

## Shared ground - D06 facts repeated, restated or stated differently elsewhere (locations only)

Other documents were searched or sampled for these points only; they are not mapped here.

**A. D06 versus D05 (final Code, platform "Doc 14")**

1. Commencement and grace period - consistent dates, different framing.
   - D06 L106 "The Code comes into effect on 1 July 2024."; L1171 "enforcement grace period of six (6) months".
   - D05 L104 "1.1 Section H comes into force on 1 August 2021; and 1.2 the rest of this Code comes into force on 1 February 2021."; D05 L110 "3. There is a grace period starting on 1 July 2024 and ending on 1 January 2025 to allow providers to come into compliance with the amendments to the Code made by the Commission 111 Contact Code (Amendment Version 2024) that came into force on 1 July 2024."; D05 L112 "4. During the grace period providers will be considered to have complied with these requirements of the Code if they complied with the Code as it was prior to the amendments."; D05 L20 "which comes into force on 1 July 2024". D05 does not print "six" months or "enforcement".
2. New clause 42 - wording differs.
   - D06 L967 quotes “If a vulnerable consumer moves premises and remains with the same provider, such provider may check the consumer’s status, and may require the vulnerable consumer (or someone on their behalf) to re-apply to demonstrate that they continue to be a vulnerable consumer if something material has changed”.
   - D05 L392 "42. If a vulnerable consumer moves premises and remains with the same provider, such provider may check the consumer’s status, and may require the vulnerable consumer (or someone on their behalf) to re-apply to demonstrate that they continue to be a vulnerable consumer." The word "material" does not occur anywhere in D05 (Grep, no matches).
3. "clause 42.2" - D06 L967 "(otherwise now clause 42.2 of the Code)"; in D05 the no-longer-vulnerable list is clause 41 with 41.1-41.3 (D05 L387-391) and clause 42 has no sub-clauses.
4. "clause 33.3" - D06 L859, L873 "(now clause 33.3 of the Code)"; D05 clause 33 prints only 33.1 and 33.2 (D05 L360-363). The 36-month test is D05 L355 "31.5 tested at least once every 36 months; and".
5. Resubmission clause number - D06 L948 "resubmitted in accordance with clause 26" (describing the Previous Code); D01 L398 "resubmitted in accordance with clause 24"; D08 L427 "resubmitted in accordance with clause 24"; D05 L391 "resubmitted in accordance with clause 28".
6. New clause 10 - D06 L716 “For the purposes of clause 9, the information must be provided to consumers so that a customer is not able to purchase a residential landline service or switch between residential landline services or technologies without being aware of such information”; D05 L239 "10. For the purposes of clause 9, the information must be provided so that a customer is not able to purchase a residential landline service or switch between residential landline services or technologies without being made aware of such information."
7. Clause 9.4.2 - identical: D06 L715 and D05 L238 "the customer switches to a different residential landline service or technology with the same provider that may not work in a power failure".
8. Clause 9.3 - identical first sentence: D06 L755; D05 L233 "9.3 provided to all customers of a residential landline service at least once every 12 months."
9. qualified third party - D06 L663 "or a person contracted to be available and is capable to contact 111 emergency services 24/7"; D05 L189 "or a person, contracted to be available and capable of contacting 111 emergency services 24/7, such as via qualified retirement village staff and relevant medical alarm call centres".
10. managed medical or safety alarm - D06 L651 (one sentence); D05 L162-166 "(a) provides a consumer with the ability to contact a 24/7 monitored contracted service, and (b) meets the requirements in section H of the Code". D05 clause 25.4 (L330) "the consumer has a managed medical or safety alarm".
11. Clause 25 chapeau - D06 L631 "if the consumer already has a device or technology which meets the requirements under the Code" = D05 L328 (which adds ", for example:"). Previous Code cl 21 had three limbs (D06 L608); D05 cl 25 has four (25.1-25.4, L330).
12. '111 emergency service' - D06 L647; D05 L119 "111 emergency service includes the ambulance service, police service and fire and emergency service, contacted directly by a consumer or via a qualified third party".
13. provider - D06 L529 (decision) and glossary L47; D05 L189 "provider means a supplier of a residential landline service to a consumer and excludes suppliers of health care services".
14. residential landline service - D06 L411-417; D05 L191-200 "means a retail landline service provided to a consumer at a premises, and excludes: (a) mobile services; (b) naked broadband services; (c) applications that provide voice services over broadband services (such as Skype); (d) business landline services; and (e) copper landline services."
15. business landline services - D06 L187 (Draft Amended Code wording, no "as amended from time to time"); D05 L125-137 adds "as amended from time to time" after Companies Act 1993 and Partnership Law Act 2019.
16. copper landline service - D06 L254 = D05 L148 (same wording).
17. premises - D06 L415 "(used or intended for residence, as opposed to occupation)"; D05 L179-184 "(a) is used or intended for residence by any person; and (b) is receiving a residential landline service".
18. minimum period - D06 L840, L1135 "a continuous eight-hour period"; D05 L168 "minimum period means a continuous eight-hour period". D05 L358 (clause 32): "whether a means can be operated at a premises for the minimum period must be assessed as if the means is used and maintained as instructed by the provider" (bears on the TCF proposal at D06 L1144).
19. More than one vulnerable consumer - D06 L557 "appropriate for the needs of each vulnerable consumer at that premises"; D05 L380 "38. ... appropriate for the needs of all vulnerable consumers at that premises."
20. Deemed appropriate / withdrawn - D06 L916; D05 L373 (clause 35) and L376 (clause 36) "A provider can consider an application to be ‘withdrawn’ if the vulnerable consumer (or someone on their behalf) rejects an appropriate means supplied by such provider which complied with the requirements set out in section H."
21. Disclosure items - D06 L995 maps to 45.3, 45.4, 45.6, 45.8; D05 L405-411: 45.3 total vulnerable consumers; 45.4 customers; 45.5 applications accepted; 45.6 declined; 45.7 ‘withdrawn’; 45.8 means supplied by type; 45.9 provisioning timing "with brief reasons for any provisioning that took longer than 10 working days". D06 L1021 final wording "with a brief reason".
22. Records - D06 L918, L1037; D05 L419-420 (46.3 accepted; 46.5 ‘withdrawn’).
23. Annual monitoring - D06 L874; D05 L383 "39. A provider must, at least once a year, contact each customer that is a vulnerable consumer".
24. Section J quote - D06 L567 = D05 L398 (clause 44), verbatim.
25. Clause 52.3 - D06 L939; D05 L450 adds "(in accordance with clause 30)".
26. Ten working days - D06 L999 "within working 10 days"; D05 L314 "22. Within ten working days of receiving a complete consumer’s application".
27. Disclosure deadline - D06 L983; D05 L402 "45. No later than 30 November of each disclosure year"; D05 L154 defines disclosure year "a period of 12 months beginning on 1 July in any year and ending on 30 June in the following year" (not defined in D06).
28. ISBNs - D06 L3 own ISBN 978-1-991287-45-8 is listed in D05 L55; D05's ISBN 978-1-991287-44-1 (D05 L4) is D06 L24.

**B. D06 versus D01 (draft decisions paper, platform "Doc 2")**

1. Submission counts - D06 L169 "18 submissions from 17 different parties"; D01 L112 "6. We received 18 submissions from 17 different parties: Spark, One NZ, 2degrees, NZ Police, Fire and Emergency, Anonymous, Business Technology Group, Sky, MyRepublic, Mercury, Whaikaha, Grey Power, Disabled Persons Assembly (DPA), Consumer NZ, New Zealand Telecommunications Forum (TCF), Wireless Internet Service Providers Association of New Zealand (WISPANZ) and Tech Users Association of New Zealand (TUANZ)."; D01 L73 "the 18 submissions we received". Same 17 names, different order.
2. Number of summarised amendments - D01's summary table has IDs 1-7 (D01 L214-236: business landline services; code-related information; application form; replacement, Clause 29.3; when a means is appropriate, Clauses 6.6 & 31; moving premises, Clause 37; disclosure of time, Clause 40.7). D06 Table 1 has IDs 1-11 (L255-349).
3. Replacement of means - D01 L368-369 "69.1 remove the requirement in clause 29.3 of the current Code to replace means at least once every 36 months; and" / "69.2 instead require providers to replace the appropriate means when the device no longer meets the minimum requirements under the Code."; D06 L845-846 restates this as the draft; D06 L869 final "test the appropriate means at least once every 36 months".
4. Provisioning-time disclosure - D01 L460 "91. Our draft decision is to amend clause 38.7 of the Code to:"; D01 L466 "with brief reasons for any provisioning that took longer than 10 working days"; D01 table L234 "Clause 40.7"; D06 L1006 restates the draft "with a reason"; D06 L1021 final "with a brief reason".
5. Ten-working-day citation - D06 fn 122 (L1011) cites draft "para 85" for both clause 27.1 and clause 18; in D01 clause 27.1 is para 85 (L446) and clause 18 / "within 10 working days of providers receiving a complete application" is para 86 (L448).
6. Text option - D06 L1155 "In paragraph 187 of the Draft Decision and Reasons paper"; D01 para 187 begins L878 and the quoted sentence is split across L880 "We note that the text option for" and L888 "contacting 111 is currently limited to people that are deaf, hearing or speech impaired."
7. Scenarios A-C - D06 L459-463; D01 L475-478 (paras 93.1-93.3), D01 L480 "94. It is the Commission’s preliminary view that the party who holds the direct billing relationship with the consumer is subject to the Code". Matches fn 36 "paras 92-95".
8. Medical alarms - D06 L603-605; D01 L547 (para 103), L551 (para 104), L565 (para 105).
9. Template - D06 fn 92 para 61; D01 L333 "61. Providers remain able to use the template".
10. Minimum period - D06 fn 134 "paras 155-162"; D01 L755-782 (uses both "continuous eight-hour period" and "continuous 8-hour minimum period").
11. Compliance review start - D06 L161 "On 30 November 2022 we commenced an evaluation of compliance with the Previous Code."; D01 L160 "On 30 November 20229 we commenced an industry-wide review of compliance with the Code."; D01 L835 "Following annual disclosures being provided to the Commission by 30 November 2022 we conducted an industry-wide review of compliance with the Code." (= D06 L1089).
12. Review start - D06 L162; D01 L162 "22. On 18 May 2023 we commenced a review of the Code with our Request for Views paper as the Code had been in force for two years, and both feedback we received during our compliance work and our own observations, specifically for the 2022 disclosure year".
13. In-force dates - D06 L142; D01 L140 "The Code came into force on 1 February 2021, and section G came into effect on 1 August 2021.7".
14. Business landline reasoning - D06 L364-368; D01 L249 (para 45), L251 (para 46), L263 (para 47), L266 (para 48).
15. Present in D01, absent from D06: D01 L874 "186. Fire and Emergency also submitted that around 85% of emergency calls are made by mobile phones." (D06 has no percentage); D01 L885 cites "FENZ ... (21 June 2023)" (D06 gives no date for Fire and Emergency's submission).
16. Copper connection figures (51,000 / 159,000, D06 L438) - no match for "51,000", "159,000", "voice-only" or "copper connections" in any other text/D*.txt.

**C. D06 versus other documents**

1. Commencement proposal - D08 L37 (Draft Amended Code text) "5. This Amended Code comes into force on a date that is 3 months following the publication of the Amended Code."; D04 L92 (Bupa) "The current proposal provides that the amendments will come into force 3 months following publication. We submit that the Commission would need to allow at least a 6 month transition period"; D06 L12 (published 26 June 2024), L1171 (in force 1 July 2024, six-month grace period), fn 137 L1175 cites Bupa page 5.
2. Submission dates as printed on the submissions versus as cited in D06:
   - TCF RfV submission: D13 L7 "16 June 2023"; D06 L610, L790, L887 "(19 June 2023)".
   - Age Concern draft-round submission: D03 L4 "29/02/2024"; D06 (e.g. L400) "(1 March 2024)".
   - Ryman: D10 L5 "February 29, 2024"; D06 L488 "(29 February 2024)" - same.
   - Bupa: D04 L93 "1 March 2024"; D06 L486 "(1 March 2024)" - same.
   - One NZ: D09 L4 "16 June 2023"; Spark: D12 L6 "16 June 2023"; Spark feedback: D11 L6 "30 November 2022" - same as D06.
   - DPA: D07 L4 prints "June 2023" (no day on that line); D06 L705 "(16 June 2023)".
   - WISPANZ (D14) and TCF draft-round (D08): no submission date found in the lines sampled (D14 L1-8; D08 L1-20 show the Draft Amended Code's own date "18 December 2023").
3. Request for Views timetable - D02 L133 "Submissions received 16 June 2023"; D02 L139 "Cross-Submissions received September"; D06 mentions no cross-submissions.
4. Two years in force - D06 L162; D02 L64 "9. As the Code has now been in force for two years"; D02 L62 "came into effect on 1 February 2021. Providers had until 1 August 2021".
5. D06 cross-refs into D02 - fn 8 "paras 13 to 15" = D02 L76-79; fn 103 "para 41" = D02 L176 "41. Question 2: Do you believe that the solutions that have been provided to vulnerable consumers have been effective".
6. TCF phrases quoted by D06 and found in D08: “when used as recommended” (D06 L1144; D08 L154, L173, L389); “operational simplicity” (D06 L752; D08 L246); “an overly specific additional requirement in the Code” (D06 L711; D08 L247); “on the customer’s website” (D06 L906; D08 L220, straight apostrophe). TCF's tracked clause 29.3: D08 L382 "If the device performance is unknown it should be replaced at least once every 36 months from the date the last means was installed." (D06 L853, L873).
7. Bupa's "four levels" - D06 L479; D04 L45, L50.
8. ARRC Agreement - D06 L502 attributes the point to the RVA (fn 50); the term "ARRC" also occurs in D10 (Ryman) L20-22.
9. Commission membership - D06 L8-11 (26 June 2024): Tristan Gilbertson, Pierre van Heerden, Nathan Strong, Loretta Lovell; D08 L7-8 (Draft Amended Code, 18 December 2023): "Tristan Gilbertson" / "Dr John Small Nathan Strong Loretta Lovell".
10. Associated-document ISBNs in D06 L17-25 recur in D01 L13-16, D05 L35-57 and D08 L13-60; project number PRJ0046469 in D01 L4, D02 L5, D05 L5, D08 L5.
11. 36-month rule - D03 L43 (Age Concern restating draft item 4) "Removing the requirement to replace appropriate means every 36 months and substituting it with the requirement to replace appropriate means when they no longer meet the minimum requirements."; D06 L850 "167. Age Concern supported the proposed amendment."

## Gaps

- Figure 1 content (L160): missing from the text capture; unresolved.
- No unread ranges in D06.
- Not verified here (outside this map's scope): page/paragraph numbers that D06's footnotes cite inside D03, D04, D07-D14; the Previous Code's own clause text (only as quoted in D06, D01 and D08).
