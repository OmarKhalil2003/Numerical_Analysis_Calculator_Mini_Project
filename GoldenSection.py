from tkinter import *
from tkinter import ttk  # Import the themed Tkinter module
from tkinter import messagebox  # Import the messagebox module
from math import *  # Import the math module to evaluate mathematical expressions

# Create the main window
Window = Tk()
Window.geometry('1100x750')  # Set the window size
Window.title("Golden Section Method")  # Set the window title
Window.config(bg='#34495E')  # Set the background color

# Define the font
f = ("Helvetica", 9, 'bold')

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

# Function to get the lower bound input value
def get_XLower():
    return float(XLowerEntry.get())

# Function to get the upper bound input value
def get_Xupper():
    return float(XUpperEntry.get())

# Function to get the mathematical function input value
def get_Function(x):
    try:
        result = eval(entry.get(), {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan})
        return result
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during expression evaluation: {e}")

def golden_section_search():
    """
    Perform golden section search optimization algorithm.

    Returns:
        Tuple: The tuple contains the final values of xl, f_xl, xu, f_xu, x1, f_x1, x2, f_x2, and d.
    """
    # Define the mathematical function
    def f(x):
        return eval(entry.get())

    direction = var.get()  # Get the selected optimization direction
    i = 0
    r = 0.618
    xl = get_XLower()  # Get the lower bound input value
    xu = get_Xupper()  # Get the upper bound input value
    
    # Iterate through the specified number of iterations
    for i in range(5):  
        d = (xu - xl) * r  # Recalculate d for each iteration
        x1 = xl + d
        x2 = xu - d
        f_x1 = f(x1)
        f_x2 = f(x2)
        f_xl = f(xl)
        f_xu = f(xu)      
        # Insert values based on the current iteration into the Treeview table
        iter.insert(parent='', index='end', iid=i, text='', values=(i, xl, f_xl, xu, f_xu, x1, f_x1, x2, f_x2, d))
        
        # Determine the next bounds based on the optimization direction
        if direction == 'minimum':
            if f_x2 > f_x1:
                xl = x2
            else:
                xu = x1
        elif direction == 'maximum':
            if f_x2 > f_x1:
                xu = x1
            else:
                xl = x2
        else:
            raise ValueError("Invalid direction. Choose either 'minimum' or 'maximum'.")
            
    return xl, f_xl, xu, f_xu, x1, f_x1, x2, f_x2, d

# Function to reset the page
def reset_page():
    # Clear input fields
    XLowerEntry.delete(0, END)
    XUpperEntry.delete(0, END)
    entry.delete(0, END)
    
    # Clear treeview table
    for child in iter.get_children():
        iter.delete(child)
    
    # Reset result label
    ResultRoot.config(text="")

# Function to go back to the previous menu
def back_to_menu():
    Window.destroy()
    import Mainpage  # Assuming this is the previous menu

# Function to set quick test values
def set_quick_test_values():
    reset_page()
    XLowerEntry.insert(0, '0')
    XUpperEntry.insert(0, '4')
    entry.insert(0, '2*sin(x)-((x**2)/10)')

# GUI setup
Frame1 = Frame(Window, bg='#34495E', width='1000', height='50')
Frame1.pack(side=TOP, fill=X)

LabelTitle = Label(Frame1, text='Golden Section Method', bg='#34495E', fg='#FF5733', font=("Helvetica", 16, 'bold'))
LabelTitle.pack(pady='5')

XlowerLAbel = Label(Window, text=' X lower', bg='#34495E', fg='#FF5733', font=f)
XlowerLAbel.place(x=50, y=100)
XLowerEntry = Entry(Window, borderwidth=2, width='30', font=f)
XLowerEntry.place(x=150, y=100)

XUpperLAbel = Label(Window, text=' X Upper', bg='#34495E', fg='#FF5733', font=f)
XUpperLAbel.place(x=50, y=150)
XUpperEntry = Entry(Window, borderwidth=2, width='30', font=f)
XUpperEntry.place(x=150, y=150)

f = Label(Window, text="f(x)", bg='#34495E', fg='#FF5733', font=f)
f.place(x=50, y=200)
entry = Entry(Window, borderwidth=2, width='30', font=f)
entry.place(x=150, y=200)

# Radio buttons for optimization direction
var = StringVar()
var.set('minimum')  # Default selection
min_radio = Radiobutton(Window, text="Minimum", variable=var, value='minimum', bg='#34495E',fg="#FF5733", font=f)
min_radio.place(x=145, y=230)
max_radio = Radiobutton(Window, text="Maximum", variable=var, value='maximum', bg='#34495E',fg="#FF5733", font=f)
max_radio.place(x=250, y=230)

iter = ttk.Treeview(Window, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), show='headings', height=9)
iter.place(x=50, y=280, width=1000)
iter.column("1", anchor=CENTER, stretch=NO, width=100)
iter.heading(1, text='i')
iter.column("2", anchor=CENTER, stretch=NO, width=100)
iter.heading(2, text='Xl')
iter.column("3", anchor=CENTER, stretch=NO, width=100)
iter.heading(3, text='f(Xl)')
iter.column("4", anchor=CENTER, stretch=NO, width=100)
iter.heading(4, text='Xu')
iter.column("5", anchor=CENTER, stretch=NO, width=100)
iter.heading(5, text='f(Xu)')
iter.column("6", anchor=CENTER, stretch=NO, width=100)
iter.heading(6, text='X1')
iter.column("7", anchor=CENTER, stretch=NO, width=100)
iter.heading(7, text='f(x1)')
iter.column("8", anchor=CENTER, stretch=NO, width=100)
iter.heading(8, text='X2')
iter.column("9", anchor=CENTER, stretch=NO, width=100)
iter.heading(9, text='f(x2)')
iter.column("10", anchor=CENTER, stretch=NO, width=100)
iter.heading(10, text='d')

ButtonRes = Button(Window, text='Determine Root', bg='#34495E', fg='#FF5733', font=f, command=golden_section_search)
ButtonRes.place(x=50, y=550)

ResultRoot = Label(Window, text="", bg='#34495E', fg='#FF5733', font=("Helvetica", 9, 'bold'))
ResultRoot.place(x=200, y=500)

ButtonReset = Button(Window, text='Reset', bg='#34495E', fg='#FF5733', font=f, command=reset_page)
ButtonReset.place(x=300, y=550)

ButtonBack = Button(Window, text='Back', bg='#34495E', fg='#FF5733', font=f, command=back_to_menu)
ButtonBack.place(x=450, y=550)

# Quick Test Button
quick_test_button = Button(Window, text='Quick Test', bg='#34495E', fg='#FF5733', font=f, command=set_quick_test_values)
quick_test_button.place(x=550, y=550)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", foreground='#FF5733', background='#34495E', font=("Helvetica", 9, 'bold'))
style.configure('Treeview.Heading', background="#34495E", foreground='#FF5733', font=("Helvetica", 9, 'bold'))
style.map("Treeview", background=[('selected', '#34495E')])

# Call the function to center the window
center_window(Window, 1000, 700)

# Start the GUI event loop
Window.mainloop()
