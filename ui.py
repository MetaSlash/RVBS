import tkinter as tk
from tkinter import ttk

def add_row():
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
    remove_button = tk.Button(row_frame, text="remove", command=lambda idx=len(rows): remove_row(idx))
    remove_button.pack(side=tk.LEFT, padx=5)

    # Store the row elements for potential removal
    rows.append((row_frame, id_entry, quantity_entry, remove_button))

    # Update the scroll region
    canvas.configure(scrollregion=canvas.bbox("all"))

def remove_row(row_index):
    # Remove the specified row
    row_frame, id_entry, quantity_entry, remove_button = rows[row_index]
    row_frame.destroy()
    rows.pop(row_index)
    # Update the scroll region
    canvas.configure(scrollregion=canvas.bbox("all"))

# Initialize the main window
window = tk.Tk()
window.geometry("455x341")
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
add_button.pack(pady=10)

# Run the application
window.mainloop()
