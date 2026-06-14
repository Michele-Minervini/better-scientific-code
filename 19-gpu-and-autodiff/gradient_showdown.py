# We will set up a scenario mimicking the optimization of a parameterized molecular ground state. We will compare the old, slow "Finite Difference" method against JAX's instant "Automatic Differentiation."
import time
import numpy as np
import jax
import jax.numpy as jnp
from jax import grad, jit

# ==============================================================================
# THE PHYSICS SCENARIO
# We are optimizing a variational parameter 'theta' for a large spin system.
# The energy landscape is complex and highly non-linear.
# ==============================================================================

def classical_energy_landscape(theta: float, noise_matrix: np.ndarray) -> float:
    """Standard NumPy implementation of the energy calculation."""
    # A fake, heavy non-linear transformation representing a chemical ansatz
    val = np.sin(theta**2) * np.exp(-theta / 10.0)
    # Heavy matrix operation to simulate computational cost
    transformed_matrix = noise_matrix * val
    return float(np.sum(np.tanh(transformed_matrix)))

def jax_energy_landscape(theta: float, noise_matrix: jnp.ndarray) -> float:
    """JAX implementation. Notice it looks EXACTLY like the NumPy version!"""
    val = jnp.sin(theta**2) * jnp.exp(-theta / 10.0)
    transformed_matrix = noise_matrix * val
    return jnp.sum(jnp.tanh(transformed_matrix))


def main():
    print("--- 🏎️ The Gradient Showdown: Finite Difference vs JAX Autodiff ---")
    
    # Setup
    theta_current = 2.5
    dim = 2000
    
    print(f"Generating a {dim}x{dim} system matrix...")
    np_matrix = np.random.rand(dim, dim)
    
    # JAX arrays are pushed to the accelerator (CPU/GPU)
    jax_matrix = jnp.array(np_matrix)

    # ==============================================================================
    # 1. THE OLD WAY: Finite Differences (NumPy)
    # ==============================================================================
    print("\n[1/2] Calculating Gradient via Finite Differences (NumPy)...")
    epsilon = 1e-5
    
    start_np = time.time()
    # We have to run the massive simulation TWICE
    energy_plus = classical_energy_landscape(theta_current + epsilon, np_matrix)
    energy_minus = classical_energy_landscape(theta_current - epsilon, np_matrix)
    
    grad_np = (energy_plus - energy_minus) / (2 * epsilon)
    time_np = time.time() - start_np
    
    print(f"      Gradient: {grad_np:.6f} | Time: {time_np:.4f} seconds")

    # ==============================================================================
    # 2. THE NEW WAY: Autodiff + JIT (JAX)
    # ==============================================================================
    print("\n[2/2] Calculating Gradient via JAX Autodiff & JIT...")
    
    # We ask JAX to mathematically derive the gradient function for us
    # We also wrap it in 'jit' to compile it instantly to machine code
    compiled_grad_fn = jit(grad(jax_energy_landscape))
    
    # Warm-up run (to hide the compilation time from our benchmark)
    _ = compiled_grad_fn(1.0, jax_matrix)
    
    start_jax = time.time()
    # We run the simulation ONCE, and get the EXACT analytical derivative
    grad_jax = compiled_grad_fn(theta_current, jax_matrix)
    
    # JAX is asynchronous. block_until_ready() forces the timer to wait until math is done.
    grad_jax.block_until_ready() 
    time_jax = time.time() - start_jax
    
    print(f"      Gradient: {grad_jax:.6f} | Time: {time_jax:.4f} seconds")

    # ==============================================================================
    # ANALYTICS
    # ==============================================================================
    speedup = time_np / time_jax
    
    print("\n" + "="*55)
    print("📊 PERFORMANCE ANALYTICS")
    print("="*55)
    
    max_bar_length = 40
    np_bar = "█" * max_bar_length
    jax_bar_length = max(1, int(max_bar_length / speedup))
    jax_bar = "█" * jax_bar_length
    
    print(f"NumPy Time : {time_np:.4f} s | {np_bar}")
    print(f"JAX Time   : {time_jax:.4f} s | {jax_bar}")
    print("-" * 55)
    print(f"🔥 JAX Autodiff is {speedup:.1f}x FASTER!")
    print(f"🎯 Accuracy: JAX is analytically exact. NumPy has truncation error.")
    print("="*55)

if __name__ == "__main__":
    main()