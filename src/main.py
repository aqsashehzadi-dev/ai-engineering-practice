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


def main():
    analyze_student_skills()
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

    name = input("Enter your name: ").strip()

    if name:
        message = greet(name)
        print(message)
    else:
        print("Name cannot be empty.")


if __name__ == "__main__":
    main()
