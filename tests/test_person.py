import unittest

from src.person import Person


class TestPerson(unittest.TestCase):

    def test_valid_name(self):
        person = Person("Aqsa")
        self.assertEqual(person.name, "Aqsa")

    def test_name_normalization(self):
        person = Person("  Aqsa  ")
        self.assertEqual(person.name, "Aqsa")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            Person("   ")

    def test_invalid_name_type(self):
        with self.assertRaises(TypeError):
            Person(123)

    def test_introduce(self):
        person = Person("Aqsa")
        self.assertEqual(
            person.introduce(),
            "My name is Aqsa."
        )


if __name__ == "__main__":
    unittest.main()