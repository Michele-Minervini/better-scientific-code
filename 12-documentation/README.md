# 12. Documentation & Type Hints: Writing for Humans 📚

## The Problem: "What does this matrix do?"
Physics code is inherently complex. If you write a function `evolve(H, rho, t, n)`, a collaborator will immediately have questions:
* Is `H` supposed to be a 2D array or a sparse matrix?
* Does `t` represent time steps or total time?
* Is `n` the number of qubits or the dimension of the system?
* Does the function return the final state, or a list of states at every time step?

If they have to read the source code to answer these questions, your documentation has failed.

## 1. Type Hints (Python 3.5+)
Python is "dynamically typed," meaning you don't have to declare variable types. But for large projects, this is dangerous. **Type Hints** allow you to explicitly state what goes in and what comes out.

❌ **Without Hints:**
```python
def calculate_fidelity(rho, sigma):
```
✅ With Hints:
```python
import numpy as np

def calculate_fidelity(rho: np.ndarray, sigma: np.ndarray) -> float:
```
Note: Type hints don't force Python to crash if you pass the wrong type, but your IDE (VS Code) and your linter (Ruff) will warn you before you even run the code!

## 2. The NumPy Docstring Standard
A "docstring" is the block of text immediately below a function definition. In scientific Python (NumPy, SciPy, Pandas), the community has agreed on a strict formatting standard.

It consists of four main parts:

1. Summary: One sentence describing what it does.

2. Parameters: A list of inputs, their types, and their physical meaning.

3. Returns: A list of outputs and their types.

4. Raises (Optional): Any errors the function might intentionally throw.

## 3. Automated Documentation Sites (MkDocs)
Why do we follow this strict NumPy formatting? Because robots can read it.

If you format your docstrings correctly, you can use tools like MkDocs (specifically the mkdocs-material theme) or Sphinx. These tools automatically read your .py files and generate beautiful, searchable websites (like the official NumPy documentation) with zero extra effort from you.

(If you want to build a site, run pip install mkdocs-material mkdocstrings[python] and look up the MkDocs documentation!)