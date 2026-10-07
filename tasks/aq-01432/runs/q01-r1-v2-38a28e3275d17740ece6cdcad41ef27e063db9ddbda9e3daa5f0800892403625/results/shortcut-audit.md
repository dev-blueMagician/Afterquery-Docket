# q01 rev 1 - shortcut auditor (fresh shortcut-auditor subagent, packet shortcut), 2026-10-06

Raw return as received:

answer: 6 — D10 lists seven pressure-selling behaviours; six map to banned practices whose breach is a criminal offence; the exception is asking children to buy products (paragraph 30 of Schedule 20), which CMA207 says is not a criminal offence.

verdict: clear

shortest_path:
1. D10 (the short guide, L13 "This is a short guide to the unfair commercial practices guidance"), L71 "The banned practices fall into the following themes", L89–91 "Pressure selling" lists seven behaviours: "exaggerating the risks they face, pretending they have ordered something when they haven't, refusing to leave their home, hassling them by repeatedly contacting them, or making them feel they can't leave your shop without buying something. You mustn't ask children to buy products, or tell customers that if they don't buy your product then your livelihood will be at risk." D10 never mentions offences or prosecution.
2. D09 (CMA207) offences chapter L1387–1391: "It is an offence to engage in a commercial practice which involves: banned practices listed in Schedule 20 … [footnote 112]"; fn112 L1885: "It is not a criminal offence to infringe paragraphs 12, 13 or 30 of Schedule 20."
3. Mapping with the D09 list: risks → 14 (L577) offence; "ordered" → 24 (L679; alternative 31 at L739 also an offence); refuse to leave home → 27 (L703) offence; repeated contact → 28 (L711) offence; can't leave premises → 26 (L695) offence; children → 30 (L729) not an offence; livelihood → 32 (L759) offence.
4. Practice numbers = paragraph numbers: D09 L573 (practice 13 at "paragraph 13 of Schedule 20"); D08 L63 refusing to leave "paragraph 27", L159 false prize impression "paragraph 22" (both match D09's numbering); D04 L6 treats paragraph 13 as fake reviews.
5. 7 − 1 = 6.

sufficient_documents: D10 + D09, both needed. D10 gives the theme and behaviours, nothing on offences; D09 gives the paragraph text and the fn112 exclusion but groups nothing into themes (only L95 "These include fake reviews, misuse of trust marks, pressure selling and sales of illegal products", naming no behaviours). D08 and D04 only back up numbering. No single document is enough.

searches: offence/prosecut/criminal/section 237/convict; "pressure selling"/themes; pressur; Schedule 20; children/exhortation/"direct appeal"; "paragraphs 12, 13". docs/ and text/ identical hit counts (D09 23, D08 3, D10 1). Read: manifest; D10 and D08 in full; D09 L1–130, L360–780 (all 32 banned practices), L1365–1444 (offences), L1870–1929 (fn109–123). D01–D07 and D11 checked by grep only (no offences, criminal liability or prosecution). question.txt, notes and other packets not read; git status in context showed file names only — not contaminated.

readings/gaps:
- "Pretending they have ordered something" as inertia selling (31) instead of 24: still 6.
- Only the five "for example by…" items as the theme: 5 — weak, since the children/livelihood sentence sits under the same heading.
- Children behaviour prosecutable through the aggressive-practices offence: 7 — ruled out by "for breaching the banned practice involved".
- Difficulty risk, not a shortcut: straightforward two-document lookup (theme list plus one footnote); someone who knows the 2008 Regulations (children's practice likewise not an offence) could guess without the packet.
- Gaps: D09 chapters 4–9 body not read in full, but offence-term searches cover them.
