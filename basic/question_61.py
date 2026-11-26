#Find the first non-repeating character.

text = "aabbcddex"
# text = "aabbcc"

count = {}

for char in text:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)


for char in text:
    if count[char] == 1:
        print(char)
        break

else:
    print("No non-repeating character found.")