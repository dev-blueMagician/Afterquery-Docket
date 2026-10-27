# q02 rev 0 full-corpus blind solve: solver-1

- Date: 2026-10-08
- Role: blind-solver (fresh, omitClaudeMd), packet tasks/aq-02102/runs/q02-r0-v2-0acd5a1e.../solver-1 (all five documents, local ids)
- Question: verbatim q02 rev 0 (tested_sha256 0acd5a1e22e7d9789aa29aa2f8f4473dcfb21d5aa012ecb7f5fe0f9b6c3119f2)
- Why run: concrete fairness issue (Doc 5's "PGA" is never spelled out; does a careful solver link it to Doc 4's Prison Governors' Association?)

## Raw return (verbatim)

answer: FDA, GMB, Unite, NCOA (National Crime Officers Association), and the Prison Governors' Association (PGA) — 5 unions, any order.

confidence: high

path:
1. 2016 compensation offer & acceptors — D05 (Cabinet Office "Consultation on reform of the Civil Service Compensation Scheme", launched 25 Sept 2017): §1.2 "The Government made a formal offer to Trade Unions on 26 September 2016." §1.3 "The offer was ultimately agreed with eight out of ten unions (FDA, Prospect, GMB, UNISON, Unite, NCOA, the Defence Police Federation and PGA)." §1.4 "The reforms were not agreed by the Prison Officers Association (POA) and the Public and Commercial Services Union (PCS)". → Accepted set (8): FDA, Prospect, GMB, UNISON, Unite, NCOA, DPF, PGA.
2. 2023 McCloud consultation — D03 (response to consultation on draft Remediable Service Regulations 2023, which "began on 6 March 2023 and closed on 14 May 2023"). §2.8 meetings with "The National Trades Union Committee (NTUC) unions ... on 21 March 2023 and 19 April 2023" and "Non-affiliated unions and member representative bodies on 4 May 2023". §2.11 "Unions engaged during the consultation process are listed below": NTUC – "PCS", "Prospect", "FDA", "GMB", "POA UK (Prison Officers' Association)", "Unite"; Non-affiliated – "DPF (Defence Police Federation)", "The ISU", "NCOA (National Crime Officers Association)", "Prison Governors' Association". → Engaged set (10): PCS, Prospect, FDA, GMB, POA, Unite, DPF, ISU, NCOA, PGA.
3. Written replies — D03 §2.9 "A number of stakeholders followed up with formal written responses"; §3.9 "five responses from organisations"; Table 2: "Unions and other representative bodies: Prospect PCS Defence Police Federation | Email | 3" (others: Civil Service Pensioners Alliance, Pen-gage); Annex A lists the same five ("Prospect Union", "Public and Communication Services Union (PCS)", "Defence Police Federation (DPF) Union"). → Unions with written replies: Prospect, PCS, DPF.
4. Computation: Engaged − written = FDA, GMB, POA, Unite, ISU, NCOA, PGA; ∩ accepted-2016 = FDA, GMB, Unite, NCOA, PGA. Excluded with reasons: Prospect & DPF (accepted, but sent written replies); UNISON (accepted, not on 2023 engagement list); POA & PCS (did not agree 2016; PCS also replied); ISU (not one of the 2016 ten). Check: 5 + 3 excluded acceptors = 8 = "eight out of ten"; FDA/GMB/Unite/NCOA/Prison Governors' Association appear in D03 only in the §2.11 list, never as respondents.

minimal_documents: D03 + D05 (no substitutes found: D05 is the only source of 2016 acceptors; D04, the 2023 consultation paper, only says it would be issued to "The National Trade Unions Congress" and "Non-affiliated unions, federations and member representative groups" — no names; D01/D02 concern a different, earlier consultation — see readings).

readings: (a) Wrong-consultation reading (rejected): D01/D02 cover the 2021–22 prospective-remedy consultation (22 Nov 2021–17 Jan 2022; D01 response published 4 March 2022), not 2023 — its written union respondents were Prospect, FDA, PCS, DPF, GCG; using it would wrongly drop FDA. (b) Narrow "union" reading: if NCOA and PGA were treated as "member representative bodies" rather than unions → FDA, GMB, Unite; weaker, since D03 lists them under "Unions engaged" and D05 counts NCOA and PGA among the "ten unions". (c) Strict alias reading: if "PGA" in D05 is not accepted as the Prison Governors' Association → FDA, GMB, Unite, NCOA.

gaps: No document expands "PGA" — matching it to D03's "Prison Governors' Association" relies on the ordinary meaning of the initials (NCOA is expanded in D03). Coverage: D03 and D05 read in full; D04 read L1–135 and L1190–1229; D01 L140–279; D02 L1–40; all five documents searched for every union name/abbreviation (D04 had no union-name matches); remainder of D04, D01, D02 not read line-by-line. All documents are text-method (pages null), no layout/PDF pages, so no extraction problems to check.

contaminated: no

## Author record

- outcome: match (gold FDA, GMB, Unite, NCOA, Prison Governors' Association), confidence high.
- The solver named both risk readings (PGA alias, "unions" vs "member representative bodies") and resolved them toward the gold from the documents' own wording (Doc 5's "ten unions", Doc 4's "Unions engaged" heading).
