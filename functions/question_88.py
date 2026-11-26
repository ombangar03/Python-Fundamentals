# Next challenge: Filter using **kwargs
# Write a function called employee_details(**kwargs).

# Requirements:
# 1. Accept multiple employee details.
# 2. Print only the values whose key is "name" or "department".
# 3. Ignore all other keys.



def employee_details(**kwargs):
    for key, value in kwargs.items():
        if key == "name" or key == "department":
            print(key ,":", value)


employee_details(
    name="Om",
    age=24,
    department="IT",
    salary=45000,
    city="Mumbai"
)
