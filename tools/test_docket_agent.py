"""Test Docket snapshot isolation, source provenance and fail-closed tool access.

Usage: python tools/test_docket_agent.py
All fixtures and packets live in temporary task roots. These tests do not invoke models,
write workspace task data or measure platform difficulty.
"""
from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

import agent_scope
import check_questions as cq
import docket_agent as da
import split_capture

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
        result = da.prepare(self.bundle, "q01")
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

    def test_prepare_idempotent_and_refuses_tampered_or_contaminated_packets(self):
        first = da.prepare(self.bundle, "q01")
        self.assertEqual(first, da.prepare(self.bundle, "q01"))
        packet = Path(first["packets"]["solver-1"])
        (packet / "answer.md").write_bytes(b"Leaked answer")
        with self.assertRaisesRegex(ValueError, "refusing reuse"):
            da.prepare(self.bundle, "q01")
        (packet / "answer.md").unlink()
        (packet / "text" / "D01.txt").write_bytes(b"Modified document")
        with self.assertRaisesRegex(ValueError, "refusing reuse"):
            da.prepare(self.bundle, "q01")

    def test_snapshot_gold_edit_cannot_reuse_unchanged_fingerprint(self):
        result = da.prepare(self.bundle, "q01")
        snapshot_path = Path(result["run"]) / "snapshot.json"
        snapshot = json.loads(snapshot_path.read_bytes())
        snapshot["sections"]["answer"] = "$100 million"
        snapshot_path.write_bytes(da.json_bytes(snapshot))
        with self.assertRaisesRegex(ValueError, "Frozen submission fields changed"):
            da.prepare(self.bundle, "q01")

    def test_snapshot_version_preserves_old_runs_and_detects_gap_metadata_tampering(self):
        digest = cq.submission_sha256(*cq.parse(self.path), cq.Bundle(self.bundle))
        old_run = self.bundle / "runs" / f"q01-r0-{digest}"
        old_run.mkdir(parents=True)
        (old_run / "snapshot.json").write_bytes(b'{"schema":1}')
        result = da.prepare(self.bundle, "q01")
        self.assertNotEqual(Path(result["run"]), old_run)
        self.assertEqual((old_run / "snapshot.json").read_bytes(), b'{"schema":1}')
        snapshot_path = Path(result["run"]) / "snapshot.json"
        snapshot = json.loads(snapshot_path.read_bytes())
        snapshot["source_gaps"] = ["Forged source-gap list"]
        snapshot_path.write_bytes(da.json_bytes(snapshot))
        with self.assertRaisesRegex(ValueError, "Frozen source-gap metadata changed"):
            da.prepare(self.bundle, "q01")

    def test_source_or_question_edit_produces_new_fingerprint_and_run(self):
        first = da.prepare(self.bundle, "q01")
        (self.bundle / "docs" / "D01.txt").write_bytes(b"Changed original bytes.\n")
        second = da.prepare(self.bundle, "q01")
        self.assertNotEqual(first["tested_sha256"], second["tested_sha256"])
        self.assertNotEqual(first["run"], second["run"])
        self.path.write_bytes(QUESTION.replace("regional freight", "freight operator").encode())
        third = da.prepare(self.bundle, "q01")
        self.assertNotEqual(second["tested_sha256"], third["tested_sha256"])
        self.assertTrue(Path(first["run"]).is_dir())

    def test_scope_requires_binding_and_denies_other_bundles_runs_notes(self):
        self.assertIsNotNone(self.access(self.bundle / "text" / "D01.txt"))
        result = da.prepare(self.bundle, "q01")
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
        first = da.prepare(self.bundle, "q01")
        second = da.prepare(self.make_second_bundle(), "q01")
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
        first = da.prepare(self.bundle, "q01")
        run_name = Path(first["run"]).name
        binding = self.root / ".claude" / "solver-scope.json"
        binding.write_bytes(json.dumps({"schema": 1, "bundle": "freight", "run": run_name}).encode())
        self.assertIsNone(self.access(Path(first["packets"]["shortcut"]) / "docs" / "D02.txt"))
        other = da.prepare(self.make_second_bundle(), "q01")
        self.assertEqual(other["bound_runs"], [f"cargo/{Path(other['run']).name}", f"freight/{run_name}"])
        scope = json.loads(binding.read_bytes())
        scope["runs"].append({"bundle": "freight", "run": "vanished-run", "bound_at": scope["runs"][0]["bound_at"]})
        scope["runs"][1]["bound_at"] -= da.BINDING_TTL_SECONDS + 1
        binding.write_bytes(da.json_bytes(scope))
        again = da.bind_scope(self.root, "cargo", Path(other["run"]).name)
        self.assertEqual([(entry["bundle"], entry["run"]) for entry in again], [("cargo", Path(other["run"]).name)])
        self.assertIsNotNone(self.access(Path(first["packets"]["shortcut"]) / "docs" / "D02.txt"))

    def test_guard_accepts_schema_two_only_with_safe_entries(self):
        result = da.prepare(self.bundle, "q01")
        binding = self.root / ".claude" / "solver-scope.json"
        target = Path(result["packets"]["solver-1"]) / "text" / "D01.txt"
        for broken in ({"schema": 2, "runs": []}, {"schema": 2, "runs": [{"bundle": "../x", "run": "r"}]},
                       {"schema": 2, "runs": "freight"}, ["freight"]):
            with self.subTest(binding=broken):
                binding.write_bytes(json.dumps(broken).encode())
                self.assertIsNotNone(self.access(target))

    def test_guard_rejects_malformed_inputs_and_windows_escape_globs(self):
        da.prepare(self.bundle, "q01")
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
            da.prepare(self.bundle, "q01")

    def test_template_gitkeep_is_inert_but_nonempty_hidden_files_are_rejected(self):
        before = da.prepare(self.bundle, "q01")
        for folder in ("docs", "text"):
            (self.bundle / folder / ".gitkeep").write_bytes(b"")
        self.assertEqual(before, da.prepare(self.bundle, "q01"))
        (self.bundle / "text" / ".gitkeep").write_bytes(b"Hidden leaked answer")
        with self.assertRaisesRegex(ValueError, "Unexpected corpus file"):
            da.prepare(self.bundle, "q01")

    def test_prepare_refuses_invalid_floor_and_frozen_questions(self):
        for value, error in ((QUESTION.replace("difficulty_target: easy", ""), "explicit difficulty_target"),
                             (QUESTION.replace("status: draft", "status: accepted"), "frozen"),
                             (QUESTION.replace("Revenue for calendar 2024 was $409.8 million.", "Wrong quote from the document."), "mechanical floor")):
            self.path.write_bytes(value.encode())
            with self.subTest(error=error), self.assertRaisesRegex(ValueError, error):
                da.prepare(self.bundle, "q01")
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


if __name__ == "__main__":
    unittest.main(verbosity=2)
