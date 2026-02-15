# Absolute Import (Best Practice)
from src.hamiltonian import random_hamiltonian
from src.solver import evolve_state

# Using the tools
H = random_hamiltonian(N=4)
rho_final = evolve_state(H, t=10)


## Common Error: ModuleNotFoundError
##
## Cause: You are running the python command from the wrong folder.
##
## Rule: Always run your script from the Project Root.
##
## ✅ python run_simulation.py (Correct)
##
### ❌ cd src then python solver.py (Wrong - Python loses track of the folder structure)
