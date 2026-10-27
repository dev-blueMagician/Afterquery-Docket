"""Test Docket snapshot isolation, source provenance and fail-closed tool access.

Usage: python tools/test_docket_agent.py
All fixtures and packets live in temporary task roots. These tests do not invoke models,
write workspace task data or measure platform difficulty.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import agent_scope
import check_questions as cq
import docket_agent as da
import platform_checks as pc
import split_capture
from test_platform_checks import PlatformChecksTests  # Included in the required regression suite.
from test_docket_efficiency import DocketEfficiencyTests
from test_lever_mine import LeverMineTests  # Included in the required regression suite.

QUESTION = """---
id: q01
status: draft
origin: codex
asks: 1
answer_type: number
documents: D01, D02
tags: Cross-document join; Aggregation
levers: Calculate across documents
revision: 0
difficulty_target: easy
---

## Question
By how many million dollars did regional freight revenue change from calendar 2024 to calendar
2025? Give the signed difference to one decimal place.

## Answer
+$2.8 million

## Components
- c1: +$2.8 million

## Reasoning
The 2024 revenue was 409.8 million and 2025 revenue was 412.6 million. Subtraction gives
412.6 - 409.8 = 2.8 million dollars.

## Evidence
- D01 (table) [c1]: "Revenue for calendar 2024 was $409.8 million."
- D02 (table) [c1]: "Revenue for calendar 2025 was $412.6 million."

## Lever checks
This is a simple fixture, not a claimed difficult candidate.

## Blind solve

## Shortcut audit

## Review

## Feedback log
"""


class DocketAgentTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="docket-agent-test-")
        self.root = Path(self.temp.name)
        self.bundle = self.root / "tasks" / "freight"
        for name in ("docs", "text", "notes", "questions"):
            (self.bundle / name).mkdir(parents=True)
        manifest = {}
        for doc_id, year, amount in (("D01", "2024", "409.8"), ("D02", "2025", "412.6")):
            data = f"Revenue for calendar {year} was ${amount} million.\n".encode()
            (self.bundle / "docs" / f"{doc_id}.txt").write_bytes(data)
            (self.bundle / "text" / f"{doc_id}.txt").write_bytes(data)
            manifest[doc_id] = {"source": f"docs/{doc_id}.txt", "method": "text"}
        (self.bundle / "text" / "manifest.json").write_bytes(da.json_bytes(manifest))
        (self.bundle / "notes" / "ideas.md").write_bytes(b"SECRET_WRITER_NOTES")
        self.path = self.bundle / "questions" / "q01.md"
        self.path.write_bytes(QUESTION.encode())

    def tearDown(self):
        self.temp.cleanup()

    def access(self, path: Path, tool: str = "Read", **kwargs):
        return agent_scope.check("blind-solver", {"tool_name": tool,
                                 "tool_input": {"file_path": str(path), **kwargs}}, self.root)

    def write_sketch(self, evidence: str | None = None) -> Path:
        folder = self.bundle / "notes" / "sketches"
        folder.mkdir(exist_ok=True)
        meta, sec = cq.parse(self.path)
        sketch = ("---\nid: i01\ndifficulty_target: easy\ndocuments: D01, D02\n---\n\n"
                  f"## Question\n{sec['question']}\n\n## Answer\n{sec['answer']}\n\n"
                  f"## Evidence\n{evidence if evidence is not None else sec['evidence']}\n")
        path = folder / "i01.md"
        path.write_bytes(sketch.encode())
        return path

    def test_short_sketch_screen_needs_no_components_or_full_writeup(self):
        path = self.write_sketch()
        before = path.read_bytes()
        result = da.screen(self.bundle, "i01")
        self.assertTrue(result["eligible_for_full_writeup"])
        self.assertEqual(result["failures"], [])
        self.assertEqual(result["supported_input_documents"], ["D01", "D02"])
        self.assertIn("No independent or platform test", result["claim"])
        self.assertFalse((self.bundle / "runs").exists())
        self.assertFalse((self.root / ".claude" / "solver-scope.json").exists())
        self.assertEqual(path.read_bytes(), before)

    def test_sketch_screen_warns_on_an_input_printed_only_in_words(self):
        # aq-02505 q01 (2026-10-09): totals printed only in words drew "Doc N doesn't mention" on the form.
        data = b"Revenue for calendar 2024 was $409.8 million. One hundred and seven stores were open.\n"
        (self.bundle / "docs" / "D01.txt").write_bytes(data)
        (self.bundle / "text" / "D01.txt").write_bytes(data)
        self.write_sketch('- D01 (table): "One hundred and seven stores were open."\n'
                          '- D02 (table): "Revenue for calendar 2025 was $412.6 million."')
        result = da.screen(self.bundle, "i01")
        self.assertEqual(result["failures"], [])
        self.assertEqual([w for w in result["warnings"] if "only in words" in w],
                         ["D01: the quote states 107 only in words (\"One hundred and seven\"): a reasoning step citing "
                          "this document for 107 draws \"Doc N doesn't mention 107\" on the form (aq-02505 q01), a "
                          "false alarm no wording clears; prefer an input printed in digits, or keep this quote as "
                          "evidence and mention the flag with the hand-over."])

    def test_sketch_screen_raises_wording_notes_before_the_quick_test(self):
        # aq-03707 q03 (2026-10-13): the floor first asked for "if any" at promotion, after the quick test, and
        # the tested sentence was edited. The screen now raises the same notes while the sentence is a sketch.
        path = self.write_sketch()
        _, sec = cq.parse(self.path)
        base = path.read_text(encoding="utf-8")
        self.assertEqual(base.count(sec["question"]), 1)

        def notes(question: str, answer: str) -> list[str]:
            path.write_bytes(base.replace(sec["question"], question)
                             .replace(f"## Answer\n{sec['answer']}", f"## Answer\n{answer}").encode())
            return [w for w in da.screen(self.bundle, "i01")["warnings"] if "word for word" in w]

        loose = notes("Which years had revenue above 400 million dollars?", "2024, 2025")
        self.assertEqual(len(loose), 2)
        self.assertIn("if any", loose[0])
        self.assertIn("no order", loose[1])
        self.assertEqual(notes("Which years, if any, had revenue above 400 million dollars? "
                               "List them in date order.", "2024, 2025"), [])
        rate = notes("What share of the two-year revenue total did the larger year take?", "50.2%")
        self.assertEqual(len(rate), 1)
        self.assertIn("precision", rate[0])
        cue = notes("How many stores were open, including any that only another document mentions?", "107 stores")
        self.assertEqual(len(cue), 1)
        self.assertIn("cue", cue[0])

    def test_sketch_screen_raises_the_notes_of_the_2026_10_16_guide(self):
        # Sections 5 and 7 of the platform guide (2026-10-15/16): no word that points at the trap, a bare gold, no
        # contrived selector, a literal reading of "the latest report", and a 20-45 word aim.
        path = self.write_sketch()
        _, sec = cq.parse(self.path)
        base = path.read_text(encoding="utf-8")

        def notes(question: str, answer: str = sec["answer"]) -> list[str]:
            path.write_bytes(base.replace(sec["question"], question)
                             .replace(f"## Answer\n{sec['answer']}", f"## Answer\n{answer}").encode())
            return [w for w in da.screen(self.bundle, "i01")["warnings"] if "word for word" in w]

        self.assertEqual(notes(sec["question"]), [])
        self.assertIn("'originally'", notes("By how many million dollars did revenue, as originally reported, change "
                                            "from calendar 2024 to calendar 2025? Give one decimal place.")[0])
        for answer in ("an increase of $2.8 million", "+$2.8 million (calendar years)"):
            with self.subTest(answer=answer):
                self.assertIn("bare value", notes(sec["question"], answer)[0])
        self.assertIn("pitfall 1", notes("By how many million dollars did revenue in the year in which the depot opened "
                                         "differ from calendar 2024? Give one decimal place.")[0])
        self.assertIn("send-back reason 8", notes("By how many million dollars did the latest report's revenue for "
                                                  "calendar 2025 differ from calendar 2024? Give one decimal place.")[0])
        self.assertIn("20-45", notes(sec["question"] + " Use the figures as each annual release prints them." * 4)[0])

    def test_hard_sketch_screen_reads_the_lever_stack(self):
        # Guide, 2026-10-16: "One lever usually lands Easy; two together land Medium or Hard". From 2026-10-14 to 16,
        # 46 screened sentences were right in 138 of 138 local solves (notes/hard-runs.md).
        for doc_id, text in (("D01", b"Revenue for calendar 2024 was $409.8 million. The depot sale added $3.0 "
                                     b"million to that revenue.\n"),
                             ("D02", b"Revenue for calendar 2025 was $412.6 million, restated to exclude the ferry "
                                     b"division.\n")):
            (self.bundle / "docs" / f"{doc_id}.txt").write_bytes(text)
            (self.bundle / "text" / f"{doc_id}.txt").write_bytes(text)
        folder = self.bundle / "notes" / "sketches"
        folder.mkdir(exist_ok=True)
        question = ("By how many million dollars did regional freight revenue change from calendar 2024 to calendar "
                    "2025, leaving out the depot sale? Give one decimal place.")
        evidence = ('- D01 (table): "Revenue for calendar 2024 was $409.8 million."\n'
                    '- D02 (table): "Revenue for calendar 2025 was $412.6 million"\n')

        def screen(stack: str | None) -> tuple[list[str], list[str]]:
            (folder / "i01.md").write_bytes(("---\nid: i01\ndifficulty_target: hard\ndocuments: D01, D02\n---\n\n"
                                            f"## Question\n{question}\n\n## Answer\n$5.8 million\n\n## Evidence\n"
                                            f"{evidence}\n" + (f"## Lever stack\n{stack}\n" if stack else "")).encode())
            result = da.screen(self.bundle, "i01")
            return result["failures"], [w for w in result["warnings"] if w.startswith("Lever stack")]

        self.assertIn("missing or unfinished", screen(None)[1][0])
        good = ('Shape: 1\n'
                '- L1: Restated figures | trap: D02 "restated to exclude the ferry division" | settles: D01 "Revenue '
                'for calendar 2024 was $409.8 million" | missed gives: $2.8 million\n'
                '- L2: Match, then exclude | trap: D01 "Revenue for calendar 2024 was $409.8 million" | settles: D01 '
                '"The depot sale added $3.0 million to that revenue" | missed gives: $8.8 million\n'
                'Steps:\n1. Take the 2025 figure on its restated basis.\n2. Take the 2024 figure.\n'
                '3. Leave out the depot sale and subtract.\n\nDecoy: $2.8 million\n')
        fails, warns = screen(good)
        self.assertEqual(fails, [])
        # "depot" and "sale" are printed in one document only and the question names them, so a search lands on the
        # passage that settles L2 (playbook 4.4).
        self.assertEqual(len(warns), 1)
        self.assertIn("L2: the question's rare word(s) depot, sale", warns[0])
        fails, _ = screen(good.replace("added $3.0 million", "added $4.0 million"))
        self.assertEqual(fails, ["Lever stack L2: the settles quote is not in D01's extracted text."])
        _, warns = screen(good.replace("missed gives: $8.8 million", "missed gives: $2.8 million"))
        self.assertTrue(any("L2 and L1: missing either gives the same wrong answer" in w for w in warns))
        _, warns = screen(good.split("- L2")[0] + "Steps:\n1. a\n2. b\n\nDecoy: $2.8 million\n")
        self.assertTrue(any("one lever" in w for w in warns))
        self.assertTrue(any("2 numbered step(s)" in w for w in warns))
        _, warns = screen(good.replace("Decoy: $2.8 million", ""))
        self.assertTrue(any("no 'Decoy:' line" in w for w in warns))

    def test_sketch_screen_warns_when_a_period_word_is_also_a_reporting_label(self):
        # aq-03120 (2026-10-12): "its last completed financial half-year" sat beside "half-year results" in a
        # document; the high model read the interim period and the gate failed. The structural wording passed.
        data = b"Revenue for calendar 2024 was $409.8 million. See the half-year results for the six months to June.\n"
        (self.bundle / "docs" / "D01.txt").write_bytes(data)
        (self.bundle / "text" / "D01.txt").write_bytes(data)
        folder = self.bundle / "notes" / "sketches"
        folder.mkdir(exist_ok=True)
        evidence = ('- D01 (table): "Revenue for calendar 2024 was $409.8 million."\n'
                    '- D02 (table): "Revenue for calendar 2025 was $412.6 million."\n')

        def sketch(question: str) -> list[str]:
            (folder / "i01.md").write_bytes(("---\nid: i01\ndifficulty_target: medium\ndocuments: D01, D02\n---\n\n"
                                            f"## Question\n{question}\n\n## Answer\n$2.8 million\n\n"
                                            f"## Evidence\n{evidence}").encode())
            result = da.screen(self.bundle, "i01")
            self.assertEqual(result["failures"], [])
            return [w for w in result["warnings"] if "reporting" in w or "label reports" in w]

        flagged = sketch("How much did regional freight revenue grow in its last completed financial half-year "
                         "before the depot opened?")
        self.assertEqual(len(flagged), 1)
        self.assertIn('the question says "half-year" and D01 prints "half-year results"', flagged[0])
        self.assertEqual(sketch("How much did regional freight revenue grow in the half of its financial year "
                                "that last ended before the depot opened?"), [])

    def test_efficiency_command_delegates_without_question_validation(self):
        import docket_efficiency
        with mock.patch.object(docket_efficiency, "main", return_value=0) as command, \
                mock.patch.object(cq, "check", side_effect=AssertionError("metrics must not validate questions")):
            self.assertEqual(da.main(["efficiency", "report"]), 0)
        command.assert_called_once_with(["report"])

    def test_sketch_screen_rejects_unsupported_gold_inputs_without_banning_simple_math(self):
        good = cq.parse(self.path)[1]["evidence"]
        for evidence in (good.replace("409.8", "900.0"), good.splitlines()[0],
                         good.replace("D02", "D01")):
            with self.subTest(evidence=evidence):
                self.write_sketch(evidence)
                result = da.screen(self.bundle, "i01")
                self.assertFalse(result["eligible_for_full_writeup"])
        self.write_sketch()
        before = da.screen(self.bundle, "i01")["sketch_sha256"]
        (self.bundle / "text" / "D01.txt").write_bytes(b"Revenue for calendar 2024 was $409.8 million. Revised.\n")
        result = da.screen(self.bundle, "i01")
        self.assertTrue(result["eligible_for_full_writeup"])
        self.assertNotEqual(before, result["sketch_sha256"])

    def test_sketch_screen_reports_known_gaps_for_later_relevance_review(self):
        self.write_sketch()
        (self.bundle / "text" / "D01.txt").write_bytes(("Revenue for calendar 2024 was $409.8 million.\n"
                            "[... 100 characters not shown on the page ...]\n").encode())
        result = da.screen(self.bundle, "i01")
        self.assertTrue(result["eligible_for_full_writeup"])
        self.assertTrue(result["source_gaps"])
        self.assertEqual(result["source_gaps"], cq.source_completeness(cq.Bundle(self.bundle)))
        self.assertEqual(result["source_gaps_sha256"], cq.source_gaps_sha256(result["source_gaps"]))
        self.assertTrue(result["warnings"])

    def test_prepare_isolates_full_corpus_without_writer_metadata(self):
        result = da.prepare(self.bundle, "q01", local_checks=True)
        snapshot = json.loads((Path(result["run"]) / "snapshot.json").read_bytes())
        self.assertEqual(snapshot["sections"]["answer"], "+$2.8 million")
        for name in da.PACKETS:
            packet = Path(result["packets"][name])
            files = {str(p.relative_to(packet)).replace("\\", "/") for p in packet.rglob("*") if p.is_file()}
            self.assertEqual(files, {"question.txt", "docs/D01.txt", "docs/D02.txt",
                                    "text/D01.txt", "text/D02.txt", "text/manifest.json"})
            self.assertNotIn(b"SECRET_WRITER_NOTES", b"".join(p.read_bytes() for p in packet.rglob("*") if p.is_file()))
            self.assertEqual((packet / "question.txt").read_bytes(),
                             (cq.parse(self.path)[1]["question"] + "\n").encode())
        closed = Path(result["packets"]["closed-book"])
        self.assertEqual({p.name for p in closed.iterdir()}, {"question.txt"})
        self.assertTrue(all((self.bundle / "docs" / f"{d}.txt").is_file() for d in ("D01", "D02")))

    def test_default_prepare_snapshots_once_without_solver_packets_or_scope(self):
        before = self.path.read_bytes()
        with mock.patch.object(da, "bind_scope", side_effect=AssertionError("No local scope by default")):
            result = da.prepare(self.bundle, "q01")
            self.assertEqual(result, da.prepare(self.bundle, "q01"))
        run = Path(result["run"])
        self.assertEqual({p.name for p in run.iterdir()}, {"snapshot.json", "corpus"})
        self.assertEqual(result["packets"], {})
        self.assertEqual(result["bound_runs"], [])
        self.assertFalse(result["local_checks"])
        self.assertIn("platform validation", result["next"])
        self.assertFalse((self.root / ".claude" / "solver-scope.json").exists())
        self.assertEqual((Path(result["corpus"]) / "docs" / "D01.txt").read_bytes(),
                         (self.bundle / "docs" / "D01.txt").read_bytes())
        self.assertEqual(self.path.read_bytes(), before)
        (run / "corpus" / "text" / "D01.txt").write_bytes(b"Altered saved source")
        with self.assertRaisesRegex(ValueError, "refusing reuse"):
            da.prepare(self.bundle, "q01")

    def test_sentence_notes_ask_for_the_empty_case_when_which_follows_an_opening_phrase(self):
        # aq-04797 i05 (2026-10-14): the floor warned 'format' only at promotion, after the quick test.
        question = ("Relative to nominal capacity, which lithium-ion cells besides NASA cell B0005 end their "
                    "constant-voltage charge at a current no higher than B0005's? List them alphabetically.")
        notes = da.sentence_notes(question, "B0006, B0007, PANASONIC NCA cells")
        self.assertTrue(any("if any" in note for note in notes))
        self.assertFalse(any("gives no order" in note for note in notes))
        settled = question.replace("cells besides", "cells, if any, besides")
        self.assertFalse(any("if any" in note for note in da.sentence_notes(settled, "B0006, B0007, PANASONIC NCA cells")))
        self.assertFalse(any("if any" in note for note in da.sentence_notes(
            "Relative to its nominal capacity, which cell ends its charge at the lowest current?", "B0018")))
        self.assertFalse(any("if any" in note for note in da.sentence_notes(
            "In the year in which revenue peaked, what was it in dollars?", "$3,441,336")))

    def test_prepare_reads_snapshots_whose_document_paths_pass_260_characters(self):
        # aq-04797 (2026-10-14): platform document names of about 125 characters under the
        # fingerprint-named run folder made 265-284 character paths; with Windows long paths off,
        # rglob skipped the documents and prepare refused its own snapshot.
        long_name = "state-of-health-" * 8 + "lithium-ion.txt"  # bundle path stays under 260
        (self.bundle / "docs" / "D01.txt").rename(self.bundle / "docs" / long_name)
        manifest = json.loads((self.bundle / "text" / "manifest.json").read_bytes())
        manifest["D01"]["source"] = f"docs/{long_name}"
        (self.bundle / "text" / "manifest.json").write_bytes(da.json_bytes(manifest))
        try:
            first = da.prepare(self.bundle, "q01")
            self.assertEqual(first, da.prepare(self.bundle, "q01"))
            corpus = cq.long_path(Path(first["corpus"]))
            self.assertGreater(len(str(Path(first["corpus"]) / "docs" / long_name)), 260)
            self.assertEqual((corpus / "docs" / long_name).read_bytes(),
                             (self.bundle / "docs" / long_name).read_bytes())
            snapshot = pc._snapshot(self.bundle.resolve(), "q01", 0, first["tested_sha256"])
            self.assertEqual(snapshot.parent, Path(first["run"]).absolute())
        finally:  # the temporary directory's own cleanup cannot reach paths past 260 characters
            shutil.rmtree(cq.long_path(self.bundle / "runs"), ignore_errors=True)

    def test_platform_prepare_preserves_opt_in_packets_and_scope(self):
        local = da.prepare(self.bundle, "q01", local_checks=True)
        binding = self.root / ".claude" / "solver-scope.json"
        before = binding.read_bytes()
        platform = da.prepare(self.bundle, "q01")
        self.assertEqual(local["tested_sha256"], platform["tested_sha256"])
        self.assertNotEqual(local["run"], platform["run"])
        self.assertEqual(binding.read_bytes(), before)
        self.assertIsNone(self.access(Path(local["packets"]["solver-1"]) / "text" / "D01.txt"))
        self.assertIsNotNone(self.access(Path(platform["corpus"]) / "text" / "D01.txt"))

    def test_prepare_cli_defaults_to_platform_and_requires_explicit_local_flag(self):
        with mock.patch.object(da, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(da.main(["prepare", str(self.bundle), "--q", "q01"]), 0)
        self.assertEqual(json.loads(output.getvalue())["packets"], {})
        with mock.patch.object(da, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(da.main(["prepare", str(self.bundle), "--q", "q01", "--local-checks"]), 0)
        self.assertEqual(set(json.loads(output.getvalue())["packets"]), {*da.PACKETS, "closed-book"})
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(da.main(["report", str(self.bundle), "--q", "q01", "--local-checks"]), 1)

    def test_prepare_idempotent_and_refuses_tampered_or_contaminated_packets(self):
        first = da.prepare(self.bundle, "q01", local_checks=True)
        self.assertEqual(first, da.prepare(self.bundle, "q01", local_checks=True))
        packet = Path(first["packets"]["solver-1"])
        (packet / "answer.md").write_bytes(b"Leaked answer")
        with self.assertRaisesRegex(ValueError, "refusing reuse"):
            da.prepare(self.bundle, "q01", local_checks=True)
        (packet / "answer.md").unlink()
        (packet / "text" / "D01.txt").write_bytes(b"Modified document")
        with self.assertRaisesRegex(ValueError, "refusing reuse"):
            da.prepare(self.bundle, "q01", local_checks=True)

    def test_snapshot_gold_edit_cannot_reuse_unchanged_fingerprint(self):
        result = da.prepare(self.bundle, "q01", local_checks=True)
        snapshot_path = Path(result["run"]) / "snapshot.json"
        snapshot = json.loads(snapshot_path.read_bytes())
        snapshot["sections"]["answer"] = "$100 million"
        snapshot_path.write_bytes(da.json_bytes(snapshot))
        with self.assertRaisesRegex(ValueError, "Frozen submission fields changed"):
            da.prepare(self.bundle, "q01", local_checks=True)

    def test_snapshot_version_preserves_old_runs_and_detects_gap_metadata_tampering(self):
        digest = cq.submission_sha256(*cq.parse(self.path), cq.Bundle(self.bundle))
        old_run = self.bundle / "runs" / f"q01-r0-{digest}"
        old_run.mkdir(parents=True)
        (old_run / "snapshot.json").write_bytes(b'{"schema":1}')
        result = da.prepare(self.bundle, "q01", local_checks=True)
        self.assertNotEqual(Path(result["run"]), old_run)
        self.assertEqual((old_run / "snapshot.json").read_bytes(), b'{"schema":1}')
        snapshot_path = Path(result["run"]) / "snapshot.json"
        snapshot = json.loads(snapshot_path.read_bytes())
        snapshot["source_gaps"] = ["Forged source-gap list"]
        snapshot_path.write_bytes(da.json_bytes(snapshot))
        with self.assertRaisesRegex(ValueError, "Frozen source-gap metadata changed"):
            da.prepare(self.bundle, "q01", local_checks=True)

    def test_source_or_question_edit_produces_new_fingerprint_and_run(self):
        first = da.prepare(self.bundle, "q01", local_checks=True)
        (self.bundle / "docs" / "D01.txt").write_bytes(b"Changed original bytes.\n")
        second = da.prepare(self.bundle, "q01", local_checks=True)
        self.assertNotEqual(first["tested_sha256"], second["tested_sha256"])
        self.assertNotEqual(first["run"], second["run"])
        self.path.write_bytes(QUESTION.replace("regional freight", "freight operator").encode())
        third = da.prepare(self.bundle, "q01", local_checks=True)
        self.assertNotEqual(second["tested_sha256"], third["tested_sha256"])
        self.assertTrue(Path(first["run"]).is_dir())

    def test_scope_requires_binding_and_denies_other_bundles_runs_notes(self):
        self.assertIsNotNone(self.access(self.bundle / "text" / "D01.txt"))
        result = da.prepare(self.bundle, "q01", local_checks=True)
        self.assertIsNotNone(self.access(self.bundle / "text" / "D01.txt"))
        self.assertIsNone(self.access(Path(result["packets"]["shortcut"]) / "docs" / "D02.txt"))
        denied = [self.root / "tasks" / "other" / "text" / "D01.txt",
                  self.bundle / "notes" / "ideas.md", Path(result["run"]) / "snapshot.json",
                  self.bundle / "runs" / "other-run" / "solver-1" / "text" / "D01.txt",
                  Path(result["packets"]["solver-1"]) / "question.txt"]
        for path in denied:
            with self.subTest(path=path):
                self.assertIsNotNone(self.access(path))
        self.assertIsNotNone(agent_scope.check("closed-book-solver", {"tool_name": "Read",
                            "tool_input": {"file_path": str(self.bundle / "text" / "D01.txt")}}, self.root))
        self.assertIsNotNone(agent_scope.check("blind-solver", {"tool_name": "Glob",
                            "tool_input": {"path": str(self.bundle / "text"), "pattern": "../notes/*"}}, self.root))

    def make_second_bundle(self) -> Path:
        other = self.root / "tasks" / "cargo"
        for name in ("docs", "text", "notes", "questions"):
            (other / name).mkdir(parents=True)
        for name in ("docs", "text"):
            for doc_id in ("D01", "D02"):
                (other / name / f"{doc_id}.txt").write_bytes((self.bundle / name / f"{doc_id}.txt").read_bytes())
        (other / "text" / "manifest.json").write_bytes((self.bundle / "text" / "manifest.json").read_bytes())
        (other / "questions" / "q01.md").write_bytes(QUESTION.encode())
        return other

    def test_concurrent_prepares_keep_each_others_runs_bound(self):
        first = da.prepare(self.bundle, "q01", local_checks=True)
        second = da.prepare(self.make_second_bundle(), "q01", local_checks=True)
        for result in (first, second):
            with self.subTest(run=result["run"]):
                self.assertIsNone(self.access(Path(result["packets"]["solver-2"]) / "text" / "D01.txt"))
                self.assertIsNotNone(self.access(Path(result["run"]) / "snapshot.json"))
        scope = json.loads((self.root / ".claude" / "solver-scope.json").read_bytes())
        self.assertEqual(scope["schema"], 2)
        self.assertEqual([entry["bundle"] for entry in scope["runs"]], ["cargo", "freight"])
        self.assertFalse((self.root / ".claude" / "solver-scope.lock").exists())
        self.assertIsNotNone(self.access(self.bundle / "runs" / "other-run" / "solver-1" / "text" / "D01.txt"))

    def test_legacy_binding_is_merged_and_stale_or_missing_runs_are_dropped(self):
        first = da.prepare(self.bundle, "q01", local_checks=True)
        run_name = Path(first["run"]).name
        binding = self.root / ".claude" / "solver-scope.json"
        binding.write_bytes(json.dumps({"schema": 1, "bundle": "freight", "run": run_name}).encode())
        self.assertIsNone(self.access(Path(first["packets"]["shortcut"]) / "docs" / "D02.txt"))
        other = da.prepare(self.make_second_bundle(), "q01", local_checks=True)
        self.assertEqual(other["bound_runs"], [f"cargo/{Path(other['run']).name}", f"freight/{run_name}"])
        scope = json.loads(binding.read_bytes())
        scope["runs"].append({"bundle": "freight", "run": "vanished-run", "bound_at": scope["runs"][0]["bound_at"]})
        scope["runs"][1]["bound_at"] -= da.BINDING_TTL_SECONDS + 1
        binding.write_bytes(da.json_bytes(scope))
        again = da.bind_scope(self.root, "cargo", Path(other["run"]).name)
        self.assertEqual([(entry["bundle"], entry["run"]) for entry in again], [("cargo", Path(other["run"]).name)])
        self.assertIsNotNone(self.access(Path(first["packets"]["shortcut"]) / "docs" / "D02.txt"))

    def test_guard_accepts_schema_two_only_with_safe_entries(self):
        result = da.prepare(self.bundle, "q01", local_checks=True)
        binding = self.root / ".claude" / "solver-scope.json"
        target = Path(result["packets"]["solver-1"]) / "text" / "D01.txt"
        for broken in ({"schema": 2, "runs": []}, {"schema": 2, "runs": [{"bundle": "../x", "run": "r"}]},
                       {"schema": 2, "runs": "freight"}, ["freight"]):
            with self.subTest(binding=broken):
                binding.write_bytes(json.dumps(broken).encode())
                self.assertIsNotNone(self.access(target))

    def test_guard_rejects_malformed_inputs_and_windows_escape_globs(self):
        da.prepare(self.bundle, "q01", local_checks=True)
        for value in ([], "text", {}, {"tool_name": "Read", "tool_input": []}):
            with self.subTest(value=value):
                self.assertIsNotNone(agent_scope.check("blind-solver", value, self.root))
        for pattern in ("C:secret", r"\secret", r"..\notes\*", "../notes/*"):
            with self.subTest(pattern=pattern):
                self.assertIsNotNone(agent_scope.check("blind-solver", {"tool_name": "Glob",
                                    "tool_input": {"path": str(self.bundle / "text"), "pattern": pattern}}, self.root))

    def test_packet_preparation_rejects_unregistered_files_that_could_leak_answers(self):
        (self.bundle / "text" / "answers.json").write_bytes(b'{"gold": "secret"}')
        with self.assertRaisesRegex(ValueError, "Unexpected corpus file"):
            da.prepare(self.bundle, "q01", local_checks=True)

    def test_template_gitkeep_is_inert_but_nonempty_hidden_files_are_rejected(self):
        before = da.prepare(self.bundle, "q01", local_checks=True)
        for folder in ("docs", "text"):
            (self.bundle / folder / ".gitkeep").write_bytes(b"")
        self.assertEqual(before, da.prepare(self.bundle, "q01", local_checks=True))
        (self.bundle / "text" / ".gitkeep").write_bytes(b"Hidden leaked answer")
        with self.assertRaisesRegex(ValueError, "Unexpected corpus file"):
            da.prepare(self.bundle, "q01", local_checks=True)

    def test_prepare_refuses_invalid_floor_and_frozen_questions(self):
        for value, error in ((QUESTION.replace("difficulty_target: easy", ""), "explicit difficulty_target"),
                             (QUESTION.replace("status: draft", "status: accepted"), "frozen"),
                             (QUESTION.replace("Revenue for calendar 2024 was $409.8 million.", "Wrong quote from the document."), "mechanical floor")):
            self.path.write_bytes(value.encode())
            with self.subTest(error=error), self.assertRaisesRegex(ValueError, error):
                da.prepare(self.bundle, "q01", local_checks=True)
        with self.assertRaises(ValueError):
            da.question_path(self.bundle, "../q01")

    def test_split_capture_persists_omissions_and_mismatch_provenance(self):
        capture = self.root / "capture.md"
        capture.write_bytes(("## Documents\n\n### Doc 1 · captured.txt\n**Report**\n"
                             "1,000 tokens · 2,000 characters\n"
                             "> **Incomplete:** only 1,000 of 2,000 characters are shown\n\n"
                             "Visible document. [... 1,000 characters not shown on the page ...]\n").encode())
        split_capture.run(capture, self.bundle)
        intake = json.loads((self.bundle / "notes" / "intake.json").read_bytes())
        doc = intake["documents"][0]
        self.assertTrue(doc["incomplete"])
        self.assertEqual(doc["gap_characters"], 1000)
        self.assertTrue(doc["matches_capture"])
        self.assertEqual(intake["capture_sha256"], hashlib.sha256(capture.read_bytes()).hexdigest())
        self.assertTrue(da.source_gaps(self.bundle))
        original = self.bundle / "docs" / "captured.txt"
        original.write_bytes(b"A different original, preserved.")
        split_capture.run(capture, self.bundle)
        self.assertEqual(original.read_bytes(), b"A different original, preserved.")
        self.assertFalse(json.loads((self.bundle / "notes" / "intake.json").read_bytes())["documents"][0]["matches_capture"])

    def test_complete_replacement_capture_resolves_gap_and_preserves_history(self):
        capture = self.root / "capture.md"
        capture.write_bytes(("## Documents\n\n### Doc 1 · recovered.txt\n**Report**\n"
                             "100 tokens · 1,000 characters\n"
                             "> **Incomplete:** only 500 of 1,000 characters are shown\n\n"
                             "A clipped excerpt.\n").encode())
        split_capture.run(capture, self.bundle)
        self.assertTrue(da.source_gaps(self.bundle))
        capture.write_bytes(("## Documents\n\n### Doc 1 · recovered.txt\n**Report**\n"
                             "100 tokens · 1,000 characters\n\nA newly supplied complete original.\n").encode())
        split_capture.run(capture, self.bundle, force=True)
        intake = json.loads((self.bundle / "notes" / "intake.json").read_bytes())
        self.assertFalse(intake["documents"][0]["incomplete"])
        self.assertTrue(intake["documents"][0]["matches_capture"])
        self.assertTrue(intake["history"][0]["documents"][0]["incomplete"])
        self.assertEqual(da.source_gaps(self.bundle), [])
        self.assertEqual(cq.source_completeness(cq.Bundle(self.bundle)), [])
        before = (self.bundle / "notes" / "intake.json").read_bytes()
        split_capture.run(capture, self.bundle, force=True)
        self.assertEqual(before, (self.bundle / "notes" / "intake.json").read_bytes())

    def test_report_and_replay_do_not_promote_or_mutate_historical_failure(self):
        failed = QUESTION.replace("## Blind solve\n", "## Blind solve\n- 2026-10-05 | rev: 0 | platform quick test | result: solved | tiers: Low 5/5 · Medium — · High — | feedback: Too easy\n")
        self.path.write_bytes(failed.encode())
        before = self.path.read_bytes()
        report = da.report(self.bundle, "q01")
        self.assertIsNotNone(report["latest_platform_record"])
        replay = da.replay(self.root)
        self.assertEqual(replay["count"], 1)
        self.assertTrue(replay["questions"][0]["ready_gate_failures"])
        self.assertEqual(self.path.read_bytes(), before)

    def test_report_reads_platform_section_without_local_checks_and_surfaces_latest_failure(self):
        digest = cq.submission_sha256(*cq.parse(self.path), cq.Bundle(self.bundle))
        text = QUESTION + ("\n## Platform validation\n"
            f"- 2026-10-08 | rev: 0 | platform difficulty check | tested_sha256: {digest} | "
            "platform_verdict: pass | passed_tier: easy | tiers: Easy 1/5 | feedback: Passed easy verification\n")
        self.path.write_bytes(text.encode())
        result = da.report(self.bundle, "q01")
        self.assertEqual(result["latest_platform_record"]["platform_verdict"], "pass")
        self.assertTrue(result["latest_platform_record_current"])
        self.assertEqual(len(result["current_revision_records"]), 1)
        self.assertEqual(da.replay(self.root)["questions"][0]["platform_records"][0]["platform_verdict"], "pass")
        text += (f"- 2026-10-08 | rev: 0 | platform difficulty check | tested_sha256: {digest} | "
                 "platform_verdict: fail | tiers: Easy 5/5 | feedback: Too easy\n")
        self.path.write_bytes(text.encode())
        self.assertEqual(da.report(self.bundle, "q01")["latest_platform_record"]["platform_verdict"], "fail")
        self.assertTrue(any("platform_verdict" in finding
                            for finding in da.replay(self.root)["questions"][0]["ready_gate_failures"]))
        self.assertEqual(self.path.read_bytes(), text.encode())
        self.path.write_bytes(text.replace("regional freight", "freight operator").encode())
        self.assertFalse(da.report(self.bundle, "q01")["latest_platform_record_current"])

    def test_checks_clearance_is_separate_from_difficulty_and_invalidates_on_edit(self):
        prepared = da.prepare(self.bundle, "q01")
        digest = prepared["tested_sha256"]
        ready = QUESTION.replace("status: draft", "status: ready") + (
            "\n## Platform validation\n"
            f"- 2026-10-08 | rev: 0 | platform difficulty check | tested_sha256: {digest} | "
            "platform_verdict: pass | passed_tier: easy | tiers: Easy 1/5 | feedback: Passed easy verification\n")
        self.path.write_bytes(ready.encode())
        self.assertTrue(da.report(self.bundle, "q01")["mechanical_failures"])
        # Reuse the complete form fixture; this test measures status separation, not prose quality.
        from test_docket_tools import GOOD
        mode = GOOD.split("## Targeted failure modes\n", 1)[1].split("\n## ", 1)[0]
        ready += "\n## Targeted failure modes\n" + mode
        self.path.write_bytes(ready.encode())
        before = self.path.read_bytes()
        report = da.report(self.bundle, "q01")
        self.assertEqual(report["mechanical_failures"], [])
        self.assertFalse(report["submission_clearance_recorded"])
        self.assertEqual(report["quality_checks"]["blocking_clearance"], "unknown")
        capture = self.root / "checks.txt"
        capture.write_text("Checks\n" + "\n".join(f"- {name}: Passed" for name in pc.CHECKS), encoding="utf-8")
        pc.record_capture(self.bundle, "q01", capture, 0, digest)
        report = da.report(self.bundle, "q01")
        self.assertTrue(report["submission_clearance_recorded"])
        self.assertTrue(report["quality_checks"]["all_checks_passed"])
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(cq.handover(self.bundle, ["q01"]), 0)
        handover = (self.bundle / "notes" / "handover-q01.md").read_text(encoding="utf-8")
        self.assertIn("Submission clearance recorded: yes", handover)
        self.assertEqual(self.path.read_bytes(), before)
        self.path.write_bytes(ready.replace("regional freight", "freight operator").encode())
        report = da.report(self.bundle, "q01")
        self.assertFalse(report["submission_clearance_recorded"])
        self.assertFalse(report["quality_checks"]["current"])

    def test_record_checks_cli_requires_explicit_version_and_preserves_question(self):
        prepared = da.prepare(self.bundle, "q01")
        capture = self.root / "checks.txt"
        capture.write_text("Checks\n" + "\n".join(f"- {name}: Passed" for name in pc.CHECKS), encoding="utf-8")
        args = ["record-checks", str(self.bundle), "--q", "q01", "--capture", str(capture)]
        before = self.path.read_bytes()
        with mock.patch.object(da, "ROOT", self.root), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(da.main(args), 1)
            self.assertFalse((self.bundle / "notes" / "platform-checks-q01.json").exists())
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(da.main(args + ["--revision", "0", "--tested-sha256", prepared["tested_sha256"]]), 0)
            self.assertEqual(da.main(["report", str(self.bundle), "--q", "q01", "--revision", "0"]), 1)
        self.assertEqual(self.path.read_bytes(), before)
        report = da.report(self.bundle, "q01")
        self.assertEqual(report["quality_checks"]["blocking_clearance"], "clear")
        self.assertFalse(report["submission_clearance_recorded"], "Checks alone cannot establish difficulty readiness")

    def hard(self, status: str = "checked") -> None:
        self.path.write_bytes(QUESTION.replace("difficulty_target: easy", "difficulty_target: hard")
                              .replace("status: draft", f"status: {status}").encode())

    def codes(self, level: str = "FAIL") -> set[str]:
        return {code for found, code, _ in cq.check(self.path, cq.Bundle(self.bundle))[2] if found == level}

    def test_screen_packet_holds_only_the_sentence_and_documents_and_binds_the_guard(self):
        sketch = self.write_sketch()
        before = sketch.read_bytes()
        result = da.screen_packet(self.bundle, idea="i01")
        packet = Path(result["packet"])
        files = {str(p.relative_to(packet)).replace("\\", "/") for p in packet.rglob("*") if p.is_file()}
        self.assertEqual(files, {"question.txt", "docs/D01.txt", "docs/D02.txt",
                                 "text/D01.txt", "text/D02.txt", "text/manifest.json"})
        content = b"".join(p.read_bytes() for p in packet.rglob("*") if p.is_file())
        self.assertNotIn(b"SECRET_WRITER_NOTES", content)
        self.assertNotIn(b"+$2.8 million", content, "the gold never enters a screen packet")
        self.assertIsNone(self.access(packet / "docs" / "D01.txt"))
        for path in (Path(result["run"]) / "screen.json", packet / "question.txt", sketch):
            with self.subTest(path=path):
                self.assertIsNotNone(self.access(path))
        self.assertEqual(sketch.read_bytes(), before)
        self.assertEqual(result, da.screen_packet(self.bundle, idea="i01"), "an intact packet is reused")
        # The same sentence carried word for word into a question file shares the binding.
        self.assertEqual(da.screen_packet(self.bundle, qid="q01")["screen_sha256"], result["screen_sha256"])
        (packet / "text" / "D01.txt").write_bytes(b"Altered saved source")
        with self.assertRaisesRegex(ValueError, "refusing reuse"):
            da.screen_packet(self.bundle, idea="i01")
        with self.assertRaisesRegex(ValueError, "exactly one"):
            da.screen_packet(self.bundle, idea="i01", qid="q01")

    def test_live_hard_target_needs_a_strong_screen_record_and_an_all_right_screen_only_warns(self):
        # 2026-10-14: 14 of 14 runs that started at the High model failed, none screened beforehand.
        self.hard()
        self.assertIn("strong-screen", self.codes())
        self.write_sketch()
        da.screen_packet(self.bundle, idea="i01")
        with self.assertRaisesRegex(ValueError, "exactly 3"):
            da.record_screen(self.bundle, idea="i01", results=["right", "contaminated", "wrong"], note="x")
        with self.assertRaisesRegex(ValueError, "one-line note"):
            da.record_screen(self.bundle, idea="i01", results=["right", "wrong", "right"], note="a | b")
        result = da.record_screen(self.bundle, idea="i01", results=["right", "wrong", "contaminated", "right"],
                                  note="the miss took the 2024 restated figure", today="2026-10-14")
        self.assertEqual(result["decision"], "may offer")
        self.assertIn("right: 2/3 | decision: may offer", result["line"])
        self.assertIn("claude-opus-5-5", result["line"])
        self.assertNotIn("strong-screen", self.codes())
        self.assertNotIn("strong-screen", self.codes("WARN"))
        _, sec = cq.parse(self.bundle / "notes" / "sketches" / "i01.md")
        self.assertEqual(sec["question"], cq.parse(self.path)[1]["question"], "recording never edits the sentence")
        # A later all-right screen of the same sentence warns: the screen ranks and the user decides
        # (aq-05049, 2026-10-14: withholding 3/3 sketches drew "you even didn't give me any questions").
        da.record_screen(self.bundle, idea="i01", results=["right"] * 3, note="all three found the clause")
        self.assertNotIn("strong-screen", self.codes())
        self.assertIn("strong-screen", self.codes("WARN"))
        sketch = self.bundle / "notes" / "sketches" / "i01.md"
        sketch.write_bytes(sketch.read_bytes().replace(b"difficulty_target: easy", b"difficulty_target: hard"))
        screened = da.screen(self.bundle, "i01")
        self.assertTrue(screened["eligible_for_full_writeup"], "a 3/3 screen ranks a sketch; it never withholds it")
        self.assertTrue(any("right in every fresh solve" in warning for warning in screened["warnings"]))
        # Any change to the sentence needs its own screen.
        self.path.write_bytes(self.path.read_bytes().replace(b"regional freight", b"freight operator"))
        self.assertIn("strong-screen", self.codes())

    def test_strong_screen_applies_only_to_live_explicit_hard_targets(self):
        self.assertNotIn("strong-screen", self.codes())  # easy target
        self.hard("draft")
        self.assertIn("strong-screen", self.codes())
        self.path.write_bytes(QUESTION.replace("difficulty_target: easy\n", "").encode())  # legacy, targetless
        self.assertNotIn("strong-screen", self.codes())
        self.write_sketch()
        da.screen_packet(self.bundle, idea="i01")
        self.hard()
        da.record_screen(self.bundle, idea="i01", results=["wrong"] * 3, note="all three gave 2.6")
        self.assertNotIn("strong-screen", self.codes())
        self.assertIn("strong-screen", self.codes("WARN"), "every strong solve missing fails the High check too")

    def test_screen_cli_records_against_the_current_sentence_only(self):
        self.write_sketch()
        with mock.patch.object(da, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()) as out, \
                contextlib.redirect_stderr(io.StringIO()) as err:
            self.assertEqual(da.main(["record-screen", str(self.bundle), "--idea", "i01",
                                      "--results", "right,wrong,right", "--note", "x"]), 1)
            self.assertIn("run packet first", err.getvalue())
            self.assertEqual(da.main(["packet", str(self.bundle), "--idea", "i01"]), 0)
            self.assertEqual(da.main(["record-screen", str(self.bundle), "--idea", "i01", "--results",
                                      "right,wrong,right", "--note", "the miss stopped at the summary table"]), 0)
            self.assertEqual(da.main(["packet", str(self.bundle), "--idea", "i01", "--note", "x"]), 1)
        self.assertIn("may offer", out.getvalue())
        digest = cq.screen_sha256(cq.parse(self.path)[1]["question"], cq.Bundle(self.bundle))
        self.assertEqual([r["right"] for r in cq.screen_records(cq.Bundle(self.bundle), digest)], [2])
        sketch = self.bundle / "notes" / "sketches" / "i01.md"
        sketch.write_bytes(sketch.read_bytes().replace(b"freight revenue", b"freight income"))
        with mock.patch.object(da, "ROOT", self.root), contextlib.redirect_stderr(io.StringIO()) as err:
            self.assertEqual(da.main(["record-screen", str(self.bundle), "--idea", "i01", "--results",
                                      "wrong,wrong,right", "--note", "x"]), 1)
        self.assertIn("run packet first", err.getvalue(), "a changed sentence cannot inherit the old packet")


if __name__ == "__main__":
    unittest.main(verbosity=2)
