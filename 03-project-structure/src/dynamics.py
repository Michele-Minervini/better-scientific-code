import numpy as np
from src.operators import get_pauli_matrices

def evolve(state, time):
    """
    A dummy evolution function.
    Notice how we import 'get_pauli_matrices' from the SIBLING file.
    """
    I, X, Z = get_pauli_matrices()
    # Dummy logic: rotate state by X
    U = np.eye(2) + 1j * X * time 
    return U @ state
