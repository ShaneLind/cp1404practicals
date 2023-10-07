"""
CP1404 Practical
Files
"""

# 1. Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.
# Remember to close your file.

# try:
#     user_name = input("What is your name?: ")
#     out_file = open("name.txt", 'w')
#     print(user_name, file=out_file)
# except FileNotFoundError:
#     print("name.txt not found")
# finally:
#     out_file.close()  # no problem with potential undefined variable

# 2. (In the same file, but as if it were a separate program) Write code that opens "name.txt"
# and reads the name (as above) then prints, "Your name is Bob" (or whatever the name is in the file).

# with open("name.txt", "r") as in_file:
#     try:
#         name = in_file.read(100)
#     except ValueError:
#         print("Invalid contents on name.txt")
#     except FileNotFoundError:
#         print("name.txt not found")
#     else:
#         in_file.close()
# print(f"Your name is: {name}")

# 3. Create a text file called numbers.txt and save it in your prac directory.
# Put the following three numbers on separate lines in the file and save it:
# 17
# 42
# 400
# Write code that opens "numbers.txt", reads only the first two numbers and adds them together then prints the result,
# which should be... 59.

# with open("numbers.txt", "r") as in_file:
#     try:
#         lines = in_file.readlines(100)
#         first_number = int(lines[0].strip())
#         second_number = int(lines[1].strip())
#         total = first_number + second_number
#     except ValueError:
#         print("Invalid contents on name.txt")
#     except FileNotFoundError:
#         print("name.txt not found")
#     else:
#         in_file.close()
# print(f"The total is: {total}")

# 4. Now write a fourth block of code that prints the total for all lines in numbers.txt or a file
# with any number of numbers.

with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        new_number = int(line.strip())
        total = total + new_number
    print(total)
