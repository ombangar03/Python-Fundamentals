text = "programming"

# find the second non-repeating character


count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)

counter = 0

for char in text:
    if count[char] == 1:
        counter += 1

        if counter == 2:
            print(char)
            break

else:
    print("Second non-repeating character not found.")
    
