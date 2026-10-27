# aq-03169 - document map

Maintained by the caller from `text/`. Navigation only; questions quote the documents, never this map.

## Bundle

- What it is: ten responses to the Competition and Markets Authority's October 2018 invitation to comment on the
  statutory audit market (four audit firms outside the Big Four, two Big Four firms, one professional body, three
  investors). Most answer the same 27 numbered questions; Q19-Q23 are on a market share cap.
- Documents: 10; local ids D01-D10 equal the task page's Doc 1-Doc 10 (`notes/intake.json`).
- Gaps: none known. Capture says "10 of 10 read in full (466,209 characters)"; every source hash matches the capture.
  The capture carried a page notice ("Docket has been updated. Reload this page ..."); it does not affect documents.
- Extraction spot-checks (plain-text captures, no pages): body and metadata compared for each document. D02's two
  charts survive only as axis labels and a jumbled value run (L248-250, L293-295, L609-610): unusable, no question
  relies on them. D02's measure table (L391-436) and D04's Annex 2 table (L828-912) are flattened row by row.
  D01 is OCR text with systematic letter errors ("betieve", "ctients", "60/o" for 60%); digits read correctly.
  Footnotes checked: D02 notes 1-5 (L169-171, L684-689), D04 notes 1-10, D05 notes 1-4, D06 notes 1-2.
- Provenance: `notes/intake.json`, capture sha256 0a431f12..., saved 2026-10-12 00:49; no earlier bundle shares these files.
- Reuse binding: `text/manifest.json` hashes as extracted 2026-10-12; all ten documents read in full by the caller
  (D04 Annex 1, L383-826, is a 2017 economic blueprint unrelated to audit; read, nothing used).

## D01 - BDO LLP (Doc 1), 30 October 2018, 28,641 chars

- Author: BDO LLP ("Challenger Firm"). Answers Q1-Q27.
- Q10 L94: about twenty companies at the top of the FTSE 100 it could not service.
- Q15 item 4 L143-155 (char 14,512): market share caps "most impactful"; "by 2023 no audit firm can act for more than 60
  FTSE 350 audit [clients]"; fines on additional fees; monitoring trustee; similar caps for financial services / non-listed PIEs.
- Q15 other items L129-174: audit-only firms (not viable), break-up, NAS restriction, joint audits ("top slicing"), direct
  support ("no merit"), staff switching, ownership.
- Q18 L195: all non-audit work to PIE audit clients barred, for every firm.
- Q19 L201: number of companies audited is the best measure.
- Q22 L221 (char 24,739): collective cap "cannot be greater than 80% of the FTSE 350", ideally 60%-70% (OCR "60/o"),
  designed as a per-firm maximum, "say 50"; phased in.
- Q23 L223: a firm at its cap may "divide individual units into two" through evenly shared joint audits.
- Q25-Q27: no independent body; current tendering frequency works.

## D02 - Deloitte LLP (Doc 2), 30 October 2018, 93,977 chars

- Letter L16-171 (paras 1.1-3.3), appendix answers Q1-Q27 L173-689.
- 1.1 L67 (char 7,420): "98% of FTSE350 companies audited by the four largest firms". 1.3 L72: four largest audit 45-50% of the
  whole US listed market, 75-80% in the UK (appendix 7.1.2 L279 says 75-85%).
- 1.11-1.12 L89-91 (char 11,154): target of 20% of the FTSE 350 for a firm outside the four largest in five years' time, "a
  sevenfold increase"; needs 60% of all tenders in the next five years, by 2023/4, plus one to two years before audits go live;
  Arthur Andersen had 8% of FTSE350 audits.
- 1.14-1.19: caps by number of companies, whole listed market plus a FTSE 350 subset; shared audits yes, joint audits no;
  five-year sunset on support measures.
- 2.5-2.6 L133-135: KAM statistics (over 55%, 7%, over 2,100 people). 3.x: ban on non-audit services to FTSE 350 / large PIE
  audit clients; audit-related services listed at 3.3 L156 (also 14.5.1, 18.4).
- Notes L170-171: US restatements 1,859 (2006) after 1,632; FRC: non-audit fees from audited entities 9.7% of fee income in
  2017 (12.0% in 2014), 48.7% of audit fees (56% in 2014).
- App. 4.2 L234 (char 31,702): 74% of the 213 FTSE 350 companies that tendered 2011-2017 appointed a new firm. App. 5.2 L254:
  "only 3% of FTSE 350 audits" outside the four largest. App. 7.1.1 L274: of 244 tenders, eight won by BDO or Grant Thornton.
- App. 14.4 L389-436: table of 17 measures rated on costs, benefits, implementation challenges; 14.5.x notes.
- App. 19 L593-602: only workable measure is number of companies. App. 20.4 L616 (char 83,552): firms outside the four
  largest "currently perform 11 audits of the FTSE 350 today", £5m of fees; a 20% share in five years needs "about 60 tenders,
  or 60% of the FTSE250 tenders in this period". App. 21.1: £40m-£70m investment over five years. App. 22.2-22.3 repeat 1.11-1.12.
- App. 27.1 L679: FTSE 350 tender every ten years, rotate every twenty.

## D03 - Ernst & Young LLP (Doc 3), 30 October 2018, 74,009 chars

- Letter L15-125: five key changes, 27 numbered proposals (UK-SOX, transparent tender regime, conflicts committee).
- Para 25 L105 (char 24,819; repeated Q4 L219): FTSE 350 companies with over 98% votes for the auditor: 78.9% (2013-14
  AGM season), 76.9% (2016-17); votes over 20% against rose from 0 to 0.6%.
- Appendix 1 L128-153; Appendix 2 answers Q1-Q27 L156-512. Q19-Q22 L416-446: risks of caps, no level given
  (Q20-Q22 refer back to Q19). Q23: against joint audits. Q25: against an independent appointing body.
- Transition to a new client affects profitability for up to five years (L211, L249). Grant Thornton "the fifth biggest firm".

## D04 - Grant Thornton UK LLP (Doc 4), 2 November 2018, 111,690 chars

- Executive summary L17-47: withdrew from FTSE 350 tendering (March 2018, 5.3 L150); non-audit fees "around 40 per cent of the
  audit fee (and up to a limit of 70%)" L30; cap not useful by itself L31; independent appointment body for FTSE 250 L36;
  successful outcome includes "10-20% of the companies in the FTSE 350 ... audited by non-Big 4 firms within three to four
  years" L40 (char 11,423).
- Q3 3.5 L133: tender every five to seven years, reappointment once. Notes 3-5 L138-158: 61 per cent basic disclosures;
  "Only 8 of 29" tendering FTSE 350 companies changed auditor; 18 do not disclose tenders; six breach the 10-year rule; 45.2 per cent.
- Q7 7.1 L181: Big 4 had 97% of FTSE 350 audits by volume in 2016/17, nearer 95% at the Competition Commission's report.
  Note 7 L206: 73% vs 81% of reviewed FTSE 350 audits.
- Q18: services to stay permitted L310-318; PIE definition to include over 5,000 employees L329.
- Q19-Q23 answered together, 23.1-23.6 L337-350 (char 64,925-66,184): cap by volume not value ("the top 175 firms on the FTSE
  account for 94% of all FTSE fees"); 20% by summer 2019 would need Big 4 help; "currently realistic that non-Big 4 auditors
  could audit c. 40-50 of the FTSE 350 firms within a three- to four-year period"; France's top four have c. 47%.
- Q26-Q27 L357-376: independent body appoints and sets fees; terms c. 5 years, switch after 10; tender every five or seven years.
- Annex 1 L383-826: "Shaping a vibrant economy" (June 2017), quotes Hermes's chief executive L549-552. Annex 2 L828-912: 16 measures.

## D05 - Hermes Investment Management (Doc 5), 30 October 2018, 10,391 chars

- L19-21: majority owned by Federated ($392.2 billion AUM); Hermes £33.6 billion AUM; Hermes EOS advises on £330.5 billion.
- L23 says the CMA "has launched a market study today" (the letter is dated 30 October; D06 L6-7 and D04 L6 date the launch 9 October).
- L32: AIG $5.1bn vs $1.5bn. L46: asks the CMA for margin data going back 5-10 years. Remedies L49-67: no single public
  appointing entity; not averse to breaking audit from consulting; shareholder committees.

## D06 - ICAEW Representation 123/18 (Doc 6), 30 October 2018, 71,264 chars

- Intro L6-21: study launched 9 October 2018; earlier investigation October 2011-October 2013; Order in effect January 2015;
  EU rules June 2016.
- Major points L35-61. Para 8 L52-53 (char 10,429-11,076): collective cap worth investigating, set at "the lower, tighter end
  of the options"; "a market cap of around 65 clients for any single firm"; review after three-to-five years.
- Q19 paras 82-87 L273-282 (char 49,046): three ways to measure; para 87: "each Big Four firm could be restricted to auditing
  65 of the FTSE 350 companies". Q22 para 92 L297: "toward the lower end of the range of options", no figure.
- Para 111 L356: Audit Commission 1983-2015, 70% in-house, rest among seven firms.
- Appendix A L370-424 (char 69,116): para 92 summary gives the only figure, "a collective Big Four market share cap of around 60%".

## D07 - Moore Stephens LLP (Doc 7), 30 October 2018, 35,412 chars

- Q14-Q15 L190-210: cap plus joint/shared audits "blended": a cap on what the big four can audit solely.
- Q19 L239 (char 28,835): measure by audit fees. Q22 L250 (char 29,562): "a progressive fee cap moving towards 70%".
- Q25 L273: FCA/PRA Skilled Person panel as a model.

## D08 - Nexia Smith & Williamson (Doc 8), October 2018, 16,172 chars

- Q12 L58: "only 4-6 credible players". Q19 L99: number of companies audited. Q20 L105-108 (char 10,686): cap "could start
  at 90%, and reduce by, say 5% per annum over 5 years"; released share open to challengers alone or in a joint audit
  with no more than one Big Four firm. Q22 L116: the sliding scale. Q23 L119: joint audits, French model.

## D09 - Standard Life (Doc 9), undated, 12,299 chars

- A3 L36-42: three competing firms are enough; shared audits would raise competition "by around one-third".
- B L57-75: no market share limits; shared-audit targets for the Big 4; audit tenders take 3-6 months.

## D10 - USS Investment Management (Doc 10), 30 October 2018, 12,364 chars

- L15-19: fund over £60 billion; six direct assets; expects auditor change at least every 20 years; voted against auditor
  re-election at 17% of 2017 UK meetings. L55-56: its own 2017 tender drew two firms.

## Shared ground (navigation only)

- Per-firm client limits: D01 L145 (60, any audit firm, by 2023), D01 L221 ("say 50"), D06 L53/L282 (65, each Big Four firm).
- Collective cap levels: D01 L221 (at most 80%, ideally 60-70%), D06 L408 (around 60%, appendix only), D07 L250 (70%, by fees),
  D08 L106 (90% falling 5% a year for 5 years); none in D03, D04, D09.
- Share for firms outside the Big Four: D02 L89 (20% target, five years), D04 L40 (10-20% in three to four years), D04 L348
  (40-50 companies realistic), D02 L616 (11 audits today), D02 L67 / L254 (98% / 3%), D04 L181 (97% in 2016/17).
- Tender numbers: only D02 (L234, L274, L616) and D04 note 4 (L155-156).
- Measure of share: number of companies D01, D02, D04 (volume), D08; audit fees D07; three options D06.
- Tendering frequency: current rule D02 L679, D04 L156; proposal D04 L133, L362, L370; D10 L19 (20 years).
- Entity crossover: D04 Annex 1 quotes Hermes's chief executive (D05's author); D05 L46 and D03 L250, D07 L136, D08 L37,
  D02 L263 mention Grant Thornton's FTSE 350 withdrawal.
