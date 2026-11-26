marks = {}

"""
Your task:
1. Predict the output.
2. Tell me how many times the loop executes.
3. Why do we use student as the dictionary key?
"""
students = ["Om", "Rahul", "Om", "Priya", "Rahul", "Om"]

for student in students:
    if student not in marks:
        marks[student] = 1
    else:
        marks[student] += 1
print(marks)