# This script simulates generating a large dataset and saving it properly with its physical metadata attached.

import h5py
import numpy as np
import time
import os

def main():
    print("--- 💾 Generating Big Data (HDF5) ---")
    
    # 1. Setup our "simulation" parameters
    n_steps = 5000
    dim = 64
    beta = 1.5
    dt = 0.01
    
    print(f"Allocating ({n_steps}, {dim}, {dim}) complex array in RAM...")
    # Generate ~320 MB of dummy data in RAM
    heavy_data = np.random.rand(n_steps, dim, dim) + 1j * np.random.rand(n_steps, dim, dim)
    
    # Ensure a data folder exists
    if not os.path.exists('data'):
        os.makedirs('data')
        
    filename = "data/simulation_results.h5"
    
    print(f"Writing to {filename}...")
    start_time = time.time()
    
    # 2. Open the HDF5 file in 'w' (write) mode
    with h5py.File(filename, 'w') as f:
        
        # Create a "folder" for this specific run
        run_group = f.create_group('run_001')
        
        # 3. Attach METADATA directly to the group! 
        # (No more ugly filenames)
        run_group.attrs['beta'] = beta
        run_group.attrs['dt'] = dt
        run_group.attrs['n_qubits'] = 6
        run_group.attrs['author'] = "Michele"
        run_group.attrs['date'] = time.strftime("%Y-%m-%d")
        
        # 4. Save the heavy data with GZIP compression
        run_group.create_dataset(
            'density_matrices', 
            data=heavy_data, 
            compression='gzip',   # Squashes the file size down dramatically
            compression_opts=4    # 1-9 (4 is a good balance of speed vs size)
        )
        
    end_time = time.time()
    file_size_mb = os.path.getsize(filename) / (1024 * 1024)
    
    print(f"✅ Saved {file_size_mb:.1f} MB file in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()