list_cube_odd_number = []
odd_number = 1
sum_div_7 = 0
for i in range(500):
    list_cube_odd_number.append(odd_number ** 3)
    odd_number += 2
for j in list_cube_odd_number:
    sum_numeric_number = 0
    x = j
    while j > 0:
        sum_numeric_number += j % 10
        j //= 10
    if sum_numeric_number % 7 == 0:
        sum_div_7 += x
print(sum_div_7)
for k in range(len(list_cube_odd_number)):
    list_cube_odd_number[k] += 17
for j in list_cube_odd_number:
    sum_numeric_number = 0
    x = j
    while j > 0:
        sum_numeric_number += j % 10
        j //= 10
    if sum_numeric_number % 7 == 0:
        sum_div_7 += x
print(sum_div_7)