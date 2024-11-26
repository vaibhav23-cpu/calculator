import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def button_click(value):
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid input!")
            entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display the current expression
entry = tk.Entry(root, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create and place buttons
row_val = 1
col_val = 0

for button in buttons:
    tk.Button(
        root, text=button, font=("Arial", 20), width=5, height=2, 
        command=lambda val=button: button_click(val)
    ).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main event loop
root.mainloop()