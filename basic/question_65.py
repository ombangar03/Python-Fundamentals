# Find the first repeating character.

text ="abacbd"

seen = set()

for char in text:
    if char in seen:
        print(char)
        break
    else:
        seen.add(char)


"""A set is sufficient because we only need to check whether a character has appeared previously. 
We don't need to store its frequency.
 Sets provide efficient membership checks."""