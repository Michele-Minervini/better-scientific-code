import numpy as np

def commutator(A, B):
    """Computes the commutator [A, B] = AB - BA."""
    return A @ B - B @ A

def is_pure_state(rho, tol=1e-6):
    """
    Checks if a density matrix represents a pure state.
    A state is pure if Tr(rho^2) = 1.
    """
    purity = np.trace(rho @ rho)
    # Return True if purity is close to 1
    return np.abs(purity - 1.0) < tol

def partial_trace_qubit(rho):
    """
    A deliberately simple (and easily broken) partial trace 
    for a 2-qubit system tracing out the second qubit.
    """
    # Reshape 4x4 matrix into a 2x2x2x2 tensor
    tensor = rho.reshape(2, 2, 2, 2)
    # Trace over the second subsystem (indices 1 and 3)
    reduced_rho = np.trace(tensor, axis1=1, axis2=3)
    return reduced_rho