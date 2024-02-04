import Register_equipment

class DivingSession:
    def __init__(self, diving_depth, instructor_name, instructor_id, location, diver_club):
        self.diving_depth = diving_depth
        self.instructor_name = instructor_name
        self.instructor_id = instructor_id
        self.location = location
        self.diver_club = diver_club  # Reference to the Diver_Club instance
        self.registered_equipment = []  # List of Register_equipment instances

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
