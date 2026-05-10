# We simulate a very common, heavy task in quantum physics: **Diagonalizing large random matrices** to find their eigenvalues. 
# We do it sequentially (the old way) and then parallelized (the new way), and print the analytics.

import time
import numpy as np
import scipy.linalg as la
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

# --- 1. THE WORKER FUNCTION ---
# This function MUST be defined at the top level of the script so it can be 
# "pickled" (packaged up) and sent to other CPU cores.
def diagonalize_matrix(seed: int) -> float:
    """
    Simulates a heavy physics calculation. 
    Generates a 600x600 random Hermitian matrix and finds its eigenvalues.
    Returns the maximum eigenvalue.
    """
    # Use the seed so each matrix is unique but reproducible
    np.random.seed(seed)
    dim = 1000
    
    # Create a random Hermitian matrix
    A = np.random.rand(dim, dim) + 1j * np.random.rand(dim, dim)
    H = A + A.conj().T
    
    # The heavy math: Diagonalization
    eigenvalues = la.eigvalsh(H)
    return float(np.max(eigenvalues))


def main():
    # Detect how many CPU cores the user actually has
    n_cores = multiprocessing.cpu_count()
    print(f"💻 System detected: {n_cores} CPU cores available.\n")
    
    print("--- 🚀 Serial vs. Parallel: The Matrix Showdown ---")
    
    # We will diagonalize 100 matrices.
    tasks = list(range(100))
    print(f"Target: Diagonalize {len(tasks)} large (600x600) matrices.")
    
    # --- 2. RUN SEQUENTIAL (THE OLD WAY) ---
    print("\n[1/2] Running Sequential (1 Core)...")
    seq_start = time.time()
    
    # Standard list comprehension / for-loop
    seq_results = [diagonalize_matrix(t) for t in tasks]
    
    seq_time = time.time() - seq_start
    print(f"      Time: {seq_time:.4f} seconds")

    # --- 3. RUN PARALLEL (THE NEW WAY) ---
    print(f"\n[2/2] Running Parallel ({n_cores} Cores)...")
    par_start = time.time()
    
    # The magic context manager that handles all the complex core assignments
    with ProcessPoolExecutor(max_workers=n_cores) as executor:
        # executor.map takes the function and the list of inputs, 
        # distributes them, and waits for them all to finish.
        par_results = list(executor.map(diagonalize_matrix, tasks))
        
    par_time = time.time() - par_start
    print(f"      Time: {par_time:.4f} seconds")

    # Verify both methods got the exact same math results
    assert np.allclose(seq_results, par_results), "Math mismatch!"

    # --- 4. FANCY ANALYTICS ---
    speedup = seq_time / par_time
    
    print("\n" + "="*55)
    print("📊 PERFORMANCE ANALYTICS")
    print("="*55)
    
    max_bar_length = 40
    seq_bar = "█" * max_bar_length
    par_bar_length = max(1, int(max_bar_length / speedup)) 
    par_bar = "█" * par_bar_length
    
    print(f"1 Core Time  : {seq_time:.4f} s | {seq_bar}")
    print(f"{n_cores} Core Time : {par_time:.4f} s | {par_bar}")
    print("-" * 55)
    
    # Calculate efficiency (perfect scaling would be 100%)
    efficiency = (speedup / n_cores) * 100
    print(f"🔥 Parallel is {speedup:.1f}x FASTER!")
    print(f"⚙️  CPU Scaling Efficiency: {efficiency:.1f}%")
    print("="*55)

if __name__ == "__main__":
    main()