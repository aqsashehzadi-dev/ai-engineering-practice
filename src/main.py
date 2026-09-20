def greet(name):
    return f"Hello, {name}!"

def show_skills(skills):
    for skill in skills:
        print(skill)


def main():
    skills = ["Python", "GitHub", "VS Code"]
    show_skills(skills)
    name = input("Enter your name: ").strip()

    if name:
        message = greet(name)
        print(message)
    else:
        print("Name cannot be empty.")


if __name__ == "__main__":
    main()