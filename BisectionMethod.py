from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import *

# Create the main window
Window = Tk()
Window.geometry('1100x750')
Window.title("Bisection Method")

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


Window.config(bg='#34495E')  # Background color changed

f = ("Helvetica", 9, 'bold')


# Function to get the lower bound input value
def get_XLower():
    return float(XLowerEntry.get())

# Function to get the upper bound input value
def get_Xupper():
    return float(XUpperEntry.get())

# Function to get the epsilon input value
def get_Epson():
    return float(EpsEntry.get())

# Function to get the mathematical function input value
def get_Function(x):
    try:
        result = eval(entry.get(), {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan, "x": x})
        return result
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during expression evaluation: {e}")
    try:
        result = eval(entry.get(), {"__builtins__": None}, {"sin": sin, "cos": cos, "tan": tan})
        return result
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during expression evaluation: {e}")

# Function to perform the bisection method
def bisect():
    xl = get_XLower()  # Get lower bound
    xu = get_Xupper()  # Get upper bound
    ep = get_Epson()   # Get epsilon

    xr = 0.0  # Initialize root
    xrold = 0.0  # Initialize previous root
    Err0r = 0.0  # Initialize error
    i = 0  # Initialize iteration counter
    
    # Clear treeview table before inserting new values
    for child in iter.get_children():
        iter.delete(child)
    
    while True:
        xrold = xr  # Store previous root
        xr = (xl + xu) / 2  # Calculate new root
        
        # Get function values at boundaries and root
        FXL = get_Function(xl)
        FXU = get_Function(xu)
        FXLI = float(FXL)
        FXUI = float(FXU)
        
        PolyCheck = FXLI * FXUI
        if PolyCheck >= 0:  # Check for no solution
            messagebox.showwarning("Warning!!", "Has No Solution")
            exit()
        
        FXR = get_Function(xr)
        FXRI = float(FXR)
        Err0r = abs((xr - xrold) / xr) * 100  # Calculate error
        
        # Insert values into the treeview
        if i == 0:
            iter.insert(parent='', index='end', iid=i, text='', values=(i, xl, FXLI, xu, FXUI, xr, FXRI, ""))
        else:
            iter.insert(parent='', index='end', iid=i, text='', values=(i, xl, FXLI, xu, FXUI, xr, FXRI, Err0r))
        
        sign_check = FXLI * FXRI
        if sign_check > 0:
            xl = xr
        elif sign_check < 0:
            xu = xr
        else:
            ResultRoot['text'] = f"The Root is :{xr} "
            return xr
            break

        i += 1

        if Err0r <= ep:
            break
    
    ResultRoot['text'] = f"The Root is :{xr} "

    return xr

# Function to reset the page
def reset_page():
    # Clear input fields
    XLowerEntry.delete(0, END)
    XUpperEntry.delete(0, END)
    EpsEntry.delete(0, END)
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

# Function to populate the entry fields with predefined values for quick testing
def quick_test():
    XLowerEntry.delete(0, END)
    XUpperEntry.delete(0, END)
    EpsEntry.delete(0, END)
    entry.delete(0, END)
    
    # Predefined values for quick testing
    XLowerEntry.insert(0, "0")
    XUpperEntry.insert(0, "1")
    EpsEntry.insert(0, "10")
    entry.insert(0, "-2+7*x-5*x**2+6*x**3")

# GUI setup
Frame1 = Frame(Window, bg='#34495E', width='1000', height='50')
Frame1.pack(side=TOP, fill=X)

LabelTitle = Label(Frame1, text='Bisection Method', bg='#34495E', fg='#FF5733', font=("Helvetica", 16, 'bold'))
LabelTitle.pack(pady='5')

XlowerLAbel = Label(Window, text=' X lower', bg='#34495E', fg='#FF5733', font=f)
XlowerLAbel.place(x=50, y=100)
XLowerEntry = Entry(Window, borderwidth=2, width='30', font=f)
XLowerEntry.place(x=150, y=100)

XUpperLAbel = Label(Window, text=' X Upper', bg='#34495E', fg='#FF5733', font=f)
XUpperLAbel.place(x=50, y=150)
XUpperEntry = Entry(Window, borderwidth=2, width='30', font=f)
XUpperEntry.place(x=150, y=150)

EPSL = Label(Window, text=' Epsilon', bg='#34495E', fg='#FF5733', font=f)
EPSL.place(x=50, y=200)
EpsEntry = Entry(Window, borderwidth=2, width='30', font=f)
EpsEntry.place(x=150, y=200)

f = Label(Window, text="f(x)", bg='#34495E', fg='#FF5733', font=f)
f.place(x=50, y=250)
entry = Entry(Window, borderwidth=2, width='30', font=f)
entry.place(x=150, y=250)

iter = ttk.Treeview(Window, columns=(1, 2, 3, 4, 5, 6, 7, 8), show='headings', height=9)
iter.place(x=50, y=300, width=900)
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
iter.heading(6, text='Xr')
iter.column("7", anchor=CENTER, stretch=NO, width=100)
iter.heading(7, text='f(Xr)')
iter.column("8", anchor=CENTER, stretch=NO, width=100)
iter.heading(8, text='Error%')

ButtonRes = Button(Window, text='Determine Root', bg='#34495E', fg='#FF5733', font=f, command=bisect)
ButtonRes.place(x=50, y=650)

ResultRoot = Label(Window, text="", bg='#34495E', fg='#FF5733', font=f)
ResultRoot.place(x=200, y=550)

ButtonReset = Button(Window, text='Reset', bg='#34495E', fg='#FF5733', font=f, command=reset_page)
ButtonReset.place(x=300, y=650)

ButtonBack = Button(Window, text='Back', bg='#34495E', fg='#FF5733', font=f, command=back_to_menu)
ButtonBack.place(x=450, y=650)

ButtonQuickTest = Button(Window, text='Quick Test', bg='#34495E', fg='#FF5733', font=f, command=quick_test)
ButtonQuickTest.place(x=600, y=650)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview", foreground='#FF5733', background='#34495E', font=f)
style.configure('Treeview.Heading', background="#34495E", foreground='#FF5733', font=f)
style.map("Treeview", background=[('selected', '#34495E')])

# Call the function to center the window
center_window(Window, 1000, 700)

# Start the GUI event loop
Window.mainloop()
