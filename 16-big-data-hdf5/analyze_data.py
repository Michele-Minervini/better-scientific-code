# This script demonstrates "Lazy Loading." It reads the metadata and extracts exactly one matrix from the middle of the file without loading the massive array into RAM.

import h5py
import numpy as np

def main():
    filename = "data/simulation_results.h5"
    
    print("--- 🔬 Analyzing Big Data (Lazy Loading) ---")
    
    # Open the file in 'r' (read-only) mode for safety
    with h5py.File(filename, 'r') as f:
        
        # 1. Access the group
        run_group = f['run_001']
        
        # 2. Read the Metadata instantly
        print("\n📊 Experimental Parameters Found:")
        for key, value in run_group.attrs.items():
            print(f"   - {key}: {value}")
            
        # 3. Access the dataset (This DOES NOT load the data into RAM!)
        dset = run_group['density_matrices']
        
        print(f"\n📁 Dataset found on disk with shape: {dset.shape} and type: {dset.dtype}")
        
        # 4. LAZY LOADING: Extract exactly one slice.
        # HDF5 goes to the exact location on the hard drive and pulls only this matrix.
        target_step = 2500
        print(f"⏳ Extracting ONLY time step {target_step} into RAM...")
        
        single_matrix = dset[target_step, :, :]
        
        print("✅ Extraction complete.")
        print(f"   Matrix shape in RAM: {single_matrix.shape}")
        print(f"   Trace of matrix: {np.trace(single_matrix):.4f}")

if __name__ == "__main__":
    main()