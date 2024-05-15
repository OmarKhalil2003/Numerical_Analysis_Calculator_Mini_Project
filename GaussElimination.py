# Import necessary modules from tkinter and math libraries
from tkinter import *
from math import *

# Function to reset all entry fields
def reset_page():
    for row in entries:
        for entry in row:
            entry.delete(0, 'end')

# Function to go back to the main page
def go_back():
    window.destroy()  # Close the current window
    import Mainpage  # Import and go back to the main page

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()  # Get screen width
    screen_height = window.winfo_screenheight()  # Get screen height
    x = (screen_width - width) // 2  # Calculate x coordinate for centering
    y = (screen_height - height) // 2  # Calculate y coordinate for centering
    window.geometry(f'{width}x{height}+{x}+{y}')  # Set window geometry to center it

# Function to retrieve matrix entries from entry fields
def get_matrix():
    matrix = []
    for row in entries:
        row_values = []
        for entry in row:
            value = entry.get()  # Get value from the entry field
            row_values.append(float(value))  # Convert the value to float and add it to the row
        matrix.append(row_values)  # Add the row to the matrix
    return matrix

# Function for partial pivoting
def partial_pivoting(matrix):
    for j in range(3):
        max_row = max(range(j, 3), key=lambda i: abs(matrix[i][j]))  # Find the row with the maximum absolute value in the current column
        matrix[j], matrix[max_row] = matrix[max_row], matrix[j]  # Swap the current row with the row with maximum absolute value
    return matrix

# Function for Gaussian elimination
def gaussian_elimination(matrix):
    for j in range(3):
        for i in range(j + 1, 3):
            factor = matrix[i][j] / matrix[j][j]  # Calculate the factor by which to multiply the current row
            for k in range(j, 4):
                matrix[i][k] -= factor * matrix[j][k]  # Subtract the product of factor and the corresponding element in the current row
    return matrix

# Function for backward substitution
def backward_substitution(matrix):
    x = [0] * 3  # Initialize the solution vector
    for i in range(2, -1, -1):  # Iterate over the rows in reverse order
        x[i] = matrix[i][3]  # Set the initial value of the solution
        for j in range(i + 1, 3):  # Iterate over the elements in the row
            x[i] -= matrix[i][j] * x[j]  # Subtract the product of the corresponding element in the row and the solution value
        x[i] /= matrix[i][i]  # Divide by the diagonal element to get the final solution value
    return x

# Function to solve the system of equations
def solve_system():
    try:
        matrix = get_matrix()  # Get the matrix of entries from the entry fields
        if partial_pivoting_var.get() == 1:  # Check if partial pivoting is enabled
            matrix = partial_pivoting(matrix)  # Perform partial pivoting
        matrix = gaussian_elimination(matrix)  # Perform Gaussian elimination
        solution = backward_substitution(matrix)  # Perform backward substitution to find the solution
        result_label['text'] = f"Solutions (X1, X2, X3): {tuple(solution)}"  # Display the solution
        steps_text.insert(END, "Matrix:\n")  # Display the matrix in the text widget
        for row in matrix:
            steps_text.insert(END, row)
            steps_text.insert(END, "\n")
        steps_text.insert(END, "\n")
    except Exception as e:
        result_label['text'] = f"Error: {str(e)}"  # Display error message if an exception occurs

# Create the main window
window = Tk()
window.config(bg='#34495E')  # Set background color
window.geometry('1100x750')  # Set window size
center_window(window, 1100, 750)  # Center the window on the screen
window.title("Gauss Elimination")  # Set window title

# Font style
f = ("Helvetica", 9, 'bold')

# Checkbutton for partial pivoting
partial_pivoting_var = IntVar()
partial_pivoting_checkbox = Checkbutton(window, text="Partial Pivoting", variable=partial_pivoting_var, bg='#34495E', fg='#E74C3C')
partial_pivoting_checkbox.grid(row=3, columnspan=4, padx=10, pady=5)

# Entry fields for matrix entries
entries = []
for i in range(3):
    row_entries = []
    for j in range(4):
        entry = Entry(window, width=10, bd=5, justify=CENTER)  # Create entry field
        entry.grid(row=i, column=j, padx='10', pady='10')  # Place entry field in the grid
        row_entries.append(entry)  # Add entry field to row
    entries.append(row_entries)  # Add row to entries list

# Button to solve the system
solve_button = Button(window, text="Solve System", bg='#34495E', fg='#E74C3C', command=solve_system)
solve_button.grid(padx='5', pady='5')

# Button to reset all entry fields
reset_button = Button(window, text="Reset", bg='#34495E', fg='#E74C3C', command=reset_page)
reset_button.grid(padx='5', pady='5')

# Button to go back to the main page
back_button = Button(window, text="Back", bg='#34495E', fg='#E74C3C', command=go_back)
back_button.grid(padx='5', pady='5')

# Label to display result
result_label = Label(window, text="   ", fg='#E74C3C', bg='#34495E')
result_label.grid(row=10, column=2, padx=20, pady=20)

# Text widget to display solution steps
steps_text = Text(window, height=25, width=100, bg='white')
steps_text.grid(row=11, column=2)

# Quick test button to populate the entry fields with sample values
def set_quick_test_values():
    reset_page()  # Reset all entry fields
    quick_test_values = [  # Define sample matrix values
        [2, 1, -1, 1],
        [5, 2, 2, -4],
        [3, 1, 1, 5]
    ]
    for i in range(3):
        for j in range(4):
            entries[i][j].insert(0, str(quick_test_values[i][j]))  # Insert sample values into entry fields

quick_test_button = Button(window, text='Quick Test', bg='#34495E', fg='#E74C3C', font=('Helvetica', 11, 'bold'), command=set_quick_test_values)
quick_test_button.grid(row=4, columnspan=4, padx=10, pady=5)

# Start the main loop
window.mainloop()
