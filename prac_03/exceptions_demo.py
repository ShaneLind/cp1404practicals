"""
CP1404 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    is_valid_input = False
    while not is_valid_input:
        try:
            denominator = int(input("Enter the denominator: "))
            if denominator == 0:
                print("Cannot divide by zero!")
            else:
                is_valid_input = True
                fraction = numerator / denominator
                print(fraction)
        except ValueError:
            print("Invalid (not an integer)")

print("Finished.")

# 1. When will a ValueError occur?
# Answer: It will occur when either the numerator or denominator are not valid numbers

# 2. When will a ZeroDivisionError occur?
# Answer: It will occur when the denominator is a zero

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Answer: Ask the user for another input when entering denominator as zero, until denominator is a valid number
