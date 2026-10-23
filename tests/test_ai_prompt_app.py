import csv
import tempfile
import unittest
from pathlib import Path

from src.ai_prompt_app import process_prompt
from src.config_manager import save_config
from src.prompt_validator import InvalidPromptError


class TestAIPromptApp(unittest.TestCase):

    def test_complete_workflow(self):
        with tempfile.TemporaryDirectory() as folder:
            folder_path = Path(folder)

            config_path = folder_path / "config.json"
            results_path = folder_path / "results.csv"

            config = {
                "model": "demo-model",
                "temperature": 0.7,
                "max_tokens": 500,
            }

            save_config(config, config_path)

            response = process_prompt(
                "  Explain Python  ",
                config_path,
                results_path,
            )

            self.assertEqual(
                response,
                "Demo response from demo-model: Explain Python",
            )

            with results_path.open(
                "r", newline="", encoding="utf-8"
            ) as file:
                rows = list(csv.DictReader(file))

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["prompt"], "Explain Python")
            self.assertEqual(rows[0]["response"], response)
            self.assertEqual(rows[0]["status"], "success")

    def test_invalid_prompt_does_not_create_results(self):
        with tempfile.TemporaryDirectory() as folder:
            folder_path = Path(folder)

            config_path = folder_path / "config.json"
            results_path = folder_path / "results.csv"

            save_config(
                {
                    "model": "demo-model",
                    "temperature": 0.7,
                    "max_tokens": 500,
                },
                config_path,
            )

            with self.assertRaises(InvalidPromptError):
                process_prompt("   ", config_path, results_path)

            self.assertFalse(results_path.exists())