# 08. Command Line Interfaces: Stop Editing Code to Run It 🎛️

## The Problem: Hardcoded Variables
Look at this standard script setup:
```python
# train_model.py
qubits = 4
learning_rate = 0.01
ansatz_type = "hardware_efficient"
```
If you want to test 6 qubits, you have to open the file, edit ``qubits = 6``, save it, and run it.
If you are running your code on a remote supercomputer or cluster, opening and editing text files via a terminal editor (like Vim or Nano) every single time is painful and error-prone.

## The Solution: ``argparse``
We want to control the script entirely from the outside, like this:

```bash
python train_model.py --qubits 6 --learning_rate 0.05
```

Python has a built-in library called ``argparse`` that handles this perfectly. It grabs the text from your terminal command, converts it into Python variables (like integers and floats), and injects them into your code.

## The 4 Steps of ``argparse``

1. **Import and Initialize**
```python
import argparse
parser = argparse.ArgumentParser(description="Quantum Machine Learning Training Script")
```

2. **Add Arguments**

    You define what inputs your script accepts, what data type they are, and what their default value should be if the user forgets to type them.

```python
parser.add_argument("--qubits", type=int, default=4, help="Number of qubits in the system")
```
3. **Parse the Arguments**
   
   Tell the parser to read the terminal command and extract the values.
   ```python
   args = parser.parse_args()
   ```

4. **Access the Arguments**
   
   The variables now live inside the ``args`` object.
   ```python
   print(f"Running simulation with {args.qubits} qubits.")
   ```

## Pro-Tip: Boolean Flags
Sometimes you just want to turn a feature ON or OFF without passing a value (e.g., ``--verbose`` or ``--save_matrix``).
Use ``action="store_true"``. If the user types the flag, the variable becomes ``True``. If they don't, it stays ``False``.
```python
parser.add_argument("--save_data", action="store_true", help="Save the output matrix")
```
Terminal usage: ``python script.py --save_data`` (No need to type ``=True``).

## Why This is Crucial for Research
When you use a cluster (like those at national labs or university computing centers), you submit "batch jobs." These jobs run your script automatically. With ``argparse``, you can submit 100 different jobs simultaneously, all pointing to the exact same ``.py`` file but passing different ``--learning_rate`` or ``--qubits`` arguments.