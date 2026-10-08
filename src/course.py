class Course:
    def __init__(self, name, duration_weeks):
        if not isinstance(name, str):
            raise TypeError("Course name must be a string.")

        if not name.strip():
            raise ValueError("Course name cannot be empty.")

        if type(duration_weeks) is not int:
            raise TypeError("Duration must be an integer.")

        if duration_weeks <= 0:
            raise ValueError("Duration must be positive.")

        self.name = name.strip()
        self.duration_weeks = duration_weeks

    def __str__(self):
        return f"{self.name} ({self.duration_weeks} weeks)"

    def __repr__(self):
        return (
            f"Course({self.name!r}, "
            f"{self.duration_weeks!r})"
        )