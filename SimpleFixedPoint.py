# Import necessary modules from tkinter, ttk, messagebox, and sympy libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sympy as sp

# Create the main window
Window = Tk()
Window.title("Simple Fixed Point Method")  # Set window title
Window.geometry('1100x750')  # Set window size
Window.config(bg='#34495E')  # Background color changed

# Define fonts
title_font = ("Helvetica", 16, 'bold')
label_font = ("Helvetica", 11)
button_font = ("Helvetica", 11, 'bold')

# Function to center the window on the screen
def center_window(window, width, height):
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y positions to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window geometry to center it
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to simplify the equation entered by the user using sympy
def simplify_equation(expr):
    x = sp.symbols('x')  # Define the variable x
    simplified_expr = sp.sympify(expr)  # Convert the input expression to a SymPy expression
    simplified_expr = sp.simplify(simplified_expr)  # Simplify the expression further
    return simplified_expr

# Function to perform the Simple Fixed Point Method
def simple_fixed_point():
    X0 = float(XnodeEntry.get())  # Get X0 value from user
    Ep = float(EpsEntry.get())  # Get epsilon value from user
    user_expr = entry.get()  # Get the user-provided expression
    simplified_expr = simplify_equation(user_expr)  # Simplify the user-provided expression
    f = sp.lambdify(sp.symbols('x'), simplified_expr)  # Convert to a lambda function

    XiP1 = 0.0  # Initialize Xiplus1
    xi = 0.0  # Initialize Xi
    Er_ = 0.0  # Initialize Error
    for i in range(100):  # Iterate up to 100 times

        xi = X0  # Xnode will be stored in new variable xi
        XiP1 = f(X0)  # Xiplus1 will be equal to the substitution of X0 in the function
        XIP1F = float(XiP1)  # Convert XiPlus1 to float

        # Insert values into Treeview for each iteration
        iter.insert(parent='', index='end', iid=i, text='', values=(i, xi, XIP1F, Er_))

        if Er_ > Ep or i == 0:  # If error is greater than epsilon or it's the first iteration
            Er_ = abs((XIP1F - xi) / XIP1F) * 100  # Calculate error
            X0 = XIP1F  # Update X0 with Xiplus1
        else:  # If error is less than epsilon, exit the loop
            break
    ResultRoot['text'] = f"The Root is :{X0} "  # Display the root
    return xi

# Function to reset the page
def reset_page():
    XnodeEntry.delete(0, END)  # Clear X0 entry field
    EpsEntry.delete(0, END)  # Clear epsilon entry field
    entry.delete(0, END)  # Clear function entry field
    ResultRoot.config(text="")  # Clear result label
    iter.delete(*iter.get_children())  # Clear Treeview

# Function to go back to the main page
def back_to_main():
    Window.destroy()  # Destroy current window
    import Mainpage  # Import and go back to the main page

# Create a frame for the title
title_frame = Frame(Window, bg='#34495E')
title_frame.pack(pady=20)

# Title label
LabelTitle = Label(title_frame, text='Simple Fixed Point Method', bg='#34495E', fg='#E74C3C', font=title_font)
LabelTitle.pack(pady=10)

# Create frame for input fields
input_frame = Frame(Window, bg='#34495E')
input_frame.pack(pady=20)

# Labels and entry fields for X0 and epsilon
XnodeL = Label(input_frame, text=' X0:', bg='#34495E', font=label_font)
XnodeL.grid(row=0, column=0, padx=10, pady=5)
XnodeEntry = Entry(input_frame, width=30, borderwidth=2)
XnodeEntry.grid(row=0, column=1, padx=10, pady=5)

EPSL = Label(input_frame, text=' Epsilon:', bg='#34495E', font=label_font)
EPSL.grid(row=1, column=0, padx=10, pady=5)
EpsEntry = Entry(input_frame, width=30, borderwidth=2)
EpsEntry.grid(row=1, column=1, padx=10, pady=5)

f_label = Label(input_frame, text="f(x)[Simplified]:", bg='#34495E', font=label_font)
f_label.grid(row=2, column=0, padx=10, pady=5)
entry = Entry(input_frame, width=30, borderwidth=2)
entry.grid(row=2, column=1, padx=10, pady=5)

# Label to display the result
ResultRoot = Label(Window, text="", bg='#34495E', fg='#FF5733', font=label_font)
ResultRoot.pack(pady=10)

# Treeview for displaying the iterations
iter = ttk.Treeview(Window, columns=("i", "Xi", "f(Xi)", "Error%"), show='headings', height=8)
iter.pack(pady=20)
iter.heading("i", text="i")
iter.heading("Xi", text="Xi")
iter.heading("f(Xi)", text="f(Xi)")
iter.heading("Error%", text="Error%")

# Button frame
button_frame = Frame(Window, bg='#34495E')
button_frame.pack(pady=20)

# Button to perform the Simple Fixed Point Method
ButtonRes = Button(button_frame, text='Determine Root', bg='#34495E', fg='#E74C3C', font=button_font,
                   command=simple_fixed_point)
ButtonRes.pack(padx='5', pady='5')

# Button to reset the page
ButtonReset = Button(button_frame, text='Reset', bg='#34495E', fg='#E74C3C', font=button_font, command=reset_page)
ButtonReset.pack(padx='5', pady='5')

# Button to go back to the main page
ButtonBack = Button(button_frame, text='Back', bg='#34495E', fg='#E74C3C', font=button_font, command=back_to_main)
ButtonBack.pack(padx='5', pady='5')

# Configure style for the Treeview
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", foreground='#FF5733', background='#F0F0F0', font=label_font)
style.configure('Treeview.Heading', background="#34495E", foreground='#E74C3C', font=label_font)
style.map("Treeview", background=[('selected', '#FF5733')])

# Function for quick testing with predefined values
def quick_test():
    XnodeEntry.delete(0, END)
    EpsEntry.delete(0, END)
    entry.delete(0, END)
    
    # Predefined values for quick testing
    XnodeEntry.insert(0, "5")
    EpsEntry.insert(0, "0.2")
    entry.insert(0, "(1.8*x+2.5)**0.5")

# Button for quick testing
ButtonQuickTest = Button(button_frame, text='Quick Test', bg='#34495E', fg='#E74C3C', font=button_font, command=quick_test)
ButtonQuickTest.pack(padx='5', pady='5')

# Start the main loop
Window.mainloop()
