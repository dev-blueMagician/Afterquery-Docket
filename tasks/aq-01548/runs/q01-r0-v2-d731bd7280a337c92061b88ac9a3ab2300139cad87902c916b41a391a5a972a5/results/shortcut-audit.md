# q01 rev 0 shortcut audit (fresh shortcut-auditor agent, packet shortcut), returned 2026-10-08

answer: May 31, 2012, the day after his May 30, 2012 termination. He moved for the TRO on March 4, 2013. On that day his Social Security disability application, filed February 5, 2013, still gave May 31, 2012 as the date his disabling condition began. He did not amend it to May 16, 2012 until March 19, 2013.

verdict: clear

shortest_path:
1. D02 (Memorandum Opinion of March 12, 2013, ECF 25, page 6, text/D02.txt line 73) says: "The Plaintiff filed his motion for a temporary restraining order on March 4, 2013, though the Court did not receive notice of the motion until the evening of March 5, 2013." This motion (ECF 20) asked the court to stop DHA Group, Hale and Getu from answering a subpoena from a Virginia custody case.
2. D08 (Memorandum Opinion of December 3, 2019, ECF 203):
   - Page 8, line 123: Document 1 says he "became unable to work" due to "a disabling condition on May 31, 2012."
   - Page 8, line 130: Document 2 amended this to "May 16, 2012," rather than May 31.
   - Page 10, line 150: "Mr. Mattiaccio applied to the SSA for disability benefits on February 5, 2013 ... He claimed that he was 'unable to work' due to his 'disabling condition on May 31, 2012,' ... On March 19, 2013, he amended the onset date of his disabling condition to May 16, 2012."
3. Comparing dates: the application (February 5, 2013) came before the TRO motion (March 4, 2013), which came before the amendment (March 19, 2013). So on the TRO day the application still said May 31, 2012. The amendment came 15 days later.
I checked these key sentences against the original files `docs/uscourts_dcd_1_12_cv_01249_1.txt` and `docs/uscourts_dcd_1_12_cv_01249_7.txt`, and they match.

sufficient_documents: D02 and D08 together. Neither works alone, and no other document can stand in for either:
- The TRO appears only in D02. My searches for restraining order, TRO, injunction and March 2013 dates found the TRO nowhere else. The "injunctive" hit in D07 is a footnote about mixed-motive relief, and the "subpoena" hit in D07 is about the National Center for Missing and Exploited Children.
- The application, onset date and amendment appear only in D08. D09 mentions his SSA and VA statements only in general terms, with no dates.

searches:
- Search terms: Social Security, onset, SSDI, SSA, disabilit*, restrain*, TRO, injunct*, March/Mar. 2013 dates, 3/x/13, subpoena, custody.
- Coverage: I read D01 to D09 in full (D07 and D08 in two parts each) plus `manifest.json`. All nine files are plain text extractions.
- What each document covers:
  - D01: dismissal of the defamation claim, December 11, 2012.
  - D02: TRO denial, March 12, 2013.
  - D03: leave to amend, September 16, 2013.
  - D04: motion to strike, November 5, 2013.
  - D05: Blitz dismissal, February 26, 2014.
  - D06: Fischer dismissal, February 26, 2014.
  - D07: summary judgment, April 6, 2015.
  - D08: estoppel and evidence of prior convictions, December 3, 2019.
  - D09: standing, July 21, 2020.
- I did not open `question.txt` or anything outside this packet's `docs/` and `text/` folders.

readings/gaps:
- Likely wrong answer: May 16, 2012. That is the amended onset date (March 19, 2013), and D08 says the SSA ultimately found him disabled as of May 16, 2012 (Document 5, April 14, 2014). It is wrong for the TRO date because the amendment came afterward.
- Other dates that could count as "moved for": the court got notice on March 5, defendants opposed on March 6, and the TRO was denied on March 12, 2013. All are before March 19, so the answer is the same.
- D08's exhibit list dates Document 1 "Feb. 1, 2013," but the text says he applied February 5, 2013. Both are before March 4, so this doesn't change the answer.
- Difficulty risk, not a shortcut: once D02 and D08 are found, the answer only takes putting three dates in order. The phrase "as it then stood" tells the reader the onset date was changed at some point, but not whether the TRO came before or after the change, so D02's date is still needed.
- I found no extraction gaps.
- Contamination check: the harness context included git status, which listed file names from an unrelated task (aq-00949). I saw no file contents, nothing about this task, no answer key, no traps and no CLAUDE.md text. I don't consider that contamination.
