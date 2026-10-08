import unittest

from src.student import Student
from src.course import Course

class TestStudent(unittest.TestCase):

    def test_student_creation(self):
        student = Student("Aqsa", 5)

        self.assertEqual(student.name, "Aqsa")
        self.assertEqual(student.study_hours, 5)

    def test_valid_study_hours(self):
        student = Student("Aqsa", 5)

        student.study_hours = 8

        self.assertEqual(student.study_hours, 8)

    def test_negative_study_hours(self):
        student = Student("Aqsa", 5)

        with self.assertRaises(ValueError):
            student.study_hours = -3

    def test_invalid_study_hours_type(self):
        student = Student("Aqsa", 5)

        with self.assertRaises(TypeError):
            student.study_hours = "five"

    def test_string_representation(self):
        student = Student("Aqsa", 5)

        self.assertEqual(
            str(student),
            "Aqsa studies 5 hours."
        )

    def test_repr(self):
        student = Student("Aqsa", 5)

        self.assertEqual(
            repr(student),
            "Student('Aqsa', 5)"
        )


    def test_student_with_course(self):
        course = Course("AI Engineering", 12)
        student = Student("Aqsa", 5, course)

        self.assertIs(student.course, course)
        self.assertEqual(
            student.course_info(),
            "Aqsa is enrolled in AI Engineering."
        )

    def test_student_without_course(self):
        student = Student("Aqsa", 5)

        self.assertIsNone(student.course)
        self.assertEqual(
            student.course_info(),
            "No course assigned."
        )

    def test_invalid_course_type(self):
        with self.assertRaises(TypeError):
            Student("Aqsa", 5, "AI Engineering")


if __name__ == "__main__":
    unittest.main()