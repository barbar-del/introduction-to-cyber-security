import Diver
from DivingSession import DivingSession
import Instructor
import Equipment

class Diver_Club:
    def __init__(self, club_name):
        self.name = club_name
        self.divers = []  # List to hold diver objects
        self.instructors = []  # List to hold instructor objects
        self.diving_sessions = []  # List to hold past DivingSession objects
        self.equipment = []  # List to hold equipment objects

    def add_new_diver(self, name, ID, age, num_of_dives, union):
        # Create a new Diver instance
        new_diver = Diver.Diver(name, ID, age, num_of_dives, union)
        # Check if the diver is already in the club
        if not any(diver.ID == ID for diver in self.divers):
            self.divers.append(new_diver)
            return new_diver
        else:
            print("Diver with ID", ID, "is already in the club.")
            return None

    def add_new_instructor(self, name, ID, age, employeeID, num_of_dives, union):
        # Create a new Instructor instance
        new_instructor = Instructor.Instructor(name, ID, age, employeeID, num_of_dives, union)
        # Check if the instructor ID or employeeID is already in the club
        if not any(instructor.ID == ID or instructor.employeeID == employeeID for instructor in self.instructors):
            self.instructors.append(new_instructor)
            return new_instructor
        else:
            print("Instructor with ID", ID, "or employeeID", employeeID, "is already in the club.")
            return None

    def hire_diver_as_instructor(self, diver_id, employeeID):
        # Find the diver in the club by ID
        diver = next((d for d in self.divers if d.ID == diver_id), None)
        if diver is None:
            print("No diver found with ID", diver_id)
            return None

        # Check if the employeeID is already in use by another instructor
        if any(instructor.employeeID == employeeID for instructor in self.instructors):
            print("Employee ID", employeeID, "is already in use.")
            return None

        # Remove the diver from the divers list
        self.divers.remove(diver)

        # Create a new Instructor instance and add it to the instructors list
        new_instructor = Instructor.Instructor(diver.name, diver.ID, diver.age, employeeID, diver.num_of_dives, diver.union)
        self.instructors.append(new_instructor)

        return new_instructor

    def add_equipment(self, equipmentID, quantity, name):
        # Check if the equipment ID already exists in the club's equipment list
        existing_equipment = next((eq for eq in self.equipment if eq.ID == equipmentID), None)
        if existing_equipment:
            # If the equipment exists, increase its quantity
            existing_equipment.quantity += quantity
        else:
            # If the equipment does not exist, create a new instance and add it to the list
            new_equipment = Equipment.Equipment(equipmentID, quantity, name)
            self.equipment.append(new_equipment)

    def remove_by_shark_attack(self, ID):
        # Check if the ID belongs to a diver
        diver = next((d for d in self.divers if d.ID == ID), None)
        if diver:
            self.divers.remove(diver)
            print(f"Diver with ID {ID} has been killed to a shark attack.... not agein... we will lose our insurance.")
            return

        # Check if the ID belongs to an instructor
        instructor = next((i for i in self.instructors if i.ID == ID), None)
        if instructor:
            self.instructors.remove(instructor)
            print(f"Instructor with ID {ID} has been killed to a shark attack.... not agein... we will lose our insurance.")
            return

        # If the ID does not belong to any diver or instructor
        print(f"No diver or instructor with ID {ID} found in the club.")