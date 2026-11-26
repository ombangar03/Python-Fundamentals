# Count words with more than 5 characters

words = ["python", "AI", "programming", "java", "developer", "SQL"]

Total_words = 0

for word in words:
    if len(word) > 5:
        Total_words += 1

print("Total_words: ",Total_words)