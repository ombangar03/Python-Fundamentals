# Department-wise average salary

def average_department_salary(employees):

    avg_dept_salary = {}

    total_salary = {}
    count = {}

    

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        if department in total_salary:
            total_salary[department] += salary
            count[department] += 1
        else:
            total_salary[department] = salary
            count[department] = 1

    for department in total_salary:
        avg_dept_salary[department] = total_salary[department] / count[department]

    # Check whether an employee's salary is greater than their department's average.
    employee_salary = []
    for employee in employees:
        salary = employee["salary"]
        department = employee["department"]

        average_department_salary = avg_dept_salary[department]

        if salary > average_department_salary:
            employee_salary.append(employee["name"])

     
    return employee_salary



employees = [
    {"name": "Om", "department": "IT", "salary": 25000},
    {"name": "Rahul", "department": "HR", "salary": 35000},
    {"name": "Priya", "department": "IT", "salary": 45000},
    {"name": "Amit", "department": "Finance", "salary": 30000},
    {"name": "Sneha", "department": "HR", "salary": 40000}
]

result = average_department_salary(employees)
print(result)