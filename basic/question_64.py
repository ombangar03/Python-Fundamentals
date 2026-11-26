# first repeating character 
text = "programming"



count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)



seen = set()

for char in seen:
    if count[char] > 1:
        print(char)
        break
    else:
        seen.add(char)

# Important: When the character is already in seen, we print it and stop. We do not add it again.


text = "swiss"

seen = set()

for char in text:
    if char in seen:
        print(char)
        break
    else:
        seen.add(char)
