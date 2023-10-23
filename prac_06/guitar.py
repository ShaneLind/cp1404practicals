"""
CP1404 Practical - Guitar class.
Expected time = 40 minutes
Actual time = 35 minutes
"""


class Guitar:

    def __init__(self, name="", year=0, cost=0):
        """Initialise a guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        current_year = 2023
        age = current_year - self.year
        return age

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False
