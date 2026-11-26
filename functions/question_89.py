# Challenge 2: Find the most frequent character
# Write a function most_frequent(s) that:
# 1. Accepts a string.
# 2. Counts character frequencies.
# 3. Finds the character with the highest frequency.
# 4. Returns that character and its count.

def most_frequent(s):
    count = {}
    for char in s:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    max_count = 0
    max_char = ""

    for key, value in count.items():
        if value >= max_count:
            max_count = value
            max_char = key

    return max_char, max_count
                    
print(most_frequent("programming"))

        
# Remember the difference:
# - > → Keeps the first character when there's a tie.
# - >= → Replaces it with the later character when there's a tie.

