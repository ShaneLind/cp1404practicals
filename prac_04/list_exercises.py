"""
CP1404 Practical
List exercises
"""


def main():
    exercise1()
    exercise2()


def exercise1():
    number_of_inputs = 0
    numbers = []
    while number_of_inputs < 5:
        number_of_inputs += 1
        new_number = [int(input(f"Number {number_of_inputs}:"))]
        numbers = numbers + new_number
    smallest_number = min(numbers)
    largest_number = max(numbers)
    average_of_numbers = sum(numbers) / len(numbers)
    print(numbers)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {smallest_number}")
    print(f"The largest number is {largest_number}")
    print(f"The average of the numbers is {average_of_numbers}")


def exercise2():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    user_input = input("Enter Username:")
    if user_input in usernames:
        print("Access Granted")
    else:
        print("Access Denied")


main()
