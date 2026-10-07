---
name: docket-capture-pipe-tables
description: "In complete captures, table blocks the earlier capture hid come out as Markdown pipe tables; the platform's own text shows those rows without pipes, so evidence quotes spanning their cells may fail the form's verbatim check. Prefer prose or tab-text rows; otherwise re-copy via Save passage."
metadata:
  node_type: memory
  type: project
  updated: 2026-10-05
  originSessionId: 3aa0fb8b-a0f5-4582-9b0e-56bdce72da25
  modified: 2026-10-06T06:15:15.379Z
---

## Current rule

- A complete capture renders the formerly hidden table blocks ("[... N characters not shown on the
  page ...]" in the clipped capture) as Markdown pipe tables: a blank header row "|  |  |", a
  "| --- |" separator, one cell per pipe. In aq-00745 the per-document pipe-table counts equal the
  old gap-marker counts exactly (D01 24, D02 10, D03 20, D04 20, D07 20, D08 9, D10 18), and the
  rows visible in both captures stay tab text ("Total reported\t2,457 1,461 141 158 697"). Some
  tab-indented blocks also gain a "```text" fence. split_capture.py keeps these bytes as captured.
- The platform's own text shows such rows without pipes: the aq-00949 form quoted a pipe-rendered
  row as "Other International (C) - - - - - - - 4 1". So an evidence quote that spans cells of a
  pipe row ("| Gross Margin | 23,327 | 1,824 | 25,151 |") passes the local floor but may fail the
  form's blocking "Verbatim evidence" check. (A pipe-free quote failed the local floor only until
  the tool change below; re-verified 2026-10-06 on aq-00998 D10: both forms pass.)
- Tool change (2026-10-05, aq-00949 session): check_questions.py now also matches quotes with the
  Markdown pipes removed (depipe in verbatim_found / quote_found; test
  test_pipe_table_row_matches_platform_text). A pipe-row input can now be quoted in the platform's
  space-separated form ("Dividends Paid (538) (528)") and still pass the local floor; the piped form
  still passes too. The form's own check remains unconfirmed for such quotes.
- At write-up, quote prose or tab-text rows where they carry the input. When an input exists only
  in pipe rows, keep the local quote, flag it at hand-over, and ask the user to Save passage on the
  platform page and report the exact text; changing evidence is a new revision and new checks.
  Quick tests need no evidence, so the risk only applies to the full form.

**Why:** aq-00745 q05 (FY2025 adjusted operating margin) needs three reconciliation rows that
exist only as pipe tables; the reviewer found no plain-text substitute.

**How to apply:** after re-ingesting a complete capture, count "| --- |" lines per document and
compare with the old gap counts; at sketch time note which inputs live only in pipe rows. See
[[docket-form-automated-checks]] and [[docket-windows-text-io]].

## Evidence and history

- 2026-10-06 (aq-01322, .txt capture, compact pipe tables): the form accepted piped quotes. The
  difficulty check unlocks only after every blocking check passes, and its run echoed the question's
  evidence "|U.S. Healthcare Solutions|$998,300|$944,969|5.6%|" with the pipes. First observed pass
  of the Verbatim evidence check on a pipe-row quote; whether the depiped form also passes is unseen.
- 2026-10-05 (aq-00745 re-ingest; aq-00949 form warning text). Inference from the platform's
  message format; no pipe-row quote has been pasted into the form yet. Unconfirmed until the form
  reports on one.
- 2026-10-05 (aq-00949 q03/q04): the dividends-paid and debt inputs exist only in pipe rows in every
  edition; the floor fix above lets write-ups quote them as the platform shows them.
- 2026-10-05 (aq-01189, a capture with no gap markers): every fenced block is a pipe table ("|---|"
  separators, no spaces), in both companies' documents, Freeport's releases included; there is no
  tab text. A bare cell value ("493", "16.4 Mt") is shorter than the form's 12-character quote
  minimum, so q01/q02 quote prose sentences or text inside one cell, and build table-only inputs
  from prose where possible (Q1 248 + Q2 245 = the six-month table's 493). Arrow glyphs inside
  BHP cells ("é"/"ê") were kept out of quotes.
- 2026-10-06 (aq-01320; also AQ-01278/01321/01322): the task page can now be saved as a plain-text
  capture ("==== DOCUMENTS ====" banners, "Doc N · ..." blocks between 72-dash rules). Its tables are
  compact pipe tables in every document, the same as complete Markdown captures, so the prose-first
  quoting rule applies. tools/split_capture.py reads this format since 2026-10-06 (docket-e1 session).
