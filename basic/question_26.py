numbers = [12, 45, 7, 89, 23, 56]

min_num = numbers[0]

for num in numbers:
    if min_num > num:
        min_num = num
print(min_num)