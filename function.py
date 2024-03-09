import Diver_Club
import tkinter as tk
import csv
import pandas as pd

def get_all_divers_names_and_id(club:Diver_Club):
  #  Return a list of names and IDs of all divers in the club.
    return [(diver.name, diver.id) for diver in club.divers]

def get_all_instructors_names_and_id(club):
  #  Return a list of names and IDs of all instructors in the club.
    return [(instructor.name, instructor.id) for instructor in club.instructors]

# Function to sort by number
def sort_by_number(tree, col, reverse):
    # Retrieve the list of items in the treeview
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    # Sort the list in place, converting values to integers for proper numerical sorting
    l.sort(key=lambda t: int(t[0]), reverse=reverse)

    # Rearrange the items in sorted order
    for index, (_, k) in enumerate(l):
        tree.move(k, '', index)

    # Reverse the sorting order for the next time
    tree.heading(col, command=lambda: sort_by_number(tree, col, not reverse))

# Function to sort by name
def sort_by_name(tree, col, reverse):
    # Retrieve the list of items in the treeview
    l = [(tree.set(k, col), k) for k in tree.get_children('')]
    # Sort the list in place, this time without converting to integers since we're dealing with strings
    l.sort(key=lambda t: t[0], reverse=reverse)

    # Rearrange the items in sorted order
    for index, (_, k) in enumerate(l):
        tree.move(k, '', index)

    # Reverse the sorting order for the next time
    tree.heading(col, command=lambda: sort_by_name(tree, col, not reverse))

# Function of adding a new dive
def open_add_dive_window(root, dive_table):
    # Create a new Toplevel window
    add_dive_window = tk.Toplevel(root)
    add_dive_window.title("Add Dive")

    # Define labels and entry widgets for each field
    labels = ['Dive_id', 'Depth', 'Instructor_name', 'Instructor_id', 'Location', 'Club', 'Equipment']
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(add_dive_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='w')
        entry = tk.Entry(add_dive_window)
        entry.grid(row=i, column=1, padx=10, pady=5, sticky='w')
        entries[label] = entry

    # Function to collect the data and update the CSV and table
    def submit_dive():
        dive_data = [entry.get() for entry in entries.values()]
        add_to_csv(dive_data, 'DivesXL.csv')
        refresh_table('DivesXL.csv', dive_table)
        add_dive_window.destroy()

    # Submit button
    submit_btn = tk.Button(add_dive_window, text="Submit", command=submit_dive)
    submit_btn.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Function of adding a new instructor
def open_add_instructor_window(root, instructor_table):
  # Create a new Toplevel window
  add_instructor_window = tk.Toplevel(root)
  add_instructor_window.title("Add Instructor")

  # Define labels and entry widgets for each field
  labels = ['ID', 'Name', 'Rank', 'Company']
  entries = {}

  for i, label in enumerate(labels):
    tk.Label(add_instructor_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(add_instructor_window)
    entry.grid(row=i, column=1, padx=10, pady=5, sticky='w')
    entries[label] = entry

  # Function to collect the data and update the CSV and table
  def submit_dive():
    dive_data = [entry.get() for entry in entries.values()]
    add_to_csv(dive_data, 'InstructorsXL.csv')
    refresh_table('InstructorsXL.csv', instructor_table)
    add_instructor_window.destroy()

  # Submit button
  submit_btn = tk.Button(add_instructor_window, text="Submit", command=submit_dive)
  submit_btn.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Function of adding a new diver
def open_add_diver_window(root, diver_table):
  # Create a new Toplevel window
  add_divers_window = tk.Toplevel(root)
  add_divers_window.title("Add Diver")

  # Define labels and entry widgets for each field
  labels = ['ID', 'Name', 'Rank']
  entries = {}

  for i, label in enumerate(labels):
    tk.Label(add_divers_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(add_divers_window)
    entry.grid(row=i, column=1, padx=10, pady=5, sticky='w')
    entries[label] = entry

  # Function to collect the data and update the CSV and table
  def submit_dive():
    dive_data = [entry.get() for entry in entries.values()]
    add_to_csv(dive_data, 'DiversXL.csv')
    refresh_table('DiversXL.csv', diver_table)
    add_divers_window.destroy()

  # Submit button
  submit_btn = tk.Button(add_divers_window, text="Submit", command=submit_dive)
  submit_btn.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Function of adding a new item
def open_add_item_window(root,items_table):
  # Create a new Toplevel window
  add_item_window = tk.Toplevel(root)
  add_item_window.title("Add Item")

  # Define labels and entry widgets for each field
  labels = ['Item', 'Quantity']
  entries = {}

  for i, label in enumerate(labels):
    tk.Label(add_item_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(add_item_window)
    entry.grid(row=i, column=1, padx=10, pady=5, sticky='w')
    entries[label] = entry

  # Function to collect the data and update the CSV and table
  def submit_dive():
    dive_data = [entry.get() for entry in entries.values()]
    add_to_csv(dive_data, 'InventoryXL.csv')
    refresh_table('InventoryXL.csv', items_table)
    add_item_window.destroy()

  # Submit button
  submit_btn = tk.Button(add_item_window, text="Submit", command=submit_dive)
  submit_btn.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Function of writing the new data the excel file
def add_to_csv(dive_data, file_path):
    # Open the CSV file in append mode and write the new row
    with open(file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(dive_data)

# Function of refreshing the data
def refresh_table(file_path, table):
    # Clear the table
    table.delete(*table.get_children())
    # Reload the table with updated data
    upload_table(file_path, table)

# Function of reading and display data from excel file
def upload_table(file_path, table):
    try:
        print(file_path)
        # Read the Excel file into a DataFrame
        df = pd.read_csv(file_path)
        df = df.dropna()
        if 'Quantity' in df.columns:
            df['Quantity'] = df['Quantity'].astype(int)
        print(df)
        # Clear the existing data in the table
        table.delete(*table.get_children())

        # Insert each row from the DataFrame into the table
        for index, row in df.iterrows():
            table.insert('', 'end', values=row.tolist())

        print("Data uploaded successfully.")
    except Exception as e:
        print("Error uploading data:", str(e))


def on_item_select(event, table, delete_button):
    selected = table.selection()
    if selected:  # If there is at least one selected item
        delete_button.config(state='normal')  # Enable the delete button


def update_excel_file(selected_values, path):
    data = pd.read_csv(path)  # Load the entire Excel file into a DataFrame

    for item_values in selected_values:
        unique_identifier = item_values[0]  # Assume the first value is a unique ID, adjust as necessary
        # Make sure the types match (e.g., both are strings or both are integers)
        data = data[data.iloc[:, 0].astype(str) != str(unique_identifier)]

    # Save the updated DataFrame back to the Excel file only once, after all deletions
    data.to_csv(path, index=False)


def delete_selected_item(table, path):
    selected_items = table.selection()  # Get all selected items
    selected_values = [table.item(item, 'values') for item in selected_items]

    for selected_item in selected_items:
        table.delete(selected_item)  # Delete items from the Treeview

    update_excel_file(selected_values, path)  # Update Excel file outside the loop