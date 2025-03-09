from func_ui import *
from debit_prep import debit_prep, display
import tkinter as tk
from tkinter import ttk

def add_row():
    """
    Add a new row to the scrollable frame, including entries for 'id wanted' and 'quantity',
    and a button to remove the row.

    Each row consists of:
    - An 'id wanted' entry field.
    - A 'quantity' entry field.
    - A 'remove' button to delete the row.
    """
    # Create a frame for the new row inside the scrollable frame
    row_frame = tk.Frame(scrollable_frame, bg="white")
    row_frame.pack(fill="x")

    # Create and place the "id wanted" entry
    id_label = tk.Label(row_frame, text="id wanted")
    id_label.pack(side=tk.LEFT, padx=5)
    id_entry = tk.Entry(row_frame, width=11)
    id_entry.pack(side=tk.LEFT, padx=5)

    # Create and place the "quantity" entry
    quantity_label = tk.Label(row_frame, text="quantity")
    quantity_label.pack(side=tk.LEFT, padx=5)
    quantity_entry = tk.Entry(row_frame, width=11)
    quantity_entry.pack(side=tk.LEFT, padx=5)

    # Create and place the "remove" button with a command to remove the row
    remove_button = tk.Button(row_frame, text="remove", command=lambda row=row_frame: remove_row(row))
    remove_button.pack(side=tk.LEFT, padx=5)

    # Store the row elements for potential removal
    rows.append((row_frame, id_entry, quantity_entry, remove_button))

    # Update the scroll region to accommodate the new row
    canvas.configure(scrollregion=canvas.bbox("all"))


def remove_row(row_frame):
    """
    Remove the specified row from the list of rows and update the scroll region of the canvas.
    
    :param row_frame: The frame of the row to remove.
    """
    # Remove the specified row
    for row in rows:
        if row[0] == row_frame:
            row[0].destroy()
            rows.remove(row)
            break
    # Update the scroll region
    canvas.configure(scrollregion=canvas.bbox("all"))

def debit_prep_button_command(connection_cred):
    """
    Reads the values from the table and calls debit_prep with the read values.
    
    :param connection_cred: A dictionary containing database connection credentials 
                            with keys 'host', 'user', 'password', and 'database'.
    """
    # Create a dictionary to store the values
    values = {"id" : [],
              "quantity" : []}
    
    # Iterate over the rows
    for row in rows:
        _, id_entry, quantity_entry, _ = row
        
        # Read the values from the entries
        id_list = values["id"]
        quantity_list = values["quantity"]
        
        # Add the values to the lists
        id_list.append(int(id_entry.get())) 
        quantity_list.append(int(quantity_entry.get())) 
    
    # Print the result of debit_prep
    print(debit_prep(connection_cred, values))

    
connection_cred = {
"host":     "192.168.0.22",
"user":     "User",
"password": "1214",
"database": "mydb"
}


# Initialize the main window
window = tk.Tk()
window.geometry("455x320")
window.title("Dynamic Form with Scrollbar")

# List to keep track of rows
rows = []

# Create a frame to contain the canvas and scrollbar
frame = tk.Frame(window)
frame.pack(fill="both", expand=True)

# Create a canvas object and a vertical scrollbar for scrolling it
canvas = tk.Canvas(frame, bg="white")
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Pack everything
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create the initial row
add_row()

# Create and place the "ADD more 1 row" button at the bottom
add_button = tk.Button(window, text="ADD more 1 row", command=add_row)
add_button.pack(pady=10, side="left")

debit_prep_button = tk.Button(window, text="debit de prep" , command=lambda: debit_prep_button_command(connection_cred=connection_cred))
debit_prep_button.pack(pady=10, side="right")
# Run the application
window.mainloop()
