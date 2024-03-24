import pickle
import tkinter as tk
from tkinter import ttk

import Entities.Instructor
import Entities.Equipment
from functions.generalFunctions import sort_by_number, sort_by_name


def on_diver_select(event, table, session, divers_list):
    # Get the item that was double-clicked
    selected_item = table.focus()
    item = table.item(selected_item)
    item_values = item['values']
    diver_id = int(item_values[0])  # Assuming the ID is the first column

    # Find the diver by ID in divers_list
    selected_diver = next((diver for diver in divers_list if diver.ID == diver_id), None)

    if selected_diver:
        # Add the found diver to the session's divers array if not already added
        if selected_diver not in session.divers:
            session.divers.append(selected_diver)
            selected_diver.num_of_dives = selected_diver.num_of_dives + 1
            selected_diver.rank = selected_diver.check_rank()
            print(f"Diver with ID {diver_id} added to the session.")
        else:
            print(f"Diver with ID {diver_id} is already in the session.")


class DivingSession:
    # Static variable to keep track of the next ID for a new DivingSession instance
    static_id = 1

    def __init__(self, diving_depth, instructor: Entities.Instructor.Instructor, location):
        # Assign a unique ID to the new DivingSession instance
        self.id = DivingSession.static_id
        DivingSession.static_id += 1

        self.diving_depth = diving_depth
        self.instructor = instructor
        self.location = location
        self.divers = []  # List to store divers registered for this diving session
        # self.registered_equipment = []  # List to store equipment registered for this diving session

    def add_all_divers(self, divers_list):
        # main window initialization
        window_width = 1100  # width
        window_height = 500  # height
        btn_width = window_width * 0.2  # button width
        root_pax_left = (window_width - btn_width) // 2 - btn_width  #

        #
        root = tk.Tk()
        root.geometry(f'{window_width}x{window_height}')
        root.title("Dive system")  # Window's title

        # Main frame
        main_frame = tk.Frame(root, bg='gray')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Divers Page Frame
        divers_page_fm = tk.Frame(main_frame)

        # Divers Title Of The Page
        divers_page_lb = tk.Label(divers_page_fm, text="Divers Page",
                                  font=('Arial', 25), fg='#0097e8')
        divers_page_lb.pack(pady=20, padx=(root_pax_left, 0))

        # button frame
        button_frame = tk.Frame(divers_page_fm)
        button_frame.pack()

        # Create a table
        table = ttk.Treeview(divers_page_fm)
        table['columns'] = ('ID', 'Name', 'Age', 'Number Of Dives', 'Rank', 'Union')
        table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
        table.column('ID', anchor=tk.CENTER, width=100)
        table.column('Name', anchor=tk.CENTER, width=150)
        table.column('Age', anchor=tk.CENTER, width=100)
        table.column('Number Of Dives', anchor=tk.CENTER, width=100)
        table.column('Rank', anchor=tk.CENTER, width=100)
        table.column('Union', anchor=tk.CENTER, width=100)
        table.heading('#0', text='', anchor=tk.W)
        table.heading("ID", text="ID", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'ID', False))
        table.heading("Name", text="Name", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Name', False))
        table.heading("Age", text="Age", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'Rank', False))
        table.heading("Number Of Dives", text="Number Of Dives", anchor=tk.CENTER,
                      command=lambda: sort_by_number(table, 'Rank', False))
        table.heading("Rank", text="Rank", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'Rank', False))
        table.heading("Union", text="Union", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Rank', False))
        table.pack(pady=20, padx=(root_pax_left, 0))
        table.bind('<Double-1>', lambda event: on_diver_select(event, table, self, divers_list))

        # Repopulate(תאכלס מחדש) the table with updated equipment_list
        for i, diver in enumerate(divers_list):
            table.insert('', 'end', text="",
                         values=(diver.ID, diver.name, diver.age, diver.num_of_dives, diver.rank, diver.union))
        divers_page_fm.pack(fill=tk.BOTH, expand=True)

    def attach_instructor(self, all_instructors):
        def submit():
            id_to_remove = id_entry.get()

            if id_to_remove.isdigit():
                for i, instructor in enumerate(all_instructors):
                    if instructor.ID == int(id_to_remove):
                        self.instructor = instructor
                        attach_window.destroy()
                        return
                    ans_label.config(text="Instructor not exist.", fg="red")
            else:
                ans_label.config(text="ID number contain letters.", fg="red")

        # New window for adding equipment
        attach_window = tk.Toplevel()
        attach_window.title("ID Instructor")

        tk.Label(attach_window, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(attach_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        submit_button = tk.Button(attach_window, text="Submit", command=submit)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(attach_window, text="")  # Create the label
        ans_label.grid(row=3, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()
