# Group words by their length

def group_by_length(words):
    
    len_of_words = {}

    for word in words:
        length = len(word)
        if length in len_of_words:
            len_of_words[length].append(word)
        else:
           len_of_words[length] = [word]

    return len_of_words

    # for key, value in len_of_words.items():

    



words = ["apple", "bat", "banana", "cat", "mango", "dog"]
print(group_by_length(words))