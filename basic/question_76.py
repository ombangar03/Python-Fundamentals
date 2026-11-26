
employees = {
    "Om": {"salary": 25000, "department": "IT"},
    "Rahul": {"salary": 35000, "department": "HR"},
    "Priya": {"salary": 45000, "department": "IT"},
    "Amit": {"salary": 30000, "department": "Finance"},
    "Sneha": {"salary": 50000, "department": "IT"},
    "Raj": {"salary": 40000, "department": "HR"}
}


#Challenge: Find the highest-paid employee in each department.
department_count = {}

for key, value in employees.items():
    if value["department"] in department_count:
        department_count[value["department"]] += 1
    else:
        department_count[value["department"]] = 1

print(department_count)

max_count = 0

for department , count in department_count.items():
    if count > max_count:
        max_count = count
    
print(max_count)


for dept, value in department_count.items():
    if value == max_count:
        print(dept)

min_count = float("inf")
# Find the department with the minimum employees
for dept, value in department_count.items():
    if value < min_count:
        min_count = value

print(min_count)

min_dept_employee = {}
for dept, value in department_count.items():
    if department_count[dept] == min_count:
        min_dept_employee[dept] = value

print(min_dept_employee)



departmnt_count = {
    "IT": 3,
    "HR": 3,
    "Finance": 1,
    "Sales": 1
}
maximum_count = 0
for depart, count in departmnt_count.items():
    if count > maximum_count:
        maximum_count = count
print(maximum_count)

dept_name = []
for deptname, count in departmnt_count.items():
    if count == maximum_count:
        dept_name.append(deptname)

print(dept_name)

