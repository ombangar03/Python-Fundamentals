employees = {
    "Om": 25000,
    "Rahul": 35000,
    "Priya": 45000,
    "Amit": 30000,
    "Sneha": 50000
}

# Your task: Create a new dictionary containing only employees whose salary is greater than ₹30,000.

salary = {}

for key, value in employees.items():
    if value > 30000:
        salary[key] = value
        # print(key, ":" ,salary[key])

print(salary)



# Task: Create a new dictionary containing employees whose salary is between ₹30,000 and ₹45,000, including both boundaries.
salaries = {}
for key, value in employees.items():
    if value >= 30000 and value <= 45000:
        salaries[key] = value
        # print(key, value)

print(salaries)