"""
CP1404 - Practical
Password checker
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    length = len(password)
    if length < MIN_LENGTH or length > MAX_LENGTH:
        return False
    else:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0

        for char in password:
            if char.islower():
                count_lower = count_lower + 1
            elif char.isupper():
                count_upper = count_upper + 1
            elif char.isdigit():
                count_digit = count_digit + 1
            elif SPECIAL_CHARS_REQUIRED:
                for special_char in SPECIAL_CHARACTERS:
                    if char == special_char:
                        count_special = count_special + 1

        if count_lower < 1:
            return False
        elif count_upper < 1:
            return False
        elif count_digit < 1:
            return False
        elif SPECIAL_CHARS_REQUIRED:
            if count_special < 1:
                return False
            else:
                return True
        else:
            return True


main()
