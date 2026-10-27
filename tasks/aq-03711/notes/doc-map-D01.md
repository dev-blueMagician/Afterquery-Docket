# aq-03711 - D01 document map (single document, full sequential read)

Navigation only. Line numbers (L...) are `Read` line numbers in `tasks/aq-03711/text/D01.txt`.
Quotes are verbatim (curly apostrophes/quotes and en dashes as in the text) so they can be grepped.
Questions quote the document, never this map. No questions, answers, traps or ratings here.

## 0. Binding and coverage ledger

- Source: `docs/nzcc_contact_code_111_111_contact_code_review_draft_decisions_and_reas.txt`
- Extraction: `text/D01.txt`, method `text`, pages `null`, 143,732 chars (manifest.json).
- sha256 (manifest.json and intake.json agree): `032d28fe3630d2775c79ec25f45bcb20decd130cb46230f028368f675d36dee6`
- Platform number: "Doc 2" (intake.json number 2). intake: incomplete false, gap_characters 0.
- Printed pages: running header "111 Contact Code Review – Draft Decisions and Reasons N" occurs 72 times, N = 2 ... 73 (last at L1430); cover = page 1. So 73 printed pages.
- The text is a flattened PDF text layer: tables run inline, footnote numbers often sit alone on a line, footnote text is interleaved at page bottoms.

| Lines read | Content (printed pages) | Status |
| --- | --- | --- |
| 1-150 | cover, associated documents, glossary, contents, executive summary, ch 1, ch 2 start (pp 1-10) | read |
| 150-299 | ch 2 rest, ch 3, ch 4 summary table, Section B, Section E (pp 10-17) | read |
| 299-449 | Sections F, G, H, J, paras 54-86 (pp 17-23) | read |
| 449-589 | paras 87-108, ch 5, ch 6 start (pp 23-29) | read |
| 589-729 | paras 109-148 (pp 30-35) | read |
| 729-869 | paras 148.3-183 (pp 35-41) | read |
| 869-999 | paras 184-213 (pp 41-45) | read |
| 999-1118 | fn 110-111, Appendix A statute, Appendix B start (pp 45-51) | read |
| 1118-1247 | Appendix B (pp 51-60) | read |
| 1247-1376 | Appendix B (pp 60-69) | read |
| 1376-1436 | Appendix B end (pp 69-73); L1435 "-----" is the last line | read |

Coverage: FULL - all 1,436 lines read sequentially. Nothing unread. One visual gap (Figure 1, section 12).

Extraction spot-checks against the original `docs/` file (the original is itself a .txt; identical text with a constant +2 line offset from the two header lines added in `text/`):
- Page count: last page marker "Draft Decisions and Reasons 73" at docs L1428 = text L1430. Match.
- Table: summary-table row 7 "15 7 Disclosure of time taken to provide appropriate means to consumers Clause 40.7" at docs L232 = text L234. Match.
- Footnote: fn 77 "77 76% of vulnerable consumers were provided with a mobile in 2021, and 79% in 2022." at docs L765 = text L767. Match.
- Figure: caption at docs L855 = text L857; no diagram content in either (the original PDF cannot be inspected - unresolved).

## 1. Identity, dates, deadlines

- Title: L6-7 "Commission 111 Contact Code Review" / "Draft Decisions and Reasons". Running header "111 Contact Code Review – Draft Decisions and Reasons".
- Issuer/author: Commerce Commission (NZ). L67 "The Commerce Commission (the Commission) has reviewed the Commission 111 Contact Code (the Code)".
- Identifiers: L3 "ISBN 978-1-991085-63-4"; L4 "Project no. PRJ0046469"; L5 "Public Version".
- Publication date: L8 "Date of publication: 18 December 2023".
- Edition/series position: the DRAFT decisions paper of the Code review (after the May 2023 Request for Views, before the final paper). L132 "After considering the submissions received, we will publish the amended Code and final Decisions and Reasons paper." (intention).
- Calendar/fiscal convention: calendar dates; "disclosure year" is a Code term (deadline 30 November); D01 uses both "2021/22 Code disclosure year" (L179, L846) and "2022 disclosure year" (L162), and plain "2021" / "2022" for the percentages (L750, L767). D01 does not define the start/end of a disclosure year.
- Submission deadline on this draft: L116 "Submissions are due by 5pm on 1 March 2024."
- Cross-submission date: NOT STATED. The string "cross" + "submission" does not occur anywhere in D01 (Grep, whole file). (D02 L139 has an indicative "Cross-Submissions received September" row - see section 11.)
- Statutory window: L191 "within 30 working days after the date on which public notice of the draft amended Code is given" (fn 10 L199 "Section 239(3)"); statute text L1057 "not later than 30 working days after the date on which public notice of the draft code is given". D01 does not state the date public notice was given.
- Submission address/subject: L118 "telecommunications@comcom.govt.nz with the subject line “Submission: 111 Contact Code Review”".

### Associated documents table (L11-16; printed page 2)

Columns: Publication date | Reference | Title. Four rows, no units.

| Publication date | Reference | Title |
| --- | --- | --- |
| 17 November 2020 | ISBN 978-1-869458-52-2 | Commission 111 Contact Code |
| 17 November 2020 | ISBN 978-1-869458-53-9 | Final Decisions and Reasons paper |
| 18 May 2023 | ISBN 978-1-991085-00-9 | Request for Views paper |
| 18 December 2023 | ISBN 978-1-991085-62-7 | Draft Commission 111 Contact Amended Code 2023 |

This paper's own ISBN ends -63-4 (L3); the draft amended Code published alongside ends -62-7 (L16).

### Glossary (L19-27; printed page 3)

- L20 "Act Telecommunications Act 2001"
- L21 "Commission Commerce Commission"
- L22 "Provider A provider of a retail landline service"
- L23 "DPA Disabled Persons Assembly"
- L24 "LFC Local Fibre Company"
- L25 "RSP A provider of retail telecommunications services TCF Telecommunications Forum" (two glossary rows on one line)
- L26 "TUANZ Tech Users Association of New Zealand"
- L27 "WISPANZ Wireless Internet Service Providers Association of NZ"

### Every date and what it marks

| Date | What it marks | Line | Quote |
| --- | --- | --- | --- |
| November 2018 | Act amended by the Telecommunications (New Regulatory Framework) Amendment Act 2018 | L136 | "In November 2018, the Act was amended by the Telecommunications (New Regulatory Framework) Amendment Act 2018." |
| 17 November 2020 | Code and the 2020 Decisions and Reasons paper published | L139, L13-14 | "We published the Code and our Decisions and Reasons paper on 17 November 2020." |
| 1 February 2021 | Code came into force | L140 | "The Code came into force on 1 February 2021, and section G came into effect on 1 August 2021.7" |
| 1 August 2021 | Section G (appropriate means) came into effect | L140; fn 7 L154 | "Section G: Requirement on providers to provide vulnerable consumers with an appropriate means for contacting 111." |
| June 2021 | Date inside the factsheet URL (fn 93) | L850 | "Telecommunications-Forum-TCF-Homephone-technology-and-calling-111-Code-factsheet-June-2021.pdf" |
| "Throughout 2022" | Compliance engagement work | L160 | "Throughout 2022 we undertook compliance engagement work to promote compliance with the Code." |
| 30 November 2022 | (a) industry-wide compliance review commenced; (b) annual disclosures provided by; (c) date of Spark's "Feedback on 111 Contact Code" letter | L160; L835; fn 27 L341 | L160 "On 30 November 20229 we commenced an industry-wide review of compliance with the Code." ; L835 "Following annual disclosures being provided to the Commission by 30 November 2022 we conducted an industry-wide review of compliance with the Code." |
| 2021/22 Code disclosure year | Period whose conclusion preceded the compliance review (fn 9 and fn 91, identical wording) | L179, L846 | "Following the conclusion of the 2021/22 Code disclosure year." |
| "2022 disclosure year" | Year whose observations showed scope for improvement | L162 | "specifically for the 2022 disclosure year, showed that there was scope for improvement" |
| May 2023 / 18 May 2023 | Request for Views paper published; review of the Code commenced | L69, L110, L162, L15 | L110 "We published a Request for Views paper on 18 May 2023" ; L162 "On 18 May 2023 we commenced a review of the Code with our Request for Views paper as the Code had been in force for two years" |
| 19 May 2023 | Anonymous submission (fn 62, 64, 88) | L666, L694, L823 | "Anonymous “Submission on 111 Contact Code Review Request for Views” (19 May 2023)" |
| 5 June 2023 | BTG submission (fn 61, 63, 66) | L665, L693, L696 | "BTG “Submission on 111 Contact Code Review Request for Views” (5 June 2023) page 1." |
| 15 June 2023 | Consumer NZ submission as dated in fn 23 and fn 34 | L316, L409 | "Consumer NZ “Submission on 111 Contact Code Review Request for Views” (15 June 2023) pages 1 & 2." |
| 16 June 2023 | 2degrees, WISPANZ, NZ Police, Whaikaha, DPA, Grey Power, Spark (RfV submission), One NZ; AND Consumer NZ as dated in fn 88, 101, 104 | L258, L284-285, L314-315, L340, L365, L558, L824, L918, L951 | L824 "Consumer NZ “Submission on 111 Contact Code Review Request for Views” (16 June 2023) page 1 & 2." |
| 19 June 2023 | TCF submission (fn 29, 33, 44, 60, 73, 81, 86, 111) | L343, L387, L557, L664, L743, L771, L799, L1002 | "TCF “Submission on 111 Contact Code Review Request for Views” (19 June 2023) para 21-22." |
| 21 June 2023 | FENZ submission (fn 97) | L885 | "FENZ “Submission on 111 Contact Code Review Request for Views” (21 June 2023) page 2." |
| 18 December 2023 | This paper and the draft amended Code published | L8, L16 | "Date of publication: 18 December 2023" |
| 1 March 2024, 5pm | Submissions on the draft amended Code and this paper due | L116 | "Submissions are due by 5pm on 1 March 2024." |
| 30 November each (disclosure) year | Provider disclosure deadline under the current Code | L416, L991 | L416 "no later than 30 November of each disclosure year" ; L991 "no later than 30 November of each year" |
| "this year or next year" / "this decade" | BTG's (quoted) expectation for satellite txt/calling | L1269 | "comes into reality this year or next year" ; "very likely to be a reality this decade" |
| "in the next 10 years" | One NZ's (quoted) report of Chorus's copper retirement plan | L1306 | "Chorus has recently announced that they plan to retire their entire copper network in the next 10 years" |
| "Some years ago" / "Recently" | NZ Police (quoted): 111 SMS text service set up; Apple SOS satellite launch | L1395, L1397 | "Some years ago, NZ Police set up and currently operate a limited" ; "Recently Apple launched their SOS satellite emergency service" |

## 2. Submitters named (all on the Request for Views consultation)

D01 pre-dates the submissions on the draft amended Code; every submission it cites or quotes is a response to the Request for Views, plus Spark's earlier 30 November 2022 letter.

- Count: L73 "After assessing the 18 submissions we received" ; L112 "We received 18 submissions from 17 different parties:".
- The 17 names at L112, in printed order: Spark; One NZ; 2degrees; NZ Police; Fire and Emergency; Anonymous; Business Technology Group; Sky; MyRepublic; Mercury; Whaikaha; Grey Power; Disabled Persons Assembly (DPA); Consumer NZ; New Zealand Telecommunications Forum (TCF); Wireless Internet Service Providers Association of New Zealand (WISPANZ); Tech Users Association of New Zealand (TUANZ).
- D01 does not say which party accounts for the 18th submission. Spark is the only party cited under two different document titles: "Feedback on 111 Contact Code" (30 November 2022) and "Submission on 111 Contact Code Review Request for Views" (16 June 2023) (e.g. L341, L365). That is an observation about the citations, not a statement in D01; the 30 November 2022 letter pre-dates the 18 May 2023 Request for Views.
- Where each of the 17 appears after L112:
  - Cited in footnotes AND quoted in Appendix B: Spark, One NZ, 2degrees, NZ Police, Fire and Emergency (FENZ), Anonymous, Business Technology Group (BTG), Whaikaha, Grey Power, DPA, Consumer NZ, TCF, WISPANZ (13).
  - Quoted in Appendix B only (no footnote cite, not named in chapters 4-6): Mercury (L1093).
  - Never cited, quoted or named again: Sky, MyRepublic, TUANZ (TUANZ otherwise only in the glossary L26). (Grep of the whole file: Sky/MyRepublic only at L112.)
  - 13 + 1 + 3 = 17.
- Aliases: "Business Technology Group" (L112, L654, L678, L691, L1267-1268) = "BTG" (fn 61, 63, 66). "Fire and Emergency" (L112, L874) = "FENZ" (fn 97 L885; L1395) = "Fire and Emergency New Zealand" (L859, L1052) = "Fire & Emergency" (L1404). "NZ Police" = "the New Zealand Police" (L859, L1050) = "Police" (L1135, L1386). "WISPANZ" = "Wireless Internet Service Providers Association" (L260) = "WISPA" (L1316). "TCF" = "Telecommunications Forum" (L25) = "New Zealand Telecommunications Forum" (L112). "TDRS" = "Telecommunication Disputes Resolution Scheme" (L599). "MSD" = "Ministry of Social Development" (L1334 "Ministry of Social Development (MSD)"; L734). Variant spellings inside quotations, not equated by D01 itself: "ONE and 2degrees" (L1275, Anonymous quote); "One NZ and 2 Degrees" (L1397, NZ Police quote); "ST Johns" (L1395, NZ Police quote) beside "Hato Hone St John" (L863, L1386).
- Organisations MENTIONED but not submitters: Chorus (L1301, L1306, L1336 - in Spark and One NZ quotes); Ministry of Social Development / MSD; Hato Hone St John; Wellington Free Ambulance; Apple (L1397); JustAnswer (L1409); Director of Civil Defence Emergency Management (L859, L1054); Minister Fa’afoi (fn 76 L765); TDRS.
- Footnote index by submitter (date as cited; pinpoint):
  - 2degrees (16 June 2023): fn 16 page 1 (L258); fn 44 page 1 (L555); fn 79 page 2 (L769); fn 85 page 1 (L798).
  - WISPANZ (16 June 2023): fn 17 page 5 (L284); fn 65 page 5 (L695); fn 74 page 5 (L744); fn 80 page 5 (L770).
  - NZ Police (16 June 2023): fn 18 page 2 (L285); fn 94 page 1 (L881); fn 96 page 1 & 2 (L884).
  - Whaikaha (16 June 2023): fn 21 pages 1 & 2 (L314); fn 28 page 1 (L342); fn 102 page 1 (L948); fn 107 page 1 & 2 (L981).
  - DPA (16 June 2023): fn 22 page 5 (L315); fn 24 page 5 (L317); fn 53 page 7 (L609); fn 54 page 5 & 6 (L610); fn 88 page 4 & 5 (L822); fn 102 page 4 (L947); fn 107 page 5 (L980).
  - Consumer NZ: fn 23 (15 June 2023) pages 1 & 2 (L316); fn 34 (15 June 2023) page 3 (L409); fn 88 (16 June 2023) page 1 & 2 (L824); fn 101 (16 June 2023) page 2 (L918); fn 104 (16 June 2023) page 2 & 3 (L951).
  - Grey Power (16 June 2023): fn 26 page 3 (L340); fn 52 page 3 (L608); fn 89 page 2 (L843).
  - Spark "Feedback on 111 Contact Code" (30 November 2022): fn 27 para 41-45 (L341); fn 32 para 12 (L386); fn 40 para 35 (L443); fn 44 para 13-21 (L556); fn 69 para 33 (L719); fn 72 para 24, 30 (L742); fn 78 para 34 (L768).
  - Spark "Submission on 111 Contact Code Review Request for Views" (16 June 2023): fn 31 para 26 (L365); fn 51 para 30-32 (L607); fn 67 para 27-29 (L717); fn 87 para 32 (L821).
  - TCF (19 June 2023): fn 29 para 21-22 (L343); fn 33 para 7 (L387); fn 44 para 11-14 (L557); fn 60 para 22 (L664); fn 73 para 16-17 (L743); fn 81 para 8-10 (L771); fn 86 para 5 (L799); fn 111 para 20 (L1002).
  - One NZ (16 June 2023): fn 44 para 7-10 (L558); fn 59 para 16 (L663); fn 68 para 14 (L718); fn 75 para 14-15 (L745); fn 82 para 13 (L772).
  - BTG (5 June 2023): fn 61 page 1 (L665); fn 63 page 1 (L693); fn 66 page 1 & 2 (L696).
  - Anonymous (19 May 2023): fn 62 page 1 & 2 (L666); fn 64 page 1 (L694); fn 88 page 1 (L823).
  - FENZ (21 June 2023): fn 97 page 2 (L885).

## 3. Chapter 4 summary table of proposed amendments (L214-237; printed pages 14-15)

Intro: L212 "Below we provide a summary table of the proposed amendments."
Columns (L214): "ID | Subject of change | Reference in Draft amended Code | Draft decision | Reference in this paper". Seven rows, IDs 1-7. No numeric units, no totals, no table footnotes.
Extraction layout: cells run inline; row 2's subject is split over L216/L218 ("providers’" / "websites"); row 7's ID follows the page-15 header at L233-234 ("15 7 Disclosure of time taken ...").

| ID | Subject of change | Reference in Draft amended Code | Draft decision (verbatim) | Reference in this paper |
| --- | --- | --- | --- | --- |
| 1 | Application of the Code to business landline services | Sections B, D | "Clarifying that the Code applies to residential landline services and not business landline services." | Page 15-16 Para 44-48 |
| 2 | Code-related information on providers’ websites | Clause 7.4 | "Adding a requirement that Code information must be displayed on the website in such a manner that a consumer cannot purchase a retail landline service without seeing information about the Code." | Page 17 Para 51-55 |
| 3 | Application form template and requirements | Section F2 | "Clarifying that the application form template is provided for guidance purposes and that providers can modify it, provided it otherwise meets Code requirements. The template will be removed from the Code and made available on the Commission’s website to avoid the inference it is compulsory." | Page 18-19 Para 58-63 |
| 4 | Replacement of appropriate means supplied to vulnerable consumers | Clause 29.3 | "Removing the requirement to replace appropriate means every 36 months and substituting it with the requirement to replace appropriate means when they no longer meet the minimum requirements." | Page 19-20 Para 67-69 |
| 5 | When a means can be considered appropriate | Clauses 6.6 & 31 | "Clarifying that if the Code’s requirements are met, the appropriate means supplied by the provider to the vulnerable consumer will be deemed to be appropriate, whether the vulnerable consumer accepts it or not." | Page 20 Para 70-75 |
| 6 | Vulnerable status when moving premises | Clause 37 | "Clarifying that if a consumer moves premises, but remains with their provider, the provider may check the consumer’s status and potentially require them to re-apply if something material has changed." | Page 21-22 Para 78-81 |
| 7 | Disclosure of time taken to provide appropriate means to consumers | Clause 40.7 | "Replacing the requirement to disclose an overall average provisioning time with a requirement to report on how long each individual install took, for each vulnerable consumer (from the date each application was accepted). If the installs took longer than 10 working days, providers must briefly describe why." | Page 22-24 Para 84-91 |

Two clause-numbering schemes sit side by side in D01 (table column = "Reference in Draft amended Code"; body = "the current Code"):
- Row 7 "Clause 40.7" (L234) vs body L460 "amend clause 38.7 of the Code" and fn 39 L441 "Clauses 38.7 of the current Code".
- Row 6 "Clause 37" (L228) vs body L412 "remove clause 35.2 of the current Code". Separately fn 55 L611 cites "Clause 37 of the current Code" for a different point (L603 "applies to any consumer who is, or who may become, vulnerable").
- Row 4 "Clause 29.3" (L224) and body L368 "clause 29.3 of the current Code" - same number in both.
- Row 5 "Clauses 6.6 & 31" (L226); the body cites "clause 26 of the current Code" (L384).
- Row 2 "Clause 7.4" (L219); the body cites "clause 6", "clauses 7.1 and 7.2 of the current Code" (L302-304).
- Row 1 "Sections B, D" (L214); body heading "Proposed amendments to Application: Section B of the Code" (L238).
- Row 3 "Section F2" (L222); body L339 "Attachment A of the Code", L346 "the guidance note in Section F2".
Table wording vs body wording: row 4 says "every 36 months"; body says "at least once every 36 months" (L356, L368) / "at least every 36 months" (L353).

## 4. Draft decisions 1-7 in detail (PROPOSALS: "Our draft decision is ...", "we propose")

### DD1 - Application of the Code to business landline services (Section B; paras 42-48; L238-272)
- Current Code: L242 "the current Code applies to all retail landline services, irrespective of whether they are provided to residential or business consumers." (2020 paper para 93, fn 14 L254).
- 2020 reasoning recalled, L247-248: "there were likely to be some small business consumers (e.g., farms, dairies) which have vulnerable consumers residing on the premises" ; "the impact of including business consumers was unlikely to be significant, as most business consumers would have the means to contact 111 in a power failure (e.g., through an employee who has a mobile phone)."
- Submitters: 2degrees - L249 "2degrees suggested that we should provide clarification that the Code applies to residential services only". WISPANZ - L251/L260 "we now agree" ... "with Wireless Internet Service Providers Association (WISPANZ) that business landline services should be excluded." NZ Police (contrary view) - L263 "While we agree with NZ Police18 that protection and resiliency is important in all areas, the Code is intended to provide resiliency in the home, where consumers may not have other protections available."
- Appendix B quotes: 2degrees L1125-1127 "We would support clarification on this point, which may include clarification that the Code should apply to consumers of residential services." ; WISPANZ L1128 "It is very clear to us that business customers should be exempt from the code" ; NZ Police L1135 "Police support the need for RSPs who provide services to business customers only to be subject to the Code and required to comply with the Code".
- Draft decision L266-270: "48.1 business landline services are defined in the Code;" ; "48.2 the definitions of retail landline services (from retail landline services to residential landline services) and premises are amended; and 48.3 Code requirements apply to only residential landline services, and the Code does not apply to business landline services."
- fn 19 L286: "While we are proposing that the Code applies to residential landline services rather than retail landline services, we have used “retail landline services” throughout this paper to avoid confusion, as this is the wording in the current Code."
- Hedges: L249 "in most cases employers will not have people residing at their premises" ; L251 "more significant on the providers of these services than we had anticipated" (no figure).

### DD2 - Code-related information on providers' websites (Section E; paras 49-55; L273-304)
- Current Code L278-282: clauses 6 and 7; L280 "at the point of sale in a manner that is consistent with the NZ Government Web Standards" ; L282 "All customers of a retail landline service must be directly provided with the information at least every 12 months and when a customer first makes contact with a provider or switches services."
- Submitters L293: "Submissions from Whaikaha21 and DPA22 mentioned the need for information to be made more accessible, and Consumer NZ23 and DPA24 raised concern that consumers are not adequately informed about the Code."
- Commission finding L295: "some providers do not present information listed in clause 6 in a clear and accessible way" (no count).
- Draft decision L302: "54.1 Explicitly require the information set out in clause 6 of the current Code to be provided in an easily discernible manner to all consumers such that these consumers are not able to purchase a retail landline service from the provider without seeing that information." ; L304 (para 55) "must be easily and clearly visible to all consumers on the relevant page of the provider’s website in a manner that is prominent and consistent with the NZ Government Web Standards, in accordance with clauses 7.1 and 7.2 of the current Code."

### DD3 - Application form template and requirements (Section F / F2; paras 56-63; L306-346)
- Current Code: L320 "This process must comply with clauses 13-24 of the current Code." ; L322 "supplies a template written application form" ... "for the purpose of clause 13.3 of the current Code."
- Submitters L326: "Grey Power26, Spark27, Whaikaha28 and TCF29 submitted that the template application form is not accessible for many consumers, and is too long and difficult to work with." (the Spark cite, fn 27, is the 30 November 2022 Feedback letter para 41-45).
- Commission L328: "It has never been our intention to require providers to use the template."
- Draft decision L339: "63.1 no longer provide the template written application form as Attachment A of the Code. A template will instead be uploaded on the Commission’s website for optional use by providers; and" ; L346 "63.2 amend the guidance note in Section F2 to state that a template can be found on our website."
- Related intention outside the Code, L987: "We also plan to publish an editable version of the application form template so this can be modified as needed, including to be made more accessible."

### DD4 - Replacement of appropriate means (Section G; paras 64-69; L348-369)
- Current Code L353: "The minimum operating period is currently a continuous 8- hour period." (sic, space after hyphen) ; "be replaced at least every 36 months from the date the last means was installed."
- Submitter: Spark, agreed with - L356 "We agree with Spark31 that the requirement to replace appropriate means at least once every 36 months is in some cases too often" (fn 31 = Spark 16 June 2023 submission para 26). Appendix B quote L1187-1189: "We suggest the requirement to replace a device every 3 years is unnecessary in many cases, as the devices we deploy are expected to last longer than 3 years." ; "Providers should have discretion on whether to replace a" ... "device after 3 years if it is still functioning and is reasonably expected to continue to function as required for another 12 months."
- Caveat L358: "The intention of this proposed amendment is not to suggest that appropriate means should be replaced less often." ; "clause 33 of the current Code requires providers to monitor whether a means remains appropriate on at least an annual basis".
- Draft decision L368-369: "69.1 remove the requirement in clause 29.3 of the current Code to replace means at least once every 36 months; and" ; "69.2 instead require providers to replace the appropriate means when the device no longer meets the minimum requirements under the Code."

### DD5 - When a means can be considered appropriate (Section G; paras 70-75; L370-384)
- Submitters: L372 "We agree with Spark32 and TCF33 that the current requirements introduce unnecessary compliance uncertainty for providers where a solution is compliant with the Code but is still rejected by the vulnerable consumer." (Spark cite = 30 November 2022 Feedback para 12; TCF para 7). L374 "WISPANZ gave battery back-up devices as an example of a solution that some vulnerable consumers dislike because of their size or LED displays, even though they meet the requirements of the Code and are the only option outside mobile coverage areas." (no footnote on this sentence; Appendix B quote L1198, ref 71).
- Draft decision L382: "74.1 clarify in the Code that if its requirements are met, the appropriate means supplied by the provider to the vulnerable consumer is deemed appropriate, whether the vulnerable consumer accepts it or not; and 74.2 amend the Code to require providers to make vulnerable consumers aware of the implications of rejecting the appropriate means."
- Qualification L384: "providers must comply with clause 26 of the current Code in discharging their obligations."
- The summary-table row 5 (L226) carries only the 74.1 limb; 74.2 is in the body only.

### DD6 - Vulnerable status when moving premises (Section H; paras 76-81; L390-412)
- Current Code - four circumstances (L391-398): 76.1 the consumer requests; 76.2 "where the consumer no longer resides at the premises where the retail landline service was supplied when the consumer submitted their application"; 76.3 obtains a means "by a manner other than through their provider under this Code"; 76.4 application not resubmitted "in accordance with clause 24".
- Submitter: Consumer NZ, agreed with - L404 "We agree with Consumer NZ34 that the requirement in clause 35.2 of the current Code is not fit for purpose, as it can put a vulnerable consumer who moves premises at risk of being without protection if they lose their vulnerable status."
- Example L405: "shift premises from an area with mobile coverage to one that does not have mobile coverage, requiring a different means such as a battery back-up."
- Draft decision L412: "81.1 remove clause 35.2 of the current Code, so that if a vulnerable consumer moves premises and remains with the same provider, that consumer does not necessarily automatically lose their vulnerable status; and 81.2 add a new clause stating that the provider may check the consumer’s status when they move premises, and may require them to re-apply if something material has changed in relation to the vulnerable consumer’s circumstances."
- Hedge scope: "may check" / "may require" are permissions given to the provider; "does not necessarily automatically lose".

### DD7 - Disclosure of time taken to provide appropriate means (Section J; paras 82-91; L414-466)
- Current Code: L416 "no later than 30 November of each disclosure year" ; disclosure items L421-428 with clause cites fn 36-39 (L435-441): 38.1, 38.2, 38.3-38.6, 38.7.
- L428 "83.3 the average number of working days from the point at which a consumer’s application is submitted to the point at which the vulnerable consumer is provided with appropriate means."
- Submitter: Spark (30 November 2022 Feedback para 35, fn 40 L443) - L432 "the requirement to provide an average number of working days taken to provide means does not provide meaningful information".
- Commission: L446 clause 27.1 "‘following the acceptance of the consumer’s application’" ; L448 "clause 18 of the current Code sets out that a consumer’s application must either be accepted or declined within 10 working days of providers receiving a complete application." ; L450 "we accept Spark’s point about the limitations of overall average provisioning times" ; "understand why providers took longer than 10 working days to provide means from the date that the consumer’s application was accepted."
- Not a compliance threshold, L452: "Providers will not necessarily be considered non-compliant if they take more time to provide the means, as non-compliance is determined by whether the means was supplied as soon as reasonably practicable."
- Draft decision L460-466: "91. Our draft decision is to amend clause 38.7 of the Code to:" ; "91.1 no longer require providers to disclose the average number of working days from the date the consumer’s application is submitted to the point that the vulnerable consumer is provided with appropriate means to contact the 111 emergency service; and" ; "91.2 require providers to disclose the provisioning timing to provide appropriate means to contact the 111 emergency service for each new vulnerable consumer (i.e., from the date that their application was accepted) in the applicable disclosure year, with brief reasons for any provisioning that took longer than 10 working days."
- Two different "10 working days" in D01: (a) clause 18 accept/decline deadline counted from receipt of a complete application (L448); (b) proposed reporting trigger counted from acceptance (L234, L450, L466). Start points: the current average runs from application SUBMITTED (L428, L465); the proposed measure runs from application ACCEPTED (L466).
- Also restated at L996 "updated the working days requirement as per paragraph 91 above."

## 5. Chapter 5 - matter under consideration, NO amendment proposed (L469-490)

- Topic: L471 "providers of residential care or assisted living facilities, including but not limited to retirement premises, rest and nursing homes, long-stay hospitals, dementia units and psycho-geriatric units (Facilities)". Raised "Outside of submissions on our Request for Views paper" (L471).
- Scenarios (L475-478): "Scenario A: The Facility purchases retail landline services, then on-sells these services to their residents. The resident is directly and separately invoiced by the Facility" ; "Scenario B: The Facility purchases services, and includes a phone in the resident’s room that is not separately paid for by the resident, but is bundled with other living costs as one bill." ; "Scenario C: The Facility does not offer retail landline services, and residents instead purchase these services directly from a retail service provider."
- Preliminary view (not a decision), L480: "It is the Commission’s preliminary view that the party who holds the direct billing relationship with the consumer is subject to the Code and must comply with all Code requirements". D01 does NOT say in this paragraph which of scenarios A-C that party is.
- Clause 21: L483 "allows a provider to consider that a consumer has an appropriate means of contacting the 111 emergency service if the consumer has access to an uninterruptable power supply". Clause 32 (fn 42 L488): L484 "If there is more than one vulnerable consumer at a premises, the means provided must be appropriate for the needs of each vulnerable consumer at that premises."
- Status L487-490: "While we currently do not consider that our existing views on this point require a Code amendment, we would like to invite submissions" ... "We are open to submissions on the three scenarios we have outlined".

## 6. Chapter 6 - 18 themes with NO proposed amendment (L493-998)

List L498-533, numbered 98.1 to 98.18. List wording vs heading wording differs for 98.13 "Other communications channels" (L522) vs "Other communication channels" (L868), and 98.18 "Review disclosure requirements" (L533) vs "Review of disclosure requirements" (L989).

| # | Theme | Submitters named in the body | Commission response (verbatim anchor) | Lines |
| --- | --- | --- | --- | --- |
| 98.1 | Application of the Code to medical alarms | "Several submissions44" = 2degrees, Spark (30 Nov 2022), TCF, One NZ (fn 44 L555-558) | L546 "We agree with TCF that consumers who have an appropriate medical alarm" ... "are already adequately protected" ; L567 "we do not consider that a blanket statement including all medical alarms as appropriate means is consistent with the purpose of the Code." | L535-567 |
| 98.2 | Clearer vulnerable consumer eligibility | Spark (16 June 2023), Grey Power, DPA | L598 "We do not believe that changes to the definition of vulnerable consumer and/or changes to the process" ... "would better meet the minimum requirements" | L569-619 |
| 98.3 | Evidence of vulnerability | One NZ, TCF | L646 "However, in our view, this does not require an amendment to the Code. Providers can include this request in their application forms." | L620-648 |
| 98.4 | Impact of satellite technology | Business Technology Group, Anonymous | L661 "do not consider this has reached the point where amendments to the Code are warranted." | L649-671 |
| 98.5 | Network resiliency | Business Technology Group, Anonymous | L684 "it is out of scope of this Code, which is limited to power failures at the consumer’s premises." | L673-685 |
| 98.6 | Providers withdrawing landline services | WISPANZ, Business Technology Group | L700 "We will continue to monitor the number of providers who withdraw their services citing reasons related to obligations under the Code" (no number) | L687-700 |
| 98.7 | Contribution of Local Fibre Companies to Code-related costs | Spark (both documents), One NZ | L715 "We remain of the view that the Code-related costs apply specifically to suppliers of retail landline services" | L702-715 |
| 98.8 | High compliance costs | Spark (30 Nov 2022), TCF, WISPANZ, One NZ | L737 "Organising a funding scheme is outside the scope of the Act." | L723-752 |
| 98.9 | Minimum period and limited market of appropriate means | Spark (30 Nov 2022), 2degrees, WISPANZ, TCF, One NZ | L780 "we do not believe the minimum period should be amended." | L754-782 |
| 98.10 | Clarification of what is out of scope | 2degrees, TCF, Spark (16 June 2023) | L806 "already clearly set out its purpose." | L784-812 |
| 98.11 | Lack of consumer awareness | DPA, Anonymous, Consumer NZ, Grey Power | L852 "It is not intended to cover all consumers who experience health vulnerabilities; only those who lack appropriate means." | L814-857 |
| 98.12 | Interested persons | NZ Police | L867 "The Commission does not have the power to amend the definition of “interested persons” in the Act." | L857-867 |
| 98.13 | Other communication channels | NZ Police, Fire and Emergency | L878 "The Code only applies to retail landline services, and states that a mobile phone is considered an appropriate means to contact the 111 emergency service." | L868-891 |
| 98.14 | Providers identify vulnerable consumers | Consumer NZ | L911 "requiring providers to seek out vulnerable consumers is not contemplated or required by the Act and risks disproportionately increasing the Code-related costs." | L893-922 |
| 98.15 | Use of term 'vulnerable' is potentially offensive | DPA, Whaikaha | L934 "The term 'vulnerable' is defined in the Act, and the Commission must stay consistent with the legislation underpinning the Code." | L923-937 |
| 98.16 | Providers should inform consumers about their right to independent information | Consumer NZ | L958 "Messaging around consumer rights, beyond those attaching to the Code, is outside the scope of this review." | L939-960 |
| 98.17 | Accessibility of Code-related information | DPA, Whaikaha | L975 "would result in a high compliance burden, particularly on smaller providers, so we do not consider that this should be a requirement under the Code." | L962-987 |
| 98.18 | Review of disclosure requirements | TCF | L996 "updated the working days requirement as per paragraph 91 above." ; L998 "Otherwise, we consider that the information disclosure requirements remain necessary and proportionate" | L989-998 |

Agreement stated without a Code change ("mentions/agrees" vs "amends"): 98.1 "We agree with TCF" (L546); 98.3 "We agree that it could be helpful" (L644); 98.4 "We agree with submitters that satellite technology is driving innovation and change" (L661); 98.5 "we do agree that network resiliency is an important matter" (L684); 98.13 "we do agree that access to emergency services more generally (e.g., via text) is important" (L878); 98.16 "We agree that independent information is important" (L955); 98.11 "We agree that the numbers of vulnerable consumers under the Code might seem low" (L842). Theme 98.18 is the one no-amendment theme where the response points to an amendment made elsewhere (para 91).

Detail anchors:
- Medical alarms: L547-548 "then that consumer does not meet the definition of vulnerable consumer under the Act or Code" ; L551 "it is open to providers to supply a new medical alarm or upgrade an existing medical alarm to satisfy their obligations under the Code" ... "This includes the requirement that the consumer will incur no costs (after any applicable government funding for the medical alarm)." ; fn 46 L561-562 "then they may lose their vulnerable consumer status" ; L565 "can be an appropriate means" ; L567 "there may be medical alarms that do not meet minimum requirements under the Code".
- Eligibility: three categories L578-582 "Health (for example, the specific circumstance is a known medical condition);" ; "Safety (for example, the specific circumstance is family violence); or 108.3 Disability (for example, the specific circumstance is sensory impairment, intellectual impairment, physical impairment).50" ; L603 "The current Code sets out the examples of health, safety and disability under clause 14.3." ; appeal route L599 "appeal that refusal through Telecommunication Disputes Resolution Scheme (TDRS)" ; L601 "Adding more details to these categories could unintentionally exclude vulnerable consumers".
- Evidence: L614 nominated person "(including name, contact details and occupation)" (clause 14.8, fn 56); L617 "must be competent, by virtue of their occupation" (fn 57 L633 "Cause 15 of the current Code." sic); fn 58 "Clause 16 of the current Code."; L627 "Clause 19 of the current Code states the grounds on which a provider is permitted to decline a consumer’s application." and "clause 19.2.2"; L648 "it is the provider who must determine whether a consumer is vulnerable" ... "cannot be delegated to a third party."
- Satellite: L669 "landline services that are delivered over satellite technology still require a power source to operate".
- Network resiliency: L685 "calibrated around ordinary power outages, rather than extended or widespread power failures."
- LFC costs: L705 "as their decision to retire the copper network is the reason the Code is required" (attributed to Spark and One NZ); L706 "LFCs should be required to pay for optical network terminal relocations where these are required to correctly install a battery back-up device." (Spark); 2020 paper paras 164-166 (fn 70).
- Costs: L732 "an alleged disproportionate impact on both Spark and any smaller providers" ; L734 "Spark, TCF and WISPANZ, along with One NZ75, also suggested that a longer-term funding model should be considered. WISPANZ in particular raised concern that the Commission would have privatised an activity that would otherwise be undertaken by the Government. One NZ suggested that the Ministry of Social Development’s scheme for monitored medical alarms could be extended to cover mobile phones and battery back-up devices."
- Minimum period: L758 "Spark78, 2degrees79, WISPANZ80, TCF81 and One NZ82 have all commented that the current continuous 8-hour minimum period requirement mean that battery back-up devices are large, expensive, and difficult to source." (five named) ; L760 "WISPANZ stated that there is only one available option for a battery back-up device that meets the minimum requirements, and that it has limited distribution options." ; L763 "These submissions suggested that the minimum period should be reduced. Spark, TCF and One NZ believe that a minimum period of 4 hours would allow providers to source cheaper and more widely available devices." (three named for 4 hours) ; L775 "TCF, One NZ, 2degrees and Spark suggested that reducing the minimum period would result in a larger pool of available devices" (four named).
- Out of scope: L802 "The word “safety” has been interpreted by customers to include situations where someone lives on their own or do not have mobile coverage, which Spark do not believe is the intention of the Code."
- Awareness: L829 "Grey Power called out that the low number of vulnerable consumers is not in line with the number of elderly people who experience health vulnerability, and therefore they consider the solutions provided have not been effective." ; L832 "at least once every 12 months" (fn 90 "Clauses 6.2 and 7.3 of the current Code.") ; L835 "some providers are not compliant with the consumer information provision requirements under the Code" ; L838 factsheet (fn 93) ; L854 "The application of the Code to residential landline services, which are used by a decreasing number of consumers".
- Interested persons: statutory list L859; NZ Police request L863 "be expanded to include Ambulance Service Providers, Hato Hone St John and Wellington Free Ambulance."
- Other channels: L871 "NZ Police would like to see the Code be extended to cover other communications channels, such as text and messaging." ; L874 FENZ figure (section 7) ; L880-888 "the text option for" ... "contacting 111 is currently limited to people that are deaf, hearing or speech impaired." (fn 99) ; L891 "powered from their nearest node (exchange or cabinet)".
- Independent information: L955 TDRS "“an independent body for the prompt, unbiased resolution of disputes”" (fn 106); clause 6.8 (fn 103 L949 "Clause 6.8 of the Code." ; fn 105 L977 "Clause 6.8 of the current Code.").
- Disclosure: L998 "having collected this data for two years now".

## 7. Number ledger (every figure in D01: body, footnotes and Appendix B quotes)

D01 contains NO numeric data table. Every statistic is in prose, a footnote, or a quotation in Appendix B. Where the same matter appears twice, both places are listed.

### 7a. Statistics and measurements

| Figure | Unit / period | Measures | Attributed to | Line | Verbatim |
| --- | --- | --- | --- | --- | --- |
| 18 | submissions on the Request for Views | submissions received | Commission | L73, L112 | "the 18 submissions we received" ; "18 submissions from 17 different parties" |
| 17 | parties | distinct submitting parties (17 names printed) | Commission | L112 | "from 17 different parties" |
| 8% | of appropriate means, 2021 | battery backups | Commission, "our assessment of annual disclosures" | L750 | "Battery backups are supplied in relatively lower numbers, making up 8% of appropriate means in 2021 and 15% in 2022." |
| 15% | of appropriate means, 2022 | battery backups | same | L750 | same sentence |
| 76% | of vulnerable consumers, 2021 | provided with a mobile | Commission, fn 77 | L767 | "76% of vulnerable consumers were provided with a mobile in 2021, and 79% in 2022." |
| 79% | of vulnerable consumers, 2022 | provided with a mobile | Commission, fn 77 | L767 | same sentence |
| 92% | of outages | resolved within eight hours | "Our analysis" in the original (2020) Decisions and Reasons paper (fn 83: paras 175-180) | L780 | "Our analysis showed that 92% percent of outages are resolved within eight hours" (sic) |
| "some 30%" | of outages | NOT resolved at four hours | same | L780 | "By contrast, at four hours, some 30% of outages are not resolved" |
| "around 85%" | of emergency calls | made by mobile phones | Fire and Emergency (body paraphrase; fn 97 FENZ 21 June 2023 page 2) | L874 | "Fire and Emergency also submitted that around 85% of emergency calls are made by mobile phones." |
| "approximately 85%" | of the time | Fire and Emergency 111 calls originating from mobile phones | Fire & Emergency (direct quote, Appendix B ref 186) | L1404 | "Fire and Emergency 111 calls originate approximately 85% of the time from mobile phones." |
| "only 15%" | of 111 calls to Police | landline phone calls ("now") | NZ Police (direct quote, Appendix B ref 185) | L1394 | "Landline phone calls now account for only 15% of 111 calls to Police" |
| 573 | people | registered as vulnerable (no date given) | Grey Power (direct quote, Appendix B ref 173) | L1371-1372 | "only" / "573 people are registered as vulnerable" (line break after "only") |
| Twenty-four percent (167,900) | of older people | experience health vulnerability (a quotation inside Grey Power's quote; its source is not named in D01) | Grey Power quoting an unnamed source | L1372-1374 | "‘Twenty-four percent (167,900) of older 173" / "people experience health vulnerability.’" (page break and ref number "173" fall inside the sentence) |
| "less than $20.00" | NZ$ per month ("often") | standard monthly rental of the phone service | WISPANZ (direct quote, Appendix B ref 149, 150) | L1323 | "The standard monthly rental is often less than $20.00" |
| "easily exceeds $1000.00" | NZ$ (no period) | cost of providing mains power backup incl. installation and maintenance | WISPANZ (same quote) | L1323 | "the cost of providing the mains power backup, including installation and maintenance easily exceeds $1000.00." |
| "half the price" | relative price | Ecoflow River Power Station vs Ecoflow River Pro | Spark (direct quote, Appendix B ref 156, 160) | L1340 | "This device is half the price of the Ecoflow River Pro" |
| 4 hours (tested) | hours | Ecoflow River Power Station battery life in testing | Spark (same quote) | L1340 | "which has been shown in testing to last 4 hours" |
| "in the next 10 years" | years | Chorus's announced plan to retire its entire copper network | One NZ (direct quote, Appendix B ref 143) | L1306 | "Chorus has recently announced that they plan to retire their entire copper network in the next 10 years" |
| 7 pages | pages | Grey Power's copy of the registration document | Grey Power (direct quote, ref 58) | L1154 | "runs to 7 pages" |
| 11 pages | pages | Vulnerable Consumers application form on the Spark website | Whaikaha (direct quote, ref 58) | L1167 | "The document is 11 pages long" |

Rounded prose vs exact figure, and same matter stated twice:
- "the majority of vulnerable consumers are provided with a mobile phone as appropriate means" (body, L749) is quantified only in fn 77 (76% / 79%, L767). Not in a table.
- "relatively lower numbers" (body, L750) is quantified in the same sentence (8% / 15%).
- Grey Power: body L829 "the low number of vulnerable consumers" (no figure) vs Appendix B quote L1371-1374 (573; Twenty-four percent; 167,900). The body says "elderly people"; the quote says "older people". The percentage is spelled out in words ("Twenty-four percent"); 167,900 is in digits.
- Fire and Emergency: body L874 "around 85% of emergency calls are made by mobile phones" vs quote L1404 "Fire and Emergency 111 calls originate approximately 85% of the time from mobile phones" (hedge word and described population differ; value the same).
- 36 months (Commission, L353/L356/L368/L224) vs "3 years" (Spark quote, L1187-1189).
- 8 hours: "continuous 8- hour period" (L353), "continuous eight-hour period" (L755), "continuous 8-hour minimum period" (L758, L782), "Minimum Period of 8 hours" (Spark quote L1340), "minimum period of eight hours" / "eight-hour requirement" (TCF quote L1348), "minimum of eight continuous hours" (TCF quote L1326), "continuous eight hours under the current Code" (TCF quote L1232).
- 4 hours: "a minimum period of 4 hours" (L763), "at four hours" / "to four hours" (L780), Spark quote "to 4 hours" (L1340), TCF quote "to four hours" (L1350), One NZ quote "a continuous four-hour period" (L1354). 2degrees quote gives no number: L1338 "Reducing the timeframe for the battery-backup".
- Parts of printed totals: none. No total, sum or residual is printed for the percentage pairs. The bases differ: 8%/15% are "of appropriate means"; 76%/79% are "of vulnerable consumers". 167,900 is given as the count equal to "Twenty-four percent" of older people; the base population is not printed. NZ Police's 15% (landline share of "111 calls to Police") and Fire and Emergency's ~85% (mobile share of "Fire and Emergency 111 calls") describe different agencies' calls; D01 does not connect them.
- Hedge attachment: "around" (L874) and "approximately" (L1404) attach to 85%; "some" attaches to 30% (L780); "only" to 15% (L1394) and to 573 (L1371); "often less than" to $20.00 and "easily exceeds" to $1000.00 (L1323); "at least" to the 36-month and 12-month intervals; 92% carries no hedge.

### 7b. Rule, threshold and count numbers

| Figure | What | Qualifier | Line | Verbatim |
| --- | --- | --- | --- | --- |
| 8 hours | current minimum period | "continuous" | L353, L755, L758, L782 | see above |
| 4 hours | minimum period sought by Spark, TCF, One NZ - not adopted | submitter proposal | L763, L780 | "a minimum period of 4 hours" |
| 36 months | current replacement interval (clause 29.3) | "at least every" / "at least once every" | L353, L356, L368, L224 | "be replaced at least every 36 months from the date the last means was installed" |
| 12 months | information to all customers | "at least every" (L282) / "at least once every" (L832) | L282, L832 | as quoted in sections 4, 6 |
| 12 months | Spark: device "expected to continue to function as required for another 12 months" | submitter | L1189 | as quoted |
| annual | clause 33 monitoring | "on at least an annual basis" | L358 | "on at least an annual basis" |
| 10 working days | clause 18 accept/decline, from receipt of a complete application | "within" | L448 | "within 10 working days of providers receiving a complete application" |
| 10 working days | proposed reporting trigger, from acceptance | "longer than" | L234, L450, L466 | "longer than 10 working days" |
| 30 working days | statutory submission period after public notice | "within" / "not later than" | L191, L1057 | as quoted in section 1 |
| 30 November | disclosure deadline | "no later than" | L416, L991 | as quoted |
| two years | Code in force when review began; data collected | - | L162, L998 | "as the Code had been in force for two years" ; "having collected this data for two years now" |
| three | categories (health, safety, disability) | - | L578 | "which of three categories most closely relates" |
| three | Facility scenarios A-C | - | L490 | "the three scenarios we have outlined" |
| four | circumstances a consumer may no longer be considered vulnerable (76.1-76.4) | "any of the following" | L391-398 | - |
| four | statutory interested persons (i)-(iv) | "include" | L859 | "(i) the New Zealand Police, (ii) Fire and Emergency New Zealand, (iii) the Director of Civil Defence Emergency Management, and (iv) every provider of an initial call answering point for the 111 emergency service." |
| one | compliant battery back-up option per WISPANZ (body) | submitter claim | L760 | "there is only one available option" |
| 7 | proposed amendments (table IDs 1-7) | - | L214-234 | - |
| 18 | no-amendment themes (98.1-98.18) | - | L500-533 | - |
| "1 or more" | things the code may do (s 238(4)) | statute | L1029 | "The code may do 1 or more of the following:" |
| 3rd | "3rd party validation" (Whaikaha quote) | - | L1169 | "The form also requires 3rd party validation" |

Not in D01 (whole file read; Grep for "survey", "complaint", "Stats NZ"): no survey results; no count of complaints, calls or providers; no total number of vulnerable consumers stated by the Commission (the only registration count is Grey Power's quoted 573); no Stats NZ citation; "complaint" occurs only as a word (L940, L1067, L1081).

## 8. Defined terms, rules, exceptions (exact text)

- Vulnerable consumer - Act s 238(5), restated L142-144: "The Act defines a vulnerable consumer8 as being a consumer of a specified telecommunications service who:" / "19.1 is at particular risk of requiring the 111 emergency service (for example, due to a known medical condition); and" / "19.2 does not have a means for contacting the 111 emergency service that can be operated for the minimum period in the event of a power failure." Statute text L1036-1038.
- Vulnerable consumer - current Code clause 9, L574-575: "9. A vulnerable consumer means a consumer of a retail landline service, who:" / "9.1 is at particular risk of requiring the 111 emergency service; and 9.2 does not have a means for contacting the 111 emergency service that can be operated for the minimum period, in the event of a power failure." (Act: "specified telecommunications service"; Code: "retail landline service".)
- "At particular risk" - current Code clause 10, L577: "means a consumer who is more likely than other consumers to require the 111 emergency service because of a specific circumstance applicable to that consumer."
- Short description L925: "vulnerable consumers are consumers who are at particular risk of requiring the 111 emergency services, and who do not have a means to contact 111 in a power failure."
- Minimum period - Act, L1036: "minimum period means the minimum period specified under subsection (3)(e)". Current Code value L353 (continuous 8 hours).
- Specified telecommunications service - Act, L1036: "means a telecommunications service specified in the Commission 111 contact code as a service to which the code applies".
- Provider (glossary L22): "A provider of a retail landline service". RSP (glossary L25): "A provider of retail telecommunications services".
- Appropriate means - current Code as described, L351: "appropriate means is a means that is appropriate for the consumer’s specific circumstances, taking into account their physical, mental and technical capabilities." Conditions to count as meeting the minimum period, L353: "the means must be fitted with a battery health indicator which is appropriate to the needs of the vulnerable consumer and be replaced at least every 36 months". Clause 26 restated L384 ("taking into account in particular the consumer’s physical, mental and technical capabilities").
- Retail landline service: NOT defined in D01 (see fn 19 L286; proposal to change the term to "residential landline services", L270).
- Business landline services: to be defined in the amended Code (L268); no definition text in D01.
- Facilities: defined by enumeration at L471 (section 5).
- Interested persons - Act s 239(2), L1048-1056.
- Mobile phone as appropriate means: L878 (fn 98 L886 "Clause 21.2 of the current Code."). Uninterruptable power supply: clause 21, L483.
- Scope limit: L675 "The scope of the Code is limited to power failures at the vulnerable consumer’s premises."
- Cost rule: L145 "at no additional cost" ; L350 "at no cost to the vulnerable consumer" ; statute L1027 "at no cost to the consumers".
- Test for amending: L195-196 "We do not consider that we are constrained by section 239(5) to only consider amendments where there is clear gap" ; "permitted to make amendments to the Code where the amended Code would better meet the minimum requirements" ; statute L1060 "The Commission may amend or revoke a code if the Commission considers that the code no longer meets all the requirements set out in this Part."
- Current-Code clause numbers cited in D01: 6, 6.2, 6.8, 7, 7.1, 7.2, 7.3, 9, 9.1, 9.2, 10, 13, 13.1, 13.2, 13.3, 13-24, 14.3, 14.8, 15, 16, 18, 19, 19.2.2, 21, 21.2, 21.3 (BTG quote L1292 "section 21.3"), 24, 26, 27.1, 29.3, 32, 33, 35.2, 37, 38, 38.1, 38.2, 38.3-38.6, 38.7; Sections B, E, F, F2, G, H, J; Attachment A (L339).
- Statutory provisions cited: 9A(1)(c)-(d); 238(1), 238(3), 238(3)(a)-(d), 238(4)(c), 238(5); 239, 239(3), 239(5); Part 7 (L186). Appendix A reproduces ss 9A, 238, 239, 240, 241 (L1005-1083). fn 12 L206 says "Clause 238(4)(c)"; TCF quote L1230 says "cl. 238(4)(b)".

## 9. Appendix B - Summary of submissions (L1086-1433; printed pages 50-73)

Columns (L1088-1089): "Submitter | Quotes | Reference in paper (para number)". Text table of direct quotations; the reference number follows each quote (sometimes in the middle of a quote that crosses a page break, e.g. L1125 "45", L1187 "67", L1372 "173"). Intro L1087 "This table provides a summary of submissions and proposals aligned to the requirements in the Code."

Three parts: "Overall feedback on efficacy of Code" (L1091); "Submissions related to changes we are proposing" (L1124); "Submissions we consider do not result in a Code amendment" (L1213).

| Part / subheading | Submitter (line) | Ref para(s) |
| --- | --- | --- |
| Overall - "Code is currently meeting its purpose" (L1092) | 2degrees (L1093) | 26 |
| | Mercury (L1093) | 26 |
| | Spark (L1095-1098) | 26 |
| | WISPANZ (L1101) | 26 |
| | TCF (L1106) | 26 |
| | One NZ (L1109) | 26 |
| Overall - "Code is not currently meeting its purpose" (L1112) | DPA (L1113-1114) | 27 |
| | Consumer NZ (L1117-1119) | 27 |
| | Grey Power (L1121) | 27 |
| Proposed - Application of the Code to business landline services | 2degrees (L1125-1127) | 45 |
| | WISPANZ (L1128-1132) | 46 |
| | NZ Police (L1135) | 47 |
| Proposed - Code-related information on providers’ websites | Whaikaha (L1140-1142) | 51 |
| | DPA (L1145-1149) | 51 |
| | Consumer NZ (L1150) | 51 |
| Proposed - Application form template and requirements | Grey Power (L1154) | 58 |
| | Spark (L1159-1164) | 58 |
| | Whaikaha (L1167-1172) | 58 |
| | TCF (L1177-1185) | 58 |
| Proposed - Replacement of appropriate means supplied to consumers | Spark (L1187-1189) | 67 |
| Proposed - When a means can be considered appropriate | Spark (L1192) | 70 |
| | TCF (L1195) | 70 |
| | WISPANZ (L1198) | 71 |
| Proposed - Vulnerable status when moving premises | Consumer NZ (L1201) | 79 |
| Proposed - Disclosure of time taken to provide appropriate means | Spark (L1206-1211) | 84 |
| No amendment - Application of the Code to medical alarms | 2degrees (L1214) | 101 |
| | Spark (L1216-1226) | 101 |
| | TCF (L1227-1237) | 101, 102 |
| | One NZ (L1239-1245) | 101 |
| No amendment - Clearer vulnerable consumer eligibility | Grey Power (L1247) | 110 |
| | DPA (L1249-1250) | 110, 111 |
| | Spark (L1253-1254) | 109 |
| No amendment - Evidence of vulnerability | TCF (L1260) | 124 |
| | One NZ (L1263-1264) | 123 |
| No amendment - Impact of satellite technology | Business Technology Group (L1267-1273) | 129 |
| | Anonymous (L1275) | 130 |
| No amendment - Network resiliency | Business Technology Group (L1278-1281) | 135 |
| | Anonymous (L1283-1284) | 136 |
| No amendment - Providers withdrawing landline services | Business Technology Group (L1287-1292) | 140 |
| | WISPANZ (L1293-1294) | 140 |
| No amendment - Contribution of Local Fibre Companies to Code-related costs | Spark (L1296-1301) | 143, 144 |
| | One NZ (L1304-1306) | 143 |
| No amendment - High compliance costs | Spark (L1308-1311) | 149, 150 |
| | WISPANZ (L1314-1325) | 149, 150 |
| | TCF (L1326-1329) | 149, 150 |
| | One NZ (L1334-1336) | 150 |
| No amendment - Minimum period and limited market of appropriate means | 2degrees (L1338) | 156, 159 |
| | Spark (L1340) | 156, 160 |
| | WISPANZ (L1345) | 156, 157, 159 |
| | TCF (L1348-1350) | 156, 158, 159 |
| | One NZ (L1353-1357) | 156, 158, 159 |
| No amendment - Clarification of what is out of scope | 2degrees (L1359) | 164 |
| | Spark (L1362) | 165 |
| | TCF (L1364) | 164 |
| No amendment - Lack of consumer awareness | Consumer NZ (L1368) | 171, 172 |
| | Grey Power (L1371-1374) | 173 |
| | Anonymous (L1376) | 171 |
| | DPA (L1379-1382) | 171, 172 |
| No amendment - Interested persons | NZ Police (L1386) | 182 |
| No amendment - Other communications channels | NZ Police (L1390-1401) | 185 |
| | Fire & Emergency (L1404) | 186 |
| No amendment - Providers identify vulnerable consumers | Consumer NZ (L1408-1410) | 190 |
| No amendment - Use of the term 'vulnerable' is potentially offensive | Whaikaha (L1413) | 195, 196 |
| | DPA (L1413-1415) | 195, 196 |
| No amendment - Providers should inform consumers about their right to independent information | Consumer NZ (L1417) | 200 |
| No amendment - Accessibility of Code-related information | Whaikaha (L1419-1421) | 206 |
| | DPA (L1424-1426) | 206 |
| No amendment - Review of disclosure requirements | TCF (L1431) | 211 |

- Distinct submitters quoted in Appendix B: 2degrees, Mercury, Spark, WISPANZ, TCF, One NZ, DPA, Consumer NZ, Grey Power, NZ Police, Whaikaha, Business Technology Group, Anonymous, Fire & Emergency = 14. Not quoted: Sky, MyRepublic, TUANZ.
- Appendix B has 7 "proposed" subheadings (same order as table IDs 1-7) and 18 "no amendment" subheadings (same order as 98.1-98.18). Heading wording differs from chapter headings in places: "Replacement of appropriate means supplied to consumers" (L1187) vs "...supplied to vulnerable consumers" (L355); "Use of the term 'vulnerable'" (L1413) vs "Use of term ‘vulnerable’" (L923).
- Reference-column entries that point at a paragraph where the submitter is not the one named (recorded as printed, not resolved): Spark minimum-period quote ref "156, 160" (L1342) - para 160 (L778) is the Commission's Response paragraph; Spark is named in paras 156, 158, 159. WISPANZ minimum-period quote ref "156, 157, 159" (L1347) - para 159 (L775) names "TCF, One NZ, 2degrees and Spark". Anonymous awareness quote ref "171" (L1378) - Anonymous is also named in para 172 (L827).
- Quote anchors with content not repeated in the body:
  - Spark overall, L1098 "We observe an increase in applications shortly after we send our annual reminders about the scheme."
  - WISPANZ, L1132 "RSPs can’t opt out from providing service"; L1314 "[Low number of vulnerable consumers] also comes as a relief" (square-bracket insertion is D01's); L1321 "many school pupils receive free of charge internet services, a process initiated by government during the COVID lockdowns."
  - Whaikaha, L1142 "In developing this response we looked into other sites [] No alternative formats could be located." (empty brackets as printed); L1167 the form "on the Spark website"; L1171 quotes clauses "13.1" and "13.2"; L1419 "Whaikaha has not considered other telco websites of practices in preparing this response."
  - Grey Power, L1154 "signed off by their general practitioner or a J.P. etc."
  - TCF, L1183 "c. The form should clarify that an existing medical alarm that allows the customer to contact 111 means the consumer is not eligible for additional support under this Code." ; L1348 "found no device at that time which could meet the eight-hour requirement" ; "an overseas supplier which subsequently had supply chain issues and pulled the model from the market".
  - One NZ, L1353 "At the time, there were no devices in the world that could meet the set requirements." ; L1334 "the number of qualifying vulnerable consumers under the Code increases as the copper network is retired".
  - Spark, L1253 "at least one retailer provides an indicative list of eligible health, disability and safety criteria on this application form" ; L1301 "Chorus should cover the cost of meeting the Code’s requirements".
  - BTG, L1280 "Cyclone Gabrielle presented a number of large outages (outside the Hawkes Bay / Gisborne areas) due to loss of power including a large part of Northland." ; L1289 "only in mobile coverage areas so they can meet the requirement under 21.2".
  - NZ Police, L1386 "per foot note 7 for paragraph 19.2" (a reference to the Request for Views paper's numbering) ; L1395-1396 "limited" / "111 SMS text service for the deaf and speech impaired community on behalf of all ESOs" ; L1401 "available at no cost to consumers (private or business) and able to be used regardless of whether there is any credit available on the device".
  - Consumer NZ, L1408 "As stated in our previous submission on the draft code" ; L1409 the 2degrees / JustAnswer customer example ; L1417 "clause 6 of the Code does not create an obligation on the provider to inform the consumer about their right to access independent information."
  - DPA, L1415 "does not align with the principles and rights in the UNCRPD." ; L1426 "New Zealand Sign Language, Braille, Easy Read, audio and large print." (five formats; the body L967 names two "such as New Zealand Sign Language or Easy Read").
- Body paraphrase vs Appendix B quote (both locations; no precedence stated):
  - 2degrees: body L249 "applies to residential services only" vs quote L1127 "which may include clarification that the Code should apply to consumers of residential services."
  - WISPANZ: body L760 "only one available option" vs quote L1345 "The sole off the shelf device suitable for the purpose available in New Zealand has very limited distribution options. There is a New Zealand built option which shows promise but is such a niche product that the manufacturer does not have it in their current product line".
  - BTG: body L654 "could negate the need for the 111 Code" vs quote L1273 "many sections may become redundant. The entire code may no longer be needed."
  - LFCs: body L705 "their decision to retire the copper network" (LFCs generally) vs quotes naming Chorus (L1301, L1306, L1336) and Spark L1296 "they made the business decision to not offer battery solutions as standard for all customers".
  - MSD scheme: body L734 attributes the MSD-extension suggestion to One NZ; TCF's quote L1329 also says "possible through existing arrangements established by MSD for monitored medical alarms".

## 10. Outside organisations quoted with figures (period and source as D01 gives them)

| Organisation | Figure | Period stated | Source D01 cites | Line |
| --- | --- | --- | --- | --- |
| Fire and Emergency (FENZ) | ~85% of (Fire and Emergency) 111 / emergency calls from mobile phones | none | FENZ RfV submission (21 June 2023) page 2 (fn 97); direct quote in Appendix B | L874, L885, L1404 |
| NZ Police | landline calls "only 15% of 111 calls to Police" | "now" (no date) | NZ Police RfV submission, direct quote in Appendix B (ref 185); body fn 96 cites pages 1 & 2 | L1394 |
| Grey Power | "573 people are registered as vulnerable" | none | Grey Power RfV submission, direct quote (ref 173); body fn 89 cites page 2 | L1371-1372 |
| Grey Power (quoting an unnamed source) | "Twenty-four percent (167,900) of older" ... "people experience health vulnerability" | none | inner quotation; source not named in D01 | L1372-1374 |
| Grey Power | registration document "runs to 7 pages" | none | direct quote (ref 58); body fn 26 cites page 3 | L1154 |
| Whaikaha | Spark-website form "is 11 pages long" | none | direct quote (ref 58); body fn 28 cites page 1 | L1167 |
| WISPANZ | rental "often less than $20.00" per month; backup cost "easily exceeds $1000.00" | none | direct quote (ref 149, 150); body fn 74 cites page 5 | L1323 |
| WISPANZ | "only one available option" (body) / "The sole off the shelf device" (quote) | none | fn 80 page 5; quote L1345 | L760, L1345 |
| Spark | Minimum Period "8 hours"; "4 hours"; Ecoflow River Power Station "half the price of the Ecoflow River Pro" | none | direct quote (ref 156, 160); body fn 78 = Feedback (30 November 2022) para 34 | L1340 |
| Spark | "every 3 years"; "longer than 3 years"; "another 12 months" | none | direct quote (ref 67); body fn 31 = RfV submission (16 June 2023) para 26 | L1187-1189 |
| One NZ | Chorus to retire its entire copper network "in the next 10 years" | "recently announced" | direct quote (ref 143); body fn 68 para 14 | L1306 |
| One NZ | "a continuous four-hour period" | none | direct quote (ref 156, 158, 159); body fn 82 para 13 | L1354 |
| TCF | "minimum period of eight hours"; "to four hours"; "minimum of eight continuous hours" | none | direct quotes; body fn 81 para 8-10, fn 73 para 16-17 | L1348-1350, L1326 |
| Minister Fa’afoi | no figure (quoted at the third reading of the Telecommunications (New regulatory framework) Amendment Bill) | none | fn 76 | L765 |
| TDRS | no figure (quoted self-description) | none | fn 106 | L955, L979 |

Commission's own figures (issuer, not an outside organisation): 8% / 15% battery backups in 2021 / 2022 (L750); 76% / 79% mobiles in 2021 / 2022 (fn 77, L767); 92% within eight hours and "some 30%" unresolved at four hours, from the analysis in its 2020 paper (L780).
No figure is attributed to Stats NZ (not mentioned), TDRS, TUANZ, Sky, MyRepublic, Mercury, 2degrees, DPA, Consumer NZ, BTG or Anonymous.

## 11. Years/events, and things stated differently in two places inside D01

Year/event statements:
- 2018: Act amended (L136). 2020: Code and Decisions and Reasons paper published 17 November (L139). 2021: Code in force 1 February; section G in effect 1 August (L140); battery backups 8% and mobiles 76% (L750, L767). 2022: "Throughout 2022" compliance engagement (L160); 30 November 2022 industry-wide compliance review commenced (L160) / annual disclosures provided by that date (L835); battery backups 15% and mobiles 79% (L750, L767). 2023: Request for Views 18 May (L110); this paper 18 December (L8). 2024: submissions due 1 March (L116).
- Review rationale: L162 "as the Code had been in force for two years" ; L671 "We retain the ability to review the Code at any time should we consider that technological or other changes warrant it." ; L90 "The Act allows the Commission to review the Code at any time".
- Technology transition: L141 "Telecommunications technologies are currently transitioning from copper lines to modern technology such as fibre and wireless broadband."
- Monitoring focus: L175 "we are focusing our compliance enforcement in this area".

Stated differently in two places (both locations; D01 gives no precedence):
1. Consumer NZ submission date: "15 June 2023" (fn 23 L316; fn 34 L409) vs "16 June 2023" (fn 88 L824; fn 101 L918; fn 104 L951).
2. Compliance review start: L160 "On 30 November 20229 we commenced an industry-wide review" vs L835 "Following annual disclosures being provided to the Commission by 30 November 2022 we conducted an industry-wide review".
3. Disclosure period label: "2021/22 Code disclosure year" (fn 9 L179; fn 91 L846) vs "the 2022 disclosure year" (L162).
4. Disclosure deadline wording: L416 "30 November of each disclosure year" vs L991 "30 November of each year".
5. Clause for the provisioning-time disclosure: "Clause 40.7" (summary table, draft amended Code, L234) vs "clause 38.7 of the Code" (para 91, L460).
6. Clause for moving premises: "Clause 37" (table, L228) vs "clause 35.2 of the current Code" (L412); and "Clause 37 of the current Code" used for another provision (fn 55, L611).
7. Replacement interval wording: "every 36 months" (table L224) vs "at least every 36 months" (L353) vs "at least once every 36 months" (L356, L368).
8. Fire and Emergency figure: "around 85% of emergency calls" (L874) vs "Fire and Emergency 111 calls originate approximately 85% of the time" (L1404).
9. Minimum-period submitters: five named for the general complaint (L758), three for "4 hours" (L763), four for the larger-pool point (L775).
10. Name of the Code's scope term: "retail landline service(s)" throughout (fn 19) but L854 "The application of the Code to residential landline services, which are used by a decreasing number of consumers" in a passage describing the current position.
11. Paper's own name: "Draft Decisions and Reasons paper" (L81, L93) vs L116 "this Decisions and Reasons paper".
12. Appendix B reference numbers vs body paragraphs (section 9: Spark "156, 160"; WISPANZ "156, 157, 159").
13. List vs heading wording for themes 98.13 and 98.18 (section 6).
14. Typographic: L780 "92% percent"; L353 "8- hour"; L633 "Cause 15"; L25 merged glossary rows.

## 12. Cross-references out of D01, and gaps

Cross-references:
- Request for Views paper: fn 2 URL L85 "https://comcom.govt.nz/__data/assets/pdf_file/0018/316170/111-Contact-Code-Review-Request-forViews.pdf." ; fn 4 L106 "Request for Views Paper, May 2023, paragraphs 13 to 15." ; ISBN L15. In bundle as D02.
- 2020 paper, "Commission 111 Contact Code: Decisions and Reasons Paper" (17 November 2020), pinpoints: para 93 (fn 14, 15); paras 147 and 149 (fn 43); para 43 (fn 50); paras 164-166 (fn 70); paras 65-66 and 150 (fn 71); para 175-180 (fn 83); para 2 (fn 84); para 22 (fn 92). Not among the 14 bundle documents (manifest sources).
- Draft amended Code ("Draft Commission 111 Contact Amended Code 2023", ISBN 978-1-991085-62-7): published alongside (L81, L93, L189). In the bundle it appears only as the tracked-changes copy inside the TCF submission D08 (D08 L4 "ISBN 978-1-991085-62-7", L7 "[Draft] Commission 111 Contact Amended Code 2023").
- Spark "Feedback on 111 Contact Code" (30 November 2022) = D11: paras cited 12, 13-21, 24, 30, 33, 34, 35, 41-45.
- Spark RfV submission (16 June 2023) = D12: paras 26, 27-29, 30-32, 32.
- One NZ RfV submission (16 June 2023) = D09: paras 7-10, 13, 14, 14-15, 16.
- TCF RfV submission (cited as 19 June 2023) = D13: paras 5, 7, 8-10, 11-14, 16-17, 20, 21-22, 22.
- WISPANZ RfV submission (16 June 2023) = D14: page 5 (every cite).
- DPA RfV submission (16 June 2023) = D07: pages 4, 5, 6, 7.
- Cited RfV submissions NOT in the bundle: 2degrees, NZ Police, Whaikaha, Consumer NZ, Grey Power, BTG, Anonymous, FENZ (and uncited Mercury, Sky, MyRepublic, TUANZ).
- Internal: para 25 L168 "These responses are summarised in Appendix B. Overall comments on the efficacy of the Code are included at the start of the table." ; L183 Appendix A.
- Websites: fn 93 factsheet URL (L850); fn 99 "https://www.police.govt.nz/111-txt." (L914); fn 106 "https://www.tdr.org.nz/about-tdr." (L979).

Gaps:
- Figure 1 (L857): only the caption "Figure 1: Subset of consumers entitled to receive appropriate means" and the lead-in L855 "The diagram below indicates the criteria a consumer must meet to be considered vulnerable under the Code." are in the text. The diagram's content is absent from both `text/D01.txt` and the `docs/` original (a .txt). Visually unresolved; nothing can be taken from the figure.
- Table cells are run together in the text layer (summary table L214-237; Appendix B). Row boundaries were reconstructed from the reading order; Appendix B reference numbers sometimes fall mid-quote at page breaks (L1125, L1187, L1232, L1289, L1304, L1354, L1372, L1413).
- No unread ranges.

## 13. Shared ground (D01 facts repeated, restated or contradicted elsewhere in the bundle)

Other documents were only Grepped / spot-read for these matches; they are NOT mapped here. Line numbers are in the named `text/D*.txt`.

Edition relationship:
- D02 (Request for Views, 18 May 2023) -> D01 (draft decisions, 18 December 2023) -> D06 (final Decisions and Reasons, D06 L12 "Date of publication: 26 June 2024") and D05 (final Code). D06 cites D01 by paragraph: D06 L467 "(18 December 2023) paras 92-95." ; L612 "paras 103-105." ; L791 "para 61." ; L1011 "para 85."
- D06 calls the pre-review code "the Previous Code" and gives old -> new clause numbers, e.g. D06 L859 "clause 29.3 of the Previous Code (now clause 33.3 of the Code)" ; L967 "clause 35.2 of the Previous Code (otherwise now clause 42.2 of the Code)" ; L715 "clause 7.4.2 of the Previous Code (now clause 9.4.2 of the Code)". D01 uses "the current Code" for the same instrument.
- D08 is the TCF's tracked-changes copy of the draft amended Code; D08 L443 shows the renumbering D01's table relies on: "38.740.7 the provisioning timing to provide appropriate means for each new vulnerable consumer".

Titles and ISBNs (associated-documents tables):
- D01 L16 "18 December 2023 ISBN 978-1-991085-62-7 Draft Commission 111 Contact Amended Code 2023" ; D06 L20-22 "18 December 2023 ISBN 978-1-991085-62-7" / "Draft Commission 111 Contact Amendment" / "Code 2023" ; D08 L14 "18 December 2023 ISBN 978-1-991085-62-7 Commission 111 Contact Amended Code [2024]" ; D08 L7 "[Draft] Commission 111 Contact Amended Code 2023".
- D01's own ISBN -63-4 is repeated at D06 L23 "18 December 2023 ISBN 978-1-991085-63-4 Draft Decisions and Reasons paper", D05 L45 and D08 L60.

Dates:
- Code in force: D01 L140 "The Code came into force on 1 February 2021, and section G came into effect on 1 August 2021.7" ; D02 L62 "The Code was published on 17 November 2020 and came into effect on 1 February 2021. Providers had until 1 August 2021 to provide vulnerable consumers with an appropriate means for contacting 1114." ; D06 L142 "The Previous Code came into force on 1 February 2021, and section G (now section H) came into effect on 1 August 2021.11" ; D05 L104 "1.1 Section H comes into force on 1 August 2021; and 1.2 the rest of this Code comes into force on 1 February 2021." ; D08 L102 "1.1 Section G comes came into force on 1 August 2021".
- 30 November 2022: D01 L160 "we commenced an industry-wide review of compliance with the Code" ; D06 L161 "On 30 November 2022 we commenced an evaluation of compliance with the Previous Code.13". Both carry the "2021/22" disclosure-year footnote (D01 L179; D06 L166).
- Two years: D01 L162 ; D02 L64 "As the Code has now been in force for two years" ; D06 L162 "as it had been in force for two years".
- Request for Views deadline vs submission dates D01 cites: D02 L150 "We are seeking submission on our paper by 5pm on Friday 16 June 2023." ; D01 cites TCF as 19 June 2023 and FENZ as 21 June 2023 (L343, L885).
- TCF submission date: D01 "19 June 2023" (eight footnotes, e.g. L343) vs the TCF document itself, D13 L7 "16 June 2023".
- DPA: D01 "16 June 2023" (e.g. L315) vs D07 L4 "June 2023" (no day). WISPANZ: D01 "16 June 2023" (L284) vs D14 (no year or date string found by Grep). One NZ: D09 L4 "16 June 2023" (agrees). Spark: D12 L6 "16 June 2023", D11 L6 "30 November 2022" (agree).
- Consumer NZ date: D06 L971 "113 Consumer NZ “Submission on 111 Contact Code Review Request for Views” (15 June 2023) page 3" (same as D01 fn 34; D01 fn 88/101/104 say 16 June).
- Forecast vs actual timetable: D02 L134-143 indicative timeframe "Draft Decision paper issued" / "Draft amended Code issued" ... "July/August" ; "Submissions received August/September" ; "Cross-Submissions received September" ; "Final Decision paper issued" ... "October". D01 actual: published 18 December 2023 (L8), submissions due 1 March 2024 (L116), no cross-submission step stated. D06 actual final: 26 June 2024 (D06 L12).
- D01's 1 March 2024 deadline vs dates of submissions on the draft as cited in D06: D06 L197 RWNZ "(25 February 2024)" ; L199 Ryman "(29 February 2024)" ; L207 ACA "(23 February 2024)" ; others "(1 March 2024)" ; D04 L93 "1 March 2024".
- Submission e-mail address: D01 L118 "telecommunications@comcom.govt.nz" vs D02 L153 "market.regulation@comcom.govt.nz".

Counts of submissions:
- D01 L112 "We received 18 submissions from 17 different parties:" = D06 L169 "We received 18 submissions from 17 different parties in response.14" ; D06 fn 14 (L186) lists the same 17 in alphabetical order.
- On the draft (after D01): D06 L179 "We received submissions from 10 parties on our Draft Decisions and Reasons paper:" (names at D06 L180).

Statistics:
- 8%/15%, 76%/79%, 92%, "some 30%", ~85% (FENZ), 15% (NZ Police), 573 and 167,900 (Grey Power): Grep of all other `text/D*.txt` for these digits found NO repeat. They are D01-only in this bundle.
- WISPANZ dollars: D01 L1323 = D14 L80 "The standard monthly rental is often less than $20.00 but the cost of providing the mains power backup, including installation and maintenance easily exceeds $1000.00."
- One NZ / Chorus: D01 L1306 = D09 L38 "Chorus has recently announced that they plan to retire their entire copper network in the next 10 years".
- Spark battery: D01 L1340 = D11 L117 (para 34) "This device is half the price of the Ecoflow River Pro". D11 L92 additionally prints "The EcoFlow RIVER Pro has a retail price of $1,599 (including GST)." - that price is NOT in D01.
- Spark 3 years: D01 L1187 "We suggest the requirement to replace a device every 3 years" vs D12 L90 "26. As a further point, we suggest the requirement to replace a device every 3 years" (Appendix B drops the lead-in).
- Spark "overall" quote in Appendix B (L1095-1098) joins text from two Spark documents: D11 L22 "9. We think the balance of the Code is about right at present and do not consider the scope should be extended" and D12 L9 "1. In our experience the 111 Contact Code appears to be working well."
- Spark LFC quote in Appendix B (L1296-1301) likewise joins D11 L114 (para 33 "At the very least, LFCs should be explicitly required to pay for ONT relocations") and D12 L100 (para 29 "Chorus benefits from copper withdrawal").
- Paragraph pinpoints checked against the in-bundle originals: D11 has paras 12 (L31), 13 (L33), 21 (L63), 24 (L92), 30 (L108), 33 (L114), 34 (L117), 35 (L120), 41-45 (L147-156); D12 has 26 (L90), 27-29 (L95-100), 30-32 (L104-107); D09 has 7 (L24), 13 (L35), 14 (L38), 15 (L43), 16 (L46); D13 has 5 (L19), 7 (L21), 8-10 (L24-28), 11-14 (L30-42), 16-17 (L46-52), 20 (L59), 21 (L62), 22 (L71). D01 fn 40 cites Spark Feedback "para 35"; D06 L1010 cites the same letter as "paras 35-39".

Draft decision vs final decision (D01 vs D06; locations only):
- Replacement: D01 L369 "instead require providers to replace the appropriate means when the device no longer meets the minimum requirements under the Code." vs D06 L310 "Remove the requirement to replace appropriate means at least every 36 months and substitute it with the requirement for the provider to test appropriate means at least every 36 months." and D06 L869 "169.2 amend the Code to require providers to test the appropriate means at least once every 36 months". D05 L355 "31.5 tested at least once every 36 months; and".
- Number of changes: D01 table IDs 1-7 (L214-234) vs D06 final-decision table running to ID 11 (D06 L344 "11 Disclosure of accepted applications"); D06 L1040 "We note that this change wasn’t in our Draft Decisions and Reasons paper."
- Medical alarms: D01 chapter 6 (no amendment, L546-567) vs D06 L284 "State that ‘medical and other safety alarms’, as defined in the Code are a valid means of contacting the 111 emergency service."
- Facilities: D01 L480 preliminary view / L487 no amendment vs D06 L464 "It was our preliminary view that the party who holds the direct billing relationship with the consumer (ie, the Facility in scenarios A and B) is subject to the Previous Code" and D06 L270-274 "State that the Code does not apply to" / "“health care services”" ... "Clarify that the Code does apply to" / "Retirement Villages where they provide telecommunications services." Scenario text repeated at D06 L459-463; D04 L41 and D10 L45 restate "direct billing relationship".
- Provisioning-time disclosure: D01 L466 = D06 L1021 "with a brief reason for any provisioning that took longer than 10 working days." ; D05 L411 ; D08 L443 ; D03 L47.
- Minimum period: D01 L780 "we do not believe the minimum period should be amended." ; D06 L1143 "We proposed no amendments to this definition in our Draft Decisions and Reasons paper." ; D05 L168 "minimum period means a continuous eight-hour period" ; D08 L154 "minimum period means a continuous eight-hour period when used as recommended;" (TCF mark-up).
- Clause 18 ten-day rule: D01 L448 "within 10 working days" ; D08 L331 "18. Within ten working days of receiving a complete consumer’s application" ; D05 L314 "22. Within ten working days of receiving a complete consumer’s application".
- Business landline attribution: D01 L249-260 (2degrees suggested clarification; Commission agrees with WISPANZ on exclusion) vs D06 L364 "2degrees and Wireless Internet Service Providers Association New Zealand (WISPANZ) suggested that the Code should only apply to residential services".
- Figure 1 caption: D01 L857 "Figure 1: Subset of consumers entitled to receive appropriate means" vs D06 L160 "Figure 1: Subset of consumers entitled to be considered vulnerable" (same lead-in sentence at D01 L855 / D06 L158; no diagram content in either text).

Other documents restating D01's table:
- D03 (Age Concern) L32-49 lists the chapter 4 draft decisions in its own numbering: its items 1-5 match D01 IDs 1-5 (D03 L43 "4. Removing the requirement to replace appropriate means every 36 months"), its item 6 is D01 ID 7 (D03 L47), and its item 7 is D01 ID 6 - D03 L49 "7. Clause 37: Age Concern New Zealand does not support the proposed amendment".
- D04 (Bupa) L13 "The focus of chapter 5 of the Commission's Draft Decisions and Reasons Paper".

Statute and Request for Views numbering:
- 30 working days: D01 L191, L1057 ; D02 L92 "within 30 working days after we gave public notice of the draft amendments to the Code" ; D06 L1231.
- NZ Police's Appendix B reference (D01 L1386 "per foot note 7 for paragraph 19.2") corresponds to D02 L88 "19.2 consulting with interested persons7 on the proposed amendments to the Code;".
- D01 fn 4 "Request for Views Paper, May 2023, paragraphs 13 to 15." corresponds to D02 L76-79 (paras 13-15).
- Cyclone Gabrielle: D01 L1280 and L1284 (BTG and Anonymous quotes) ; D02 L66 "Recent weather events, such as Cyclone Gabrielle".
