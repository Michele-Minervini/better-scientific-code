# This script calculates the expectation value $\langle O \rangle = \text{Tr}(O \rho)$ for a large batch of density matrices. It does it using terrible, slow Python loops.

import numpy as np
import time

def calculate_expectation_values_slow(observables, states):
    """
    Calculates Tr(O * rho) for a list of observables and states.
    Written using slow, nested Python for-loops.
    """
    n_obs = observables.shape[0]
    n_states = states.shape[0]
    results = np.zeros((n_obs, n_states), dtype=complex)
    
    # 🛑 THE BOTTLENECK: Python handles the logic for every single pair
    for i in range(n_obs):
        for j in range(n_states):
            O = observables[i]
            rho = states[j]
            # Matrix multiplication and trace
            mult = O @ rho
            results[i, j] = np.trace(mult)
            
    return results

if __name__ == "__main__":
    # --- SETUP PARAMETERS ---
    dim = 64        # 6 qubits
    n_obs = 50      # Number of observables
    n_states = 2000 # Number of density matrices
    
    print(f"Generating matrices (Dim={dim}, Obs={n_obs}, States={n_states})...")
    obs = np.random.rand(n_obs, dim, dim) + 1j * np.random.rand(n_obs, dim, dim)
    rhos = np.random.rand(n_states, dim, dim) + 1j * np.random.rand(n_states, dim, dim)
    
    print("Running Slow Physics (Nested Loops)...")
    start = time.time()
    res = calculate_expectation_values_slow(obs, rhos) 
    end = time.time()
    
    print(f"Time taken: {end - start:.4f} seconds")