# This file turns the folder into a recognizable Python module. You can use it to expose your most important functions to the top level, making them easier for users to import.

"""
Quantum Chemistry Algorithms Library
------------------------------------
Tools for simulating complex spin dynamics and analyzing phase transitions.
"""

# Expose the core functions directly at the top level
from .dynamics import evolve_spin_system

# Define what gets imported when someone runs `from qchem_algorithms import *`
__all__ = ["evolve_spin_system"]

# Define the package version
__version__ = "0.1.0"