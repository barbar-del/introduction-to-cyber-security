import Diver
from DivingSession import DivingSession
import Instructor


class Diver_Club:
    def __init__(self):
        self.divers = []  # List to hold diver objects
        self.instructors = []  # List to hold instructor objects
        self.diving_sessions = []  # List to hold past DivingSession objects

    def register_diver(self, name, id, diver_rank):
        # Create a new Diver instance and add it to the divers list
        new_diver = Diver(name, id, diver_rank)
        self.divers.append(new_diver)
        return new_diver

    def create_instructor(self, name, id, diver_rank, company_name):
        # Create a new Instructor instance and add it to the instructors list
        new_instructor = Instructor(name, id, diver_rank, company_name)
        self.instructors.append(new_instructor)
        return new_instructor

                    #promote a diver to an instructor
    def promote_to_instructor(self, diver_id, company_name):
        # Find the diver by id, create an Instructor instance, and remove the diver from the divers list
        for diver in self.divers:
            if diver.id == diver_id:
                # Assuming diver_rank is accessible. Adjust as necessary based on your Diver class structure
                new_instructor = Instructor(diver.name, diver.id, diver.diver_rank, company_name)
                self.instructors.append(new_instructor)
                self.divers.remove(diver)  # Remove the diver from the divers list
                return new_instructor
        return None  # Return None if diver not found

    def create_diving_session(self, diving_depth, instructor_name, instructor_id, location):
        # Find the instructor in the club by instructor_id
        instructor = None
        for ins in self.instructors:
            if ins.id == instructor_id:
                instructor = ins
                break
        
        if instructor is None:
            print(f"No instructor found with ID {instructor_id}. Cannot create diving session.")
            return None
        
        # Create a new DivingSession instance
        new_session = DivingSession(diving_depth, instructor_name, instructor_id, location, self)
        
        # Add the new session to the club's list of diving sessions
        self.diving_sessions.append(new_session)
        
        return new_session
