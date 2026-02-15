# 03. Project Structure & Imports 🏗️

## The Problem: The "God File"
When you start a project, you usually put everything into one file (`script.py`).
Eventually, this file hits 1,000 lines. You scroll up and down endlessly to find that one `def` you wrote. Variables from the plotting section interfere with the simulation section. It’s a mess.

## The Solution: Modularization
**Modularization** is breaking your code into separate files (Modules) based on **logic**, not execution order.

### 1. The Standard Research Structure
For a typical physics/simulation project, organize your files like this:

```text
my_project/
│
├── README.md              # Project documentation
├── requirements.txt       # List of libraries (numpy, scipy, etc.)
├── data/                  # Folder for .csv/.npz outputs (Ignored by Git!)
│
├── run_simulation.py      # The "Driver" script (The one you actually run)
├── plot_results.py        # Separate script for analysis
│
└── src/                   # Source code folder
    ├── __init__.py        # Tells Python this folder is importable
    ├── hamiltonian.py     # Definitions of H
    ├── solver.py          # The time-evolution logic
    └── utils.py           # Helper functions (pauli matrices, partial trace)
```

### Pro-Tip: The .gitignore File
You never want to commit your heavy simulation data to GitHub.
So, create a file named .gitignore in your root and add:
```text
data/
*.npz
*.csv
__pycache__/
