text = "Python is easy. Python is powerful. Python is popular."

"""Task: Write a Python program to:
1. Convert the entire string to lowercase.
2. Count how many times "python" appears.
3. Replace every occurrence of "python" with "Java".
4. Print the original string and the modified string separately."""

new_text = text.lower()
# print(new_text)

count = new_text.count("python")
print(count)
modified_text = new_text.replace("python", "Java")
print(modified_text)

print(text)
# print(new_text)