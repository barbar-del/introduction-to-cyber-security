import Diver
from DivingSession import DivingSession
import Instructor


class Diver_Club:
    def __init__(self,club_name):
        self.name=club_name
        self.divers = []  # List to hold diver objects
        self.instructors = []  # List to hold instructor objects
        self.diving_sessions = []  # List to hold past DivingSession objects


#check if the diver is already registered, if not create a new diver and add it to the divers list
    def register_diver(self, name, id, diver_rank):
        # Create a new Diver instance and add it to the divers list
        check = self.checkForDiver(id, name, diver_rank)
        if check == True:
            raise ValueError("the diver is already registered")
        new_diver = Diver(name, id, diver_rank)
        self.divers.append(new_diver)
        
        
#check if the instructor is already registered, if not create a new instructor and add it to the instructors list
    def create_instructor(self, name, id, diver_rank, company_name):
        # Create a new Instructor instance and add it to the instructors list
        if self.checkForDiver(id, name, diver_rank):
            raise ValueError("the instructoe is already registered")
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
        raise ValueError("cant find the diver to promote to instructor")
    
    
#creating a new diving session. u need the instructor id to create a new session.
#once the sesion is created, we need to manualy add the participants to the session and there equipment (will be done in the gui)
    def create_diving_session(self, diving_depth, instructor_name, instructor_id, location):
        # Find the instructor in the club by instructor_id
        instructor = None
        for ins in self.instructors:
            if ins.id == instructor_id:
                instructor = ins
                break
        
        if instructor is None:
            raise ValueError("cant find the instructor in the club that maches the id provided")
        
        # Create a new DivingSession instance
        new_session = DivingSession(diving_depth, instructor_name, instructor_id, location, self)
        
        # Add the new session to the club's list of diving sessions
        self.diving_sessions.append(new_session)
        
        return new_session

#check if the diver is already registered in the club
    def checkForDiver(self, id, name, diver_rank):
        
        for diver in self.divers:
            if diver.id == id:
                return True
        for instructor in self.instructors:
            if instructor.id == id:
                return True
        return False
