# Next: **kwargs
# Just as *args collects multiple positional arguments, 
# **kwargs collects multiple keyword arguments.


def student_details(**kwargs):
    print(kwargs)

student_details(name="Om", age=24, city="Mumbai")



def display(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display(name="Om", role="Python Developer", experience=1)