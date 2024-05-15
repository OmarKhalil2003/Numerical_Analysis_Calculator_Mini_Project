# Import necessary modules from tkinter and sympy libraries
from tkinter import *
from tkinter import ttk
import sympy as sp

# Create the main window
Window = Tk()
Window.title("Newton Method")  # Set window title
Window.geometry('1100x750')  # Set window size
Window.config(bg='#34495E')  # Background color changed

# Define the variable x as a symbol for sympy
x = sp.symbols('x')

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()  # Get screen width
    screen_height = window.winfo_screenheight()  # Get screen height
    x = (screen_width - width) // 2  # Calculate x coordinate for centering
    y = (screen_height - height) // 2  # Calculate y coordinate for centering
    window.geometry(f'{width}x{height}+{x}+{y}')  # Set window geometry to center it

# Function to get the initial guess X0
def get_Xnode():
    Xnode = float(XnodeEntry.get())  # Get X0 value from the entry field
    return Xnode

# Function to get the function entered by the user
def get_Function():
    Func = entry.get()  # Get the function expression from the entry field
    return Func

# Function to get the epsilon value
def get_Eps():
    EPS = float(EpsEntry.get())  # Get epsilon value from the entry field
    return EPS

# Function to go back to the previous page
def prevPage():
    Window.destroy()  # Destroy the current window
    import Mainpage  # Import and go back to the main page

# Function to reset all input fields and clear results
def reset_fields():
    XnodeEntry.delete(0, 'end')  # Clear X0 entry field
    EpsEntry.delete(0, 'end')  # Clear epsilon entry field
    entry.delete(0, 'end')  # Clear function entry field
    iter.delete(*iter.get_children())  # Clear Treeview
    ResultRoot['text'] = ""  # Clear result label

# Function to perform the Newton's Method
def newton():
    xo = get_Xnode()  # Get the initial guess X0
    e = get_Eps()  # Get the epsilon value
    xip1 = 0.0  # Initialize X_i+1
    xi = 0.0  # Initialize X_i
    er = 0.0  # Initialize error
    f = sp.sympify(get_Function())  # Convert the function string to a sympy expression
    f_prime = sp.diff(f, x)  # Differentiate the function with respect to x

    for i in range(100):  # Iterate up to 100 times
        xi = xo  # Set current value of X_i
        FDashFi = f_prime.subs(x, xi)  # Evaluate the derivative at X_i
        FX = f.subs(x, xi)  # Evaluate the function at X_i
        c = FX / FDashFi  # Calculate the increment
        xip1 = xi - c  # Calculate X_i+1 using Newton's method

        # Insert values into Treeview for each iteration
        iter.insert(parent='', index='end', iid=i, text='', values=(i, xo, FX, FDashFi, er))

        if er > e or i == 0:  # If error is greater than epsilon or it's the first iteration
            er = abs((xip1 - xi) / xip1) * 100  # Calculate error
            xo = xip1  # Update X0 with X_i+1
        else:  # If error is less than epsilon, exit the loop
            break
    ResultRoot['text'] = f"The Root is: {xo}"  # Display the root

# Function to set quick test values
def set_quick_test_values():
    reset_fields()  # Reset all fields
    XnodeEntry.insert(0, '5')  # Set initial guess X0
    EpsEntry.insert(0, '0.7')  # Set epsilon value
    entry.insert(0, '-0.9*x**2+1.7*x+2.5')  # Set function expression

# Create a frame for the title
Frame1 = Frame(Window, bg='#2C3E50', width='300', height='200')
Frame1.pack(side=TOP, padx='20', pady='20')
LabelTitle = Label(Frame1, bg='#2C3E50', text='Newton Method', fg='#E74C3C', width='300', font=('Helvetica', 16, 'bold')).pack(padx='20', pady='20')

# Labels and entry fields for X0, epsilon, and function
XnodeL = Label(Window, text=' X0', bg='#34495E', fg='#E74C3C', font=('Helvetica', 11, 'bold')).pack(padx='10')
XnodeEntry = Entry(Window, width='30', borderwidth=5, justify=CENTER)
XnodeEntry.pack(padx='10', pady='10')

EPSL = Label(Window, text=' Epsilon', bg='#34495E', fg='#E74C3C', font=('Helvetica', 11, 'bold')).pack(padx='10')
EpsEntry = Entry(Window, width='30', borderwidth=5, justify=CENTER)
EpsEntry.pack(padx='10', pady='10')

f_label = Label(Window, text="f(x)", bg='#34495E', fg='#E74C3C', font=('Helvetica', 11, 'bold')).pack()
entry = Entry(Window, width='30', borderwidth=5, justify=CENTER)
entry.pack(padx='3', pady='3')

# Button to perform Newton's Method
ButtonRes = Button(Window, text='Determine Root', fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=newton).pack(padx='5', pady='5')

# Treeview for displaying the iterations
iter = ttk.Treeview(Window, columns=(1, 2, 3, 4, 5), show='headings', height=8)
iter.pack()
iter.column("1", anchor=CENTER, stretch=NO, width=100)
iter.heading(1, text='i', anchor=CENTER)
iter.column("2", anchor=CENTER, stretch=NO, width=100)
iter.heading(2, text='Xi', anchor=CENTER)
iter.column("3", anchor=CENTER, stretch=NO, width=100)
iter.heading(3, text='f(Xi)', anchor=CENTER)
iter.column("4", anchor=CENTER, stretch=NO, width=100)
iter.heading(4, text='f`(Xi)', anchor=CENTER)
iter.column("5", anchor=CENTER, stretch=NO, width=100)
iter.heading(5, text='Error%', anchor=CENTER)

# Label to display the result
ResultRoot = Label(Window, text="", fg='#E74C3C', font=('Helvetica', 14, 'bold'), bg='#34495E')
ResultRoot.pack()

# Frame for buttons
button_frame = Frame(Window, bg='#34495E')
button_frame.pack()

# Button to go back to the previous page
ButtonBack = Button(button_frame, text='Back', fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=prevPage)
ButtonBack.pack(side=LEFT, padx='5', pady='5')

# Button to reset all fields
ButtonReset = Button(button_frame, text='Reset', fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=reset_fields)
ButtonReset.pack(side=LEFT, padx='5', pady='5')

# Quick Test Button
quick_test_button = Button(Window, text='Quick Test', fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=set_quick_test_values)
quick_test_button.pack(padx='5', pady='5')

# Start the main loop
Window.mainloop()
