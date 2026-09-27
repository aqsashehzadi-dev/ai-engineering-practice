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
