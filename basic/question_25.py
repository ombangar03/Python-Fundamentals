numbers = [12, 45, 7, 89, 23, 56]

# Find the largest number without using max().

max_num = numbers[0]

for num in numbers:
    if max_num <= num:
        max_num = num
print(max_num)