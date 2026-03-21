# 07. Environment Management: "It Works on My Machine" 🌍

## The Problem
You write a brilliant algorithm that runs perfectly on your laptop. You send the code to a collaborator. They run it and get a massive wall of errors. 

Why? Because your laptop has `numpy` version 2.0.0 and Python 3.12, but their laptop has `numpy` version 1.19.0 and Python 3.8. Functions have been deprecated, math behaves differently, and the code breaks. 

If you install all your Python packages globally on your computer, every project shares the same libraries. Upgrading `scipy` for Project A might completely break Project B.

## The Solution: Virtual Environments
A virtual environment is like a soundproof room for your project. It contains its own private Python interpreter and its own private folder of installed libraries. What happens inside the environment stays inside the environment.

There are two main tools for this in computational science: **pip/venv** and **Conda**.

---

## 1. The Standard Way: `pip` and `requirements.txt`
This is the native Python method. It is lightweight and perfect for pure Python projects.

**How to create and use it:**
```bash
# 1. Create a virtual environment named "venv"
python -m venv venv

# 2. Activate it (Mac/Linux)
source venv/bin/activate

# 3. Install packages
pip install numpy scipy pennylane qiskit
```

### The requirements.txt File:
Instead of telling people "just pip install these 10 things," you give them a list.
To generate this list from your current environment, run:

```bash
pip freeze > requirements.txt
```
To install everything from a list someone else gave you:

```bash
pip install -r requirements.txt
```

## 2. The Heavyweight Way: Conda and environment.yml
For physics and data science, packages often rely on heavy C++ or Fortran libraries under the hood. ``pip`` sometimes struggles to compile these. Conda is a package manager designed specifically to handle these complex scientific dependencies.

### How to create and use it:
Instead of a text file, Conda uses an ```environment.yml``` file to build the room.

```bash
# 1. Create the environment from a file
conda env create -f environment.yml

# 2. Activate it
conda activate qml_env
```

To export your current Conda environment so someone else can replicate it:

```bash
conda env export --no-builds > environment.yml
```
## Best Practices for Researchers
1. **Never use the "base" environment**: Treat your system's base Python like the foundation of a house. Never install random packages into it. Always create a new room (environment) for a new paper or project.

2. **Commit the recipe, not the ingredients**: Always commit requirements.txt or environment.yml to your GitHub repository. Never commit the actual venv/ folder (we added this to .gitignore in Lesson 06!).

3. **Pin your versions**: Don't just list numpy. List numpy==1.26.4. This guarantees that if numpy releases a breaking update next year, your paper's code will still run exactly as it did today.