# Learning Notes — Python Environment Setup

## Date

September 2026

## Project

AI Engineering Practice

## Topic

Python Virtual Environment and Dependency Management

---

## 1. Objective

Set up and verify an isolated Python development environment for the AI Engineering Practice project.

The goal was to ensure that the project uses its own Python environment and dependencies instead of relying on the system-wide Python installation.

---

## 2. Python Version

Verified Python version:

```text
Python 3.14.7
```

---

## 3. Virtual Environment

Created a virtual environment named:

```text
.venv
```

Project location:

```text
C:\Users\dell\Desktop\ai-engineering-practice
```

The virtual environment is located at:

```text
C:\Users\dell\Desktop\ai-engineering-practice\.venv
```

---

## 4. Activation Issue

While activating the virtual environment in PowerShell, an execution-policy restriction was encountered.

The issue was investigated rather than bypassed blindly.

The PowerShell execution policy was configured appropriately, allowing the activation script to run.

The virtual environment was then activated successfully.

Current terminal prompt:

```text
(.venv) PS C:\Users\dell\Desktop\ai-engineering-practice>
```

The `(.venv)` prefix confirms that the virtual environment is active.

---

## 5. Python Verification

Ran:

```powershell
python --version
```

Result:

```text
Python 3.14.7
```

Then verified which Python executable was being used:

```powershell
where.exe python
```

The first result was:

```text
C:\Users\dell\Desktop\ai-engineering-practice\.venv\Scripts\python.exe
```

This confirms that the project is using the Python executable from the virtual environment.

---

## 6. pip Verification

Ran:

```powershell
python -m pip --version
```

Result:

```text
pip 26.2.1 from C:\Users\dell\Desktop\ai-engineering-practice\.venv\Lib\site-packages\pip (python 3.14)
```

This confirms that pip is installed and being used from the project's virtual environment.

---

## 7. What I Learned

* A virtual environment isolates project dependencies from the system Python installation.
* The `(.venv)` prefix in PowerShell indicates that the environment is active.
* `where.exe python` can be used to verify which Python executable is being selected.
* `python -m pip --version` can verify that pip belongs to the active Python environment.
* PowerShell execution policies can affect whether activation scripts are allowed to run.
* Troubleshooting the activation problem provided a practical Break → Debug → Improve experience.

---

## 8. Commands Practiced

```powershell
python --version
where.exe python
python -m pip --version
```

Virtual environment activation:

```powershell
.venv\Scripts\Activate.ps1
```

---

## 9. Current Status

**Environment setup: COMPLETE ✅**

The Python virtual environment is active and verified.

No external Python packages have been installed yet.

---

## 10. Next Step

Proceed with the next Python engineering task while continuing to follow:

**Learn → Build → Break → Debug → Improve → Document → Ship → Review → Share**
## 11. First Python Program and Debugging Exercise

Created the first Python program in `src/main.py`.

The program uses a `main()` function and the standard:

```python
if __name__ == "__main__":
    main()

pattern.

Build

The program successfully printed:

AI Engineering Practice Started
Break

A missing closing parenthesis was intentionally introduced:

print("AI Engineering Practice Started"

Python produced:

SyntaxError: '(' was never closed
Debug

The traceback identified the problematic line. The missing ) was restored.

Result

The program executed successfully again.

Learning

I practiced reading a Python traceback, identifying a syntax error, fixing the source code, and verifying the fix by running the program again.

Workflow practiced:

Build → Run → Break → Debug → Fix → Run Again
## 12. Functions, User Input, and Validation

Updated `src/main.py` to create a reusable `greet()` function.

The function accepts a name and returns a greeting:

```python
def greet(name):
    return f"Hello, {name}!"

The program now accepts user input at runtime:

name = input("Enter your name: ")
Input Validation

Added validation using:

if name.strip():

This prevents the program from accepting an empty or whitespace-only name.

Tests

Empty input:

Enter your name:
Name cannot be empty.

Valid input:

Enter your name: Aqsa
Hello, Aqsa!
Learning

I practiced:

Function parameters
Arguments
Return values
User input
Conditional statements
String methods
Basic input validation
Testing both valid and invalid inputs

Workflow practiced:

Build → Test → Handle Invalid Input → Test Again