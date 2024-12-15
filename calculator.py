import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, getcontext
import math
from sympy import gcd, lcm

def calculate(operation):
    try:
        getcontext().prec = int(precision_entry.get())  # Set precision for Decimal
        x = Decimal(entry_x.get()) if entry_x.get() else None
        y = Decimal(entry_y.get()) if entry_y.get() else None

        if operation == "add":
            result.set(x + y)
        elif operation == "subtract":
            result.set(x - y)
        elif operation == "multiply":
            result.set(x * y)
        elif operation == "divide":
            if y == 0:
                raise ValueError("Division by zero is undefined")
            result.set(x / y)
        elif operation == "power":
            result.set(x ** y)
        elif operation == "sqrt":
            if x < 0:
                raise ValueError("Cannot calculate the square root of a negative number")
            result.set(x.sqrt())
        elif operation == "factorial":
            if x % 1 != 0 or x < 0:
                raise ValueError("Factorial is only defined for non-negative integers")
            result.set(math.factorial(int(x)))
        elif operation == "mod":
            result.set(x % y)
        elif operation == "gcd":
            result.set(gcd(int(x), int(y)))
        elif operation == "lcm":
            result.set(lcm(int(x), int(y)))
        elif operation == "scientific_notation":
            result.set(f"{x:.{int(precision_entry.get())}E}")
        elif operation == "absolute":
            result.set(abs(x))
        elif operation == "negation":
            result.set(-x)
        elif operation == "reciprocal":
            if x == 0:
                raise ValueError("Cannot compute reciprocal of zero")
            result.set(1 / x)
        elif operation == "square":
            result.set(x ** 2)
        elif operation == "cube":
            result.set(x ** 3)
        elif operation == "ln":
            if x <= 0:
                raise ValueError("Logarithm undefined for zero or negative values")
            result.set(x.ln())
        elif operation == "log10":
            if x <= 0:
                raise ValueError("Logarithm undefined for zero or negative values")
            result.set(math.log10(x))
        elif operation == "exp":
            result.set(x.exp())
        elif operation == "nCr":
            if x % 1 != 0 or y % 1 != 0 or x < y:
                raise ValueError("nCr is only defined for non-negative integers where n ≥ r")
            result.set(math.comb(int(x), int(y)))
        elif operation == "nPr":
            if x % 1 != 0 or y % 1 != 0 or x < y:
                raise ValueError("nPr is only defined for non-negative integers where n ≥ r")
            result.set(math.perm(int(x), int(y)))
        elif operation == "floor_division":
            if y == 0:
                raise ValueError("Division by zero is undefined")
            result.set(x // y)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Big Number Calculator")

# Input Fields
tk.Label(root, text="X:").grid(row=0, column=0, padx=5, pady=5)
entry_x = tk.Entry(root, width=50)
entry_x.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Y:").grid(row=1, column=0, padx=5, pady=5)
entry_y = tk.Entry(root, width=50)
entry_y.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Precision:").grid(row=2, column=0, padx=5, pady=5)
precision_entry = tk.Entry(root, width=10)
precision_entry.insert(0, "20")  # Default precision
precision_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Result Field with Larger Font
result = tk.StringVar()
tk.Label(root, text="Result:").grid(row=3, column=0, padx=5, pady=5)
result_display = tk.Entry(
    root, textvariable=result, state="readonly", font=("Arial", 16), fg="blue", width=70
)
result_display.grid(row=3, column=1, padx=5, pady=5)

# Buttons for Operations
operations = [
    ("Add", "add"), ("Subtract", "subtract"), ("Multiply", "multiply"), ("Divide", "divide"),
    ("Power (X^Y)", "power"), ("Square Root (√X)", "sqrt"), ("Factorial (X!)", "factorial"),
    ("Modulo (X % Y)", "mod"), ("GCD", "gcd"), ("LCM", "lcm"), ("Scientific Notation", "scientific_notation"),
    ("Absolute Value (|X|)", "absolute"), ("Negation (-X)", "negation"), ("Reciprocal (1/X)", "reciprocal"),
    ("Square (X^2)", "square"), ("Cube (X^3)", "cube"), ("Natural Log (ln X)", "ln"),
    ("Log Base-10 (log10 X)", "log10"), ("Exponential (e^X)", "exp"),
    ("Combination (nCr)", "nCr"), ("Permutation (nPr)", "nPr"), ("Floor Division (X // Y)", "floor_division")
]

for i, (text, op) in enumerate(operations):
    tk.Button(root, text=text, command=lambda op=op: calculate(op), width=20).grid(row=4 + i // 3, column=i % 3, padx=5, pady=5)

# Run the GUI
root.mainloop()

