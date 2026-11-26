def group_employees(employees):

    group_of_department = {}

    for emp in employees:
        # print(emp["name"], emp["department"])
        if emp["department"] not in group_of_department:
            group_of_department[emp["department"]] = [emp["name"]]
        else:
            group_of_department[emp["department"]].append(emp["name"])
        
    return group_of_department
            
    
employees = [
    {"name": "Om", "department": "IT"},
    {"name": "Rahul", "department": "HR"},
    {"name": "Priya", "department": "IT"},
    {"name": "Amit", "department": "Finance"},
    {"name": "Sneha", "department": "HR"}
]


print(group_employees(employees))


