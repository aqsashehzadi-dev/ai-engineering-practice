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

### 4. Install Project Dependencies

Install the dependencies listed in `requirements.txt`:
```powershell
python -m pip install -r requirements.txt
```

### 5. Run automated tests
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

**Latest test result:** Created 46 automated tests covering OOP classes, prompt validation, JSON configuration management, CSV storage, and application integration.

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

## AI Prompt Processing & Configuration Manager

Developed a modular Python application to practice robust error handling, file operations, configuration management, logging, and automated testing in an AI-oriented workflow.

### Features

- **Prompt Validation:** Validates input types, removes surrounding whitespace, and rejects empty prompts using custom exceptions.
- **JSON Configuration Management:** Saves, loads, and validates application settings.
- **Atomic File Writing:** Uses temporary files and `os.replace()` to reduce the risk of corrupting existing configuration files during failed writes.
- **CSV Results Storage:** Stores processed prompts, demo responses, and execution status in CSV format.
- **Logging:** Records successful operations and provides exception tracebacks for debugging.
- **Automated Testing:** Includes unit tests, simulated failures, and end-to-end integration tests.

### Application Workflow

```text
User Prompt
    |
    v
Prompt Validation
    |
    v
JSON Configuration Loading
    |
    v
Local Demo Response
    |
    v
CSV Results Storage
    |
    v
Logging
```

**Note:** This application uses simulated responses for software engineering practice. It does not currently connect to a real AI model or external API.

### New Project Files

```text
src/
├── ai_prompt_app.py
├── prompt_validator.py
├── config_manager.py
└── results_manager.py

tests/
├── test_ai_prompt_app.py
├── test_prompt_validator.py
├── test_config_manager.py
└── test_results_manager.py

data/
├── ai_config.json
└── prompt_results.csv   # Generated locally; Git-ignored
```

### Running the Application

From the project root:

```powershell
python -m src.ai_prompt_app
```

Example output:

```text
INFO:src.results_manager:Prompt result saved successfully.
INFO:__main__:Prompt processed successfully.
Demo response from demo-model: Explain AI Engineering
```

### Testing

Run the complete automated test suite:

```powershell
python -m unittest discover -s tests -v
```

**Latest verified result:** 46 tests passed, 0 failures.

### Engineering Concepts Practiced

- Custom exceptions and exception chaining
- Input and configuration validation
- JSON serialization and deserialization
- CSV file operations
- Atomic file replacement
- Logging and debugging
- Unit and integration testing
- Failure simulation using `unittest.mock`
- Modular Python application design

### Development Methodology

Learn → Build → Break → Debug → Improve → Document → Ship → Review → Share
