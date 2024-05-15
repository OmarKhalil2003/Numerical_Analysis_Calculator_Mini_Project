# Import necessary modules from tkinter and math libraries
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import *

# Define the main window
Window = Tk()
Window.title("False Position Method")  # Set window title
Window.geometry('1100x750')  # Set window size
Window.config(bg='#2C3E50')  # Background color changed

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

# Function to get the input values
def get_Xi():
    Xi = float(XiE.get())  # Get Xi value from entry field
    return Xi

def get_Xm():
    Xm = float(XMinEntry.get())  # Get Xi-1 value from entry field
    return Xm

def get_Epson():
    EPS = float(EpsEntry.get())  # Get epsilon value from entry field
    return EPS

def get_Function(x):
    try:
        result = eval(entry.get(), {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, "x": x})
        return result
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during expression evaluation: {e}")

# Function to execute the Secant Method
def SecantMethod():
    Er_ = 0.0  # Initialize error
    xiPlus1 = 0.0  # Initialize xiPlus1
    xi = get_Xi()  # Get Xi value from user input
    XiM1 = get_Xm()  # Get Xi-1 value from user input
    Ep = get_Epson()  # Get epsilon value from user input
    
    for i in range(100):  # Iterate to find the root
        XIF = get_Function(xi)  # Evaluate function at Xi
        XIFF = float(XIF)
        XIM = get_Function(XiM1)  # Evaluate function at Xi-1
        XIMF = float(XIM)
        xiPlus1 = xi - (XIFF * (XiM1 - xi)) / (XIMF - XIFF)  # Calculate next xi using Secant method formula
        iter.insert(parent='', index='end', iid=i, text='', values=(i, XiM1, XIMF, xi, XIFF, Er_))

        if Er_ > Ep or i == 0:  # Check if error is greater than epsilon or it's the first iteration
            Er_ = abs((xiPlus1 - xi) / xiPlus1) * 100  # Calculate error percentage
            XiM1 = xi  # Update Xi-1
            xi = xiPlus1  # Update Xi
        else:  # If error is less than epsilon, exit the loop
            break
    ResultRoot['text'] = f"The Root is :{xi} "  # Display the root
    return xi

# Function to reset entries and clear results
def reset():
    XiE.delete(0, END)  # Clear Xi entry field
    XMinEntry.delete(0, END)  # Clear Xi-1 entry field
    EpsEntry.delete(0, END)  # Clear epsilon entry field
    entry.delete(0, END)  # Clear function entry field
    iter.delete(*iter.get_children())  # Clear treeview
    ResultRoot.config(text='')  # Clear result label

# Function to go back to the main page
def back_to_main():
    Window.destroy()  # Destroy current window
    import Mainpage  # Import and go back to the main page

# Frame and Labels
Frame1 = Frame(Window, bg='#34495E', width='300', height='200')  # Create frame for title
Frame1.pack(side=TOP, padx='20', pady='20')
LabelTitle = Label(Frame1, bg='#34495E', text='Secant Method', fg='#E74C3C', width='300', font=('Helvetica', 16, 'bold')).pack(padx='20', pady='20')  # Title label

XiLAbel = Label(Window, text=' Xi', bg='#2C3E50', fg='#E74C3C', font=('Helvetica', 11, 'bold')).pack(padx='10')  # Label for Xi entry
XiE = Entry(Window, width='30', borderwidth=5, justify=CENTER)  # Entry field for Xi
XiE.pack(padx='3', pady='3')
XMinLAbel = Label(Window, text=' Xi-1', bg='#2C3E50', fg='#E74C3C', font=('Helvetica', 11, 'bold')).pack(padx='10')  # Label for Xi-1 entry
XMinEntry = Entry(Window, width='30', borderwidth=5, justify=CENTER)  # Entry field for Xi-1
XMinEntry.pack(padx='10', pady='10')
EPSL = Label(Window, text=' Epson', bg='#2C3E50', fg='#E74C3C', font=('Helvetica', 11, 'bold')).pack(padx='10')  # Label for epsilon entry
EpsEntry = Entry(Window, width='30', borderwidth=5, justify=CENTER)  # Entry field for epsilon
EpsEntry.pack(padx='10', pady='10')
Label(Window, text="f(x)", bg='#2C3E50', fg='#E74C3C', font=('Helvetica', 11, 'bold')).pack()  # Label for function entry
entry = Entry(Window, borderwidth=5, width='30', justify=CENTER)  # Entry field for function
entry.pack(padx='10', pady='10')
ResultRoot = Label(Window, text=' ', bg='#2C3E50', fg='#E74C3C')  # Result label
ResultRoot.pack()

# Treeview
iter = ttk.Treeview(Window, columns=(1, 2, 3, 4, 5, 6), show='headings', height=8)  # Treeview for iterations
iter.pack()
iter.column("1", anchor=CENTER, stretch=NO, width=100)
iter.heading(1, text='i', anchor=CENTER)
iter.column("2", anchor=CENTER, stretch=NO, width=100)
iter.heading(2, text='Xi-1', anchor=CENTER)
iter.column("3", anchor=CENTER, stretch=NO, width=100)
iter.heading(3, text='f(Xi-1)', anchor=CENTER)
iter.column("4", anchor=CENTER, stretch=NO, width=100)
iter.heading(4, text='Xi', anchor=CENTER)
iter.column("5", anchor=CENTER, stretch=NO, width=100)
iter.heading(5, text='f(Xi)', anchor=CENTER)
iter.column("6", anchor=CENTER, stretch=NO, width=100)
iter.heading(6, text='Error', anchor=CENTER)

# Button to execute Secant Method
ButtonRes = Button(Window, text='Determine Root', bg="#2C3E50", fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=SecantMethod)
ButtonRes.pack(padx='5', pady='5')

# Button to reset entries and clear results
ButtonReset = Button(Window, text='Reset', bg="#2C3E50", fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=reset)
ButtonReset.pack(padx='5', pady='5')

# Back button
ButtonBack = Button(Window, text='Back', bg="#2C3E50", fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=back_to_main)
ButtonBack.pack(padx='5', pady='5')

# Function for quick testing with predefined values
def quick_test():
    XiE.delete(0, END)  # Clear Xi entry field
    XMinEntry.delete(0, END)  # Clear Xi-1 entry field
    EpsEntry.delete(0, END)  # Clear epsilon entry field
    entry.delete(0, END)  # Clear function entry field
    
    # Predefined values for quick testing
    XiE.insert(0, "3.5")
    XMinEntry.insert(0, "2.5")
    EpsEntry.insert(0, "0.5")
    entry.insert(0, "0.95*x**3-5.9*x**2+10.9*x-6")

# Button for quick testing
ButtonQuickTest = Button(Window, text='Quick Test', bg="#2C3E50", fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=quick_test)
ButtonQuickTest.pack(padx='5', pady='5')

Window.mainloop()  # Start the Tkinter event loop
