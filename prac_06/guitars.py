"""
CP1404 Practical - Client code to use the Guitar class.
"""
from guitar import Guitar

my_guitars = []

print("My Guitars!")
name = input("Name: ")
while not name == "":
    year = input("Year: ")
    cost = input("Cost: ")
    my_guitars += [name, year, cost]
    print(f"{name} ({year}) : ${cost} added.")
    name = input("Name: ")

# Left for testing
# my_guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
# my_guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
# my_guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))

print("These are my guitars:")
for i, guitar in enumerate(my_guitars, 1):
    vintage_string = "(vintage)" if Guitar.is_vintage(guitar) else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
