# aq-01432 - document map, part 1 of 4 (D01, D03, D04, D06)

Written by bundle-mapper (part 1 of a 4-way parallel map), 2026-10-06, for the caller to merge into
`notes/doc-map.md`. Navigation only: where things are, not what to ask. Questions quote the
documents, never this map.

Conventions: locations are line numbers of `text/Dnn.txt` ("L12" = line 12). L1 of each file is
the inserted header "# Dnn | docs/<file>". Quotes below collapse doubled spaces (D01 has many) and
normalise curly quotes/apostrophes to straight ones; hyphenation splits are kept as printed
("ad-vertising"). Copy evidence from `text/Dnn.txt`, not from this map. Platform numbering:
D01 = Doc 1, D03 = Doc 2, D04 = Doc 5, D06 = Doc 6 (local ids are alphabetical by file name).

## Part 1 bundle notes

- Scope: four documents. Two US: D01 (rule text) and D03 (FTC staff Q&A on that rule). Two UK:
  D04 (CMA208 fake reviews guidance) and D06 (short guide for businesses publishing reviews).
  D02, D05 and D07-D11 belong to parts 2-4 and were not read here.
- Provenance: `notes/intake.json` lists these four (capture numbers 1, 2, 5, 6) as
  "incomplete": false, "gap_characters": 0, "matches_capture": true, with captured_sha256 equal
  to source_sha256. `text/manifest.json`: method "text", pages null; source chars D01 20,536,
  D03 31,469, D04 49,587, D06 8,152.
- Extraction spot-checks against `docs/` originals (the originals are plain text, so there is no
  page image to inspect):
  - Page count: not applicable (plain text, no page markers, no printed page numbers in any of
    the four). Separator lines "-----": D01 5 (L47, L105, L165, L215, L257; original also 5, at
    orig L46, L105, L166, L217, L260); D04 29 (original 29); D03 1 (L307, end of file); D06 0.
  - Table: not applicable. None of the four has a table (no pipe or tab-aligned rows). D04's
    contents list (L21-L37) is a dot-leader list with page numbers. D04 Figures 1 and 2 are
    diagrams rendered as text lines.
  - Footnote: D04 has footnotes 1-25. Footnote 8 checked word for word against the original
    (orig L246 = text L181). D01, D03 and D06 have no footnotes.
  - D01's out-of-order words in § 465.2(a)/(b) (L132-L161) appear identically in the original
    (orig L133-L153). This is a layout defect in the source, not one introduced by extraction.
  - Confirmed in originals: D01 "SOURCE: 89 FR 68077, Aug. 22, 2024" (orig L78); D03
    "November 2024" (orig L301); D04 "CMA208" and "4 April 2025" (orig L2, L5); D06
    "© Crown copyright 2025" (orig L3); D06 "full fake reviews guidance" (orig L13).
- Unresolved (no page image exists): the printed reading behind D01's two-column garbling and
  the box layout of D04 Figure 2.

## D01 (platform Doc 1) - 16 CFR Part 465, "Rule on the Use of Consumer Reviews and Testimonials", preceded by a tail of Part 463

- Source: docs/16-CFR-Part-465-Use-of-Consumer-Reviews-and-Testimonials.txt | text/D01.txt,
  258 lines | no page numbers. Five "-----" separators (L47, L105, L165, L215, L257). The L47
  separator falls inside Part 465's section list, so the separators may mark page or column
  breaks. That cannot be verified from the text.
- Written or submitted by: no author or issuer line. "16 CFR" appears only in the file name. The
  only issuer word in the text is "the Commission's in-tention" (L31), and that sits in § 463.8 of
  the Part 463 tail, not in Part 465. "AUTHORITY: 15 U.S.C. 57a." (L78). D03 calls the rule "The
  Commission's Rule on the Use of Consumer Reviews and Testimonials" and answers as "FTC staff"
  (D03 L9, L11). That attribution is cross-document only.
- Type, date, edition: codified regulation text reflowed from a two-column page. "SOURCE: 89 FR
  68077, Aug. 22, 2024, unless otherwise noted." (L79). No other source note appears. No
  effective date, amendment history or edition date is printed. The effective date
  (October 21, 2024) is only in D03 L9. "Pt. 465" at L3 is a running header.
- Period covered: not applicable (rule text; no fiscal or calendar periods).

### Where Part 465 starts and ends
- L3-L35 are NOT Part 465. They are the tail of Part 463, whose title is not printed:
  - L5-L11: the closing paragraphs of a section whose heading and number are outside the capture.
    L5 ends the item before (a)(3) ("result in the consumer not benefiting financially from the
    product or service."). (a)(3) is at L6-L7 and cross-refers to "§ 463.3(a) and (b) and
    paragraph (c) of this section". (b) is [Reserved] (L9). (c) "Any item without Express,
    Informed Consent" (L10-L11) cross-refers to "§§ 463.3(a) and (b), 463.4, and paragraph (a) of
    this section". § 463.6(a)(4) at L20 cites "the requirements of § 463.5" for Add-ons.
  - § 463.6 Recordkeeping (L13-L26). Records are kept "for a period of twenty-four months from
    the date the record is created" (L15). Items (a)(1)-(5) list the records, with (a)(2)
    [Reserved] (L18). (b) is at L26: "Failure to keep all records required under paragraph (a) of
    this section will be a violation of this part."
  - § 463.7 Waiver not permitted (L27-L28).
  - § 463.8 Severability (L29-L31): "If any provision is stayed or determined to be invalid, it is
    the Commission's in-tention that the remaining provisions will continue in effect."
  - § 463.9 Relation to State laws (L32-L35). (a) In general: the part does not supersede State
    law "except to the extent that such statute ... is inconsistent". (b) Greater protection under
    State law: State law is "not inconsistent ... if the protection ... is greater".
  - Capitalised Part 463 terms whose definitions are not in the capture: Covered Motor Vehicle
    Dealer, Dealer, Vehicle, Add-ons, GAP Agreements, Express, Informed Consent, Materially
    different.
- Part 465 begins at L37. The heading words are out of order across L37-L42: "PART 465—RULE ON THE
  USE OF" / "AND" / "CONSUMER" / "TESTIMONIALS" / "## REVIEWS".
- L44-L77: section list (scrambled at L49-L58, e.g. "con-celebrity" L52 and "sumer testimonials."
  / "[Reserved]" L49-L50). It lists nine section numbers, one reserved: 465.1 Definitions;
  465.2 Fake or false consumer reviews, consumer testimonials, or celebrity testimonials;
  465.3 [Reserved]; 465.4 Buying positive or negative consumer reviews; 465.5 Insider consumer
  reviews and consumer testimonials; 465.6 Company-controlled review websites or entities;
  465.7 Review suppression; 465.8 Misuse of fake indicators of social media influence;
  465.9 Severability.
- L78 AUTHORITY; L79 SOURCE.
- Section ranges: § 465.1 L81-L129 | § 465.2 L131-L178 | § 465.3 [Reserved] L180 | § 465.4
  L182-L185 | § 465.5 L187-L211 | § 465.6 L212-L217 | § 465.7 L218-L242 | § 465.8 L244-L251 |
  § 465.9 L253-L255.
- Part 465 ends at L255, the last text line of the file (L257 is a separator). Nothing follows it.

### Entities and aliases
- "business" (defined, L83); "officers, managers, employees, or agents" (§ 465.2(c) L163,
  § 465.5(b)(1) L191); "immediate relatives" (L163, L201-L203); "purchasers" in the
  generalized-solicitation exceptions (L176, L198, L211).
- "anyone" is the actor in § 465.7(a) (L223) and § 465.8 (L247). "a business" is the actor in
  § 465.2, 465.4, 465.6 and 465.7(b). "an officer or manager" is the actor in § 465.5(a) and (c).
- "seller" appears only in § 465.7(b)(2) (L240) and is undefined there; the paragraph's actor is
  "a business" (L227).
- No agency is named in Part 465. "the Commission" appears only at L31 (Part 463).

### Operative definitions: § 465.1 (a)-(p), 16 lettered terms; the last, (p), is at L127-L129
- (a) L83 Business: "an individual who sells products or services, a partnership that sells
  products or services, a cor-poration that sells products or services, or any other commercial
  entity that sells products or services."
- (b) L84 Celebrity testimonial: "an ad-vertising or promotional message (including verbal
  statements, demonstrations, or depictions of the name, signature, likeness, or other
  identifying personal characteristics of an individual) that consumers are likely to believe
  re-flects the opinions, beliefs, or experiences of a well-known individual who purchased, used,
  or otherwise had experience with a product, service, or business."
- (c) L86-L100 Clear and conspicuous: "a required disclosure is easily noticeable (i.e., difficult
  to miss) and easily understandable by ordinary consumers, including in all of the following
  ways:". There are eight numbered ways:
  - (1) L87: same means as the communication; for visual-plus-audible communications, "at least
    the same means as the representation(s) requiring the disclosure".
  - (2) L89: a visual disclosure "must stand out".
  - (3) L91: an audible disclosure needs "a volume, speed, and ca-dence sufficient".
  - (4) L93: "In any communication using an interactive electronic medium, such as social media or
    the internet, the disclosure must be unavoidable. A disclosure is not clear and conspicuous if
    a consumer must take any action, such as clicking on a hyperlink or hovering over an icon, to
    see it."
  - (5) L95: understandable diction and syntax, and "each language in which the representation
    that requires the disclosure appears".
  - (6) L96: each medium, "including all electronic devices and face-to-face communications".
  - (7) L98: not contradicted or mitigated.
  - (8) L100: a specific audience, "such as children, the elderly, or the terminally ill".
- (d) L101 Consumer review: "a consumer's evaluation, or a purported consumer's evaluation, of a
  product, service, or business that is submitted by the consumer or purported consumer and that
  is published to a website or platform dedicated in whole or in part to receiving and displaying
  such eval-uations. For the purposes of this part, consumer reviews include consumer ratings
  regardless of whether they include any text or narrative."
- (e) L102 Consumer review hosting: "providing the technological means by which a website or
  platform enables consumers to see or hear the consumer reviews that consumers have submitted to
  the website or platform."
- (f) L103-L107 Consumer testimonial: built like (b), but "of a consumer who has purchased, used,
  or otherwise had experience with a product, service, or business." It spans the L105 separator.
- (g) L109 Distribute fake indicators of social media influence: "the distribution of fake
  indicators of social media influence to individuals or businesses who could use the indicators
  to misrepresent their influence."
- (h) L111 Fake indicators of social media influence: "indicators of social media influence
  generated by bots, purported individual accounts not associated with a real individual,
  accounts created with a real individual's personal information without their consent, or
  hijacked accounts, or that otherwise do not reflect a real individual's or entity's activities,
  opinions, findings, or experiences."
- (i) L113: "Immediate Relative means a spouse, parent, child, or sibling." (4 relations)
- (j) L115 Indicators of social media influence: "any metrics used by the public to make
  assessments of an individual's or entity's social media influence, such as followers, friends,
  connections, sub-scribers, views, plays, likes, saves, shares, reposts, and comments."
  (11 example metrics; the last is "comments")
- (k) L117 Manager: "an employee of a business who supervises other employees or agents and who
  either holds the title of a 'manager' or otherwise serves in a managerial role."
- (l) L118: "Officers include owners, execu-tives, and managing members of a business."
- (m) L120 Purchase a consumer review: "to provide something of value, such as money, gift
  certificates, products, services, discounts, coupons, contest en-tries, or another review, in
  exchange for a consumer review." (8 example things of value; the last is "another review")
- (n) L122-L124: "Reviewer means the author or pur-ported author of a consumer review." (split
  over a blank line)
- (o) L125 Testimonialist: "the individual giving or purportedly giving a consumer testimonial or
  celebrity testimonial."
- (p) L127-L129 Unfounded or groundless legal threat: "a legal threat based on claims, defenses,
  or other legal contentions un-warranted by existing law or based on factual contentions that
  have no evidentiary support or will likely have no evidentiary support after a reasonable
  opportunity for further investigation or discovery."

### Operative rules, actors, knowledge standards and carve-outs
Each of § 465.2, 465.4, 465.5, 465.6, 465.7 and 465.8 opens "It is an unfair or deceptive act or
practice and a violation of this part ...".
- § 465.2(a) L132-L147. A business may not "write, create, or sell a consumer [review, consumer]
  testimonial, or celebrity testimonial that materially misrepresents, expressly or by
  implication:" (1) that the reviewer or testimonialist exists; (2) that they used or otherwise had
  experience; (3) "The reviewer's or testimonialist's experience". No knowledge standard applies.
  - Layout defect: "review, consumer" (L134), "or" (L136) and "reviewer" (L138, L145) sit on
    their own lines, so items (1)-(2) read "That testimonialist exists;" (L141) and "That
    testimonialist used ..." (L143). The original has the same defect.
- § 465.2(b) L149-L161. A business may not "purchase a consumer review, or ... disseminate or cause
  the dissemination of a consumer testimonial or celebrity testimonial, about the business or one
  of the products or services it sells, which the business knew or should have known materially
  misrepresented ...". The same three items follow, with the same displaced "reviewer"/"or"
  fragments (L155-L159).
- § 465.2(c) L163-L170. A business may not "procure a consumer review from its officers, managers,
  employees, or agents, or any of their immediate relatives, for posting on a third-party
  platform or website, when the review is about the business ... and when the business knew or
  should have known that the review materially misrepresented". Items (1)-(3) at L167-L170 are
  clean text; the paragraph spans the L165 separator.
- § 465.2(d) L172-L178 is a carve-out for (b) and (c) only, not (a): "However, paragraphs (b) and
  (c) of this section do not apply to: (1) Reviews or testimonials that re-sulted from a business
  making generalized solicitations to purchasers to post reviews or testimonials about their
  experiences with the product, service, or business; or (2) Reviews that appear on a website or
  platform as a result of the business merely engaging in consumer review hosting."
- § 465.3 [Reserved] L180.
- § 465.4 L185. A business may not "provide compensation or other incentives in exchange for, or
  conditioned expressly or by implication on, the writing or creation of consumer reviews
  expressing a particular sentiment, whether positive or negative, regarding the product, service,
  or business that is the subject of the review." It has no carve-out and no knowledge standard.
- § 465.5(a) L190. An officer or manager may not write or create a review or testimonial about the
  business that lacks "a clear and conspicuous disclosure of the officer's or manager's material
  relationship to the business, unless, in the case of a consumer testimonial, the relationship is
  otherwise clear to the audience." The "otherwise clear" exception covers testimonials only.
- § 465.5(b)(1) L191-L195. A business may not disseminate a consumer testimonial by "one of its
  officers, managers, employees, or agents" without a clear and conspicuous disclosure, "when the
  relationship is not otherwise clear to the audience and the business knew or should have known
  the testimonialist's relationship to the business." The text is garbled at L193-L195 ("of" /
  "the disclosure conspicuous testimonialist's"), as in the original.
- § 465.5(b)(2) L197-L199: "(b)(1) of this section does not apply to: (i) Generalized solicitations
  to purchasers for them to post testimonials ..., or (ii) Merely engaging in consumer review
  hosting."
- § 465.5(c)(1) L201-L209. The provision applies when an officer or manager solicits or demands a
  review from "any of their immediate relatives or from any employee or agent of the business", or
  asks employees or agents to seek reviews from their relatives, and two conditions hold:
  - (i) the result is a review "without a disclosure of the reviewer's material relationship to
    the business", and
  - (ii) the officer or manager:
    - (A) "Encouraged the prospective reviewer not to make such a disclosure",
    - (B) "Did not instruct that prospective reviewers disclose clearly and con-spicuously their
      relationship to the business", or
    - (C) "knew or should have known that such a review appeared without such a disclosure and
      failed to take remedial steps" (the last item, L209).
- § 465.5(c)(2) L211: "(c)(1) of this section does not apply to generalized solicitations to
  purchasers for them to post reviews about their experiences". (c)(2) has no hosting carve-out.
- § 465.6 L213-L217. A business may not "materially misrepresent, expressly or by implication,
  that a website, organization, or entity that it controls, owns, or operates provides independent
  reviews or opinions, other than consumer reviews, about a category of businesses, products, or
  services including the business or one or more of the products or services it sells." The
  section spans the L215 separator.
- § 465.7(a) L223-L226 (actor "anyone"). Prohibited: "to use an unfounded or groundless legal
  threat, a physical threat, intimidation, or a public false accusation in response to a consumer
  review that is made with the knowl-edge that the accusation was false or made with reckless
  disregard as to its truth or falsity, in an attempt to: (1) Prevent a review or any portion
  thereof from being written or created, or (2) Cause a review or any portion thereof to be
  removed, whether or not that review or a portion thereof is re-placed with other content".
- § 465.7(b) L227-L242 (actor "a business"). Prohibited: misrepresenting that displayed reviews
  "represent most or all the reviews submitted to the website or platform when reviews are being
  sup-pressed (i.e., not displayable) based upon their ratings or their negative sentiment."
  - Carve-out: "a review is not considered sup-pressed based upon rating or negative sentiment if
    the suppression occurs based on criteria for withholding reviews that are applied equally to
    all reviews submitted without regard to sentiment, such as when:"
    - (1) the review contains:
      - (i) "Trade secrets or privileged or con-fidential commercial or financial information"
        (L231)
      - (ii) "Defamatory, harassing, abusive, obscene, vulgar, or sexually explicit content"
        (L233)
      - (iii) "The personal information or likeness of another individual" (L235)
      - (iv) "Content that is discriminatory with respect to race, gender, sexuality, ethnicity,
        or another intrinsic char-acteristic" (L236)
      - (v) "Content that is clearly false or misleading" (L238)
    - (2) "The seller reasonably believes the review is fake" (L240)
    - (3) "The review is wholly unrelated to the products or services offered by or available at
      the website or platform." (L242, the last ground)
  - That gives 3 numbered grounds and 7 leaf grounds. "such as when" makes the list illustrative.
- § 465.8 L247-L251 (actor "anyone"): "(a) Sell or distribute fake indicators of social media
  influence that they knew or should have known to be fake and that can be used by individuals or
  businesses to materially misrepresent their influence or importance for a commercial purpose; or
  (b) Purchase or procure fake indicators of social media influence that they knew or should have
  known to be fake and that materially misrepresent their influence or importance for a commercial
  purpose."
- § 465.9 Severability L255: "If any provision is stayed or determined to be invalid, the remaining
  provisions will continue in effect."
- "knew or should have known" appears at § 465.2(b) L149, § 465.2(c) L163, § 465.5(b)(1) L195,
  § 465.5(c)(1)(ii)(C) L209 and § 465.8(a)-(b) L249-L251. It is absent from § 465.2(a), § 465.4,
  § 465.5(a), § 465.6 and § 465.7(b). § 465.7(a) uses "knowl-edge that the accusation was false or
  ... reckless disregard" (L223).

### Other template fields
- Lists:
  - § 465.1: 16 terms; (c) has 8 ways; (j) 11 metrics; (m) 8 things of value; (h) 4 named
    sources plus a catch-all; (i) 4 relations; (l) 3 officer types.
  - § 465.2(a), (b) and (c): 3 items each. § 465.2(d): 2.
  - § 465.5(b)(2): 2. § 465.5(c)(1)(ii): 3.
  - § 465.7(b): 3 grounds, with 5 sub-items under (1).
  - § 465.8: 2.
- Tables: none.
- Forecasts, guidance, deadlines, effective dates: only "Aug. 22, 2024" (L79, SOURCE). The Part 463
  tail has a "twenty-four months" retention period (L15), which is not in Part 465. D01 has no
  penalty figure or monetary amount.
- Hedged claims:
  - "likely" in definitions (b) L84 and (f) L107 qualifies what consumers "are likely to believe".
    It is a definitional element, not a hedge on a prohibition.
  - (p) L127-L129 "will likely have no evidentiary support" is also definitional.
  - § 465.7(b)(2) L240 "reasonably believes".
  - § 465.7(b) L227 "such as when" introduces illustrative grounds.
  - No "may" or "could" qualifies any prohibition.
- Rounded prose beside exact figures: not applicable.
- Notes (layout defects present in the source):
  - Heading out of order at L37-L42; section list scrambled at L49-L58.
  - Displaced words in § 465.2(a)/(b) at L132-L161, and in § 465.5(b)(1) at L193-L195.
  - Headings and definitions split at separators: L122-L124, L182-L184, L244-L246.
- Amendments or contradictions: no amendment, replacement or "new" statement in D01. The two
  severability clauses in the capture are worded differently:
  - § 463.8 (L31): "it is the Commission's in-tention that the remaining provisions will continue
    in effect".
  - § 465.9 (L255): "the remaining provisions will continue in effect".
  - Part 463 also has § 463.9 Relation to State laws (L32-L35). Part 465 has no State-law section.
- Coverage: full. Read L1-L258 in one chunk; every line inspected; no unread range. The heading of
  the Part 463 fragment at L5-L11 lies outside the capture, which starts mid-sentence at L5. That is
  a capture boundary, not a gap in Part 465. Part 465 is complete from its heading (L37) to § 465.9
  (L255).

## D03 (platform Doc 2) - Consumer Reviews and Testimonials Rule: Questions and Answers (FTC staff)

- Source: docs/Consumer-Reviews-and-Testimonials-Rule-Questions-and-Answers.txt | text/D03.txt,
  308 lines | one "-----" at L307 (end of file) | no page numbers.
- Title: no title line in the text, which opens with "Tags:" (L3). The title comes from the file
  name only.
- Written or submitted by: FTC staff.
  - "Here are FTC staff answers to some questions businesses may have about the rule." (L11)
  - "Our staff guidance isn't definitive or comprehensive, and it doesn't provide a safe harbor
    from potential liability. As with many other laws and rules, the answers to some questions
    will depend on the context and the specific facts at issue." (L13)
  - Answers refer to "The Commission" in the third person (L193, L197, L205).
  - Organisations merely named: TikTok ("TikTok's Symphony Avatars", L133); the example businesses
    "John's Steakhouse" and "Jane's Arcade" (L155). Categories named: advertising agencies, public
    relations firms, review brokers and reputation management companies (L33-L35); review
    management firms (L181).
- Type, date, edition: staff Q&A guidance dated "November 2024" (L303, the last content line before
  "Return to top"). Tags (L3-L7): "Advertising and Marketing", "Endorsements, Influencers, and
  Reviews". No edition or revision note.
- Dates: the rule "went into effect on October 21, 2024" (L9); "November 2024" (L303). No other
  dates.
- Period covered: not applicable.
- Statements about the rule:
  - L9: "The Commission's Rule on the Use of Consumer Reviews and Testimonials, which went into
    effect on October 21, 2024, addresses deceptive and unfair conduct involving consumer reviews
    and testimonials. The rule authorizes courts to impose civil penalties for knowing violations".
    No penalty amount is given.
  - L57: "No, the rule does not provide a private right of action."
  - L135: "As discussed in our Federal Register notice, Section 465.2 of the rule is drafted
    specifically so as to not prohibit companies from using virtual influencers." The notice is not
    cited by number or date.

### Q&A index
65 question headings (a grep for lines ending "?" returns 65), in seven sections. Some headings
contain two questions on one line (L187, L191, L195, L199, L207, L245, L269). Format: "line, topic:
answer (provision or citation)".

General (L15-L57), 8 headings:
1. L17, consumer review vs testimonial. Definitions at L19 and L21. L23: "Most consumer reviews are
   not consumer testimonials, and most consumer testimonials are not consumer reviews. But if a
   business pays for or gives incentives for consumer reviews of its business, products, or
   services, then those incentivized reviews would also be considered consumer testimonials under
   the rule."
2. L25, individual liability: "Ordinary consumers can't be liable" (L27). Influencers in the
   business of posting testimonials "are selling celebrity testimonials and could be liable under
   Section 465.2(a)" (L29). An individual in the business of selling or creating fake reviews:
   465.2(a) (L31).
3. L33, agencies, PR firms, review brokers and reputation management companies: "Yes. These
   entities are not immune". Provisions 465.2(a), 465.4, 465.7(a) and 465.8 (L35).
4. L37, endorsements by businesses or entities: only Section 465.6 applies. "The terms 'celebrity
   testimonial' and 'consumer testimonial' in the rule do not include endorsements by business or
   other entities." (L39)
5. L41, who counts as well known: categories at L43. "whether someone is well known does not matter
   ..., because any provisions that apply to celebrity testimonials also apply to consumer
   testimonials." (L45)
6. L47, a celebrity signing autographs at a grand opening: "It is highly unlikely ... would violate
   the rule" (L49).
7. L51, influencer disclosure: "No. The rule's only disclosure requirements relate to certain
   situations involving company insiders. But failing to disclose ... could violate the FTC Act."
   (L53)
8. L55, private right of action: No (L57).

§ 465.2 (L59-L137), 19 headings:
9. L61, brokers of fake reviews: "Yes. Brokers of fake reviews would generally fall under Section
   465.2(a)'s prohibition against selling a consumer review" (L63).
10. L65, consumers paid to write honest reviews: "No." (L67)
11. L69, a retailer hosting reviews: not liable "assuming you didn't write or buy them". 465.2(d)
    (L71).
12. L73, false testimonials on the business's own website: putting testimonials on its own website
    "is disseminating them and is not merely 'hosting' them"; the business could be liable (L75).
13. L77, hosting exemption when the business solicits submissions or aggregates star ratings: yes,
    the exemption applies (L79).
14. L81, a duty to investigate hosted reviews: "There is no such requirement or obligation under the
    rule." (L83)
15. L85, when a host could be liable: if it wrote or created fake reviews, or bought reviews it knew
    or should have known were false (L87).
16. L89, sharing reviews with a third-party review platform: "Not unless the some of [sic] ...
    reviews ... your business procured from company insiders or purchased." (L91)
17. L93, routine email to every purchaser, after which an employee writes a false review: No.
    465.2(d) generalized solicitations (L95).
18. L97, hired influencers' reviews: "a hired influencer's social media post touting a product would
    be considered a celebrity testimonial, not a review". 465.2(b), knew or should have known (L99).
19. L101, knowing whether influencers tell the truth: red flags. Examples: the testimonialist gives
    a testimonial and then asks for the product; they use a competing product; the business supplies
    text without a reasonable basis (L103).
20. L105, when a business should know bought reviews are fake: there is no general duty; the
    "should have known" standard applies. Example: a third party hands out free samples. Signs of
    notice: reviews "appear so quickly after purchase", "an unusually large number of reviews appear
    in a very short period of time", "they refer to the wrong product" (L107).
21. L109, misrepresenting an opinion: "No. Section 465.2 addresses misrepresenting a reviewer's or
    testimonialist's 'experience' ... It does not address merely their 'opinion' of it." (L111)
22. L113, asking only happy customers: "The rule does not contain a specific prohibition ... But this
    practice could violate the FTC Act." 255.2(d), (e)(11) (L115).
23. L117, answers in a product Q&A section: not covered if posters were not incentivized and had no
    other connection. "Such posts are not testimonials." (L119)
24. L121, actors portraying testimonialists in a TV ad: not covered unless the underlying
    testimonials were fake; FTC Act caution. 255.1(g), 255.2(c) (L123).
25. L125, actors in a dramatized TV commercial: an obviously fictional dramatization involves no
    testimonials. Same citations (L127).
26. L129, hosting exemption for reviews featured in ads: "No. When featured in that context, consumer
    reviews become testimonials" (L131).
27. L133, AI stock avatars: "no blanket prohibition on the use of AI-generated avatars". Avatars do
    not give "consumer reviews"; use of one might be a "testimonial", prohibited only if the
    underlying testimonials were fake. Using a celebrity avatar without permission "would also
    violate the rule ... if reasonable consumers would think that the celebrity actually gave a
    testimonial" (L135-L137).

§ 465.4 (L139-L167), 7 headings:
28. L141, incentives for reviews: not prohibited "as long as there isn't an express or implied
    requirement that the reviews have to express a particular sentiment". Failing to disclose
    incentives could violate the FTC Act. 255.5(a), (b)(6)(ii) (L143).
29. L145, incentives for 5-star reviews on third-party platforms, with disclosure: "No. That conduct
    would violate Section 465.4. Note also that this section applies whether the reviews appear on
    your website or third-party review platforms." (L147)
30. L149, § 465.4 and hired influencers: "No. Section 465.4 only applies to consumer reviews. Hired
    influencers are providing testimonials" (L151).
31. L153, implied positivity. Examples: "Tell us how much you loved your visit to John's Steakhouse
    and get a $5 coupon" or "Tell your friends about all the fun you had at Jane's Arcade for a
    chance to win prizes." (L155)
32. L157, an incentive for a review merely expected to be positive: No; FTC Act caution. 255.2(d),
    (e)(11) (L159).
33. L161, paying to remove or change a review: "No, but paying consumers to change or remove
    truthful negative reviews may violate the FTC Act". 255.2(d) (L163).
34. L165, consumers accepting money for a 5-star review: "No. Section 465.4 only applies to the
    businesses that provide compensation or other incentives, not to the consumers who accept them."
    (L167)

§ 465.5 (L169-L219), 12 headings:
35. L171, insiders writing reviews with disclosures: "Yes, so long as the reviews the disclosures
    [sic] are clear and conspicuous". Caution: "if these reviews materially increase the average
    star rating of a product, the business could be violating the FTC Act even with such
    disclosures". 255.5(b)(6)(ii) (L173).
36. L175, a small business owner's family members: "Yes, but ask them to clearly and conspicuously
    disclose their relationship" (L177).
37. L179, whether "agents" in 465.5(b) covers paid influencers: "No, the term 'agents' here does not
    include influencers. The term 'agents' is meant to apply to people like representatives of
    advertising agencies, public relations firms, and review management firms." (L181)
38. L183, "otherwise clear to the audience": the audience knows the testimonialist is an executive,
    or the context shows it (an image or video of them in the company's offices or in a company
    uniform) (L185).
39. L187, an email to all recent customers, including some employees, plus an incentive to all: no
    violation, under the generalized-solicitations exemption. "The answer is the same regardless of
    whether you've offered an incentive to all recipients who post reviews." (L189)
40. L191, asking every testimonialist whether they are an agent or relative: "The Commission does
    not expect ...". Red-flag example: an image of the person in front of the company's
    headquarters (L193).
41. L195, after an officer asks employees to get reviews from relatives: "The Commission does not
    expect an officer or manager to scour every review". Red flags: a reviewer with the same last
    name as an employee ("at least applicable to smaller companies"); an employee sending the
    officer a link to the review (L197).
42. L199, "unavoidable" and hyperlinks: "'Unavoidable' is an objective standard". Quotes the
    definition (L201).
43. L203, a disclosure in a review's first line: "the Commission would consider such a disclosure
    to be unavoidable" (L205).
44. L207, hashtags and "#Ad": "Maybe." "#Ad" could work "at the beginning of a text-only post" but
    "may be too easy to miss in a video post" (L209). "The only provision for which the 'clear and
    conspicuous' definition is relevant is Section 465.5." Adequate disclosures include "my
    company's" or "my wife's company's" (L211).
45. L213, a platform's built-in disclosure tool: "Not necessarily." (L215)
46. L217, "stand out" on social media: a disclosure at the start of a text-only testimonial stands
    out; in a video it must actually be noticed (L219).

§ 465.6 (L221-L241), 5 headings:
47. L223, consumer reviews on a retail site: "No. The provision states explicitly that it does not
    apply to consumer reviews." (L225)
48. L227, whether it covers only review websites: No. It covers a "website, organization, or
    entity"; example: a "fake seal program" (L229).
49. L231, an affiliated institute's reviews: "No, so long as you are not misrepresenting" their
    independence (L233).
50. L235, an owned ranking site with an ownership disclosure: "It depends." An express claim of
    independence "can't be cured byyour [sic] contradictory disclosure"; for an implied claim, the
    net impression decides (L237).
51. L239, a media company with independent film critics and an owned studio: not misrepresenting
    (L241).

§ 465.7 (L243-L287), 11 headings:
52. L245, responding publicly to a negative review: yes. The rule prohibits a false accusation
    known to be false or made with reckless disregard, and physical threats or intimidation "to get
    the review (or a portion of it) removed or changed" (L247).
53. L249, the meaning of intimidation: "abusive communications, stalking, character assassination,
    and sexual harassment" when used to intimidate (L251).
54. L253, threatening legal action over defamation: allowed "if you have a legitimate basis".
    Paraphrases the definition (L255).
55. L257, contacting negative reviewers to resolve issues: not prohibited. Also not prohibited:
    "simply asking satisfied customers to update their reviews" (L259).
56. L261, incentives to take down negative reviews: the rule does not prohibit them, but they "could
    be an unfair practice in violation of the FTC Act". 255.2(d) (L263).
57. L265, ordering by "most helpful" votes: "Organizing reviews is not suppressing reviews under the
    rule." (L267)
58. L269, default ordering by rating with five-star reviews on top: "the rule does not cover that
    situation"; could violate Section 5 of the FTC Act (L271).
59. L273, selective use of positive reviews in marketing: the provision applies only to reviews
    "displayed in a portion of its website or platform dedicated ...". Section 5; 255.2(b) (L275).
60. L277, refusing a review about the wrong business ("patently false"): "Yes." (L279)
61. L281, a policy of not posting reviews that mention other products: "Yes, as long as your policy
    treats all such reviews equally" (L283).
62. L285, excluding reviews only about customer service: no violation if treated equally; Section 5
    caution. 255.2(e)(8)(ii) (L287).

§ 465.8 (L289-L301), 3 headings:
63. L291, a vendor secretly supplied fake followers: the provision is "limited to the purchase of
    fake indicators ... which you knew or should have known to be fake"; not liable unless there
    were red flags (L293).
64. L295, influencers asking their followers to follow the business: No, these are real people.
    Paraphrases the definition (L297).
65. L299, hiring influencers who have fake followers: "No. The provision focuses on the
    'distribution' of fake indicators" (L301).

There is no Q&A heading for § 465.1, § 465.3 or § 465.9, and no Q&A cites "465.7(b)" by number.

### Other template fields
- Entities and aliases:
  - "the rule" = "The Commission's Rule on the Use of Consumer Reviews and Testimonials" (L9).
  - "FTC staff" (L11, L53); "the Commission" (L193, L197, L205).
  - "FTC Act" (L53, L115, L123, L127, L137, L143, L159, L163, L173, L263); "Section 5 of the FTC
    Act" (L271, L275, L287).
  - "Endorsement Guides" (L9 and the citations below). A testimonial is "one type of endorsement"
    (L21).
- Cross-references to other instruments:
  - Endorsement Guides, cited "16 C.F.R 255.x" except "16 CFR" at L275 and L287:
    - 255.2(d) and (e)(11): L115, L159
    - 255.1(g) and 255.2(c): L123, L127, L137
    - 255.5(a) and (b)(6)(ii): L143
    - 255.2(d): L163, L263
    - 255.5(b)(6)(ii): L173
    - 255.2(b): L275
    - 255.2(e)(8)(ii): L287
  - Rule sections cited by number:
    - 465.2(a): L29, L31, L35, L63
    - 465.2(b): L99
    - 465.2(d): L71, L95
    - 465.2: L111, L133, L135
    - 465.4: L35, L147, L149, L151, L167
    - 465.5: L211
    - 465.5(b): L179
    - 465.6: L39, L237
    - 465.7(a): L35
    - 465.8: L35
  - Unnamed links: "You can read more about the background and content of the rule here" and "our
    other guidance on reviews and testimonials, including materials relating to our Endorsement
    Guides" (L9); "FTC staff has guidance about such disclosures" (L53). Whether these match other
    bundle documents is for the merge step; D05 and D07-D11 were not read in part 1.
- Tables: none. Lists: well-known categories (L43); red flags (L103, L107, L193, L197); 4 forms of
  intimidation (L251).
- Figures in examples: "$5 coupon" (L155); "5-star" (L145, L165); "five-star" (L269). No penalty
  amounts.
- Hedged claims (claim / hedge word / what it attaches to):
  - L13: "isn't definitive or comprehensive", "doesn't provide a safe harbor" (the guidance's status).
  - L29: "could be liable" (influencer liability, conditional on lying).
  - L49: "highly unlikely ... would violate"; "would likely not communicate" (the autograph scenario).
  - L63: "would generally fall under"; "are generally being paid" (brokers).
  - L107: "there may be clear indications"; "may trigger liability"; "would likely be on notice".
  - L137: "It's possible that a company's use of such an avatar might be considered a 'testimonial'".
  - L163: "may violate the FTC Act"; "may wind up distorting".
  - L173: "could be violating the FTC Act even with such disclosures". This attaches to the FTC Act;
    the rule answer is a firm "Yes".
  - L197: "at least applicable to smaller companies" (limits the same-last-name example).
  - L209: "Maybe"; "could work"; "may be too easy to miss" ("#Ad").
  - L215: "Not necessarily"; "may generate inadequate disclosures".
  - L237: "It depends"; "may or may not be adequate". This applies to implied claims only; the
    express-claim answer is firm.
  - L263, L271, L275: "could be"; L287: "can be deceptive".
  - Pattern: many answers give a firm rule answer followed by a hedged FTC Act caution (L115, L123,
    L127, L137, L143, L159, L163, L173, L263, L271, L275, L287). The hedge attaches to FTC Act
    exposure, not to the rule answer.
- Rounded prose: not applicable.
- Notes (typos as printed): L91 "Not unless the some of"; L159 "it needs be positive"; L173 "so long
  as the reviews the disclosures are"; L207 mismatched quotes around "#Ad"; L237 "byyour"; L261 "for
  taking take down".
- D03's restatements of D01 definitions: consumer review L19; testimonial L21; "unavoidable" L201
  (quotes § 465.1(c)(4)); unfounded legal threat L255; fake indicators L297; distribution L301.
  Wording differences are listed under Shared ground.
- Amendments or contradictions: D03 does not say it replaces or updates earlier guidance.
- Coverage: full. Read L1-L308 in one chunk; no unread range. Hyperlink targets (L9 "here") are not
  in the capture.

## D04 (platform Doc 5) - Fake reviews, CMA208: Guidance on the prohibition under paragraph 13 of Schedule 20 to the DMCC Act 2024

- Source: docs/Fake-reviews-guidance-CMA208-Competition-and-Markets.txt | text/D04.txt, 755 lines
  (last content L752) | 29 "-----" separators (29 in the original) | no printed page numbers.
- Title block (L3-L9): "Fake reviews" / "CMA208" / "Guidance on the prohibition under paragraph 13
  of Schedule 20 to the Digital Markets, Competition and Consumers Act 2024" / "4 April 2025" /
  "www.gov.uk/cma". L13: "© Crown copyright 2025". L15-L17: Open Government Licence (no version
  number) and The National Archives contact details.
- Written or submitted by: the CMA. Evidence: the document code "CMA208" (L4); "www.gov.uk/cma"
  (L9); "The CMA has published guidance ..." (fn 15, L280); "notifying the CMA" (8.26(g), L699). The
  expansion "Competition and Markets Authority" is not printed in the text, only in the file name.
  Self-references: "this Guidance" (L47, L494) and "the Guidance" (L521). Organisations merely
  named: The National Archives (L17); "the Advertising Standards Authority's Codes" (L111);
  "enforcement authorities" (L629).
- Type, date, edition: statutory guidance dated 4 April 2025 (L7). No commencement or effective
  date is printed, and there is no edition number or version history. L45: "There is a new banned
  practice relating to reviews in the Digital Markets, Competition and Consumers Act 2024 (DMCC
  Act)." It gives no date for "new".
- Period covered: not applicable.
- Contents (L21-L37), with printed page numbers. Eight chapters:
  1. Overview, 3
  2. Key concepts, 6
  3. Submitting or commissioning fake reviews and concealed incentivised reviews, 9
  4. Publishing consumer reviews in a misleading way, 12
  5. Publishing consumer review information in a misleading way, 15
  6. Offering to procure banned reviews and information for traders, 16
  7. Offering services that facilitate the submission, commissioning or publication of banned
     reviews and information, 17
  8. Prevention and removal of banned reviews and false or misleading consumer review information,
     18
  - Derived check (not printed): if the page after the contents separator (L39) is counted as p3,
    every chapter heading falls on its listed page, and the last page (L742-L753) would be p28.
- Chapter and paragraph ranges:
  - Ch1 L41-L113: 1.1 L43-L47; 1.2 L49-L59; 1.3 L61-L63; Figure 1 L71-L101; heading "Interaction
    with other provisions in the UCP and other legislation" L103; 1.4 L105-L111.
  - Ch2 L117-L207: 2.1 L119-L121 through 2.12 L201-L205.
  - Ch3 L211-L313: 3.1-3.5 L217-L256; example boxes L258-L301; 3.6 L305; 3.7 L307-L313.
  - Ch4 L317-L396: 4.1-4.10.
  - Ch5 L400-L414: 5.1.
  - Ch6 L418-L434: 6.1, examples L426-L432.
  - Ch7 L438-L455: 7.1, examples L446-L452.
  - Ch8 L459-L752: 8.1-8.32. Subheadings: Prevention and removal policy L523; Assessing the risks
    L547; Detection L599; Investigation L635; Response L665; Internal evaluations L703; What is
    reasonable and proportionate in a given context L707.
- Paragraph-number layout: these numbers sit on their own line, apart from their text: 1.1 L43,
  1.2 L49, 1.3 L61, 1.4 L105, 2.1 L119, 2.4 L131, 2.6 L141, 2.8 L156, 3.2 L225, 3.7 L307, 4.8 L378,
  4.9 L387, 4.10 L394, 6.1 L422, 7.1 L442, 8.8 L519, 8.16 L581, 8.21 L642, 8.22 L647, 8.23 L659 and
  8.30 L715.
  - At L463-L469, the numbers 8.1, 8.2, 8.3 and 8.4 are stacked, followed by four paragraphs
    (L471, L473, L475, L477). In order: 8.1 = "Traders have to take such reasonable and
    proportionate steps ..." (L471); 8.2 = the "positive" obligation (L473); 8.3 = "'Publishers' in
    this context ..." (L475); 8.4 = "There is unlikely to be a 'one size fits all' ..." (L477). This
    alignment is by order; the numbers are not printed beside the text.

### Footnotes 1-25
Each footnote sits at the foot of its page, before a separator.
- 1 L65: para 13(1) of Sch 20. 2 L66: para 13(2) and 13(3). 3 L67: para 13(4).
- 4 L113: may also infringe practice 12 of Sch 20 (paid editorial content without making that
  clear) and practice 25 (falsely claiming not to act for business purposes, or falsely
  representing oneself as a consumer), "or could, for example, give rise to a misleading action or
  omission under section 226 or section 227 of the DMCC Act".
- 5 L145: para 13(5)(a). "'Transactional decision' is defined in section 245 of the DMCC Act". Also:
  "There does not need to be an actual transaction between the consumer and trader for there to be
  a transactional decision".
- 6 L146: para 13(5)(b). 7 L180: para 13(5)(c).
- 8 L181: "Note that offering the chance to earn a reward which does not guarantee a direct benefit
  for the reviewer (for example, traders may encourage consumers to leave reviews by telling them
  that they will be entered into a prize draw) is unlikely to amount to commissioning in the context
  of the banned practice."
- 9 L207: para 13(5)(d). 10 L241: para 13(1). 11 L242: para 13(5)(e).
- 12 L243: 'closed systems', "where only a confirmed buyer or user of the product is able to submit a
  review". Such a site "sends out emails to all customers inviting them to submit feedback".
- 13 L244: para 13(5)(g).
- 14 L245: banned practices 12 and 25; "The UCP provisions are not mutually exclusive."
- 15 L280-L281: the CMA's labelling guidance, "Hidden ads: Being clear with your audience - GOV.UK and
  Hidden ads: Principles for social media platforms - GOV.UK." These titles are to be matched against
  other bundle documents at merge.
- 16 L351: para 13(2) and (5)(i). 17 L352: para 13(5)(i). 18 L382: para 13(5)(i)(iii).
- 19 L383: "See Chapter 3 above." 20 L414: para 13(2). 21 L434: para 13(4)(a). 22 L454: para
  13(4)(b).
- 23 L455: "Paragraph 1351 DMCC Act explanatory notes." 24 L487: para 13(3).
- 25 L488: para 13(5)(h). "The use of the term 'publisher' is not intended to have any impact on other
  areas of law where it is defined more specifically, such as the Defamation Act 2013."
- Footnote markers are fused into the text: "Chapter 3,1" L55; "Chapter 8,2" L57; "Chapter 7.3" L59
  (Chapter 7 plus fn 3, although it reads like "7.3"); "reviewer12" L229; "means.13,14" L235;
  "reviews15" L270.
- Sub-paragraphs of para 13, as mapped by the footnotes:
  - 13(1): submitting and commissioning
  - 13(2): misleading publication
  - 13(3): prevention and removal
  - 13(4): procurement; 13(4)(a) offering to procure; 13(4)(b) facilitating services
  - 13(5)(a) consumer review; (b) fake review; (c) concealed incentivised; (d) consumer review
    information; (e) submitting; (g) commissioning; (h) publisher; (i) misleading publication;
    (i)(iii) omitted circumstances
  - 13(5)(f) is not cited anywhere in D04 (checked).

### Operative definitions and shorthand (verbatim)
- L47: "This Guidance uses 'banned reviews' as a shorthand for fake reviews and concealed
  incentivised reviews. It also uses 'banned reviews and information' as a shorthand for fake
  reviews, concealed incentivised reviews and consumer reviews or consumer review information which
  is published in a misleading way. Consumer review information that is false or misleading is
  discussed separately – see Chapter 8."
- 2.4 L133: "For the purposes of the DMCC Act, a consumer review means a review of a product, a
  trader or any other matter relevant to a transactional decision.5 They are reviews that influence
  consumers' decision making. It does not have to be written by a consumer to fall within the
  definition. It is a broad concept."
- 2.5 L137-L139: "A fake review is a consumer review that purports to be, but is not, based on a
  person's genuine experience.6"
- 2.9 L162-L166: "A review conceals the fact it has been incentivised if: (a) a person has been
  commissioned to provide the review, and (b) that fact is not made apparent (whether through the
  contents of the review or otherwise).7 This would include missing, obscure or hidden disclosure of
  the fact that the review has been incentivised."
- 2.10 L168: "Commissioning can take many forms and is not limited to making monetary payments.8 It
  could include a trader requesting a member of staff to write a review of the trader's product."
- 2.11 L195-L198: "Consumer review information is information that is derived from, or is influenced
  by, consumer reviews.9 ... Examples of consumer review information include aggregated information
  in the form of overall ratings, overall summaries, review counts and rankings."
- 3.1 L217-L223: reviews are unlawful when they "(a) are fake, or (b) conceal the fact they have been
  incentivised (banned reviews)."
- 3.2 L227: "Submitting a banned review means supplying it with a view to publication.11". L235:
  "Commissioning another person to submit or write (or create by any other means) banned reviews
  includes incentivising by any means.13,14"
- Figure 1 glosses (L79-L83): Submit "(i.e. supply with a view to publication)"; Commission "(i.e.
  incentivise by any means)"; Publish "(i.e. disseminate or otherwise make available by any means)".
- 4.8 L380: "'catalogue abuse', sometimes known as review hijacking or review merging, involves
  presenting reviews of a different product as relating to the product a consumer is considering."
- 8.2 L473: "This element of the banned practice creates a 'positive' obligation, meaning it requires
  traders who publish consumer reviews or consumer review information by any means to take effective
  action to comply with the law, rather than merely refraining from a specified action."
- 8.3 L475: "'Publishers' in this context include traders who display or make available by any means
  consumer reviews or consumer review information on their own media (retailer websites, print
  publications etc.) and various intermediaries who display or make available reviews of other
  traders or their products (for example, specialist review sites, online marketplaces, search
  services, social media, trader recommendation platforms etc.).25"
- 8.32(b) L732:
  - A 'first-party publisher' is "directly responsible for obtaining, verifying and managing reviews
    and information (namely, a 'first-party publisher' such as a review website)".
  - A 'second-party publisher' "'syndicates' reviews and information (namely, a 'second-party
    publisher' such as a trader who displays on its own website ratings for its business given on a
    first-party publisher's site)".
  - "the duty to take steps to prevent and remove banned reviews and false or misleading consumer
    review information is non-delegable and applies to all traders who publish consumer reviews or
    consumer review information".
- 1.4 L111: "UCP provisions" = "other unfair commercial practices provisions contained in Chapter 1 of
  Part 4 of the DMCC Act".
- Also defined elsewhere: 'Transactional decision' (fn 5, s.245, not quoted); 'closed systems'
  (fn 12).

### Rules and scope (who is covered, prohibitions, allowances)
Overview and key concepts:
- 1.1 L45: the banned practice "sets out behaviour that is automatically unfair and illegal".
  "Traders publishing reviews must also take steps to prevent the publication of fake reviews and
  reviews where incentives are hidden, as well as information derived from reviews which is false or
  misleading."
- 1.2 L51-L59: three supply-chain practices: (a) submission and commissioning by traders (Ch3, fn 1);
  (b) publication by traders (Ch4, Ch5, Ch8, fn 2); (c) procurement by traders (Ch6, Ch7, fn 3).
- 1.4 L107: "These prohibitions are not mutually exclusive and they do not all have to be present for
  the banned practice to be infringed."
- 2.7 L152-L154: a review is not fake just because the trader dislikes it, if it reflects genuine
  experience. Nor is it fake because the experience was "not been paid for or completed by the
  reviewer": "a review of a gift purchased by a friend of the reviewer or of an experience (for
  example, a hotel stay) which was cut short because the reviewer felt unsafe can still be
  considered a genuine review."
- 2.8 L158: covers positive and negative fake reviews in any form and medium (online or analogue).

Chapter 3, submitting and commissioning:
- 3.3 L237-L249: "Anyone who engages in the commercial practice of either submitting or commissioning
  banned reviews will be in breach of the banned practice. This includes professional reviewers,
  journalists, content creators (such as bloggers, influencers, online streamers, celebrities, social
  media personalities), marketing companies, individuals acting on behalf of traders, etc." The list
  spans the L247 separator; the last named member is "individuals acting on behalf of traders".
- 3.4 L251: "While it is not prohibited per se to publish an incentivised review, many publication
  media (for example, websites, platforms etc.) do not allow incentivised reviews. Where this is the
  case, submitting an incentivised review is likely to be misleading."
- 3.5 L253-L256: the review "must be clearly identifiable as incentivised". "Usually, it will be
  necessary for the reviewer at least to label the review prominently as incentivised, namely, as an
  advert. The label should not have an ambiguous meaning or be placed where it might not be seen."
- 3.6 L305: allowed: genuine-experience reviews; "merely emailing customers generally to ask if they
  wish to provide a review, is not prohibited under the banned practice."
- 3.7 L309-L313: incentives are allowed if the trader does both: "(a) tell consumers that the review
  has been incentivised, and (b) the review must still reflect the reviewer's genuine experience."

Chapters 4-7, misleading publication, procurement and facilitation:
- 4.1 L319-L331: publishers are the reviewed trader (e.g. on its own website) or intermediaries:
  "(a) platforms (or third-party traders operating on platforms), including search engines, online
  marketplaces and social media, (b) specialist review sites, (c) trader recommendation platforms,
  (d) retailers, (e) booking agents." (5; the last, "booking agents", is at L331)
- 4.2 L333: prohibited; followed by "non-exhaustive examples".
- 4.4 L339: "While it is important to suppress fake negative reviews, suppressing genuine negative
  reviews is problematic." "Traders should not:"
  - (a) interfere with reviewers' ability and willingness to leave negative reviews:
    - (i) "through threats of harm or legal action" (L349, before the L354 separator)
    - (ii) "by preventing bona fide users from leaving reviews"
    - (iii) "by arbitrarily stopping and starting review invitations"
    - (iv) "by making an offer of dispute resolution contingent on a consumer not leaving a negative
      review etc." (L360-L362)
  - (b) "limit access to and/or the impact of negative reviews by editing, withholding or removing
    such reviews." (L364-L366)
- 4.5 L368: cherry-picking includes "encouraging just those who are satisfied to leave reviews".
- 4.6 L372: omission covers hidden incentives, a reviewer with a financial interest ("an employee or
  shareholder of the trader"), and a commercial link ("a supplier of the trader").
- 4.7 L374: "publishers must distinguish the incentivised review from other reviews".
- 4.8-4.9 L380-L390 (catalogue abuse): merging is "most likely" misleading where products differ
  materially. Shared reviews are "more likely to comply" when the experience is materially the same.
  Different-sized products made to a different quality standard: merging "could mislead consumers
  and is, therefore, less likely to comply".
- 4.10 L396: outdated genuine reviews.
- 5.1 L404-L412: (a) a star rating or review count not updated after fake reviews are removed;
  (b) review information influenced by "accepting commissions from the trader who is being reviewed
  in return for greater prominence in rankings."
- 6.1 L424: it is prohibited to offer to submit or commission banned reviews, or to offer traders
  misleading publication. "This element of the banned practice is aimed at addressing and disrupting
  the business model of acting as a broker procuring banned reviews and information."
- 7.1 L444: it is prohibited to offer facilitating services, e.g. expertise in bypassing fake review
  detection (fn 22, 23).

Chapter 8, prevention and removal:
- 8.1 L471: "Traders have to take such reasonable and proportionate steps as are necessary to prevent
  and remove from publication banned reviews and false or misleading consumer review
  information.24"
- 8.4 L477: there is no "one size fits all" or "tick box" approach.
- 8.5 L479-L485: "all publishers will need: (a) to have a clear policy ... and in addition (b) assess
  the risks ... and take such further proactive steps".
- 8.6-8.7 L492-L494: design and evaluate steps. Showing banned content "may indicate" that the
  publisher is not taking the required steps.
- Figure 2 L496-L517 (general steps): a published policy that prohibits fake reviews and sets out
  the approach to incentivised reviews and consumer review information (word order garbled at L501);
  risk assessments; develop and apply steps (detection, investigation, actions including sanctions);
  regular assessments of effectiveness. The caption (L517) follows the L515 separator.
- 8.8 L521: non-exhaustive specific steps; cross-ref "paragraphs 8.28-8.32 below".
- 8.9 L525-L527: policies prohibit fake reviews. "In either case concealed incentivised reviews must
  be prohibited." Where users have any control over how reviews are presented, "the publisher must
  make clear what is and is not permitted".
- 8.10 L529-L531: policies must be readily available and "written in plain English".
- 8.11 L533-L543: explain the difference between a review and a complaint. Publishers should not:
  "(a) try to persuade consumers to submit a complaint, rather than leave a review for publication,
  (b) try to dissuade consumers from leaving a review of their experience even if their initial
  problem has been resolved through the complaints process, (c) treat a negative review intended for
  publication as a complaint and not publish it." (the last, (c), is at L541-L543)
- 8.12-8.14 L549-L563, risk assessments: (a) assess the risks; (b) identify measures.
  - 8.13 lists sources: "(a) content or activity on the publisher's media, including by using
    technology designed to identify banned reviews ..., (b) third-party reports to the publisher, and
    (c) the findings of investigations or internal evaluations."
  - 8.14 L563: "this is not a one-off exercise". A publisher may reasonably rate the risk "as low,
    such that only limited further steps are necessary".
- 8.15 L565-L579: at a minimum, systems for (a) detection, (b) investigation and (c) actions; (c)
  follows the L575 separator.
- 8.16 L583-L595: balance. "removing a negative review that was genuinely created may mislead
  consumers as much as publishing a fake positive review". The measures must cover (a) how reviews
  are collected and checked, (b) the basis for publishing and removing, (c) how ratings and rankings
  work.
- 8.17 L597: before and after publication.
- 8.18-8.19 L601-L631, detection:
  - (a)(i) clear rules for who can submit (L609-L613): "Publishers should not prevent users from
    leaving reviews merely because they have not bought the relevant product themselves (for
    example, where it is received as a gift)."
  - (a)(ii) vetting traders before they join a trader recommendation platform.
  - (b)(i) records of submission history and profiles; (b)(ii) manual checks.
  - (b)(iii) automated software. Anomaly examples (L625): "reviews written by different reviewers
    from the same email or IP address, networks of reviewers reviewing the same products or
    businesses, average review length, a spike in highly positive or negative reviews over a short
    period of time etc". A third-party provider is an option.
  - (c)(i) publicly accessible reporting, including by "enforcement authorities"; (c)(ii) letting
    users see a reviewer's public review history.
  - L631: "publishers should not rely on users (especially consumers) to police ..." and "The
    publisher is ultimately responsible".
- 8.20-8.23 L637-L661, investigation: a process is required; cross-ref "see paragraph 2.6" (L645);
  8.22 (a)-(c) timeliness; 8.23 temporary measures, and keeping suspicious reviews out of ratings in
  the interim.
- 8.24-8.26 L667-L701, response:
  - 8.24: (a) remove; (b) correct "published review counts, overall ratings, rankings and
    AI-generated review summaries" (L673).
  - 8.25: sanction the sources: "those who submit, commission, procure or facilitate".
  - 8.26: sanctions "may include" (7; the last, (g), is at L699-L701):
    - (a) suspending or revoking privileges
    - (b) "clear and prominent warnings on the pages of traders"
    - (c) banning user accounts and preventing new accounts
    - (d) removing from public view all published reviews for traders who submitted or benefited
      [L691 separator]
    - (e) terminating trader recommendation platform memberships or contracts
    - (f) keeping records so sanctions can escalate
    - (g) "notifying the CMA of breaches of the banned practice where these are systematic by one
      trader."
- 8.27 L705: regular effectiveness assessments.
- 8.28 L709-L711: reasonable and proportionate steps, because "consumer reviews originate from third
  parties and the publisher may therefore make such banned reviews ... available inadvertently."
- 8.29-8.30 L713-L721: an outcomes-focused approach. Higher risks "(whether by seriousness or by
  volume)" need more extensive measures (spans the L719 separator).
- 8.31 L723: "Publishers cannot avoid implementing effective prevention and removal steps solely due
  to the (lack of) resources and capabilities available to them. Even a small trader publishing only
  reviews from their own customers or a nascent platform which presently enables a relatively small
  number of users to upload consumer reviews directly is required to implement reasonable and
  proportionate measures where their content poses a risk."
- 8.32 L725-L752, considerations (a)-(f) (6; (f) at L752 is the document's last content line):
  - (a) business model: a search platform vs a website of its own customers' reviews, where there is
    "direct proof of a purchase or genuine experience".
  - (b) source: the non-delegable duty; first-party vs second-party publisher. (b)(i): first-party
    steps "may differ from, and be more significant than" second-party steps. (b)(ii): a second-party
    publisher relying on first-party policies must be satisfied "on reasonable grounds".
    [L740 separator]
  - (c) functionality: merging reviews, creating 'variants', recycling reviews, "catalogue abuse".
  - (d) type of content: endorsements and trustworthiness.
  - (e) potential impact: "while size is not determinative".
  - (f) "any additional risk (including the risk of harm to other traders) stemming from the impact
    or potential impact of banned reviews on aggregated consumer review information."

### Numbered examples (example boxes)
Numbers are printed but sometimes separated from the text. 15 numbered examples in total
(2 + 2 + 6 + 3 + 2).
- "Submitting fake reviews" (L260-L268; numbers detached at L262-L264):
  1. (L266) stating that a product or trader met expectations when it did not, or when the reviewer
     had not used it.
  2. (L268) a video demonstrating results while actually using a different product.
- "Submitting concealed incentivised reviews15" (L270-L278; numbers detached at L272-L274):
  1. (L276) no disclosure of a commercial relationship or of free products.
  2. (L278) a positive review that does not reveal the product was free "unless they click on a link
     labelled 'learn more' in the review."
- "Commissioning fake reviews or concealed incentivised reviews" (L285-L301):
  1. (L287) a free or discounted product "in exchange for a five-star review (which is not
     reflective of their genuine experience)".
  2. (L289) asking for a review of a free or discounted product without making clear the reviewer
     must disclose, e.g. by "labelling their review as an advertisement".
  3. (L291-L293) a social media post "asking for five-star reviews in exchange for free products".
  4. (L295) a refund and/or a gift card in return for changing a negative review.
  5. (L297-L299) customers buy with their own money and are "reimbursed once they have submitted a
     positive review".
  6. (L301, the last) "Buying reviews which look like they have been written by individual consumers
     but have in fact been generated by software applications (such as bots)."
- Ch6 examples (L426-L432):
  1. social media groups that recruit fake or concealed-incentive reviewers.
  2. (L430) "Selling reviews which look like they have been written by individual consumers but have
     in fact been generated by software applications (such as bots)."
  3. (L432) an SEO service that promises a better rating by means that include fake reviews.
- Ch7 examples (L446-L452):
  1. setting up accounts so as to avoid detection.
  2. (L452) running a platform "while being aware of and allowing services to be sold ... to offer to
     post or otherwise arrange for fake reviews or concealed incentivised to be posted on other
     sites" (the word "reviews" is missing as printed).
- Commissioning example 6 (buying bot reviews, L301) and Ch6 example 2 (selling them, L430) are
  worded in parallel.

### Other template fields
- Other enumerated lists:
  - 2.10 commissioning examples "include, but are not limited to" (7; (e)-(g) are on the next page,
    and the last, (g), is at L191):
    - (a) money
    - (b) commissions
    - (c) discounts or vouchers
    - (d) leases or loans free of charge or on more favourable terms
    - [L183 separator] (e) products given free of charge ('freebies')
    - (f) free stays
    - (g) invitations to events etc.
  - 2.11: 4 aggregated forms (L198).
  - 2.12: (a) published misleadingly, see Ch5; (b) false or misleading, see Ch8.
- Figures: no money amounts or durations; only "five-star" (L287, L291). No penalty amounts or
  penalty provisions in D04.
- Tables: none. Figures 1 and 2 are diagrams rendered as text.
- Hedged claims (claim / hedge / what it attaches to):
  - 2.4 L133: "are likely to include opinions about the product" (illustrates scope).
  - 2.6 L143: "Fake reviews could be positive or negative"; "often".
  - fn 8 L181: "unlikely to amount to commissioning" (prize draws).
  - 3.4 L251: "likely to be misleading". This attaches to submitting incentivised reviews where the
    medium disallows them; publishing an incentivised review is "not prohibited per se".
  - 3.5 L255: "Usually, it will be necessary ... to label". This attaches to the labelling method;
    "must be clearly identifiable" is firm.
  - 4.3 L337: "may infringe". 4.5: "might be done".
  - 4.6 L372: "may be misleading", then the firm "It will include a situation where the reviewer has
    a financial interest".
  - 4.8-4.9: "most likely", "more likely to comply", "could mislead ... less likely to comply".
  - 4.10: "might reasonably remain", "might need to change".
  - 8.4 L477: "unlikely to be a 'one size fits all'".
  - 8.7 L494: "may indicate"; "likely to constitute reasonable steps".
  - 8.14 L563: "it is possible that a publisher may reasonably identify the risk ... as low".
  - 8.26 L677: "It may be appropriate for escalating sanctions"; the sanctions list "may include".
  - 8.32(a) and (b)(i): "may differ from, and be more significant than". 8.32(e): "while size is not
    determinative ... may pose higher risks".
  - Firm "must" statements: 3.5 "must be clearly identifiable"; 4.7 "publishers must distinguish";
    8.9 "concealed incentivised reviews must be prohibited" and "the publisher must make clear";
    8.18 "Publishers must take proactive steps"; 8.20 "Publishers must have a process"; 8.24 "must
    take steps"; 8.30 "must take".
- Rounded prose: not applicable.
- Notes: typo "An short overview" (L473); Ch7 example 2 is missing "reviews" (L452); Figure 2 has
  stray bullets "-" at L496 and L498.
- Cross-references to other instruments and documents:
  - DMCC Act Sch 20 para 13 (title L6, and the footnotes).
  - Practices 12 and 25 of Sch 20 (fn 4, fn 14); ss.226, 227 and 245 DMCC Act (fn 4, fn 5); Chapter 1
    of Part 4 DMCC Act (L111).
  - Fraud Act 2006 and ASA Codes (L111); DMCC Act explanatory notes para 1351 (fn 23); Defamation Act
    2013 (fn 25).
  - The CMA's "Hidden ads: Being clear with your audience" and "Hidden ads: Principles for social
    media platforms" (fn 15).
  - "the summary note that can be accessed here" (L473; the link target is not captured).
  - Internal cross-refs: 8.28-8.32 (L521); 2.6 (L645); Chapter 3 (fn 19); Chapters 3, 4/5/8 and 6/7
    (L53-L59); Chapter 8 (L47).
- Amendments or contradictions: the only change statement is "new banned practice" (L45). D04 does
  not say it replaces earlier guidance. Two related internal passages: 4.4 (L339) calls suppressing
  fake negative reviews "important"; 8.16 (L583) says removing a genuine negative review "may mislead
  consumers as much as publishing a fake positive review".
- Coverage: full. Read in five chunks: L1-L120, L120-L279, L279-L438, L438-L597 and L597-L755. Every
  line inspected; no unread range. Link targets (L473 "accessed here"; the GOV.UK titles in fn 15)
  are not in the capture. The diagrams exist only as text.

## D06 (platform Doc 6) - Short guide for businesses publishing consumer reviews and complying with consumer protection law

- Source: docs/Short-guide-for-businesses-publishing-consumer-reviews-and.txt | text/D06.txt, 154
  lines | no separators, no page numbers.
- Title: not printed in the body. It comes from the URL slug at L11
  ("https://www.gov.uk/government/publications/fake-reviews/short-guide-for-businesses-publishing-consumer-reviews-and-complying-with-consumer-protection-law")
  and from the file name. L3 is a stray "-".
- Written or submitted by: not named. Evidence: "© Crown copyright 2025" (L5); "Where we have
  identified any third party copyright information ..." (L9); the gov.uk publication URL (L11). The
  string "CMA" does not occur in D06 (checked). Licence: "Open Government Licence v3.0" (L7).
- Type, date, edition: short summary guidance. L13: "This summary is for businesses who publish
  consumer reviews or review information. It explains what you need to do to comply with your legal
  obligations." The only date is the copyright year 2025 (L5). No day or month, effective date or
  edition.
- Period covered: not applicable.
- Headings: What fake reviews look like L17; Who this guidance applies to L37; Preventing and
  removing banned content L61; Steps publishers need to take L71; Policies you must publish L99;
  Completing a risk assessment L103; Processes you must have in place L123; Deciding what is
  reasonable for your circumstances L135.
- Scope statement and cross-references:
  - L15: "There are other things businesses must not do (such as writing or commissioning others to
    write fake reviews). These are further explained in the full fake reviews guidance where you can
    also find lots of examples."
  - L85: "a fuller list of sanctions is published in the full guidance".
  - The full guidance is not named by code or date.

### Definitions and descriptions (verbatim)
- L19-L25: reviews "might look like" (3 forms):
  - text ("a written blog or a comment posted under a product listing on a website")
  - speech ("a verbal opinion expressed in a video on a sharing platform")
  - graphic representations ("a star rating appearing next to a restaurant's name in search engine
    results, or a thumbs up next to a 'helpful' review")
- L27: "Information derived from or influenced by consumer reviews (consumer review information) is
  aggregated information in the form of overall ratings, review summaries, review counts and
  rankings."
- Deceptive types (3; the last is false or misleading consumer review information):
  - L31: "fake reviews: these are reviews that look or claim to be genuine, but are actually fake"
  - L33: "concealed incentivised reviews: these are reviews that conceal the fact that they have been
    incentivised (for example, not making it clear that a review has been written in exchange for
    money or other benefits, like a free stay at a hotel or another 'freebie')"
  - L35: "false or misleading consumer review information: this includes aggregated information (when
    information is gathered from lots of individual reviews to give one overall score or rating) that
    is based on fake reviews"
- L65: "banned content (namely fake reviews, concealed incentivised reviews and false or misleading
  consumer review information)".

### Who is covered, and responsibility
- L39-L43: applies to a trader who publishes consumer reviews or consumer review information
  "including about other traders and their products", and "from any source, including if you publish
  consumer reviews or consumer review information originally collated by someone else" (2 bullets).
- L45-L59: "You are responsible for any publication formats you operate. These might include:"
  websites, social media, search services, online marketplaces, specialist review sites, trader
  recommendation platforms, print publications (7; the last, "print publications", is at L59).
- L63: "The law on fake reviews applies to all traders who publish consumer reviews or consumer review
  information. But what you need to do in practice depends on factors such as the source of the
  reviews, the volume of reviews you publish and the risk of fake reviews being contributed."
- L65: "Each individual trader who publishes reviews and review information is responsible for
  preventing and taking steps to remove banned content".
- L67: "If a third party also provides access to these reviews or information, they are also
  responsible and must take steps to comply with the law."
- L69: "You can make agreements with a third party to monitor reviews and information, but you are
  still responsible for taking your own steps to prevent and remove banned content."

### Steps (lists)
- L73: reasonable and proportionate steps to prevent and remove the three banned types. L75: your own
  procedures. L77: "You should have a published policy that clearly prohibits fake reviews. Your
  policy should also state your approach to incentivised reviews and consumer review information."
- L79-L85: "there are several steps you will likely need to take to:" (3) detect; investigate; take
  action. The third adds: "This could include imposing sanctions where appropriate (for example,
  putting clear warnings on pages or banning users: a fuller list of sanctions is published in the
  full guidance)".
- L89-L97: "You will need to consider:" (4) policies you must publish; completing a risk assessment;
  processes you must have in place; deciding what is reasonable for your circumstances. Each is a
  later heading.
- L101: traders "should publish policies which clearly prohibit fake reviews" (the heading says
  "must"; the body says "should").
- L105: "You must assess the risk of banned content being published in content you control."
- L107-L119: the risk assessment should (3 bullets, 3 sub-bullets; the last is findings, L119):
  - assess the risks
  - identify measures
  - consider evidence "including, but not limited to:"
    - your own identification procedures
    - concerns flagged up to you by users and others
    - findings of investigations or internal evaluations that you carry out
- L121: "Assessing the risk is not a one-off exercise: you should do so regularly, and especially if
  you are planning to make any changes to the way you operate that might increase the risk of banned
  information appearing."
- L125-L131: processes "you must design" (3): detect and prevent; investigate suspected cases; take
  actions that remove the content and "reduce the risk of it reappearing".
- L133: regularly assess effectiveness and respond to emerging risks.
- L141-L153: factors (6; the last, L153, is the document's final line):
  - "the incentives and opportunities people have for posting fake content in the particular area you
    operate in"
  - "the source of the consumer reviews or consumer review information that you publish, such as
    whether users can publish directly on your site, or if they are first published on a site
    controlled by someone else"
  - "the functionality you have on your site for sharing or promoting reviews"
  - "the type of content you show to consumers"
  - "the potential impact of the activity on the traders being reviewed"
  - "any additional risks resulting from the impact or potential impact of banned reviews on
    aggregated consumer review information"

### Other template fields
- Tables: none. Footnotes: none. Figures or amounts: none.
- Hedged claims:
  - L19 "might look like"; L29 "might see"; L45 "These might include" (the formats list is
    illustrative).
  - L79 "you will likely need to take". This attaches to the need for the detect, investigate and act
    steps; L125 then says "you must design processes" for the same three functions.
  - L85 "could include imposing sanctions"; L121 "might increase the risk".
- Rounded prose: not applicable.
- Notes, modal verbs:
  - "must" at L15, L67, L91, L95, L99, L105, L123, L125.
  - "should" at L75, L77, L101, L107, L121, L133, L137.
  - "need to" at L13, L63, L71, L73, L79, L87, L89, L139. L9 "need to obtain permission" is licence
    text.
- Amendments or contradictions: none stated. Two internal wording shifts: the heading "Policies you
  must publish" (L99) vs the body "should publish policies" (L101); and L79 "will likely need to take"
  vs L125 "you must design processes".
- Coverage: full. Read L1-L154 in one chunk; no unread range. The link target of "the full fake
  reviews guidance" (L15) is not in the capture.

## Shared ground (navigation only; part 1 documents)

### US pair: D01 (rule) and D03 (staff Q&A)
- Same instrument: D03 L9 "The Commission's Rule on the Use of Consumer Reviews and Testimonials" is
  the D01 Part 465 heading (L37-L42, words out of order). D03 cites D01 sections by number (listed
  above), never § 465.1, § 465.3 or § 465.9.
- Dates:
  - D01 SOURCE "89 FR 68077, Aug. 22, 2024" (L79).
  - D03 effective date "October 21, 2024" (L9) and document date "November 2024" (L303).
  - D03's "our Federal Register notice" (L135) has no citation or date. In part 1, only D03 L9 gives
    an effective date.
- Penalties and remedies: D03 L9 "authorizes courts to impose civil penalties for knowing
  violations"; D03 L57: no private right of action. D01 has no penalty or remedy text.

Definitions as D03 restates them, compared with D01:
- Consumer review: D03 L19 says "submitted to and published on a website or platform dedicated in
  whole or in part to receiving and displaying such evaluations". D01 L101 says "submitted by the
  consumer or purported consumer and that is published to a website or platform ..." and adds the
  ratings sentence ("consumer reviews include consumer ratings regardless of whether they include
  any text or narrative"), which D03 L19 omits.
- Testimonial: D03 L21 says "an advertising message ... of a consumer or celebrity who has
  purchased, used, or otherwise had experience". D01 (b) L84 and (f) L103-L107 say "an advertising
  or promotional message (including verbal statements, demonstrations, or depictions of the name,
  signature, likeness ...)".
- § 465.6: D03 L39 says "that it controls"; D01 L213 says "that it controls, owns, or operates". D03
  L229 quotes "website, organization, or entity" and "provides independent reviews or opinions"
  (D01 L213-L217).
- Fake indicators: D03 L35 says "fake or false indicators"; D01 § 465.8 says "fake indicators". D03
  L297 restates D01 (h) L111, and D03 L301 restates (g) L109.
- Unfounded legal threat: D03 L255 says "legal contentions unwarranted by existing law"; D01 (p)
  L127 says "claims, defenses, or other legal contentions unwarranted by existing law".
- § 465.7(a): D03 L247 says "a false accusation about the reviewer" used "to get the review (or a
  portion of it) removed or changed". D01 L223-L226 says "a public false accusation in response to a
  consumer review", in an attempt to "(1) Prevent ... from being written or created, or (2) Cause ...
  to be removed, whether or not ... re-placed with other content".
- Exact quotes: "unavoidable" (D03 L201 = D01 (c)(4) L93, "a consumer must take any action, such as
  clicking on a hyperlink or hovering over an icon, to see"); "displayed in a portion of its website
  or platform dedicated in whole or in part to receiving and displaying consumer reviews" (D03 L275 =
  D01 L227); "otherwise clear to the audience" (D03 L183 = D01 L190, L195).
- Experience vs opinion: D03 L111 on § 465.2. D01 § 465.2 items use "experience" (L143, L147, L153,
  L161, L168, L170); D01 definitions (b) and (f) include "opinions, beliefs, or experiences" (L84,
  L107).

D03 scope-limiting statements, matched to D01 text:
- Only disclosure requirements are for insiders: D03 L53; D01 § 465.5 L187-L211.
- "clear and conspicuous" is relevant only to § 465.5: D03 L211. In D01 the term appears only in
  § 465.1(c) L86 and § 465.5 L190, L191-L195 and L207.
- Only § 465.6 covers entity endorsements: D03 L39.
- § 465.4 covers only consumer reviews: D03 L151.
- "agents" excludes influencers: D03 L181. D01 uses "agents" at L117, L163, L191 and L201-L203.
- Consumers are not liable: D03 L27, L167.
- § 465.4 applies on the business's own website or on third-party platforms: D03 L147. D01 L185 is
  silent on venue.

Exceptions, knowledge standard and suppression:
- D01 § 465.2(d) (L172-L178) is applied in D03 L71, L79, L95 and L131.
- D01 § 465.5(b)(2) and (c)(2) (L197-L199, L211) are applied in D03 L189, where an incentive offered
  to all recipients does not change the answer.
- D01's "knew or should have known" (L149, L163, L195, L209, L249-L251) is discussed in D03 L87, L99,
  L105-L107 and L293.
- D01 § 465.7(b)(1)-(3) (L227-L242) vs D03 L265-L287: ordering by helpfulness; ordering by rating;
  selective use in marketing; a wrong-business review ("patently false"); a policy on reviews that
  mention other products; excluding customer-service-only reviews; "treats all such reviews
  equally".
- Insider and relative terms: D01 (i) Immediate Relative L113, (k) Manager L117, (l) Officers L118;
  D03 L175-L177 (family members), L191-L197 (immediate relatives, officer and manager red flags).

### UK pair: D04 (CMA208) and D06 (short guide)
- How each refers to the other:
  - D04 L473: "An short overview of traders' obligations set out in this chapter can be found in the
    summary note that can be accessed here."
  - D06 L13: "This summary is for businesses who publish consumer reviews ...". D06 L15: "the full
    fake reviews guidance". D06 L85: "the full guidance".
  - Neither names the other by title, code or date. D06's URL path is
    "/government/publications/fake-reviews/" (L11); D04's title is "Fake reviews" (L3).
- Dates: D04 "4 April 2025" (L7) and "© Crown copyright 2025" (L13); D06 only "© Crown copyright
  2025" (L5).
- Review forms: D04 2.2 L125 and D06 L19-L25 give the same three forms and examples.
- Consumer review information: D04 2.11 L195-L198 says "derived from, or is influenced by" and
  "Examples ... include aggregated information in the form of overall ratings, overall summaries,
  review counts and rankings". D06 L27 says it "is aggregated information in the form of overall
  ratings, review summaries, review counts and rankings". Differences: "overall summaries" vs
  "review summaries"; "Examples ... include" vs "is".
- Fake review: D04 2.5 L137-L139 "purports to be, but is not, based on a person's genuine
  experience" vs D06 L31 "look or claim to be genuine, but are actually fake".
- Concealed incentivised reviews: D04 2.9 L162-L166 and the 2.10 examples (money L170, freebies L185,
  free stays L189) vs D06 L33 (money, a free stay at a hotel, a 'freebie').
- Shorthand terms:
  - D04 (L47): 'banned reviews' = fake + concealed incentivised. 'banned reviews and information'
    adds misleadingly published reviews or information. False or misleading consumer review
    information is "discussed separately – see Chapter 8".
  - D06 "banned content" = fake + concealed incentivised + false or misleading consumer review
    information (L65).
- Publisher media:
  - D04 8.3 L475: own media (retailer websites, print publications) and intermediaries (specialist
    review sites, online marketplaces, search services, social media, trader recommendation
    platforms).
  - D04 4.1 L319-L331: platforms including search engines, online marketplaces and social media;
    specialist review sites; trader recommendation platforms; retailers; booking agents.
  - D06 L45-L59: websites, social media, search services, online marketplaces, specialist review
    sites, trader recommendation platforms, print publications.
  - "booking agents" and "retailers" appear only in D04 4.1; "print publications" appears in D04 8.3
    and D06.
- The duty and who holds it: D04 8.1 L471, 8.28 L709-L711 and 8.32(b) L732 (non-delegable; applies
  to all traders who publish) vs D06 L63, L65, L67, L69, L73 and L87.
- Policy: D04 8.5(a) L481, 8.9 L525-L527 and 8.10 L529-L531 vs D06 L77, L101.
- Risk assessment:
  - The two aims in D04 8.12 L549-L553 match D06 L109-L111.
  - D04 8.13 sources (a)-(c) L555-L561 vs D06 sub-bullets L113-L119: the first two are worded
    differently; the third is nearly identical.
  - "not a one-off exercise" appears in D04 8.14 L563 and D06 L121. D06 adds "especially if you are
    planning to make any changes to the way you operate".
- Processes: D04 8.15 (a)-(c) L565-L579 and Figure 2 L496-L517 vs D06 L79-L85 ("will likely need")
  and L125-L131 ("must design").
- Sanctions: D04 8.26 (a)-(g) L677-L701 vs D06 L85, whose examples "putting clear warnings on pages
  or banning users" correspond to 8.26(b) L681 and (c) L685. D06 points to "a fuller list" in the
  full guidance.
- Effectiveness: D04 8.27 L705 vs D06 L133.
- Reasonable and proportionate factors: D04 8.32 (a)-(f) L729-L752 vs D06 L143-L153; both have six
  items.
  - Items 2 (source), 3 (functionality), 4 (type of content) and 6 (additional risk from aggregated
    information) correspond.
  - Item 1 differs: D04 "the publisher's business model" vs D06 "the incentives and opportunities
    people have for posting fake content in the particular area you operate in".
  - Item 5 differs: D04 "the potential impact of the trader's activity – while size is not
    determinative ..." vs D06 "the potential impact of the activity on the traders being reviewed".
  - D04 (f) includes "(including the risk of harm to other traders)"; D06's sixth item omits it.
- Exclusion facts: D06 has no section on submitting, commissioning, offering or facilitating (it
  defers these to the full guidance, L15). It has no numbered examples, footnotes or statutory
  citations, and does not mention the DMCC Act, Schedule 20 or the CMA.

### Across the US and UK documents
These are facts only. The documents belong to different legal regimes, and none states a precedence
between them.
- Prize and contest incentives: D01 (m) lists "contest en-tries" among things of value (L120). D03
  L155 uses "for a chance to win prizes" as an implied-positivity example under § 465.4. D04 fn 8
  L181 says a prize draw is "unlikely to amount to commissioning".
- General solicitations: D01 § 465.2(d)(1) L176, § 465.5(b)(2)(i) L198 and (c)(2) L211; D03 L95,
  L189; D04 3.6 L305 ("merely emailing customers generally"); D04 fn 12 L243 (a closed system emails
  all customers).
- Staff and insider reviews: D01 § 465.2(c) L163 and § 465.5 L187-L211; D03 L171-L197; D04 2.10 L168
  ("a trader requesting a member of staff to write a review") and 4.6 L372 (employee, shareholder,
  supplier).
- Threats and suppression: D01 § 465.7(a) L223-L226; D03 L245-L255; D04 4.4(a)(i) L349 ("threats of
  harm or legal action") and 4.4(b) L364-L366.
- Soliciting only satisfied customers: D03 L113-L115 (no specific rule prohibition; FTC Act
  caution); D04 4.5 L368 ("encouraging just those who are satisfied to leave reviews" counts as
  cherry-picking).
- Paying to change or remove reviews: D03 L161-L163 and L261-L263 (the rule does not prohibit it;
  FTC Act caution); D04 Commissioning example 4 L295 (a refund or gift card to change a negative
  review).
- Five-star incentives: D03 L145-L147 (violates § 465.4 even with disclosure); D04 Commissioning
  examples 1 and 3 (L287, L291).
- Bots: D01 (h) L111 (fake social media indicators generated by bots); D04 L301 (buying bot-generated
  reviews) and L430 (selling them).
- Brokers: D03 L33-L35, L61-L63; D04 6.1 L424 ("acting as a broker procuring banned reviews").
- Influencers: D03 L29, L51-L53, L97-L103, L149-L151, L179-L181, L295-L301; D04 3.3 L239 (influencers
  among content creators).
- Hosting vs publishing duties: D01 § 465.2(d)(2) L178 (hosting carve-out); D03 L81-L83 (no duty to
  investigate) and L107 (no general duty); D04 8.1-8.2 L471-L473 (positive obligation to prevent and
  remove) and 8.19(c)(ii) L631; D06 L63-L69.
- Disclosure and labelling: D01 (c) L86-L100; D03 L199-L219 (first line, "#Ad", hyperlinks, built-in
  tools); D04 2.9 L166 ("missing, obscure or hidden disclosure"), 3.5 L255 (label "as an advert") and
  Submitting example 2 L278 (a link labelled 'learn more').
- Detection red flags: D03 L107 (reviews soon after purchase; an unusually large number in a very
  short period; the wrong product); D04 8.19(b)(iii) L625 (same email or IP address; reviewer
  networks; average length; a spike over a short period).
- Ratings and aggregation: D03 L77-L79 (aggregating star ratings stays within the hosting exemption)
  and L173 (insider reviews raising the average star rating); D04 5.1(a) L408, 8.23 L661 and 8.24(b)
  L673; D06 L27, L35 and L153.
- Ordering reviews: D03 L265-L271; D04 4.10 L396 (chronological display of older reviews) and 8.16(c)
  L593-L595.
- AI: D03 L133-L137 (AI stock avatars); D04 8.24(b) L673 ("AI-generated review summaries").
- Gifts: D04 2.7 L154 (a gift bought by a friend still yields a genuine review) and 8.19(a)(i) L613
  (a product received as a gift); D01 (m) lists "gift certificates" as a thing of value (L120).
- Issuers vs organisations merely named:
  - Issuers: D01 has no issuer line ("the Commission" appears only in Part 463, L31); D03 is FTC staff
    (L11); D04 is the CMA (L4, L9, L280, L699); D06 names none (Crown copyright, gov.uk).
  - Named only: TikTok (D03 L133); John's Steakhouse and Jane's Arcade (D03 L155); The National
    Archives (D04 L17, D06 L7); the Advertising Standards Authority (D04 L111).
- Dates in part 1: Aug. 22, 2024 (D01 L79); October 21, 2024 (D03 L9); November 2024 (D03 L303);
  4 April 2025 (D04 L7); copyright 2025 (D04 L13, D06 L5).
- Edition relationships: none of the four says it amends, replaces or supersedes an earlier version.
  D04 calls the banned practice "new" (L45). D06 calls itself a summary (L13). In the D01 capture,
  Part 463's tail sits immediately before Part 465.
- Overview passages that repeat detail found elsewhere:
  - D04 Figure 1 (L71-L101) repeats 1.2 and Chapters 3-8.
  - D04 Figure 2 (L496-L517) repeats 8.5 and 8.9-8.27.
  - D06 as a whole restates D04 Chapter 8 at summary level.
  - D03's General section restates D01 definitions (L19, L21).

## Gaps (part 1)
- Unread ranges: none. Read in full: D01 L1-L258, D03 L1-L308, D04 L1-L755, D06 L1-L154.
- Not in the capture (missing source, not unread):
  - D01: the Part 463 text before L5, including the heading of the fragment at L5-L11.
  - Hyperlink targets: D03 L9 "here"; D04 L473 "accessed here"; D06 L15 "full fake reviews guidance".
  - The titles of D03 and D06 (file name or URL only), and D04's expanded issuer name.
- Unresolved (originals are text-only, with no page image): the printed reading of the garbled D01
  § 465.2(a)/(b) and § 465.5(b)(1) lines, and the D04 Figure 2 box at L500-L501.
- Not inspected in part 1: D02, D05 and D07-D11 (parts 2-4); the capture's bundle-overview text.
- Next mapping chunk for part 1: none.
