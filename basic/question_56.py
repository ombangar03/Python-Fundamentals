# find the longest word

words = ["python", "programming", "java", "developer", "machinelearning"]

# Task: Find the longest word in the list.

longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print(longest_word)        




words = ["apple", "mango", "grape", "banana"]

longest_word = ""

for word in words:
    if len(word) >= len(longest_word):
        longest_word = word

print(longest_word)


"""Important difference
- > keeps the first word when multiple words have the same maximum length.
- >= keeps the last word when multiple words have the same maximum length."""