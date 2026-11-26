# Next challenge: Find the maximum using *args
# Write a function

def find_max(*args):
    if not args:
        return None
    
    largest = args[0]

    for num in args:
        if num > largest:
            largest = num
    
    return largest

print(find_max(10, 45, 23, 89, 12))
print(find_max())  # indexerror: tuple index out of range. 
