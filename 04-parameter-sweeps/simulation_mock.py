import time
import numpy as np

def run_quantum_task(N, beta):
    """
    Simulates a heavy quantum dynamics calculation.
    Returns: fidelity (float) and a dummy density matrix (array).
    """
    # Simulate compute time (0.1 seconds)
    time.sleep(0.1)
    
    # Fake physics result: Fidelity drops as Beta increases and N increases
    noise = np.random.normal(0, 0.05)
    fidelity = np.exp(-beta / N) + noise
    fidelity = min(max(fidelity, 0.0), 1.0) # Keep between 0 and 1
    
    # Fake large matrix (e.g., a density matrix or Hamiltonian)
    rho = np.eye(2**N) * fidelity
    
    return fidelity, rho