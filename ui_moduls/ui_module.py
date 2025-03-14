from libs import *
from core import stock_rest_calc

def add_row(scrollable_frame, rows, canvas):
    """
    Add a new row to the scrollable frame, including entries for 'id wanted' and 'quantity',
    and a Button to remove the row.
    """
    row_frame = Frame(scrollable_frame, bg="white")
    row_frame.pack(fill="x")

    id_label = Label(row_frame, text="id wanted")
    id_label.pack(side="left", padx=5)
    id_entry = Entry(row_frame, width=11)
    id_entry.pack(side="left", padx=5)

    quantity_label = Label(row_frame, text="quantity")
    quantity_label.pack(side="left", padx=5)
    quantity_entry = Entry(row_frame, width=11)
    quantity_entry.pack(side="left", padx=5)

    remove_button = Button(row_frame, text="remove", command=lambda row=row_frame: remove_row(row, rows, canvas))
    remove_button.pack(side="left", padx=5)

    rows.append((row_frame, id_entry, quantity_entry, remove_button))
    canvas.configure(scrollregion=canvas.bbox("all"))

def remove_row(row_frame, rows, canvas):
    """
    Remove the specified row from the list of rows and update the scroll region of the canvas.
    """
    for row in rows:
        if row[0] == row_frame:
            row[0].destroy()
            rows.remove(row)
            break
    canvas.configure(scrollregion=canvas.bbox("all"))

def debit_prep_button_command(connection_cred, rows):
    """
    Reads the values from the table and calls debit_prep with the read values.
    
    :param connection_cred: A dictionary containing database connection credentials 
                            with keys 'host', 'user', 'password', and 'database'.
    """
    # Create a dictionary to store the values
    values = {"id" : [],
              "quantity" : []}
    message = ""
    
    # Iterate over the rows
    for row in rows:
        _, id_entry, quantity_entry, _ = row
        
        # Read the values from the entries
        id_list = values["id"]
        quantity_list = values["quantity"]
        
        # Add the values to the lists
        id_list.append(int(id_entry.get())) 
        quantity_list.append(int(quantity_entry.get())) 
    
    debit = stock_rest_calc(connection_cred, values)["machine readable"]
    message = stock_rest_calc(connection_cred, values)["human readable"]

    

    show_popup(message)
    # Print the result of debit_prep
    print(debit)


def show_popup(message):
    """
    Creates a Toplevel window with a label and a Button to show a given message.
    """
    popup = Toplevel()
    popup.title("Popup Window")

    content_frame = Frame(popup)
    content_frame.pack(expand=True, fill="both", padx=10, pady=10)

    label = Label(content_frame, text=message, justify="left")
    label.pack(anchor="w")

    close_button = Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10, side="bottom")
