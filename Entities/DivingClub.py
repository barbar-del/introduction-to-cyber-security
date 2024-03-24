import tkinter as tk
from tkinter import ttk

from Entities.Diver import Diver
from Entities.DivingSession import DivingSession
from Entities.Instructor import Instructor
from Entities.Equipment import Equipment
from functions.generalFunctions import sort_by_number, sort_by_name


class DivingClub:
    name = ''
    divers = None
    instructors = None
    diving_sessions = None
    equipments = None

    def __init__(self, club_name):
        self.name = club_name
        self.divers = []  # List to hold diver objects
        self.instructors = []  # List to hold instructor objects
        self.diving_sessions = []  # List to hold past DivingSession objects
        self.equipments = []  # List to hold equipment objects
        self.locations = []  # List to hold all the location in the club

    def add_new_equipment(self):
        def submit():
            name = name_entry.get()
            count = count_entry.get()
            # Find the smallest unused ID
            existing_ids = [equipment.ID for equipment in self.equipments]
            smallest_id = 1
            while smallest_id in existing_ids:
                smallest_id += 1

            # Add the new equipment item with the smallest unused ID
            if count.isdigit():
                self.equipments.append(Equipment(ID=smallest_id, name=name, quantity=int(count)))
                self.equipments.sort(key=lambda equipment: equipment.ID)
                add_window.destroy()
            else:
                ans_label.config(text="Your count number contain letters.", fg="red")

        # New window for adding equipment
        add_window = tk.Toplevel()
        add_window.title("Add Equipment")

        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Count:").grid(row=1, column=0, padx=10, pady=10)
        count_entry = tk.Entry(add_window)
        count_entry.grid(row=1, column=1, padx=10, pady=10)

        submit_button = tk.Button(add_window, text="Submit", command=submit)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(add_window, text="")  # Create the label
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()

    def add_new_diver(self):
        def submit():
            id_diver = id_entry.get()
            name = name_entry.get()
            age = age_entry.get()
            union = union_entry.get()

            # Find the smallest unused ID
            existing_ids = [diver.ID for diver in self.divers]
            smallest_id = 1
            while smallest_id in existing_ids:
                smallest_id += 1

            # Add the new equipment item with the smallest unused ID
            if id_diver.isdigit():
                if age.isdigit():
                    self.divers.append(Diver(ID=int(id_diver), name=name, age=int(age), union=union))
                    self.divers.sort(key=lambda diver: diver.ID)
                    add_window.destroy()
                else:
                    ans_label.config(text="Your age contain letters.", fg="red")
            else:
                ans_label.config(text="Your ID number contain letters.", fg="red")

        # New window for adding equipment
        add_window = tk.Toplevel()
        add_window.title("Add Diver")

        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_window, text="ID:").grid(row=1, column=0, padx=10, pady=10)
        id_entry = tk.Entry(add_window)
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Age:").grid(row=2, column=0, padx=10, pady=10)
        age_entry = tk.Entry(add_window)
        age_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Union:").grid(row=3, column=0, padx=10, pady=10)
        union_entry = tk.Entry(add_window)
        union_entry.grid(row=3, column=1, padx=0, pady=10)

        submit_button = tk.Button(add_window, text="Submit", command=submit)
        submit_button.grid(row=5, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(add_window, text="")  # Create the label
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()

    def add_new_instructor(self):
        def submit():
            name = name_entry.get()
            id_instructor = id_entry.get()
            age = age_entry.get()
            union = union_entry.get()

            # Find the smallest unused ID
            existing_ids = [instructor.ID for instructor in self.instructors]
            smallest_id = 1
            while smallest_id in existing_ids:
                smallest_id += 1

            # Add the new equipment item with the smallest unused ID
            if id_instructor.isdigit():
                if age.isdigit():
                    self.instructors.append(
                        Instructor(ID=int(id_instructor), name=name, age=int(age), employeeID=smallest_id,
                                   num_of_dives=0,
                                   union=union))
                    self.instructors.sort(key=lambda instructor: instructor.ID)
                    add_window.destroy()
                else:
                    ans_label.config(text="Your age contain letters.", fg="red")
            else:
                ans_label.config(text="Your ID number contain letters.", fg="red")
            # New window for adding equipment

        add_window = tk.Toplevel()
        add_window.title("Add Instructor")

        tk.Label(add_window, text="Name:").grid(row=0, column=0, padx=10, pady=10)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(add_window, text="ID:").grid(row=1, column=0, padx=10, pady=10)
        id_entry = tk.Entry(add_window)
        id_entry.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Age:").grid(row=2, column=0, padx=10, pady=10)
        age_entry = tk.Entry(add_window)
        age_entry.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(add_window, text="Union:").grid(row=3, column=0, padx=10, pady=10)
        union_entry = tk.Entry(add_window)
        union_entry.grid(row=3, column=1, padx=10, pady=10)

        submit_button = tk.Button(add_window, text="Submit", command=submit)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(add_window, text="")  # Create the label
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()

    def add_new_diving_session(self, all_locations):
        def submit():
            depth = depth_entry.get()
            location = location_combobox.get()  # Use .get() on the Combobox to get the selected value

            if depth.isdigit():
                if location in all_locations:
                    new_diving_session = DivingSession(diving_depth=int(depth), instructor=None, location=location)
                    new_diving_session.attach_instructor(self.instructors)
                    self.diving_sessions.append(new_diving_session)
                    self.diving_sessions.sort(key=lambda session: session.id)
                    add_window.destroy()
                    return
                else:
                    ans_label.config(text="Location doesn't exist.", fg="red")
            else:
                ans_label.config(text="Depth contain letters.", fg="red")

        # New window for adding a diving session
        add_window = tk.Toplevel()
        add_window.title("Add Dive")

        # Depth entry
        tk.Label(add_window, text="Depth:").grid(row=0, column=0, padx=10, pady=10)
        depth_entry = tk.Entry(add_window)
        depth_entry.grid(row=0, column=1, padx=10, pady=10)

        # Location selection using a Combobox
        tk.Label(add_window, text="Location:").grid(row=1, column=0, padx=10, pady=10)
        location_combobox = ttk.Combobox(add_window, values=all_locations)
        location_combobox.grid(row=1, column=1, padx=10, pady=10)
        location_combobox.set("Select a location")  # Optional: set a default placeholder text

        # Submit button
        submit_button = tk.Button(add_window, text="Submit", command=submit)
        submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Answer label
        ans_label = tk.Label(add_window, text="")
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)

    def add_new_location(self):
        # Create a new window for adding a location
        add_location_window = tk.Toplevel()
        add_location_window.title("Add New Location")
        add_location_window.geometry("200x130")  # Width x Height

        # Label for the new location
        new_location_label = tk.Label(add_location_window, text="New Location:")
        new_location_label.pack(pady=(10, 0))

        # Text field for the new location
        new_location_entry = tk.Entry(add_location_window)
        new_location_entry.pack()

        # Function to append the new location and close the window
        def append_location():
            new_location = new_location_entry.get()  # Get the value from the text field
            self.locations.append(new_location)  # Append the new location to the locations list
            print("New Location Added:", new_location)  # Printing to console for verification
            add_location_window.destroy()  # Close the add location window

        # Add button
        add_button = tk.Button(add_location_window, text="Add", command=append_location)
        add_button.pack(pady=(10, 0))

        # ans_label = tk.Label(add_location_window, text="")  # Create the label
        # ans_label.pack(pady=(10, 0))  # Place the label using .grid()

    # Remove Location
    def remove_location(self):
        # Create a new window for adding a location
        remove_location_window = tk.Toplevel()
        remove_location_window.title("Add New Location")
        remove_location_window.geometry("200x130")  # Width x Height

        # Label for the new location
        new_location_label = tk.Label(remove_location_window, text="Location name:")
        new_location_label.pack(pady=(10, 0))

        # Text field for the new location
        new_location_entry = tk.Entry(remove_location_window)
        new_location_entry.pack()

        # Function to append the new location and close the window
        def inner_remove_location():
            remove_location = new_location_entry.get()  # Get the value from the text field
            for loc in self.locations:
                if loc == remove_location:
                    print(f"{loc} was removed.")  # Printing to console for verification
                    self.locations.remove(loc)  # Append the new location to the locations list
                    remove_location_window.destroy()  # Close the add location window
                    return
            ans_label.config(text="Location not found.", fg="red")

        # Add button
        add_button = tk.Button(remove_location_window, text="Remove", command=inner_remove_location)
        add_button.pack(pady=(10, 0))

        ans_label = tk.Label(remove_location_window, text="")
        ans_label.pack(pady=10)  # Use pack instead of grid

        # ans_label = tk.Label(add_location_window, text="")  # Create the label
        # ans_label.pack(pady=(10, 0))  # Place the label using .grid()

    # Function to display the locations in the GUI
    def display_locations(self):
        # Create a Toplevel window to display the locations
        locations_window = tk.Toplevel()
        locations_window.title("Locations List")
        locations_window.geometry("300x200")

        # Create a Listbox widget to display the locations
        listbox = tk.Listbox(locations_window)
        listbox.pack(fill='both', expand=True)

        # Insert each location into the Listbox
        for location in self.locations:
            listbox.insert(tk.END, location)

    def delete_equipment(self):
        def submit():
            id_to_remove = id_entry.get()
            if id_to_remove.isdigit():  # in valid
                for equipment in self.equipments:  # find the equipment from the DB
                    if equipment.ID == int(id_to_remove):
                        self.equipments.remove(equipment)  # remove the equipment from the DB
                        for diver in self.divers:  # for each driver
                            for equipment_in_diver in diver.equipment_list:  # find the equipment in the diver's all_equipments
                                if equipment_in_diver.ID == int(id_to_remove):
                                    diver.equipment_list.remove(equipment_in_diver)  # remove
                        for instructor in self.instructors:  # for each driver
                            for equipment_in_instructor in instructor.equipment_list:  # find the equipment in the instructor's all_equipments
                                if equipment_in_instructor.ID == int(id_to_remove):
                                    instructor.equipment_list.remove(equipment_in_instructor)  # remove

                        remove_window.destroy()
                        return
                else:
                    ans_label.config(text="ID number is not exist.", fg="red")
            else:
                ans_label.config(text="number ID contain letters.", fg="red")

        # New window for adding equipment
        remove_window = tk.Toplevel()
        remove_window.title("Remove Equipment")

        tk.Label(remove_window, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(remove_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        submit_button = tk.Button(remove_window, text="Submit", command=submit)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(remove_window, text="")  # Create the label
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()

    def delete_diver(self):
        def submit():
            id_to_remove = id_entry.get()
            if id_to_remove.isdigit():

                for i, diver in enumerate(self.divers):
                    if diver.ID == int(id_to_remove):
                        self.divers.remove(diver)
                        remove_window.destroy()
                        return
                ans_label.config(text="ID number is not exist.", fg="red")
            else:
                ans_label.config(text="number ID contain letters.", fg="red")

        # New window for adding equipment
        remove_window = tk.Toplevel()
        remove_window.title("Remove Diver")

        tk.Label(remove_window, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(remove_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        submit_button = tk.Button(remove_window, text="Submit", command=submit)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(remove_window, text="")  # Create the label
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()

    def delete_instructor(self):
        def submit():
            id_to_remove = id_entry.get()
            if id_to_remove.isdigit():
                for instructor in self.instructors:
                    if instructor.ID == int(id_to_remove):
                        self.instructors.remove(instructor)
                        remove_window.destroy()
                        return
                else:
                    ans_label.config(text="ID number is not exist.", fg="red")
            else:
                ans_label.config(text="number ID contain letters.", fg="red")

        # New window for adding equipment
        remove_window = tk.Toplevel()
        remove_window.title("Remove Instructor")

        tk.Label(remove_window, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(remove_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        submit_button = tk.Button(remove_window, text="Submit", command=submit)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(remove_window, text="")  # Create the label
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()

    def delete_dive(self):
        def submit():
            id_to_remove = id_entry.get()
            if id_to_remove.isdigit():

                for i, diving_session in enumerate(self.diving_sessions):
                    if diving_session.id == int(id_to_remove):
                        self.diving_sessions.remove(diving_session)
                        remove_window.destroy()
                        return
                else:
                    ans_label.config(text="ID number is not exist.", fg="red")
            else:
                ans_label.config(text="number ID contain letters.", fg="red")

        # New window for adding equipment
        remove_window = tk.Toplevel()
        remove_window.title("Remove Dive")

        tk.Label(remove_window, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(remove_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        submit_button = tk.Button(remove_window, text="Submit", command=submit)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(remove_window, text="")  # Create the label
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()

    def promotion_diver(self):
        def submit():
            id_to_remove = id_entry.get()
            if id_to_remove.isdigit():
                for i, diver in enumerate(self.divers):
                    if diver.ID == int(id_to_remove):
                        # Find the smallest unused ID of instructor
                        existing_ids = [instructor.ID for instructor in self.instructors]
                        smallest_id = 1
                        while smallest_id in existing_ids:
                            smallest_id += 1

                        # Add is instructor
                        self.instructors.append(
                            Instructor(ID=diver.ID, name=diver.name, age=diver.age, employeeID=smallest_id,
                                       num_of_dives=diver.num_of_dives, union=diver.union,
                                       equipment_list=diver.equipment_list))
                        self.instructors.sort(key=lambda instructor: instructor.ID)

                        # Remove from Divers
                        self.divers.remove(diver)
                        promotion_window.destroy()
                    else:
                        ans_label.config(text="Diver doesn't exist.", fg="red")
            else:
                ans_label.config(text="ID number contain letters.", fg="red")

        # New window for adding equipment
        promotion_window = tk.Toplevel()
        promotion_window.title("Promotion Diver")

        tk.Label(promotion_window, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(promotion_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        submit_button = tk.Button(promotion_window, text="Submit", command=submit)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)

        ans_label = tk.Label(promotion_window, text="")  # Create the label
        ans_label.grid(row=6, column=0, columnspan=2, sticky=tk.EW, pady=10)  # Place the label using .grid()

    def fire_instructor(self):
        def submit():
            id_to_remove = int(id_entry.get())

            for i, fired_intructor in enumerate(self.instructors):
                if fired_intructor.ID == id_to_remove:
                    # Find the smallest unused ID of instructor
                    fired_intructor.return_equipments(self.equipments)
                    self.instructors.remove(fired_intructor)
                    remove_window.destroy()

        # New window for adding equipment
        remove_window = tk.Toplevel()
        remove_window.title("Fire Instructor")

        tk.Label(remove_window, text="ID:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = tk.Entry(remove_window)
        id_entry.grid(row=0, column=1, padx=10, pady=10)

        submit_button = tk.Button(remove_window, text="Submit", command=submit)
        submit_button.grid(row=2, column=0, columnspan=2, pady=10)
