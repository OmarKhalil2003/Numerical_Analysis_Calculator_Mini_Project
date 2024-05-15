# Import necessary libraries
from tkinter import *
import numpy as np

# Create the main window
window = Tk()
window.config(bg='#34495E')

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f'{width}x{height}+{x}+{y}')

# Set window properties
window.title("Cramer's Rule")
f = ("Helvetica", 9, 'bold')

# Function to retrieve matrix entries from entry fields
def get_matrix():
    matrix = []  # Initialize an empty matrix to store the entries
    for row in rows:  # Iterate over each row of entry fields
        a = []  # Initialize an empty list to store the values of the current row
        for col in row:  # Iterate over each column (entry field) in the row
            m = col.get()  # Get the value entered in the entry field
            a.append(int(m))  # Convert the value to an integer and append it to the row list
        matrix.append(a)  # Append the row list to the matrix
    return matrix  # Return the constructed matrix


# Function to reset all entry fields and text widget
def reset():
    for row in rows:
        for col in row:
            col.delete(0, END)
    Steps.delete('1.0', END)
    Result['text'] = "   "

# Function to go back to the main page
def back_to_main():
    window.destroy()
    import Mainpage

# Create entry fields
rows = []  # Initialize an empty list to store the rows of entry fields
for i in range(3):  # Iterate over each row
    cols = []  # Initialize an empty list to store the entry fields in the current row
    for j in range(4):  # Iterate over each column in the current row
        # Create an Entry widget and place it in the window grid
        e = Entry(window, width=10, bd=5, justify=CENTER)
        e.grid(row=i, column=j, padx=5, pady=5)
        cols.append(e)  # Append the Entry widget to the list of columns
    rows.append(cols)  # Append the list of columns to the list of rows


# Function to perform Cramer's Rule and solve the system
def get_GE():
    # Get the coefficient matrix and constant vector
    r = get_matrix()
    b1, b2, b3 = r[0][3], r[1][3], r[2][3]
    B = np.array([b1, b2, b3])
    
    # Initialize lists to store the augmented matrices
    a = []
    for i in range(3):
        k = []
        for j in range(3):
            k.append(r[i][j])
        a.append(k)
    
    # Convert lists to numpy arrays
    A = np.array(a)
    
    # Calculate the determinant of the coefficient matrix
    D = int(np.linalg.det(A))
    
    # Display the determinant of the coefficient matrix
    Steps.insert(END, "det(D):")
    Steps.insert(END, D)
    Steps.insert(END, "\n", "\n", "\n", "\n")
    
    # Iterate over each column of the coefficient matrix
    for i in range(3):
        # Create a copy of the coefficient matrix and replace the ith column with the constant vector
        A1 = np.array(a)
        A1[0:3, i] = B
        
        # Display the augmented matrix
        Steps.insert(END, f"A{i+1}: ")
        Steps.insert(END, A1)
        Steps.insert(END, "\n", "\n", "\n", "\n")
        
        # Calculate the determinant of the augmented matrix
        D1 = int(np.linalg.det(A1))
        
        # Display the determinant of the augmented matrix
        Steps.insert(END, f"det(D{i+1}): {D1}")
        Steps.insert(END, "\n", "\n", "\n", "\n")
        
        # Calculate the value of xi using Cramer's Rule
        xi = D1 / D
        
        # Display the value of xi
        Steps.insert(END, f"x{i+1} = D{i+1} / D = {xi}")
        Steps.insert(END, "\n", "\n", "\n", "\n")
    
    # Display the result after solving the system
    Result['text'] = f"After Solving The System, (X1, X2, X3) : {xi}"

# Buttons and labels
ButtonGetX = Button(window, text="Solve System", bg='#34495E', fg='#E74C3C', command=get_GE)
ButtonGetX.grid(padx='5', pady='5')

ResetButton = Button(window, text="Reset", bg='#34495E', fg='#E74C3C', command=reset)
ResetButton.grid(padx='5', pady='5')

BackButton = Button(window, text="Back", bg='#34495E', fg='#E74C3C', command=back_to_main)
BackButton.grid(padx='5', pady='5')

Result = Label(window, text="   ", fg='#E74C3C', bg='#34495E')
Result.grid(row=10, column=2, padx=5, pady=10)

Steps = Text(window, height=25, width=100, bg='white')
Steps.grid(row=11, column=2, padx=5, pady=10)

# Function to fill entry fields with quick test values
def set_quick_test_values():
    reset()
    quick_test_values = [
        [2, 1, -1, 1],
        [5, 2, 2, -4],
        [3, 1, 1, 5]
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
