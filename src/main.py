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


def main():
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
