import datetime
from Entities.Employee import *
from Entities.Diver import Diver


class Instructor(Employee, Diver):
    def __init__(self, ID, name, age, employeeID, num_of_dives, union, equipment_list = []):
        Employee.__init__(self, ID, name, age, employeeID)  # Explicitly initialize Employee part
        Diver.__init__(self, ID, name, age, union, equipment_list)  # Explicitly initialize Diver part
        self.num_of_dives = num_of_dives
        self.start_date = datetime.date.today()  # Set the start date to today
        self.seniority = self.calculate_seniority()  # Ensure this method is defined
        self.locations = []

    def return_equipments(self, all_equipments):
        for stored_equipment in all_equipments:
            for my_equipment in self.equipment_list:
                if stored_equipment.ID == my_equipment.ID:
                    stored_equipment.quantity = stored_equipment.quantity + my_equipment.quantity
                    my_equipment.quantity = 0
                    break

    def update_seniority(self):
        # Calculate the seniority based on the number of years since the start date
        today = datetime.date.today()
        self.seniority = (today - self.start_date).days // 365

    def calculate_seniority(self):
        # Calculate the seniority based on the number of years since the start date
        today = datetime.date.today()
        return (today - self.start_date).days // 365
