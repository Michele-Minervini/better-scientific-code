# 18. Packaging: Building an Installable Library 📦

## The Problem: "Module Not Found"
You spent months building a robust codebase for simulating spin systems and phase properties. Now, you want to write a quick Jupyter Notebook in a completely different folder to plot some results. 

You type `from qchem_algorithms import dynamics`, and Python throws a `ModuleNotFoundError`. 

Python only looks for imports in two places: the folder you are currently in, and its global `site-packages` directory (where things like `numpy` live). If your code isn't in either, Python is blind to it.

## The Solution: The `pip install` Standard
Instead of hacking your system paths, you should package your code so that `pip` recognizes it as a real library. 

Historically, this was done using a highly confusing file called `setup.py`. Today, the entire Python community has unified around a single, clean standard: **`pyproject.toml`**.

## How to Package Your Code

### 1. The `src/` Layout
To prevent Python from getting confused about what is a script and what is a library, the industry standard is to hide your library folder inside a `src/` directory.

### 2. The `pyproject.toml` File
This is a plain-text configuration file that sits at the root of your project. It tells `pip` what your package is named, who wrote it, and what dependencies it needs to run.

### 3. The Local Install (Editable Mode)
When developing, you don't want to re-install your package every time you fix a bug. You install it in **Editable Mode** using the `-e` flag.

Open your terminal in the same folder as your `pyproject.toml` and run:
```bash
pip install -e .
```
(The . means "look in this current directory").

Now, your code is symbolically linked into your Python environment. You can open a terminal anywhere on your Mac or cluster, run Python, and import your library perfectly. Any changes you make to the source code are instantly reflected without needing to reinstall.

# The Final Boss: Publishing to PyPI
Once you have your ``pyproject.toml`` set up, you are only two commands away from sharing your code with the world.
Tools like ```build``` and ``twine`` allow you to upload your package to the Python Package Index. Once there, anyone in the world can run ``pip install your-package-name``!


# How to test this:

1. Open your terminal and navigate to ``18-packaging``.

2. Run the magic command: ``pip install -e .`` (Make sure your virtual environment is activated if you are using one!).

3. Now, leave that folder. Go to your desktop, or your documents folder, or anywhere else.

4. Launch Python in the terminal by typing ``python``.

5. Type ``import qchem_algorithms``. It works.

6. Type ``qchem_algorithms.evolve_spin_system(4, 10.0)``. It executes.

7. Your codebase is now a fully-fledged, globally accessible software library on your machine.