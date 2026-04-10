# 10. Code Formatting & Linting: Writing Professional Code 🧹

## The Problem: "It Works, But It's Ugly"
In research, we often write code in a rush to test an idea. This leads to:
* **Unused imports** cluttering the top of the file.
* **Inconsistent spacing** (some lines use spaces, some use tabs).
* **Massive lines of math** that require horizontal scrolling.
* **Undefined variables** that crash the code halfway through a run.

These issues make code incredibly hard to read for your collaborators (and for your future self).

## The Solution: Linters and Formatters
Instead of manually fixing spacing, we use automated tools. 

1. **The Linter:** Analyzes your code for logical errors and bad practices (e.g., "You imported `numpy` but never used it", or "You defined `x` twice").
2. **The Formatter:** Analyzes your code for style and automatically rewrites it to look beautiful and consistent (e.g., breaking long lines, fixing indentation).

## The Tool: `Ruff` ⚡
For years, Python developers used a combination of tools like `Flake8` (linting), `Black` (formatting), and `isort` (sorting imports). 

Today, the industry standard is **Ruff**. It is written in Rust, meaning it does the job of all three older tools combined, but is roughly 100x faster. 

*(To install: run `pip install ruff` in your terminal).*

## How to Use Ruff

### 1. Linting (Finding Errors)
To check your code for logical errors and style violations, run:
```bash
ruff check script.py
```
It will output a list of issues. You can even tell Ruff to automatically fix the safe ones (like deleting unused imports) by running:
```bash
ruff check --fix script.py
```
### 2. Formatting (Making it Beautiful)
To automatically reformat your code to match the strict Python standard (PEP 8), run:
```bash
ruff format script.py
```
Ruff will instantly rewrite your file. Long matrices will be neatly stacked, spaces will be fixed, and quotes will be standardized.