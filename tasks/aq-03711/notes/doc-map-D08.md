# aq-03711 - document map for D08 only (platform "Doc 12")

Navigation only: where things are, not what to ask. Questions quote the documents, never this map.
Line numbers are `text/D08.txt` lines (the `docs/` original is the same text shifted by -2 lines, because
`text/` adds a 2-line header). Quotes are verbatim, including the source's typos and run-together words.
"D05 Lnnn" = `text/D05.txt` (final Code, 26 June 2024, platform "Doc 14"); "D06" = final Decisions and Reasons
paper; "D01" = Draft Decisions and Reasons paper.

## 0. Binding, coverage ledger

- Source: `docs/nzcc_contact_code_111_nz_telecommunications_forum_inc_submission_on_dr.txt`
- sha256 (manifest and intake agree): `3a4b224e25e829e7ddeb61c1323ec86dd644dfd29143cc759f0c7ccb11a0f395`; 62,598 chars; 711 lines; `incomplete: false`, `gap_characters: 0`.
- Reuse: `notes/doc-map.md` was still the blank template, so nothing was reused.
- D08 read ledger (sequential, all readable text): L1-150, L150-299, L299-448, L448-647, L647-711. Remaining: none. **Coverage: full.**
- Other files read for comparison only (not mapped): D05 L1-459 (whole file); D06 L1-32, L176-205, L262-350, L355-450, L598-667, L676-1030, L1128-1176; D01 L1-30, L106-121, L196-479; D03 L16-51; D13 L1-30. Everything else in those files is unread by this mapper.
- Whole-bundle greps run (all `text/D*.txt`): `36 months|three years|3 years`; `3 months|three months|six months|grace period|1 July 2024|1 January 2025`; `used as recommended|used as instructed`; `10 working days|ten working days|five working days|30 November|10 February 2021|12 months|once a year|5 years`; `eight-hour|8-hour|8 hour(s)`; commissioner names, ISBNs, project number, `0800 943 600`; `ONT|fridge|multiple devices|RSP|FWA`; `clause N|Section X` in the short documents.
- Extraction spot-checks against `docs/` original: page count not-applicable (plain text, no page markers); one table (Code history, docs L9-12 = text L11-14) identical; one comment block ("Commented :" count 14 in both; docs L171 = text L173) identical; no footnotes in D08 (not-applicable).
- Unresolved (cannot be inspected): the original Word/PDF mark-up. The supplied source is already flattened text, so colour/strike-through that would show which run-together words are insertions and which are deletions, and which mark-up is the Commission's and which is the TCF's, is not visible. Where this map says "inserted" or "deleted" it gives the document that supports it; otherwise it says unresolved.

## 1. What D08 is

- **It is not a letter or a table of comments.** It is the Commerce Commission's own published "[Draft] Commission 111 Contact Amended Code" (the draft amending instrument plus Appendices A-C, i.e. the whole 2020 Code with the Commission's tracked changes), onto which the TCF has added its own tracked edits and 14 margin comments. There is no cover letter, no author line, no TCF letterhead, no signature and no submission date anywhere in D08.
- Printed header, L3-L9: `3950406.1` / `ISBN 978-1-991085-62-7` / `Project no. PRJ0046469` / `Public Version` / L7 `[Draft] Commission 111 Contact Amended Code 2023 The Commission: Tristan Gilbertson` / L8 `Dr John Small Nathan Strong Loretta Lovell` / L9 `Date of publication: 18 December 2023`.
- The only date D08 prints for itself is the Commission's publication date, 18 December 2023 (L9, L14). The TCF's submission date is **not in D08**; D06 supplies it: `TCF “Submission on draft amended 111 Code tracked changes” (1 March 2024) pages 12 & 14.` (D06 L408; same title/date at D06 L197, L199, L201, L614, L633, L727, L728, L769, L866, L909, L972). D08 has no page numbers, so D06's page references (12, 13, 14, 16, 21, 22, 23) cannot be matched to D08 lines except by content.
- TCF named inside D08 only twice, both inside comments: L248 `The TCF does not see this adds any value` and L395 `The TCF proposes flexibility`. Elsewhere the comments say "we" / `our members` (L174, L390). The issuer of the underlying text is the Commission; the TCF is the commenter/submitter.
- D06 identifies a **second, separate** TCF document of the same date that is not D08: `TCF “Submission on draft amended 111 Code and draft decisions and reasons paper” (1 March 2024) page 2.` (D06 L203, L482, L1100). No file in `text/manifest.json` corresponds to it (the only other TCF file is D13, the June 2023 Request-for-Views submission). D06 L182: `Some of the TCF’s members did not provide their own individual submissions as the TCF’s submission represents views of its members on the amendments to the Previous Code.`
- Structure, in order:
  - L3-L9 cover; L11-L14 "Code history" table; L16-L18 "Drafting notes".
  - L20-L37 the amending instrument: `I. Title` (cl. 1-2), `II. Amended Code` (cl. 3, 3.1-3.3, 4), `III. Commencement and application` (cl. 5). These five clauses are numbered separately from the Code's own clauses 1-50.
  - L39-L64 `APPENDIX A` Associated documents (replaces the Code's associated-documents page).
  - L66-L86 `APPENDIX B` Contents (replaces the Code's table of contents).
  - L88-L488 `APPENDIX C`: Introduction (L89-L97) and Code sections A-M, clauses 1-50 in the draft's new numbering.
  - L490-L709 `ATTACHMENT A – APPLICATION FORM TO BE CONSIDERED A VULNERABLE CONSUMER` (the 2020 template form, Parts A-E, Guidance Notes 1-3, General Guidance).
  - L711 `-----` end marker.

## 2. How the extraction shows insertions, deletions and comments

- L18 `Amendments to the Code are marked as tracked changes.` and L35 `4. The deletions, substitutions, and additions are all marked as tracked changes.` In the text, **no mark-up survives**: deleted and inserted words are printed one after the other with no marker and often no space.
- Comments: each starts with the literal string `Commented : ` (author initials are blank). 14 blocks, at L173, L197, L201, L218 (mid-line, after clause 7.1), L246, L247, L252, L253, L285, L389, L393, L397, L422, L441 (mid-line, after clause 40.4). Comments are **displaced** from the text they annotate (e.g. the comment on the "minimum period" definition at L154 is printed at L173 after "protection order"); anchors below are by content and by D06's descriptions.
- Catalogue of run-together strings (every one seen):
  - `retailresidential` (old "retail" + new "residential"): L92, L94, L134, L137, L139, L146, L170, L177, L209, L228, L231, L233, L288, L335, L371, L375, L433, L441, L454 (19 lines, one occurrence each). With a space: L105 `retail residential landline services`, L179 `retail residential landline service means`. Printed with "residential" alone: L236 `purchase a residential service`, L255 `a consumer of a residential landline service` (and inside TCF comments at L198, L252). Printed with "retail" alone (inside a deleted sub-clause): L424 `where the retail landline service was supplied`. Support that retail->residential is the Commission's draft change: D01 L270 `48.2 the definitions of retail landline services (from retail landline services to residential landline services) and premises are amended`.
  - `comescame` L100; `comes came` twice on L102 (direction unresolved; D05 L102/L104 print "comes").
  - `Hhas` L134.
  - `sectionclause 232` L150 (D05 L160 prints `section 232`).
  - `from time to timeand is available from the Electricity Authority’s website here:` L160 (see section 6).
  - `occupation residence` L169 (D06 L415 `the definition of premises (used or intended for residence, as opposed to occupation) is amended`).
  - Old+new clause numbers fused: `6.56.6`, `6.66.7` (L209), `6.76.8` (L211), `6.86.9` (L212), `6.8.16.9.1`, `6.8.26.9.2`, `6.8.36.9.3` (L214); `(c)(d)`, `(d)(e)` (L185-L186); `36.335.4` (L361); `3536` (L375, L414, L430, L451, L457); `31.32.` (L409), `32.33.` (L410), `33.34.` (L413), `34.35.` (L414), `35.36.`, `35.136.1` (L418-L420), `35.336.2`, `35.436.3` (L426-L427), `36.38.` (L430), `37.39.` (L433), `38.40.` ... `38.740.7` (L436-L443), `39.41.`, `4042`, `39.141.1`, `39.241.2`, `3334`, `39.341.3`, `39.441.4` (L447-L451), `40.42.`, `3941`, `40.142.1` etc. (L453-L457), `41.43.` to `48.50.` (L459-L486), `4143` (L461), `3638` (L478), `4648` (L484).
  - `onat the Commission’s websiteAttachment A` L283 (D01 L339/L346: template removed from Attachment A and guidance note changed to refer to the website).
  - `this Section Gat least once every 36 months` L382 (see clause 29.3).
  - `notifies a provider that they have moved moves premises` L428 (TCF insertion + original word; comment L441).
  - `10 working days.the average number of working days` L443 (new 40.7 text + deleted old 38.7 text; D01 L465-L466).
  - Appendix B page numbers fused: see section 4, table T4.
- Numbering collision as printed: a TCF-proposed clause numbered `32.` (L405) is followed by the Commission's renumbered `31.32.` (L409), so two clauses carry "32" in D08.
- Typos carried in the source (useful for grepping): L162 `retail er-obligations`; L201 `that that`; L220 `on the customer's website`; L224 `reject the the`; L248 `adhere too`; L262 `Telecommunication Act 2001`; L348 `uninterruptable` (defined term L190 is `uninterruptible`); L462 `of one those parties`; L503 `Instructions for completing from`.

## 3. Numbers ledger (every number in D08)

**Negative finding: D08 contains no counts of vulnerable consumers, registrations, applications, customers or providers, no costs, no dollar amounts and no percentages.** Grep of D08 for `%`, `$`, `per cent`, `percent`, `million`, `thousand` and comma-grouped digits returns nothing. No figure is tied to a named year as a count; every year in D08 is part of a date, an ISBN/reference or a statute title. All four-digit years that appear: 1993, 2001, 2003, 2018, 2019, 2020, 2021, 2023, 2024 (there is no "2022").

| Line | Figure | Unit / what it is | Quote |
|---|---|---|---|
| L3 | 3950406.1 | document reference | `3950406.1` |
| L4, L14 | ISBN 978-1-991085-62-7 | this draft's ISBN | `ISBN 978-1-991085-62-7` |
| L5 | PRJ0046469 | project number | `Project no. PRJ0046469` |
| L7, L14, L18 | 2023 / [2024] | title year, printed three ways | L7 `Amended Code 2023`; L14 `Commission 111 Contact Amended Code [2024]`; L18 `This [Draft] Commission 111 Contact Amended Code [2024] amends` |
| L9 | 18 December 2023 | publication date of the draft | `Date of publication: 18 December 2023` |
| L13 | 17 November 2020 | publication of the principal Code, ISBN 978-1-869458-52-2 | `17 November 2020 ISBN 978-1-869458-52-2 Commission 111 Contact Code` |
| L37 | 3 months | proposed commencement lag after publication of the Amended Code | `5. This Amended Code comes into force on a date that is 3 months following the publication of the Amended Code.` |
| L42-L62 | nine dated rows | Associated documents (table T2) | see section 4 |
| L68-L86 | fused page numbers | Appendix B contents (table T4) | see section 4 |
| L102 | 1 August 2021 | Section G in force | `1.1 Section G comes came into force on 1 August 2021; and 1.2 the rest of this Code comes came into force on 1 February 2021.` |
| L102 | 1 February 2021 | rest of the Code in force | same line |
| L103-L488 | Act sections | statutory references: 238(2) L103; 238(3)(a) L106; 238(1) L109; 232 L134, L150; 5 L156; 238(3)(b) L243; 238(5) L262; 238(3)(c) and 4)(b) L362; 238(3)(d) L407; 238(4)(c) L411, L416, L432, L435, L445; 241-245 L464-L465, L481, L699; 242(2) and (3) L473; 240(1)(a) L481; Part 7 L483; 236(1)-(4) L484; 239(5)-(7) L488 | e.g. L484 `section 236(1)-(4) of the Act` |
| L119-L128 | 1993; 2019 | Companies Act 1993; Partnership Law Act 2019 | `Act 1993;` / `Partnership Law Act 2019;` |
| L146, L171 | section 9; section 79; 2018 | Family Violence Act 2018 | `section 9 of the Family Violence Act 2018` / `section 79 of the Family Violence Act 2018;` |
| L148 | 12 months; 1 July; 30 June | disclosure year | `disclosure year means a period of 12 months beginning on 1 July in any year and ending on 30 June in the following year;` |
| L148 | 2003 | Health Practitioners Competence Assurance Act 2003 | same line |
| L154 | eight-hour | minimum period | `minimum period means a continuous eight-hour period when used as recommended;` |
| L164 | 1.1; 1.3; 1 July 2019 | Web Accessibility Standard 1.1, Web Usability Standard 1.3, effective date | `effective from 1 July 2019` |
| L173, L389 | 8 hours | TCF comment restating the minimum period | `(i.e. 8 hours)` |
| L173, L389 | a single home phone | hardware the battery must support (ONT, modem, one phone) | `i.e. ONT, modem and a single home phone.` |
| L175, L391 | 8 hour | TCF comment | `111 calling for the continuous 8 hour period.` |
| L229 | 10 February 2021 | first deadline to give information to all customers | `10 February 2021 and at least once every 12 months thereafter.` |
| L229 | 12 months | repeat-information interval | same |
| L331 | ten working days | deadline to accept/decline a complete application | `18. Within ten working days of receiving a complete consumer’s application` |
| L382 | 36 months (twice) | replacement interval (deleted text + TCF sentence) | see clause 29.3 |
| L393 | 8 hours; 3 years | TCF comment on status quo | `as long as the battery lasted for 8 hours when we gave it to the customer` ... `as long as it is replaced in 3 years).` |
| L395 | 3 years (twice) | TCF proposal | `the device must be replaced every 3 years but that an RSP can additionally choose to leave the device in place longer than 3 years` |
| L409 | one | means per premises at any one time | `one means for contacting the 111 emergency service per premises.` |
| L413, L414 | once a year | monitoring contact (must) / circumstances enquiry (may) | `A provider must, at least once a year,` / `A provider may, at least once a year,` |
| L436 | 30 November | annual disclosure deadline | `No later than 30 November of each disclosure year` |
| L443 | 10 working days | threshold above which reasons for provisioning time are required | `with brief reasons for any provisioning that took longer than 10 working days.` |
| L454, L456, L457 | 5 years (three times) | record-retention periods | `a period of 5 years or more has passed` |
| L463 | five working days | when a disagreement becomes a dispute | `that disagreement is not resolved within five working days.` |
| L501, L613, L679, L683, L685 | 8-hour | application form wording | L501 `continuous 8-hour period.`; L683 `continuous 8- hour period`; L685 `continuous (ie non-stop) 8-hour period if used as instructed.` |
| L626 | type 2 | Scenario two, diabetes type | `Fatima has type 2 diabetes` |
| L631 | three months | Scenario four, recovery period | `during recovery over the next three months.` |
| L709 | 0800 943 600 | Commission enquiries phone | `0800 943 600` |

Units note: the same replacement interval is "36 months" in the clause text (L382) and "3 years" in the TCF comments (L393, L395); the minimum period is "eight-hour" in the definition (L154), "8 hours"/"8 hour" in comments (L173-L175, L389-L393) and "8-hour" in the form (L501 etc.); the application deadline is "ten working days" in words (L331) while the provisioning threshold is "10 working days" in digits (L443).

## 4. Tables

T1. Code history (L11-L14). Columns: `Publication date Reference Title`. Two rows:
- `17 November 2020 ISBN 978-1-869458-52-2 Commission 111 Contact Code`
- `18 December 2023 ISBN 978-1-991085-62-7 Commission 111 Contact Amended Code [2024]`

T2. APPENDIX A - Associated documents (L40-L64). Columns: `Publication date Reference Title`. Nine rows, no totals, no units:
1. `12 September 2019 ISBN 978-1-869457-55-6 Commission 111 Contact Code Emerging Views Paper`
2. `11 March 2020 ISBN 978-1-869458-02-7` - `Commission 111 Contact Code: Draft Decisions and Reasons Paper`
3. `11 March 2020 ISBN 978-1-869458-01-0 Draft Commission 111 Contact Code`
4. `11 March 2020 2020-au1101` - `New Zealand Gazette Notices “Notification of Commerce Commission’s Draft 111 Contact Code”`
5. `17 November 2020 ISBN 978-1-869458-53-9` - `Commission 111 Contact Code: Decisions and Reasons Paper`
6. `17 November 2020 2020-au5242` - `New Zealand Gazette Notices “Notification of Commerce Commission’s 111 Contact Code”`
7. `17 November 2020 ISBN 978-1-869458-52-2 Commission 111 Contact Code`
8. `18 May 2023 ISBN 978-1-991085-00-9` - `111 Contact Code Review - Request for views on the effectiveness of the 111 Contact Code in meeting the requirements in the Act`
9. `18 December 2023 ISBN 978-1-991085-63-4` - `111 Contact Code Review – Draft decisions and Reasons`
- Footer L63-L64 `Commerce Commission` / `Wellington, New Zealand`.
- Compare D05 L25-L64: the same nine rows plus five more (14 rows): `18 December 2023 978-1-991085-62-7` `Draft Commission 111 Contact Amended Code` `2024` (D05 L48-L50); `18 December 2023 2023-au5823` Gazette notice of draft amendments (D05 L51-L53); `26 June 2024 ISBN 978-1-991287-45-8` Decisions and Reasons paper (D05 L55-L56); `26 June 2024 ISBN 978-1-991287-43-4` `Commission 111 Contact Code (Amendment Version 2024)` (D05 L57-L59); `26 June 2024 2024-au2994` Gazette notice (D05 L61-L64). D08's own list does not include D08's own ISBN row.

T3. Amending instrument contents (L21-L24): `I. Title`, `II. Amended Code`, `III. Commencement and application`.

T4. APPENDIX B - Contents (L67-L86). Heading followed by fused page numbers (several superseded page numbers run together; which digits are current is unresolved):

| Line | Entry | Printed number string |
|---|---|---|
| L68 | INTRODUCTION TO THE COMMISSION 111 CONTACT CODE | 8884 |
| L69 | A. COMMENCEMENT DATE | 9995 |
| L70 | B. APPLICATION | 9995 |
| L71 | C. PURPOSE | 9995 |
| L72 | D. DEFINED TERMS | 9995 |
| L73-L74 | E. REQUIREMENT ON PROVIDERS TO INFORM ALL CONSUMERS ABOUT OPTIONS AVAILABLE FOR VULNERABLE CONSUMERS | 1212128 |
| L75-L76 | F. PROCESS FOR A CONSUMER TO DEMONSTRATE THEY ARE A VULNERABLE CONSUMER | 14141410 |
| L77-L78 | G. REQUIREMENT ON PROVIDERS TO PROVIDE VULNERABLE CONSUMERS WITH AN APPROPRIATE MEANS FOR CONTACTING 111 | 19191915 |
| L79-L80 | H. CIRCUMSTANCES WHERE A CONSUMER MAY NO LONGER BE CONSIDERED VULNERABLE | 21212117 |
| L81 | I. REQUIREMENT ON PROVIDERS TO NOT WITHDRAW SERVICE | 22222217 |
| L82 | J. REQUIREMENT ON PROVIDERS TO DISCLOSE INFORMATION | 22222217 |
| L83 | K. REQUIREMENT ON PROVIDERS TO KEEP RECORDS | 23232318 |
| L84 | L. DISPUTE RESOLUTION | 24242419 |
| L85 | M. AMENDMENT OR REVOCATION OF THE CODE | 25252520 |
| L86 | ATTACHMENT A – APPLICATION FORM TO BE CONSIDERED A VULNERABLE CONSUMER | 26262621 |

- 13 lettered sections A-M plus Introduction and Attachment A. D05 contents (L67-L86) has 14 lettered sections A-N, page numbers 5-21, and **no Attachment A**. Section letter map draft -> final: A->A, B->B, (new) -> C `GRACE PERIOD FOR COMPLYING WITH AMENDMENTS TO THE CODE`, C->D, D->E, E->F (final title adds `OF RESIDENTIAL LANDLINE SERVICES`), F->G, G->H, H->I, I->J, J->K, K->L, L->M, M->N.

T5. Application form (L490-L709) contains tick-box grids, not data tables; see section 9.

## 5. Clause by clause: D08 draft text, TCF change/comment, final Code (D05)

Clause number map, D08 (new draft numbers) -> D05: 1->1; 2->2; [D05 new 3, 4 = grace period]; 3->5; 4->6; 5->7; 6->8; 7->9; [D05 new 10]; 8->11 (only 8.2 survives); 9->12; 10->13; 11->14; 12->15; 13->16; [D05 new 17]; 14->18; 15->19; 16->20; 17->21; 18->22; 19->23; 20->24; 21->25; 22->26; 23->27; 24->28; 25->29; 26->30; 27->31; 28->32; 29->33; 30->34; 31->35; TCF's `32.` (L405)->36; `31.32.`->37; `32.33.`->38; `33.34.`->39; `34.35.`->40; `35.36.`->41; `37.`->42; `36.38.`->43; `37.39.`->44; `38.40.`->45; `39.41.`->46; `40.42.`->47; `41.43.`->48; `42.44.`->49; `43.45.`->50; `44.46.`->51; `45.47.`->52; `46.48.`->53; `47.49.`->54; `48.50.`->55. D08 draft Code ends at clause 50; D05 ends at clause 55.

### Amending instrument (L26-L37) - no counterpart text in D05
- cl. 1 L27 `1. This is the [Draft] Commission 111 Contact Amended Code (Amended Code).`
- cl. 2 L28 amends `Commission 111 Contact Code ISBN 978-1-869458- 52-2 (Code).`
- cl. 3 L31-L34: Appendix A replaces associated documents page; Appendix B replaces contents page; Appendix C replaces `(i) introduction to the Code and (ii) body of the Code.`
- cl. 5 L37: **commencement 3 months after publication.** No TCF comment on it.
- Final: D05 is the consolidated Code, not the amending instrument. D05 L13 `Date of publication: 26 June 2024`; D05 L20 `made by the Commission 111 Contact Code (Amendment Version 2024) which comes into force on 1 July 2024.` D05 L110 `3. There is a grace period starting on 1 July 2024 and ending on 1 January 2025`; D05 L112 `4. During the grace period providers will be considered to have complied with these requirements of the Code if they complied with the Code as it was prior to the amendments.` D06 L106 `a six-month grace period starting on 1 July 2024 and ending on 1 January 2025.`; D06 L1171 `an enforcement grace period of six (6) months`. D08 has no grace period. The final amending instrument itself (ISBN 978-1-991287-43-4) is not a file in this bundle. "3 months" as a commencement lag is restated in one other document, D04 L92 (Bupa para 21: "will come into force 3 months following publication"); it is not in D01, D05 or D06 (caller correction, 2026-10-12).
- Cover: D08 L7-L8 Commission members `Tristan Gilbertson` / `Dr John Small Nathan Strong Loretta Lovell`; D05 L9-L12 `Tristan Gilbertson` / `Pierre van Heerden` / `Nathan Strong` / `Loretta Lovell` (same four at D06 L8-L11). "John Small" appears only in D08.

### Introduction (L89-L97)
- L89 `As consumers transition away from using traditional copper voice services` -> D05 L90 `As consumers of residential landline services transition away`.
- L92 `providers of retailresidential landline services` -> D05 L94 `providers of residential landline services`.
- L94 `The Code primarily affects current and future vulnerable consumers of retailresidential landline services, and their retail providers.` -> sentence absent from D05 introduction (D05 L89-L98).
- L97 URL `.../telecommunications/projects/commission111-contact-code.` -> D05 L98 `.../telecommunications/telecommunications-forconsumers/commission-111-contact-code.`

### A. Commencement date - clause 1 (L99-L103)
- L100 `1. This Code comescame into force as follows:`; L102 `1.1 Section G comes came into force on 1 August 2021; and 1.2 the rest of this Code comes came into force on 1 February 2021.`
- D05 L102-L104: `1. This Code comes into force as follows:` / `1.1 Section H comes into force on 1 August 2021; and 1.2 the rest of this Code comes into force on 1 February 2021.` Differences: section letter G -> H; D05 prints "comes" only. No TCF comment.

### B. Application - clause 2 (L104-L106)
- L105 `2. This Code applies to retail residential landline services.` -> D05 L107 `2. This Code applies to residential landline services.` Reference line L106 `section 238(3)(a).` = D05 L108.

### [D05 only] C. Grace period - D05 clauses 3-4 (D05 L109-L112). No counterpart in D08.

### C. Purpose - clause 3 (L107-L109) -> D05 clause 5 (D05 L114). Wording identical.

### D. Defined terms - clause 4 (L110-L190) -> D05 clause 6 (D05 L117-L204). See section 6 for every term.

### E. Inform consumers - clauses 5-8 (L191-L243) -> D05 section F, clauses 7-11 (D05 L207-L242)
- Heading L191 `E. Requirement on providers to inform all consumers about options available for vulnerable consumers` -> D05 L207 `F. Requirement on providers to inform all consumers of residential landline services about options available for vulnerable consumers`.
- cl. 5 L192: `to contact, either directly or through a third party provider, the 111 emergency service in the event of a power failure at the customer’s premises.` The words `either directly or through a third party provider` are a TCF proposal (comment L201). D05 L208 cl. 7: `A provider must provide information to consumers of residential landline services on the options available for consumers, including vulnerable consumers, to contact the 111 emergency service in the event of a power failure at the customer’s premises.` (TCF words not in the clause; "of residential landline services" added; the idea is carried instead in the D05 definition of "111 emergency service", D05 L119).
- cl. 6 L194-L214: nine items 6.1-6.9 as renumbered. 6.1 technologies (`including fibre and fixed wireless`); 6.2 devices (`including cordless phones and medical alarms if they do not have an inbuilt battery`); 6.3 alternative means; 6.4 who is a vulnerable consumer and the process; 6.5 supply at no cost for the minimum period; `6.56.6 the implications to vulnerable consumers if they reject the appropriate means supplied by the provider (given the consequences set out in clause 31);` (L209); `6.66.7` cannot deny or cease supply; `6.76.8` how to contact the provider; `6.86.9` how to complain, with `6.8.16.9.1`, `6.8.26.9.2`, `6.8.36.9.3`.
  - The "implications" item is the Commission's draft addition: D01 L226 `Clauses 6.6 & 31`; D01 L382 `74.2 amend the Code to require providers to make vulnerable consumers aware of the implications of rejecting the appropriate means.`; D06 L906 `(in clause 6.6 of the Draft Amended Code)`. Whether `(given the consequences set out in clause 31)` is Commission or TCF wording is unresolved.
  - TCF comment L218-L224 (quoted in section 8, R4).
  - D05 cl. 8 L209-L227 has **eight** items 8.1-8.8: the "implications" item is gone; 8.6 = cannot deny or cease supply; 8.7 = contact; 8.8 (8.8.1-8.8.3) = complaints. The topic moved to new D05 cl. 17 (D05 L262-L264).
- cl. 7 L216-L236 (four ways 7.1-7.4):
  - 7.1 L218 website, `consistent with the NZ Government Web Standards;` = D05 9.1 L229.
  - 7.2 L226 `made easily accessible to all consumers at the point of sale` -> D05 9.2 L231 `made easily accessible to all customers at the point of sale` (**consumers -> customers**).
  - 7.3 L228-L229 `provided to all customers of a retailresidential landline service no later than` / `10 February 2021 and at least once every 12 months thereafter.` -> D05 9.3 L233 `provided to all customers of a residential landline service at least once every 12 months.` (date and "thereafter" removed; D06 L760 para 142 gives the reason).
  - 7.3.1 L230 preferred method `(eg, email, phone call)`; 7.3.2 L231 `if the provider does not know the customer’s preferred method of contact, in writing in an easily discernible manner;` = D05 9.3.1/9.3.2 L234. TCF comment L246 `We proposed that this wording is removed for operational simplicity`; D06 L752 para 138 says the wording targeted is `“if the provider does not know the customer’s preferred method of contact”`; the words still print in D08 and are kept in D05.
  - 7.4 L231-L234: 7.4.1 first contracts; 7.4.2 L234 `the customer switches between telecommunications technologies or services with the provider (including any switch that means the telecommunications technology or service will not work in a power failure)` -> D05 9.4.2 L238 `the customer switches to a different residential landline service or technology with the same provider that may not work in a power failure.`
  - Tail L236 `such that the customer is not able to purchase a residential service or switch between telecommunications technologies or services without being aware of such information.` (Commission's draft addition: D01 L219-L220 `Clause 7.4`). TCF comment L247-L250 calls it unnecessary. -> D05 new **cl. 10** L239 `10. For the purposes of clause 9, the information must be provided so that a customer is not able to purchase a residential landline service or switch between residential landline services or technologies without being made aware of such information.`
- cl. 8 L238-L242:
  - 8.1 L240 `clauses 6.1, 6.2 and 6.3, notwithstanding anything else in this Code, this information must also be provided to a person when they first contract with a provider for the supply of a naked broadband service or a copper landline service; and` (`or a copper landline service` = TCF addition, comment L252). -> **removed entirely** from D05 (D06 L418 `51.6 clause 8.1 of the Previous Code is removed.`).
  - 8.2 L241 `clause 6.4, the information must note the existence and purpose of the written application form referred to in clause 13.3, and ensure the form is readily available to consumers; and` -> D05 cl. 11 L240 `11. For the purposes of clause 8.4, the information must note the existence and purpose of the written application form referred to in clause 16.3, and ensure the form is readily available to consumers.`
  - 8.3 L242 `clauses 7.3, 7.4 and 8.1, the requirement to provide information will be met where a provider provides a link to the required information and adequately describes what information is available at the link.` (TCF addition, comment L253). -> not in D05.
- Reference L243 `sections 238(3)(b).` = D05 L242.

### F. Process to demonstrate vulnerability - clauses 9-24 (L244-L362) -> D05 section G, clauses 12-28 (D05 L243-L343)
- cl. 9 L255-L257 -> D05 cl. 12 L244-L245: identical wording (9.1/9.2 -> 12.1/12.2).
- cl. 10 L258-L259 -> D05 cl. 13 L248: identical except `clause 9.1` -> `clause 12.1`.
- Unnumbered paragraph L261 `For the purpose of clause 9.2, a ‘means for contacting 111 emergency service’ includes managed medical devices which can be used to contact 111 emergency service either directly or via a third party service.` TCF proposal (comment L285-L286). -> not in D05 cl. 13; D05 instead adds the defined term `managed medical or safety alarm` (D05 L162-L166) and cl. 25.4 (D05 L330).
- cl. 11 L264 -> D05 cl. 14 L251 identical. cl. 12 L266 `clauses 13 to 24` -> D05 cl. 15 L253 `clauses 16 to 28`.
- cl. 13 L269-L273 (13.1-13.3; 13.3 refers to `clause 14`) -> D05 cl. 16 L256-L260 (16.3 refers to `clause 18`).
- [D05 only] cl. 17 D05 L262-L264: `17. The provider must make clear in the written application form that if a vulnerable consumer, or someone on their behalf, were to reject the appropriate means supplied by the provider which complies with the requirements set out in section H of this Code then:` `17.1 their application can be considered withdrawn and no means needs to be supplied by the provider; and` `17.2 the consumer, or someone on their behalf, is able to reapply to demonstrate that they are (or will be) a vulnerable consumer.`
- Guidance note L283 `Guidance note: A template written application form is provided onat the Commission’s websiteAttachment A. The template form requests all the information that is required by clause 14 to be included in a consumer’s application. A provider may choose (but is not obliged) to offer this form (or some adaption that provides the equivalent detail) for the purpose of clause 13.3.` -> D05 L266 `Guidance note: A template written application form is provided on the Commission’s website. A provider may choose (but is not obliged) to offer this form for the purpose of clause 16.3.` (middle sentence and the "(or some adaption ...)" bracket are not in D05).
- cl. 14 L276-L314 (14.1-14.9) -> D05 cl. 18 L269-L296. Same content; only cross-references change (14.8.1 -> 18.8.1). 14.3 categories: health / safety / disability (three). 14.8 either nominated person (14.8.1) or sufficient evidence (14.8.2).
- cl. 15 L315-L317 nominated person examples: 15.1 health practitioner; 15.2 `a police officer, a currently registered social worker, a lawyer (with a current practicing certificate), or a family court judge` -> D05 cl. 19 L297-L299 identical (refs 14.x -> 18.x).
- cl. 16 L319-L326 evidence examples, four: 16.1 MDC form `which includes a certification from a District Health Board (DHB), private hospital or GP;` 16.2 protection order; 16.3 letter from a health practitioner; 16.4 documentation of impairment -> D05 cl. 20 L301-L309 identical.
- cl. 17 L328 -> D05 cl. 21 L311 identical.
- cl. 18 L331-L333 **ten working days** -> D05 cl. 22 L314-L315 identical.
- cl. 19 L334-L343 decline grounds 19.1-19.5 (19.2 has 19.2.1 and 19.2.2; 19.4 `subject to clause 20`) -> D05 cl. 23 L317-L325 identical apart from `retailresidential`/`residential` and cross-references (15->19, 20->24, 14.8.x->18.8.x).
- cl. 20 L344 -> D05 cl. 24 L326 (19.4 -> 23.4).
- cl. 21 L346-L348 `if any of the following circumstances apply:` `21.1 the consumer’s premises receives a copper landline service; 21.2 the consumer has unrestricted access to a mobile phone and that consumer’s premises has adequate mobile phone network coverage; or 21.3 the consumer has an uninterruptable power supply to maintain a means for contacting the 111 emergency service in a power failure.` (three circumstances; no tracked change printed in D08). -> D05 cl. 25 L328-L330 `if the consumer already has a device or technology which meets the requirements under the Code, for example:` 25.1 copper; 25.2 mobile; 25.3 UPS; `or 25.4 the consumer has a managed medical or safety alarm.` (lead-in changed from closed list to examples; fourth item added).
- cl. 22 L350-L355 -> D05 cl. 26 L331-L337 identical. cl. 23 L356-L359 -> D05 cl. 27 L339-L340 identical.
- cl. 24 L361 `If the consumer does not resubmit their application, the provider may regard that consumer as no longer being a vulnerable consumer in accordance with clause 36.335.4.` -> D05 cl. 28 L341 `If the consumer does not re-submit their application, the provider may regard that consumer as no longer being a vulnerable consumer in accordance with clause 41.3.` (also 14.4/14.5 -> 18.4/18.5; "resubmit" -> "re-submit").
- Reference L362 `section 238(3)(c) and 4)(b).` = D05 L343.

### G. Appropriate means - clauses 25-35 (L363-L416) -> D05 section H, clauses 29-39 (D05 L344-L384)
- cl. 25 L365 -> D05 cl. 29 L346 identical. cl. 26 L367 (`clause 25`) -> D05 cl. 30 L348 (`clause 29`).
- cl. 27 L368-L375, five items 27.1-27.5: 27.1 `supplied as soon as reasonably practicable following acceptance of the consumer’s application;` 27.2 at the premises; 27.3 minimum period; 27.4 `supported for the duration of the contract for the retailresidential landline service, including ensuring the means is regularly and appropriately maintained, except where the vulnerable consumer ceases to be a vulnerable consumer in accordance with clause 3536; and 27.5 provided with clear instructions and guidance on how to operate the means and who to contact if there are any issues.`
  - D05 cl. 31 L349-L356 has **six** items: 31.4 `... regularly and appropriately maintained to ensure it remains appropriate and functional, except where the vulnerable consumer ceases to be a vulnerable consumer in accordance with clause 41; 31.5 tested at least once every 36 months; and` / `31.6 provided with clear instructions and guidance ...`. New words `to ensure it remains appropriate and functional`; new item 31.5.
- cl. 28 L376 -> D05 cl. 32 L358 identical (`clause 27.3` -> `clause 31.3`); both say `used and maintained as instructed by the provider.`
- cl. 29 L378-L382, three items:
  - 29.1 L379 `able to operate for the minimum period when equipped with a new fully charged battery and used as recommended;` (`and used as recommended` = TCF addition, comment L389-L391) -> D05 33.1 L362 `able to operate for the minimum period when equipped with a new fully charged battery; and`.
  - 29.2 L381 battery health indicator -> D05 33.2 L363 identical, now the last item.
  - 29.3 L382 `29.3 replaced (or the battery that powers the means is replaced) when it no longer meets the requirements set out in this Section Gat least once every 36 months from the date the last means was installed. If the device performance is unknown it should be replaced at least once every 36 months from the date the last means was installed.` Three layers fused: (i) the Commission's draft insertion `when it no longer meets the requirements set out in this Section G` (D01 L368-L369 paras 69.1-69.2); (ii) the 2020 Code's `at least once every 36 months from the date the last means was installed.` which the Commission's draft deletes (D01 L368); (iii) the TCF's proposed sentence `If the device performance is unknown it should be replaced at least once every 36 months ...` (D06 L853 para 168, L873 para 171). TCF comments L393-L395 and L397.
  - D05: **no 33.3**; cl. 33 has only 33.1 and 33.2 (D05 L360-L363). The 36-month figure survives only in D05 31.5 as a **test**, not a replacement (D05 L355).
- cl. 30 L384-L401 (30.1 with 30.1.1, 30.1.2; 30.2; 30.3; comment blocks L389-L397 interrupt it) -> D05 cl. 34 L365-L371 identical.
- cl. 31 L403 `31. The means provided to the vulnerable consumer is deemed appropriate if such means complies with the requirements set out in this section G, whether the vulnerable consumer accepts it or not.` (Commission's draft addition, D01 L226) -> D05 cl. 35 L373 `35. The means provided to the vulnerable consumer is deemed appropriate if such means complies with the requirements set out in section H, whether the vulnerable consumer (or someone on their behalf) accepts it or not.`
- TCF clause `32.` L405 `32. If the vulnerable consumer does not accept the compliant device then the application should be considered withdrawn.` (comment L422) -> D05 cl. 36 L376 `36. A provider can consider an application to be ‘withdrawn’ if the vulnerable consumer (or someone on their behalf) rejects an appropriate means supplied by such provider which complied with the requirements set out in section H.` ("should be" -> "can consider"; D05 also adds reapplication at 17.2 and reporting at 45.7 / 46.5).
- Reference L407 `sections 238(3)(d).` = D05 L377.
- G2 `31.32.` L409 one means per premises -> D05 cl. 37 L379 (`clause 25` -> `clause 29`). `32.33.` L410 -> D05 cl. 38 L380 identical.
- G3 `33.34.` L413 `A provider must, at least once a year, contact each customer ... to ensure that the means it has provided to the vulnerable consumer remains appropriate and functional.` -> D05 cl. 39 L383 identical.
- `34.35.` L414 `A provider may, at least once a year, contact each customer ... to enquire whether the consumer’s circumstances may have changed in any of the ways described in clause 3536 below.` In D08 this sits in **G3 Requirement to monitor**, before the section H heading (L417). In D05 the same sentence is cl. 40 (D05 L386) and sits **after** the heading `I. Circumstances where a consumer may no longer be considered vulnerable` (D05 L385), so D05's H3 holds only cl. 39.

### H. No longer vulnerable - clauses 36-38 (L417-L432) -> D05 section I, clauses 40-43 (D05 L385-L396)
- `35.36.` L418-L427: `35.136.1` on request; **`35.2 where the consumer no longer resides at the premises where the retail landline service was supplied when the consumer submitted their application to be a vulnerable consumer to the provider;`** (L424, the 2020 sub-clause the Commission's draft deletes: D01 L412 para 81.1); `35.336.2` obtains a means otherwise; `35.436.3` not resubmitted `in accordance with clause 24`. -> D05 cl. 41 L387-L391: three items 41.1-41.3 (41.3 refers to `clause 28`). The "no longer resides" ground is not in D05.
- `37.` L428 `37. If a vulnerable consumer notifies a provider that they have moved moves premises and remains with the same provider, such provider may check the consumer’s status, and may require the vulnerable consumer (or someone on their behalf) to re-apply to demonstrate that they continue to be a vulnerable consumer if something material has changed.` TCF insertion `notifies a provider that they have moved` (comment L441). -> D05 cl. 42 L392 `42. If a vulnerable consumer moves premises and remains with the same provider, such provider may check the consumer’s status, and may require the vulnerable consumer (or someone on their behalf) to re-apply to demonstrate that they continue to be a vulnerable consumer.` **D05 as printed omits `if something material has changed`**; see section 10 (D06 quotes the clause with those words).
- `36.38.` L430 (`clause 3536`) -> D05 cl. 43 L395 (`clause 41`) otherwise identical.

### I. Not withdraw service - `37.39.` (L433) -> D05 section J cl. 44 (D05 L398). Identical apart from "residential".

### J. Disclose information - `38.40.` (L436-L445) -> D05 section K cl. 45 (D05 L402-L411)
- Lead-in identical: `No later than 30 November of each disclosure year ... in respect of the preceding disclosure year:`.
- D08 seven items 40.1-40.7: 40.1 process for clauses 6/7 (`clause 6 in the ways required by clause 7`); 40.2 process for `clauses 13-24`; 40.3 total vulnerable consumers `(as at the last day of the disclosure year)`; 40.4 number of customers; 40.5 applications declined `(in accordance with clause 19)` by ground; 40.6 means supplied by type `(eg the number of mobile phones supplied, the number of battery-backups)`; 40.7 L443 `the provisioning timing to provide appropriate means for each new vulnerable consumer (counting from the date that their application was accepted), with brief reasons for any provisioning that took longer than 10 working days.` followed, fused, by the deleted 2020 text `the average number of working days from the point at which a consumer’s application is submitted to the point at which the vulnerable consumer is provided with appropriate means to contact the 111 emergency service.` No TCF comment on section J (the comment printed mid-line at L441 belongs to clause 37).
- D05 **nine** items 45.1-45.9: 45.1 (`clause 8 ... clause 9`); 45.2 (`clauses 16-28`); 45.3; 45.4; **45.5 `the number of consumer applications accepted by the provider;`** (new); 45.6 declined (`clause 23`, `23.2.1`, `23.2.2`); **45.7 `the number of ‘withdrawn’ applications under clause 36;`** (new); 45.8 means supplied by type; 45.9 provisioning timing, same words as D08's inserted 40.7, `10 working days`.

### K. Keep records - `39.41.`, `40.42.` (L446-L457) -> D05 section L cl. 46-47 (D05 L415-L427)
- D08 four record items: `39.141.1 ... clauses 7.3, 7.4 and 8.1;` `39.241.2 ... clause 3334;` `39.341.3` declined applications and grounds; `39.441.4` consumers who cease to be vulnerable.
- D05 six items: 46.1 `clauses 9.3 and 9.4;` 46.2 `clause 39;` **46.3 `the number of consumer applications accepted by the provider;`** 46.4 declined; **46.5 `the number of ‘withdrawn’ applications under clause 36;`** 46.6 ceased.
- Retention, D08 L454-L457: three limbs each `5 years or more`: after contract termination (42.1); after application declined (42.2); after ceasing to be vulnerable (42.3). D05 L424-L427: same three limbs, each `5 years or more`; 47.2 reads `for the purposes of clauses 46.3, 45.4 and 46.5, if a period of 5 years or more has passed since the point in time when the consumer’s application was accepted, declined, and ‘withdrawn’; or` (prints "45.4" between 46.3 and 46.5, as printed).

### L. Dispute resolution - `41.43.` to `45.47.` (L458-L481) -> D05 section M cl. 48-52 (D05 L429-L451)
- L463 `that disagreement is not resolved within five working days.` = D05 49.2 L436. L464-L465 `sections 241-` / `245 of the Act apply.` = D05 cl. 50 L437.
- `44.46.` four sub-items (L467-L473) = D05 cl. 51. `45.47.` three matters (L474-L479): 47.2 `clause 3638` -> D05 52.2 `clause 43`; 47.3 `clause 26` -> D05 52.3 `clause 30`.
- No TCF comment in this section.

### M. Amendment or revocation - `46.48.` to `48.50.` (L482-L488) -> D05 section N cl. 53-55 (D05 L452-L458)
- `47.49.` L484 `it must apply the procedure set out in section 236(1)-(4) of the Act, with any necessary modifications.` -> D05 cl. 54 L454 `it must apply the procedure set out in section 239(1)-(4) of the Act, with any necessary modifications.` (**236 -> 239**; D06 L8 `Amendments made under section 239 of the Telecommunications Act 2001`).
- Reference L488 `section 239(5)-(7).` = D05 L458.

### Attachment A (L490-L709) -> not in D05 (D05's last text line is L458, the reference under clause 55). See section 9.

## 6. Defined terms in D08 clause 4 (30 terms by this mapper's tally) versus D05 clause 6 (33 terms)

Terms only in D05: `health care services` (D05 L156), `managed medical or safety alarm` (D05 L162-L166), `qualified third party` (D05 L189). No D08 term is missing from D05.

| Term | D08 line and definition (verbatim) | D05 | Match? |
|---|---|---|---|
| 111 emergency service | L112 `includes the ambulance service, police service and fire and emergency service;` | D05 L119 `includes the ambulance service, police service and fire and emergency service, contacted directly by a consumer or via a qualified third party;` | No: words added |
| Act | L114 `means Telecommunications Act 2001;` | D05 L121 | Yes |
| at particular risk of requiring the 111 emergency service | L116 `has the meaning given at clause 10;` | D05 L123 `clause 13` | Number only |
| business landline services | L118-L128 `means a telecommunications service that is primarily marketed and/or provided for businesses purposes, and includes a telecommunications service provided to:` (a) `a company, as defined in the Companies` `Act 1993;` (b) body corporate; (c) corporation sole; (d) sole trader; (e) `a partnership, as defined in the Partnership Law Act 2019;` | D05 L125-L137; (a) `as defined in the Companies Act` `1993, as amended from time to time;` (e) `Partnership Law Act 2019, as amended from time to time;` | No: "as amended from time to time" added twice |
| Code | L130 `means this Commission 111 Contact Code;` | D05 L139 | Yes |
| Commission | L132 | D05 L141 | Yes |
| consumer | L134-L137 `Hhas the same meaning as given in section 232 of the Act, and, in the case of a retailresidential landline service, includes:` (a) the customer; (b) a person who ordinarily resides at the premises | D05 L143-L146 | Yes apart from retail/residential |
| consumer’s application | L139-L142 `... for the purposes of demonstrating that:` `(a) the customer is (or will become) a vulnerable consumer; or` `(b) a person who ordinarily resides at the customer’s premises is (or will become) a vulnerable consumer;` | D05 L146 `... for the purposes of demonstrating that a consumer is (or will become) a vulnerable consumer;` | No: two limbs collapsed into one |
| copper landline service | L144 `means a landline service provided over a copper line using traditional analogue copper voice technology, but excludes any voice service that is provided using technologies (hardware or software) that rely on mains powered electricity at the premises;` | D05 L148 | Yes |
| customer | L146 `means a consumer who has a contract with a provider for the supply of a retailresidential landline service;` | D05 L150 | Yes apart from retail/residential |
| family violence | L146 `section 9 of the Family Violence Act 2018;` | D05 L152 | Yes |
| disclosure year | L148 (12 months, 1 July to 30 June) | D05 L154 | Yes |
| health practitioner | L148 | D05 L158 | Yes |
| industry dispute resolution scheme | L150 `has the same meaning as given in sectionclause 232 of the Act;` | D05 L160 `section 232 of the Act;` | D05 prints "section" |
| landline service | L152 `means a voice service provided over a fixed-line or fixed wireless;` | D05 L160 | Yes |
| minimum period | L154 `means a continuous eight-hour period when used as recommended;` (`when used as recommended` = TCF addition, comment L173) | D05 L168 `minimum period means a continuous eight-hour period;` | No: TCF words not adopted (D06 L1147 para 244) |
| naked broadband services | L156 | D05 L168 | Yes |
| network | L156 `section 5 of the Act` | D05 L168 | Yes |
| nominated person | L156 `in accordance with clause 14.8.1;` | D05 L168 `clause 18.8.1` | Number only |
| Notice of Potential Medically Dependent Consumer (MDC) Status | L156-L162 `means the form provided at Appendix A of the Electricity Authority’s ‘Guidelines on arrangements to assist medically dependent consumers’, as updated from time to timeand is available from the Electricity Authority’s website here:` + URL | D05 L168-L172 `..., as updated from time to time;` (no URL) | No: website sentence and URL not in D05 |
| NZ Government Web Standards | L162-L165 `Means Web Accessibility Standard 1.1 and Web Usability Standard 1.3 (as amended from time to time, and any subsequent Standards that supplement or replace these Standards), issued by the New Zealand Government, effective from 1 July 2019, and, as updated from time to time are available from the Digital.govt.nz website here:` + URL | D05 L174-L175 `... effective from 1 July 2019, and, as updated from time to time;` (no URL) | No: website words and URL not in D05 |
| power failure | L165 `means an interruption in the supply of electricity to a premises;` | D05 L177 | Yes |
| premises | L167-L170 `(a) is used or intended for occupation residence by any person; and` `(b) is receiving a retailresidential landline service;` | D05 L179-L184 `(a) is used or intended for residence by any person; and` / `(b) is receiving a residential landline service;` | "occupation" -> "residence" (Commission's draft change) |
| protection order | L170-L171 | D05 L186-L187 | Yes |
| provider | L177 `means a supplier or suppliers of a retailresidential landline service to a consumer;` | D05 L189 `provider means a supplier of a residential landline service to a consumer and excludes suppliers of health care services;` | No: "or suppliers" gone; health-care exclusion added |
| residential landline service | L179-L186 `retail residential landline service means a landline service provided to a consumer at a premises, and excludes:` (a) mobile services; (b) `naked broadband services; and` (c) `applications that provide voice services over broadband services (such as Skype); and` `(c)(d)copper landline services; and` `(d)(e)business landline services.` | D05 L191-L200 `residential landline service means a retail landline service provided to a consumer at a premises, and excludes:` (a) mobile services; (b) naked broadband services; (c) applications (such as Skype); `(d) business landline services; and` `(e) copper landline services.` | No: D05 definition says "means a **retail** landline service"; order of the last two exclusions is reversed (D08 copper then business; D05 business then copper) |
| telecommunication | L188 | D05 L202 | Yes |
| telecommunications service | L188 | D05 L202 | Yes |
| uninterruptible power supply | L190 | D05 L204 | Yes |
| vulnerable consumer | L190 `has the meaning given in clause 9.` | D05 L204 `clause 12.` | Number only |

- Exclusion list history, located: 2020 Code had three exclusions (D06 L355-L360: `(a) mobile services;` `(b) naked broadband services; and` `(c) applications ... (such as Skype).`); the Commission's draft added business landline services (D01 L268-L270); the TCF's mark-up in D08 added copper landline services (comment L197-L199); D05 has five.
- Terms the TCF comments use but D08 does not define: `Vulnerable Consumer scheme` (L197-L198, L222), `battery pack` (L173), `ONT` (L173), `RSP` (L395, L422), `VC`/`VCs` (L422), `FWA` (L441), `managed medical devices` (L261), `third party provider` (L192), `third party service` (L261), `call handling service` (L286).

## 7. Outside organisations quoted with figures

**None.** D08 quotes no outside organisation's statistics, surveys or figures. Organisations merely named in the Code text (no figures attributed): Electricity Authority (L160, form L664); New Zealand Government / Digital.govt.nz (L164-L165); District Health Board (L321); Telecommunications Dispute Resolution Scheme (L699-L705, with URL `https://www.tdr.org.nz/about-tdr/all-about-tdr`); Commerce Commission contact (L709). The TCF comments cite only `our members` (L174, L390) with no numbers.

## 8. The TCF's own requests (comments and proposed text), kept apart from reproduced Code text

Fourteen `Commented :` blocks. None asks for a delay, a later commencement date, a shorter battery period or any change to the 10-working-day, 30 November or 5-year provisions. Each entry: D08 location and quote; the text change it goes with; what D06 records (D06 location).

- R1 (L173-L175; repeated at L389-L391 as R10). `We propose this additional wording to clarify that the battery pack should be able to operate for the minimum period (i.e. 8 hours) when used as recommended.` ... `i.e. ONT, modem and a single home phone.` ... `our members regularly observe cases where customers plug in multiple devices (e.g. fridges, TVs and other household appliances).` ... `It would be helpful if the Code acknowledged that providers' obligation is to support 111 calling for the minimum period, not provide a battery pack that can support other use cases for the same period`. Text changes: definition L154 `when used as recommended`; clause 29.1 L379 `and used as recommended`. Figures: 8 hours. D06 L1144 para 243 restates it; D06 L1147 `244. We disagree with the TCF regarding the amendment of the definition of minimum period and as such haven’t amended the Previous Code.`
- R2 (L197-L199). `Additional wording proposed because the Code is focused on the Vulnerable` `Consumer scheme which is not available to customers on 'copper landline services' (as those are defined above). So these can be excluded from the definition of a 'residential landline service' and just called out individually in the Code where appropriate (eg section` `8)`. Text change: L185 `(c)(d)copper landline services; and`. D06 L393 para 50; D06 L434 `59. We agree with the TCF that copper landline services should be explicitly excluded from the definition of a residential landline service.` -> D05 L200.
- R3 (L201). `We propose that wording be added to clarify that that 'contact 111 emergency service' does not only mean calling the 111 service, it can also mean access to a 111 emergency service (ambulance, police, fire) via a medical alarm provider`. Text change: clause 5 L192 `either directly or through a third party provider`. D06 L617 para 105; D06 L658 `116. We also agree with the TCF and the RVA that contacting the 111 emergency service can be done via a ‘qualified third party’` -> D05 L119, L189.
- R4 (L218-L224). `While we welcome the clarification in Clause 31, we consider information on the consequences of rejecting an appropriate means is something which can be explained to the customer later in the application form or on the customer's website.` / `Including this new paragraph in 6.6 means it will need to be provided to everyone as part of the information about the Vulnerable Consumer scheme, whereas it will only be relevant for a subset of customers.` / `Instead we propose this information need only be explained to customers in the case where the customer wishes to reject the the appropriate means`. D06 L906 para 182 (with footnote D06 L910 `108 We assume the TCF meant on the ‘provider’s website’.`); D06 L936 `190. We also agree with the TCF’s feedback that not all consumers require information regarding the implications of rejecting an appropriate means.` -> D05 cl. 8 without the item; D05 cl. 17.
- R5 (L246). `Commented : We proposed that this wording is removed for operational simplicity`. Anchor not visible in D08; D06 L752 para 138 identifies the wording as `“if the provider does not know the customer’s preferred method of contact”` (clause 7.3.2, L231). D06 L757 `140. We disagree with the TCF’s suggestion to remove the requirement regarding the provider’s knowledge of the customer’s preferred method of contact.`
- R6 (L247-L250). `The additional clause is unnecessary. Providers should be compliant to the requirements already set out in cl. 7, without having an overly specific additional requirement in the Code.` / `The TCF does not see this adds any value to what is already a very detailed set of requirements that Providers must adhere too.` / `Working with those non-compliant Providers on how best to present this information would be a more useful exercise`. Target: the clause 7.4 tail at L236. D06 L711 para 128; D06 L731 `We also do not agree with the TCF’s suggestion to remove clause 7.4.2.84`; D06 L747 footnote 84 `We clarified the feedback TCF provided in the marked up version of the document and their comment related to clause 7.4.2 of the Previous Code including the proposed additional wording.`
- R7 (L252). `We propose to add ‘or a copper landline service’ here because we have recommended removing it from the defined term of’ residential landline service’ above`. Text change: clause 8.1 L240. D06 L442 `63. ... we disagree with the TCF’s additional proposal to provide a person the required Code information set out in clause 6 when they first contract with a provider for a copper landline service.` (repeated D06 L449 para 66); clause 8.1 removed (D06 L418).
- R8 (L253). `We propose the addition of cl8.3 to the Code to clarify that linking to additional information on the Provider's website is sufficient. 111 Code related information is not relevant for all customers, sharing key information in a prominent way with a link to further information is a good way of ensuring that relevant customers can easily find the information while avoid information overload for the rest.` Text change: clause 8.3 L242. D06 L710 para 127 describes it as about `clauses 5 and 6`; D06 L726-L731 `131. We do not agree with the TCF that providers can necessarily be considered as meeting their obligations by providing a link to Code information and adequately` `describing what information is available at the link.`
- R9 (L285-L286). `Proposed paragraph added to the` `Code to make it clear to readers that if the customer has a medical alarm that can be used to contact 111 emergency services directly, or via a call handling service, they do not meet the definition of a vulnerable consumer under this Code.` Text change: paragraph L261. D06 L607 para 104; D06 L649 `111. We agree with the TCF that adding this wording to the Code would make it clearer to providers and consumers.` -> D05 cl. 25.4 and definition (not the TCF's wording).
- R10 (L389-L391): same text as R1, ending with a full stop (`for the same period.`), printed beside clause 29/30.
- R11 (L393-L395). `The suggested change is helpful, but potentially creates some challenges as now we must know how long batteries are currently lasting (rather than the status quo where as long as the battery lasted for 8 hours when we gave it to the customer then we don't have to take a view on battery life - as long as it is replaced in 3 years).` / `The TCF proposes flexibility e.g., the device must be replaced every 3 years but that an RSP can additionally choose to leave the device in place longer than 3 years if the provider is confident the device is still able to meet the minimum period requirements.` Figures: 8 hours; 3 years (three times). D06 L853 para 168 (restated as `every 36 months if the device’s performance was unknown`); D06 L873 `171. However, we disagree with the TCF’s proposed changes to clause 29.3 of the Previous Code (now clause 33.3 of the Code) to state that if the device performance is unknown, it should be replaced at least once every 36 months.`; D06 L869 para 169.2 test at least once every 36 months -> D05 31.5.
- R12 (L397). `Commented : Proposed wording as we recommend keeping the existing option available`. Goes with clause 29.3 (L382); which words it anchors is not visible.
- R13 (L422). `Proposed addition of a clause to clarify in the Code that if a customer rejects a suitable device then their application should be considered withdrawn or declined. It should not be possible for a customer to be registered as VC if they do not have a device as this would break RSP processes which assume all VCs have been provided with a device.` Text change: clause `32.` L405 (clause text says `withdrawn` only; the comment says `withdrawn or declined`). D06 L904-L905 para 181; D06 L922 `185. ... we agree with the TCF that vulnerable consumer applications can be considered withdrawn` -> D05 cl. 36, 17.1, 45.7, 46.5.
- R14 (L441, printed mid-line after clause 40.4). `We propose additional wording to note that this obligation should only apply where the vulnerable consumer (or person acting on their behalf) notifies the provider that they have moved. There may be cases where providers do not automatically know if the vulnerable consumer has moved premises, such as where the vulnerable consumer is not a customer or if their home phone runs over FWA connection.` Text change: clause 37 L428. D06 L959 para 196; D06 L976 `199. We do not believe there is a need to adjust the wording regarding notification by consumers as suggested by the TCF.`

TCF text edits without a visible comment: none found beyond those above. Text that is the Commission's draft and that the TCF expressly welcomes: clause 31 (L220 `we welcome the clarification in Clause 31`); the 29.3 change (L393 `The suggested change is helpful, but`).

## 9. Attachment A - application form (L490-L709), index

- Status: the 2020 template form. D01 L339 draft decision `63.1 no longer provide the template written application form as Attachment A of the Code.`; D08 still prints it (and Appendix B L86 still lists it); D05 has none. D06 L798 `151.1 remove ‘Attachment A – Application form to be considered a vulnerable consumer’ from the Code;`.
- Layout problem: text boxes are out of order. L490-L495 (question 2 and its note `You must be added as an authority to the customer’s account before you make this application`) print **before** the Attachment A heading (L496). Part headings print after their content: `PART B` L568 (after Q6-Q7 at L561-L566), `Part C` L581, `PART E: Guidance` L640 (inside Guidance Note 1). Step numbers for Part D print as `3.` and `4.` (L609-L611).
- Eligibility statement L501: `be at particular risk of requiring the 111 emergency service (either now or sometime in the near future); and` / `not have a means to contact the 111 emergency service at their premises that can work for a continuous 8-hour period.`
- Who may complete the form, three bullets L502: `a customer (the account holder);` / `a person who is listed as an authority on the customer’s account; or` / `the customer or person listed as an authority on the customer’s account on behalf of someone who lives at the premises where the home phone line is supplied.` D06 L806-L812 paras 154-155 repeats these three and says they do not align with clause 14.2 (now 18.2).
- Parts: A personal details (Q1-Q5, with 3a, 3b, 5a); B (Q6 category `□ Health □ Safety □ Disability`; Q7 `□ Permanent` / `□ Temporary`); C (Q8, 8a, 8b, 8c); D general declaration; E guidance. Questions are numbered 1 to 8; "3" appears only as 3a and 3b.
- Guidance Note 1 (L616-L646): four scenarios - `Scenario one` Mary and Joe, pensioners, falls (L623-L624); `Scenario two` Fatima, `type 2 diabetes and is in the early stages of dementia` (L625-L626); `Scenario three` Jennifer's father, family violence (L628-L629); `Scenario four` Tane, both knees replaced, `over the next three months` (L630-L631).
- Guidance Note 2 (L647-L671): nominated person examples (L657, same four safety occupations as clause 15.2) and four evidence examples (L664-L671, adding `(eg, a GP)` and `(eg, an ID card)` to the clause 16 list).
- Guidance Note 3 (L673-L693): `must be able to work for a continuous (ie non-stop) 8-hour period if used as instructed.` (L685); three ways a person already has a means (L689-L693: copper landline, mobile with coverage, UPS `(eg a battery back-up)`).
- General guidance (L694-L709): purpose (`an appropriate means (eg, a mobile phone)` L697); `Currently, the relevant industry dispute resolution scheme is the Telecommunications Dispute Resolution Scheme.` (L699); TDR is `a free, independent service` (L704); Commission contact L709.

## 10. Contradictions, conflicts and amendments (neutral, both locations)

1. Title/year of the draft instrument, same ISBN 978-1-991085-62-7: D08 L7 `[Draft] Commission 111 Contact Amended Code 2023`; D08 L14 `Commission 111 Contact Amended Code [2024]`; D08 L18 `[Draft] Commission 111 Contact Amended Code [2024]`; D01 L16 `Draft Commission 111 Contact Amended Code 2023`; D05 L48-L50 `Draft Commission 111 Contact Amended Code` `2024`; D06 L20-L22 `Draft Commission 111 Contact Amendment` `Code 2023`. No precedence stated.
2. Commencement: D08 L37 (3 months after publication) versus D05 L13/L20 (published 26 June 2024; amendments in force 1 July 2024) and the grace period D05 L110, D06 L106, D06 L1171. D06 L1174 para 252 gives the Commission's reason for the dates.
3. Clause 42 wording, final documents disagree with each other: D06 L967 para 198.2 `add a new clause 42 which states “If a vulnerable consumer moves premises and remains with the same provider, such provider may check the consumer’s status, and may require the vulnerable consumer (or someone on their behalf) to re-apply to demonstrate that they continue to be a vulnerable consumer if something material has changed”.` versus D05 L392, which ends `to demonstrate that they continue to be a vulnerable consumer.` D08 L428 (draft cl. 37) has the `if something material has changed` words; D06 L336 summary table also has them. D06 L967 also says `remove clause 35.2 of the Previous Code (otherwise now clause 42.2 of the Code)`.
4. "Clause 33.3": D06 L859 and L873 refer to `clause 29.3 of the Previous Code (now clause 33.3 of the Code)`; D05 clause 33 has only 33.1 and 33.2 (D05 L362-L363).
5. Resubmission cross-reference: D08 L427 and D01 L398 `in accordance with clause 24`; D06 L948 para 192.4, describing the Previous Code, `in accordance with clause 26`.
6. Draft clause 7.4 tail as quoted: D08 L236 `purchase a residential service or switch between telecommunications technologies or services without being aware of such information`; D06 L695 para 125.1 quotes the draft decision as `purchase a residential landline service or switch between telecommunications technologies or services without being aware of such information`; D01 L302 para 54.1 `such that these consumers are not able to purchase a retail landline service from the provider without seeing that information.`
7. Scope of TCF's clause 8.3: D08 L242 `clauses 7.3, 7.4 and 8.1`; D06 L710 `obligation to provide information under clauses 5 and 6`.
8. Amendment procedure section: D08 L484 `section 236(1)-(4)`; D05 L454 `section 239(1)-(4)`.
9. D05 internal cross-reference as printed: D05 L426 `clauses 46.3, 45.4 and 46.5` (D08 counterpart L456 `clause 39.341.3`).
10. Date of the TCF's earlier (Request for Views) submission, for entity alignment only: D13 L7 `16 June 2023`; D01 L343 and D06 L610/L790/L887 cite it as `(19 June 2023)`.
11. TCF battery position across its two submissions (locations only): D13 L28 `10. Reducing the battery backup requirement to four hours would likely increase the pool of suppliers`; D08 L154/L173 keeps eight hours and asks for `when used as recommended`.
12. Units/wording for the application deadline: D08 L331 and D05 L314 `Within ten working days`; D01 L448 `within 10 working days`; D06 L999 `within working 10 days`.

## 11. Shared ground (facts in D08 located elsewhere in the bundle)

- Edition relationship: 2020 Code ("current Code" in D01; "Previous Code" in D06; ISBN 978-1-869458-52-2, not a file in the bundle, but its text is recoverable from D08's fused old wording and old clause numbers) -> D08 draft (Commission mark-up of 18 Dec 2023 + TCF mark-up) -> D05 final (26 June 2024). Old clause numbers 31-48 are visible in D08 as the first half of each fused number (e.g. old 38.7 = draft 40.7 = final 45.9; old 29.3 = draft 29.3 = no final equivalent; old 35.2 deleted; old 33 = draft 34 = final 39).
- D01's summary table of seven proposed amendments uses D08's draft numbering: D01 L214-L234 `Sections B, D`; `Clause 7.4`; `Section F2`; `Clause 29.3`; `Clauses 6.6 & 31`; `Clause 37`; `Clause 40.7`. D03 (Age Concern) also uses draft numbering: D03 L49 `Clause 37`; D03 L43 and L47 restate the 36-month and 10-working-day proposals.
- D06 uses "Previous Code" numbers with the final numbers in brackets, e.g. D06 L836 `Clause 26 of the Previous Code (now clause 30 of the Code)`; D06 L995 `Clauses 38.3-38.6 of the Previous Code (now clauses 45.3, 45.4, 45.6, and 45.8 of the Code)`; D06 L1136-L1137 `Clause 7.2 ... (now clause 9.2 of the Code)`, `Clause 13 ... (now clause 16 of the Code)`.
- Submission deadline for the consultation D08 belongs to: D01 L116 `Submissions are due by 5pm on 1 March 2024.` D06 dates the TCF mark-up 1 March 2024 (D06 L408). D06 L179-L180 lists the 10 submitters on the draft.
- Repeated figures (same value): eight-hour minimum period - D08 L154; D05 L168; D01 L353 `a continuous 8- hour period`; D06 L1135 `“a continuous eight-hour period”`; D13 L24. 36 months - D08 L382; D01 L224, L353, L356, L368; D03 L43; D05 L355 (as a test interval); D06 L310, L840, L842, L845, L853, L859, L869, L873, L874. 10 working days (provisioning reasons) - D08 L443; D01 L234, L450, L466; D03 L47; D05 L411; D06 L342, L1006, L1021. Ten working days (application decision) - D08 L331; D05 L314; D01 L448. 30 November disclosure - D08 L436; D05 L402; D01 L416, L991; D06 L983. 5 years retention - D08 L454-L457; D05 L424-L427. Five working days - D08 L463; D05 L436. Once a year - D08 L413-L414; D05 L383, L386; D06 L874. 12 months - D08 L229; D05 L233; D06 L683, L724, L744, L755, L762; D01 L282. 10 February 2021 - D08 L229; D06 L744, L760 (removed in D05). 1 August 2021 / 1 February 2021 - D08 L102; D05 L104. Project no. PRJ0046469 - D08 L5; D01 L4; D02 L5; D05 L5; D06 L4. `3950406.1` - D08 L3; D05 L3.
- D06 verbatim repeats of D08 Code text: business landline services definition D06 L187 (footnote 15, `Defined in the Draft Amended Code as`) = D08 L118-L128; clause 21.1-21.3 D06 L608 = D08 L348; clause 7.3 D06 L744 = D08 L228-L229; the three excluded services of the 2020 definition D06 L357-L360.
- D06 restatements of TCF comments with changed wording: `“means a continuous eight-hour period when used as recommended”` D06 L1144 (= D08 L154); `“an overly specific additional requirement in the Code”` D06 L711 (= D08 L247); `“operational simplicity”` D06 L752 (= D08 L246); `“on the customer’s website”` D06 L906 (= D08 L220, straight apostrophe in D08); "3 years" (D08 L393-L395) restated as `36 months` (D06 L853).
- D06 page citations to D08 (D08 has no page markers): pages 12 & 14 (D06 L197, L408), pages 12, 21 & 22 (D06 L199), pages 13 & 14 (D06 L201), page 12 (D06 L633), page 14 (D06 L727, L728, L769), page 16 (D06 L614), page 21 (D06 L866), page 22 (D06 L909), page 23 (D06 L972).
- Earlier TCF positions that D01/D06 tie to the same topics (D13 = TCF Request-for-Views submission; mapped by the caller, not here): D13 L21 para 7 (consumer who does not accept a suitable device), cited at D01 L387 and D06 L887; medical alarms D13 L29-L30 para 11 onward, cited at D06 L610; application form `paras 21-22`, cited at D01 L343 and D06 L790.
- Entities: issuer of the D08 base text = Commerce Commission (L7, L63); commenter = TCF / New Zealand Telecommunications Forum (D06 L53 `TCF New Zealand Telecommunications Forum`; D01 L25 `TCF Telecommunications Forum`). Commission member lists: D08 L7-L8 versus D05 L9-L12 and D06 L8-L11.
- Not in D08 but adjacent in D06 to a D08 topic (copper exclusion): D06 L438 para 61 gives copper connection counts and dates; D08 gives no counts.

## 12. Gaps

- D08 text: none unread; no clipped or missing text reported by intake.
- Visual gap: tracked-change mark-up and comment anchors are not recoverable from the supplied text (section 0). Attribution of each fused string to the Commission or the TCF rests on the D08 comments, D01 and D06 as cited; items marked unresolved: direction of `comescame`; authorship of `(given the consequences set out in clause 31)` (L209); anchor of comment R12 (L397); current page numbers in Appendix B (T4); whether the TCF's mark-up keeps or strikes the Attachment A form.
- D06's page references to D08 cannot be checked (no page markers in D08).
- Other documents: only the line ranges listed in section 0 were read by this mapper.
