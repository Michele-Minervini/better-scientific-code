# This file shows the contrast between "grad student hack" code and "published researcher" code. Notice how the second function feels like a real, trustworthy software library.

import numpy as np
import scipy.linalg as la

# ---------------------------------------------------------
# ❌ THE BAD WAY (No hints, no docstring)
# ---------------------------------------------------------
def purity(r):
    # calculates purity
    return np.trace(r @ r).real


# ---------------------------------------------------------
# ✅ THE PROFESSIONAL WAY (Type hints + NumPy Docstrings)
# ---------------------------------------------------------
def calculate_purity(rho: np.ndarray) -> float:
    """
    Calculates the quantum purity of a density matrix.
    
    The purity is defined as Tr(rho^2). For a pure state, the purity is 1. 
    For a maximally mixed state of dimension d, the purity is 1/d.

    Parameters
    ----------
    rho : np.ndarray
        A 2D complex array representing the density matrix of the quantum state.
        Must be a square Hermitian matrix with trace 1.

    Returns
    -------
    float
        The purity of the state, bounded between 1/d and 1.0.

    Raises
    ------
    ValueError
        If the input matrix `rho` is not square.
        
    Examples
    --------
    >>> pure_state = np.array([[1, 0], [0, 0]])
    >>> calculate_purity(pure_state)
    1.0
    """
    
    # 1. Input Validation (Defensive Programming)
    if rho.ndim != 2 or rho.shape[0] != rho.shape[1]:
        raise ValueError(f"Density matrix must be square. Received shape {rho.shape}")
        
    # 2. Physics Calculation
    purity_val = np.trace(rho @ rho)
    
    # Trace can technically return a complex number with a 0j imaginary part.
    # We cast it to a real float for the return type.
    return float(np.real(purity_val))

if __name__ == "__main__":
    # Test the function
    rho_mixed = np.eye(4) / 4.0
    p = calculate_purity(rho_mixed)
    print(f"Purity of maximally mixed 4-level system: {p}")

# In VS Code, if you hover your mouse over the word calculate_purity at the bottom of the script, VS Code will pop up a beautiful, formatted tooltip showing your parameters, the physical explanation, and the return type.