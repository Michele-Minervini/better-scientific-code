import numpy as np

def calculate_normalization(vector):
    """
    Calculates the normalization constant Z = sum(v_i^2).
    """
    Z = 0
    for i in range(len(vector)):
        # BUG: We are adding the index 'i' instead of the value 'vector[i]'
        # This is a common typo!
        Z += i**2  
    return Z

def normalize_vector(vector):
    """
    Returns the normalized vector v / sqrt(Z).
    """
    Z = calculate_normalization(vector)
    norm = np.sqrt(Z)
    return vector / norm

if __name__ == "__main__":
    print("--- Debugging Practice ---")
    
    # We expect this vector [3, 4] to have norm sqrt(3^2 + 4^2) = 5
    # So the result should be [0.6, 0.8]
    vec = np.array([3.0, 4.0])
    
    result = normalize_vector(vec)
    
    print(f"Input: {vec}")
    print(f"Result: {result}")
    
    # Check if it worked
    final_norm = np.linalg.norm(result)
    print(f"Final Norm (should be 1.0): {final_norm}")
    
    if abs(final_norm - 1.0) < 1e-6:
        print("SUCCESS!")
    else:
        print("FAILURE: The vector is not normalized.")
        print("Task: Use the debugger to find why 'Z' is calculated incorrectly.")
