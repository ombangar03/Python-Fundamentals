employees = {
    "Om": {"salary": 25000, "department": "IT"},
    "Rahul": {"salary": 35000, "department": "HR"},
    "Priya": {"salary": 45000, "department": "IT"},
    "Amit": {"salary": 30000, "department": "Finance"},
    "Sneha": {"salary": 50000, "department": "IT"}
}

# Create a new dictionary containing only employees from the IT department.

it_employess = {}
 
for key, value in employees.items():
    if value["department"] == "IT" and value["salary"] > 30000:
            it_employess[key] = value
        # print(key, value)

print(it_employess)


max_salary = 0

for key, value in employees.items():
    if value["salary"] > max_salary:
        max_salary = value["salary"]

print(max_salary)


highest_salary = {}

for key, value in employees.items():
    if max_salary == value["salary"]:
        highest_salary[key] = value

print(highest_salary)