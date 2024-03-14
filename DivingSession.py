import Instructor

# The DivingSession class is used to represent a diving session, which is a gathering of divers and instructors at a specific location to dive to a certain depth.
# The class has the following attributes: diving_depth, instructor_name, instructor_id, location, diver_club, and registered_equipment.
#registered_equipment is a list of Register_equipment instances, each of which holds a participant (a diver or an instructor) and the equipment they have registered for the session.
#add stitic int to the class to keep track of the number of sessions created
class DivingSession:
    static_id = 0
    def __init__(self, diving_depth, instructor: Instructor, location, divers):
        self.id = DivingSession.static_id
        self.static_id += 1
        self.diving_depth = diving_depth
        self.instructor = instructor
        self.location = location
        self.divers = divers 

#add a participant to the session, check if the participant is already in the session's registered equipment, if not check if the participant exists in the Diver_Club.
# If the participant is found, create a new Register_equipment instance and add it to the session's registered_equipment list.

    def add_participant(self, participant_id, equipment):
        return

    def add_instructor(self, participant_id):
        return
