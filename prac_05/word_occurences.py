"""
Word Occurrences
Estimate: 30 minutes
Actual: 40 minutes
"""

# get user input and creat dictionary
text = str(input("Text: "))
words = text.split(' ')
word_to_count = {word: words.count(word) for word in words}
# print(word_to_count)

# sort dictionary
keys = list(word_to_count.keys())
keys.sort()
key_to_count = {key: words.count(key) for key in keys}
max_length = max(len(key) for key in keys)

# print sorted dictionary
for key, count in key_to_count.items():
    print(f"{key:{max_length + 1}}: {count:1}")
