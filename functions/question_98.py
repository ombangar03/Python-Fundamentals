def group_by_length(words):
    len_of_words = {}

    for word in words:
        length = len(word)

        if length in len_of_words:
            len_of_words[length].append(word)
        else:
            len_of_words[length] = [word]

    return len_of_words


words = ["cat", "dog", "apple"]
print(group_by_length(words))



#exercise:
employee = {
    "IT": ["Om", "Rahul"],
    "HR": ["Priya"]
}

new_employees = [
    ("Amit", "IT"),
    ("Sneha", "Finance"),
    ("Raj", "HR"),
    ("Karan", "Finance")
]

for name, department in new_employees:

    if department in employee:
        employee[department].append(name)
    else:
        employee[department] = [name]

print(employee)


