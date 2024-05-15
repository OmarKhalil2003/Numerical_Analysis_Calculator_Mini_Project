from tkinter import *  # Importing the tkinter module for GUI
from math import *  # Importing math module for mathematical functions

# Function to reset all entry fields
def reset_page():
    for row in rows:
        for col in row:
            col.delete(0, 'end')  # Delete the content of each entry field

# Function to destroy the window and return to the main menu
def go_back():
    window.destroy()  # Destroy the current window
    import Mainpage  # Importing the main menu (assuming it's in a file named Mainpage)

window = Tk()  # Create the main window
window.config(bg='#34495E')  # Set background color
window.geometry('1100x750')  # Set window dimensions

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

window.config(bg='#34495E')  # Background color changed

f = ("Helvetica", 9, 'bold')  # Define font

window.title("Gauss-Jordan Elimination")  # Set window title

# Function to get matrix values from the entry fields
def getmatrix():
    matrix = []  # Initialize an empty list to store the matrix values
    for row in rows:  # Iterate over each row in the entry field grid
        a = []  # Initialize an empty list to store values for the current row
        for col in row:  # Iterate over each column in the current row
            m = col.get()  # Get the content of the current entry field
            a.append(float(m))  # Convert the content to float and append it to the current row list
        matrix.append(a)  # Append the current row list to the matrix list
    return matrix  # Return the matrix containing all the values from the entry fields


# Create entry fields for the matrix
rows = []  # Initialize an empty list to store rows of entry fields
for i in range(3):  # Iterate over each row
    cols = []  # Initialize an empty list to store entry fields in the current row
    for j in range(4):  # Iterate over each column in the current row
        e = Entry(window, width=10, bd=5, justify=CENTER)  # Create an entry field widget
        e.grid(row=i, column=j, padx='10', pady='10')  # Place the entry field in the grid with padding
        cols.append(e)  # Append the entry field to the current row list
    rows.append(cols)  # Append the current row list to the rows list


# Function to perform Gauss-Jordan Elimination
def Get_GJ():
    r = getmatrix()  # Get the matrix values from the entry fields
    n = len(r)  # Get the size of the matrix

    Steps.delete(1.0, END)  # Clear previous steps

    for i in range(n):
        # Partial pivoting
        max_row = max(range(i, n), key=lambda k: abs(r[k][i]))  # Find the row with the maximum absolute value in the current column
        r[i], r[max_row] = r[max_row], r[i]  # Swap the current row with the row having the maximum absolute value

        pivot = r[i][i]  # Select the pivot element from the diagonal

        # Divide the row by the pivot to make it 1
        for j in range(i, n + 1):
            r[i][j] /= pivot

        # Subtract this row from all other rows to make the corresponding elements 0
        for k in range(n):
            if k != i:
                factor = r[k][i]  # Get the factor to eliminate the element in the current column
                for j in range(i, n + 1):
                    r[k][j] -= factor * r[i][j]  # Perform row operations

        # Display step
        Steps.insert(END, f"Step {i + 1}:\n")
        for row in r:
            Steps.insert(END, row)  # Insert the row into the Steps widget
            Steps.insert(END, "\n")  # Insert a newline after each row
        Steps.insert(END, "\n")  # Insert an additional newline after each step

    # Extract solution
    sol = [row[-1] for row in r]  # Extract the solution from the last column of the matrix
    Result['text'] = f"After Solving The System, (X1, X2, X3): {tuple(sol[:3])}"  # Display the solution in the Result widget

# Create buttons and labels
ButtonGetX = Button(window, text="Solve System", bg='#34495E', fg='#E74C3C', command=Get_GJ)
ButtonGetX.grid(padx='5', pady='5')

ButtonReset = Button(window, text="Reset", bg='#34495E', fg='#E74C3C', command=reset_page)
ButtonReset.grid(padx='5', pady='5')

ButtonBack = Button(window, text="Back", bg='#34495E', fg='#E74C3C', command=go_back)
ButtonBack.grid(padx='5', pady='5')

Result = Label(window, text="   ", fg='#E74C3C', bg='#34495E')
Result.grid(row=10, column=2, padx=20, pady=20)

Steps = Text(window, height=25, width=100, bg='white')
Steps.grid(row=11, column=2)

# Function to fill entry fields with quick test values
def set_quick_test_values():
    reset_page()
    quick_test_values = [
        [4, 1, -1, -2],
        [5, 1, 2, 4],
        [6, 1, 1, 6]
    ]
    for i in range(3):
        for j in range(4):
            rows[i][j].insert(0, str(quick_test_values[i][j]))

# Quick Test Button
quick_test_button = Button(window, text='Quick Test', bg='#34495E', fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=set_quick_test_values)
quick_test_button.grid(row=4, columnspan=4, padx=10, pady=5)

# Center the window and start the main loop
center_window(window, 900, 600)
window.mainloop()
