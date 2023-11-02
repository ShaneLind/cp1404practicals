"""
CP1404 Practical
Estimated Time: 90mins
Actual Time: ???mins
"""
from project import Project

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            print("Option L")
            read_from_file()
        elif choice == "S":
            print("Option S")
        elif choice == "D":
            print("Option D")
        elif choice == "F":
            print("Option F")
        elif choice == "A":
            print("Option A")
        elif choice == "U":
            print("Option U")
        else:
            print('Invalid menu choice')

        print(MENU)
        choice = input(">>> ").upper()


def read_from_file():
    """Read information from the file specified by the user"""
    project_list = []

    # get user input file name
    # print("The name of the file is:")
    # file_name = input(">>>")

    # for testing
    file_name = "projects.txt"

    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project_list.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    in_file.close()

    for project in project_list:
        print(project)


main()
