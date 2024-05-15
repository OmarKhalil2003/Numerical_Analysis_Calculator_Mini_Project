from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

# Function to switch to the next page based on the selected method
def nextPage(selected_method):
    if selected_method == "Select your method":
        messagebox.showerror("Error", "Please select a method.")
    else:
        Window.destroy()  # Close the current window
        # Import the corresponding module based on the selected method
        if selected_method == "Bisection Method":
            import BisectionMethod
        elif selected_method == "False Position Method":
            import FalsePs
        elif selected_method == "Secant Method":
            import SecantMethod
        elif selected_method == "Simple Fixed Point":
            import SimpleFixedPoint
        elif selected_method == "Newton Method":
            import Newton
        elif selected_method == "Gauss Elimination":
            import GaussElimination
        elif selected_method == "LU Decomposition":
            import LuDecomposition
        elif selected_method == "Cramer Rule":
            import Cramer
        elif selected_method == "Golden Section":
            import GoldenSection
        elif selected_method == "Gradiant":
            import Gradiant
        elif selected_method == "Gauss Jordan":
            import GaussJordan

# Setup Window
Window = Tk()  # Create the main window
Window.title("Numerical Analysis Calculator")  # Set the title of the window
Window.geometry('1100x750')

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

f = ("Helvetica", 16, 'bold')

  # Set the size of the window
Window.resizable(0, 0)  # Disable window resizing


# Fonts
title_font = Font(family="Helvetica", size=20, weight="bold")  # Title font settings
button_font = Font(family="Helvetica", size=12, weight="bold")  # Button font settings

# Main Frame
main_frame = Frame(Window, bg='#34495E')  # Create the main frame
main_frame.pack(expand=True, fill=BOTH)  # Expand and fill the main frame

# Title Label
Label(main_frame, text='Numerical Analysis Calculator', fg='#E74C3C', bg='#34495E', font=title_font).pack(pady='20')  # Title label

# Menu Bar
menubar = Menu(Window)  # Create the menu bar
filemenu = Menu(menubar, tearoff=0)  # Create the file menu
filemenu.add_separator()  # Add a separator
menubar.add_cascade(label="File", menu=filemenu)  # Add file menu to the menu bar
Window.config(menu=menubar)  # Configure the menu bar

# Choose Method Frame
choose_method_frame = Frame(main_frame, bg='#34495E')  # Create the frame to choose a method
choose_method_frame.pack(pady=(20, 0))  # Pack the frame with padding

LabelChoose = Label(choose_method_frame, text='Choose a Method:', fg='#E74C3C', bg='#34495E', font=('Arial', 14, 'bold'))  # Label to prompt user to choose a method
LabelChoose.grid(row=0, column=0, padx=10, pady=10)  # Grid layout for the label

methods = [ "Bisection Method", "False Position Method", "Secant Method", "Simple Fixed Point", "Newton Method", "Gauss Elimination", "LU Decomposition", "Cramer Rule", "Golden Section", "Gradiant", "Gauss Jordan"]  # List of available methods
method_var = StringVar(Window)  # Variable to store the selected method
method_var.set(methods[0])  # Set the default option

method_menu = OptionMenu(choose_method_frame, method_var, *methods)  # Option menu for selecting the method
method_menu.config(bg='#34495E', fg='#E74C3C', font=f)  # Configure option menu settings
method_menu.grid(row=0, column=1, padx=10, pady= 0)  # Grid layout for the option menu

ButtonSelect = Button(main_frame, text='Select Method', bg='#34495E', fg='#E74C3C', font=f, command=lambda: nextPage(method_var.get()))  # Button to select the method
ButtonSelect.pack(pady=(100, 10))  # Pack the button with padding


Window.mainloop()  # Start the main event loop
