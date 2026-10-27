# aq-03711 - document map

Navigation only. Questions quote the documents, never this map. Detailed sequential maps of the three long
documents sit beside this file: [doc-map-D01.md](doc-map-D01.md) (Doc 2), [doc-map-D06.md](doc-map-D06.md)
(Doc 3), [doc-map-D08.md](doc-map-D08.md) (Doc 12, with a clause-by-clause draft-versus-final comparison).

## Bundle

- What it is: the NZ Commerce Commission's 2023-24 review of the Commission 111 Contact Code (vulnerable
  consumers' means of calling 111 in a power cut): Request for Views, six submissions on it (one a Spark letter
  of 30 November 2022), Draft Decisions and Reasons, four submissions on the draft (one of them the draft Code
  itself with the TCF's tracked changes), final Decisions and Reasons, and the final Code.
- Documents: 14, plain text. Local id -> platform Doc number (notes/intake.json):
  D01 = Doc 2, D02 = Doc 1, D03 = Doc 10, D04 = Doc 11, D05 = Doc 14, D06 = Doc 3, D07 = Doc 4, D08 = Doc 12,
  D09 = Doc 5, D10 = Doc 13, D11 = Doc 6, D12 = Doc 7, D13 = Doc 8, D14 = Doc 9.
- Gaps: none in the capture (14 of 14 "read in full", gap_characters 0). Source-text defects that are part of
  the documents as the platform holds them: D09 (One NZ) jumps from "Page 2 of 6" to "Page 4 of 6" (page 3,
  paras 8-10, absent; para 7 breaks off mid-sentence at L25); Figure 1 is a caption only in D01 (L857) and D06
  (L160); D08's tracked changes are flattened (old and new words and clause numbers fused, comments displaced
  from their anchors, Attachment A text boxes out of order); D11 (Spark) has "[ ]" redactions for every cost
  and count except the $1,599 retail price.
- Extraction spot-checks: text files equal the captured bodies (hashes in notes/intake.json match the manifest).
  D01 73 printed pages, D06 58: one table row and one footnote each checked by the mappers. Short documents
  read in full by the caller against their page markers; no tables in them.
- Provenance: AQ-03711_2026-10-12_2132.txt, capture sha256 e0798b2a...; split 2026-10-12, no warnings.
- Reuse binding: manifest sha256 per document (text/manifest.json); the three long maps name theirs.
- Not a repeat bundle (no "111 Contact Code" text or file in any earlier task, 10.6-10.8). Family: NZ Commerce
  Commission consultations (aq-02940, aq-03066, aq-03120, aq-03423, aq-03557, aq-03635, aq-03707).

## Coverage

| Id | Doc | What | Read |
| --- | --- | --- | --- |
| D02 | 1 | Request for Views, 18 May 2023 | caller, full |
| D01 | 2 | Draft Decisions and Reasons, 18 Dec 2023 | mapper, full (L1-1436); caller L50-277, L469-492, L690-799, L1340-1414 |
| D06 | 3 | Decisions and Reasons, 26 June 2024 | mapper, full (L1-1259); caller L150-389, L440-589, L976-1183 |
| D07 | 4 | DPA submission, June 2023 | caller, full |
| D09 | 5 | One NZ submission, 16 June 2023 | caller, full (page 3 absent from source) |
| D11 | 6 | Spark feedback letter, 30 Nov 2022 | caller, full |
| D12 | 7 | Spark submission, 16 June 2023 | caller, full |
| D13 | 8 | TCF submission, 16 June 2023 | caller, full |
| D14 | 9 | WISPANZ submission, June 2023 | caller, full |
| D03 | 10 | Age Concern NZ submission, 29/02/2024 | caller, full |
| D04 | 11 | Bupa submission, 1 March 2024 | caller, full |
| D08 | 12 | Draft amended Code with TCF mark-up | mapper, full (L1-711); caller L1-60, L96-170, L360-711 |
| D10 | 13 | Ryman Healthcare submission, 29 Feb 2024 | caller, full |
| D05 | 14 | Commission 111 Contact Code 2024, 26 June 2024 | caller, full |

## Short documents (facts only they state)

- D02 (Doc 1): RfV published 18 May 2023; submissions "by 5pm on Friday 16 June 2023" (L150); indicative
  timetable L129-143 (draft decision "July/August", submissions "August/September", cross-submissions
  "September", final decision "October"; no year printed after June 2023); seven questions (L174-193); Code
  published 17 November 2020, in effect 1 February 2021, means by 1 August 2021 (L62); "in force for two
  years" (L64); statutory steps incl. 30 working days (L92).
- D11 (Doc 6, Spark, 30 Nov 2022): about 18 languages (L17); "around half of our registered vulnerable
  consumers have medical alarms of some sort" (L35); 4 handset types (L78); team of 6 (L90); EcoFlow RIVER
  Pro retail "$1,599 (including GST)" (L92); 4-hour River unit "half the price" (L117); measure 38.7 and five
  delay causes (L120-134); eight topic headings. All other figures redacted.
- D12 (Doc 7, Spark, 16 June 2023): Medical Dependency scheme (L11-13); Cyclone Gabrielle customer, "three
  short (1-2 hours) power cuts ... over a two-day period" (L28); three application outcomes (L62-65); list of
  the eight November 2022 topics (L75-89); "replace a device every 3 years is unnecessary" and "another 12
  months" (L90); Chorus should cover costs (L100-101).
- D09 (Doc 5, One NZ): Far North and Auckland-floods customers (L10-11); missing battery, multiple appliances
  (L13); TCF Vulnerable End User Code in development (L17); four-hour request (L35); "Chorus has recently
  announced that they plan to retire their entire copper network in the next 10 years" (L38); three proposals
  a-c (L52-58).
- D13 (Doc 8, TCF, 16 June 2023): does not answer the RfV questions (L11); sections B-H; four hours (L28);
  "around half" have a medical alarm (L34); 16 members listed, WISPA-NZ "represents 28 Wireless Internet
  Service Providers", members "over 95 percent" of consumers (L83-84).
- D14 (Doc 9, WISPANZ): "33 WISPS", "an estimated 70,000 end users" (L20-21); no member known to have supplied
  a mobile (L37); rental "often less than $20.00", backup "easily exceeds $1000.00" (L80; quoted in D01
  L1323); business customers should be exempt (L90-95).
- D07 (Doc 4, DPA): four recommendations (L95-102); five alternative formats (L100).
- D03 (Doc 10, Age Concern): 30 local Age Concerns in 40 locations (L18); 1.2 million aged 65+ "within a
  decade", "over 850,000" now (L24); one in four disabled, 35% of them 65+ = 370,000 (L28); 25%, 20%, 30%
  (L29); lists the draft's seven amendments in its own order, supports six, opposes "Clause 37" (L33-50);
  four recommendations (L53-64).
- D04 (Doc 11, Bupa): 3,500 staff (L6); "35 retirement villages and 39 care homes", "more than 5,000
  residents", care homes "offer rest home and hospital care, with certain care homes offering dementia and
  psychogeriatric care" (L7); four care levels (L45); "We do not supply landlines to these consumers" (villages,
  L47); no landlines offered to dementia and psychogeriatric residents, rest-home and hospital residents "may
  choose to be provided with a landline" (L48); proposed definitions (L76-87); "3 months following
  publication" and "at least a 6 month transition period" (L92).
- D10 (Doc 13, Ryman): 40 villages, about 12,000 residents: 6,000 independent, 3,000 serviced apartments, 3,000
  care centres (L8); ARC = rest home, hospital, dementia (L18); ARRC clause D19.6 (L22); NZS 8134:2008 (L29;
  Bupa cites NZS 8134:2021); restates scenarios a-c (L41-43); "In situations where Ryman on-sells communication
  services" (L46); nurse-call with battery back-up; proposed wording (L61).
- D05 (Doc 14, final Code): published 26 June 2024; amendments in force 1 July 2024 (L20); grace period
  1 July 2024 - 1 January 2025 (L110-112); 33 defined terms incl. disclosure year 1 July - 30 June (L154),
  health care services, managed medical or safety alarm, minimum period "a continuous eight-hour period"
  (L168), provider "excludes suppliers of health care services" (L189), qualified third party, residential
  landline service with five exclusions (L191-200); 12 months (9.3); ten working days (22); decline grounds
  23.1-23.5; examples 25.1-25.4; "tested at least once every 36 months" (31.5); one means per premises (37);
  once a year (39, 40); moving premises (42, without "if something material has changed"); disclosure by 30
  November, nine items (45.1-45.9); six record items, 5 years (46-47); five working days (49.2).

## Shared ground (navigation only)

- Edition chain of the Code: 2020 Code (text only inside D08's fused wording; described as "current Code" in
  D01 and "Previous Code" in D06) -> draft of 18 Dec 2023 (D08, D01) -> final of 26 June 2024 (D05, D06).
  Clause numbers differ in each: old 38.7 = draft 40.7 = final 45.9; draft 37 = final 42; draft 31 = final 35.
- Rules printed twice: every final rule in D05 and D06; every draft rule in D08 and D01. D01's Appendix B
  quotes each Request-for-Views submission; D06 summarises each submission on the draft with page pinpoints.
- Single-source facts: the submitters' own facts above; D02's timetable and deadline; D08 clause 5 (3 months
  after publication; restated only in D04 L92), the 2020 wording and Attachment A's four scenarios (L623-631);
  D06 L438 copper connections (159,000 at 31 December 2020; 51,000 at 31 March 2024) and its four facility
  examples (L570-577); D01 L750 and L767 (battery 8%/15%, mobile 76%/79%, 2021/2022), L780 (92% within eight
  hours, "some 30%" unresolved at four), L1371-1374 (Grey Power: 573 registered; 24% = 167,900).
- Proposal versus outcome: draft table of 7 amendments (D01 L214-234) versus final table of 11 (D06
  L255-349); 18 no-change topics (D01 L498-533) versus 13 closed without discussion (D06 L1051-1072);
  commencement 3 months after publication (D08 L37) versus 1 July 2024 with a six-month grace period (D06
  L1171, citing Bupa at L1175).
- Conflicts between documents: listed in doc-map-D08.md section 10 and doc-map-D06.md Shared ground (clause 42
  wording; "clause 33.3"; TCF dated 16 June in D13 and 19 June in D01/D06; Age Concern 29/02/2024 in D03 and
  1 March 2024 in D06; WISP members 28 in D13 and 33 in D14; NZS 8134 edition 2008 in D10 and 2021 in D04).
- Counts of parties: "18 submissions from 17 different parties" on the RfV (D01 L112, D06 L169); 10 parties on
  the draft (D06 L179-180). Only Spark is cited with two documents.
