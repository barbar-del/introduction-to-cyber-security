from enum import Enum

import tkinter as tk
import Entities.Person
from Entities.Equipment import Equipment
from tkinter import ttk
from functions.generalFunctions import sort_by_number, sort_by_name


# Define an enumeration for diver ranks
class Rank(Enum):
    Beginner = 1
    Intermediate = 2
    Advanced = 3
    Expert = 4


# Functions
def on_equipment_select(event, table, diver, equipments_list):
    # Verify the double-click is on an item
    if table.identify_region(event.x, event.y) != "cell":
        return  # Exit if not clicked on a cell

    # Get the item that was double-clicked
    selected_item = table.focus()
    if not selected_item:
        return  # Exit if no item is focused

    item = table.item(selected_item)
    item_values = item['values']

    # Check if item_values is not empty
    if item_values:
        try:
            equipment_id = int(item_values[0])  # Assuming the ID is the first column
        except ValueError:
            return  # Exit if conversion to int fails

        selected_equipment = next((equipment for equipment in equipments_list if equipment.ID == equipment_id), None)

        if selected_equipment:
            is_exist = any(equipment.ID == selected_equipment.ID for equipment in diver.equipment_list)

            if is_exist:
                for equipment in diver.equipment_list:
                    if equipment.ID == selected_equipment.ID:
                        if selected_equipment.quantity > 0:
                            equipment.quantity += 1
                            selected_equipment.quantity -= 1
                            print(f"{diver.name} has {equipment.quantity} of {equipment.name}.")
                        elif selected_equipment.quantity == 0:
                            print(f"{equipment.name} is out of stock.")
                        else:
                            print(f"{equipment.name}'s stock is less than zero, please report the admin.")
            else:
                new_equipment = Equipment(selected_equipment.ID, 1, selected_equipment.name)
                selected_equipment.quantity -= 1
                diver.equipment_list.append(new_equipment)
                print(f"Equipment with ID {equipment_id} added to {diver.name}.")
    else:
        print("No equipment selected.")


# Class
class Diver(Entities.Person.Person):

    def __init__(self, ID, name, age, union, equipment_list=[]):
        super().__init__(ID, name, age)  # Call the constructor of the parent class
        self.num_of_dives = 0  # Default
        self.rank = Rank.Beginner.value  # Default
        self.union = union
        self.equipment_list = equipment_list  # List to store the diver's equipment

    def add_all_equipments(self, equipment_list):
        # main window initialization
        window_width = 1100  # width
        window_height = 500  # height
        btn_width = window_width * 0.2  # button width
        root_pax_left = (window_width - btn_width) // 2 - btn_width  #

        #
        root = tk.Tk()
        root.geometry(f'{window_width}x{window_height}')
        root.title("Equipments list")  # Window's title

        # Main frame
        main_frame = tk.Frame(root, bg='gray')
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Divers Page Frame
        equipments_page_fm = tk.Frame(main_frame)

        # Divers Title Of The Page
        equipments_page_lb = tk.Label(equipments_page_fm, text="Equipments list",
                                  font=('Arial', 25), fg='#0097e8')
        equipments_page_lb.pack(pady=20, padx=(root_pax_left, 0))

        # button frame
        button_frame = tk.Frame(equipments_page_fm)
        button_frame.pack()

        # Create a table
        table = ttk.Treeview(equipments_page_fm)
        table['columns'] = ('ID', 'Item', 'Quantity')
        table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
        table.column('ID', anchor=tk.CENTER, width=100)
        table.column('Item', anchor=tk.CENTER, width=150)
        table.column('Quantity', anchor=tk.CENTER, width=100)
        table.heading("ID", text="ID", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'ID', False))
        table.heading("Item", text="Name", anchor=tk.CENTER, command=lambda: sort_by_name(table, 'Item', False))
        table.heading("Quantity", text="Quantity", anchor=tk.CENTER, command=lambda: sort_by_number(table, 'Quantity', False))
        table.pack(pady=20, padx=(root_pax_left, 0))
        table.bind('<Double-1>', lambda event: on_equipment_select(event, table, self, equipment_list))

        # Repopulate(תאכלס מחדש) the table with updated equipment_list
        for equipment in equipment_list:
            table.insert('', 'end', text="",
                         values=(equipment.ID, equipment.name, equipment.quantity))
        equipments_page_fm.pack(fill=tk.BOTH, expand=True)

    # Function to check the amount of dives the diver has done and assign a rank accordingly
    # 0-5 dives = beginner, 6-10 dives = intermediate, 11-15 dives = advanced, 15+ dives = expert
    def check_rank(self):
        if self.num_of_dives >= 16:
            return Rank.Expert.value
        elif self.num_of_dives >= 11:
            return Rank.Advanced.value
        elif self.num_of_dives >= 6:
            return Rank.Intermediate.value
        else:
            return Rank.Beginner.value







