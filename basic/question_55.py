# Count words starting with a particular letter

words = ["python", "java", "programming", "javascript", "pandas", "php"]

# task: Count how many words start with the letter "p".

count = 0

for word in words:
    if word.startswith("p"):
        count += 1

print("Words starting with p:", count)