import pyttsx3  # Import pyttsx3 for voice feedback
import math
import tkinter as tk
from tkinter import messagebox, simpledialog

# Global Variables
memory = None
history = []

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def greet_user():
    """Greets the user with their name."""
    user_name = simpledialog.askstring("Welcome", "What's your name?")
    if user_name:
        label_greeting.config(text=f"Hello, {user_name}! Ready to learn and calculate?")
    else:
        label_greeting.config(text="Hello! Ready to learn and calculate?")

def display_steps(steps):
    """Display the steps of calculation in the UI."""
    label_steps.config(text="Steps:\n" + "\n".join(steps))

def basic_operations(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = None
        steps = []

        if operation == "+":
            result = num1 + num2
            steps = [f"{num1} + {num2} = {result}"]
        elif operation == "-":
            result = num1 - num2
            steps = [f"{num1} - {num2} = {result}"]
        elif operation == "*":
            result = num1 * num2
            steps = [f"{num1} × {num2} = {result}"]
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = num1 / num2
            steps = [f"{num1} ÷ {num2} = {result}"]
        elif operation == "%":
            result = num1 % num2
            steps = [f"{num1} % {num2} = {result}"]

        log_history(f"{num1} {operation} {num2}", result)
        label_result.config(text=f"Result: {result}")
        display_steps(steps)  # Correctly call display_steps here
        give_feedback(result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))


def advanced_operations(operation):
    try:
        num = float(entry_num1.get())
        steps = []
        if operation == "sqrt":
            if num < 0:
                raise ValueError("Square root of a negative number is not supported.")
            result = math.sqrt(num)
            steps = [f"√{num} = {result}"]
            log_history(f"√{num}", result)
        elif operation == "power":
            exponent = float(entry_num2.get())
            result = math.pow(num, exponent)
            steps = [f"{num} ^ {exponent} = {result}"]
            log_history(f"{num} ^ {exponent}", result)
        else:
            raise ValueError("Invalid operation.")

        label_result.config(text=f"Result: {result}")
        display_steps(steps)
        give_feedback(result)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def unit_conversion(conversion_type):
    """Converts units between meters/kilometers or grams/kilograms."""
    try:
        value = float(entry_num1.get())
        result = None
        steps = []

        if conversion_type == "m_to_km":
            result = value / 1000
            steps = [f"{value} meters ÷ 1000 = {result} kilometers"]
        elif conversion_type == "km_to_m":
            result = value * 1000
            steps = [f"{value} kilometers × 1000 = {result} meters"]
        elif conversion_type == "g_to_kg":
            result = value / 1000
            steps = [f"{value} grams ÷ 1000 = {result} kilograms"]
        elif conversion_type == "kg_to_g":
            result = value * 1000
            steps = [f"{value} kilograms × 1000 = {result} grams"]

        log_history(f"{value} {conversion_type}", result)
        label_result.config(text=f"Result: {result}")
        display_steps(steps)
        give_feedback(result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

def decimal_to_binary():
    """Convert decimal to binary."""
    try:
        decimal_value = int(entry_num1.get())
        result = bin(decimal_value)[2:]  # convert to binary string
        steps = [f"{decimal_value} in binary is {result}"]
        log_history(f"{decimal_value} binary", result)
        label_result.config(text=f"Result: {result}")
        display_steps(steps)
        give_feedback(result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid decimal number.")

def decimal_to_hex():
    """Convert decimal to hexadecimal."""
    try:
        decimal_value = int(entry_num1.get())
        result = hex(decimal_value)[2:]  # convert to hex string
        steps = [f"{decimal_value} in hexadecimal is {result}"]
        log_history(f"{decimal_value} hex", result)
        label_result.config(text=f"Result: {result}")
        display_steps(steps)
        give_feedback(result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid decimal number.")

def binary_to_decimal():
    """Convert binary to decimal."""
    try:
        binary_value = entry_num1.get()
        result = int(binary_value, 2)  # convert binary string to decimal
        steps = [f"{binary_value} in decimal is {result}"]
        log_history(f"{binary_value} decimal", result)
        label_result.config(text=f"Result: {result}")
        display_steps(steps)
        give_feedback(result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid binary number.")

def hex_to_decimal():
    """Convert hexadecimal to decimal."""
    try:
        hex_value = entry_num1.get()
        result = int(hex_value, 16)  # convert hex string to decimal
        steps = [f"{hex_value} in decimal is {result}"]
        log_history(f"{hex_value} decimal", result)
        label_result.config(text=f"Result: {result}")
        display_steps(steps)
        give_feedback(result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid hexadecimal number.")

def log_history(operation, result):
    """Logs calculations to the history."""
    history.append(f"{operation} = {result}")
    label_history.config(text="\n".join(history[-5:]))  # Display last 5 entries

def give_feedback(result):
    """Provides voice feedback for correct or incorrect results."""
    if result is not None:
        engine.say(f"The result is {result}")
        engine.runAndWait()

# Functions for C and AC
def clear_entry():
    """Clear the current input fields."""
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")

def all_clear():
    """Reset the entire calculator."""
    global memory, history
    memory = None
    history = []
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    label_result.config(text="Result: ")
    label_history.config(text="History: ")
    label_memory.config(text="Memory: None")
    label_steps.config(text="Steps:")

def memory_store():
    """Store the current result in memory."""
    global memory
    try:
        memory = float(label_result.cget("text").split(": ")[1])
        label_memory.config(text=f"Memory: {memory}")
    except ValueError:
        messagebox.showerror("Memory Error", "No valid result to store.")

def memory_recall():
    """Recall the value stored in memory."""
    global memory
    if memory is not None:
        entry_num1.delete(0, tk.END)
        entry_num1.insert(0, memory)
        messagebox.showinfo("Memory Recall", f"Recalled value: {memory}")
    else:
        messagebox.showerror("Memory Error", "No value stored in memory.")

def memory_clear():
    """Clear the memory."""
    global memory
    memory = None
    label_memory.config(text="Memory: None")
    messagebox.showinfo("Memory Clear", "Memory cleared.")

# GUI Setup
root = tk.Tk()
root.title("Advanced Calculator")

# Greeting Section
frame_greeting = tk.Frame(root)
frame_greeting.pack(pady=10)

label_greeting = tk.Label(frame_greeting, text="Welcome! Ready to learn and calculate?", font=("Helvetica", 12))
label_greeting.pack()
greet_user()

# Input Section
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="Number 1:").grid(row=0, column=0, padx=5)
entry_num1 = tk.Entry(frame_input)
entry_num1.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Number 2:").grid(row=1, column=0, padx=5)
entry_num2 = tk.Entry(frame_input)
entry_num2.grid(row=1, column=1, padx=5)

# Buttons Section
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# Basic Operations
tk.Button(frame_buttons, text="+", command=lambda: basic_operations("+")).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="-", command=lambda: basic_operations("-")).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="*", command=lambda: basic_operations("*")).grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="/", command=lambda: basic_operations("/")).grid(row=0, column=3, padx=5)
tk.Button(frame_buttons, text="%", command=lambda: basic_operations("%")).grid(row=0, column=4, padx=5)

# Advanced Operations
tk.Button(frame_buttons, text="√", command=lambda: advanced_operations("sqrt")).grid(row=1, column=0, padx=5)
tk.Button(frame_buttons, text="^", command=lambda: advanced_operations("power")).grid(row=1, column=1, padx=5)

# Unit Conversions
tk.Button(frame_buttons, text="m to km", command=lambda: unit_conversion("m_to_km")).grid(row=1, column=2, padx=5)
tk.Button(frame_buttons, text="km to m", command=lambda: unit_conversion("km_to_m")).grid(row=1, column=3, padx=5)
tk.Button(frame_buttons, text="g to kg", command=lambda: unit_conversion("g_to_kg")).grid(row=1, column=4, padx=5)
tk.Button(frame_buttons, text="kg to g", command=lambda: unit_conversion("kg_to_g")).grid(row=1, column=5, padx=5)

# Number Conversion
tk.Button(frame_buttons, text="Decimal to Binary", command=decimal_to_binary).grid(row=2, column=0, padx=5)
tk.Button(frame_buttons, text="Decimal to Hex", command=decimal_to_hex).grid(row=2, column=1, padx=5)
tk.Button(frame_buttons, text="Binary to Decimal", command=binary_to_decimal).grid(row=2, column=2, padx=5)
tk.Button(frame_buttons, text="Hex to Decimal", command=hex_to_decimal).grid(row=2, column=3, padx=5)

# Memory Functions
tk.Button(frame_buttons, text="MC", command=memory_clear).grid(row=2, column=4, padx=5)
tk.Button(frame_buttons, text="MR", command=memory_recall).grid(row=2, column=5, padx=5)
tk.Button(frame_buttons, text="MS", command=memory_store).grid(row=2, column=6, padx=5)

# Clear and All Clear
tk.Button(frame_buttons, text="C", command=clear_entry).grid(row=3, column=0, padx=5)
tk.Button(frame_buttons, text="AC", command=all_clear).grid(row=3, column=1, padx=5)

# Result Display
frame_result = tk.Frame(root)
frame_result.pack(pady=10)

label_result = tk.Label(frame_result, text="Result: ", font=("Helvetica", 14))
label_result.pack()

# History Display
frame_history = tk.Frame(root)
frame_history.pack(pady=10)

label_history = tk.Label(frame_history, text="History: ", font=("Helvetica", 12))
label_history.pack()

# Calculation Steps Display
frame_steps = tk.Frame(root)
frame_steps.pack(pady=10)

label_steps = tk.Label(frame_steps, text="Steps:", font=("Helvetica", 12))
label_steps.pack()

# Memory Display
frame_memory = tk.Frame(root)
frame_memory.pack(pady=10)

label_memory = tk.Label(frame_memory, text="Memory: None", font=("Helvetica", 12))
label_memory.pack()

# Run the GUI
root.mainloop()
