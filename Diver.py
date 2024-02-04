from enum import Enum

class Rank(Enum):
    Beginner = 1
    Intermediate = 2
    Advanced = 3
    Expert = 4

class Diver:
    def __init__(self, name, id, diver_rank):
        self.name = name
        self.id = id
        # Ensure diver_rank is an instance of Rank
        if isinstance(diver_rank, Rank):
            self.diver_rank = diver_rank
        else:
            raise ValueError("diver_rank must be an instance of Rank Enum")

    def get_diver_rank(self):
        """Return the diver's rank."""
        return self.diver_rank

    def set_diver_rank(self, diver_rank):
        """Update the diver's rank, if it's an instance of Rank."""
        if isinstance(diver_rank, Rank):
            self.diver_rank = diver_rank
        else:
            print(f"Invalid rank: {diver_rank}. Rank must be an instance of Rank Enum.")
