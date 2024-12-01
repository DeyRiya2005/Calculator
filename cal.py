import tkinter as tk

# Function to handle button clicks
def button_click(value):
    if value == "C":
        entry.delete(0, tk.END)  # Clear the entry field
    elif value == "=":
        try:
            expression = entry.get()
            result = eval(expression)  # Evaluate the mathematical expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)  # Insert the clicked value into the entry field

# Main application window
root = tk.Tk()
root.title("My Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#00134b")

# Title Label
title_label = tk.Label(root, text="CALCULATOR", font=("Arial", 20, "bold"), bg="#00134b", fg="#00cc80")
title_label.grid(row=0, column=0, columnspan=4, pady=10)

# Entry field for user input
entry = tk.Entry(root, font=("Arial", 24), bg="#80eeff", borderwidth=2, relief="solid", justify="right")
entry.grid(row=1, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)

# Button configuration
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Colors for the buttons
button_colors = {
    "C": "#800000", "=": "#80003c", "/": "#73cc1a", "*": "#73cc1a", 
    "-": "#73cc1a", "+": "#73cc1a"
}
default_color = "#008000"

# Create buttons and place them in the grid
row_value = 2
col_value = 0
for button in buttons:
    btn = tk.Button(
        root, text=button, font=("Arial", 18), bg=button_colors.get(button, default_color), 
        fg="white", width=5, height=2, command=lambda b=button: button_click(b)
    )
    btn.grid(row=row_value, column=col_value, padx=5, pady=5)
    col_value += 1
    if col_value > 3:
        col_value = 0
        row_value += 1

# Author name at the bottom
author_label = tk.Label(root, text="Made by Riya Dey", font=("Arial", 12, "italic"), bg="#00134b", fg="tomato")
author_label.grid(row=6, column=0, columnspan=4, pady=10)

# Run the application
root.mainloop()