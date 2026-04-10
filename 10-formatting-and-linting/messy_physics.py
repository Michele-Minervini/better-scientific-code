# This file is deliberately atrocious. It has unused imports, bad spacing, multiple statements on one line, and a dictionary that is impossible to read.

import sys
import os
import time
import numpy as np
import scipy.linalg as la

def calculate_energy   (   H,state):
    # This function calculates the energy of a state
    E= np.trace(H@state) ; return E.real

if __name__=="__main__":
            print( "Starting simulation..." )
            
            # A completely unreadable matrix
            H = np.array([[1.0, 0.5, 0.2, 0.1], [0.5, 2.0, 0.3, 0.2], [0.2, 0.3, 3.0, 0.4], [0.1, 0.2, 0.4, 4.0]])
            
            state=np.eye(4)/4.0 # Maximally mixed state
            energy=calculate_energy(H, state)
            
            parameters={'qubits':2,'beta':1.0,'dt':0.01,'solver':'rk4','tolerance':1e-6}
            
            print(f"Energy: {energy}")

## LESSON
# 1. Open your terminal and install the tool: python -m pip install ruff

# 2. Navigate to 10-formatting-and-linting.

# 3. Look at messy_physics.py in VS Code. It hurts the eyes.

# 4. Run the linter to find the bad practices:
#    ruff check messy_physics.py
# (It will warn you that sys, os, time, and la are imported but unused).

# 5. Tell the linter to fix what it can:
# ruff check --fix messy_physics.py

# 6. Now, run the formatter to fix the spacing and line lengths:
# ruff format messy_physics.py

# 7. Look at messy_physics.py in VS Code again. It will be perfectly formatted, with the long matrix broken onto multiple readable lines, the dictionary spaced out, and the unused imports deleted!