import unittest

from src.prompt_validator import (
    InvalidPromptError,
    validate_prompt,
)


class TestPromptValidator(unittest.TestCase):

    def test_valid_prompt(self):
        result = validate_prompt("Explain Python")
        self.assertEqual(result, "Explain Python")

    def test_prompt_normalization(self):
        result = validate_prompt("  Explain AI  ")
        self.assertEqual(result, "Explain AI")

    def test_empty_prompt(self):
        with self.assertRaises(InvalidPromptError):
            validate_prompt("")

    def test_whitespace_prompt(self):
        with self.assertRaises(InvalidPromptError):
            validate_prompt("   ")

    def test_invalid_prompt_type(self):
        with self.assertRaises(TypeError):
            validate_prompt(123)

    def test_intentional_failure(self):
        result = validate_prompt("  Hello AI  ")
        self.assertEqual(result, "Hello AI")