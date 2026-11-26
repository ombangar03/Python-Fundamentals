# 

# find the shortest word


words = ["python", "programming", "java", "developer", "AI"]

shortest_word = words[0]

for word in words:
    if len(word) < len(shortest_word):
        shortest_word = word
    
print(shortest_word)