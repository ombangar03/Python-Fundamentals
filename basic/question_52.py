# Count words in a sentence

text = "Python is easy to learn"

# Task: Count the total number of words in the sentence.

t = text.split()
print(t)
print("Total words:", len(t))

#The split() method separates a string into a list of words.


text = "Python   is    easy"

words = text.split()

print(words)
print(len(words))
print(text.split(" "))
print(len(text.split(" ")))

"""1. split()
- Splits on whitespace.
- Treats consecutive spaces as one separator.
- Ignores leading and trailing whitespace.

2. split(" ")
- Splits on each individual space character.
- Consecutive spaces create empty strings ('') between them.
"""

