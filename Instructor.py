import Employee
import Diver
import Equipment

# Assuming the Rank Enum and Diver class are defined as previously
#create the instructor class that inherits from the diver class
class Instructor(Employee, Diver):
    def __init__(self, name, ID, age, employeeID, seniority, start_date, num_of_dives, rank, union, equipment: Equipment, locations):
        super().__init__(name, ID, age, employeeID, seniority, start_date, num_of_dives, rank, union, equipment)
        self.locations = locations

    def get_fired(self):
        return
    
    def update_seniority(self):
        return
