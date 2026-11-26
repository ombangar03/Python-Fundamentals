
employees = {
    "Om": {"salary": 25000, "department": "IT"},
    "Rahul": {"salary": 35000, "department": "HR"},
    "Priya": {"salary": 45000, "department": "IT"},
    "Amit": {"salary": 30000, "department": "Finance"},
    "Sneha": {"salary": 50000, "department": "IT"}
}

# Next challenge: Find the second-highest salary in a nested dictionary.

"""Your task:
1. Find the highest salary.
2. Find the second-highest distinct salary.
3. Store all employees earning that second-highest salary.
"""
highest_salary = 0

for key, value in employees.items():
    if value["salary"] > highest_salary:
        highest_salary = value["salary"]

print(highest_salary)

second_highest_salary = 0
for key, value in employees.items():
    if  value["salary"] < highest_salary:
        if value["salary"] > second_highest_salary:
            second_highest_salary = value["salary"]

print(second_highest_salary)

result = {}
for key, value in employees.items():
    if value["salary"] == second_highest_salary:
        result[key] = value

print(result)


