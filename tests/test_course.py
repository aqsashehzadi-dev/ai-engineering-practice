import unittest

from src.course import Course


class TestCourse(unittest.TestCase):

    def test_valid_course(self):
        course = Course("AI Engineering", 12)

        self.assertEqual(course.name, "AI Engineering")
        self.assertEqual(course.duration_weeks, 12)

    def test_course_name_normalization(self):
        course = Course("  Python  ", 8)

        self.assertEqual(course.name, "Python")

    def test_empty_course_name(self):
        with self.assertRaises(ValueError):
            Course("   ", 12)

    def test_invalid_course_name_type(self):
        with self.assertRaises(TypeError):
            Course(123, 12)

    def test_invalid_duration_type(self):
        with self.assertRaises(TypeError):
            Course("Python", "eight")

    def test_negative_duration(self):
        with self.assertRaises(ValueError):
            Course("Python", -5)

    def test_zero_duration(self):
        with self.assertRaises(ValueError):
            Course("Python", 0)

    def test_course_str(self):
        course = Course("AI Engineering", 12)

        self.assertEqual(
            str(course),
            "AI Engineering (12 weeks)"
        )

    def test_course_repr(self):
        course = Course("AI Engineering", 12)

        self.assertEqual(
            repr(course),
            "Course('AI Engineering', 12)"
        )


if __name__ == "__main__":
    unittest.main()