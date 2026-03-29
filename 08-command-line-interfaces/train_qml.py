# This script simulates a Quantum Machine Learning training loop (e.g., for finding ground states of molecules). It demonstrates how to properly set up the argument parser in the `main` block.

import argparse
import time

def run_vqe_training(n_qubits, lr, max_steps, save_results):
    """
    A mock function representing a quantum algorithm or QML training loop.
    """
    print(f"\n🚀 Initializing Quantum Environment...")
    print(f"   - Qubits: {n_qubits}")
    print(f"   - Learning Rate: {lr}")
    print(f"   - Max Steps: {max_steps}")
    
    # Fake training loop
    energy = 0.0
    for step in range(1, max_steps + 1):
        energy -= lr * (1 / step)  # Fake optimization descent
        if step % 50 == 0:
            print(f"   Step {step}/{max_steps} | Energy: {energy:.4f} Ha")
            time.sleep(0.1)
            
    print("✅ Training Complete.")
    
    if save_results:
        print(f"💾 Saving optimized parameters to disk...")
        # e.g., np.savez("optimized_params.npz", ...)

if __name__ == "__main__":
    # 1. Initialize Parser
    parser = argparse.ArgumentParser(
        description="Run a Quantum Machine Learning optimization loop.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter # Shows defaults in help menu!
    )
    
    # 2. Add Arguments
    parser.add_argument(
        "-q", "--qubits", 
        type=int, 
        default=4, 
        help="Number of qubits representing the molecular system."
    )
    
    parser.add_argument(
        "-lr", "--learning_rate", 
        type=float, 
        default=0.01, 
        help="Step size for the optimizer."
    )
    
    parser.add_argument(
        "--steps", 
        type=int, 
        default=100, 
        help="Maximum number of training iterations."
    )
    
    parser.add_argument(
        "--save", 
        action="store_true", 
        help="Include this flag to save the final state to disk."
    )
    
    # 3. Parse Arguments
    args = parser.parse_args()
    
    # 4. Pass arguments to the physics engine
    run_vqe_training(
        n_qubits=args.qubits, 
        lr=args.learning_rate, 
        max_steps=args.steps, 
        save_results=args.save
    )