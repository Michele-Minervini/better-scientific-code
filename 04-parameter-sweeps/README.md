# 04. Automating Experiments: Sweeps & Logs 🔄

## The Goal
Computational research isn't about running code once. It's about running it hundreds of times across different parameters (like system size, inverse temperature, or time steps) to find physical trends. 

We want to move from **"Change variable -> Run -> Copy result to Excel"** to **"Configure range -> Run once -> Analyze Data"**.

## 1. The "Orchestrator" Pattern
A clean project separates the physics from the loops.
1.  **The Engine:** A function `run_quantum_dynamics(N, beta, t)` that returns a result. It knows absolutely nothing about loops, CSV files, or progress bars.
2.  **The Orchestrator (Driver):** A separate script that defines the parameter grid, loops through it, calls the engine, and safely logs the data.

## 2. Cleaner Loops with `itertools`
When sweeping over multiple variables, nested loops get ugly and hard to read quickly.

```python
# The Ugly Way
for N in [2, 4, 6]:
    for beta in [0.1, 1.0, 5.0]:
        for t in [1.0, 10.0]:
             run_simulation(N, beta, t)
```

### The Pythonic Way:
Use itertools.product to flatten the loop. It generates every combination mathematically automatically.

```python
import itertools

# Create a flat list of all (N, beta, t) combinations
params = itertools.product(N_list, beta_list, t_list)

for (N, beta, t) in params:
    run_simulation(N, beta, t)
```

## 3. "Append-Write" Logging (Crash Proofing) 🛡️
Never save your data only at the very end of a script. If you are runnign your simulation for 3 days and the cluster kills your job at 99%, you lose everything.

Best Practice: Open the CSV file, write one row of data, and close it immediately inside the loop.

```python
with open("results.csv", mode="a", newline="") as f:  # 'a' for Append
    writer = csv.writer(f)
    writer.writerow([N, beta, t, error])
```
Because the file closes after every iteration, your data is perfectly safe up to the exact moment of a crash.

## 4. Progress Bars (tqdm)
When a script runs for hours, a blinking cursor gives you no information. The tqdm library wraps around any loop to give you a smart progress bar with an estimated time of completion (ETA).

```python
from tqdm import tqdm

for param in tqdm(param_grid, desc="Simulating Dynamics"):
    # The progress bar updates automatically each loop!
```