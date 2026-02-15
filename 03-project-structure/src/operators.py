import numpy as np

def get_pauli_matrices():
    """Returns standard Pauli matrices."""
    I = np.eye(2, dtype=complex)
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    return I, X, Z
