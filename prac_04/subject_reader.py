"""
CP1404 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read data form list and display subject details"""
    data = get_data()
    print(data)
    get_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    nested_list = []
    for line in input_file:
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")
        nested_list += [parts]
    input_file.close()
    return nested_list


def get_details(data):
    """Decode list and print subject details"""
    for detail in data:
        subject_details = detail
        print(f"{subject_details[0]} is taught by {subject_details[1]} and has {subject_details[2]} students")


main()
