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
