"""
CP1404 Practical - Guitar class user program
"""

from guitar import Guitar


def main():
    guitar_collection = []
    in_file = open('guitars.csv', 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar_info = Guitar(parts[0], parts[1], parts[2])
        guitar_collection.append(guitar_info)
    in_file.close()

    for guitar_info in guitar_collection:
        print(guitar_info)


main()
