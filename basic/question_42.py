text = "  Python Programming  "

result = text.strip().upper()

print(result)
print(len(result))
print(len(text))


"""
strip() removes whitespace from the beginning and end.
upper() converts all letters to uppercase.
len(result) counts 18 characters after removing the four surrounding spaces.
len(text) counts all 22 characters, including those four spaces.
"""