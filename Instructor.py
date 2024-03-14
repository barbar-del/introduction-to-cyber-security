import datetime
import Employee
import Diver

class Instructor(Employee.Employee, Diver.Diver):
    def __init__(self, name, ID, age, employeeID, num_of_dives, union):
        super().__init__(name, ID, age, employeeID, num_of_dives, union)
        self.start_date = datetime.date.today()  # Set the start date to today
        self.seniority = self.calculate_seniority()
        self.locations = []
        

    def calculate_seniority(self):
        # Calculate the seniority based on the number of years since the start date
        today = datetime.date.today()
        return (today - self.start_date).days // 365

    def quit_club(self, instructor_list):
        # Remove the instructor from the list of instructors
        instructor_list.remove(self)
