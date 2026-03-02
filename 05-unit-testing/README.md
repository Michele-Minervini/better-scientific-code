# 05. Unit Testing: Trusting Your Code 🧪

## The "Silent Failure" Problem in Physics
If a web developer makes a mistake, the website crashes or a button disappears. It's obvious. 
If a computational physicist makes a mistake (e.g., forgets a complex conjugate, transposes a matrix incorrectly), the code usually **still runs**. It just outputs a Hamiltonian with incorrect eigenvalues or a density matrix that isn't trace-preserving. 

We cannot rely on "it ran without errors" as proof that the code is correct. We need **Automated Testing**.

## What is Unit Testing?
Unit testing involves writing small, isolated scripts that check if individual functions behave exactly as expected under known conditions. 

If you write a function to compute a commutator $[A, B]$, a unit test will pass the Pauli matrices $X$ and $Y$ into it and assert that the output is exactly $2iZ$. 

## The Tool: `pytest`
`pytest` is the industry standard for testing in Python. It automatically finds any file starting with `test_` and runs all functions inside it that start with `test_`.

*(To install: run `pip install pytest` in your terminal).*

## The Anatomy of a Good Test: A-A-A
Every reliable unit test follows the **Arrange, Act, Assert** pattern:

1. **Arrange:** Set up the initial conditions (e.g., define the matrices).
2. **Act:** Run the function you are testing.
3. **Assert:** Check if the result matches the mathematical truth.

### Example
```python
def test_commutator():
    # 1. Arrange
    X = np.array([[0, 1], [1, 0]])
    Y = np.array([[0, -1j], [1j, 0]])
    expected = 2j * np.array([[1, 0], [0, -1]]) # 2iZ
    
    # 2. Act
    result = commutator(X, Y)
    
    # 3. Assert
    np.testing.assert_allclose(result, expected)
```
## Why This is a Superpower
1. Refactoring: You can rewrite a slow function to be 10x faster. How do you know you didn't break the physics? Run the tests. If they pass, your new code is mathematically identical to the old code.

2. The "Done" State: Writing tests before you write the complex logic (Test-Driven Development) gives you a clear finish line.