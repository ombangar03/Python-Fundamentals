# Next: *args — Multiple positional arguments
# Sometimes you don't know how many arguments will be passed to a function. 
# Python provides *args for this.

def add_numbers(*args):
    print(args)

add_numbers(10, 20, 30, 40)

"""Important:
- *args collects multiple positional arguments.
- It stores them as a tuple.
- You can loop through them."""

