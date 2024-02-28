from enum import Enum

from Diver import Diver

# Assuming the Rank Enum and Diver class are defined as previously
#create the instructor class that inherits from the diver class
class Instructor(Diver):  # Inherits from Diver
    def __init__(self, name, id, diver_rank, company_name):
        super().__init__(name, id, diver_rank)  # Initialize parent class properties
        self.company_name = company_name  # Additional property for Instructor

    def get_company_name(self):
        """Return the instructor's company name."""
        return self.company_name