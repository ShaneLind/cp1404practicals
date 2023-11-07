"""
CP1404 Practical - Project class
"""

import datetime


class Project:
    """Project Class """

    def __init__(self, name="", start_date="00/00/00", priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise a project instance"""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return string version of project"""
        return f"{self.name},{self.start_date},{self.priority},{self.cost_estimate},{self.completion_percentage}"

    def __lt__(self, other):
        """Compare projects based on their date"""
        return self.start_date < other.start_date
