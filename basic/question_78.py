employees = {
    "Om": {"salary": 25000, "department": "IT"},
    "Rahul": {"salary": 35000, "department": "HR"},
    "Priya": {"salary": 45000, "department": "IT"},
    "Amit": {"salary": 30000, "department": "Finance"},
    "Sneha": {"salary": 50000, "department": "IT"},
    "Raj": {"salary": 40000, "department": "HR"}
}

# Find the average salary of each department.
department_salary = {}
department_count = {}

for key, value in employees.items():
    salary = value["salary"]
    department = value["department"]

    if department in department_salary:
        department_salary[department] += salary
        department_count[department] += 1

    else:
        department_salary[department] = salary
        department_count[department] = 1

print(department_salary)
print(department_count)

department_average = {}

for key, value in department_salary.items():
    department_average[key] = department_salary[key] / department_count[key]

print(department_average)

# find highest_avg_salary

highest_avg_salary = 0

for key, value in department_average.items():
    if value > highest_avg_salary:
        highest_avg_salary = value

print(highest_avg_salary)

for key, value in department_average.items():
    if value == highest_avg_salary:
        print(key, value)


#Find all employees whose salary is greater than the average salary of their respective department.
above_average_employees = {}

for department, avg_salary in department_average.items():
    for employee_name, employee_details in employees.items():
        if employee_details["department"] == department and employee_details["salary"] > avg_salary:
            above_average_employees[employee_name] = employee_details

print(above_average_employees)


"""You're checking two things:
1. Does the employee belong to the current department?
2. Is their salary greater than that department's average?"""



