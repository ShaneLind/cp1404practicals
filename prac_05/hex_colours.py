"""
CP1404Practical
hexadecimal colour codes in a dictionary
"""

colour_to_code = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                "Aqua": "#00ffff", "Aureolin": "#fdee00", "Brilliant Rose": "#ff55a3"}

print(colour_to_code)

colour_code = input("Enter colour name: ").title()
while colour_code != "":
    try:
        print(colour_code, "is", colour_to_code[colour_code])
    except KeyError:
        print("Invalid colour name")
    colour_code = input("Enter short state: ").title()
