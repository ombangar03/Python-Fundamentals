# Count vowels and consonants

text = "programming"

# vowels = ("a", "e", "i", "o", "u")
vowels = "aeiou"
vowels_count = 0
consonent = 0

for char in text:
    if char in vowels:
        # print("vowels:", char)
        vowels_count += 1
        # vowels_count.append(char)
    else:
        consonent += 1
        
print("Vowels_count: ",vowels_count)
print("consonent: ",consonent)

    
        
