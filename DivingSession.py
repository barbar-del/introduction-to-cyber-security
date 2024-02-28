import Register_equipment


# The DivingSession class is used to represent a diving session, which is a gathering of divers and instructors at a specific location to dive to a certain depth.
# The class has the following attributes: diving_depth, instructor_name, instructor_id, location, diver_club, and registered_equipment.
#registered_equipment is a list of Register_equipment instances, each of which holds a participant (a diver or an instructor) and the equipment they have registered for the session.
#add stitic int to the class to keep track of the number of sessions created
class DivingSession:
    static_id = 0
    def __init__(self, diving_depth, instructor_name, instructor_id, location, diver_club):
        self.id = DivingSession.static_id
        self.static_id += 1
        self.diving_depth = diving_depth
        self.instructor_name = instructor_name
        self.instructor_id = instructor_id
        self.location = location
        self.diver_club = diver_club  # Reference to the Diver_Club instance
        self.registered_equipment = []  # List of Register_equipment instances

#add a participant to the session, check if the participant is already in the session's registered equipment, if not check if the participant exists in the Diver_Club.
# If the participant is found, create a new Register_equipment instance and add it to the session's registered_equipment list.

    def add_participant_equipment(self, participant_id, equipment):
        # First, check if the participant is already in the session's registered equipment
        for reg_eq in self.registered_equipment:
            if reg_eq.participant.id == participant_id:
                reg_eq.add_equipment(equipment)
                return

        # If not already in the session, check if the participant exists in the Diver_Club
        participant = self.find_participant_in_club(participant_id)
        if participant:
            new_reg = Register_equipment(participant=participant, equipment_list=[equipment])
            self.registered_equipment.append(new_reg)
        else:
            print(f"Error: Participant with ID {participant_id} does not exist in the club.")

    def find_participant_in_club(self, participant_id):
        # Check both divers and instructors in the club for the participant
        for diver in self.diver_club.divers:
            if diver.id == participant_id:
                return diver
        for instructor in self.diver_club.instructors:
            if instructor.id == participant_id:
                return instructor
        # Return None if the participant is not found
        return None
