"""
Emails
Estimate: 30 minutes
Actual: 50 minutes
"""


def main():
    email = str(input("Email: "))
    email_to_name = {}

    while email != "":
        name = decipher_name(email)

        print(f"Is your name {name}?")
        answer = input("(Y/N): ").lower()
        if answer == 'y' or answer == "":
            print(f"Name: {name}")
        elif answer == 'n':
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")

    keys = list(email_to_name.keys())
    max_length = max(len(key) for key in keys)
    for email, name in email_to_name.items():
        print(f"Email: {email:{max_length + 1}}- Name: {name:1}")


def decipher_name(email):
    """Decipher user's name"""
    sections = email.split('@')
    if '.' in sections[0]:
        name = ' '.join(sections[0].split('.'))
    else:
        name = sections[0]
    return name


main()
