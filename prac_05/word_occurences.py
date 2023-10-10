"""
Word Occurrences
Estimate: 30 minutes
Actual:
"""

text = str(input("Text: "))
words = text.split(' ')

word_to_count = {word: words.count(word) for word in words}

print(text)
print(words)
print(word_to_count)

# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     try:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     except KeyError:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()
