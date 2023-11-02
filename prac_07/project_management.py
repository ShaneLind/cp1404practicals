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
            project_information = read_from_file()
            for project in project_information:
                print(project)

        elif choice == "S":
            print("Option S")
            save_to_file(project_information)
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
    """Read project information from the file specified by the user"""
    project_information = []

    # print("The name of the file is:")
    # file_name = input(">>>")

    # for testing
    file_name = "projects.txt"

    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project_information.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    in_file.close()

    return project_information


def save_to_file(project_list):
    """save project information to the file specified by the user"""
    # print("The name of the file is:")
    # file_name = input(">>>")

    # for testing
    file_name = "test.txt"

    out_file = open(file_name, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for line in project_list:
        parts = [line.name, line.start_date, line.priority, line.cost_estimate, line.completion_percentage]
        output = '\t'.join(parts)
        print(output, file=out_file)
    out_file.close()


main()
