# 11. Continuous Integration: Automating Your Checks 🤖

## The Problem: The Human Factor
You wrote unit tests (`pytest`). You installed a linter (`ruff`). 
But on a Friday at 5:00 PM, you make a "tiny, obvious fix" to your Hamiltonian code and immediately type `git push`. You don't run the tests because you are confident. 

On Monday, your collaborator pulls the code and their simulation crashes. Your "tiny fix" broke the matrix dimensions.

## The Solution: Continuous Integration (CI)
Continuous Integration means that **every single time** you push code to GitHub, a server automatically boots up, installs your code, and runs your tests and linters for you. 

If the tests pass, GitHub puts a ✅ next to your commit. 
If they fail, GitHub puts a ❌ and sends you an email telling you exactly what broke.

## Enter GitHub Actions
GitHub provides free computing power for public repositories to run these checks. You control these servers using a YAML file called a "Workflow."

A Workflow answers three questions:
1. **When** should this run? (e.g., "Every time I push to the `main` branch").
2. **Where** should this run? (e.g., "On an Ubuntu Linux machine").
3. **What** should it do? (e.g., "Install Python 3.11, install `pytest`, and run the tests").

## How to Set It Up

To use GitHub Actions, you must create a very specific, hidden folder structure in the **root** of your repository (not inside this lesson folder!).

1. Go to the root directory of your project.
2. Create a folder named exactly `.github` (with the dot).
3. Inside it, create a folder named exactly `workflows`.
4. Inside that, create a file named `ci.yml` (or copy the template from this lesson).

```text
your_repository/
├── .github/
│   └── workflows/
│       └── ci.yml   <-- The automation file!
├── src/
└── README.md