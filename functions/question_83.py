# Next concept: Positional Arguments vs Keyword Arguments
# 1. Positional arguments

# Values are assigned based on their position.

def student(name, age):
    print(name, age)

student("Om", 24)



def employee(name, salary, department):
    print(name, salary, department)

employee("Om", department="IT", salary=45000)

#om: positional argument (name)
#salary = 45000 -> keyword argument (salary)
#department = "IT" -> keyword argument (department)

def employee(name, salary, department):
    print(name, salary, department)

employee("Om", 45000, "IT")    # syntax error.

