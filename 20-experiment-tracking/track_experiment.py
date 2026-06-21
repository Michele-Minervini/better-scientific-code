# This script simulates a VQE (Variational Quantum Eigensolver) or machine learning training loop. It demonstrates how seamlessly you can inject tracking into an existing script.

import time
import math
import random
import argparse
import wandb

def simulate_training_loop(config):
    """
    A mock optimization loop. We simulate the loss decreasing over time,
    with some noise added based on the system size.
    """
    print(f"🚀 Starting optimization for {config.n_qubits} qubits...")
    
    current_energy = 5.0  # Starting high energy
    
    for epoch in range(1, config.epochs + 1):
        # 1. Simulate the math (Loss goes down, but bounces around)
        noise = (random.random() - 0.5) * (config.n_qubits / 10.0)
        gradient_descent_step = config.learning_rate * math.log(epoch + 1)
        
        current_energy = current_energy - gradient_descent_step + noise
        
        # Calculate a secondary metric (e.g., State Fidelity)
        fidelity = 1.0 - math.exp(-epoch / 20.0)
        
        # 2. THE MAGIC: Log the metrics to the cloud
        # wandb automatically tracks the step count!
        wandb.log({
            "epoch": epoch,
            "ground_state_energy": current_energy,
            "state_fidelity": fidelity,
        })
        
        # Print to terminal just so we can watch it locally
        if epoch % 10 == 0:
            print(f"   Epoch {epoch:03d} | Energy: {current_energy:.4f} | Fidelity: {fidelity:.4f}")
            
        time.sleep(0.05) # Fake computation delay
        
    print("✅ Training complete.")
    
    # 3. Save a final artifact (like an array or model weights)
    # wandb will upload this file and link it permanently to this specific run!
    with open("final_ansatz_parameters.txt", "w") as f:
        f.write("theta_1 = 0.54\ntheta_2 = 1.23")
    
    wandb.save("final_ansatz_parameters.txt")


def main():
    parser = argparse.ArgumentParser(description="Tracked Quantum Optimization")
    parser.add_argument("--lr", type=float, default=0.01, help="Learning Rate")
    parser.add_argument("--qubits", type=int, default=4, help="System Size")
    parser.add_argument("--epochs", type=int, default=100, help="Training Steps")
    args = parser.parse_args()

    # ==============================================================================
    # INITIALIZE WEIGHTS & BIASES
    # ==============================================================================
    # The first time you run this, it will ask you to paste an API key from wandb.ai
    
    run = wandb.init(
        project="research-software-handbook",
        notes="Testing the new tracking integration.",
        tags=["baseline", "tutorial"],
        config={
            "learning_rate": args.lr,
            "n_qubits": args.qubits,
            "epochs": args.epochs,
            "optimizer": "Adam",
            "ansatz_depth": 3
        }
    )
    
    # Run the physics
    simulate_training_loop(wandb.config)
    
    # Safely close the recorder
    wandb.finish()

if __name__ == "__main__":
    main()