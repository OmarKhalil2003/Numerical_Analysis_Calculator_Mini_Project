# Import necessary modules from tkinter and math libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import *

# Create a Tkinter window
Window = Tk()
Window.title("False Position Method")  # Set window title
Window.geometry('1100x750')  # Set window size

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

# Configure window background color
Window.config(bg='#34495E')

# Font configurations
f = ("Helvetica", 14, 'bold')
title_font = ("Helvetica", 16, 'bold')
label_font = ("Helvetica", 11)
button_font = ("Helvetica", 11, 'bold')

# Function to evaluate the mathematical expression entered by the user
def get_function(x):
    try:
        result = eval(entry.get(), {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, "x": x})
        return result
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during expression evaluation: {e}")

# Functions to get user inputs for X lower, X upper, and epsilon
def get_x_lower():
    try:
        xl = float(x_lower_entry.get())
        return xl
    except ValueError:
        messagebox.showerror("Error", "Invalid input for X lower")
        return None

def get_x_upper():
    try:
        xu = float(x_upper_entry.get())
        return xu
    except ValueError:
        messagebox.showerror("Error", "Invalid input for X upper")
        return None

def get_epsilon():
    try:
        epsilon = float(epsilon_entry.get())
        return epsilon
    except ValueError:
        messagebox.showerror("Error", "Invalid input for epsilon")
        return None

# False position method function to find the root of the equation
def false_position():
    xl = get_x_lower()  # Get X lower value from user input
    xu = get_x_upper()  # Get X upper value from user input
    ep = get_epsilon()  # Get epsilon value from user input
    if xl is None or xu is None or ep is None:
        return
    
    xr = 0.0  # Initialize variable for the estimated root
    xrold = 0.0  # Initialize variable to store old estimated root
    error = 0.0  # Initialize error variable
    i = 0  # Initialize iteration counter

    # Loop until the error is less than or equal to epsilon
    while True:
        xrold = xr
        fxl = get_function(xl)  # Calculate f(X lower)
        fxu = get_function(xu)  # Calculate f(X upper)
        fxli = float(fxl)
        fxui = float(fxu)
        xr = xu - (fxui * (xl - xu) / (fxli - fxui))  # Estimate the root using false position formula
        poly_check = fxli * fxui
        if poly_check >= 0:
            messagebox.showwarning("Warning!!", "No solution exists")
            return
        fxr = get_function(xr)  # Calculate f(X root)
        fxri = float(fxr)
        error = abs((xr - xrold) / xr) * 100  # Calculate error percentage
        if i == 0:
            # Insert iteration data into the treeview
            iter_tree.insert(parent='', index='end', iid=i, text='', values=(i, xl, fxli, xu, fxui, xr, fxri, ' '))
        else:
            iter_tree.insert(parent='', index='end', iid=i, text='', values=(i, xl, fxli, xu, fxui, xr, fxri, error))
        sign_check = fxli * fxri
        if sign_check > 0:
             xl = xr
        elif sign_check < 0:
            xu = xr
        else:
            result_label['text'] = f"The Root is: {xr}"
            return xr
        i += 1
        if error <= ep:
            break
     
    result_label['text'] = f"The Root is: {xr}"

# Function to reset all input fields and clear the result label
def reset_page():
    x_lower_entry.delete(0, END)
    x_upper_entry.delete(0, END)
    epsilon_entry.delete(0, END)
    entry.delete(0, END)
    result_label.config(text="")
    for item in iter_tree.get_children():
        iter_tree.delete(item)

# Function to destroy the current window and return to the main page
def back_to_main():
    Window.destroy()
    import Mainpage

# Function to perform a quick test using predefined values
def quick_test():
    # Set predefined values for quick testing
    x_lower_entry.insert(0, "0.5")
    x_upper_entry.insert(0, "1")
    epsilon_entry.insert(0, "0.2")
    entry.insert(0, "-26+82.3*x-88*x**2 + 45.4*x**3 - 9*x**4 + 0.65*x**5")

    # Call the false position method
    false_position()

# Frame for the title
title_frame = Frame(Window, bg='#34495E')
title_frame.pack(pady=20)

# Label for the title
Label(title_frame, text='False Position Method', bg='#34495E', fg='#E74C3C', font=title_font).pack(pady=10)

# Frame for input fields
input_frame = Frame(Window, bg='#34495E')
input_frame.pack(pady=20)

# Labels and entry fields for X lower, X upper, and epsilon
Label(input_frame, text='X lower:', bg='#34495E', fg='#E74C3C', font=label_font).grid(row=0, column=0, padx=10, pady=5)
x_lower_entry = Entry(input_frame, width=30, borderwidth=2, font=label_font)
x_lower_entry.grid(row=0, column=1, padx=10, pady=5)

Label(input_frame, text='X upper:', bg='#34495E', fg='#E74C3C', font=label_font).grid(row=1, column=0, padx=10, pady=5)
x_upper_entry = Entry(input_frame, width=30, borderwidth=2, font=label_font)
x_upper_entry.grid(row=1, column=1, padx=10, pady=5)

Label(input_frame, text='Epsilon:', bg='#34495E', fg='#E74C3C', font=label_font).grid(row=2, column=0, padx=10, pady=5)
epsilon_entry = Entry(input_frame, width=30, borderwidth=2, font=label_font)
epsilon_entry.grid(row=2, column=1, padx=10, pady=5)

Label(input_frame, text="f(x):", bg='#34495E', fg='#E74C3C', font=label_font).grid(row=3, column=0, padx=10, pady=5)
entry = Entry(input_frame, width=30, borderwidth=2, font=label_font)
entry.grid(row=3, column=1, padx=10, pady=5)

# Treeview to display iteration data
iter_tree = ttk.Treeview(Window, columns=("i", "Xl", "f(Xl)", "Xu", "f(Xu)", "Xr", "f(Xr)", "Error (%)"), show='headings', height=9)
iter_tree.pack()

# Configure headings for the treeview
for col in ("i", "Xl", "f(Xl)", "Xu", "f(Xu)", "Xr", "f(Xr)", "Error (%)"):
    iter_tree.heading(col, text=col)
    iter_tree.column(col, anchor=CENTER, stretch=NO, width=100)

# Frame for buttons
button_frame = Frame(Window, bg='#34495E')
button_frame.pack()

# Buttons to perform actions
Button(button_frame, text='Determine Root', bg='#34495E', fg='#E74C3C', font=f, command=false_position).pack(padx='5', pady='5')
Button(button_frame, text='Reset',bg='#34495E', fg='#E74C3C', font=f, command=reset_page).pack(padx='5', pady='5')
Button(button_frame, text='Back',bg='#34495E', fg='#E74C3C', font=f, command=back_to_main).pack(padx='5', pady='5')

# Button for quick testing
Button(button_frame, text='Quick Test', bg='#34495E', fg='#E74C3C', font=f, command=quick_test).pack(padx='5', pady='5')

# Label to display the result
result_label = Label(Window, text="", fg='#E74C3C', font=("Helvetica", 14, 'bold'), bg='#34495E')
result_label.pack()

# Style configurations for the treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", foreground='#E74C3C', background='#34495E', font=('Arial', 10))
style.configure('Treeview.Heading', background='#34495E', foreground='#E74C3C', font=('Arial', 10, 'bold'))
style.map("Treeview", background=[('selected', '#34495E')])

# Center the window on the screen
center_window(Window, 1000, 700)

# Start the Tkinter event loop
Window.mainloop()
