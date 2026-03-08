import csv
import itertools
import os
import numpy as np
from tqdm import tqdm
from simulation_mock import run_quantum_task

def main_sweep():
    print("--- Starting Parameter Sweep ---")

    # 1. Define Parameter Ranges
    N_values = [2, 3, 4]
    beta_values = np.linspace(0.1, 2.0, 10)  # 10 temperature points
    
    # itertools.product creates a list of tuples: [(2, 0.1), (2, 0.31), ...]
    param_grid = list(itertools.product(N_values, beta_values))
    
    # 2. Setup Data File
    # We put it in a 'data' folder to keep the root clean
    if not os.path.exists('data'):
        os.makedirs('data')
        
    filename = "data/sweep_results.csv"
    file_exists = os.path.isfile(filename)
    
    # Write header ONLY if the file is brand new
    if not file_exists:
        with open(filename, mode="w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["N", "Beta", "Fidelity"])

    print(f"Total simulations to run: {len(param_grid)}")

    # 3. The Loop (wrapped in tqdm for the visual progress bar)
    for (N, beta) in tqdm(param_grid, desc="Simulating"):
        
        # A. Run Physics
        fid, rho = run_quantum_task(N, beta)
        
        # B. Save Scalar Data immediately (Append Mode)
        with open(filename, mode="a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([N, beta, fid])
            
        # C. (Optional) Save Matrix Data
        # Matrices eat up disk space quickly! Only save them if a specific 
        # condition is met (e.g., saving the state when fidelity drops too low)
        if fid < 0.3:
            np.savez(f"data/failed_state_N{N}_B{beta:.2f}.npz", rho=rho)

    print("\n✅ Sweep Complete. Data safely logged to data/sweep_results.csv")

if __name__ == "__main__":
    main_sweep()