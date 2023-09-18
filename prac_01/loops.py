"""
CP1404 - Practical
Loops
"""

# odd numbers between 1 and 20 with a space between each one.
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()
# count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# print n stars
number_of_stars = int(input("Enter number of stars: "))
for i in range(0, number_of_stars, 1):
    print(end='*')
print()

# print n lines of increasing stars.
print('Increasing Stars')
for i in range(0, number_of_stars, 1):
    print('*' * (i+1))
