import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, getcontext
import math
from sympy import gcd, lcm

def parse_input(value, is_hex):
    """Convert input based on whether it's decimal or hexadecimal."""
    if is_hex:
        return Decimal(int(value, 16))  # Convert hex to decimal
    return Decimal(value)  # Decimal input

def calculate(operation):
    try:
        getcontext().prec = int(precision_entry.get())  # Set precision for Decimal
        x = parse_input(entry_x.get(), hex_x.get()) if entry_x.get() else None
        y = parse_input(entry_y.get(), hex_y.get()) if entry_y.get() else None

        if operation == "add":
            result_decimal = x + y
        elif operation == "subtract":
            result_decimal = x - y
        elif operation == "multiply":
            result_decimal = x * y
        elif operation == "divide":
            if y == 0:
                raise ValueError("Division by zero is undefined")
            result_decimal = x / y
        elif operation == "floor_division":
            if y == 0:
                raise ValueError("Division by zero is undefined")
            result_decimal = x // y
        elif operation == "mod":
            result_decimal = x % y
        elif operation == "power":
            result_decimal = x ** y
        elif operation == "square":
            result_decimal = x ** 2
        elif operation == "cube":
            result_decimal = x ** 3
        elif operation == "sqrt":
            if x < 0:
                raise ValueError("Cannot calculate the square root of a negative number")
            result_decimal = x.sqrt()
        elif operation == "cbrt":
            result_decimal = Decimal(x ** (1 / 3))  # Cubic root
        elif operation == "factorial":
            if x % 1 != 0 or x < 0:
                raise ValueError("Factorial is only defined for non-negative integers")
            result_decimal = Decimal(math.factorial(int(x)))
        elif operation == "nCr":
            if x % 1 != 0 or y % 1 != 0 or x < y:
                raise ValueError("nCr is only defined for non-negative integers where n ≥ r")
            result_decimal = Decimal(math.comb(int(x), int(y)))
        elif operation == "nPr":
            if x % 1 != 0 or y % 1 != 0 or x < y:
                raise ValueError("nPr is only defined for non-negative integers where n ≥ r")
            result_decimal = Decimal(math.perm(int(x), int(y)))
        elif operation == "ln":
            if x <= 0:
                raise ValueError("Logarithm undefined for zero or negative values")
            result_decimal = x.ln()
        elif operation == "log10":
            if x <= 0:
                raise ValueError("Logarithm undefined for zero or negative values")
            result_decimal = Decimal(math.log10(x))
        elif operation == "exp":
            result_decimal = x.exp()
        elif operation == "absolute":
            result_decimal = abs(x)
        elif operation == "negation":
            result_decimal = -x
        elif operation == "reciprocal":
            if x == 0:
                raise ValueError("Cannot compute reciprocal of zero")
            result_decimal = Decimal(1 / x)
        elif operation == "scientific_notation":
            result_decimal = Decimal(f"{x:.{int(precision_entry.get())}E}")
        elif operation == "gcd":
            result_decimal = Decimal(gcd(int(x), int(y)))
        elif operation == "lcm":
            result_decimal = Decimal(lcm(int(x), int(y)))
        else:
            raise ValueError("Invalid operation")

        # Update result fields
        decimal_result.set(f"Decimal: {result_decimal}")
        hex_result.set(f"Hex: {hex(int(result_decimal))}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def toggle_theme(theme):
    """Switch between predefined color schemes."""
    colors = themes[theme]
    root.configure(bg=colors['bg'])
    for widget in root.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.configure(bg=colors['entry_bg'], fg=colors['fg'], insertbackground=colors['fg'])
        else:
            widget.configure(bg=colors['bg'], fg=colors['fg'])
    result_display_decimal.configure(bg=colors['result_bg'], fg=colors['result_fg'])
    result_display_hex.configure(bg=colors['result_bg'], fg=colors['result_fg'])

# Predefined color themes
themes = {
    "Light Mode": {
        "bg": "white",
        "fg": "black",
        "entry_bg": "#f9f9f9",
        "result_bg": "#e9e9e9",
        "result_fg": "black"
    },
    "Dark Mode": {
        "bg": "#2e2e2e",
        "fg": "#e0e0e0",
        "entry_bg": "#3b3b3b",
        "result_bg": "#1e1e1e",
        "result_fg": "#00ff00"
    }
}

# GUI setup
root = tk.Tk()
root.title("Big Number Calculator")
current_theme = "Dark Mode"  # Default theme

# Input Fields for X
tk.Label(root, text="X (Decimal):").grid(row=0, column=0, padx=5, pady=5)
entry_x = tk.Entry(root, width=50)
entry_x.grid(row=0, column=1, padx=5, pady=5)

hex_x = tk.BooleanVar()  # Checkbox for X being in hex
tk.Checkbutton(root, text="Hex", variable=hex_x).grid(row=0, column=2)

# Input Fields for Y
tk.Label(root, text="Y (Decimal):").grid(row=1, column=0, padx=5, pady=5)
entry_y = tk.Entry(root, width=50)
entry_y.grid(row=1, column=1, padx=5, pady=5)

hex_y = tk.BooleanVar()  # Checkbox for Y being in hex
tk.Checkbutton(root, text="Hex", variable=hex_y).grid(row=1, column=2)

# Precision Control
tk.Label(root, text="Precision:").grid(row=2, column=0, padx=5, pady=5)
precision_entry = tk.Entry(root, width=10)
precision_entry.insert(0, "20")  # Default precision
precision_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

# Result Fields
decimal_result = tk.StringVar()
tk.Label(root, text="Decimal Result:").grid(row=3, column=0, padx=5, pady=5)
result_display_decimal = tk.Entry(
    root, textvariable=decimal_result, state="readonly", width=70
)
result_display_decimal.grid(row=3, column=1, padx=5, pady=5)

hex_result = tk.StringVar()
tk.Label(root, text="Hex Result:").grid(row=4, column=0, padx=5, pady=5)
result_display_hex = tk.Entry(
    root, textvariable=hex_result, state="readonly", width=70
)
result_display_hex.grid(row=4, column=1, padx=5, pady=5)

# Theme Toggle Dropdown
tk.Label(root, text="Theme:").grid(row=5, column=0, padx=5, pady=5)
theme_dropdown = tk.StringVar(value=current_theme)
tk.OptionMenu(root, theme_dropdown, *themes.keys(), command=toggle_theme).grid(row=5, column=1)

# Buttons for Operations
operations = [
    ("Add", "add"), ("Subtract", "subtract"), ("Multiply", "multiply"), ("Divide", "divide"),
    ("Power (X^Y)", "power"), ("Square Root (√X)", "sqrt"), ("Factorial (X!)", "factorial"),
    ("Modulo (X % Y)", "mod"), ("GCD", "gcd"), ("LCM", "lcm"), ("Scientific Notation", "scientific_notation"),
    ("Absolute Value (|X|)", "absolute"), ("Negation (-X)", "negation"), ("Reciprocal (1/X)", "reciprocal"),
    ("Square (X^2)", "square"), ("Cube (X^3)", "cube"), ("Cubic Root (³√X)", "cbrt"),
    ("Natural Log (ln X)", "ln"), ("Log Base-10 (log10 X)", "log10"), ("Exponential (e^X)", "exp"),
    ("Combination (nCr)", "nCr"), ("Permutation (nPr)", "nPr"), ("Floor Division (X // Y)", "floor_division")
]

for i, (text, op) in enumerate(operations):
    tk.Button(
        root, text=text, command=lambda op=op: calculate(op), width=20
    ).grid(row=6 + i // 3, column=i % 3, padx=5, pady=5)

# Apply initial theme
toggle_theme(current_theme)

# Run the GUI
root.mainloop()

