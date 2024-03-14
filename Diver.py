from enum import Enum
import Person
import Equipment
import DivingSession
import pickle

# Define an enumeration for diver ranks
class Rank(Enum):
    Beginner = 1
    Intermediate = 2
    Advanced = 3
    Expert = 4
    
class Diver(Person.Person):
    def __init__(self, name, ID, age, num_of_dives, union):
        super().__init__(name, ID, age)  # Call the constructor of the parent class
        self.num_of_dives = num_of_dives
        self.union = union
        self.equipment_list = []  # List to store the diver's equipment
        self.rank = self.check_rank()  # Call check_rank to set the initial rank

    # Function to check the amount of dives the diver has done and assign a rank accordingly
    # 0-5 dives = beginner, 6-10 dives = intermediate, 11-15 dives = advanced, 15+ dives = expert
    def check_rank(self):
        if self.num_of_dives >= 16:
            self.rank = Rank.Expert
            return
        elif self.num_of_dives >= 11:
            self.rank = Rank.Advanced
            return
        elif self.num_of_dives >= 6:
            self.rank = Rank.Intermediate
            return
        else:
            self.rank = Rank.Beginner
            return

    def increase_rank(self):
        self.num_of_dives += 1  # Increment the number of dives
        self.check_rank()  # Update the rank based on the new number of dives

    def add_equipment(self, equipment: Equipment.Equipment):
        if equipment.quantity > 1:
            # Check if the equipment ID already exists in the equipment_list
            existing_equipment = next((eq for eq in self.equipment_list if eq.ID == equipment.ID), None)
            if existing_equipment:
                # If the equipment exists, increase its quantity in the list and decrease the original equipment's quantity
                existing_equipment.quantity += 1
                equipment.quantity -= 1
            else:
                # If the equipment does not exist, create a new instance with quantity 1 and append it to the list
                new_equipment = Equipment.Equipment(equipment.ID, 1, equipment.name)
                self.equipment_list.append(new_equipment)
                equipment.quantity -= 1

    def add_location_to_instructor(self, instructor_id, location):
        # Find the instructor in the club by ID
        instructor = next((i for i in self.instructors if i.ID == instructor_id), None)
        if instructor:
            # Add the location to the instructor's locations list
            instructor.locations.append(location)
            print(f"Location {location} added to instructor with ID {instructor_id}.")
        else:
            print(f"No instructor found with ID {instructor_id}.")

    def create_diving_session(self, diving_depth, instructor_id, location):
        # Find the instructor in the club by ID
        instructor = next((i for i in self.instructors if i.ID == instructor_id), None)
        if instructor is None:
            print(f"No instructor found with ID {instructor_id}.")
            return None

        # Check if the instructor knows the location
        if location not in instructor.locations:
            print(f"Instructor with ID {instructor_id} does not know the location {location}.")
            return None

        # Create a new DivingSession instance
        new_session = DivingSession.DivingSession(diving_depth, instructor, location, self.equipment)
        self.diving_sessions.append(new_session)
        return new_session
    
    
    def serialize(self):
        with open('diver.pickle', 'wb') as f:
            pickle.dump(Diver, f)

    @staticmethod
    def deserialize():
        with open('diver.pickle', 'rb') as f:
            return pickle.load(f)