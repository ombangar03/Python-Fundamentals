text = "Hello World"

print(text.startswith("Hello"))
print(text.endswith("World"))
print(text.isalpha())
print(text.isdigit())
print("12345".isdigit())

"""
Method	                  Purpose
startswith() Checks whether a string starts with given text
endswith()	Checks whether a string ends with given text
isalpha()	Checks whether all characters are alphabetic
isdigit()	Checks whether all characters are digits


Remember:
- "Hello" → isalpha() returns True.
- "Hello World" → isalpha() returns False because of the space.
- "12345" → isdigit() returns True.
- "12345abc" → isdigit() returns False.
"""
