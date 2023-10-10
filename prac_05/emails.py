"""
Emails
Estimate: 30 minutes
Actual: 50 minutes
"""

email = str(input("Email: "))
email_to_name = {}

while email != "":
    # decipher user's name
    sections = email.split('@')
    if '.' in sections[0]:
        name = ' '.join(sections[0].split('.'))
    else:
        name = str(sections[0])

    # check if user's name is correct
    print(f"Is your name {name}?")
    answer = input("(Y/N): ").lower()
    if answer == 'y' or answer == "":  # if name is correct
        print(f"Name: {name}")  # return user's name
    elif answer == 'n':  # if name is correct
        name = str(input("Name: "))  # get user to input correct name
    email_to_name[email] = name  # update dictionary
    email = str(input("Email: "))  # ask for next input

# print dictionary
keys = list(email_to_name.keys())
max_length = max(len(key) for key in keys)
for email, name in email_to_name.items():
    print(f"Email: {email:{max_length + 1}}- Name: {name:1}")
