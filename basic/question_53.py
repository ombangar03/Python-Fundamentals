# Reverse the words in a sentence

text = "Python is easy to learn"

# Your task: Reverse the order of words, not the characters inside each word.

t1 = text.split()

t1.reverse()

result = " ".join(t1)
print(result)


"""t1.reverse()       # Modifies original list, returns None
t1[::-1]           # Creates a reversed list
" ".join(t1)       # Creates a string"""