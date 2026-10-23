import csv
import tempfile
import unittest
from pathlib import Path

from src.results_manager import save_result


class TestResultsManager(unittest.TestCase):

    def test_save_result(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "results.csv"

            save_result(
                "Explain Python",
                "Python is a programming language.",
                "success",
                path,
            )

            with path.open("r", newline="", encoding="utf-8") as file:
                rows = list(csv.DictReader(file))

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["prompt"], "Explain Python")
            self.assertEqual(rows[0]["status"], "success")

    def test_multiple_results(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "results.csv"

            save_result("Prompt 1", "Response 1", "success", path)
            save_result("Prompt 2", "Response 2", "success", path)

            with path.open("r", newline="", encoding="utf-8") as file:
                rows = list(csv.DictReader(file))

            self.assertEqual(len(rows), 2)
            self.assertEqual(
                rows[1]["response"],
                "Response 2",
            )

    def test_header_not_duplicated(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "results.csv"

            save_result("Prompt 1", "Response 1", "success", path)
            save_result("Prompt 2", "Response 2", "success", path)

            content = path.read_text(encoding="utf-8")

            self.assertEqual(
                content.count("prompt,response,status"),
                1,
            )

    def test_empty_prompt(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "results.csv"

            with self.assertRaises(ValueError):
                save_result("", "Response", "success", path)

    def test_invalid_field_type(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "results.csv"

            with self.assertRaises(TypeError):
                save_result("Explain AI", 123, "success", path)