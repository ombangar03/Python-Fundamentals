# Exercise 1.
# Department-wise employee count

def department_count(employees):

    employee_count = {}

    for emp in employees:
        department = emp["department"]

        if department in employee_count:
            employee_count[department] += 1
        
        else:
            employee_count[department] = 1

    return employee_count

employees = [
    {"name": "Om", "department": "IT"},
    {"name": "Rahul", "department": "HR"},
    {"name": "Priya", "department": "IT"},
    {"name": "Amit", "department": "Finance"},
    {"name": "Sneha", "department": "HR"},
    {"name": "Raj", "department": "IT"}
]


result = department_count(employees)
print(result)