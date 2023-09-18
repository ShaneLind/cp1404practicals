"""
CP1404 - Practical
Menus
"""

name = (input("Enter name: "))
MENU = """H - Say Hello
G - Say Goodbye
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print(f'Hello {name}')
    elif choice == "G":
        print(f'Goodbye {name}')
    else:
        print('Invalid Choice')

    print(MENU)
    choice = input(">>> ").upper()

print('Finished')
