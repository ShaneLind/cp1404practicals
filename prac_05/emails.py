"""
Emails
Estimate: 30 minutes
Actual: ?? minutes
"""

email = str(input("Email: "))
name = email.split('.')
first_name = name[0]
last_name = name[1].split('@')
while email != "":
    # print(email)
    print(f"Is your name {first_name} {last_name[0]}?")
    answer = input("(Y/N): ").lower()
    if answer == 'y' or answer == "":
        print(f"Name: {first_name} {last_name[0]}")
    elif answer == 'n':
        email = str(input("Email: "))

    email = str(input("Email: "))
