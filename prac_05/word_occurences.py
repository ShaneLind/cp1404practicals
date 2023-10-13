"""
Word Occurrences
Estimate: 30 minutes
Actual: 40 minutes
"""

text = str(input("Text: "))
words = text.split(' ')
word_to_count = {word: words.count(word) for word in words}

keys = list(word_to_count.keys())
keys.sort()
key_to_count = {key: words.count(key) for key in keys}
max_length = max(len(key) for key in keys)

for key, count in key_to_count.items():
    print(f"{key:{max_length + 1}}: {count:1}")
