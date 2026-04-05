# This script does the exact same math, but pushes the entire operation into C using NumPy broadcasting and Einstein summation.

import numpy as np
import time

def calculate_expectation_values_fast(observables, states):
    """
    Calculates Tr(O * rho) using Einstein Summation.
    'oab' -> observable index 'o', matrix indices 'a,b'
    'sba' -> state index 's', matrix indices 'b,a' (effectively transposing)
    'os'  -> output observable index 'o', state index 's'
    """
    # 🚀 THE FIX: Single C-call for the entire operation
    return np.einsum('oab, sba -> os', observables, states)

if __name__ == "__main__":
    # --- SETUP PARAMETERS (Must match slow_physics.py) ---
    dim = 64
    n_obs = 50
    n_states = 2000
    
    print(f"Generating matrices (Dim={dim}, Obs={n_obs}, States={n_states})...")
    obs = np.random.rand(n_obs, dim, dim) + 1j * np.random.rand(n_obs, dim, dim)
    rhos = np.random.rand(n_states, dim, dim) + 1j * np.random.rand(n_states, dim, dim)
    
    print("Running Fast Physics (Vectorized einsum)...")
    start = time.time()
    res = calculate_expectation_values_fast(obs, rhos) 
    
    end = time.time()
    print(f"Time taken: {end - start:.4f} seconds")