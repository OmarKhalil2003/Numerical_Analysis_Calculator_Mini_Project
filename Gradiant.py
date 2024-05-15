# Importing necessary modules for GUI creation and mathematical operations
from tkinter import *        # Importing basic tkinter widgets and functions
from tkinter import ttk      # Importing themed tkinter widgets
from tkinter import messagebox   # Importing messagebox for displaying messages
import sympy as sp           # Importing sympy library for symbolic mathematics
from math import *           # Importing mathematical functions like sin, cos, tan, etc.


# Create the main window
Window = Tk()
Window.geometry('1100x750')
Window.title("Gradient Method")
Window.config(bg='#34495E')

# Define the font
f = ("Helvetica", 9, 'bold')

# Function to center the window on the screen
def center_window(window, width, height):
    """
    Center the window on the screen.

    Args:
        window: Tkinter window object.
        width (int): Width of the window.
        height (int): Height of the window.
    """
    # Get the screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y positions to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window geometry to center it
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to get the lower bound input value
def get_X():
    """Get the value of X entered by the user."""
    return float(XEntry.get())

# Function to get the upper bound input value
def get_Y():
    """Get the value of Y entered by the user."""
    return float(YEntry.get())

# Function to get the mathematical function input value
def get_Function(x):
    """
    Get the mathematical function input value.

    Args:
        x: Value of the function variable.

    Returns:
        float: Result of evaluating the function at the given value.
    """
    try:
        result = eval(entry.get(), {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan})
        return result
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during expression evaluation: {e}")

def gradiant():
    # Prompt the user to enter the function f(x, y)
    expr = entry.get()  # Get the user input for the mathematical function
    x_val = float(XEntry.get())  # Get the value of X from the entry field
    y_val = float(YEntry.get())  # Get the value of Y from the entry field

    # Convert the expression string to a sympy expression
    x, y = sp.symbols('x y')  # Define symbolic variables for the mathematical expression
    try:
        f_expr = sp.sympify(expr)  # Convert the user input into a sympy expression
        # Calculate the first-order partial derivatives
        df_dx = sp.diff(f_expr, x)  # Calculate the partial derivative of f with respect to x
        df_dy = sp.diff(f_expr, y)  # Calculate the partial derivative of f with respect to y

        # Calculate the gradient as radians
        gradient_radians = sp.atan2(df_dx, df_dy)  # Calculate the gradient in radians

        # Calculate the second-order partial derivatives
        d2f_dx2 = sp.diff(df_dx, x)  # Calculate the second derivative of f with respect to x
        d2f_dy2 = sp.diff(df_dy, y)  # Calculate the second derivative of f with respect to y
        d2f_dxdy = sp.diff(df_dx, y)  # Calculate the mixed partial derivative of f

        # Create the Hessian matrix
        H = sp.Matrix([[d2f_dx2, d2f_dxdy], [d2f_dxdy, d2f_dy2]])

        # Evaluate H_det numerically
        H_det = H.det().evalf(subs={x: x_val, y: y_val})  # Evaluate the determinant of the Hessian matrix

        # Check if it's a local maximum or minimum
        H_det_value = H_det
        d2f_dx2_val = d2f_dx2.evalf(subs={x: x_val, y: y_val})  # Evaluate the second derivative of f with respect to x
        if H_det_value > 0 and d2f_dx2_val < 0:
            result_text = "The point ({}, {}) is a local maximum.".format(x_val, y_val)
        elif H_det_value > 0 and d2f_dx2_val > 0:
            result_text = "The point ({}, {}) is a local minimum.".format(x_val, y_val)
        else:
            result_text = "The point ({}, {}) may be a saddle point or inconclusive.".format(x_val, y_val)

        # Construct the symbolic steps string
        symbolic_steps_text = "Symbolic Steps:\n"
        symbolic_steps_text += "First-order partial derivatives:\n"
        symbolic_steps_text += f"df/dx: {df_dx}\n"
        symbolic_steps_text += f"df/dy: {df_dy}\n\n"

        symbolic_steps_text += "Gradient as radians:\n"
        symbolic_steps_text += f"{gradient_radians}\n\n"

        symbolic_steps_text += "Second-order partial derivatives:\n"
        symbolic_steps_text += f"d^2f/dx^2: {d2f_dx2}\n"
        symbolic_steps_text += f"d^2f/dy^2: {d2f_dy2}\n"
        symbolic_steps_text += f"d^2f/dxdy: {d2f_dxdy}\n\n"

        symbolic_steps_text += "Hessian matrix:\n"
        symbolic_steps_text += f"{H}\n\n"

        # Construct the numerical steps string
        numerical_steps_text = "Numerical Results:\n"
        numerical_steps_text += f"Hessian determinant: {H_det}\n"
        numerical_steps_text += f"d^2f/dx^2 value: {d2f_dx2_val}\n"

        # Display both symbolic and numerical steps in the Steps text widget
        Steps.delete(1.0, END)  # Clear the contents of the Steps text widget
        Steps.insert(END, symbolic_steps_text + numerical_steps_text)  # Insert the steps into the Steps text widget

        # Display the result
        ResultRoot.config(text=result_text)  # Display the result text in the ResultRoot label
    except sp.SympifyError as e:
        ResultRoot.config(text="Invalid expression: " + str(e))  # Display an error message if the expression is invalid

# Function to reset the page
def reset_page():
    """Reset the input fields and result label."""
    # Clear input fields
    XEntry.delete(0, END)
    YEntry.delete(0, END)
    entry.delete(0, END)
    
    # Clear result label
    ResultRoot.config(text="")

# Function to go back to the previous menu
def back_to_menu():
    """Close the current window and return to the previous menu."""
    Window.destroy()
    import Mainpage
    # Add code to go back to the previous menu

# Function to set quick test values
def set_quick_test_values():
    """Set quick test values for the input fields."""
    reset_page()
    XEntry.insert(0, '-1')
    YEntry.insert(0, '1')
    entry.insert(0, '2*x*y+2*x-x**2-2*y**2')

# GUI setup
Frame1 = Frame(Window, bg='#34495E', width='1000', height='50')
Frame1.pack(side=TOP, fill=X)

LabelTitle = Label(Frame1, text='Gradient Method', bg='#34495E', fg='#FF5733', font=("Helvetica", 16, 'bold'))
LabelTitle.pack(pady='5')

XLAbel = Label(Window, text='X', bg='#34495E', fg='#FF5733', font=f)
XLAbel.place(x=50, y=100)
XEntry = Entry(Window, borderwidth=2, width='30', font=f)
XEntry.place(x=150, y=100)

YLAbel = Label(Window, text='Y', bg='#34495E', fg='#FF5733', font=f)
YLAbel.place(x=50, y=150)
YEntry = Entry(Window, borderwidth=2, width='30', font=f)
YEntry.place(x=150, y=150)

f = Label(Window, text="f(x)", bg='#34495E', fg='#FF5733', font=f)
f.place(x=50, y=200)
entry = Entry(Window, borderwidth=2, width='30', font=f)
entry.place(x=150, y=200)

ResultRoot = Label(Window, text="  ", fg='#E74C3C', font=('Helvetica', 14, 'bold'), bg='#34495E')
ResultRoot.pack()

Result = Label(Window, text="   ", fg='#E74C3C', bg='#34495E')
Result.pack(side=BOTTOM, padx=5, pady=10)

Steps = Text(Window, height=25, width=100, bg='white')
Steps.pack(side=BOTTOM, padx=5, pady=10)

ButtonRes = Button(Window, text='Determine Root', bg='#34495E', fg='#FF5733', font=f, command=gradiant)
ButtonRes.place(x=50, y=700)

ButtonReset = Button(Window, text='Reset', bg='#34495E', fg='#FF5733', font=f, command=reset_page)
ButtonReset.place(x=300, y=700)

ButtonBack = Button(Window, text='Back', bg='#34495E', fg='#FF5733', font=f, command=back_to_menu)
ButtonBack.place(x=450, y=700)

# Quick Test Button
quick_test_button = Button(Window, text='Quick Test', bg='#34495E', fg='#FF5733', font=f, command=set_quick_test_values)
quick_test_button.place(x=550, y=700)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", foreground='#FF5733', background='#34495E', font=("Helvetica", 9, 'bold'))
style.configure('Treeview.Heading', background="#34495E", foreground='#FF5733', font=("Helvetica", 9, 'bold'))
style.map("Treeview", background=[('selected', '#34495E')])

# Call the function to center the window
center_window(Window, 1000, 750)

# Start the GUI event loop
Window.mainloop()
