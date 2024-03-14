import Instructor
import Diver
import Equipment

class DivingSession:
    # Static variable to keep track of the next ID for a new DivingSession instance
    static_id = 0

    def __init__(self, diving_depth, instructor: Instructor.Instructor, location, club_equipment):
        # Assign a unique ID to the new DivingSession instance
        self.id = DivingSession.static_id
        DivingSession.static_id += 1

        self.diving_depth = diving_depth
        self.instructor = instructor
        self.location = location
        self.divers = []  # List to store divers registered for this diving session
        self.registered_equipment = []  # List to store equipment registered for this diving session
        self.club_equipment = club_equipment  # Reference to the club's equipment list

    def add_diver(self, diver: Diver.Diver):
        # Add a diver to the diving session if not already added
        if diver not in self.divers:
            self.divers.append(diver)

    def check_instructor_knowledge(self):
        # Check if the instructor knows the location for the diving session
        if self.location not in self.instructor.locations:
            raise Exception("Instructor does not know the location. Please change the instructor or the location.")

    def add_equipment(self, equipment_id, quantity):
        # Find the equipment in the club's equipment list
        club_equipment = next((eq for eq in self.club_equipment if eq.ID == equipment_id), None)
        if club_equipment and club_equipment.quantity >= quantity:
            # Check if the equipment ID already exists in the session's equipment list
            session_equipment = next((eq for eq in self.registered_equipment if eq.ID == equipment_id), None)
            if session_equipment:
                # If the equipment exists in the session, increase its quantity
                session_equipment.quantity += quantity
            else:
                # If the equipment does not exist in the session, create a new instance and add it to the list
                new_equipment = Equipment.Equipment(equipment_id, quantity, club_equipment.name)
                self.registered_equipment.append(new_equipment)
            # Decrease the quantity in the club's equipment list
            club_equipment.quantity -= quantity
        else:
            raise Exception(f"Not enough quantity of equipment with ID {equipment_id} available in the club.")

    def end_session(self):
        # Return the equipment to the club
        for equipment in self.registered_equipment:
            # Find the corresponding equipment in the club's equipment list
            club_equipment = next((eq for eq in self.club_equipment if eq.ID == equipment.ID), None)
            if club_equipment:
                club_equipment.quantity += equipment.quantity  # Increase the quantity in the club
            else:
                print(f"Equipment with ID {equipment.ID} not found in the club.")
        self.registered_equipment = []  # Clear the registered equipment list