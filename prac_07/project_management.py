"""
CP1404 Practical
Estimated Time: 90 minutes
Actual Time: 180 minutes
"""
from project import Project
import datetime

MENU = """- (L)oad projects
- (S)ave projects
- (D)isplay projects
- (F)ilter projects by date
- (A)dd new project
- (U)pdate project
- (Q)uit
"""


def main():
    """Perform different functions based on user input"""
    project_information = read_from_file()
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "L":
            project_information = read_from_file()
            print("Projects have been loaded")

        elif choice == "S":
            save_to_file(project_information)
            print("Projects have been saved")

        elif choice == "D":
            project_information = display_project_information(project_information)

        elif choice == "F":
            filtered_project_information = []
            date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            for project in project_information:
                if filter_date <= project.start_date:
                    filtered_project_information += [project]
            display_project_information(filtered_project_information)

        elif choice == "A":
            new_project = add_new_project(project_information)
            project_information.append(new_project)
            print(f"Project: '{new_project.name}, "
                  f"start: {new_project.start_date}, "
                  f"priority = {new_project.priority}, "
                  f"estimate: ${new_project.cost_estimate}, "
                  f"completion: {new_project.completion_percentage}%' has been added")

        elif choice == "U":
            project_information = display_project_information(project_information)
            print("Enter the number of a project to modify its completion percentage and priority.")
            project_number = int(input("Project Number: "))
            print(f"{project_information[project_number - 1].name}, "
                  f"start: {project_information[project_number - 1].start_date}, "
                  f"priority = {project_information[project_number - 1].priority}, "
                  f"estimate: ${project_information[project_number - 1].cost_estimate}, "
                  f"completion: {project_information[project_number - 1].completion_percentage}%")

            user_input_completion_percentage = input("New Completion Percentage: ")
            if user_input_completion_percentage != "":
                project_information[project_number - 1].completion_percentage = user_input_completion_percentage
            user_input_priority = input("New Priority: ")
            if user_input_priority != "":
                project_information[project_number - 1].priority = user_input_priority

        else:
            print('Invalid menu choice')

        print(MENU)
        choice = input(">>> ").upper()

    save_to_file(project_information)  # save to file when quitting
    print("The file has been saved")
    print("The program has ended")


def display_project_information(project_information):
    """Print a sorted and formatted list of the projects"""
    entry_number = 0
    sorted_project_information = sorted(project_information)
    for project in sorted_project_information:
        entry_number += 1
        formatted_date = project.start_date.strftime('%d/%m/%Y')
        print(f"{entry_number} {project.name}, start: {formatted_date}, priority = {project.priority}, "
              f"estimate: ${project.cost_estimate}, completion: {project.completion_percentage}%")
    return sorted_project_information


def read_from_file():
    """Read project information from the file specified by the user"""
    project_information = []
    print("The name of the file is:")
    file_name = input(">>>")

    in_file = open(file_name, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split('\t')
        project_information.append(Project(parts[0], parts[1], parts[2], parts[3], parts[4]))
    in_file.close()
    return project_information


def save_to_file(project_list):
    """save project information to the file specified by the user"""
    print("The name of the file is:")
    file_name = input(">>>")

    out_file = open(file_name, 'w')
    print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
    for line in project_list:
        parts = [line.name, str(line.start_date), line.priority, line.cost_estimate, line.completion_percentage]
        output = '\t'.join(parts)
        print(output, file=out_file)
    out_file.close()


def add_new_project(project_information):
    """Get user input to add new project"""
    print("Add new project:")
    new_name = input("Project name: ")
    new_start_date = input("Start date: ")
    new_priority = input("Project priority: ")
    new_cost_estimate = input("Project cost estimate: ")
    new_completion_percentage = input("Project completion percentage: ")
    new_project = Project(new_name, new_start_date, new_priority, new_cost_estimate, new_completion_percentage)
    return new_project


main()
