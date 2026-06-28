# 21. Workflow Orchestration: Automated Pipelines (Snakemake) 🐍

## The Problem: Breaking the Dependency Chain
Scientific research requires multi-step pipelines. Data generation feeds into model training, which feeds into analysis, which feeds into plotting. 

If you modify the source data or tweak a parameter in step 1, you must manually re-execute every downstream script in the correct order. This is error-prone. If you fail to rerun the plotting script, you risk publishing a paper with figures that do not match your underlying data.

## The Solution: Snakemake
Snakemake is a workflow management system based on Python. You define "Rules." Each rule specifies an input file, an output file, and the command required to generate the output from the input.

*(To install: `pip install snakemake`)*

Snakemake reads your rules and builds a **Directed Acyclic Graph (DAG)** of dependencies. 

### The Core Mechanics
1. **Target-Driven Execution:** You do not tell Snakemake what to run. You ask it for a specific file (e.g., `figure_1.pdf`). Snakemake traces the dependencies backward to determine exactly which scripts need to run to produce that PDF.
2. **Intelligent Caching:** If you ask Snakemake to generate `figure_1.pdf` again, it checks the timestamps of the source files. If the inputs have not changed, it does nothing. If a single intermediate file was modified, it recalculates *only* the affected downstream steps.
3. **Cluster Integration:** Snakemake integrates seamlessly with Slurm (Lesson 15). It can automatically dispatch individual rules to different cluster nodes based on their resource requirements.

## Why This is Essential for Publications
A `Snakefile` acts as executable documentation for your methodology. When you publish your code, reviewers do not need to guess the execution order of your scripts. They type `snakemake` in the terminal, and the entire pipeline executes sequentially, generating the exact figures used in your manuscript.