import datetime
import Person

class Employee(Person):
    def __init__(self, name, ID, age, employeeID, ):
        super().__init__(name, ID, age)
        self.employeeID = employeeID
        self.seniority = 0
        #insure that the start_date is a datetime.date object
        self.start_date = None
        