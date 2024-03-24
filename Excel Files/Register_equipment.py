from enum import Enum
import Equipment
import Diver
import Instructor

# list that hold one person( a diver or an instructor) and the equipment that he has.
class Register_equipment:
    def __init__(self, participant, equipment_list):
        if not isinstance(participant, (Diver, Instructor)):
            raise ValueError("Participant must be a Diver or an Instructor")
        self.participant = participant
        self.equipment_list = equipment_list  # List of Equipment enums
#add equipment to the list
    def add_equipment(self, equipment):
        if equipment in Equipment:
            self.equipment_list.append(equipment)
        else:
            print(f"{equipment} is not a valid piece of equipment.")
#remove equipment from the list
    def remove_equipment(self, equipment):
        if equipment in self.equipment_list:
            self.equipment_list.remove(equipment)
        else:
            print(f"{equipment} is not in the equipment list.")