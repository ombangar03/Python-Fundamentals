employees = {
    "Om": {"salary": 25000, "department": "IT"},
    "Rahul": {"salary": 35000, "department": "HR"},
    "Priya": {"salary": 45000, "department": "IT"},
    "Amit": {"salary": 30000, "department": "Finance"},
    "Sneha": {"salary": 50000, "department": "IT"},
    "Raj": {"salary": 40000, "department": "HR"}
}

# Your task
# Create a dictionary called department_employees and group employee names according to their departments.

count = {}

for name, value in employees.items():
    if value["department"] in count:
        count[value["department"]] += 1
    else:
        count[value["department"]] = 1

print(count)


department_employees = {}

for name, details in employees.items():
    department = details["department"]
    if department in department_employees:
        department_employees[department].append(name)

    else:
        department_employees[department] = [name]

print(department_employees)


    