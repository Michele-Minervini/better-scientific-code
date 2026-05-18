# This script acts as the "payload". It ties together our CLI knowledge (argparse) and our multiprocessing knowledge (concurrent.futures), explicitly obeying the core limits set by the Slurm script.

import argparse
import time
from concurrent.futures import ProcessPoolExecutor

def heavy_simulation(sample_id):
    """Mock heavy computation."""
    # Simulating a math calculation
    time.sleep(0.1) 
    return sample_id ** 2

def main():
    parser = argparse.ArgumentParser(description="Cluster Compute Payload")
    parser.add_argument("--beta", type=float, required=True, help="Inverse temperature")
    parser.add_argument("--n_samples", type=int, default=100, help="Number of Monte Carlo samples")
    parser.add_argument("--cores", type=int, default=1, help="Number of CPUs granted by Slurm")
    
    args = parser.parse_args()
    
    print(f"--- 🌌 Cluster Job Initialized ---")
    print(f"Parameters : Beta = {args.beta}")
    print(f"Workload   : {args.n_samples} samples")
    print(f"Resources  : {args.cores} CPU Cores allocated by Slurm")
    
    start = time.time()
    
    # Run the parallel workload EXACTLY matching the cores Slurm gave us
    with ProcessPoolExecutor(max_workers=args.cores) as executor:
        results = list(executor.map(heavy_simulation, range(args.n_samples)))
        
    end = time.time()
    
    print(f"\n✅ Simulation Complete.")
    print(f"Processed {len(results)} items in {end - start:.2f} seconds.")

if __name__ == "__main__":
    main()