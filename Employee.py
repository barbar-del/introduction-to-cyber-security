import datetime
import pickle
import Person

class Employee(Person):
    def __init__(self, name, ID, age, employeeID, ):
        super().__init__(name, ID, age)
        self.employeeID = employeeID
        self.seniority = 0
        #insure that the start_date is a datetime.date object
        self.start_date = None
    
    
    def serialize(self):
        with open('employee.pickle', 'wb') as f:
            pickle.dump(Employee, f)

    @staticmethod
    def deserialize():
        with open('employee.pickle', 'rb') as f:
            return pickle.load(f)