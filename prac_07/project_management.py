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
            print("Projects have been loaded")

        elif choice == "S":
            try:
                save_to_file(project_information)  # prevented error using try statement
                print("Projects have been saved")
            except UnboundLocalError:
                print("Data has not been loaded")
        elif choice == "D":
            try:
                for project in project_information:
                    print(project)
            except UnboundLocalError:
                print("Data has not been loaded")
        elif choice == "F":
            print("Option F")
        elif choice == "A":
            print("Option A")
            new_project = add_new_project(project_information)
            project_information.append(new_project)
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


def add_new_project(project_information):
    print("Add new project:")
    # new_name = input("Project name: ")
    # new_start_date = input("Start date: ")
    # new_priority = input("Project priority: ")
    # new_cost_estimate = input("Project cost estimate: ")
    # new_completion_percentage = input("Project completion percentage: ")
    # new_project = Project(new_name, new_start_date, new_priority, new_cost_estimate, new_completion_percentage)

    # for testing
    new_project = Project("That thing that happened", "17/3/2004", "5", "777.77", "27")

    return new_project


main()
