# 09. Profiling & Optimization: Stop Guessing Why It's Slow ⏱️

## The Problem: Premature Optimization
When a simulation takes 10 hours, it's tempting to start rewriting everything to be "faster." This is a trap. 
In most scientific code, **90% of the execution time is spent in 10% of the code**. If you spend three days optimizing a setup function that only takes 0.5 seconds to run, you have wasted your time. 

You must **measure** before you optimize.

## 1. The Profiler: `cProfile`
Python comes with a built-in tool that tracks exactly how many times every function is called and how long it takes. 

You don't even need to edit your code to use it. Just run your script from the terminal like this:
```bash
python -m cProfile -s tottime your_script.py
```
(The ``-s tottime`` flag sorts the output so the slowest functions are at the very top).

When you look at the output, find the functions you wrote. If ``calculate_metropolis_weight`` takes 95% of the time, that is the only function you need to fix.

## 2. The Golden Rule of NumPy: No for Loops for Math
If you are doing math in Python, and you type ``for i in range(...)``, your code is probably 100x slower than it needs to be.

Python is a slow language. NumPy is incredibly fast because it is written in C. Vectorization is the art of giving NumPy the entire block of data at once so it can do the math in C, rather than looping in Python.

### Example: Squaring an array of numbers
❌ The Slow Way (Python Loop):
```python 
results = np.zeros(100000)
for i in range(100000):
    results[i] = data[i] ** 2  # Python translates this 100,000 times.
```
✅ The Fast Way (Vectorized):
```python 
results = data ** 2  # NumPy pushes this entirely into C.
```

## 3. The Superpower: np.einsum

In quantum mechanics, we do a lot of trace operations, tensor products, and partial traces. Doing these with loops or standard ``np.dot`` can get messy and slow for multi-dimensional tensors.
Learn to use **Einstein Summation** (``np.einsum``). It is the ultimate tool for fast, readable tensor math.

- Trace of a matrix: ``np.einsum('ii', A)``

- Matrix Multiplication: ``np.einsum('ij,jk->ik', A, B)``

- Inner product of state vectors: ``np.einsum('i,i->', psi_1, psi_2)``