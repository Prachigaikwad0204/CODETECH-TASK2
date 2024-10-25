import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x / y

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == 'Add':
            result = add(num1, num2)
        elif operation == 'Subtract':
            result = subtract(num1, num2)
        elif operation == 'Multiply':
            result = multiply(num1, num2)
        elif operation == 'Divide':
            result = divide(num1, num2)
        else:
            raise ValueError("Invalid operation.")

        messagebox.showinfo("Result", f"The result is: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# Set up the main application window
root = tk.Tk()
root.title("Basic Calculator")

# Create a frame for better layout control
frame = tk.Frame(root, bg='pink')
frame.pack(padx=20, pady=20)

# Create input fields with custom background colors
entry1 = tk.Entry(frame, width=15, bg='white')
entry1.pack(pady=10)

entry2 = tk.Entry(frame, width=15, bg='white')
entry2.pack(pady=10)

operation_var = tk.StringVar(value='Add')

# Create radio buttons for operations with custom colors
operations = ['Add', 'Subtract', 'Multiply', 'Divide']
for operation in operations:
    tk.Radiobutton(frame, text=operation, variable=operation_var, value=operation, bg='pink').pack(anchor=tk.W)

# Calculate button with custom background
calculate_button = tk.Button(frame, text="Calculate", command=calculate, bg='dark green', fg='white')
calculate_button.pack(pady=20)

# Run the application
root.mainloop()
