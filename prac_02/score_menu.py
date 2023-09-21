"""
Shane Lind
Score menu
"""


def main():
    """Get user input to either get and check if a score is valid, print the classification of the score
     or display a number of asterisks equal to the score"""
    menu = """G - Get a valid score (0-100)
P - Print result
S - Display stars
Q - Quit"""
    print(menu)
    score = float(input("Enter score: "))
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            print(menu)
        elif choice == "P":
            result = classify_the_score(score)
            print(f"Score is {result}")
            print(menu)
        elif choice == "S":
            print_asterisks(score)
            print(menu)
        else:
            print("Invalid Name")

        choice = input(">>> ").upper()
        print(menu)
    print("Good Bye")


def get_valid_score():
    """Get a valid score"""
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
        score = input("Enter score: ")
    else:
        print("Score is valid")
    return score


def classify_the_score(score):
    """Classify score"""
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def print_asterisks(score):
    """Print the as many asterisks as the value of the score"""
    number_of_asterisks = round(score)
    print(f"Number of Asterisks: {number_of_asterisks}")
    print('*' * number_of_asterisks)


main()
