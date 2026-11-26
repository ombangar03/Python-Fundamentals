# functions: 

# print() vs return
# print()	                                                                return
# Displays output on the screen.	                                        Sends a value back from a function.
# Doesn't make the value available to the caller by itself.	                Allows the caller to store and reuse the value.
# Doesn't terminate a function.                                             Ends the function's execution.



def check(num):
    if num > 10:
        return "Greater"
    else:
        return "Smaller"

result = check(5)
print(result)


def greet(name):     # parameter
    return "Hello" + " " + name

result = greet("om") #argument

print(result)