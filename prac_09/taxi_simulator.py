"""
CP1404 Practical
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """ ??????????    """
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            print("Option C")
        elif choice == "Q":
            print("Option Q")
        else:
            print('Invalid menu choice')

        print(MENU)
        choice = input(">>> ").upper()