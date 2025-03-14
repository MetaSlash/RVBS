from core import add_row, debit_prep_button_command
from libs import *


def ui(connection_cred):
    # Initialize the main window
    window = Tk()
    window.geometry("455x320")
    window.title("Debit de prep")

    # List to keep track of rows
    rows = []

    # Create a frame to contain the canvas and scrollbar
    frame = Frame(window)
    frame.pack(fill="both", expand=True)

    # Create a canvas object and a vertical scrollbar for scrolling it
    canvas = Canvas(frame, bg="white")
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
    add_row(scrollable_frame, rows, canvas)

    # Create and place the "ADD more 1 row" button at the bottom
    add_button = Button(window, text="Ajouter une ligne", command=lambda: add_row(scrollable_frame, rows, canvas))
    add_button.pack(pady=10, side="left")

    debit_prep_button = Button(window, text="Faire le débit", command=lambda: debit_prep_button_command(connection_cred, rows))
    debit_prep_button.pack(pady=10, side="right")

    # Run the application
    window.mainloop()


if __name__ == "__main__":

    connection_cred = {
        "host": "192.168.0.22",
        "user": "User",
        "password": "1214",
        "database": "mydb"
    }

    ui(connection_cred)
