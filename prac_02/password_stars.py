"""
Shane Lind
Password check program
"""


def main():
    """Get user choice to record password or print password length"""
    MENU = """G - Get Password
P - Print Password Length in Asterisks
Q - Quit"""
    print(MENU)
    password = ""
    min_length = 3
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            password = get_password(min_length)
            print(MENU)
        elif choice == "P":
            print_asterisks(password)
            print(MENU)
        else:
            print("Invalid Name")
            password = get_password(min_length)
        choice = input(">>> ").upper()
        print(MENU)


def get_password(min_length):
    """ Get user input as password and check if it is of valid length"""
    password = input("Enter a password: ")
    while len(password) < min_length:
        print("Invalid Name (too short)")
        password = input("Enter a password: ")
    return password


def print_asterisks(password):
    """Print the length of password as asterisks"""
    print('*' * len(password))


main()
