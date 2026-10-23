import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.config_manager import (
    ConfigurationError,
    load_config,
    save_config,
    validate_config,
)

class TestConfigManager(unittest.TestCase):

    def test_save_and_load_config(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"

            config = {
                "model": "demo-model",
                "temperature": 0.7,
                "max_tokens": 500,
            }

            save_config(config, path)
            loaded = load_config(path)

            self.assertEqual(loaded, config)

    def test_invalid_config_type(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"

            with self.assertRaises(TypeError):
                save_config("invalid config", path)

    def test_missing_config_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "missing.json"

            with self.assertRaises(ConfigurationError):
                load_config(path)

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"
            path.write_text("{invalid json}", encoding="utf-8")

            with self.assertRaises(ConfigurationError):
                load_config(path)

    def test_json_array_instead_of_object(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"
            path.write_text(
                json.dumps(["model-a", "model-b"]),
                encoding="utf-8",
            )

            with self.assertRaises(ConfigurationError):
                load_config(path)

    def test_valid_configuration(self):
        config = {
            "model": "demo-model",
            "temperature": 0.7,
            "max_tokens": 500,
        }

        self.assertEqual(validate_config(config), config)

    def test_empty_model(self):
        config = {
            "model": "   ",
            "temperature": 0.7,
            "max_tokens": 500,
        }

        with self.assertRaises(ConfigurationError):
            validate_config(config)

    def test_invalid_temperature(self):
        config = {
            "model": "demo-model",
            "temperature": 3.0,
            "max_tokens": 500,
        }

        with self.assertRaises(ConfigurationError):
            validate_config(config)

    def test_invalid_max_tokens(self):
        config = {
            "model": "demo-model",
            "temperature": 0.7,
            "max_tokens": -10,
        }

        with self.assertRaises(ConfigurationError):
            validate_config(config)
    def test_atomic_write_failure_preserves_original(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "config.json"

            original_config = {
                "model": "original-model",
                "temperature": 0.5,
                "max_tokens": 300,
            }

            updated_config = {
                "model": "updated-model",
                "temperature": 0.8,
                "max_tokens": 600,
            }

            save_config(original_config, path)

            with patch(
                "src.config_manager.os.replace",
                side_effect=OSError("Simulated write failure"),
            ):
                with self.assertRaises(ConfigurationError):
                    save_config(updated_config, path)

            self.assertEqual(load_config(path), original_config)