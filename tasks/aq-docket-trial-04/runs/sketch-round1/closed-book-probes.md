# Sketch round 1: closed-book probes (question text only), 2026-10-06

Fresh closed-book-solver agents (Claude Code, claude-opus-5-5, no tools), each given only the
sketch question text below. Returns copied verbatim. Sketch wording at the time did not name the
region (fixed afterwards in q01 rev 1 and q02).

## i02

Question: Which country had the largest percentage decline in requested State Department- and USAID-managed aid from the Biden Administration's FY2023 request to its FY2025 request, and what was that decline, to the nearest whole percent?

Return:

answer: El Salvador, about 40% (a guess)
confidence: low
basis: I don't remember the source table, so both the country and the percentage are inferences. The wording "State Department- and USAID-managed" matches Congressional Research Service reports on Latin America. Within that region, El Salvador seemed the likeliest to see a big cut in requested aid because of U.S. friction with President Bukele. Other plausible answers include Nicaragua, or Tunisia if the source covers the Middle East and North Africa. The 40% figure is an estimate, not a recalled number. To answer properly I'd need the country-level request figures for FY2023 and FY2025.
contaminated: no

## i01

Question: Which countries saw the Biden Administration's requested State Department- and USAID-managed aid decline from its FY2023 request to its FY2024 request and decline again in its FY2025 request? List them alphabetically.

Return:

answer: Iraq, Lebanon, Tunisia

confidence: low

basis: I couldn't work out which document or region this question refers to, so this is a guess. The question seems to come from a specific table, probably in a Congressional Research Service report, that compares the FY2023, FY2024 and FY2025 requests by country. I assumed it is a Middle East and North Africa table. My guess rests on trends I partly remember: the administration cut its requests for Tunisia after President Saied's 2021 power grab, and its requests for Iraq and Lebanon seemed to shrink. I can't recall the actual figures, and the table may cover a different region, such as Latin America and the Caribbean.

contaminated: no

## i03

Question: How much of the Biden Administration's FY2025 aid request for Haiti was for accounts that carry out part I of the Foreign Assistance Act of 1961?

Return:

answer: About $195 million. This is a rough estimate, not a figure I remember.
confidence: low
basis: I don't remember the exact account-by-account figure. I worked it out from a hazy memory that the FY2025 request for Haiti was about $235–260 million. The accounts that carry out Part I of the Foreign Assistance Act are Development Assistance, Global Health Programs (both the USAID and State/PEPFAR parts) and International Narcotics Control and Law Enforcement. The Economic Support Fund and military training funds fall under Part II, so I left them out. Getting the exact number would need the source document, most likely a CRS report or the FY2025 budget justification.
contaminated: no

## Caller notes

- i02: misses (gold Honduras, 35% decline).
- i01: misses; exposed the missing region in the wording (fixed: "Latin American and Caribbean").
- i03: misses the amount but states the FAA part I/II account split from memory, so D04 would
  not be necessary in practice (platform removal test). i03 dropped.
