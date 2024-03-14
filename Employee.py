import datetime
import Person

class Employee(Person):
    def __init__(self, name, ID, age, employeeID, seniority, start_date):
        super().__init__(name, ID, age)
        self.employeeID = employeeID
        self.seniority = seniority
        if isinstance(start_date, datetime.date):
            self.start_date = start_date
        else:
            raise ValueError("start_date must be a datetime.date object")
        
        