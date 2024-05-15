from tkinter import *
from math import *

# Function to reset all entry fields
def reset_page():
    for row in rows:
        for col in row:
            col.delete(0, 'end')

# Function to go back to the main page
def go_back():
    window.destroy()
    import Mainpage

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

# Function to retrieve matrix entries from entry fields
def get_matrix():
    matrix = []  # Initialize an empty list to store the matrix
    for row in rows:  # Iterate through each row in the entry fields
        row_values = []  # Initialize an empty list to store the values of the current row
        for col in row:  # Iterate through each column in the current row
            m = col.get()  # Get the value entered in the current entry field
            row_values.append(float(m))  # Convert the value to float and add it to the row_values list
        matrix.append(row_values)  # Add the row_values list to the matrix list
    return matrix  # Return the resulting matrix containing all the entries


# Create the main window
window = Tk()
window.config(bg='#34495E')
window.geometry('1100x750')
center_window(window, 1100, 750)
window.title("LU Decomposition")

# Font style
f = ("Helvetica", 9, 'bold')

# Entry fields for matrix entries
rows = []  # Initialize an empty list to store the rows of entry fields
for i in range(3):  # Iterate over the rows
    cols = []  # Initialize an empty list to store the entry fields in the current row
    for j in range(4):  # Iterate over the columns
        e = Entry(window, width=10, bd=5, justify=CENTER)  # Create an Entry widget
        e.grid(row=i, column=j, padx='10', pady='10')  # Place the Entry widget in the window
        cols.append(e)  # Append the Entry widget to the current row list
    rows.append(cols)  # Append the current row list to the rows list


# Checkbox for partial pivoting
partial_pivoting_var = IntVar()
partial_pivoting_checkbox = Checkbutton(window, text="Partial Pivoting", variable=partial_pivoting_var, bg='#34495E', fg='#E74C3C')
partial_pivoting_checkbox.grid(row=3, columnspan=4, padx=10, pady=5)

# Function to perform LU decomposition and solve the system
def Get_GE():
    r = get_matrix()  # Retrieve the matrix from the entry fields
    b = [row[3] for row in r]  # Extract the vector b from the matrix
    n = len(r)  # Get the size of the matrix
    L = [[0] * n for _ in range(n)]  # Initialize the lower triangular matrix L
    U = [[0] * n for _ in range(n)]  # Initialize the upper triangular matrix U

    for i in range(n):
        L[i][i] = 1  # Set the diagonal elements of L to 1

    for j in range(n):
        if partial_pivoting_var.get() == 1:
            # Partial pivoting
            max_row = max(range(j, n), key=lambda i: abs(r[i][j]))  # Find the row with the maximum absolute value in the current column
            r[j], r[max_row] = r[max_row], r[j]  # Swap the rows to perform partial pivoting
            
        for i in range(j, n):
            U[j][i] = r[j][i] - sum(L[j][k] * U[k][i] for k in range(j))  # Calculate the elements of U
            
        for i in range(j+1, n):
            L[i][j] = (r[i][j] - sum(L[i][k] * U[k][j] for k in range(j))) / U[j][j]  # Calculate the elements of L

    # Solve Lc = b
    c = [0] * n
    for i in range(n):
        c[i] = b[i] - sum(L[i][k] * c[k] for k in range(i))

    # Solve Ux = c
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = (c[i] - sum(U[i][k] * x[k] for k in range(i+1, n))) / U[i][i]

    # Display the result and LU matrices
    Result['text'] = f"After Solving The System ,(X1,X2,X3): {tuple(x)}"  # Display the solution
    Steps.insert(END, "L Matrix\n")  # Display the L matrix
    for row in L:
        Steps.insert(END, row)
        Steps.insert(END, "\n")
    Steps.insert(END, "\n")
    Steps.insert(END, "U Matrix\n")  # Display the U matrix
    for row in U:
        Steps.insert(END, row)
        Steps.insert(END, "\n")
    Steps.insert(END, "\n")

# Button to solve the system
ButtonGetX = Button(window, text="Solve System", bg='#34495E', fg='#E74C3C', command=Get_GE)
ButtonGetX.grid(padx='5', pady='5')

# Button to reset all entry fields
ButtonReset = Button(window, text="Reset", bg='#34495E', fg='#E74C3C', command=reset_page)
ButtonReset.grid(padx='5', pady='5')

# Button to go back to the main page
ButtonBack = Button(window, text="Back", bg='#34495E', fg='#E74C3C', command=go_back)
ButtonBack.grid(padx='5', pady='5')

# Label to display result
Result = Label(window, text="   ", fg='#E74C3C', bg='#34495E')
Result.grid(row=10, column=2, padx=10, pady=10)

# Text widget to display LU matrices
Steps = Text(window, height=25, width=100, bg='white')
Steps.grid(row=11, column=2, padx=10, pady=10)

# Quick test button to populate the entry fields with sample values
def set_quick_test_values():
    reset_page()
    quick_test_values = [
        [2, 1, -1, 1],
        [5, 2, 2, -4],
        [3, 1, 1, 5]
    ]
    for i in range(3):
        for j in range(4):
            rows[i][j].insert(0, str(quick_test_values[i][j]))

quick_test_button = Button(window, text='Quick Test', bg='#34495E', fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=set_quick_test_values)
quick_test_button.grid(row=4, columnspan=4, padx=10, pady=5)

# Start the main loop
window.mainloop()
