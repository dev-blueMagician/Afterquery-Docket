# q01 rev 0 removal probe: solver-1 (left out D01 = Doc 2)

- Date: 2026-10-08
- Role: blind-solver (fresh, omitClaudeMd), packet tasks/aq-02102/runs/q01-r0-alt-k4/solver-1 (renumbered D01-D04)
- Question: verbatim q01 rev 0 (tested_sha256 b7c12ecb74dbef0da7954ed9c37189f3e29589e900757a0da78ce7ad47adfb36)
- Input: workspace root, packet path, question, and the instruction to add a forced guess with probability if not answerable
- Packet ids (probe-map.json): D02->D01, D03->D02, D04->D03, D05->D04

## Raw return (verbatim)

answer: not answerable from this packet (2023 share computable = 102/107 = 95.33%, but no 2021-22 response counts exist in the packet). Forced best guess: about 2.42 percentage points, probability ≈ 0.01 that it is correct.

confidence: high (that the packet cannot answer it); forced guess very low

path:
1. 2021-22 consultation = D01 (the consultation paper only). D01 L32 "From 22/11/2021 to 17/01/2022" (cover L9 says "ends on 17 January 2021", an evident typo). D01 L56: "A response to this consultation exercise is due to be published by 10 February 2022" – that response document is not in the packet. All "respon"/"respondent" hits in D01 checked: none gives response counts (L498 refers to respondents to HM Treasury's separate 2020 consultation; L919 is the Civil Service People Survey).
2. 2023 consultation report = D02. L28 consultation "began on 6 March 2023 and closed on 14 May 2023." Para 3.9 (L189): "The Cabinet Office received 107 responses in total from scheme members, trade unions and other organisations which in some way addressed the consultation questions. These consisted of 102 responses from individuals and five responses from organisations. In addition another ten responses were received from individuals that did not address the questions posed by the consultation". Table 2 (L203-209): "|Individuals|Email|102|", "|Total||107|" (the "Of which: Queried the effect of the remedy… 68" row is a subset of the 102, not additive). Annex A lists the five organisations (CSPA, Pen-gage, Prospect, PCS, DPF).
3. 2023 calculation: 102/107 = 0.953271 → 95.33% (organisations 5/107 = 4.67%).
4. Fall = (2021-22 individuals' share) − 95.33; the 2021-22 share is unavailable, so the fall cannot be computed. (The question's word "fall" implies the 2021-22 share exceeded 95.33%.)
5. D03 (2023 consultation paper) "respon" hits are only response instructions/privacy text, no counts; D04 is a 2017 Civil Service Compensation Scheme consultation, unrelated to McCloud, no such figures.
Forced-guess basis: no documentary basis; I do not reliably recall the 2021-22 consultation-outcome figures and did not fill them from memory. Assumed a plausible 2021-22 individuals' share of ~97.75% (midpoint of a plausible 96–99.5% range consistent with "fall") minus 95.33% → ~2.42 pp. Any specific two-decimal value has ~0.01 probability.

minimal_documents: D02 (for the 2023 figures) plus the 2021-22 consultation response/outcome report (the document promised in D01), which is missing; D01 only identifies the 2021-22 consultation. No in-packet replacement exists (D03, D04 tested: no counts).

readings: Reading A (2023 denominator = the 107 responses that addressed the questions; Table 2 "Total 107"): 2023 share = 102/107 = 95.33%, fall = S(2021-22) − 95.33. Reading B ("all responses received" includes the additional ten individual responses that did not address the questions): 2023 share = 112/117 = 0.957265 → 95.73%, fall = S(2021-22) − 95.73. The two readings differ by 0.40 pp, which matters at two decimals; an analogous denominator question (counted responses vs all emails received) may apply to the 2021-22 figures but cannot be checked.

gaps: Decisive missing fact – the 2021-22 consultation response/outcome (expected ~February 2022) giving the number of responses from individuals and the total received; not among the packet's four documents (manifest lists only D01–D04; docs/ holds the same four .txt sources). Sources are .txt (manifest method "text", pages null) – no PDFs/layout files to inspect for lost tables. Coverage: D02 read L1–260, L500–579 plus targeted L270–294, L355–358, L469–476; D01 read L1–200, L496–499, L917–919; D03 L1–135; D04 L1–120. Not read line-by-line: remainder of D01 (EQIA, draft regulations), most of D03 (policy sections/annexes), remainder of D04. All four files were explicitly searched for: respon/respondent, received, individual(s), organisations, trade union, %/per cent, "total of", "responses in total", "Total Received", count patterns followed by responses/individuals/respondents/organisations, and 2021-22/previous/earlier consultation references – the only response counts found anywhere are D02's 2023 figures.

contaminated: no (only workspace root, packet path and question provided; forced-guess instruction did not reveal any answer).

## Author record

- result: misses (unforced "not answerable"); forced guess 2.42 percentage points at p 0.01 (gold 3.81).
- note: the probe listed Doc 4's 102/107 and 112/117 as two readings of "all responses received" without choosing; this is relevant to the form's "One defensible answer" check (see q01 Lever checks).
