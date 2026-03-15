# 06. Git & GitHub: Version Control for Research 🐙

## The "Time Machine" Mindset
Git is not a backup system like Google Drive or Dropbox. It is a **version control system**. 
Google Drive saves the *state* of a file. Git saves the *history of changes* (the "diffs"). If you break your quantum algorithm today, Git allows you to instantly rewind your code back to exactly how it looked last Tuesday at 4:00 PM.



## The Three Stages of Git
To use Git effectively, you must understand its three areas:
1.  **Working Directory:** Your actual files on your computer. You edit them here.
2.  **Staging Area (The "Loading Dock"):** You use `git add` to place specific changed files here, preparing them to be saved.
3.  **The Repository (The "Vault"):** You use `git commit` to permanently save everything in the Staging Area into the timeline.

## Best Practice 1: The `.gitignore` File
This is the #1 mistake researchers make. You should **never** commit data files, compiled binaries, or virtual environments to GitHub.
If you commit a 5GB `.npz` file of density matrices, your repository will become bloated, slow, and GitHub will eventually block you.

Create a file named literally `.gitignore` in the root of your project. Git will pretend any file listed inside it doesn't exist.

## Best Practice 2: Atomic Commits
A commit should represent **one logical change**. Do not work for three weeks and submit one massive commit called `Update everything`. 

**Bad Workflow:**
* Edit Hamiltonian logic, fix a plotting bug, rewrite the README.
* `git commit -m "updates"`

**Good Workflow (Atomic):**
* `git add physics_math.py` $\to$ `git commit -m "Fix sign error in commutator calculation"`
* `git add plot.py` $\to$ `git commit -m "Change plot axes to logarithmic scale"`

## Best Practice 3: How to Write a Commit Message
A good commit message tells your future self **WHY** a change was made, not just **WHAT** changed. The "what" can be seen in the code diff. The "why" is in your head.

* ❌ **Bad:** `Changed beta to 1.5`
* ✅ **Good:** `Increase default inverse temperature to 1.5 to capture low-energy ground state dynamics`

**The "If applied" rule:** A good commit message should complete the sentence: *"If applied, this commit will..."*
* ...`Fix typo in README`
* ...`Add tqdm progress bar to simulation loop`

## Best Practice 4: Branching for "Experiments"
When you have a working simulation but want to try a crazy new idea (like swapping your numerical solver), **do not edit the working code.** Create a branch.



```bash
# Create a new parallel universe for your idea
git checkout -b try-new-solver

# ... do your work, break things, commit them ...

# If the idea is terrible, you can just delete the branch.
# If it works perfectly, you merge it back into your main code!
git checkout main
git merge try-new-solver