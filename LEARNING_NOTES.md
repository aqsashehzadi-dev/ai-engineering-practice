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
---

## 13. Git Repository, GitHub SSH, and First Push

### Git Repository Setup

Initialized the `ai-engineering-practice` project as a Git repository:

```bash
git init
```

The repository initially used the `master` branch, so I renamed it to `main`:

```bash
git branch -M main
```

Verified the repository using:

```bash
git status
```

### `.gitignore`

Created a `.gitignore` file to prevent local and unnecessary files from being committed.

The project ignores:

```gitignore
.venv/
__pycache__/
*.py[cod]
.env
.env.*
.vscode/
```

This keeps the virtual environment, Python cache files, environment-variable files, and local VS Code settings out of the repository.

### Staging and First Commit

Added the project files to the Git staging area:

```bash
git add .
```

Verified the staged files with:

```bash
git status
```

Created the first meaningful commit:

```bash
git commit -m "Set up Python project and add input validation"
```

The first commit included:

* `.gitignore`
* `LEARNING_NOTES.md`
* `README.md`
* `src/main.py`

After the commit, I verified:

```text
On branch main
nothing to commit, working tree clean
```

### Connecting the Local Repository to GitHub

Created a GitHub repository named:

```text
ai-engineering-practice
```

Added the GitHub repository as the `origin` remote using SSH:

```bash
git remote add origin git@github.com:aqsashehzadi-dev/ai-engineering-practice.git
```

Verified it with:

```bash
git remote -v
```

### SSH Authentication Problem

The first push failed with:

```text
git@github.com: Permission denied (publickey).
fatal: Could not read from remote repository.
```

Testing SSH also initially returned:

```text
git@github.com: Permission denied (publickey).
```

I checked the existing SSH files and confirmed that the GitHub-specific key already existed:

```text
github_aqsa_ed25519
github_aqsa_ed25519.pub
```

I then checked the SSH agent:

```bash
ssh-add -l
```

It returned:

```text
Error connecting to agent: No such file or directory
```

The Windows OpenSSH Authentication Agent was checked with:

```powershell
Get-Service ssh-agent
```

Its status was:

```text
Stopped
```

### Starting the Windows SSH Agent

In Administrator PowerShell, I configured the SSH agent to start automatically:

```powershell
Set-Service -Name ssh-agent -StartupType Automatic
```

Then started it:

```powershell
Start-Service ssh-agent
```

Verified that its status was:

```text
Running
```

Added the existing GitHub SSH private key to the agent:

```powershell
ssh-add C:\Users\dell\.ssh\github_aqsa_ed25519
```

GitHub authentication was then successfully verified:

```bash
ssh -T git@github.com
```

Result:

```text
Hi aqsashehzadi-dev! You've successfully authenticated, but GitHub does not provide shell access.
```

### Diagnosing Git's SSH Client

Although manual SSH authentication worked, `git push` still returned:

```text
Permission denied (publickey).
```

I used Git tracing and remote testing to investigate the issue:

```powershell
$env:GIT_TRACE=1
git ls-remote origin
```

I checked the SSH executable used by PowerShell:

```powershell
Get-Command ssh | Select-Object -ExpandProperty Source
```

It returned:

```text
C:\Windows\System32\OpenSSH\ssh.exe
```

Git for Windows also had its own bundled SSH executable:

```text
C:\Program Files\Git\usr\bin\ssh.exe
```

Testing the Git-bundled SSH directly failed with:

```text
git@github.com: Permission denied (publickey).
```

This showed that Windows OpenSSH could authenticate successfully with the loaded key, while the Git-bundled SSH client could not use the authentication setup successfully.

### Configuring Git to Use Windows OpenSSH

Configured Git globally to use Windows OpenSSH:

```bash
git config --global core.sshCommand "C:/Windows/System32/OpenSSH/ssh.exe"
```

Verified the configuration:

```bash
git config --global --get core.sshCommand
```

Result:

```text
C:/Windows/System32/OpenSSH/ssh.exe
```

Disabled Git tracing after debugging:

```powershell
Remove-Item Env:GIT_TRACE
```

Then tested remote access:

```bash
git ls-remote origin
```

The command completed without an authentication error.

### First Successful GitHub Push

Pushed the local `main` branch to GitHub:

```bash
git push -u origin main
```

The push succeeded:

```text
[new branch] main -> main
branch 'main' set up to track 'origin/main'.
```

Final verification:

```bash
git status
```

Result:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### Learning

I practiced:

* Initializing a Git repository
* Renaming a Git branch
* Understanding untracked and staged files
* Creating a `.gitignore`
* Creating a meaningful Git commit
* Adding and verifying a GitHub remote
* Using SSH authentication with GitHub
* Checking existing SSH keys
* Understanding the role of `ssh-agent`
* Starting and configuring the Windows SSH agent
* Loading an SSH private key with `ssh-add`
* Testing GitHub SSH authentication
* Diagnosing `Permission denied (publickey)`
* Using `GIT_TRACE` for Git debugging
* Identifying different SSH executables
* Configuring Git to use Windows OpenSSH
* Testing remote repository access
* Pushing a branch to GitHub
* Setting an upstream branch
* Verifying a clean and synchronized working tree

### Workflow Practiced

**Build → Test → Debug → Diagnose → Fix → Verify → Document → Ship**
---

## 14. Input Normalization and Validation

Improved `src/main.py` to clean user input before validating it.

Previously, the program checked the input using:

```python
name = input("Enter your name: ")

if name.strip():
```

This correctly rejected empty or whitespace-only input, but the cleaned value was not stored. Therefore, input such as:

```text
   Aqsa   
```

could still contain leading and trailing spaces when passed to `greet()`.

### Debugging the Input

Temporarily used:

```python
print(repr(name))
```

to make whitespace visible.

For input containing spaces around the name, `repr()` showed:

```text
'   Aqsa   '
```

This confirmed that the original string still contained the whitespace.

### Input Normalization

Updated the input statement to:

```python
name = input("Enter your name: ").strip()
```

Now `.strip()` removes leading and trailing whitespace immediately and stores the cleaned value in `name`.

Because `name` is already normalized, the validation can be simplified to:

```python
if name:
```

The program now follows this flow:

**Raw Input → Normalize → Validate → Process**

### Testing

Tested a normal valid name:

```text
Enter your name: Aqsa
Hello, Aqsa!
```

Tested a name with leading and trailing spaces:

```text
Enter your name:    Aqsa
Hello, Aqsa!
```

The extra whitespace was removed successfully.

Tested whitespace-only input:

```text
Enter your name:
Name cannot be empty.
```

The whitespace-only value became an empty string after `.strip()` and was correctly rejected.

### Regression Testing

After simplifying:

```python
if name.strip():
```

to:

```python
if name:
```

I tested the valid and invalid input paths again.

Both continued to work correctly.

This demonstrated a basic form of regression testing: after changing or simplifying code, verify that previously working behavior still works.

### Learning

I practiced:

* String normalization with `.strip()`
* Difference between validation and normalization
* Inspecting strings with `repr()`
* Debugging hidden whitespace
* Testing edge cases
* Simplifying redundant code
* Using truthiness of strings with `if name:`
* Regression testing after a code change
* Inspecting changes with `git diff`

### Workflow Practiced

**Build → Break → Debug → Improve → Test → Inspect → Document**
## Section 15 — Python Lists and Practical Integration

### What I Learned

I practiced Python lists using the interactive Python REPL and then applied them to the actual project.

### List Basics

Created a list:

```python
skills = ["Python", "Git", "GitHub"]
```

I learned that Python lists:

* Can store multiple values.
* Use zero-based indexing.
* Support negative indexing.
* Are mutable, so their contents can be changed after creation.

### Indexing and Length

```python
skills[0]
skills[-1]
len(skills)
```

I learned:

* Index `0` accesses the first item.
* Index `-1` accesses the last item.
* `len()` returns the number of items in a list.
* Accessing an index that does not exist raises an `IndexError`.

### Modifying Lists

I practiced:

```python
skills.append("VS Code")
skills[1] = "Git Basics"
skills.remove("Git Basics")
```

I learned that list methods and index assignment can modify the original list.

Trying to remove a value that does not exist produced:

```text
ValueError: list.remove(x): x not in list
```

I learned to avoid this by checking membership first:

```python
if "Java" in skills:
    skills.remove("Java")
```

### Iterating Through Lists

I used a `for` loop:

```python
for skill in skills:
    print(skill)
```

I also combined loops, conditions, and f-strings:

```python
for skill in skills:
    if skill == "Python":
        print("Python is my main language")
    else:
        print(f"Also learning {skill}")
```

This helped me understand nested indentation and decision-making while processing list items.

### List Slicing

I practiced:

```python
skills[0:2]
skills[:2]
skills[1:]
skills[-2:]
skills[::2]
skills[::-1]
```

I learned the general slicing pattern:

```text
[start:stop:step]
```

The start index is included and the stop index is excluded.

I also learned that slicing such as `skills[::-1]` returns a new list and does not modify the original list.

### Sorting

I practiced:

```python
skills.sort()
sorted(skills, reverse=True)
```

I learned:

* `sort()` modifies the original list.
* `sorted()` returns a new sorted list without changing the original list.

### Removing and Returning Items

I practiced:

```python
removed_skill = skills.pop()
first_skill = skills.pop(0)
```

I learned that `pop()` removes an item and also returns the removed value.

### append() vs extend()

I practiced:

```python
skills.extend(["GitHub", "VS Code"])
skills.append(["HTML", "CSS"])
```

I learned:

* `extend()` adds multiple items individually.
* `append()` adds its argument as one item.
* Appending another list can create a nested list.

### Nested Lists

Example:

```python
skills = ["Python", "GitHub", "VS Code", ["HTML", "CSS"]]
```

I accessed nested values using:

```python
skills[3][0]
skills[3][1]
```

This returned `"HTML"` and `"CSS"`.

### Applying Lists to the Project

I added a reusable function:

```python
def show_skills(skills):
    for skill in skills:
        print(skill)
```

Inside `main()`, I created and passed a list:

```python
skills = ["Python", "GitHub", "VS Code"]
show_skills(skills)
```

This connected lists, functions, parameters, arguments, and loops in the actual program.

### Testing

I tested:

* Normal name input.
* Empty input.
* Whitespace-only input.
* Skills list output.

The existing name validation continued to work after adding the new list functionality.

### Development Workflow Practiced

```text
Learn → Build → Break → Debug → Improve → Test → Inspect → Document
```

Before staging the changes, I used:

```bash
git diff
```

to inspect exactly what had changed.

## Section 16 — Python Tuples, Immutability, and Unpacking

### What I Learned

I practiced Python tuples in the interactive Python REPL and then integrated tuple returning and unpacking into the actual project.

### Creating a Tuple

```python
skills = ("Python", "GitHub", "VS Code")
```

A tuple is an ordered collection. Like lists, tuple elements can be accessed using indexes.

### Indexing, Length, and Slicing

```python
skills[0]
skills[-1]
len(skills)
skills[0:2]
```

I learned that:

* Tuples use zero-based indexing.
* Negative indexes can access elements from the end.
* `len()` returns the number of elements.
* Tuples support slicing.
* A tuple slice returns another tuple.

### Tuple Immutability

I intentionally tried:

```python
skills[0] = "Java"
```

Python raised:

```text
TypeError: 'tuple' object does not support item assignment
```

This demonstrated that tuples are immutable: their elements cannot be directly replaced after creation.

### Membership and Iteration

I practiced membership checking:

```python
"GitHub" in skills
```

and iteration:

```python
for skill in skills:
    print(skill)
```

Tuples support both membership operators and `for` loops.

### Single-Item Tuples

I learned an important syntax difference:

```python
("Python")    # string
("Python",)   # tuple
```

A comma is required to create a single-item tuple.

### Tuple Unpacking

I practiced:

```python
language, platform, editor = skills
```

The tuple values were assigned to variables according to their order.

I also intentionally tried to unpack three values into only two variables:

```python
first, second = skills
```

This raised:

```text
ValueError: too many values to unpack (expected 2, got 3)
```

### Starred Unpacking

I used:

```python
first, *rest = skills
```

This assigned the first tuple value to `first` and collected the remaining values into `rest`.

I verified that `rest` is a list:

```python
type(rest)
```

### Tuple Methods

I practiced `count()`:

```python
numbers = (10, 20, 10, 30, 10)
numbers.count(10)
```

and `index()`:

```python
numbers.index(30)
numbers.index(10)
```

I learned that:

* `count()` returns how many times a value occurs.
* `index()` returns the index of the first occurrence.

Searching for a missing value with `index()` raised a `ValueError`.

I avoided this using defensive programming:

```python
if 50 in numbers:
    print(numbers.index(50))
```

### Tuple and List Conversion

I converted a tuple to a list:

```python
skills_list = list(skills)
```

Because lists are mutable, I could then modify an element:

```python
skills_list[0] = "Java"
```

The original tuple remained unchanged.

I also converted the list back to a tuple:

```python
new_tuple = tuple(skills_list)
```

### Tuple Concatenation and Repetition

I practiced concatenation:

```python
more_skills = skills + ("Git", "SQL")
```

This created a new tuple without modifying the original tuple.

I also practiced repetition:

```python
("Python",) * 3
```

### Returning Multiple Values from a Function

I created:

```python
def get_profile():
    return "Aqsa", "Python", "AI Engineering"
```

The returned values were stored as a tuple.

I also unpacked them directly:

```python
name, language, field = get_profile()
```

### Mutable Objects Inside Tuples

I created a tuple containing a list:

```python
data = ("Aqsa", ["Python", "GitHub"])
```

I could modify the list inside the tuple:

```python
data[1].append("VS Code")
```

However, replacing the tuple element itself was not allowed:

```python
data[1] = ["Java"]
```

This raised a `TypeError`.

I learned that a tuple is immutable, but a mutable object stored inside it can still change internally.

### Nested Indexing

I practiced:

```python
data[1][0]
```

The first index accessed the list inside the tuple, and the second index accessed an element inside that list.

### List vs Tuple

I learned the practical distinction:

* Use a **list** when the collection needs to be modified.
* Use a **tuple** when the collection represents values that should remain fixed.

### Applying Tuples to the Project

I added a function that returns multiple values:

```python
def get_learning_profile():
    return "Python", "AI Engineering"
```

Inside `main()`, I unpacked the returned tuple:

```python
language, field = get_learning_profile()
print(f"Learning: {language} | Direction: {field}")
```

### Testing

I tested:

* Tuple functionality in the Python REPL.
* Normal name input after project integration.
* Empty name input.
* Whitespace-only name input.
* Existing skills list output.
* Learning profile output.

All existing functionality continued to work after the tuple integration.

### Development Workflow Practiced

```text
Learn → Build → Break → Debug → Improve → Test → Inspect → Document
```

Before documenting and staging the changes, I inspected the project code using:

```bash
git diff src/main.py
```



