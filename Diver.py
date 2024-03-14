from enum import Enum
import Person
import Equipment

class Rank(Enum):
    Beginner = 1
    Intermediate = 2
    Advanced = 3
    Expert = 4
#the diver class get an id, name and rank, check if the rank is an instance of the Rank enum and if so  crate the diver
class Diver(Person):
    def __init__(self, name, ID, age, num_of_dives, rank, union, equipment):
        super().__init__(name, ID, age)
        self.num_of_dives = num_of_dives
        self.union = union
        self.equipment = equipment
        # Ensure diver_rank is an instance of Rank
        if isinstance(rank, Rank):
            self.rank = rank
        else:
            raise ValueError("The rank must be an instance of Rank Enum")

    def get_diver_rank(self):
        """Return the diver's rank."""
        return self.diver_rank

    def set_diver_rank(self, diver_rank):
        """Update the diver's rank, if it's an instance of Rank."""
        if isinstance(diver_rank, Rank):
            self.diver_rank = diver_rank
        else:
            print(f"Invalid rank: {diver_rank}. Rank must be an instance of Rank Enum.")

    def update_rank(self):
        return
    
    def buy_equipment(self, equipments: Equipment):
        return
