"""
CP1404Practical
hexadecimal colour codes in a dictionary
"""

NAME_TO_CODE = {"Absolute Zero": "#0048ba"}
print(NAME_TO_CODE)

colour_code = input("Enter colour name: ")
while colour_code != "":
    try:
        print(colour_code, "is", NAME_TO_CODE[colour_code])
    except KeyError:
        print("Invalid colour name")
    colour_code = input("Enter short state: ")
