"""
CP1404 Practical
Quick picks
"""
import random

number_of_picks = int(input("How many quick picks?:"))
counter = 0
random_numbers = []
minimum_range = 1
maximum_range = 45
while counter < number_of_picks:
    counter += 1
    for index1 in range(0, 6):
        random_number = random.randint(minimum_range, maximum_range)
        valid_number = False
        while not valid_number:
            if random_number in random_numbers:
                random_number = random.randint(1, 45)
                # print("Duplicate number")
            else:
                valid_number = True
        random_numbers += [random_number]

    line = sorted(random_numbers)
    random_numbers = []
    for index2 in range(0, 6):
        if len(str(line[index2])) == 1:
            print(" " + str(line[index2]), end=' ')
        else:
            print(str(line[index2]), end=' ')
    print(" ")
