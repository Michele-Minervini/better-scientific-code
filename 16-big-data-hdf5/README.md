# 16. Big Data Formats: Escaping the RAM Trap with HDF5 🗄️

## The Problem: The RAM Limit
You just ran a Slurm job on a supercomputer that simulated the time evolution of a 6-qubit system over 10,000 time steps. The output is a NumPy array of shape `(10000, 64, 64)`. 

If you save this as an `.npz` file, you face two massive problems:
1. **Metadata Loss:** Where do you save the `beta`, `dt`, and `learning_rate` used to generate this data? Usually, researchers resort to messy filenames like `data_beta1.5_dt0.01.npz`.
2. **The RAM Crash:** Six months later, you want to plot the matrix at time step `t=5000`. To get it, `np.load()` forces your laptop to load the entire 10,000-step array into your RAM. If the file is 50GB, your laptop crashes.

## The Solution: `h5py` (HDF5)
HDF5 is designed specifically for big data. It solves both problems beautifully by acting like a virtual hard drive inside a single `.h5` file.

*(To install: `pip install h5py`)*

### The Three Pillars of HDF5
1. **Groups (Folders):** You can organize data inside the file using a directory structure (e.g., `/experiment_1/`).
2. **Datasets (Files):** The actual NumPy arrays, stored efficiently and highly compressed.
3. **Attributes (Metadata):** Tiny dictionaries attached directly to Groups or Datasets. You can pin your experimental parameters directly to the data they generated!

## The Superpower: "Lazy Loading"
When you open an `.h5` file in Python, **no data is loaded into memory**. 
Python just looks at the table of contents. If you ask for `dataset[5000, :, :]`, HDF5 goes straight to that exact byte on your hard drive, lifts out *only* that single matrix, and leaves the rest of the 50GB file safely on the disk.

This allows you to analyze terabytes of data on a standard MacBook.