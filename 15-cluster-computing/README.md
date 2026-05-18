# 15. Cluster Computing: Moving to the Supercomputer 🖥️

## The Problem: The Login Node Trap
When you SSH into a university cluster (`ssh username@cluster.edu`), you land on what is called the **Login Node**. 
The #1 mistake new researchers make is running `python script.py` right there. The login node is just the lobby of the hotel; it has very little power. If you run heavy math in the lobby, the system administrators will kill your process and send you an angry email.

To do real work, you must request a room (a **Compute Node**) by submitting a "Job".

## The Solution: Slurm and Bash Scripts
**Slurm** is the traffic cop of the supercomputer. You interact with it by writing a bash script (`.sh`) that tells Slurm exactly what resources you need and what commands to run once those resources are granted.

### The 4 Essential Slurm Commands
* `sbatch submit_job.sh` : Submits your job to the queue.
* `squeue -u your_username` : Checks the status of your jobs (waiting, running, or failed).
* `scancel 123456` : Cancels job number 123456.
* `sinfo` : Shows the status of the cluster (how many nodes are free).

## Anatomy of a Slurm Script
A Slurm script is just a standard terminal script with a block of "magic" comments at the top. These comments start with `#SBATCH` and act as your request form to the traffic cop.

1. **Resources:** How many CPUs? How much RAM? How much time? *(Never ask for 10 days if your script takes 2 hours; smaller requests skip the line faster).*
2. **Environment:** Supercomputers are bare-bones. You must explicitly load Python and activate your virtual environment (Lesson 07).
3. **Execution:** Finally, you call your Python script, usually passing arguments via the CLI we built in Lesson 08!