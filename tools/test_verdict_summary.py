"""Regression tests for the difficulty-capture summary, on a synthetic capture only."""
from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

import verdict_summary as vs

RULE = "-" * 72
QUESTION = "What is the host's monthly bill for the two feeds?"


def attempt(label: str, grade: str, full: str, where: str = "", reasoning: str = "thinking") -> str:
    head = f"Attempt {label} · {grade}"
    note = f"Where it left your evidence: {where}\n\n" if where else ""
    return (f"{head}\n{'-' * len(head)}\nDocs: Doc 5, Doc 6 · Note: —\n\nFinal answer: \\] | Your answer (gold): $2,375\n\n"
            f"{note}Full answer\n-----------\n\n{full}\n\nReasoning\n---------\n\n{reasoning}\n\n")


def run(number: int, title: str, tiers: str, changed: str, gold: str, body: str) -> str:
    return (f"{RULE}\nRun {number} · {title}\n{tiers}\n{RULE}\n\nWhat changed before this run: {changed}\n\n"
            f"Solver summary: Run {number} · In band · 1 of 3 right\n\nYour answer: {gold}\n\n{body}")


CAPTURE = (
    "AQ-00000 · Sample — difficulty check\n\nSaved: 2026-10-10 03:56 (local time)\nAttempts read: 6\n\n"
    "8 of 10 runs left · 14 of 50 runs used in the last 24 h (all tasks)\n\nIn band — Medium tier\n\n"
    "- Low model: 0 of 2 attempts right\n- Medium model: 1 of 2 attempts right (the question landed here)\n\n"
    "RUN HISTORY\n\n2 runs\n\n"
    + run(2, "In band — Medium tier · Result the gate uses",
          "Oct 10, 2026, 3:07 AM · Version 8ce393 (current) · Low 0/2 · Medium 1/2 · High —",
          "answer: removed “$1,625”; added “$2,375”", "$2,375",
          "Closed-book check\n=================\nThe low model answers with no documents at all.\n\n"
          + attempt("1", "Needed the documents ✓", "Total monthly bill = $13,000 + $15,500 = $28,500")
          + "Low model\n=========\n\n"
          + attempt("1", "Wrong", "Answer: $875 per month ($500 + $375)\n\nHow the bill is calculated\n\n- a table",
                    where="It omitted the set fees.", reasoning=f'We need parse: "{QUESTION}"')
          + attempt("2", "Wrong", "Answer: The host falls back to the regular program:\n\n- EDGX Top: $750/month\n\n"
                    "Total distribution bill: $1,000/month (plus the usual per-user fees).\n\n(The $350 fee is not due.)")
          + "Medium model\n============\n\n"
          + attempt("1", "Right", "Working...\n\n$$\\$2{,}000 + \\$375 = \\boxed{\\$2{,}375 \\text{ per month}}$$",
                    reasoning=f'Asked: "{QUESTION}"\n\nLow model\n\nnot a section: no underline here')
          + attempt("2", "Wrong", "$2,387.50")
          + "Document check\n==============\n\n"
          + attempt("With every document", "Reached your answer ✓", "Feed totals\n\n$500 (EDGX) + $375 (BYX) = $875 per month.")
          + attempt("Without document 6", "Needed document 6 ✓", "The document does not provide BYX pricing."))
    + run(1, "In band — Easy tier · Earlier version — does not count",
          "Oct 10, 2026, 1:33 AM · Version be6014 · Low 2/5 · Medium — · High —", "first run", "$1,625",
          "Low model\n=========\n\n" + attempt("1", "Right", "- Combined: $1,625/month"))
)


class VerdictSummaryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.parsed = vs.parse(CAPTURE)

    def test_runs_tiers_and_sections(self) -> None:
        runs = self.parsed["runs"]
        self.assertEqual([r["number"] for r in runs], [2, 1])
        self.assertIn("Version 8ce393 (current) · Low 0/2 · Medium 1/2", runs[0]["tiers"])
        self.assertEqual(runs[0]["your_answer"], "$2,375")
        self.assertEqual(runs[1]["your_answer"], "$1,625")
        self.assertEqual([s["name"] for s in runs[0]["sections"]],
                         ["Closed-book check", "Low model", "Medium model", "Document check"])
        self.assertEqual([len(s["attempts"]) for s in runs[0]["sections"]], [1, 2, 2, 2])
        self.assertIn("- Low model: 0 of 2 attempts right", self.parsed["head"])

    def test_committed_values(self) -> None:
        low, medium, doc = (self.parsed["runs"][0]["sections"][i]["attempts"] for i in (1, 2, 3))
        self.assertEqual(vs.committed(low[0]["full"]), "Answer: $875 per month ($500 + $375)")
        self.assertEqual(vs.committed(low[1]["full"]), "Total distribution bill: $1,000/month (plus the usual per-user fees).")
        self.assertEqual(vs.committed(medium[0]["full"]), "boxed: $2,375 per month")
        self.assertEqual(vs.committed(medium[1]["full"]), "$2,387.50")
        self.assertEqual(vs.committed(doc[0]["full"]), "$500 (EDGX) + $375 (BYX) = $875 per month.")
        self.assertEqual(vs.committed(doc[1]["full"]), "The document does not provide BYX pricing.")
        self.assertEqual(vs.committed([]), "")

    def test_committed_list_answer_keeps_every_item(self) -> None:
        bullets = ["The witnesses who held or had held a role at VisitBritain were:", "",
                   "- Anthony Pickles (former Head of Tourism Affairs, VisitBritain)",
                   "- Patricia Yates (Chief Executive, VisitBritain/VisitEngland)"]
        self.assertEqual(vs.committed(bullets),
                         "- Anthony Pickles (former Head of Tourism Affairs, VisitBritain) | "
                         "- Patricia Yates (Chief Executive, VisitBritain/VisitEngland)")
        numbered = ["Based on the evidence:", "1. Anthony Pickles", "2. Ian Edwards"]
        self.assertEqual(vs.committed(numbered), "1. Anthony Pickles | 2. Ian Edwards")
        long_item = "- " + "x" * 200
        self.assertLessEqual(len(vs.committed(["- short one", long_item]).split(" | ")[1]), vs.ITEM_WIDTH)
        # A closing remark with no figure does not hide the list; a closing total does.
        self.assertEqual(vs.committed(bullets + ["No other witness had a role there."]),
                         vs.committed(bullets))
        self.assertEqual(vs.committed(["- three on 20 July", "- six on 1 February", "Total: 9 witnesses."]),
                         "Total: 9 witnesses.")
        # A single bullet and a dollar breakdown keep the older picks.
        self.assertEqual(vs.committed(["Only one:", "- Anthony Pickles"]), "- Anthony Pickles")
        self.assertEqual(vs.committed(["- EDGX: $500", "- BYX: $375"]), "- BYX: $375")

    def test_fields_and_text_inside_reasoning_are_not_headers(self) -> None:
        low, medium = (self.parsed["runs"][0]["sections"][i]["attempts"] for i in (1, 2))
        self.assertEqual(low[0]["where"], "It omitted the set fees.")
        self.assertEqual(low[0]["grade"], "Wrong")
        self.assertEqual(medium[0]["grade"], "Right")
        # "Low model" inside a Reasoning block has no "=" underline, so it opens no section.
        self.assertEqual(len(self.parsed["runs"][0]["sections"]), 4)

    def test_identity_lines_from_a_question_file(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "q01.md"
            path.write_text(f"---\nid: q01\n---\n\n## Question\n\n{QUESTION}\n\n## Answer\n\n$2,375\n\n## Components\n",
                            encoding="utf-8")
            question, gold = vs.question_fields(path)
        self.assertEqual((question, gold), (QUESTION, "$2,375"))
        text = vs.render(self.parsed, question, gold)
        self.assertIn("question quoted verbatim 2 time(s) in this run; \"Your answer\" equals the file's gold ($2,375): yes",
                      text)
        self.assertIn("question quoted verbatim 0 time(s) in this run; \"Your answer\" equals the file's gold ($2,375): no",
                      text)
        self.assertIn("Low model (0 of 2 right)", text)
        self.assertIn("Medium model (1 of 2 right)", text)
        only = vs.render(self.parsed, only_run=1)
        self.assertIn("Run 1 · In band — Easy tier", only)
        self.assertNotIn("Run 2 ·", only)

    def test_trace_spans_and_unloaded_reasoning_are_reported(self) -> None:
        low, medium = (self.parsed["runs"][0]["sections"][i]["attempts"] for i in (1, 2))
        lines = CAPTURE.split("\n")
        self.assertEqual(lines[low[0]["line"] - 1], "Attempt 1 · Wrong")
        self.assertEqual(low[0]["end"] + 1, low[1]["line"])
        self.assertEqual(vs.reasoning_state(low[0]), "loaded")
        self.assertTrue(vs.bare_answer(medium[1]))      # "$2,387.50": the route is only in the Reasoning block
        self.assertFalse(vs.bare_answer(low[0]))
        text = vs.render(self.parsed)
        self.assertNotIn("Reasoning not loaded", text)
        self.assertIn(f"trace: lines {medium[1]['line']}-{medium[1]['end']}, reasoning loaded; the Full answer is a bare "
                      "value, so its route is only in the Reasoning block", text)
        saved_early = vs.parse(CAPTURE.replace(f'We need parse: "{QUESTION}"', "Loading the reasoning…"))
        self.assertEqual(vs.reasoning_state(saved_early["runs"][0]["sections"][1]["attempts"][0]), "not loaded")
        warned = vs.render(saved_early)
        self.assertIn("Reasoning not loaded for 1 attempt(s): Run 2 Low model 1.", warned)
        self.assertNotIn("Reasoning not loaded", vs.render(saved_early, only_run=1))

    def test_evidence_echo_separates_an_unread_ending_from_a_read_one(self) -> None:
        quote = ("from 26 July 2028 as regards companies that had more than 3 000 employees on average, with the "
                 "exception of the measures necessary to comply with Article 16, which Member States shall apply "
                 "to those companies for financial years starting on or after 1 January 2029")
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "q01.md"
            path.write_text(f"## Question\n\n{QUESTION}\n\n## Answer\n\n$2,375\n\n## Evidence\n\n"
                            f'- D02 (Article 37(1)(b), L1039) [c1]: "{quote}"\n'
                            '- D01 (Article 11, L821) [c1]: "published by 30 April each year"\n\n## Necessary documents\n',
                            encoding="utf-8")
            rows = vs.evidence_rows(path)
        self.assertEqual([label for label, _ in rows], ["D02 Article 37(1)(b), L1039", "D01 Article 11, L821"])
        head = "(b) from 26 July 2028 as regards companies that had more than 3,000 employees on average... so 2028."
        share, tail = vs.echo(quote, head)
        self.assertTrue(0 < share < 50)
        self.assertFalse(tail)                      # the closing exception never appears in this attempt
        self.assertEqual(vs.echo(quote, "It says: " + quote), (100, True))
        self.assertEqual(vs.echo(quote, "nothing relevant here"), (0, False))
        # "3 000" in the source and "3,000" in a solver's trace are the same run of words.
        self.assertEqual(vs.echo("more than 3 000 employees on average", "had more than 3,000 employees on average"),
                         (100, True))
        captured = vs.parse(CAPTURE.replace('We need parse: "' + QUESTION + '"', head))
        text = vs.render(captured, evidence=rows)
        self.assertIn("Evidence rows: E1 D02 Article 37(1)(b), L1039; E2 D01 Article 11, L821.", text)
        self.assertIn("% · E2 0%", text)
        self.assertRegex(text, r"evidence echoed: E1 \d+%, end not echoed · E2 0%")
        self.assertNotIn("evidence echoed", vs.render(captured))       # only with a question file's evidence

    def test_a_page_without_runs_is_reported(self) -> None:
        self.assertEqual(vs.parse("AQ-00000 · Sample\n\nSaved: 2026-10-10\n")["runs"], [])


if __name__ == "__main__":
    unittest.main()
