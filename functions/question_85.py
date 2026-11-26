def calculate(*args):
    total = 0

    for num in args:
        total += num

    return total

print(calculate(10, 20, 30))
print(calculate(5,5,5,5))


