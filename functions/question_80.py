"""Write a function called is_even() that:
1. Accepts one number as an argument.
2. Returns "Even" if the number is even.
3. Returns "Odd" otherwise.
Test it with is_even(7)."""


def is_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

number = is_even(7)
print(number)