def greet(name):
    return f"Hello, {name}!"


def show_skills(skills):
    for skill in skills:
        print(skill)


def show_unique_skills(skills):
    unique_skills = set(skills)
    print("Unique Skills:")
    for skill in unique_skills:
        print(skill)


def show_profile(profile):
    print("Learning Profile:")
    for key, value in profile.items():
        print(f"{key}: {value}")


def get_learning_profile():
    return "Python", "AI Engineering"


courses = {
    "Python": 5000,
    "Git": 3000,
    "SQL": 4000
}
def get_course_price(course_name):
    normalized_name = course_name.strip().lower()
    for name, price in courses.items():
        if name.lower() == normalized_name:
            return price
    return None


def calculate_discount(price, discount_percent):
    if discount_percent < 0 or discount_percent > 100:
        return "Invalid discount."
    discount_amount = price * discount_percent / 100
    return price - discount_amount


def calculate_course_fee(course_name, discount_percent=0):
    price = get_course_price(course_name)
    if price is None:
        return "Course not found."
    return calculate_discount(price, discount_percent)


def analyze_student_skills():
    students = [
        {"name": "Aqsa", "skills": ["Python", "Git", "SQL"]},
        {"name": "Ali", "skills": ["Git", "JavaScript", "SQL"]}
    ]
    unique_skills = set()
    for student in students:
        unique_skills.update(student["skills"])
    print("Unique Skills:", unique_skills)

    skill_counts = {}
    for student in students:
        for skill in student["skills"]:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1
    print("Skill Counts:", skill_counts)

    if skill_counts:
        max_count = max(skill_counts.values())
        most_common_skills = []
        for skill, count in skill_counts.items():
            if count == max_count:
                most_common_skills.append(skill)
        print("Most Common Skills:", most_common_skills)
    else:
        print("No skill data available.")

    student_summaries = []
    for student in students:
        student_summaries.append((student["name"], len(student["skills"])))
    print("Student Summaries:")
    for name, count in student_summaries:
        print(f"{name} has {count} skills")
    target_skill = "Python"
    matching_students = []
    for student in students:
        if target_skill in student["skills"]:
            matching_students.append(student["name"])
    if matching_students:
        print(f"Students with {target_skill}:", matching_students)
    else:
        print(f"No students found with {target_skill} skill.")


def analyze_course_enrollments():
    enrollments = [
        {"student": "Aqsa", "course": "Python", "status": "Active"},
        {"student": "Ali", "course": "Git", "status": "Active"},
        {"student": "Sara", "course": "Python", "status": "Completed"},
        {"student": "Aqsa", "course": "Git", "status": "Completed"},
        {"student": "Aqsa", "course": "Python", "status": "Active"},
    ]

    if not enrollments:
        print("No enrollment data available.")
        return

    unique_courses = set()
    course_counts = {}
    status_groups = {}
    course_students = {}
    student_courses = {}

    for enrollment in enrollments:
        student = enrollment["student"]
        course = enrollment["course"]
        status = enrollment.get("status", "Unknown")

        unique_courses.add(course)

        course_counts[course] = course_counts.get(course, 0) + 1

        status_groups.setdefault(status, [])
        status_groups[status].append(student)

        course_students.setdefault(course, [])
        course_students[course].append(student)

        student_courses.setdefault(student, set())
        student_courses[student].add(course)

    print("Unique Courses:", unique_courses)
    print("Course Counts:", course_counts)

    print("Students by Status:")
    for status, students in status_groups.items():
        print(f"{status}: {students}")

    print("Students by Course:")
    for course, students in course_students.items():
        print(f"{course}: {students}")

    print("Courses by Student:")
    for student, courses in student_courses.items():
        print(f"{student}: {courses}")


def main():
    analyze_student_skills()
    analyze_course_enrollments()
    skills = ["Python", "GitHub", "VS Code", "Python", "GitHub"]
    show_skills(skills)
    show_unique_skills(skills)

    profile = {
        "language": "Python",
        "field": "AI Engineering",
        "status": "Learning"
    }
    show_profile(profile)

    language, field = get_learning_profile()
    print(f"Learning: {language} | Direction: {field}")
    print("Course Fee Tests:")
    print(calculate_course_fee("Python"))
    print(calculate_course_fee("Python", 20))
    print(calculate_course_fee("  SQL  ", 25))
    print(calculate_course_fee("Git", 10))
    print(calculate_course_fee("Java"))
    print(calculate_course_fee("Python", 120))

    name = input("Enter your name: ").strip()

    if name:
        message = greet(name)
        print(message)
    else:
        print("Name cannot be empty.")


if __name__ == "__main__":
    main()
