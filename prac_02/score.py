"""
CP1404 - Practical
Program to determine score classification
"""
import random


def main():
    """Get user input as score and prints the score's classification"""
    score = float(input("Enter score: "))
    result = classify_the_score(score)
    print(f"user score is {result}")

    random_score = random.randint(0, 100)
    print(f"Random score is: {random_score}")
    result = classify_the_score(random_score)
    print(f"random score is {result}")


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


main()
