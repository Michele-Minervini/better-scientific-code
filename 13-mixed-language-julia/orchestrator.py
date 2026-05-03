## This is our Python script. It handles the user interface and timing, but hands the actual computation off to the Julia module.

import time
import random
import math
from juliacall import Main as jl

# --- THE PURE PYTHON EQUIVALENT ---
def simulate_heavy_stochastic_process_python(steps: int, initial_state: float) -> float:
    """The exact same math, but trapped in a slow Python for-loop."""
    state = initial_state
    for _ in range(steps):
        noise = random.random() - 0.5
        state = math.sin(state + noise)
    return state

def main():
    print("--- 🚀 Python vs. Julia: The 'Two-Language' Showdown ---")
    
    # 1. Setup
    print("Loading Julia physics engine... (This takes a moment on the first run)")
    jl.include("physics_engine.jl")
    engine = jl.PhysicsEngine
    
    steps = 10_000_000
    initial_state = 1.0
    
    print(f"\nTarget: Custom sequential stochastic loop for {steps:,} steps.")
    
    # --- 2. RUN PURE PYTHON ---
    print("\n[1/2] Running pure Python implementation...")
    py_start = time.time()
    py_final_state = simulate_heavy_stochastic_process_python(steps, initial_state)
    py_end = time.time()
    py_time = py_end - py_start
    print(f"      Result: {py_final_state:.6f} | Time: {py_time:.4f} seconds")

    # --- 3. RUN JULIA VIA JULIACALL ---
    print("\n[2/2] Running Julia implementation (via juliacall)...")
    
    # WARM-UP: Julia compiles the function the first time it sees it.
    # We run a tiny 10-step dummy call so compilation isn't included in our timer.
    _ = engine.simulate_heavy_stochastic_process(10, initial_state) 
    
    jl_start = time.time()
    jl_final_state = engine.simulate_heavy_stochastic_process(steps, initial_state)
    jl_end = time.time()
    jl_time = jl_end - jl_start
    print(f"      Result: {jl_final_state:.6f} | Time: {jl_time:.4f} seconds")

    # --- 4. FANCY ANALYTICS ---
    speedup = py_time / jl_time
    
    print("\n" + "="*55)
    print("📊 PERFORMANCE ANALYTICS")
    print("="*55)
    
    # Generate a visual bar chart in the terminal
    max_bar_length = 40
    py_bar = "█" * max_bar_length
    jl_bar_length = max(1, int(max_bar_length / speedup)) # Scale Julia bar relative to Python
    jl_bar = "█" * jl_bar_length
    
    print(f"Python Time : {py_time:.4f} s | {py_bar}")
    print(f"Julia Time  : {jl_time:.4f} s | {jl_bar}")
    print("-" * 55)
    print(f"🔥 Julia is {speedup:.1f}x FASTER than Python!")
    print("="*55)

if __name__ == "__main__":
    main()