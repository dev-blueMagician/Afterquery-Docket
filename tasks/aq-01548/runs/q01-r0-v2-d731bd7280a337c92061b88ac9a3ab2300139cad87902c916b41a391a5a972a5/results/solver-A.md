# q01 rev 0 blind solver A (fresh blind-solver agent, packet solver-1), returned 2026-10-08

answer: May 31, 2012. That is the onset date his Social Security disability application gave when he moved for the TRO on March 4, 2013. He did not amend it to May 16, 2012 until March 19, 2013.

confidence: high

path:
1. **TRO date.** D02, the Memorandum Opinion of Mar. 12, 2013 (ECF 25), page 6, at text/D02.txt line 73: "The Plaintiff filed his motion for a temporary restraining order on March 4, 2013, though the Court did not receive notice of the motion until the evening of March 5, 2013."
   - The motion was against the Defendants. D02 page 1 (line 10) says the defendants are "DHA Group, Inc., David Hale, and Ami Getu (collectively 'Defendants')" and that the Plaintiff's "[20] Motion for Temporary Restraining Order ... seeks an order barring the Defendants from responding to a subpoena issued by a Virginia state court."
   - D02 is the only TRO motion in the packet.
2. **Original application.** D08, the Memorandum Opinion of Dec. 3, 2019 (ECF 203), page 10 (D08.txt line 150): "Mr. Mattiaccio applied to the SSA for disability benefits on February 5, 2013 ... He claimed that he was 'unable to work' due to his 'disabling condition on May 31, 2012,' id., which was the day after his termination."
   - Page 8 (line 123) says the same: he stated in Document 1 that he "became unable to work" due to "a disabling condition on May 31, 2012" and was "still disabled" as of February 5, 2013.
   - Page 4 (line 60) lists Document 1 as "Application Summaries for Disability Insurance Benefits ... (Feb. 1, 2013)".
3. **Amendment.** D08 page 10 (line 150): "On March 19, 2013, he amended the onset date of his disabling condition to May 16, 2012, Sealed Document 2 at 1, the date that he was placed on administrative leave."
   - Page 8 (line 130) says he "amended his application to state that he 'became unavailable to work because of [his] disabling condition on May 16, 2012,' rather than May 31."
   - Page 4 (line 62) lists Document 2 as "Amendments to Application for Disability Insurance Benefits ... (Mar. 19, 2013)".
4. **Timeline.** Application of Feb. 1/Feb. 5, 2013, with onset May 31, 2012 → TRO motion of Mar. 4, 2013 (court notice Mar. 5) → amendment of Mar. 19, 2013, changing onset to May 16, 2012. The amendment came 15 days after the motion (Mar. 19 − Mar. 4), so on the motion date the application still said May 31, 2012.
5. The decisive phrases match the source files: docs/uscourts_dcd_1_12_cv_01249_1.txt line 71 and docs/uscourts_dcd_1_12_cv_01249_7.txt lines 121 and 148.

minimal_documents: D02 and D08. No alternatives: D02 is the only document that dates the TRO motion, and D08 is the only one that describes the SSA application and its amendment.

readings:
- **Final or adjudicated onset (ignoring "as it then stood"):** May 16, 2012. That is the amended date, and D08 says "the SSA determined that he was disabled ... as of May 16, 2012" (Document 5 at 1). The question's wording rules this reading out.
- **Treating the TRO date as Mar. 5, 2013** (when the court got notice): still May 31, 2012.

gaps:
- The SSA documents themselves are sealed and not in the packet, so I rely on the court's description of them.
- D08 dates Document 1 Feb. 1, 2013 but gives the application date as Feb. 5, 2013. Both are before Mar. 4, 2013, so the difference doesn't matter.
- Coverage: I read D01–D06, D08 and D09 in full. For D07 I read lines 1–70 and 160–234 in full; I checked the rest only by keyword search (social security, disab, onset, restraining, injunct, TRO, and the relevant dates), with no relevant hits.
- All sources are plain text; there were no PDFs to inspect.
- I did not open the packet's question.txt.

contaminated: no. The auto-attached git status listed only unrelated workspace file names, with no answer or hint for this question.

Key files:
- D:\Agents\Docket\tasks\aq-01548\runs\q01-r0-v2-d731bd7280a337c92061b88ac9a3ab2300139cad87902c916b41a391a5a972a5\solver-1\text\D02.txt
- D:\Agents\Docket\tasks\aq-01548\runs\q01-r0-v2-d731bd7280a337c92061b88ac9a3ab2300139cad87902c916b41a391a5a972a5\solver-1\text\D08.txt
