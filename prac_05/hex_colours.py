"""
CP1404Practical
hexadecimal colour codes in a dictionary
"""

COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                "Aqua": "#00ffff", "Aureolin": "#fdee00", "Brilliant Rose": "#ff55a3"}

print(COLOUR_TO_CODE)
COLOUR_TO_CODE = {colour_code.lower(): hex_code for colour_code, hex_code in COLOUR_TO_CODE.items()}

colour_code = input("Enter colour name: ").lower()
while colour_code != "":
    try:
        print(colour_code, "is", COLOUR_TO_CODE[colour_code])
    except KeyError:
        print("Invalid colour name")
    colour_code = input("Enter short state: ").lower()
