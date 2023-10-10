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
    print(email)
    print(first_name, last_name[0])

    email = str(input("Email: "))


