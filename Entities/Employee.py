from Entities.Person import Person


class Employee(Person):
    def __init__(self, ID, name, age, employee_id):
        Person.__init__(self, ID, name, age)  # Call Person's __init__ directly
        self.employeeID = employee_id
        self.seniority = 0
        self.start_date = None  # ensure that the start_date is a datetime.date object
