import numpy as np
import pytest
from physics_math import commutator, is_pure_state, partial_trace_qubit

def test_commutator_pauli():
    """Test if [X, Y] = 2iZ"""
    # 1. Arrange
    X = np.array([[0, 1], [1, 0]], dtype=complex)
    Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
    Z = np.array([[1, 0], [0, -1]], dtype=complex)
    
    expected = 2j * Z
    
    # 2. Act
    result = commutator(X, Y)
    
    # 3. Assert
    np.testing.assert_allclose(result, expected, err_msg="Commutator failed for Pauli X and Y")

def test_is_pure_state_true():
    """Test a known pure state (|0><0|)."""
    # Arrange
    rho_pure = np.array([[1, 0], [0, 0]], dtype=complex)
    
    # Act
    result = is_pure_state(rho_pure)
    
    # Assert
    assert result == True

def test_is_pure_state_mixed():
    """Test a known maximally mixed state (I/2)."""
    # Arrange
    rho_mixed = np.array([[0.5, 0], [0, 0.5]], dtype=complex)
    
    # Act
    result = is_pure_state(rho_mixed)
    
    # Assert
    assert result == False

def test_partial_trace_bell_state():
    """
    Test partial trace on a Bell state (|00> + |11>)/sqrt(2).
    Tracing out one qubit should leave the maximally mixed state I/2.
    """
    # Arrange: Create Bell state density matrix
    bell_vec = np.array([1, 0, 0, 1]) / np.sqrt(2)
    rho_bell = np.outer(bell_vec, bell_vec)
    
    expected_reduced = np.array([[0.5, 0], [0, 0.5]], dtype=complex)
    
    # Act
    result = partial_trace_qubit(rho_bell)
    
    # Assert
    np.testing.assert_allclose(result, expected_reduced, atol=1e-7)