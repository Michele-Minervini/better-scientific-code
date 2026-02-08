# 02. Stop Printing, Start Debugging 🐞

## The "Print Statement" Trap
When code doesn't work, the instinct is to sprinkle `print(variable)` everywhere.
* `print("Here 1")`
* `print(matrix.shape)`
* `print("Why is this zero??")`

**Why this is bad for Research Code:**
1.  **Clutter:** You have to delete them all later, risking deleting actual code.
2.  **Noise:** If you run a simulation loop 10,000 times, you get 10,000 lines of output, burying the error.
3.  **Limited View:** You only see what you *thought* to print. You can't see the hidden state (like a variable `n` that was supposed to be `N`) that actually caused the bug.

## The Solution: The VS Code Debugger
The Debugger is a tool that lets you **pause time** inside your code. It freezes the universe at a specific line so you can walk around, inspect variables, and even run new math equations using the current memory state.



## Key Concepts

### 1. The Breakpoint (🔴)
* **What it is:** A "Stop Sign" you place on a line of code.
* **How to set it:** Click to the left of the line number in VS Code (in the margin). A bright red dot appears.
* **Effect:** When Python execution reaches this line, it **freezes** *before* executing it.

### 2. The Controls (Top Toolbar)
Once the code is frozen, a floating toolbar appears at the top:
* **▶️ Continue (F5):** Resume normal speed until the next breakpoint (or the end).
* **↷ Step Over (F10):** Run the current line and stop at the next one. (Most common action).
* **⬇️ Step Into (F11):** If the current line is a function call, dive *inside* that function definition.
* **⬆️ Step Out (Shift+F11):** Finish the current function immediately and return to the line where it was called.
* **🟥 Stop (Shift+F5):** Kill the program immediately.

### 3. The "Variables" Pane (Left Side)
* **Locals:** Shows every variable currently alive in memory.
* **Data Viewer:** This is a superpower for physics. Right-click large lists or NumPy arrays and select **"View Value in Data Viewer"**. This opens a spreadsheet view—essential for checking if your matrices are correct!

### 4. The Debug Console (Bottom) 🌟
* This is your "Jupyter Cell" inside the debugger.
* While the code is frozen, you can type Python code here using the current variables.
* **Example:** You are paused at `x = 5`. You can type `x + 10` in the console, and it returns `15`.
* **Use Case:** Test a fix for a bug *before* you actually write it in the code.

## The Workflow for Fixing Bugs

1.  **Spot the Bug:** "The energy is becoming NaN after step 50."
2.  **Set Breakpoint:** Put a red dot inside the loop or function where you suspect the math goes wrong (e.g., right before the division).
3.  **Launch (F5):** Press F5 or click the "Run and Debug" icon on the left sidebar. Select "Python File" if asked.
4.  **Inspect:** Look at the Variables pane. Is `H` the right shape? Is `beta` zero?
5.  **Step:** Use F10 to move line-by-line and watch how the variables change.
6.  **Fix:** Stop the debugger (Red Square), edit the code, and run again.

## Practice Task
Open `practice_debug.py` in this folder. It contains a deliberate bug in a normalization function.
1.  Run it and see the failure message.
2.  Use the debugger to find *why* `Z` is calculated incorrectly.
3.  Fix it!
