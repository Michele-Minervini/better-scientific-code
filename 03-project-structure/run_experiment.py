import numpy as np

# IMPORTING from our folder
from src.dynamics import evolve

def main():
    print("--- Experiment Start ---")
    
    # Initial State
    psi = np.array([1, 0], dtype=complex)
    
    # Run Physics
    t = 0.5
    psi_t = evolve(psi, t)
    
    print(f"Time: {t}")
    print(f"Final State: {psi_t}")
    print("--- Experiment End ---")

if __name__ == "__main__":
    main()
