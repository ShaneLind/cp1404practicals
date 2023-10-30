"""
CP1404 Practical - Client code to use the Guitar class.
"""
from guitar import Guitar

my_guitars = []

print("My Guitars!")
name = input("Name: ")
while not name == "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    my_guitars += [Guitar(name, year, cost)]
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")

print("These are my guitars:")
for i, guitar in enumerate(my_guitars, 1):
    vintage_string = "(vintage)" if Guitar.is_vintage(guitar) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
