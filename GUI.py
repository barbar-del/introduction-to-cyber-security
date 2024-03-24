import tkinter as tk
from tkinter import ttk

from Entities.DivingClub import DivingClub
from functions.generalFunctions import sort_by_name, sort_by_number, on_item_select, delete_selected_item, on_close, \
    deserialize, active_button

# Global array (our DB for the program)
my_club = DivingClub('Marina')


def run_app():
    # main window initialization
    window_width = 1100  # width
    window_height = 500  # height
    btn_width = window_width * 0.2  # button width
    root_pax_left = (window_width - btn_width) // 2 - btn_width  #
    root = tk.Tk()  #
    root.geometry(f'{window_width}x{window_height}')  #
    root.title("Dive system")  # Window's title

    # menu
    def switch(page):
        for fm in main_frame.winfo_children():
            fm.destroy()
            root.update()
        page()

    # Display menu
    def toggle_menu():
        def collapse_toggle_menu():
            toggle_menu_fm.destroy()
            toggle_btn.config(text='☰', command=toggle_menu)

        # toggle_menu
        toggle_menu_fm = tk.Frame(root, bg='#158aff')
        toggle_menu_fm.place(x=0, y=50, height=root.winfo_height(), width=btn_width)
        toggle_btn.config(text='X', command=collapse_toggle_menu)
        # manager button
        manager_btn = tk.Button(toggle_menu_fm, text='Home', font=('Bold', 20), bd=0, bg='#158aff', fg='white',
                                command=lambda: switch(page=manager_page))
        manager_btn.place(x=20, y=toggle_menu_fm.winfo_height())
        # inventory button
        inventory_btn = tk.Button(toggle_menu_fm, text='Inventory', font=('Bold', 20), bd=0, bg='#158aff', fg='white',
                                  command=lambda: switch(page=inventory_page))
        inventory_btn.place(x=20, y=60)
        # divers button
        divers_btn = tk.Button(toggle_menu_fm, text='Divers', font=('Bold', 20), bd=0, bg='#158aff', fg='white',
                               command=lambda: switch(page=divers_page))
        divers_btn.place(x=20, y=120)
        # Instructors button
        instructors_btn = tk.Button(toggle_menu_fm, text='Instructors', font=('Bold', 20), bd=0, bg='#158aff',
                                    fg='white',
                                    command=lambda: switch(page=instructors_page))
        instructors_btn.place(x=20, y=180)
        # dives button
        dives_btn = tk.Button(toggle_menu_fm, text='Dives', font=('Bold', 20), bd=0, bg='#158aff', fg='white',
                              command=lambda: switch(page=dives_page))
        dives_btn.place(x=20, y=240)

    # Top Frame Creation
    head_frame = tk.Frame(root, bg='#158aff', highlightbackground='white', highlightthickness=0.5)
    head_frame.pack(side=tk.TOP, fill=tk.X)
    head_frame.pack_propagate(False)
    head_frame.configure(height=50)

    # Manu Button Creation
    toggle_btn = tk.Button(head_frame, text='☰', bg='#158aff', fg='white', font=('Bold', 20), bd=0,
                           activebackground='#158aff', activeforeground='black', command=toggle_menu)
    toggle_btn.pack(side=tk.LEFT)

    # Title Creation
    title_lbl = tk.Label(head_frame, text="Dive System", bg='#158aff', fg='white', font=('Bold', 20), bd=0, )
    title_lbl.pack(side=tk.LEFT)

    # Main frame
    main_frame = tk.Frame(root, bg='gray')
    main_frame.pack(fill=tk.BOTH, expand=True)

    def manager_page():
        # Home Page Frame
        home_page_fm = tk.Frame(main_frame)
        home_page_fm.pack(fill=tk.BOTH, expand=True)

        # Home Page Title Of The Page
        home_page_lb = tk.Label(home_page_fm, text="Admin Page", font=('Arial', 25), fg='#0097e8')
        home_page_lb.pack(pady=20)

        # Create a container frame for the columns to control their layout more easily
        columns_container = tk.Frame(home_page_fm)
        columns_container.pack(fill=tk.BOTH, expand=True)

        # Buttons column 1
        button_frame_col1 = tk.Frame(columns_container)
        button_frame_col1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(20, 10), pady=20)
        # Title for column 1
        col1_title = tk.Label(button_frame_col1, text="Delete", font=('Arial', 14), bg='white', fg='#0097e8')
        col1_title.pack(side=tk.TOP, fill=tk.X)  # fill=tk.X will make the title expand to fill the width with the
        # column
        delete_equipment_button = tk.Button(button_frame_col1, text="Delete Equipment", relief=tk.RAISED, borderwidth=4,
                                            background="#0097e8", foreground="white", font=('Arial', 14),
                                            highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                            command=lambda: my_club.delete_equipment(), width=15)
        delete_equipment_button.pack(side=tk.TOP, pady=(20, 0))
        delete_diver_button = tk.Button(button_frame_col1, text="Delete Diver", relief=tk.RAISED, borderwidth=4,
                                        background="#0097e8", foreground="white", font=('Arial', 14),
                                        highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                        command=lambda: my_club.delete_diver(), width=15)
        delete_diver_button.pack(side=tk.TOP, pady=(10, 0))
        delete_instructor_button = tk.Button(button_frame_col1, text="Delete Instructor", relief=tk.RAISED,
                                             borderwidth=4,
                                             background="#0097e8", foreground="white", font=('Arial', 14),
                                             highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                             command=lambda: my_club.delete_instructor(), width=15)
        delete_instructor_button.pack(side=tk.TOP, pady=(10, 0))
        delete_dive_button = tk.Button(button_frame_col1, text="Delete Dive", relief=tk.RAISED, borderwidth=4,
                                       background="#0097e8", foreground="white", font=('Arial', 14),
                                       highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                       command=lambda: my_club.delete_dive(), width=15)
        delete_dive_button.pack(side=tk.TOP, pady=(10, 0))

        # Buttons column 2
        button_frame_col2 = tk.Frame(columns_container)
        button_frame_col2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=20)
        # Title for column 2
        col2_title = tk.Label(button_frame_col2, text="Add", font=('Arial', 14), bg='white', fg='#0097e8')
        col2_title.pack(side=tk.TOP, fill=tk.X)
        add_equipment_button = tk.Button(button_frame_col2, text="Add Equipment", relief=tk.RAISED, borderwidth=4,
                                         background="#0097e8", foreground="white", font=('Arial', 14),
                                         highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                         command=lambda: my_club.add_new_equipment(), width=15)
        add_equipment_button.pack(side=tk.TOP, pady=(20, 0))
        add_diver_button = tk.Button(button_frame_col2, text="Add Diver", relief=tk.RAISED, borderwidth=4,
                                     background="#0097e8", foreground="white", font=('Arial', 14),
                                     highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                     command=lambda: my_club.add_new_diver(), width=15)
        add_diver_button.pack(side=tk.TOP, pady=(10, 0))
        add_instructor_button = tk.Button(button_frame_col2, text="Add Instructor", relief=tk.RAISED, borderwidth=4,
                                          background="#0097e8", foreground="white", font=('Arial', 14),
                                          highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                          command=lambda: my_club.add_new_instructor(), width=15)
        add_instructor_button.pack(side=tk.TOP, pady=(10, 0))
        add_dive_button = tk.Button(button_frame_col2, text="Add Dive", relief=tk.RAISED, borderwidth=4,
                                    background="#0097e8", foreground="white", font=('Arial', 14),
                                    highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                    command=lambda: my_club.add_new_diving_session(my_club.locations), width=15)
        add_dive_button.pack(side=tk.TOP, pady=(10, 0))
        # Buttons column 3
        button_frame_col3 = tk.Frame(columns_container)
        button_frame_col3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(10, 20), pady=20)
        # Title for column 3
        col3_title = tk.Label(button_frame_col3, text="Other", font=('Arial', 14), bg='white', fg='#0097e8')
        col3_title.pack(side=tk.TOP, fill=tk.X)
        upgrade_diver_button = tk.Button(button_frame_col3, text="Upgrade Diver", relief=tk.RAISED, borderwidth=4,
                                         background="#0097e8", foreground="white", font=('Arial', 14),
                                         highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                         command=lambda: my_club.promotion_diver(), width=15)
        upgrade_diver_button.pack(side=tk.TOP, pady=(20, 0))
        add_location_button = tk.Button(button_frame_col3, text="Add Location", relief=tk.RAISED, borderwidth=4,
                                        background="#0097e8", foreground="white", font=('Arial', 14),
                                        highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                        command=lambda: my_club.add_new_location(), width=15)
        add_location_button.pack(side=tk.TOP, pady=(10, 0))
        print_locations_button = tk.Button(button_frame_col3, text="Print Locations", relief=tk.RAISED, borderwidth=4,
                                           background="#0097e8", foreground="white", font=('Arial', 14),
                                           highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                           command=lambda: my_club.display_locations(), width=15)
        print_locations_button.pack(side=tk.TOP, pady=(10, 0))
        remove_location_button = tk.Button(button_frame_col3, text="Remove Locations", relief=tk.RAISED, borderwidth=4,
                                           background="#0097e8", foreground="white", font=('Arial', 14),
                                           highlightthickness=0, activebackground="#040f46", activeforeground="white",
                                           command=lambda: my_club.remove_location(), width=15)
        remove_location_button.pack(side=tk.TOP, pady=(10, 0))

    def inventory_page():
        # Inventory Page Frame
        inventory_page_fm = tk.Frame(main_frame)

        # Inventory Title Of The Page
        inventory_page_lb = tk.Label(inventory_page_fm, text="Inventory Page",
                                     font=('Arial', 25), fg='#0097e8')
        inventory_page_lb.pack(pady=20, padx=(root_pax_left, 0))

        # Create a table
        table = ttk.Treeview(inventory_page_fm, columns=('ID', 'Item', 'Quantity'))
        table['columns'] = ('ID', 'Item', 'Quantity')
        table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
        table.column('ID', anchor=tk.CENTER, width=150)
        table.column('Item', anchor=tk.CENTER, width=150)
        table.column('Quantity', anchor=tk.CENTER, width=100)
        table.heading('#0', text='', anchor=tk.W)
        table.heading("ID", text="ID", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'ID', False))
        table.heading("Item", text="Item", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Item', False))
        # table.heading('Quantity', text='Quantity', anchor=tk.CENTER)
        table.heading("Quantity", text="Quantity", anchor=tk.CENTER,
                      command=lambda: sort_by_number(table, 'Quantity', False))
        table.pack(pady=20, padx=(root_pax_left, 0))

        # Repopulate(תאכלס מחדש) the table with updated equipment_list
        for i, equipment in enumerate(my_club.equipments):
            table.insert('', 'end', text="", values=(equipment.ID, equipment.name, equipment.quantity))
        inventory_page_fm.pack(fill=tk.BOTH, expand=True)

    def divers_page():
        # Divers Page Frame
        divers_page_fm = tk.Frame(main_frame)

        # Divers Title Of The Page
        divers_page_lb = tk.Label(divers_page_fm, text="Divers Page",
                                  font=('Arial', 25), fg='#0097e8')
        divers_page_lb.pack(pady=20, padx=(root_pax_left, 0))
        # label_width = divers_page_lb.winfo_reqwidth() (We didn't use that, so I put that in comment)

        #
        button_frame = tk.Frame(divers_page_fm)
        button_frame.pack()

        # Add equipments
        add_equipments_button = tk.Button(button_frame, text="Order Equipment", relief=tk.RAISED, borderwidth=2,
                                          background="#0097e8", foreground="white", font=('Arial', 14),
                                          highlightthickness=0)
        add_equipments_button.pack(side=tk.RIGHT, padx=0)
        add_equipments_button.config(state='disabled',
                                     command=lambda: [active_button(add_equipments_button),
                                                      find_clicked_diver(table, 'diver')])

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
        table.heading("Age", text="Age", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'Age', False))
        table.heading("Number Of Dives", text="Number Of Dives", anchor=tk.CENTER,
                      command=lambda: sort_by_number(table, 'Number Of Dives', False))
        table.heading("Rank", text="Rank", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'Rank', False))
        table.heading("Union", text="Union", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Union', False))
        table.pack(pady=20, padx=(root_pax_left, 0))
        table.bind('<<TreeviewSelect>>',
                   lambda event: active_button(add_equipments_button))
        table.bind('<Double-1>', lambda event: find_and_display_equipments(event, table,
                                                                           my_club.divers)
        if table.selection() else None)
        # Repopulate(תאכלס מחדש) the table with updated equipment_list
        for i, diver in enumerate(my_club.divers):
            table.insert('', 'end', text="",
                         values=(diver.ID, diver.name, diver.age, diver.num_of_dives, diver.rank, diver.union))
        divers_page_fm.pack(fill=tk.BOTH, expand=True)

    def instructors_page():
        # Instructors Page Frame
        instructors_page_fm = tk.Frame(main_frame)

        # Instructors Title Of The Page
        instructors_page_lb = tk.Label(instructors_page_fm, text="Instructors Page",
                                       font=('Arial', 25), fg='#0097e8')
        instructors_page_lb.pack(pady=20, padx=(root_pax_left, 0))
        # label_width = Instructors_page_lb.winfo_reqwidth() (We didn't use that, so I put that in comment)

        button_frame = tk.Frame(instructors_page_fm)
        button_frame.pack()

        # Add equipments
        add_equipments_button = tk.Button(button_frame, text="Order Equipment", relief=tk.RAISED, borderwidth=2,
                                          background="#0097e8", foreground="white", font=('Arial', 14),
                                          highlightthickness=0)
        add_equipments_button.pack(side=tk.RIGHT, padx=0)
        add_equipments_button.config(state='disabled',
                                     command=lambda: [active_button(add_equipments_button),
                                                      find_clicked_diver(table, 'instructor')])

        # Create a table
        table = ttk.Treeview(instructors_page_fm)
        table['columns'] = ('ID', 'Name', 'Age', 'Number Of Dives', 'Start Date', 'Seniority', 'Rank', 'Union')
        table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
        table.column('ID', anchor=tk.CENTER, width=100)
        table.column('Name', anchor=tk.CENTER, width=150)
        table.column('Age', anchor=tk.CENTER, width=100)
        table.column('Number Of Dives', anchor=tk.CENTER, width=100)
        table.column('Start Date', anchor=tk.CENTER, width=100)
        table.column('Seniority', anchor=tk.CENTER, width=100)
        table.column('Rank', anchor=tk.CENTER, width=100)
        table.column('Union', anchor=tk.CENTER, width=100)
        table.heading('#0', text='', anchor=tk.W)
        table.heading("ID", text="ID", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'ID', False))
        table.heading("Name", text="Name", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Name', False))
        table.heading("Age", text="Age", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'Age', False))
        table.heading("Number Of Dives", text="Number Of Dives", anchor=tk.CENTER,
                      command=lambda: sort_by_number(table, 'Number Of Dives', False))
        table.heading("Start Date", text="Start Date", anchor=tk.CENTER)
        table.heading("Seniority", text="Seniority", anchor=tk.CENTER,
                      command=lambda: sort_by_number(table, 'Seniority', False))
        table.heading("Rank", text="Rank", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'Rank', False))
        table.heading("Union", text="Union", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Union', False))
        table.pack(pady=20, padx=(root_pax_left, 0))
        table.bind('<<TreeviewSelect>>',
                   lambda event: active_button(add_equipments_button))
        table.bind('<Double-1>', lambda event: find_and_display_equipments(event, table, my_club.instructors))
        # Repopulate(תאכלס מחדש) the table with updated equipment_list
        for i, instructor in enumerate(my_club.instructors):
            table.insert('', 'end', text="", values=(
                instructor.ID, instructor.name, instructor.age, instructor.num_of_dives, instructor.start_date,
                instructor.seniority, instructor.rank, instructor.union))
        instructors_page_fm.pack(fill=tk.BOTH, expand=True)

    def dives_page():
        # Dive Page Frame
        dives_page_fm = tk.Frame(main_frame)

        # Dive Title Of The Page
        dives_page_lb = tk.Label(dives_page_fm, text="Dives Page",
                                 font=('Arial', 25), fg='#0097e8')
        dives_page_lb.pack(pady=20, padx=(root_pax_left, 0))
        # label_width = dives_page_lb.winfo_reqwidth() (We didn't use that, so I put that in comment)

        #
        button_frame = tk.Frame(dives_page_fm)
        button_frame.pack()

        # Add divers
        add_divers_button = tk.Button(button_frame, text="Add Divers", relief=tk.RAISED, borderwidth=2,
                                      background="#0097e8", foreground="white", font=('Arial', 14),
                                      highlightthickness=0)
        add_divers_button.pack(side=tk.RIGHT, padx=0)
        add_divers_button.config(state='disabled',
                                 command=lambda: [active_button(add_divers_button), find_clicked_session(table)])

        # Create a table
        table = ttk.Treeview(dives_page_fm)
        table['columns'] = ('Dive ID', 'Depth', 'Location', 'Instructor name')
        table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
        table.column('Dive ID', anchor=tk.CENTER, width=100)
        table.column('Depth', anchor=tk.CENTER, width=100)
        table.column('Location', anchor=tk.CENTER, width=150)
        table.column('Instructor name', anchor=tk.CENTER, width=100)
        table.heading('#0', text='', anchor=tk.CENTER)
        table.heading("Dive ID", text="Dive ID", anchor=tk.CENTER,
                      command=lambda: sort_by_number(table, 'Dive ID', False))
        table.heading("Depth", text="Depth", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'Depth', False))
        table.heading("Location", text="Location", anchor=tk.CENTER,
                      command=lambda: sort_by_name(table, 'Location', False))
        table.heading("Instructor name", text="Instructor name", anchor=tk.CENTER,
                      command=lambda: sort_by_name(table, 'Instructor name', False))
        table.pack(pady=20, padx=(root_pax_left, 0))
        table.bind('<<TreeviewSelect>>', lambda event: active_button(add_divers_button))
        table.bind('<Double-1>', lambda event: find_and_display_divers(event, table,
                                                                       my_club.diving_sessions) if table.focus() else None)
        # Repopulate(תאכלס מחדש) the table with updated equipment_list
        for i, dive in enumerate(my_club.diving_sessions):
            if dive.instructor is not None:
                table.insert('', 'end', text="",
                             values=(dive.id, dive.diving_depth, dive.location, dive.instructor.name))
        dives_page_fm.pack(fill=tk.BOTH, expand=True)

    manager_page()
    global my_club
    my_club = deserialize()
    if my_club is None:
        my_club = DivingClub("Marina")

    def find_clicked_session(table):
        # Get the selected item from the table
        selected_item = table.selection()[0]  # Assuming single selection mode
        item_values = table.item(selected_item, 'values')
        dive_id = int(item_values[0])  # Assuming 'Dive ID' is the first value

        # Find the diving_session with the same 'Dive ID'
        for session in my_club.diving_sessions:
            if session.id == dive_id:
                # Perform the necessary actions with the found session
                # For example, add divers to this session or perform some checks
                # Example: session.add_divers(some_divers_list)
                print(f"Found diving session with ID: {dive_id}")
                session.add_all_divers(my_club.divers)
                break
        else:
            print(f"No diving session found with ID: {dive_id}")

    def find_and_display_divers(event, table, diving_sessions):
        if table.identify_region(event.x, event.y) != "cell":
            return  # Ignore double-clicks not on cells

        # Proceed with the rest of the function...
        selected_item = table.focus()
        item = table.item(selected_item)
        item_values = item['values']

        if item_values:  # Additional check to ensure item_values is not empty
            session_id = int(item_values[0])  # Assuming the ID is the first column
            selected_session = next((session for session in diving_sessions if session.id == session_id), None)

            if selected_session:
                # Create a new window to display the divers of the selected session
                divers_window = tk.Toplevel()
                divers_window.title(f"Divers in Session {session_id}")

                # Create a table to display the divers
                divers_table = ttk.Treeview(divers_window)
                divers_table['columns'] = ('ID', 'Name', 'Age', 'Number Of Dives', 'Rank', 'Union')
                divers_table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
                divers_table.column('ID', anchor=tk.CENTER, width=100)
                divers_table.column('Name', anchor=tk.CENTER, width=150)
                divers_table.column('Age', anchor=tk.CENTER, width=100)
                divers_table.column('Number Of Dives', anchor=tk.CENTER, width=100)
                divers_table.column('Rank', anchor=tk.CENTER, width=100)
                divers_table.column('Union', anchor=tk.CENTER, width=100)

                # Define the headings
                divers_table.heading('ID', text='ID')
                divers_table.heading('Name', text='Name')
                divers_table.heading('Age', text='Age')
                divers_table.heading('Number Of Dives', text='Number Of Dives')
                divers_table.heading('Rank', text='Rank')
                divers_table.heading('Union', text='Union')

                for diver in selected_session.divers:
                    divers_table.insert('', 'end', values=(
                        diver.ID, diver.name, diver.age, diver.num_of_dives, diver.rank, diver.union))

                divers_table.pack(expand=True, fill='both')

    def find_and_display_equipments(event, table, divers):
        # Use identify to check if the double-click is on an item
        if table.identify("region", event.x, event.y) != "cell":
            return  # Exit if not clicked on a cell

        # Use identify_row to get the item at the event's y-coordinate
        row_id = table.identify_row(event.y)
        if not row_id:
            return  # Exit if the click is not on a row

        # Proceed with getting the item's values
        item_values = table.item(row_id, 'values')
        if item_values:
            try:
                diver_id = int(item_values[0])  # Assuming the ID is the first column
            except ValueError:
                return  # Exit if conversion to int fails

            selected_diver = next((diver for diver in divers if diver.ID == diver_id), None)

            if selected_diver:
                equipments_window = tk.Toplevel()
                equipments_window.title(f"Equipments Of Diver {diver_id}")

                equipments_table = ttk.Treeview(equipments_window)
                equipments_table['columns'] = ('ID', 'Name', 'Quantity')
                equipments_table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
                equipments_table.column('ID', anchor=tk.CENTER, width=100)
                equipments_table.column('Name', anchor=tk.CENTER, width=150)
                equipments_table.column('Quantity', anchor=tk.CENTER, width=100)

                # Define the headings
                equipments_table.heading('ID', text='ID', command=lambda: sort_by_number(table, 'ID', False))
                equipments_table.heading('Name', text='Name', command=lambda: sort_by_name(table, 'Age', False))
                equipments_table.heading('Quantity', text='Quantity', command=lambda: sort_by_number(table,
                                                                                                     'Quantity', False))

                for equipment in selected_diver.equipment_list:
                    equipments_table.insert('', 'end', values=(
                        equipment.ID, equipment.name, equipment.quantity))

                equipments_table.pack(expand=True, fill='both')

    def find_clicked_diver(table, type):
        # Get the selected item from the table
        selected_item = table.selection()[0]  # Assuming single selection mode
        item_values = table.item(selected_item, 'values')
        diver_id = int(item_values[0])  # Assuming 'Dive ID' is the first value

        if type == 'diver':
            # Find the diving_session with the same 'Dive ID'
            for diver in my_club.divers:
                if diver.ID == diver_id:
                    # Perform the necessary actions with the found session
                    # For example, add divers to this session or perform some checks
                    # Example: session.add_divers(some_divers_list)
                    print(f"Found diver with ID: {diver_id}")
                    diver.add_all_equipments(my_club.equipments)
                    break
            else:
                print(f"No diver found with ID: {diver_id}")
        elif type == 'instructor':
            # Find the diving_session with the same 'Dive ID'
            for instructor in my_club.instructors:
                if instructor.ID == diver_id:
                    # Perform the necessary actions with the found session
                    # For example, add divers to this session or perform some checks
                    # Example: session.add_divers(some_divers_list)
                    print(f"Found instructor with ID: {diver_id}")
                    instructor.add_all_equipments(my_club.equipments)
                    break
            else:
                print(f"No instructor found with ID: {diver_id}")

    root.protocol("WM_DELETE_WINDOW", lambda: on_close(root, my_club))
    root.mainloop()
