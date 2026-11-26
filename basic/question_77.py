department_count = {
    "IT": 3,
    "HR": 3,
    "Finance": 1,
    "Sales": 1
}

# Challenge: Find the second-highest distinct employee count and all departments having that count.

maximum_count = 0

for count in department_count.values():
    if maximum_count < count:
        maximum_count = count

print(maximum_count)


second_highest_salary = 0

for key, value in department_count.items():
    if value < maximum_count:
        if value > second_highest_salary:
            second_highest_salary = value

print(second_highest_salary)

department_name = []
for key, value in department_count.items():
    if value == second_highest_salary:
        department_name.append(key)

print(department_name)