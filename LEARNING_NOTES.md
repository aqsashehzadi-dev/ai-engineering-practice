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
## 17. Python Sets, Set Operations, and Unique Data

### What I Learned

A Python **set** is an unordered collection of unique elements. Sets are useful when duplicate values should be removed, membership needs to be checked, or different collections need to be compared.

### Creating a Set

```python
skills = {"Python", "GitHub", "VS Code"}
```

A set may display its elements in a different order because set ordering should not be relied upon.

### Set Length

```python
len(skills)
```

`len()` returns the number of unique elements in the set.

### Sets Automatically Remove Duplicates

```python
numbers = {10, 20, 10, 30, 20}
```

Result:

```python
{10, 20, 30}
```

Duplicate values are stored only once.

### Membership Checking

```python
20 in numbers
50 in numbers
```

Results:

```text
True
False
```

The `in` operator checks whether an element exists in a set.

### Adding Elements

A single element can be added using `add()`:

```python
skills.add("Git")
```

Adding an element that already exists does not create a duplicate.

Multiple elements can be added using `update()`:

```python
skills.update(["Git", "SQL"])
```

### Removing Elements with `remove()`

```python
skills.remove("Git")
```

If the requested element does not exist:

```python
skills.remove("Java")
```

Python raises:

```text
KeyError: 'Java'
```

### Safe Removal with `discard()`

```python
skills.discard("Java")
```

Unlike `remove()`, `discard()` does not raise an error when the element does not exist.

### Set Union

```python
backend_skills = {"Python", "SQL", "Git"}
ai_skills = {"Python", "Machine Learning", "SQL"}

backend_skills | ai_skills
```

Union contains all unique elements from both sets.

Method form:

```python
backend_skills.union(ai_skills)
```

### Set Intersection

```python
backend_skills & ai_skills
```

Result contains elements that exist in both sets:

```python
{"Python", "SQL"}
```

Method form:

```python
backend_skills.intersection(ai_skills)
```

### Set Difference

```python
backend_skills - ai_skills
```

This returns elements that exist in `backend_skills` but not in `ai_skills`.

Reverse difference:

```python
ai_skills - backend_skills
```

Difference is direction-dependent.

### Symmetric Difference

```python
backend_skills ^ ai_skills
```

This returns elements that exist in either set but are not common to both.

### Subsets and Supersets

```python
core_skills = {"Python", "SQL"}

core_skills.issubset(backend_skills)
backend_skills.issuperset(core_skills)
```

A subset contains only elements that are also present in the other set.

A superset contains all elements of the smaller set.

### Proper Subsets

```python
{"Python", "SQL"} < {"Python", "SQL", "Git"}
```

Result:

```text
True
```

`<` checks for a proper subset.

Equal sets are not proper subsets:

```python
{"Python", "SQL"} < {"Python", "SQL"}
```

Result:

```text
False
```

`<=` allows equality:

```python
{"Python", "SQL"} <= {"Python", "SQL"}
```

Result:

```text
True
```

Similarly:

* `>` checks for a proper superset.
* `>=` checks for a superset and allows equality.

### Iterating Through a Set

```python
for skill in skills:
    print(skill)
```

Sets can be iterated with a `for` loop, but code should not rely on a particular iteration order.

### Empty Sets

This does **not** create an empty set:

```python
empty_set = {}
```

Its type is:

```text
<class 'dict'>
```

The correct way is:

```python
empty_set = set()
```

Its type is:

```text
<class 'set'>
```

### Sets Do Not Support Indexing

Intentional test:

```python
skills[0]
```

Result:

```text
TypeError: 'set' object is not subscriptable
```

Sets do not provide positional indexing like lists and tuples.

### Hashable Set Elements

A list cannot be stored directly inside a set:

```python
test_set = {"Python", ["Git", "GitHub"]}
```

This raises a `TypeError` because a list is unhashable.

A tuple containing hashable values can be used:

```python
test_set = {"Python", ("Git", "GitHub")}
```

Not every tuple is automatically hashable. If a tuple contains an unhashable object such as a list, that tuple cannot be used as a set element.

### Removing Duplicates from a List

```python
languages = ["Python", "Java", "Python", "SQL", "Java"]

unique_languages = set(languages)
```

The duplicate values are removed.

The original list remains unchanged.

The set can be converted back into a list:

```python
unique_languages_list = list(unique_languages)
```

This produces a list of unique values, but the original list order should not be assumed to be preserved through the set conversion.

### `pop()` with Sets

```python
removed_skill = skills.pop()
```

`pop()` removes and returns an arbitrary element from a non-empty set. Code should not depend on which element is removed.

Calling `pop()` on an empty set:

```python
temp_skills.pop()
```

raises:

```text
KeyError: 'pop from an empty set'
```

### Clearing a Set

```python
temp_skills.clear()
```

`clear()` removes all elements while the set object still exists.

An empty set displays as:

```python
set()
```

### Disjoint Sets

```python
frontend_skills = {"HTML", "CSS", "JavaScript"}

frontend_skills.isdisjoint(backend_skills)
```

`True` means the sets have no common elements.

After adding a common element:

```python
frontend_skills.add("Python")
```

`isdisjoint()` returns `False`.

### Set Comprehension

A set can be created using comprehension syntax:

```python
squares = {number ** 2 for number in range(1, 6)}
```

A condition can also be included:

```python
even_squares = {
    number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}
```

This creates a set containing the squares of even numbers.

### `union()` vs `update()`

```python
combined_skills = backend_skills.union(ai_skills)
```

`union()` returns a new set and does not modify the original sets.

In contrast:

```python
practice_skills.update(ai_skills)
```

`update()` modifies the existing set in place.

### Copying Sets

```python
practice_skills = backend_skills.copy()
```

A copy can be modified independently without changing the original set.

### `difference_update()`

```python
practice_backend = backend_skills.copy()

practice_backend.difference_update({"SQL", "Java"})
```

`difference_update()` modifies the existing set in place by removing matching elements.

Missing elements such as `"Java"` are ignored.

### `intersection_update()`

```python
practice_backend = backend_skills.copy()

practice_backend.intersection_update({"Python", "Java", "SQL"})
```

The existing set is modified so that only common elements remain.

### `symmetric_difference_update()`

```python
practice_backend = backend_skills.copy()

practice_backend.symmetric_difference_update(
    {"Python", "Java", "SQL"}
)
```

The existing set is modified so that only elements that are not common to both sets remain.

### Set Equality

Set equality is based on elements rather than display order:

```python
{"Python", "Git", "SQL"} == {"SQL", "Python", "Git"}
```

Result:

```text
True
```

### Frozen Sets

A `frozenset` is an immutable version of a set:

```python
fixed_skills = frozenset({"Python", "Git", "SQL"})
```

Its type is:

```text
<class 'frozenset'>
```

Trying to modify it:

```python
fixed_skills.add("Machine Learning")
```

raises an `AttributeError` because `frozenset` does not provide `add()`.

Membership checking still works:

```python
"Python" in fixed_skills
```

Non-mutating set operations also work:

```python
fixed_skills | {"Machine Learning"}
```

This returns a new `frozenset` while the original remains unchanged.

Because a `frozenset` is hashable when its elements are hashable, it can itself be stored inside a set:

```python
skill_groups = {
    fixed_skills,
    frozenset({"HTML", "CSS"})
}
```

### Practical List vs Set Difference

A list is useful when:

* order matters,
* duplicates are allowed,
* positional indexing is required.

A set is useful when:

* unique values are required,
* duplicate removal is needed,
* membership checking is important,
* collections need union/intersection/difference operations.

### Project Integration

The existing project was extended with:

```python
def show_unique_skills(skills):
    unique_skills = set(skills)
    print("Unique Skills:")
    for skill in unique_skills:
        print(skill)
```

The skills list intentionally included duplicate values:

```python
skills = [
    "Python",
    "GitHub",
    "VS Code",
    "Python",
    "GitHub"
]
```

The function was called using:

```python
show_unique_skills(skills)
```

The normal list output showed duplicates, while the set-based output showed each skill only once.

The order of unique skills changed between runs, reinforcing that set order should not be relied upon.

### Regression Testing

After integrating Sets, the program was tested with:

* a valid name,
* empty input,
* whitespace-only input.

Existing input normalization and validation continued to work correctly.

### Code Inspection

Before documentation and Git staging, the changes were inspected using:

```bash
git diff src/main.py
```

An accidental trailing-whitespace change was identified and removed before proceeding.

### Key Takeaways

* Sets store unique elements.
* Set ordering should not be relied upon.
* Sets do not support positional indexing.
* `add()` adds one element.
* `update()` adds multiple elements and mutates the set.
* `remove()` raises `KeyError` for a missing element.
* `discard()` safely ignores a missing element.
* Union combines unique elements.
* Intersection finds common elements.
* Difference is direction-dependent.
* Symmetric difference finds non-common elements.
* `issubset()`, `issuperset()`, and `isdisjoint()` compare relationships between sets.
* `copy()` allows safe independent modification.
* `difference_update()`, `intersection_update()`, and `symmetric_difference_update()` mutate an existing set.
* `{}` creates an empty dictionary, while `set()` creates an empty set.
* `frozenset` provides immutable set behavior.
* Sets are useful for deduplication and collection comparison.

### Workflow Practiced

Learn → Build → Break → Debug → Improve → Test → Inspect → Document

This continued the project workflow of learning Python concepts through practical experimentation and then integrating them into a real repository.

## 18. Python Dictionaries, Key-Value Data, and Practical Integration

### What I Learned

A Python dictionary stores data as **key-value pairs**.

```python
student = {
    "name": "Aqsa",
    "skill": "Python",
    "level": "Beginner"
}
```

Each key is used to access its corresponding value.

### Accessing Dictionary Values

Values can be accessed using their keys:

```python
student["name"]
student["skill"]
```

Trying to access a missing key with square brackets raises a `KeyError`:

```python
student["age"]
```

This was intentionally tested to understand dictionary errors.

### Safe Access with `get()`

The `get()` method can safely access a key without raising a `KeyError`:

```python
student.get("age")
```

If the key does not exist, it returns `None`.

A default value can also be supplied:

```python
student.get("age", "Not provided")
```

### Adding and Updating Key-Value Pairs

A new key-value pair can be added using assignment:

```python
student["field"] = "AI Engineering"
```

An existing value can be updated using its key:

```python
student["level"] = "Intermediate"
```

### Dictionary Length

`len()` returns the number of key-value pairs:

```python
len(student)
```

### Membership Testing

Using `in` directly with a dictionary checks its **keys**:

```python
"name" in student
```

Values can be checked explicitly:

```python
"Aqsa" in student.values()
```

### Dictionary Views

Important dictionary methods include:

```python
student.keys()
student.values()
student.items()
```

* `keys()` provides a view of the keys.
* `values()` provides a view of the values.
* `items()` provides key-value pairs as tuple-like pairs.

### Iterating Through Dictionaries

Iterating directly over a dictionary iterates over its keys:

```python
for key in student:
    print(key)
```

Values can be iterated with:

```python
for value in student.values():
    print(value)
```

Keys and values can be processed together using `items()` and tuple unpacking:

```python
for key, value in student.items():
    print(key, ":", value)
```

### Updating with `update()`

`update()` can modify existing keys and add new ones:

```python
student.update({"level": "Advanced Beginner"})
student.update({"city": "Gujranwala", "status": "Learning"})
```

### Removing Dictionary Items

`pop()` removes a specified key and returns its value:

```python
student.pop("status")
```

Trying to pop a missing key without a default raises `KeyError`.

A safe default can be supplied:

```python
student.pop("age", "Not found")
```

`popitem()` removes and returns the last inserted remaining key-value pair:

```python
student.popitem()
```

A specific key can also be deleted using:

```python
del student["field"]
```

Deleting a missing key raises `KeyError`.

### Empty Dictionaries

An empty dictionary can be created in two ways:

```python
empty_dict = {}
another_empty_dict = dict()
```

An important distinction is that `{}` creates an empty **dictionary**, not an empty set.

### Creating Dictionaries with `dict()`

A dictionary can also be created with the `dict()` constructor:

```python
profile = dict(
    name="Aqsa",
    skill="Python",
    level="Beginner"
)
```

### Duplicate Keys

Dictionary keys must be unique.

```python
{"skill": "Python", "skill": "Git"}
```

When duplicate keys occur during dictionary construction, the later value replaces the earlier value.

### Dictionary Keys and Hashability

Dictionary keys must be **hashable**.

A list cannot be used as a dictionary key:

```python
{["Python", "Git"]: "Skills"}
```

This intentionally produced a `TypeError`.

A tuple containing hashable elements can be a key:

```python
{("Python", "Git"): "Skills"}
```

However, a tuple is not automatically a valid key if it contains an unhashable object.

This was intentionally tested:

```python
{("Python", ["Git", "SQL"]): "Skills"}
```

It raised a `TypeError` because the tuple contained a mutable and unhashable list.

A nested tuple containing hashable values works:

```python
{("Python", ("Git", "SQL")): "Skills"}
```

### Mutable Dictionary Values

Although dictionary keys must be hashable, dictionary **values can be mutable**.

For example, a list can be stored as a value:

```python
skills_data = {
    "skills": ["Python", "Git", "SQL"]
}
```

The list can also be modified through the dictionary.

### Nested Dictionaries

A dictionary can contain another dictionary:

```python
student_data = {
    "name": "Aqsa",
    "learning": {
        "language": "Python",
        "field": "AI Engineering"
    }
}
```

Nested values can be accessed using multiple keys:

```python
student_data["learning"]["language"]
```

### Safe Nested Dictionary Access

Nested dictionaries can be accessed more safely using chained `get()` calls:

```python
safe_profile.get("learning", {}).get("language")
```

If the outer key does not exist, `{}` provides a safe fallback dictionary.

A final default value can also be supplied:

```python
safe_profile.get("education", {}).get(
    "degree",
    "Not provided"
)
```

This avoids a `KeyError` when expected nested data is missing.

### Lists of Dictionaries

Dictionaries can be stored inside lists:

```python
students = [
    {"name": "Aqsa", "skill": "Python"},
    {"name": "Ali", "skill": "Git"}
]
```

Individual dictionary values can then be accessed using list indexing followed by dictionary key access:

```python
students[0]["name"]
students[1]["skill"]
```

Lists of dictionaries can also be iterated:

```python
for student in students:
    print(student["name"], "-", student["skill"])
```

### `setdefault()`

`setdefault()` returns an existing value if the key already exists.

If the key is missing, it adds the key with the supplied default value:

```python
profile.setdefault("field", "AI Engineering")
```

It does not overwrite an existing value:

```python
profile.setdefault("skill", "Java")
```

If `"skill"` already contains `"Python"`, it remains `"Python"`.

### `dict.fromkeys()`

`dict.fromkeys()` can create multiple keys with the same initial value:

```python
topics = dict.fromkeys(
    ["Python", "Git", "SQL"],
    "Pending"
)
```

### Important `fromkeys()` Mutable-Value Gotcha

Using a mutable object as the shared value requires care:

```python
shared_lists = dict.fromkeys(
    ["Python", "Git"],
    []
)
```

Both keys reference the **same list object**.

Therefore:

```python
shared_lists["Python"].append("Learning")
```

resulted in both keys showing the change:

```python
{
    "Python": ["Learning"],
    "Git": ["Learning"]
}
```

When a separate mutable object is required for each key, a dictionary comprehension is safer:

```python
separate_lists = {
    key: []
    for key in ["Python", "Git"]
}
```

After:

```python
separate_lists["Python"].append("Learning")
```

only the `"Python"` list changed.

### Dictionary Comprehensions

Dictionaries can be generated concisely with comprehensions:

```python
squares = {
    number: number ** 2
    for number in range(1, 6)
}
```

Conditions can also be included:

```python
even_squares = {
    number: number ** 2
    for number in range(1, 11)
    if number % 2 == 0
}
```

### Copying Dictionaries

A shallow copy can be created with:

```python
profile_copy = profile.copy()
```

Changing a top-level immutable value in the copy does not change the original dictionary.

However, `copy()` is a **shallow copy**.

With nested mutable objects:

```python
original = {
    "name": "Aqsa",
    "skills": {
        "primary": "Python"
    }
}

copied = original.copy()
```

Changing:

```python
copied["skills"]["primary"] = "AI Engineering"
```

also affected the nested dictionary visible through `original`, because both outer dictionaries referenced the same nested mutable object.

This demonstrated the difference between copying the outer dictionary and independently copying nested mutable data.

### Dictionary Merge Operator

Dictionaries can be merged using `|`:

```python
combined = basic | advanced
```

This creates a new dictionary.

If both dictionaries contain the same key, the value from the dictionary on the right wins:

```python
{"Python": "Beginner"} | {
    "Python": "Intermediate"
}
```

The `|=` operator updates a dictionary in place:

```python
basic |= {"SQL": "Learning"}
```

### Dictionary Unpacking with `**`

Dictionary key-value pairs can be unpacked into another dictionary:

```python
full_profile = {
    **base_profile,
    "field": "AI Engineering"
}
```

If a later key duplicates an unpacked key, the later value replaces the earlier value:

```python
updated_profile = {
    **base_profile,
    "skill": "Machine Learning"
}
```

### Dictionary Equality and Insertion Order

Two dictionaries with the same key-value pairs compare equal even if they were created in different insertion orders.

Python dictionaries preserve **insertion order**.

For example:

```python
order_test = {
    "third": 3,
    "first": 1,
    "second": 2
}
```

keeps that insertion order during normal iteration/display.

Calling:

```python
sorted(order_test)
```

returns a sorted list of keys without modifying the original dictionary.

### Dynamic Dictionary Views

Dictionary views are dynamic.

For example:

```python
profile_keys = profile.keys()
```

If another key is later added to `profile`, the existing `profile_keys` view reflects that change automatically.

### Set-Like Operations on Dictionary Keys

Dictionary key views support useful set-like operations.

Given two dictionaries, common keys can be found with intersection:

```python
python_profile.keys() & ai_profile.keys()
```

Keys present only in the first dictionary can be found with difference:

```python
python_profile.keys() - ai_profile.keys()
```

Keys that occur in only one of the two dictionaries can be found with symmetric difference:

```python
python_profile.keys() ^ ai_profile.keys()
```

This connects dictionary key handling with previously learned set operations.

### Mixed Value Types

Dictionary values do not all need to have the same type.

For example:

```python
developer = {
    "name": "Aqsa",
    "skills": ["Python", "Git"],
    "experience": 0
}
```

A mutable nested list can be modified directly:

```python
developer["skills"].append("SQL")
```

### Key Existence vs `get()` Returning `None`

There is an important difference between checking whether a key exists and checking its value with `get()`.

For example:

```python
settings = {"theme": None}
```

This returns `True`:

```python
"theme" in settings
```

but:

```python
settings.get("theme")
```

returns `None`.

Therefore, `get()` returning `None` does not always mean the key is missing. The key may exist and actually contain `None`.

Use:

```python
key in dictionary
```

when the goal is specifically to test key existence.

### Counting with Dictionaries

Dictionaries are useful for frequency counting.

The pattern:

```python
counts["Python"] = counts.get("Python", 0) + 1
```

uses `get()` to return `0` when the key does not yet exist.

This was applied to a list:

```python
skills_list = [
    "Python",
    "Git",
    "Python",
    "SQL",
    "Git",
    "Python"
]

skill_counts = {}

for skill in skills_list:
    skill_counts[skill] = skill_counts.get(
        skill,
        0
    ) + 1
```

The resulting counts were:

```python
{
    "Python": 3,
    "Git": 2,
    "SQL": 1
}
```

### Creating a Dictionary with `zip()`

Two related iterables can be combined into a dictionary:

```python
names = ["Python", "Git", "SQL"]
statuses = ["Learning", "Done", "Pending"]

learning_status = dict(
    zip(names, statuses)
)
```

If the iterables have different lengths, normal `zip()` stops when the shortest iterable is exhausted.

### Reversing Keys and Values with a Comprehension

A dictionary can sometimes be reversed using:

```python
reversed_status = {
    value: key
    for key, value in learning_status.items()
}
```

However, this can lose information when multiple original keys have the same value.

For example:

```python
{
    "Python": "Learning",
    "SQL": "Learning"
}
```

cannot be safely reversed into a one-to-one dictionary because duplicate `"Learning"` keys would overwrite each other.

### Clearing a Dictionary

`clear()` removes all key-value pairs but keeps the dictionary variable:

```python
temp.clear()
```

The result is:

```python
{}
```

### Deleting an Entire Dictionary Variable

There is a difference between clearing a dictionary and deleting the variable itself.

```python
del delete_test
```

removes the variable name completely.

Trying to access it afterward raises `NameError`.

Therefore:

* `dictionary.clear()` → variable remains, but becomes empty.
* `del dictionary` → variable itself is removed.

### Practical Project Integration

Dictionary knowledge was integrated into `src/main.py`.

A reusable function was added:

```python
def show_profile(profile):
    print("Learning Profile:")
    for key, value in profile.items():
        print(f"{key}: {value}")
```

Inside `main()`, a dictionary was created:

```python
profile = {
    "language": "Python",
    "field": "AI Engineering",
    "status": "Learning"
}
```

It was passed to the function:

```python
show_profile(profile)
```

This demonstrated:

* Creating structured key-value data
* Passing a dictionary to a function
* Iterating with `items()`
* Tuple unpacking inside dictionary iteration
* Using dictionary data in a real project

### Testing and Regression Testing

The program was tested with valid input:

```text
Enter your name: Aqsa
Hello, Aqsa!
```

The existing whitespace validation was also retested.

Whitespace-only input correctly produced:

```text
Name cannot be empty.
```

This confirmed that the new dictionary functionality did not break existing project behavior.

### Code Inspection and Formatting

Before documenting or committing the changes, the source diff was inspected using:

```bash
git diff -- src/main.py
```

The inspection revealed formatting issues in the newly added dictionary block.

The indentation and extra whitespace were corrected.

VS Code's formatter was then used to apply consistent formatting, including proper spacing between top-level functions and a newline at the end of the file.

The program was run again after formatting to confirm that functionality remained correct.

### Key Takeaways

* Dictionaries store structured data as key-value pairs.
* Keys must be unique and hashable.
* Values may contain mutable objects such as lists and dictionaries.
* `get()` provides safer access when a key may be missing.
* `items()` is useful for iterating through keys and values together.
* Dictionaries can contain nested structures and can be stored inside lists.
* `update()`, `pop()`, `popitem()`, `del`, and `clear()` modify dictionary contents in different ways.
* Dictionary comprehensions provide a concise way to build dictionaries.
* `copy()` creates a shallow copy, so nested mutable objects require special care.
* `|`, `|=`, and `**` provide useful dictionary merging and unpacking techniques.
* Dictionary key views support useful set-like operations.
* `dict.fromkeys()` can unexpectedly share the same mutable object between multiple keys.
* Dictionaries are useful for counting, structured records, configuration-style data, and many other real programs.
* Existing functionality should always be regression-tested after integrating new features.

### Workflow Practiced

**Learn → Build → Break → Debug → Improve → Test → Inspect → Format → Document**

## 19. Data Structures & Problem Solving — Student Skills Analyzer

### Purpose

This practice combined Python lists, dictionaries, sets, and tuples to solve a practical data-analysis problem. The goal was to move beyond learning each data structure separately and use them together for storing, searching, filtering, counting, comparing, and summarizing student skill data.

### Data Structure Design

Student records were stored as dictionaries inside a list:

```python
students = [
    {"name": "Aqsa", "skills": ["Python", "Git", "SQL"]},
    {"name": "Ali", "skills": ["Git", "JavaScript", "SQL"]}
]
```

This structure combines:

* **List:** stores multiple student records.
* **Dictionary:** represents each student using key-value data.
* **Nested List:** stores multiple skills for each student.
* **Set:** is later used to collect unique skills and remove duplicates automatically.
* **Tuple:** is used to create fixed student summaries such as `("Aqsa", 3)`.

Nested data can be accessed step by step. For example:

```python
students[0]["skills"][0]
```

returns:

```text
Python
```

This means: select the first student, access that student's `"skills"` list, and then access the first skill.
### Unique Skills and Frequency Counting

A set was used to collect all unique skills:

```python
unique_skills = set()

for student in students:
    unique_skills.update(student["skills"])
```

Because sets do not store duplicate values, repeated skills such as `"Git"` and `"SQL"` appear only once.

A dictionary was then used to count how many students had each skill:

```python
skill_counts = {}

for student in students:
    for skill in student["skills"]:
        skill_counts[skill] = skill_counts.get(skill, 0) + 1
```

The result was:

```text
{'Python': 1, 'Git': 2, 'SQL': 2, 'JavaScript': 1}
```

The `.get(skill, 0)` pattern safely returns the current count when the skill already exists and `0` when it does not exist. Adding `1` updates the frequency without requiring a separate check for every new key.
### Most Common Skills and Tie Handling

Before using `max()`, the program checks whether `skill_counts` contains data:

```python
if skill_counts:
    max_count = max(skill_counts.values())
```

This prevents `max()` from being called on an empty collection.

Instead of assuming that only one skill can have the highest frequency, all skills with the maximum count are collected:

```python
most_common_skills = []

for skill, count in skill_counts.items():
    if count == max_count:
        most_common_skills.append(skill)
```

For the current student data, both `"Git"` and `"SQL"` have a count of `2`, so the result is:

```text
['Git', 'SQL']
```

This practice demonstrated an important problem-solving principle: code should correctly handle ties instead of assuming that a single maximum result always exists.

### Student Summaries and Tuple Unpacking

A list of tuples was created to store each student's name and number of skills:

```python
student_summaries = []

for student in students:
    student_summaries.append(
        (student["name"], len(student["skills"]))
    )
```

The resulting data has this form:

```text
[('Aqsa', 3), ('Ali', 3)]
```

Each tuple can then be unpacked directly inside a loop:

```python
for name, count in student_summaries:
    print(f"{name} has {count} skills")
```

Output:

```text
Aqsa has 3 skills
Ali has 3 skills
```

This combines lists, dictionaries, tuples, `len()`, loops, and tuple unpacking in one practical workflow.
### Filtering Students by Skill

A target skill can be used to search and filter students:

```python
target_skill = "Python"
matching_students = []

for student in students:
    if target_skill in student["skills"]:
        matching_students.append(student["name"])
```

For `"Python"`, the result is:

```text
['Aqsa']
```

Instead of only printing a matching student immediately, the matching names are stored in a list. This makes the result reusable later in the program.

The program also handles the case where no students match:

```python
if matching_students:
    print(f"Students with {target_skill}:", matching_students)
else:
    print(f"No students found with {target_skill} skill.")
```

When `"C++"` was tested and no student had that skill, the result was handled safely:

```text
No students found with C++ skill.
```

This practice combined membership testing with `in`, filtering, conditional logic, loops, dictionaries, nested lists, and result storage.
### Edge Cases and Defensive Programming

During practice, errors were intentionally triggered to understand how the program behaves with invalid or missing data.

#### Empty Data with `max()`

Calling `max()` on an empty collection caused:

```python
empty_counts = {}
max(empty_counts.values())
```

Result:

```text
ValueError: max() iterable argument is empty
```

The safer approach is to check that the dictionary contains data before calling `max()`:

```python
if empty_counts:
    max_count = max(empty_counts.values())
```

An empty case can also provide a meaningful message:

```python
if not empty_counts:
    print("No skill data available.")
```

#### Missing Dictionary Key

A student record without a `"skills"` key was tested:

```python
student_without_skills = {"name": "Sara"}
```

Direct access:

```python
student_without_skills["skills"]
```

caused:

```text
KeyError: 'skills'
```

Using `.get()` with a default empty list safely handled the missing key:

```python
student_without_skills.get("skills", [])
```

Result:

```text
[]
```

These tests demonstrated defensive programming: validate data and provide safe defaults before performing operations that may fail.
### Project Integration and Testing

The Student Skills Analyzer was integrated into `src/main.py` as a separate function:

```python
def analyze_student_skills():
    ...
```

It is called from `main()`:

```python
def main():
    analyze_student_skills()
```

The program was tested with the normal student data. It successfully:

* collected unique skills,
* counted skill frequencies,
* identified multiple most-common skills when there was a tie,
* created student summary tuples,
* unpacked and displayed the summaries,
* filtered students by a target skill,
* and handled a no-match result.

Regression testing was also performed on the existing name-input functionality.

Valid input:

```text
Enter your name: Aqsa
Hello, Aqsa!
```

Whitespace-only input:

```text
Enter your name:
Name cannot be empty.
```

This confirmed that adding the Student Skills Analyzer did not break the existing program behavior.

### Key Takeaways

* Lists are useful for ordered collections of students and skills.
* Dictionaries represent structured key-value records.
* Sets efficiently remove duplicates and support unique-data analysis.
* Tuples provide a compact structure for fixed summary values.
* Nested loops can process data stored inside nested collections.
* `.get()` is useful for frequency counting and safe dictionary access.
* Membership testing with `in` supports searching and filtering.
* Empty collections should be checked before operations such as `max()`.
* Real problems often require several data structures to work together.
* Edge-case and regression testing help make programs more reliable.

### Workflow Practiced

**Learn → Build → Break → Debug → Improve → Test → Inspect → Format → Document**

The problem started with small REPL experiments, intentionally tested failure cases, improved unsafe logic, integrated the solution into the project, tested existing functionality again, inspected the Git diff, checked whitespace with `git diff --check`, and documented the learning before committing the work.

