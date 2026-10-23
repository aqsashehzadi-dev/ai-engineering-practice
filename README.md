# AI Engineering Practice

A hands-on Python learning repository focused on building strong programming foundations, software engineering skills, and practical AI engineering capabilities.

## Project Objectives

- Develop clean, readable, and maintainable Python code.
- Practice object-oriented programming and modular development.
- Implement input validation and error handling.
- Write automated tests to verify functionality.
- Build practical software engineering skills using Git and GitHub.

## Technologies

- Python 3.14
- Visual Studio Code
- Git and GitHub
- Python Virtual Environments (`venv`)
- Python `unittest`

## Project Structure

```text
ai-engineering-practice/
├── src/
│   ├── main.py
│   ├── calculator.py
│   ├── analytics.py
│   ├── course_fees.py
│   ├── person.py
│   ├── student.py
│   ├── course.py
│   └── utils/
├── tests/
│   ├── test_person.py
│   ├── test_student.py
│   └── test_course.py
├── docs/
├── README.md
└── LEARNING_NOTES.md
```
## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/aqsashehzadi-dev/ai-engineering-practice.git
cd ai-engineering-practice
```

### 2. Create a virtual environment
```powershell
python -m venv .venv
```

### 3. Activate the virtual environment (Windows PowerShell)
```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Run automated tests
```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

## Object-Oriented Programming

Implemented a student and course management model using three classes:

- **Person:** Parent class responsible for name validation and normalization.
- **Student:** Inherits from `Person`, validates study hours, and supports course enrollment.
- **Course:** Represents a course with validated name and duration.

### OOP Concepts

- Classes and objects
- Constructors (`__init__`)
- Inheritance and `super()`
- Encapsulation with properties
- Composition (Student HAS-A Course)
- Input validation and exception handling
- Special methods (`__str__` and `__repr__`)

## Automated Testing

Created 23 automated unit tests covering the `Person`, `Student`, and `Course` classes.

Run tests from the project root:

```powershell
python -m unittest discover -s tests -p "test_*.py" -v
```

**Latest test result:** 23 tests passed, 0 failures.

## Learning Progress

- Python fundamentals and functions
- Data structures and input validation
- Modular programming
- Object-oriented programming
- Automated unit testing
- Git and GitHub workflows

## Key Learning Outcomes

Through this repository, I have practiced:

- Designing reusable Python classes using inheritance and composition.
- Implementing input validation and encapsulation through properties.
- Writing automated unit tests for valid and invalid inputs.
- Organizing Python code into modules and packages.
- Debugging errors and improving code reliability.
- Documenting development progress and maintaining projects with Git and GitHub.

## Future Development

Continue developing Python projects, improving testing practices, and progressing toward practical AI engineering applications.
