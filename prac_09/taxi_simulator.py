"""
CP1404 Practical
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = """q)uit, c)hoose taxi, d)rive"""


def main():
    """Take user input to choose and drive a taxi"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    bill = 0.00
    print("Let's Drive!")
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            print("Taxis Available:")
            display_available_taxis(taxis)
            taxi_choice = int(input("Choose Taxi:  "))
            if 0 <= taxi_choice <= 2:
                current_taxi = taxi_choice
            else:
                print("Invalid Taxi Choice")

        elif choice == "D":

            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = float(input("Drive How Far? (km): "))
                taxis[current_taxi].start_fare()
                taxis[current_taxi].drive(distance)
                current_bill = taxis[current_taxi].get_fare()
                bill += current_bill
                print(f"Your {taxis[current_taxi].name} trip cost you ${current_bill:.2f}")

        else:
            print("Invalid menu choice")

        print(f"Bill to date: ${bill:.2f}")

        print(MENU)
        choice = input(">>> ").upper()

    print(f"Total Trip Cost: ${bill:.2f}")
    print("Taxis are now:")
    display_available_taxis(taxis)


def display_available_taxis(taxis):
    """Print the available taxis"""
    taxi_number = 0
    for taxi in taxis:
        print(f"{taxi_number} - {taxi.__str__()}")
        taxi_number += 1


main()
