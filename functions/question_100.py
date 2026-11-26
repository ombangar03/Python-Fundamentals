# Your task: Write department_salary(employees).

# Hint:
# - Create an empty dictionary.
# - Iterate through employees.
# - If the department exists, add the salary.
# - Otherwise, initialize the department with that salary.



def department_salary(employees):

    total_department_salary = {}

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        if department in total_department_salary:
            total_department_salary[department] += salary
        else:
            total_department_salary[department] = salary

    
        # if employee["department"] in total_department_salary: 
        #     total_department_salary[employee["department"]] +=  [employee["salary"]]
        #     total_department_salary[employee["department"]] = sum(total_department_salary[employee["department"]])
            
        # else:
        #     total_department_salary[employee["department"]] = [employee["salary"]]

    return total_department_salary

employees = [
    {"name": "Om", "department": "IT", "salary": 25000},
    {"name": "Rahul", "department": "HR", "salary": 35000},
    {"name": "Priya", "department": "IT", "salary": 45000},
    {"name": "Amit", "department": "Finance", "salary": 30000},
    {"name": "Sneha", "department": "HR", "salary": 40000}
]

print(department_salary(employees))

# Let's remember:
# Operator	Meaning
# =	Assign or replace
# +=	Add to existing value
# .append()	Add an element to a list