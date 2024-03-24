import pickle
import sys

import pandas as pd


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


def on_item_select(delete_button):
    delete_button.config(state='normal')  # Enable the delete button


def delete_selected_item(table, typeOfList, objects_list):
    # Get all selected items
    selected_items = table.selection()

    # This assumes that the ID is in the first column of your table
    for selected_item in selected_items:
        item = table.item(selected_item)
        item_values = item['values']
        item_id = int(item_values[0])  # Get the ID of the selected item, convert to int if necessary

        if typeOfList == 'equipment':
            # Find the corresponding equipment object by ID and remove it
            equipment_to_delete = None
            for equipment in objects_list:
                if equipment.ID == item_id:
                    equipment_to_delete = equipment
                    break  # Break the loop once the item is found

            # If an equipment object was found, remove it from the list
            if equipment_to_delete:
                objects_list.remove(equipment_to_delete)
                table.delete(selected_item)  # Also remove the item from the treeview
                print(f"Removed equipment with ID: {item_id}")
            else:
                print(f"No equipment found with ID: {item_id}")

        if typeOfList == 'diver':
            # Find the corresponding diver object by ID and remove it
            diver_to_delete = None
            for diver in objects_list:
                if diver.ID == item_id:
                    diver_to_delete = diver
                    break  # Break the loop once the item is found

            # If an equipment object was found, remove it from the list
            if diver_to_delete:
                objects_list.remove(diver_to_delete)
                table.delete(selected_item)  # Also remove the item from the treeview
                print(f"Removed diver with ID: {item_id}")
            else:
                print(f"No diver found with ID: {item_id}")

        if typeOfList == 'instructor':
            # Find the corresponding instructor object by ID and remove it
            instructor_to_delete = None
            for instructor in objects_list:
                if instructor.ID == item_id:
                    instructor_to_delete = instructor
                    break  # Break the loop once the item is found

            # If an equipment object was found, remove it from the list
            if instructor_to_delete:
                objects_list.remove(instructor_to_delete)
                table.delete(selected_item)  # Also remove the item from the treeview
                print(f"Removed instructor with ID: {item_id}")
            else:
                print(f"No instructor found with ID: {item_id}")

        if typeOfList == 'dive':
            # Find the corresponding instructor object by ID and remove it
            dive_to_delete = None
            for dive in objects_list:
                if dive.id == item_id:
                    dive_to_delete = dive
                    break  # Break the loop once the item is found

            # If an equipment object was found, remove it from the list
            if dive_to_delete:
                objects_list.remove(dive_to_delete)
                table.delete(selected_item)  # Also remove the item from the treeview
                print(f"Removed dive with ID: {item_id}")
            else:
                print(f"No dive found with ID: {item_id}")


def on_close(root, diver_club):
    print("Window closed!")
    with open('DB/DivingClub.pickle', 'wb') as f:
        pickle.dump(diver_club, f)
    root.destroy()


def deserialize():
    from Entities.DivingSession import DivingSession  # Import inside the function
    sys.modules['DivingClub'] = sys.modules['Entities.DivingClub']
    sys.modules['DivingSession'] = sys.modules['Entities.DivingSession']
    print("deserialize")
    try:
        with open('DB/DivingClub.pickle', 'rb') as f:
            new_diving_club = pickle.load(f)
        print("Loaded locations:", new_diving_club.locations)  # Add this line
        del sys.modules['DivingClub']
        del sys.modules['DivingSession']
        max_id = 0
        if len(new_diving_club.diving_sessions) > 0:
            max_id = max(session.id for session in new_diving_club.diving_sessions)
        # Set the static_id to one more than the maximum found
        DivingSession.static_id = max_id + 1
        # Clear sessions without instructor
        for diving_session in new_diving_club.diving_sessions:
            if diving_session.instructor is None:
                new_diving_club.diving_sessions.remove(diving_session)
        # Update seniority of all the instructors
        for instructor in new_diving_club.instructors:
            instructor.update_seniority()
        return new_diving_club  # Return the loaded object
    except FileNotFoundError:
        print("No previous data found")
        del sys.modules['DivingClub']
        return None


def active_button(btn):
    btn.config(state='normal')
