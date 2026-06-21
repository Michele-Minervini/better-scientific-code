# 20. Experiment Tracking: Escaping the Spreadsheet Nightmare 📊

## The Problem: The "Naming" Convention
When running parameter sweeps or optimizing variational circuits, researchers usually rely on messy filenames and manual spreadsheets to remember their results:
* `results_lr0.01_beta1.5.csv`
* `plot_final_v3_USE_THIS.png`
* `model_weights_backup.npz`

Six months later, when you are writing the paper, you will have absolutely no idea what code produced which plot. You also have no easy way to compare the loss curves of 50 different runs overlaid on the same graph without writing a custom, fragile matplotlib script.

## The Solution: Weights & Biases (W&B)
**Weights & Biases (`wandb`)** is the industry standard for experiment tracking. It acts as a cloud-based flight data recorder for your code. 

With three lines of Python, it automatically logs:
1. Every hyperparameter you used.
2. The Git commit hash of the code you ran (so you know *exactly* what version of the math produced the data).
3. System hardware metrics (CPU/GPU utilization and memory).
4. Real-time loss curves, fidelities, and terminal outputs.

*(To install: `pip install wandb`)*

## The 3 Steps of Tracking

### 1. Initialize (`wandb.init`)
You start the recorder. You tell it the name of your project, and you hand it a dictionary of your configuration parameters.
```python
import wandb

wandb.init(
    project="quantum-phase-transition",
    config={
        "learning_rate": 0.01,
        "n_qubits": 8,
        "ansatz": "hardware_efficient"
    }
)
```
### 2. Log Metrics (wandb.log)
Inside your training loop, instead of appending to a CSV or printing to the terminal, you send a dictionary to the cloud.

```Python
for step in range(100):
    loss = compute_loss()
    wandb.log({"step": step, "energy_loss": loss})
```
### 3. The Dashboard
You open your browser and go to ``wandb.ai``. You instantly have beautiful, interactive dashboards where you can filter, group, and compare thousands of runs. No matplotlib code required.
# Why This is Essential for Research
When your PI or collaborator asks, "How did the model perform when we increased the system size?", you don't need to dig through folders. You send them a URL to a W&B report. It creates a single source of truth for your entire lab's computational output.