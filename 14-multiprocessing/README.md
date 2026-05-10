# 14. Multiprocessing: Using All Your CPU Cores 🚀

## The Problem: The Single-Lane Highway
Imagine you need to calculate the ground state energy for 100 different molecular configurations. If each calculation takes 1 minute, a `for` loop will take 100 minutes. 

By default, Python is strictly bound by the **Global Interpreter Lock (GIL)**, meaning it can only process one instruction at a time on a single CPU core. Even if you have a 16-core MacBook Pro, a standard script leaves 15 cores completely unused.

## The Solution: `concurrent.futures`
We need to bypass the GIL by spinning up entirely separate Python processes—one for each core. We split our 100 configurations into chunks, hand a chunk to each core, and gather the results at the end. 

Instead of a 1-lane highway, we build an 8-lane or 16-lane highway.

### Threads vs. Processes (Crucial Physics Distinction)
* **Multithreading:** Good for downloading files or waiting for web APIs (I/O bound). **Terrible for math.** The GIL will block threads from doing heavy math simultaneously.
* **Multiprocessing:** Good for matrix diagonalization, Monte Carlo, and solving ODEs (CPU bound). This spawns completely isolated Python environments. **Always use this for physics.**

## How to Parallelize in Modern Python
The modern standard is the `ProcessPoolExecutor` from the built-in `concurrent.futures` library. 

```python
from concurrent.futures import ProcessPoolExecutor

# 1. Define the function (The "Worker")
def heavy_math(parameter):
    return result

# 2. Define the inputs
parameters = [0.1, 0.2, 0.3, ..., 10.0]

# 3. Map the function to the inputs across all cores
with ProcessPoolExecutor(max_workers=8) as executor:
    results = list(executor.map(heavy_math, parameters))
```
## ⚠️ The Golden Rule of Multiprocessing
You MUST wrap your parallel execution code inside an ``if __name__ == "__main__":`` block.
If you don't, when Python tries to spawn new processes, those processes will accidentally try to spawn their own processes, leading to an infinite loop that will crash your computer (especially on macOS and Windows).