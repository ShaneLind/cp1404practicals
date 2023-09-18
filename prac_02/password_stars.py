"""
Shane Lind
Password check program
"""
min_length = 3
password = input("Enter a password: ")

while True:
    length = len(password)
    if length >= min_length:
        print('*' * length)
        break
    else:
        print("Invalid word length (too short)")
        password = input("Enter a password: ")
