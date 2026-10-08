from src.person import Person
from src.course import Course
class Student(Person):
    def __init__(self, name, study_hours=0, course=None):
        super().__init__(name)
        self._study_hours = 0
        self.study_hours = study_hours

        if course is not None and not isinstance(course, Course):
            raise TypeError("Course must be a Course object.")

        self.course = course
    @property
    def study_hours(self):
        return self._study_hours

    @study_hours.setter
    def study_hours(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Study hours must be a number.")

        if value < 0:
            raise ValueError("Study hours cannot be negative.")

        self._study_hours = value


    def course_info(self):
        if self.course is None:
            return "No course assigned."

        return f"{self.name} is enrolled in {self.course.name}."


    def __str__(self):
        return f"{self.name} studies {self.study_hours} hours."

    def __repr__(self):
        return f"Student({self.name!r}, {self.study_hours!r})"