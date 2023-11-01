"""
CP1404 Practical - Guitar class user program
"""

from guitar import Guitar


def main():
    guitar_collection = []
    guitar_output = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar_info = Guitar(parts[0], parts[1], parts[2])
        guitar_output.append(line.strip())
        guitar_collection.append(guitar_info)
    in_file.close()

    guitar_collection.sort()
    for guitar_info in guitar_collection:
        print(guitar_info)

    out_file = open("guitars.csv", 'w')
    new_guitar = ','.join(get_new_guitar())
    guitar_output.append(new_guitar)
    for index in guitar_output:
        print(index, file=out_file)
    out_file.close()


def get_new_guitar():
    print("**Add a new song**")
    new_guitar_name = input("New guitar name: ")
    new_guitar_year = input("When was the new guitar released?: ")
    new_guitar_cost = input("What is the price of the new guitar?: ")
    new_guitar = new_guitar_name, new_guitar_year, new_guitar_cost
    return new_guitar


main()
