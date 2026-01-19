# 01. Moving from Notebooks to Production Scripts

## The Mental Shift

Jupyter Notebooks are powerful tools for exploration—plotting data, checking a matrix shape, or prototyping an idea.  
However, they are poor tools for production—running long simulations, managing complex logic, or running on supercomputers.

To build robust research software, we must transition from the **"Cell-by-Cell"** mindset to the **"Script-Based"** mindset.

## Key Differences

| Feature | Jupyter Notebook (.ipynb) | Python Script (.py) |
|--------|---------------------------|--------------------|
| **Execution** | Non-linear (can run cells in any order) | Top-to-Bottom (always runs line 1 to end) |
| **State** | Variables persist in memory until restart | Memory is wiped clean every run |
| **Best For** | Plotting, Prototyping, Teaching | Simulations, heavy math, reusable libraries |
| **Version Control** | Hard (GitHub sees a messy JSON file) | Perfect (GitHub sees clean text diffs) |

## The Anatomy of a Script

Unlike a notebook, a script needs a specific entry point.  
We use the `if __name__ == "__main__":` block to tell Python:  
“If I run this file directly, do this.”

### Example Structure

```python
import numpy as np

# 1. Define Functions (The Tools)
def calculate_energy(H):
    return np.linalg.eigvalsh(H)

# 2. Define the Main Execution Block (The Action)
if __name__ == "__main__":
    print("Starting Simulation...")
    H = np.random.rand(4, 4)
    E = calculate_energy(H)
    print(f"Energies: {E}")
```

## How to Run Scripts (The Terminal Workflow)

You do not need to leave VS Code to run scripts. Use the built-in terminal.

1. Open Terminal
   Shortcut: `Ctrl` +  ` (backtick)
2. Navigate
   Always check "where you are" before running code.
   ```bash
   pwd                     # Print Working Directory (Check where you are)
   ls                      # List files (Check what is here)
   cd "folder_name"        # Change Directory (Go into a folder
   cd ..                   # Go back one folder
   ```
   
3. Execute
   To run the file `simulation.py`:
   ``python simulation.py``

## Pro-Tips for the Transition

1. Printing is Mandatory: In notebooks, typing `x` shows the value.
   In scripts, you must type `print(x)`, otherwise, the calculation happens silently and is lost.
2. The "Import" Superpower: Once your code is in a script (e.g., `physics_tools.py`), you can import it into other scripts or notebooks using `from physics_tools import calculate_energy`.
   You cannot easily import code from one notebook to another.
3. Clean Slate: Because scripts restart from zero every time you run them, you are guaranteed that your results are reproducible.
   You will never have a bug caused by a "ghost variable" left over from a cell you ran 20 minutes ago.
