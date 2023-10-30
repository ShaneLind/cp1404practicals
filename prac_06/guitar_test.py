"""
CP1404 Practical - Test code to evaluate the Guitar class.
"""

from guitar import Guitar

first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
second_guitar = Guitar("Another Guitar", 2013, 10000)

print(f"Gibson L-5 CES get_age() - Expected 101. Got {Guitar.get_age(first_guitar)}")
print(f"Gibson L-5 CES get_age() - Expected 10. Got {Guitar.get_age(second_guitar)}")

print(f"Gibson L-5 CES is_vintage() - Expected True. Got {Guitar.is_vintage(first_guitar)}")
print(f"Gibson L-5 CES is_vintage() - Expected False. Got {Guitar.is_vintage(second_guitar)}")